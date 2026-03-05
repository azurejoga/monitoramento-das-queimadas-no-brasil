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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45e4b97f-e98b-3c90-8f58-41058f677f93 | -20.75364 | -50.53456 | 2026-03-05 04:21:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e18f71bf-d24e-3c31-a030-ad8fd9523572 | -22.96799 | -49.91057 | 2026-03-05 04:21:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 672c9de3-4c99-313e-b2c9-d3763b4c5a76 | -25.00731 | -49.30037 | 2026-03-05 04:21:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e29b878e-54f5-3f93-a5cc-400ec7e2c102 | -25.00865 | -49.29245 | 2026-03-05 04:21:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a713c92c-f170-3f66-9f6d-17317f2697fb | -21.47653 | -48.69137 | 2026-03-05 04:21:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e47d2a4-7440-3304-9707-024839e4319d | -20.94179 | -48.71122 | 2026-03-05 04:21:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8556d80f-ed09-3743-ac08-d896710c17be | -21.23372 | -48.52488 | 2026-03-05 04:21:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a1c15ac-5bf9-3e58-a986-955c4be2cb49 | -24.28089 | -49.71516 | 2026-03-05 04:21:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d43635f5-baa8-395f-840e-20ba895097b1 | -22.91566 | -48.60554 | 2026-03-05 04:21:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a420948d-4319-3758-8e34-3cdf52ac06e4 | -20.94035 | -48.71818 | 2026-03-05 04:21:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6757a851-f417-3e0d-a9e2-929f78c453c0 | -20.94172 | -48.71023 | 2026-03-05 04:21:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f820350d-7832-3fd6-8a89-bef3d9ba6a03 | -23.22473 | -46.56055 | 2026-03-05 04:21:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ac66914c-f01a-3026-9a75-3c10aba9c90a | -21.22143 | -49.48631 | 2026-03-05 04:21:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3a8e556c-75bc-3467-a652-9e82fdad1eda | -25.17295 | -49.39921 | 2026-03-05 04:21:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f095bb4f-e894-38e8-a132-0f17bcf7c2f8 | -25.01876 | -49.29448 | 2026-03-05 04:21:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 20b53727-17b6-310d-b4bd-a920c1c09192 | -21.70706 | -56.32439 | 2026-03-05 04:21:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2594110-0c08-32ce-a028-d58c6d5529f5 | -21.30303 | -48.59411 | 2026-03-05 04:21:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0e50a5d8-9f77-3e50-8e8d-2dc421aff9aa | -24.79166 | -49.63518 | 2026-03-05 04:21:00 | NOAA-21 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3b24b88d-c375-35a4-822c-33cd50ab6381 | -21.08969 | -49.2211 | 2026-03-05 04:21:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0621ae50-fa18-307b-ad86-ec5bf9ff4c80 | -23.78195 | -49.04809 | 2026-03-05 04:21:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 305070c0-8153-357e-8159-e76e393f456d | -21.70593 | -48.43607 | 2026-03-05 04:21:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 873d27e9-ab28-3a85-8b49-4db27540db51 | -20.94112 | -48.7152 | 2026-03-05 04:21:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| d4ce8a51-a36f-316d-840d-8a34c95ad351 | -20.91714 | -50.53198 | 2026-03-05 04:21:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| beaa84b7-8511-3a04-97e5-b4e25b7977de | -21.30236 | -48.59805 | 2026-03-05 04:21:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 70114886-612f-3b25-bdce-7a32b28116e0 | -25.0154 | -49.29377 | 2026-03-05 04:21:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5910303b-35ea-307f-ad68-30b1aaee2e1b | -29.67373 | -49.9765 | 2026-03-05 04:23:00 | NOAA-21 | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| e635572e-4286-3ec4-94a7-f6f7ae45bd2d | -28.7382 | -50.94825 | 2026-03-05 04:23:00 | NOAA-21 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cc432066-ddd0-32cc-98c4-d3b5c282acba | -29.67439 | -49.97247 | 2026-03-05 04:23:00 | NOAA-21 | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 03e86510-9dca-3ee3-9cf6-280b7b5c8739 | -28.66511 | -49.88676 | 2026-03-05 04:23:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2bfddc3c-790d-30a9-84b5-c2b096ee8c08 | 2.7816 | -60.3338 | 2026-03-05 04:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 0b6965c5-b1c9-3ae2-aaf8-d54226995131 | 2.7816 | -60.3528 | 2026-03-05 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 88ebdf82-e9ec-3b22-9283-de80356d9bd4 | 0.0455 | -60.9799 | 2026-03-05 04:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 84498bc8-65aa-391f-acab-3c3a5096b8b5 | 0.0455 | -60.9799 | 2026-03-05 04:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 20.8 |
| fd9231e8-df79-3eb8-8810-43ba003a6122 | 2.7816 | -60.3528 | 2026-03-05 04:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| dd559686-6a88-3bbb-b0e9-4f393606d2c3 | 2.7816 | -60.3338 | 2026-03-05 04:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 157.4 |
| deca6b4e-079f-382d-992e-117360e13fc3 | 4.96616 | -60.26827 | 2026-03-05 04:42:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 188bf453-e55f-3df3-944f-37743c761d00 | 4.54138 | -60.57128 | 2026-03-05 04:42:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4b496cc-4f6e-3c9d-97da-274758f8707d | 4.53404 | -60.57059 | 2026-03-05 04:42:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f876d1e4-8590-30e6-8290-75f9f01eb6d1 | 4.96531 | -60.26214 | 2026-03-05 04:42:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 150c6cc2-0e9f-3b29-a2b9-88a6eb7d1bc4 | 4.54248 | -60.57897 | 2026-03-05 04:42:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dab154b6-aa18-370d-b0a4-c55354f4f769 | 0.66871 | -60.30903 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93efb173-2cfc-33aa-b1bf-a9ab39db84ee | 3.03398 | -60.82595 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8c6c7ed8-b660-311a-89a2-538cfe7dc8b7 | 2.69568 | -60.70859 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ccd0f9ed-09b9-3bc4-b38e-982c079f2f2b | 2.78071 | -60.34365 | 2026-03-05 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| fdd8be86-564e-3218-b2df-1beca84cbfe7 | 3.03301 | -60.81925 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 078fe71a-7dc0-37df-93f0-2e621043bc5b | 3.28429 | -60.72559 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55610d15-85cc-3cdc-9844-22871772e75b | 2.78849 | -60.34889 | 2026-03-05 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 11f5aa25-fb83-3042-b8f7-d58fa19d7633 | 0.47289 | -60.32113 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2961646d-b070-31e3-b55e-5e34ac27f9ac | 2.70062 | -60.69431 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c918af72-cc88-3710-9e49-03905d4f788b | 3.18775 | -60.5728 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1163e887-34fa-38a4-889f-aefb80cdbe78 | 2.98943 | -61.04374 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8ccc94cb-4f90-38d5-8b9b-91e21e723924 | 0.76965 | -59.89842 | 2026-03-05 04:44:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2af7493a-60a2-3548-96e6-4ccd2fbb6c55 | 0.7687 | -59.896 | 2026-03-05 04:44:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5dab193-01da-3057-b6d8-256df9600e78 | 2.78755 | -60.34256 | 2026-03-05 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 31c0bf3f-1ff7-3909-a4ff-d0c431ba6398 | 2.72379 | -60.67239 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa5dcb70-4957-34dc-ab69-114aadfeaf70 | 0.66208 | -60.31015 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7529eb4d-2b3c-3fe1-916c-0f36987d6fab | 2.78662 | -60.33629 | 2026-03-05 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 05c3abe7-8d5c-3f41-9e5a-0e684287d725 | 0.48042 | -60.32578 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e886d369-0d41-3dc9-81a5-8adb447d2c0a | 0.48133 | -60.33148 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 134abee1-bbf1-3fc3-ba48-d9be088d1085 | 2.96186 | -61.10537 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ac2f9c0-722b-3796-a530-c49c25d374b9 | 1.08257 | -59.25598 | 2026-03-05 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d88ecf12-f4e7-3993-99a5-5bf488df1674 | 2.69377 | -60.71072 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 81d44efc-d816-38a9-8bbb-f9f5af704b74 | 2.2289 | -60.23023 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 627b47db-fdb6-3949-bff1-7067ee0db9bd | 3.28252 | -60.74136 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e2ce829-5326-3445-a302-b5db824c81ab | 0.05128 | -60.99209 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4f83b6ca-df21-3c99-a352-1f90121491c6 | 2.97175 | -61.04076 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2313d56-50aa-3ce0-a17a-75d2a5504d5d | 1.50709 | -59.91881 | 2026-03-05 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1d679019-9808-3d15-99e1-182050469449 | 3.02693 | -60.82708 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a5e64df6-053a-32f5-ad62-010756d7a076 | 2.77887 | -60.33123 | 2026-03-05 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7b15d70d-32ab-3f67-aadf-c89da35492b0 | 1.50536 | -59.90737 | 2026-03-05 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4faebeec-61ef-3e61-bbc6-86f899a957f5 | 3.06269 | -60.63093 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b016faf-7bd7-3994-a23c-e6b1f83d1d4f | 3.0279 | -60.83377 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 600688de-d150-3e8a-9304-d507d8f60d54 | 2.99554 | -61.03566 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb8e5b85-7423-383a-acda-a15a75ac3343 | 1.50804 | -59.91265 | 2026-03-05 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0060a9f8-1f69-3bab-8114-e299c269dfde | 2.96801 | -61.04717 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04b0d558-cf27-3e9e-9702-4df1a5e1ecbb | 1.50622 | -59.91305 | 2026-03-05 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| edfdb0e9-7a00-3fa4-8b36-11e101c327f8 | 2.78257 | -60.35615 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 84ce3e38-1c7f-3f4d-a0df-99f7fb586f34 | 3.07066 | -60.63643 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a3f8452-6418-3f85-9f01-c9c71309f2ca | 2.68869 | -60.70959 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5d81e8d6-249c-36cd-adc9-116e31eb30df | 1.51266 | -59.91128 | 2026-03-05 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b40ddba8-0e32-31d5-bf92-2c8404e8cb08 | 1.50714 | -59.90699 | 2026-03-05 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6f311dcf-8558-316e-9074-938f6ef25c1e | 2.96492 | -61.09182 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03208376-563e-3b27-a1d9-607dadc369f2 | 2.69279 | -60.7041 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 50bb5a8a-eac0-3f63-bd2e-b68d3b6a2d1e | 2.9884 | -61.03679 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 586930c6-745a-3458-9c72-94d49a14bf42 | 0.66118 | -60.30444 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ed45466-0375-3ad2-b873-22121198c4ee | 2.96598 | -61.09882 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d0135eec-0e7a-3669-9875-ea3e7043202e | 2.77979 | -60.33745 | 2026-03-05 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ddbb3af7-ad9a-3327-a34e-9f582bbbe0da | 1.11178 | -59.19599 | 2026-03-05 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f354c98-1bc4-3be9-a941-1ad259e64b59 | 0.30722 | -60.4614 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd453968-5e4b-36a5-b603-bc89aef60983 | 3.03062 | -60.83356 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f94de350-6675-33a7-8ab6-031d6dbb9b86 | 0.30058 | -60.46263 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74e12929-be68-3fde-91b0-25aab678918b | 2.78571 | -60.33018 | 2026-03-05 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4fb5147f-1ad4-3c7a-bb86-bbcf72915011 | 1.51181 | -59.90561 | 2026-03-05 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 42afd2ec-09b3-3507-a2f0-6458d01a5831 | 3.02859 | -60.82019 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b9006a20-87ab-371c-9c86-92dec723bf6e | 2.97413 | -61.03902 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9b609a0-cd89-32d3-b2e3-0ce8baaf1df3 | 2.22798 | -60.22409 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d07719e5-559f-3c94-8d78-200a984b10c0 | 2.69465 | -60.70193 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e5aa39a5-58a3-3589-969e-71b8c2755ddb | 3.28523 | -60.73229 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1c950e9-081b-38fa-92f6-e3b3de8b40d1 | 0.05023 | -60.98558 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d5eda9e3-08e6-38fd-9964-7bc5edfbc51c | 0.04243 | -60.98072 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README6.md)
