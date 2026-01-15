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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8fc927e-7388-344b-97a7-5685c84b1b5f | -7.22163 | -39.9501 | 2026-01-15 04:33:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4cbd8340-6e92-3f62-a9cf-610b7e5157d9 | -8.43104 | -44.02403 | 2026-01-15 04:33:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3039b0e2-fc25-3cce-af16-5051140455e7 | -12.31703 | -44.53738 | 2026-01-15 04:33:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a192e6a9-5678-35e9-b143-f59b688fb103 | -7.05281 | -43.9509 | 2026-01-15 04:33:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab6521c9-4a39-3d01-8d0c-9437049ce63d | -9.01161 | -39.86158 | 2026-01-15 04:33:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 200cd3af-b111-3bdc-95f5-a0c5e75aa4af | -7.24825 | -43.05393 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e95fdc02-b62a-3d26-85bf-a408b6344333 | -11.95402 | -44.21043 | 2026-01-15 04:33:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 907d4bf7-a587-3855-a41f-a241ea887ac4 | -8.16088 | -43.18687 | 2026-01-15 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 808506af-5118-361c-ba86-bcbf66815de4 | -5.93392 | -43.51032 | 2026-01-15 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96c310f4-280a-34d8-bf71-a23b984e9805 | -5.60376 | -45.20791 | 2026-01-15 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc1689d7-1739-3eb4-aa86-31b835c1542d | -7.60969 | -47.05681 | 2026-01-15 04:33:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 824eff29-2fd0-3b7d-addd-d1c2f61fef63 | -8.16107 | -43.18677 | 2026-01-15 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6cb7fee3-3cb5-384e-995f-9a1e226b4ad9 | -10.15833 | -42.20979 | 2026-01-15 04:33:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df276778-9bc5-3540-9ece-3de603e4e1c1 | -7.2442 | -43.05331 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5d95a7f1-fabc-31b9-b6a0-88f9a0750393 | -10.15385 | -42.20915 | 2026-01-15 04:33:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0776434d-0c75-338b-b775-2dd1662c671e | -10.34579 | -44.82626 | 2026-01-15 04:33:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6209c371-820b-322a-b5ff-266759f19695 | -12.08826 | -45.57144 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6663631-cef6-3b63-8b03-8d884b68a36f | -7.86198 | -39.09479 | 2026-01-15 04:33:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3e1a729e-37e1-3379-aa82-dc24fce5bbfc | -7.23205 | -43.05148 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f3467014-061c-33b1-a34f-01da2cfcaf84 | -12.12969 | -45.57301 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 945095b6-df85-3748-95be-83d39df78aa4 | -12.09259 | -45.2966 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eacf373f-814c-3b85-aa5d-1b697a5505f4 | -9.37014 | -47.07937 | 2026-01-15 04:33:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e559249-5693-3381-93d7-d7f93ad746c5 | -7.05211 | -43.95562 | 2026-01-15 04:33:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aecc76e7-b249-3f71-8fb9-011edb3c055f | -5.93319 | -43.51517 | 2026-01-15 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ff3825f-fd75-336f-8f61-9b9f0e2e3760 | -8.16142 | -43.18325 | 2026-01-15 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b3b43485-a96a-3791-8d74-e6f35a8af053 | -8.15329 | -43.18198 | 2026-01-15 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27928587-3993-3e68-abdc-894d5bf3cad6 | -12.0783 | -45.58823 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 494e71b3-31e7-3987-b4e5-92464861b156 | -5.47844 | -43.03753 | 2026-01-15 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6db80ac1-f1a9-3ae8-b668-552417860356 | -5.29411 | -44.20139 | 2026-01-15 04:33:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a301c41f-2d52-3b51-a7f5-b51e25dca486 | -7.60915 | -47.06036 | 2026-01-15 04:33:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca32bfed-c7c1-3019-a564-afbc862ca170 | -12.08889 | -45.56696 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 186d9de7-4039-3682-9cf9-3896d213b7a5 | -9.94042 | -47.84084 | 2026-01-15 04:33:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6fc5748-e689-3e60-afe4-8a802775926f | -8.42716 | -44.02347 | 2026-01-15 04:33:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88860b50-9abf-38c4-92aa-e6d4938ad3a2 | -12.66407 | -46.76704 | 2026-01-15 04:36:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc2955e8-5ae1-38c5-8ded-39834c946589 | -10.31731 | -59.05661 | 2026-01-15 04:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82dbf406-8ac5-3cf1-bb26-3f77fd0f4055 | -16.64444 | -45.13716 | 2026-01-15 04:36:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2f9a652-cf21-3417-9753-83efa4ad6420 | -13.74467 | -43.66269 | 2026-01-15 04:36:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17f5743e-31b6-3e14-a0b6-bd414d5a7686 | -10.313 | -59.06053 | 2026-01-15 04:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85fc2ff5-69a9-3ae4-be85-a26927564749 | -12.66114 | -46.76247 | 2026-01-15 04:36:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 77d4d555-35b2-3a5f-8844-8a7f28b1b6a9 | -12.65762 | -46.76192 | 2026-01-15 04:36:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 36e2d0dc-b6ee-3468-8fb8-bec9d4d35741 | -13.54184 | -43.63257 | 2026-01-15 04:36:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 494af619-4e00-3726-89de-508d1103323f | -12.66056 | -46.76648 | 2026-01-15 04:36:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f30c0cac-aecf-3b86-a7d5-1eddbc53617c | -17.02437 | -54.07245 | 2026-01-15 04:36:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ef31ec7-cd29-378b-97a1-4631d11e6f9e | -14.40682 | -44.58575 | 2026-01-15 04:36:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3a90574-0562-3c3f-a6ba-9788e6236a15 | -10.31655 | -59.0605 | 2026-01-15 04:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87f4e365-080c-3e91-aa60-fd06d49591e2 | -17.01997 | -54.07809 | 2026-01-15 04:36:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49ad5630-2e71-329f-bb4b-6895c8b96993 | -14.17275 | -43.71648 | 2026-01-15 04:36:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a31bdb74-5f10-3140-98e4-4585118aaeb7 | -17.01993 | -54.07624 | 2026-01-15 04:36:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fb592db-a0d8-327b-9a7e-5cc9339c9744 | -10.31936 | -59.05765 | 2026-01-15 04:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f18e096d-ff6d-315f-b696-b32fb75a2dea | -15.59318 | -57.34295 | 2026-01-15 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f761e014-73af-33b3-aa69-812b639e9db4 | -14.17222 | -43.72063 | 2026-01-15 04:36:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 103c089d-c5d3-3cb8-bc9f-102620183bac | -16.64528 | -45.13637 | 2026-01-15 04:36:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 577c4dd8-b4f3-3767-8af9-3ddfbb81d4ca | -10.31863 | -59.06151 | 2026-01-15 04:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0de8e3f1-f9b6-3b3c-83a1-cf177deb62a7 | -14.28691 | -47.42162 | 2026-01-15 04:36:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 340e1c1f-4906-35bd-8b8e-e52fe564f5f5 | -13.60359 | -43.56152 | 2026-01-15 04:36:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9f64eae-ca89-36fd-9efe-ecbb643f26d4 | -18.28042 | -42.43662 | 2026-01-15 04:36:00 | NOAA-21 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 64fec230-9eb3-375a-9371-b087dc5045b7 | -10.31578 | -59.06444 | 2026-01-15 04:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d36a62f3-601a-3c00-ae01-345bb98a3aff | -17.02357 | -54.07696 | 2026-01-15 04:36:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f80c1ba-d819-3315-b442-99f5013adfa6 | -12.23678 | -46.86744 | 2026-01-15 04:36:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1c1f2c7-6f10-384e-961d-ceeee90b07ac | -17.02073 | -54.07172 | 2026-01-15 04:36:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4470284c-1634-3f26-b95f-c0b3277532c3 | -12.65704 | -46.76593 | 2026-01-15 04:36:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3ac905ea-c652-3a87-9e74-059b9c94c38a | -13.60789 | -43.56211 | 2026-01-15 04:36:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f84515d-9584-3d96-945d-4c4ba2fe6f98 | -14.40731 | -44.58208 | 2026-01-15 04:36:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cab9d5a-ad7a-3bbe-ab7f-99d0947fc076 | -12.51293 | -47.24934 | 2026-01-15 04:36:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcdaec11-a449-38a7-86d4-78f517be8569 | -17.02075 | -54.07356 | 2026-01-15 04:36:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2f9d7cc-7760-355b-acd7-13c797b8e7fa | -20.70947 | -56.4501 | 2026-01-15 04:38:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b776f5a-671b-371e-97b9-da31c16f4f78 | -20.4237 | -57.83958 | 2026-01-15 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4b68e96f-a0f6-3df0-a919-89c9d0385ce7 | -20.30546 | -55.79565 | 2026-01-15 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a1a420f-72fa-3428-a88c-e63881ceffab | -22.86921 | -43.08596 | 2026-01-15 04:38:00 | NOAA-21 | NITERÓI | RIO DE JANEIRO | Brasil | 3303302 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 47f32f99-f070-327c-99cb-8f26bbd50767 | -20.07259 | -57.19205 | 2026-01-15 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5f30176-bf25-3959-a302-e67046ee0fd1 | -20.41939 | -57.83863 | 2026-01-15 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b0dc2f73-d4f1-3fd0-87ec-8236c41ac089 | -24.10765 | -50.4837 | 2026-01-15 04:38:00 | NOAA-21 | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d001916-6fb5-307e-b187-55c14796fabd | -18.95276 | -52.37752 | 2026-01-15 04:38:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d12b962e-b00b-318f-ad4c-7cd90269097b | -25.2107 | -53.36286 | 2026-01-15 04:38:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f8bbd585-d7e0-3b5f-b44f-22482ac19f90 | -19.3733 | -40.86734 | 2026-01-15 04:38:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 46bf0336-6807-3ae6-8a18-7b6e5eb1b967 | -19.37381 | -40.86608 | 2026-01-15 04:38:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5128079d-2ecf-35db-a1b3-1bccd96ea965 | -20.84406 | -51.74152 | 2026-01-15 04:38:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d1efa68b-705b-3c8e-a5a4-55c49b228016 | -20.40732 | -57.80869 | 2026-01-15 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c7b7b33d-18c8-35f3-abb6-2e5ef5e20e82 | -20.84465 | -51.73784 | 2026-01-15 04:38:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 35e0347b-08d3-310f-b5d4-c9b886f62e04 | -27.24376 | -48.77949 | 2026-01-15 04:40:00 | NOAA-21 | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f504e056-4268-388b-b388-afe71b6c5695 | -25.71738 | -51.59515 | 2026-01-15 04:40:00 | NOAA-21 | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e4f76d5b-7efb-3b7b-bad5-ad56ef72e74c | -27.78122 | -50.52128 | 2026-01-15 04:40:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3d51e967-3e36-3baa-a7eb-4784e09ad0c6 | -26.10696 | -50.17603 | 2026-01-15 04:40:00 | NOAA-21 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2171b9f0-278f-34d9-83e4-c2aabea61ad0 | -26.10637 | -50.18026 | 2026-01-15 04:40:00 | NOAA-21 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ecb8220f-8547-3ce2-8b32-648b4a32f56d | -0.08912 | -51.27986 | 2026-01-15 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 756b6b5a-5223-35c8-82a8-4e107cfa3997 | -2.65385 | -54.84119 | 2026-01-15 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f990c0e-f553-3834-b0a1-3c3f9578490b | -2.65047 | -54.84066 | 2026-01-15 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65ebf009-3a06-33ef-b0b9-568128d72ca3 | -3.23448 | -41.80268 | 2026-01-15 05:01:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 96fbd3e0-2ac2-3607-afc8-a4e49b422072 | -3.23371 | -41.80191 | 2026-01-15 05:01:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ebd2f92b-9d82-366f-87ba-7c01b4171599 | -2.25025 | -48.17536 | 2026-01-15 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e548e759-9618-3af5-94fe-650f82df6871 | -5.8966 | -42.54541 | 2026-01-15 05:01:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4909760e-c448-37ed-a918-960c273cf84d | -2.45578 | -46.90575 | 2026-01-15 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bf105ab-6931-32ec-ba2d-6d92a894a596 | -3.23293 | -41.80712 | 2026-01-15 05:01:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| bda5d480-c02a-38bd-bfb6-7a75b61f56db | -2.92813 | -48.23011 | 2026-01-15 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7bb8e3b-78b5-3d5a-89ba-66f190eeab7b | -0.90781 | -47.55201 | 2026-01-15 05:01:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2d945df-5f24-36ec-885d-59cd52a18009 | -2.93282 | -48.22708 | 2026-01-15 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74d907a4-f43f-31b6-a0ae-b4cccc1dc189 | -2.25082 | -48.17168 | 2026-01-15 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f95151d-ded0-3d0e-818b-36fc66dc6a7c | 2.69853 | -60.07093 | 2026-01-15 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe2f2866-5d83-3995-9a2c-f6a1cc23558d | 2.83887 | -60.80872 | 2026-01-15 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 718d02f7-2eae-3a47-96c3-544ba7142e32 | -2.93226 | -48.23077 | 2026-01-15 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
