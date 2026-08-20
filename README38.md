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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ca8f51b-c2b2-3f23-b183-3684fade90f0 | -15.44987 | -48.58609 | 2026-08-20 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dec505a-b96f-3beb-9b21-6c80e98744c2 | -17.93719 | -44.40528 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1a95050-0ee8-3312-be05-f958b09d4e71 | -18.84352 | -47.14229 | 2026-08-20 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0972ebe0-aaf6-3d8d-8eaa-643fa3820c43 | -14.34391 | -51.90218 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 063043fc-f09d-3c0b-91a1-ad81d1ae7b83 | -18.03759 | -44.62125 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| baac2e23-934d-3002-bac4-5a74b373516a | -14.01435 | -53.67568 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfaaa950-d518-3bb6-94cd-7b3730093a87 | -15.54239 | -50.27806 | 2026-08-20 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53bdea78-d1c2-3a91-869b-cce24aedc293 | -15.18181 | -48.76767 | 2026-08-20 04:21:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11350d32-8050-336f-9a4f-85785d4f7d50 | -15.4905 | -48.43595 | 2026-08-20 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec0d5262-f966-35f9-87ac-492145f4b2f0 | -16.61107 | -43.37349 | 2026-08-20 04:21:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b740854c-3e60-3a91-bcfc-945e1d4e3868 | -12.80117 | -48.42616 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8058ca2-ec3c-3c45-b11e-31df5ce098e4 | -14.31668 | -51.94915 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 960e82ac-410c-3fb6-814c-49effb2bdd3d | -14.45348 | -45.62505 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d3d81344-c307-3f8c-b9ec-9cf78a466d42 | -14.27707 | -51.88918 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5adb03c6-d50e-3555-acd5-204685e54275 | -13.94013 | -53.8684 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a247b1b6-3987-3158-a8ad-7148e73c6d24 | -13.39999 | -54.38216 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce2c4fa1-c584-39ea-9737-ba3770e8f702 | -12.48332 | -54.72458 | 2026-08-20 04:21:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb2bdd5f-bf5b-35b2-9b8b-6dfec9b4e9a6 | -13.47712 | -51.44245 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5cd90cac-b06c-3809-82bd-b49ac7728f5f | -17.9299 | -44.43093 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78f38b81-f957-3536-b3c2-c1ff95fdcfcc | -11.23844 | -54.8302 | 2026-08-20 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43e06ef1-1323-3577-acbe-f0945af577ee | -17.92653 | -44.43037 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78f2be01-be6c-30e6-a66c-0102c4e9ab9e | -18.88327 | -41.09242 | 2026-08-20 04:21:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0acccf86-7074-3b32-be3b-adfd1bb73fc0 | -11.18353 | -54.03053 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fcce860-666c-3be2-ac4f-e84606a2c68d | -14.01373 | -53.67891 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b9ac5bf-8a9f-3638-a21d-3c0483ebde06 | -16.07564 | -54.97171 | 2026-08-20 04:21:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 339db97e-98b7-3045-bd37-b49e75e08cde | -13.94586 | -53.86622 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a610440-abe5-316c-b5e3-ab2284ca42ef | -11.81221 | -56.60026 | 2026-08-20 04:21:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b6a9aea-7b8a-3961-8438-71b5c6ba5cc1 | -15.44914 | -48.59032 | 2026-08-20 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68d0bdfd-4756-3266-a931-f3c747da5a93 | -11.83498 | -58.84689 | 2026-08-20 04:21:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2df9c3b3-07a2-358f-a442-f083d256843a | -14.97539 | -46.59252 | 2026-08-20 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7d81833-ad74-3638-8ff5-e5fd61461cd0 | -11.18829 | -54.00584 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d83c709-f836-3587-b6d2-10e913c78206 | -11.20045 | -54.00099 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82e9f975-d326-31d1-aa97-97bbe24b5750 | -19.67209 | -42.1069 | 2026-08-20 04:21:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ffaf4bf9-1815-38de-9b70-2071937803c4 | -11.21057 | -54.00677 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 758c6600-155d-3339-b794-99cf23a9c8f6 | -17.33184 | -43.62965 | 2026-08-20 04:21:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| f9249ea4-83bc-3739-9788-decdb2daded6 | -18.03366 | -44.62445 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23627f71-440a-3499-b5f3-45ff8615aaaf | -11.191 | -54.02092 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78f9aa05-0755-3010-bd1f-c347d21d8cee | -19.43571 | -42.51904 | 2026-08-20 04:21:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dc737a45-52b8-3342-9664-770a050334cf | -13.43643 | -57.06909 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2b8ba4b-2540-35a8-bea7-080c0c31995c | -12.84532 | -48.42727 | 2026-08-20 04:21:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d241e53-3f78-35c1-b466-48f36b2653fa | -14.31375 | -51.91528 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9bbbb06b-85b7-36fd-bd88-befbc713f5c7 | -14.32269 | -51.91691 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 55ab4fa9-30de-3a3e-bd09-4278d7429bf8 | -18.03029 | -44.62388 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 566f0dad-7a16-3cbe-8872-425294f9ce30 | -14.20011 | -52.88176 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0d572ed-f3f9-398f-b217-64e10a475b53 | -14.44856 | -45.61324 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8f2ad480-9f3e-3df3-82fb-2b5ab435c9a1 | -11.18423 | -54.02693 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc4ea386-46e9-3ae5-8989-0c9a89baf422 | -15.56359 | -43.43784 | 2026-08-20 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 917bf154-54ed-357a-a3f2-3d05501bfbf7 | -11.80886 | -56.59838 | 2026-08-20 04:21:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4813dae0-380d-370c-a370-c3168701804c | -18.02468 | -44.61522 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab1ce91f-a1b4-3ea4-805e-3a747a699627 | -13.6083 | -51.79169 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f441e8c3-c8ef-321d-8421-500e892a3010 | -14.44079 | -45.61925 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32711890-90fe-337a-8e69-edfa347ce0ac | -19.39298 | -46.41049 | 2026-08-20 04:21:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e955f4ce-a98a-35c7-a640-255d8c9af8d4 | -11.19776 | -54.01503 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c896bb76-3cc8-30f6-bc73-2ab2b2902862 | -14.32183 | -51.9215 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d8978f00-872f-32f5-bcb1-c6c1e17716d5 | -10.32404 | -57.56423 | 2026-08-20 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26c900c9-08d9-3452-98ef-8fe796e4c300 | -11.8185 | -56.60156 | 2026-08-20 04:21:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d0cfdb9-f2bb-3f70-9be6-77e205bdf5bc | -15.35683 | -52.7756 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e472b5b1-946f-3d77-8610-3df9a52efeb8 | -12.00497 | -53.44253 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce8b1f27-a569-3732-bebe-ab8c87c55c6d | -12.80979 | -48.43485 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1b06b3f-e720-3c91-a41b-e5056beb4d31 | -16.86568 | -43.23571 | 2026-08-20 04:21:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d4b4aa3-ec34-3f13-a9cb-d16f84412afd | -11.41942 | -54.31329 | 2026-08-20 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 893bf80a-2c3d-3700-bfaf-4757acd5fb72 | -18.03085 | -44.62011 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b9c1e0dc-8e7f-3742-aa99-ec8b91b8a440 | -16.08968 | -47.94592 | 2026-08-20 04:21:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f16a516-f887-312d-8763-e0d6cd92cd27 | -14.44354 | -45.62337 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 698f58d8-0f59-3b11-bbb6-fc6241ea8121 | -13.54257 | -52.22578 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 561bbeaf-eed8-3372-aac6-e9c841b21824 | -12.80858 | -48.42725 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9696640f-385b-308b-b991-a6d874dfa39b | -15.56074 | -43.43346 | 2026-08-20 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 911cecbd-25fb-3dc6-9c4f-0c0ae47191ff | -15.58867 | -43.73719 | 2026-08-20 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 332287f1-92d5-3ccb-8441-9a4ff8f68f35 | -16.42664 | -42.63355 | 2026-08-20 04:21:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 755dec83-9c3c-34d3-a4de-a70181db3968 | -12.81668 | -48.4243 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfd35e92-aefc-3490-86f5-619ab75a40a7 | -14.73469 | -47.15165 | 2026-08-20 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90af564c-fe11-3d21-8e34-67ce975ec697 | -12.00637 | -53.44333 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a658cca-5d49-354b-9da1-6e4b1472f4c6 | -13.43292 | -57.07249 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4c8ee9e-e974-3820-b84e-83a3064d28ca | -18.03872 | -44.61371 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 278a0776-57d7-3d4f-a5e4-cdcc86f40a38 | -19.61183 | -46.27174 | 2026-08-20 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db7c4ee5-449d-3957-8a69-0ff4808229ef | -18.55306 | -48.29469 | 2026-08-20 04:21:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 568317d1-6cb8-3230-8ad7-0b68eaf28ab1 | -14.15197 | -53.05197 | 2026-08-20 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19879797-68e0-31ae-8de6-cb41c12f6048 | -14.31013 | -51.90989 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 501ecb4c-f988-3884-bb73-76870e2e6a36 | -14.11559 | -44.38783 | 2026-08-20 04:21:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8107f653-b1f4-3342-afef-b4abfd63fe1f | -12.82837 | -48.41555 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 055131cb-8413-3314-b9ea-408b073449a9 | -14.30641 | -47.17329 | 2026-08-20 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 001307ba-a7eb-377f-838c-02002c03e226 | -11.23921 | -54.82626 | 2026-08-20 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 699b0e5a-c50b-3421-88ad-84f8d0b35fa1 | -19.71806 | -46.22271 | 2026-08-20 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9312e8d-d833-31f1-b461-572158d5381a | -11.21246 | -55.05386 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 02a9e026-44cd-3ba7-a228-8e95ee917a95 | -13.4427 | -57.07048 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cee5aef-9583-3fe1-8538-2a93b6f1a791 | -12.81352 | -48.4431 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 038b5916-54c8-371b-8cf7-32d44c373813 | -12.82531 | -48.43307 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76c5ede0-33f7-3742-87d4-caa0b4bcf706 | -14.03534 | -43.8507 | 2026-08-20 04:21:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1f90f26-54e5-34ab-9b6e-3c1dd703d429 | -13.1564 | -42.41298 | 2026-08-20 04:21:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d9636508-ae4b-340a-b8fe-9f60b065614b | -12.81644 | -48.44835 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 886b5fd1-00c3-3dc1-a30a-683236ecba56 | -11.20588 | -55.05677 | 2026-08-20 04:21:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9e6a1a50-dd27-3fcf-8625-ec4918e1a0d6 | -14.15304 | -53.04652 | 2026-08-20 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 263ca39a-b3e6-3710-8271-f1a7bf389d4d | -16.60761 | -43.37294 | 2026-08-20 04:21:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a34994ed-1c80-3706-90c5-74619bc34c1a | -17.9976 | -49.39978 | 2026-08-20 04:21:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07fb803b-13d4-3232-8b92-527c17fa5455 | -14.03479 | -43.85434 | 2026-08-20 04:21:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93776a37-0655-3fb9-8560-8391be170c9d | -11.22072 | -55.07315 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c004f45-6b6f-3704-a043-f4dcfc523f13 | -14.08631 | -49.22549 | 2026-08-20 04:21:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f6cc7ba-2579-3d9f-9f28-9627cae47239 | -18.87881 | -41.09536 | 2026-08-20 04:21:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d79a251c-9a03-3edb-b86e-49b3e9f1b38d | -11.18762 | -54.00932 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16561d56-2bda-309d-a0c7-ba4c1bd552a4 | -12.77552 | -48.42057 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README39.md)
