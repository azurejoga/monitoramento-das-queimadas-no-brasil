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
| 46f4642a-e667-3d3d-9162-cd658f75d7f4 | -11.31365 | -45.86628 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8710bbc1-7c86-3d03-a8e7-8fb1f1ba20ef | -6.87077 | -56.40779 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e70728c-7879-3746-a7d2-4509580bbdb8 | -14.48251 | -45.68023 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f9a86e14-48b7-3a99-aa81-9eb2d67f7633 | -10.47114 | -46.31593 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 028541a1-6374-3250-8e16-b7d82dc659c9 | -7.39748 | -55.48157 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a80b382-15d8-36f6-8640-fe17fbc8bf54 | -12.68127 | -48.51872 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 072f20cb-0494-301a-bf25-25f603faf854 | -6.10978 | -57.7329 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4c3e10f6-6c9d-3a6c-bea3-a2f888fb3a60 | -8.62978 | -54.72338 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d203d44-dc66-3dc7-bcb2-9876859c7e3d | -12.57051 | -47.86553 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e49c0b3-4048-3d0c-8568-3242fbe2e36f | -15.04287 | -47.02289 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df3daeb3-3636-38d3-9442-b3e15ffcbd9b | -10.27234 | -48.28487 | 2026-08-17 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f39a884d-be30-3730-9b54-6c99b03d0f3d | -10.11191 | -48.81574 | 2026-08-17 04:21:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f76b7e81-4d84-35e1-8af5-f454e58ae92b | -10.50413 | -50.01847 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 0a6f0b57-75da-3fc8-a9c1-599ac1e1f4c2 | -9.12727 | -46.01639 | 2026-08-17 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8d4aeb3-fce4-3e2b-85df-e920255f765a | -11.54983 | -46.8506 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 554a3ac1-86a5-383b-ab1a-13c63e6239d1 | -9.27378 | -45.64608 | 2026-08-17 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 644a5735-c8df-3f09-b577-343e285c6340 | -8.73646 | -45.32132 | 2026-08-17 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d96049d-cab3-3de0-8b4a-f9af345725b2 | -13.51056 | -46.25458 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffa01a34-9435-3bc1-9e36-e5edfb677d4c | -12.72618 | -48.46182 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d8367c30-95b3-3964-a780-01f5e5682a0b | -14.29693 | -47.20246 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d6f41ce-e7a5-3d3f-88a3-450dbd3f2e98 | -13.50778 | -46.22882 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 446ef636-0591-3e30-9a3b-bb668d8f4e36 | -14.03362 | -53.62451 | 2026-08-17 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f51a8a7b-4a43-3121-89e0-cb582db2331b | -11.7135 | -54.6022 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fde0067-9c87-3def-baea-ce5948aa5ca3 | -11.10203 | -47.28345 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b49d92fd-3bef-3b43-8f68-dc87c0638e43 | -6.81868 | -56.4481 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91a0b173-8297-35ec-9f39-9d6b465a6e76 | -9.47252 | -51.60818 | 2026-08-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1799ada1-3907-3331-8d9b-c25ffd8b374d | -8.67069 | -54.77373 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 754060df-5450-3f28-a3dc-6124fadaa138 | -13.52377 | -46.23504 | 2026-08-17 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 986a3f13-4436-3c4d-9d1c-2ad0e7ced911 | -14.38094 | -51.86762 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfee99be-7391-33eb-b30f-ca3e0a5406ec | -14.46004 | -51.84457 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc002ab0-608f-3bac-b1c4-262d282e8269 | -11.13389 | -46.49199 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a33714c-6e55-3842-b832-2fb07c711104 | -12.67567 | -48.50955 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d80882b6-ba09-3efa-9b31-ccf40854ec84 | -6.11541 | -57.74012 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bb9441ba-ddab-3b61-a353-c7c2e95bb09e | -8.63999 | -54.72841 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4eeb3714-8828-3ae2-8198-969da7e9a2c2 | -11.49083 | -46.57913 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 326f83e8-52df-3067-9511-748fa3a81c10 | -14.30138 | -47.19588 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ebf176b-12c1-3578-bf30-43b4211be056 | -11.41305 | -46.4041 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e620616-8956-3ea0-8ee0-1a62b3b18863 | -8.44422 | -43.86803 | 2026-08-17 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b3d606c-ae52-3b5f-bf94-dac182db61c5 | -11.31303 | -46.30444 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7defaf74-fd2f-3d21-8781-4f54f03f9cdb | -14.88589 | -46.63537 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3ca2e6c4-9312-3e4e-a954-1b3460da0512 | -11.29855 | -54.8765 | 2026-08-17 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a9fa099-89c6-3285-aff5-254274f8062d | -11.49854 | -46.59493 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 413bf7c5-b131-39bd-8677-5bc7633c8d8f | -10.50575 | -50.00887 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35de3906-77f5-398e-8689-87d911996af6 | -9.49467 | -51.60835 | 2026-08-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9f1d8eb6-138f-3bab-b34b-adfecc0a2f86 | -12.55199 | -47.85094 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fb6d448-4e70-3feb-b86e-c532b81a2907 | -11.09925 | -47.27926 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba30aadb-2d00-31fc-aaa3-3fca6a2b80a8 | -11.53964 | -46.22628 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e034088c-6f67-3863-8b07-925241ac8ef2 | -7.38132 | -55.50425 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a41ff339-bda5-347b-a816-b6361335058c | -9.55853 | -45.37074 | 2026-08-17 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74b6eda3-8ac5-3ef5-835c-a832dfd9a15a | -7.38942 | -55.49285 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d1d73981-adb2-3314-b801-9f2b482e07ae | -11.71744 | -54.60913 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dce347cc-2c36-366c-a73b-f738f8f6f1a2 | -14.71762 | -47.97284 | 2026-08-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecfd6999-2372-3e1d-9240-d84dee1bb5a5 | -11.84382 | -51.77383 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26052ec0-52d1-3852-adfb-09e46433fa93 | -11.08327 | -47.23941 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f21c7d26-351f-3fb8-828c-95dbae2db53a | -14.88533 | -46.63893 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f5107012-0fe6-3378-8a39-34c3ced37d10 | -12.00554 | -46.46473 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8f4e656-2bdb-3cb2-98ab-53d81cf3d876 | -14.45908 | -53.07477 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c19e8345-36a5-32dd-b288-827ac3e13553 | -11.21796 | -54.01409 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1f80503-eb75-3bc1-be9f-6af148a5906a | -10.3736 | -48.30921 | 2026-08-17 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 237abc48-aac4-3721-ad27-aed342377f93 | -14.40517 | -51.87213 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21842944-744f-3917-8ebc-745d06a1b87f | -10.5003 | -50.01781 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 646ef758-3493-3542-992f-4385b790a272 | -12.67964 | -48.44256 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa99cfa4-c18e-3467-9161-ef03973630f0 | -14.8699 | -46.6509 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e815ecb9-ebb1-34c4-b0fe-fab27ecaefe8 | -15.14813 | -50.05088 | 2026-08-17 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 404044a0-0dc5-34c1-8f30-c82daf075f66 | -8.58837 | -54.69292 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 098917d4-625a-36f5-a7a0-96ff35ff0287 | -11.13163 | -46.50617 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8c13d9a-ebdf-3574-8070-8f6b7e738767 | -12.56531 | -47.87608 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3165d45d-0daa-3f0d-9405-de4959cd2d5a | -9.6984 | -47.66253 | 2026-08-17 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82fc78f0-d12e-3ea4-a43f-e4252a6daf04 | -6.13523 | -57.73399 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb8e530d-84d3-316a-8937-87e8b4bfd531 | -12.75806 | -48.43501 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 952f0201-fc15-3460-932f-a729e718d6f9 | -11.45151 | -46.59098 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff75492e-bf77-3bb3-9886-1b604a086fde | -11.13275 | -46.4991 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ad702af-91a1-32c0-9a61-00e72418dae9 | -12.71 | -48.49553 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f14f534-eb5b-3cda-bab5-123dfa86aaf6 | -8.52388 | -54.89359 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44307a67-1ee1-3013-88ed-4856aae2a8c4 | -14.47863 | -45.68331 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f073d3b-9c5f-3a77-a0de-69baa750db60 | -12.67222 | -48.50888 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| edf8c5b9-c798-3c13-968f-d0880dba5ab6 | -11.10144 | -47.28708 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0f00fb5-4bd9-37dd-ad85-312853415cb5 | -12.02161 | -46.42749 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b2b19cfb-615f-3954-bffa-42a705fa5280 | -11.72361 | -54.60418 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c8bc7c9-3175-3916-a504-2503b59ff8ce | -8.36932 | -46.37871 | 2026-08-17 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4af44b3c-fa93-336c-ad8f-a01aa4bfd713 | -6.11761 | -57.72841 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1cd101ba-cccd-3865-b868-db0218fa39e0 | -7.39823 | -55.47754 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3e8b716-56b6-3efd-8b5f-682a0c312553 | -8.36262 | -46.37769 | 2026-08-17 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 348f3303-3ec0-36b4-a88b-c5dca4e0bc66 | -14.38201 | -53.15005 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb15c2f3-262a-34d6-b808-482b14a755c2 | -9.47678 | -51.60916 | 2026-08-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 788b8669-e000-3a19-a534-ba6c69f8bb4f | -11.45594 | -46.58448 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71c5241c-972a-3768-8b98-9e71719a2f47 | -9.05497 | -45.82858 | 2026-08-17 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76dd81ae-48e6-3322-bf1f-095b48dda221 | -10.47708 | -50.37027 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5e3d7f3-9525-3ce5-9f20-50fd5547c205 | -11.81209 | -44.81031 | 2026-08-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bf9cef19-2d36-3dc5-8fa5-8206abc879e4 | -6.87608 | -56.41365 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf69a078-45a4-30ec-8d4c-a22858856b1f | -14.87432 | -46.64434 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed134f52-68c8-3965-84b8-673a73713a7f | -12.25139 | -43.14805 | 2026-08-17 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7314f08d-7416-37ee-aede-9fed7e883a98 | -11.69599 | -54.61158 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93877173-c468-3f8c-9b7e-d13e5e8e18c5 | -12.6704 | -48.47693 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f1d4c47-8813-3474-a893-ffd9fc7ee7c7 | -12.53513 | -47.89007 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0582f86c-f617-3cc2-8fa5-db9785fd5e6d | -12.04365 | -46.4816 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba87c0b3-e36d-3ff1-89db-c3a10f54de1b | -11.4991 | -46.59137 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 368c1cf9-9dc8-35d8-92c7-ab514acbe77f | -14.45754 | -53.08331 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6119f11d-b475-3bf7-86c3-8bf9d6e927b2 | -14.29976 | -47.18462 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff088a90-c8a6-327d-8b9a-e071404dd77e | -11.55233 | -47.17172 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README17.md)
