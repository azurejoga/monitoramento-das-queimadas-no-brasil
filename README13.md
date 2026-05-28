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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63b5fe2a-ce5e-3d6a-963c-5c46a8182138 | -13.20585 | -54.51419 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98d25832-b3fb-3ba6-9d8b-2348a05326dc | -12.72375 | -54.20147 | 2026-05-28 05:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87216207-c0ea-391a-b05c-a53e26c46c26 | -17.93566 | -51.34309 | 2026-05-28 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6307d55a-8099-36eb-af6f-10de54b352d5 | -13.22338 | -54.49527 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a57b2472-254c-3775-9cac-37494163f9cf | -13.22151 | -54.50793 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 075bcf84-bb93-3e29-966e-d390dc4d414d | -13.22699 | -54.49581 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04c29b0c-c361-3dd0-a6a8-c30e5fc2a56f | -13.21966 | -54.5205 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c7dd247-db3e-3eb8-bdeb-1107d2df5caf | -11.79441 | -57.01606 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f02e5568-81e4-307a-9a8c-b5ab9e2b24d2 | -13.20286 | -54.50943 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cce976a9-d80c-34b7-b264-82a9ddd67e21 | -11.72515 | -56.83478 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 244618cc-6cea-33a5-8387-3ff42aed6c1a | -13.22389 | -54.51683 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd5b6a59-5aaf-3dce-b8ed-ed1fd3840351 | -13.19803 | -54.51726 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71d80ae6-b373-32c4-a55c-b3d2289fa3f9 | -17.93279 | -51.32774 | 2026-05-28 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e476639b-9447-3b15-95c3-4d10730d4fc5 | -11.78951 | -57.01193 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a253da85-6e2c-3518-bbcd-e7d2b57578cb | -13.20946 | -54.51472 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d667c2a3-acda-3dd6-8658-89c37a356b49 | -11.79496 | -57.01253 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 350669df-dcd5-3c1e-8f78-d75108bf2754 | -16.15944 | -58.47333 | 2026-05-28 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 52520ab0-9d9e-3477-8e17-03d850954173 | -16.16945 | -58.47504 | 2026-05-28 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| fa6b19a3-15e6-37a1-aec6-9d578b80ad81 | -17.93219 | -51.3327 | 2026-05-28 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b00fff6b-0dc0-382e-83d5-fe17d75358db | -13.20163 | -54.51782 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 244ed416-5e76-377d-9cdb-d9f2de8948ca | -11.72348 | -56.84539 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c03488a-d4e7-3e0e-a573-72793aaa2578 | -17.92752 | -51.33212 | 2026-05-28 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fe2ec1d-3d7a-3317-81e0-dde5fad48703 | -13.94916 | -53.8691 | 2026-05-28 05:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76cf0a95-4522-3825-813b-314282de7f1b | -11.79284 | -57.01247 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17091467-b00f-30d3-aa6a-1f4dccb10a16 | -13.21069 | -54.50632 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66c42aec-c74d-3a37-9513-690a6a9ab2cf | -16.16611 | -58.47447 | 2026-05-28 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 464163e2-9a5b-3fc6-976f-7e26dda52fc4 | -13.18203 | -52.70713 | 2026-05-28 05:16:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c21e9c6-107a-3852-9823-0b04deb696e3 | -13.21492 | -54.50264 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2b2a0c3-a61d-335a-bb8e-af05767856d0 | -13.22028 | -54.51632 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d820bc9-af4b-32bc-b0ae-acc201042060 | -17.92812 | -51.32718 | 2026-05-28 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6165b311-a8b0-38b5-8b6c-a93c06730e19 | -11.80573 | -57.35465 | 2026-05-28 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b36ce2f-5b80-3c57-b6d1-ed1c614e3ffb | -11.81295 | -57.35221 | 2026-05-28 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf518252-ae3d-32f1-b85b-d63f043000a6 | -13.21729 | -54.5116 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6adc695-c763-33ad-a8b6-5ccd8b2421ce | -13.65783 | -55.29673 | 2026-05-28 05:16:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7c06729-19c2-3c27-94bc-f7dd1a79520c | -13.21245 | -54.51944 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57207b0c-bdc0-39e2-917a-6aef08eb6659 | -13.22513 | -54.50845 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 474c6cda-1726-3fa4-9d01-7ed90cecce8c | -13.21007 | -54.51053 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fead7b25-49f0-34d3-aa09-6ec5389b2d2a | -17.95167 | -54.46565 | 2026-05-28 05:16:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f207075e-9d3d-39ac-9c29-89cbe40d1ad3 | -13.20884 | -54.51891 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5952bd7-9f84-3fe7-b34d-175d80579f95 | -13.22451 | -54.51265 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5505fd2a-8608-3d98-bbbb-e5fadad2b350 | -13.21306 | -54.51526 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51dfacaa-659f-3279-9b44-0a628f229c41 | -12.72438 | -54.19722 | 2026-05-28 05:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59bc9ce6-9d31-39ca-805a-37e68209199f | -11.63337 | -56.85937 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f3399c0f-d29e-3bb9-b5c5-1c942e7d43b5 | -13.21131 | -54.50209 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7e8bfd7-087e-33ea-88eb-37bae904c1ec | -11.72126 | -56.83778 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 175d0e0f-a2ff-3d0a-9755-dfc4ad2b72b2 | -16.2345 | -59.98572 | 2026-05-28 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b7d394c-370a-3bba-b7d7-7bbd3b62561f | -16.16221 | -58.47746 | 2026-05-28 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4cdc6eb9-171d-3ea6-87bc-32c30ab72075 | -11.80906 | -57.35519 | 2026-05-28 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bf69a4f-6379-3f67-afde-66ad71c33751 | -11.72848 | -56.83532 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3436531b-4acd-3f1b-9252-19143ddb5805 | -11.54741 | -56.93629 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 876712ab-453f-377c-a7e6-fb7a3eb4e1e1 | -14.01688 | -53.36314 | 2026-05-28 05:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3170cd6d-b76d-3b35-8b2f-a94975f1ac5a | -13.65083 | -55.29565 | 2026-05-28 05:16:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42507284-d9e7-3222-ad04-081c53dd2d2d | -16.21738 | -59.66545 | 2026-05-28 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fe94ad0-693a-347e-ad2b-422a4e5d3a3f | -13.65433 | -55.29619 | 2026-05-28 05:16:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d289abad-cd13-3dba-9b6f-0eaba33aa3eb | -11.63908 | -58.2432 | 2026-05-28 05:16:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 142784a9-4c56-3c4a-a77a-91aa2ba6bde1 | -13.21368 | -54.51107 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 926ea6cd-390f-3d92-bb52-cdae33446958 | -11.7934 | -57.00895 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12ebf50a-fa8b-3486-a0fd-f4bba3ad6639 | -21.54438 | -47.04502 | 2026-05-28 05:18:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 912ebd4c-64af-35ef-b477-fe6975b4a102 | -20.73557 | -56.13559 | 2026-05-28 05:18:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3324bf93-1b37-3ee4-981a-6ccee972b821 | -21.30071 | -48.58807 | 2026-05-28 05:18:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 665fb885-b89f-3588-bc0c-edcdc5ded35f | -21.42434 | -47.07155 | 2026-05-28 05:18:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d7cd209-a4dc-3fc2-8f75-7888fea9f2f4 | -21.30113 | -48.58362 | 2026-05-28 05:18:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 294eaa74-5ac2-3f61-8646-5ff9f2e58d5c | -21.42385 | -47.07731 | 2026-05-28 05:18:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95e65a6e-1c60-36c0-b1d8-a7b1a7a6673a | -21.54658 | -48.897 | 2026-05-28 05:18:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4efee9b3-9084-3b0b-8f40-4693252d9d44 | -20.14246 | -56.34249 | 2026-05-28 05:18:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9a22512-7bd1-321d-a4a9-7efc447a26db | -19.00175 | -57.62477 | 2026-05-28 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| efd001ba-e055-3139-b178-7f4fe444f3d4 | -21.98396 | -57.60381 | 2026-05-28 05:18:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3b3e694-c742-3112-ada8-35a7fcf84b47 | -21.9805 | -57.60329 | 2026-05-28 05:18:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9808c333-343a-3da4-aac3-65b9086101df | -22.05647 | -56.18534 | 2026-05-28 05:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dd3c3f4-48e7-3d24-ada8-dd5da85d439f | -9.14569 | -51.28294 | 2026-05-28 05:31:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bb2b531-a269-3d03-bad4-97085cac7502 | -6.52791 | -55.06282 | 2026-05-28 05:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14d5af05-866b-3c42-9257-b315b1b5e6bb | -8.34022 | -51.92508 | 2026-05-28 05:31:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a922666f-dd41-36df-a667-eae8b259b238 | -5.20473 | -56.04662 | 2026-05-28 05:31:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c7bfd68-d231-3b3d-991a-c2977f41cde6 | -9.14019 | -51.28533 | 2026-05-28 05:31:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92d0b07c-9eb4-3a08-9bae-39c285147953 | -7.86344 | -61.49201 | 2026-05-28 05:31:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d641dcf6-d43b-3fec-95bc-5276e85e3105 | -9.14638 | -51.28607 | 2026-05-28 05:31:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3e2f8e8-d720-37a3-bc2e-8c3ef2b1e005 | -6.53255 | -55.06347 | 2026-05-28 05:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6809225e-d6b0-35e1-8948-4529cd3273fa | -7.86399 | -61.48848 | 2026-05-28 05:31:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0e537c5-f52f-3327-a26e-48742617020a | -9.147 | -51.28136 | 2026-05-28 05:31:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fceb5d0-923c-37f9-8738-960b15a78391 | -8.33595 | -51.92046 | 2026-05-28 05:31:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e905377-7677-3400-8f45-9fde57e4bb94 | -9.1451 | -51.28767 | 2026-05-28 05:31:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5852c724-bdbd-3aae-aac6-e6fd3d8f5ab8 | -8.34081 | -51.92056 | 2026-05-28 05:31:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c42142de-40e1-30fc-8dce-268fccb8f5b4 | -9.14761 | -51.27665 | 2026-05-28 05:31:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8bf409b-8f74-3bdd-9a77-3603659c9768 | -9.14627 | -51.27823 | 2026-05-28 05:31:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 302cb043-7d4f-3229-b47d-376e32d7ed37 | -11.03808 | -56.92539 | 2026-05-28 05:33:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69b056b8-5ded-38f0-940b-e6e7e646e734 | -14.01736 | -53.36406 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e80d81b-3386-3c21-bc7f-70407aed32b2 | -11.47379 | -52.92292 | 2026-05-28 05:33:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c06c7851-1197-346b-880b-f496f24545b4 | -12.05113 | -57.41799 | 2026-05-28 05:33:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e478a47-3bfc-3a36-ba63-b2abcbcc0d48 | -13.21832 | -54.51137 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfe26209-a101-3345-ba0b-4f55263ab61a | -13.20309 | -54.51289 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a8cd020-0345-380d-9eb0-dbda1e5b64cc | -13.22068 | -54.50139 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9b01d9c-685f-33cc-bbdf-3bb965b0483b | -13.21871 | -54.50803 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 982901df-481e-3ab7-a52e-aa172532da29 | -11.29964 | -54.03513 | 2026-05-28 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1237c6f9-2bb7-3f0d-b7e1-4807b77cf9c0 | -13.20435 | -54.50283 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c062d769-4094-30cf-8620-abbaa447d218 | -11.93193 | -57.04253 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 132fa3a8-0a77-3603-8172-4e544aaf65ef | -13.22431 | -54.51526 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96576bc6-ed86-3ce1-98c3-11cdfbe77062 | -11.79304 | -57.0116 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e6d47e4-563d-3a13-83aa-ba1421e52d66 | -11.45656 | -52.92073 | 2026-05-28 05:33:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b171000a-782d-3a46-883b-410cae9cda22 | -13.22402 | -54.5086 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eeee8055-7b46-34d8-8f65-6ed098e20326 | -10.14025 | -52.39777 | 2026-05-28 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README14.md)
