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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cfdd896-7af8-3416-a945-b7a441e342eb | -14.13551 | -45.3455 | 2026-05-08 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1813bb79-b9fb-311c-800b-bc1e61606a02 | -12.14987 | -46.66122 | 2026-05-08 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21c33005-843e-3892-b812-0cdca2bae102 | -14.17817 | -52.88528 | 2026-05-08 04:49:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 692649bc-6a5c-3813-9cb1-770d32921793 | -15.61631 | -46.51991 | 2026-05-08 04:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| da9b0c77-609d-304c-8c0b-e2cfb2fdc5c7 | -11.84131 | -55.01625 | 2026-05-08 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f14bd783-e88d-3126-aaec-715860f7602f | -12.14917 | -46.66606 | 2026-05-08 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2d48487-7a2f-3692-a739-097fc4490ea7 | -11.47317 | -52.92306 | 2026-05-08 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f41e4911-ef13-3885-b9e2-daf71b0af2fb | -13.64182 | -44.28678 | 2026-05-08 04:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7eef5c46-a9b6-307b-9641-e82a6e0373af | -14.13599 | -45.37493 | 2026-05-08 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80b664da-95e9-33e5-a651-56e08b7b6703 | -7.29183 | -49.62794 | 2026-05-08 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 003b7eb5-e288-3664-a7da-d863e2281eeb | -11.92084 | -54.10151 | 2026-05-08 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d78ad44-2bec-3cb9-9b36-87c0b351557d | -6.02351 | -44.22489 | 2026-05-08 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39767976-4def-3cac-b1dc-3b702c086a18 | -11.80532 | -47.10586 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ade45612-ddbd-3981-8495-5feae2a4692f | -14.17478 | -52.8847 | 2026-05-08 04:49:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4c766a0-b453-3c2d-958d-f2b1cfcae189 | -14.13982 | -45.34612 | 2026-05-08 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e392679-1cb5-3a19-a14d-8ba5d1fda3f4 | -18.24906 | -51.26551 | 2026-05-08 04:49:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b84c1828-cc7a-33d0-af36-3d08c7d49010 | -12.86567 | -43.75772 | 2026-05-08 04:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca903648-1846-35f9-8196-bc775ac69a23 | -11.46971 | -52.92246 | 2026-05-08 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f80bc8c-180a-3762-a98f-08bab93a5df2 | -18.25243 | -51.26608 | 2026-05-08 04:49:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69408aa3-7399-3bfd-ae67-9f00c01a8814 | -15.61223 | -46.51936 | 2026-05-08 04:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e7ad0deb-e995-3018-87d0-b047ce8b0947 | -18.48679 | -51.68246 | 2026-05-08 04:49:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16e51842-5977-3405-b91e-83e287cd2ea8 | -11.80464 | -47.10347 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6418a4e-674a-3235-bd8f-414b93fd72f3 | -11.30824 | -54.03461 | 2026-05-08 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb6b4db1-d97e-3a43-8690-1b7468550361 | -14.17539 | -52.881 | 2026-05-08 04:49:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e938e2fe-c65f-3a0f-9345-caf66cea155a | -18.33351 | -54.52474 | 2026-05-08 04:49:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b15a5ec3-5bbc-3e54-9af6-5a03eeae7edd | -11.80157 | -47.09841 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49ca642b-d26d-3a25-a1e5-96a2f21e5692 | -11.84248 | -57.84197 | 2026-05-08 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb27e7b2-4230-39a3-b74b-a7a002b548e0 | -16.59475 | -58.24326 | 2026-05-08 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 76f9ee96-2955-33f1-8a36-a34b58b05ed2 | -11.84513 | -55.01691 | 2026-05-08 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aed9f90c-894c-391b-b811-aadb84f985bf | -13.59921 | -47.85994 | 2026-05-08 04:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e8b11af-3066-380b-8b8a-30da61ece7d1 | -11.80286 | -47.09629 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f45447ad-7c11-3ece-bfaf-19cea47424cf | -18.16888 | -51.1041 | 2026-05-08 04:49:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 494372a6-145a-3e59-bee6-69aae5d40e57 | -13.47891 | -48.9161 | 2026-05-08 04:49:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d2cfe8d-9524-3cd0-ac0a-40fc003ccc60 | -13.59859 | -47.8642 | 2026-05-08 04:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4115ef19-e03a-367d-a482-12513b39d1f7 | -11.80223 | -47.09388 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c0f1869-892f-3b53-b7c4-1528b34f0250 | -19.1814 | -47.35246 | 2026-05-08 04:49:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34770bb9-4ae5-3637-9dda-aac44755af07 | -7.1539 | -48.24 | 2026-05-08 04:49:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed700272-b5de-3278-b665-14ea21d1c3a8 | -11.47381 | -52.91922 | 2026-05-08 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5797e75-272d-3668-9ada-9698df0e14a4 | -12.54679 | -54.61839 | 2026-05-08 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 250beade-ad82-3752-9e51-45f02a847ee5 | -14.13606 | -45.34136 | 2026-05-08 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef0e29de-e0a0-38f2-b192-09cd793b2377 | -11.79977 | -47.09119 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2408b27e-ac5b-3654-a89d-a7325e1a4c0c | -12.425 | -54.21361 | 2026-05-08 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cf23fe2-144e-3261-b048-6f562edbc294 | -6.89039 | -42.8572 | 2026-05-08 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e616ddec-c0ee-3dab-9bb4-42e2f39dbd50 | -12.41266 | -49.66975 | 2026-05-08 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 654a6e3e-1b33-3f89-a5cf-e0fae0c7a684 | -11.62889 | -47.88739 | 2026-05-08 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1c56c9c-5c4a-3124-a0b1-87a6a4ffcf83 | -14.13544 | -45.37909 | 2026-05-08 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abbed942-aabc-3ba6-a93e-9716eaf65963 | -6.66328 | -47.54684 | 2026-05-08 04:49:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb5586ee-84d7-33e9-846d-2bf33d52268e | -11.62828 | -47.8915 | 2026-05-08 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81dfaeb9-182e-31a3-914c-a2b1d454837e | -12.40352 | -46.75901 | 2026-05-08 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2b7831a-0d9a-3a20-9af8-edb944cafe9b | -12.15303 | -46.66662 | 2026-05-08 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47e546c6-2b82-3c85-8e27-4be1dace2d95 | -11.98056 | -46.79036 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65cefd58-c426-3db2-bf34-67bd26916f4d | -12.35086 | -50.02759 | 2026-05-08 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3a0abaec-48ef-362c-892f-1d1dbb56fd57 | -7.29238 | -49.62447 | 2026-05-08 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 178bd2b1-b8f8-3e4d-ac0e-e06e76ae3a1f | -11.79475 | -47.09279 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf237e09-d0d7-3ee1-a2e8-f3b78104fc98 | -12.41605 | -49.67028 | 2026-05-08 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54c7a486-2c4f-369c-b291-434cca7c03d3 | -11.79912 | -47.09573 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03221d70-23ce-327d-ad6a-eed08294e8a3 | -11.47035 | -52.91862 | 2026-05-08 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbd3d868-e904-338f-b206-4db2f79300b7 | -11.60373 | -54.18734 | 2026-05-08 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f975f037-8686-3e92-952c-8bd58718087e | -14.13176 | -45.34074 | 2026-05-08 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f86e109-183b-372e-a4f5-4cab1690f935 | -11.84796 | -55.01472 | 2026-05-08 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b82970d4-7f01-3e6e-91b4-478a80ab63eb | -5.78629 | -45.12115 | 2026-05-08 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 838437b8-577b-3947-8d60-2e33d7f34aa2 | -19.18202 | -47.35321 | 2026-05-08 04:49:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8672d3cd-2f52-3aa7-b70a-618f3d7da90c | -6.77141 | -46.81934 | 2026-05-08 04:49:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 249a2808-abc1-37e2-81f1-b6441368cfed | -17.9452 | -52.95875 | 2026-05-08 04:49:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d791c31-5955-3c19-a1fb-e4188f84e452 | -11.06906 | -52.47493 | 2026-05-08 04:49:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09105a34-39e4-3fb8-bdbc-381c70a3e1f7 | -18.4996 | -51.68844 | 2026-05-08 04:49:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37f04386-4cf3-3b35-b7e0-a208f5abc3eb | -14.14863 | -52.89217 | 2026-05-08 04:49:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1323c38c-9949-324b-a685-ccc32c91d9bf | -12.15372 | -46.66177 | 2026-05-08 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 241276a6-face-34aa-b665-f204fe77fc1c | -15.61681 | -46.51621 | 2026-05-08 04:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3db62081-74b4-3f91-ac4d-cf34a0cfe18e | -5.78485 | -45.13073 | 2026-05-08 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cc79435-85f1-3cbe-807e-91585f4427a1 | -17.10564 | -51.34538 | 2026-05-08 04:49:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 48d5f920-90d3-375c-8c92-42a982e20c94 | -11.80222 | -47.10081 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0211596f-fc45-3f14-a0b7-7ab5e0a8e719 | -16.42539 | -52.79627 | 2026-05-08 04:49:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ad5c104b-b247-34ba-aadf-36c70bad40e0 | -12.8556 | -43.76145 | 2026-05-08 04:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd98c8a0-4a1f-3552-8654-c6ee2ecbce03 | -11.6125 | -54.18003 | 2026-05-08 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d67105f4-da2d-3ffb-b218-c09d42072cf4 | -11.84974 | -55.01286 | 2026-05-08 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bcf2304-5860-34e8-9663-60d7c8528bc4 | -15.62139 | -46.51308 | 2026-05-08 04:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d294e0c0-77f5-3deb-bbb8-5ca91f8b5239 | -11.60797 | -55.32767 | 2026-05-08 04:49:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc2d8a5a-3802-38bb-b84e-810f8b2c000b | -15.62088 | -46.51677 | 2026-05-08 04:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56c20742-a85b-3e53-9abd-e5a6d3946892 | -6.66182 | -47.54739 | 2026-05-08 04:49:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22e78441-df8d-35cd-a754-69d7ab484afb | -16.16143 | -58.48711 | 2026-05-08 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 50c5e6d3-8ec6-3e5b-adca-78adb28e2275 | -16.16583 | -58.48801 | 2026-05-08 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9fbc7343-8dc9-3d93-b44b-21e8c0850dda | -11.79783 | -47.09787 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aadae110-bcb7-3659-b1a0-33aa9fd45cbf | -11.7985 | -47.09333 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbb36b79-ec59-3cab-b110-57529ec30aba | -11.60885 | -54.17937 | 2026-05-08 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c5769a8-6bbf-3e1f-8702-047af6b6ea8c | -16.15618 | -58.49065 | 2026-05-08 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 69321c97-efd3-3eef-b35d-a1a091a759f2 | -7.33732 | -49.78856 | 2026-05-08 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c673fa9-17e2-375d-9e10-d5a2155d4dc7 | -11.82522 | -47.33667 | 2026-05-08 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09b4d825-f1a3-3c50-8b4e-fec9526e10b0 | -11.84617 | -57.84761 | 2026-05-08 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04d8c072-aecc-304f-acdf-2fb52b0ad2e1 | -11.8009 | -47.10293 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc3dce74-3797-3a57-82f3-5f12b5168684 | -17.70096 | -51.66788 | 2026-05-08 04:49:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| abccc6fb-1b22-381b-80bb-ae40721e7aa2 | -11.06967 | -52.4712 | 2026-05-08 04:49:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f00b0ee6-7a3f-3b3d-b1dd-ebf6657e182b | -14.13863 | -45.38797 | 2026-05-08 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5820a7cc-ac53-33f9-9580-c08aae901873 | -12.12158 | -54.66895 | 2026-05-08 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dfcaf00-021f-35f1-ade5-62db80b6ced0 | -11.80531 | -47.09895 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61fe6963-6050-3624-b724-4671143a69f5 | -14.20039 | -57.42329 | 2026-05-08 04:49:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1fb82f0-b4fb-38b1-a95d-100dab5dfefb | -14.14036 | -45.34197 | 2026-05-08 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5730f2cf-0542-36d8-a99a-51e9c5ba4dfe | -18.38961 | -51.44026 | 2026-05-08 04:49:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 957deaa1-3bd4-3a3c-b514-6d02201cba3d | -14.13489 | -45.38324 | 2026-05-08 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1672c0ff-1fc3-3409-a9a1-828e4a903c65 | -11.80598 | -47.09443 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README8.md)
