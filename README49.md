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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c31f7f2e-cccd-3744-97e9-065e709d9f1b | -8.28967 | -55.10938 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 312ad68f-a590-3642-85cc-a3c7c9acb607 | -9.83894 | -48.48713 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8939d882-4d0a-3982-96b2-c5bf251057d9 | -9.85392 | -48.50032 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d44b9055-1c27-3cf6-874f-0e55ec7a87a6 | -10.07144 | -49.12927 | 2026-09-24 04:46:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c32857b-4909-306f-b8ee-47c8145181d8 | -10.91161 | -53.95508 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8034df3-3587-33b6-9733-d5cf53733ee2 | -12.41726 | -46.94667 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cea9020-e2a4-3314-a472-bbed19e07e72 | -10.71816 | -48.72572 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b58ad4a-fff0-3889-8e50-fbc17c707127 | -11.32505 | -47.34243 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 868e43c8-0584-3a5a-85a9-e02786150779 | -11.79301 | -51.00115 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2833c30-8722-3f81-ba4d-b3e53e3c7724 | -12.14788 | -50.77877 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72233807-bd99-3241-97ef-d57f44692300 | -6.68006 | -58.57908 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e3baf75-9b9e-3d19-a83d-59df2e0b506b | -10.62163 | -53.99239 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a8338eb-ea78-3a1b-bd9f-7d738f0751ca | -6.46427 | -54.99946 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cdd6bb2-e736-3151-8221-0393d9c4edc5 | -12.11957 | -50.74033 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68fd96de-849c-3924-bdcd-665755565a43 | -11.93567 | -48.22285 | 2026-09-24 04:46:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b468cf5f-44a3-349d-94a6-6ce491d5fd4a | -12.14477 | -50.75536 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9b3cfc5-3a69-368e-9798-0813e4148110 | -5.86732 | -60.162 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a6c8719-f3a8-3102-b786-a939ff670865 | -11.44059 | -47.40591 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9088c4a9-6246-3403-84f3-9715ecb0f73b | -12.12516 | -50.7489 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9b66071-74e0-371c-a805-c234e5f7a044 | -6.68043 | -55.05197 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b623b9bd-6560-3602-85ab-7c562ec7ab9b | -12.41667 | -46.95056 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 507a247f-6ed1-33d4-803c-507e2f47ca4b | -10.08655 | -46.05719 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59917b2a-b932-33e3-ad3a-2b3b01e9d48a | -10.71095 | -48.72816 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ac7bc16-d8ea-3386-9c70-3ba9dbab4b90 | -12.12698 | -50.73778 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e1fd589e-dd5c-331b-8fbe-563e62018ea5 | -11.72204 | -50.75406 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5edbbb0f-059a-305b-8c68-45c73b13436c | -7.4272 | -49.86246 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fde9dbb7-f56c-3c48-b240-1197d4aebd5b | -8.74524 | -44.26081 | 2026-09-24 04:46:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae551eb2-7f36-3613-bc95-044d7f0f7501 | -5.59886 | -60.20666 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86d8db74-161b-389c-979a-b5070b184659 | -10.2658 | -49.96082 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6b38da6-41ed-3680-93f5-ce427ae06ab7 | -13.46289 | -46.25597 | 2026-09-24 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 771fc1e6-e5c3-320e-b542-d51be16d32d7 | -11.92895 | -50.74982 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cad2d821-1b28-32ca-ab54-e640a44c0d5f | -8.8999 | -45.91009 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d41ea07e-ecd2-3c2e-94e5-cdd20e9d01d3 | -11.40425 | -47.39275 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cb491867-b294-33b4-9ec5-c728c714ec01 | -11.40199 | -47.36163 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ca40b39-4cf5-3d6e-9dac-3023b85b223e | -6.63339 | -59.93753 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c456d5d-b72e-3455-af83-75722178eb60 | -8.91826 | -50.88916 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e91af8fd-4f0c-3329-8db6-1bf42a1ee82b | -12.14338 | -50.74438 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fe14ca2-1fa3-319f-8696-71f86963845c | -12.00995 | -50.32221 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dab966d6-2310-3184-8fcd-9d2f8d225af4 | -10.42008 | -49.36663 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 611390fd-1060-3f82-bef9-a3c0f9102f8f | -12.16117 | -50.76196 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc0cae3e-caae-38de-b949-db1a47a0140a | -12.412 | -46.95779 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7615221b-992a-338a-8eab-1d23deb6505f | -10.09008 | -46.05778 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4dada72-328e-337f-82a0-dcd93fae9633 | -6.88516 | -55.56539 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 011f5489-1613-33a8-a789-521a10a2d062 | -11.23008 | -51.38403 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d03a5820-803c-3a45-b564-e3379499730b | -12.41607 | -46.95444 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ff8a4c5-5b29-32f7-9c07-4db13e9bd52b | -10.61626 | -54.00195 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b572d41f-671d-3d7e-b0cf-427bbb3b3ced | -8.30527 | -48.22017 | 2026-09-24 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d67a93b5-60cb-34f2-8f37-a514ca6c71b2 | -8.45989 | -51.49126 | 2026-09-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4e14852-f931-3dd1-ae04-7286c6489f52 | -9.83617 | -48.48308 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0be2e8b3-62a8-3fe2-bccc-494c9216e694 | -6.89782 | -55.57831 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1070ede3-fc8f-30d9-b194-1f5340aeb7ab | -10.24422 | -49.98696 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c442398b-6633-3a6d-ba70-999175bfcc86 | -7.88837 | -61.17177 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e463e9b6-9388-382f-bb60-e4e3bffe5aa5 | -13.17893 | -51.54185 | 2026-09-24 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ea443e63-0101-39ca-b25d-d7e17aa878cd | -11.39688 | -47.39537 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d8b3b92-09b4-3b6c-8735-d7bd67811c19 | -6.00162 | -57.72551 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e114b3a-1d36-3a0f-be58-024a22795bc2 | -11.4925 | -47.34096 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 391eb8bd-76fc-34a7-80a4-1da17cfefbe0 | -11.86426 | -49.95059 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b09e1ca-3498-3b66-b2ea-cd55e5c52774 | -12.14679 | -50.74496 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 865c0619-1269-35a5-a5b7-377ec909f1e8 | -11.22701 | -51.35924 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df27680e-f9db-3c1c-8404-cb24f9048ccf | -11.78957 | -51.00056 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a406e80-80d8-3f04-b84f-c92041047aa2 | -12.41679 | -46.95765 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d9dcf11-92e0-3a69-99a1-80dc9733a0d9 | -9.26312 | -46.24195 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3d820210-8604-3cb0-841e-2323e26fcdae | -8.7852 | -45.8375 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08887a80-713c-32e1-95c4-3e4be9059cc0 | -11.65374 | -43.48491 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 304d7dc3-a0b2-3627-a348-f855ddc9b513 | -5.91662 | -59.92184 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e8ec276-115e-3b54-a909-6a6c550e976f | -8.15362 | -49.54432 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cb59000-3aa0-3920-b05c-78bc2563468c | -11.45106 | -47.63591 | 2026-09-24 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a7fe90b-48fe-3fc5-b038-32bd4c0acc69 | -6.10405 | -59.88167 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 053f46d5-16e2-3192-9c5d-7b6c829c20bb | -10.61496 | -54.00618 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c35a85c4-ad3e-3305-81d2-a1a187c89b55 | -11.2327 | -51.3683 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2aab0ed-a584-32dc-86b3-64b4dee737ef | -8.38386 | -46.29106 | 2026-09-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c837a3b7-405c-3932-bdc5-607c1e9bf398 | -11.41389 | -47.39809 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6dca9d08-8aef-3ef3-867c-bda311786f1f | -11.23466 | -51.35652 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce87ae7c-a0fc-3746-8095-4df31e36e016 | -11.92087 | -50.73772 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 075a3039-f696-3c0e-8f34-39ee24245701 | -7.90196 | -61.1739 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e3c77839-2bdd-3aeb-8139-6151b5c6ff26 | -15.1628 | -43.57226 | 2026-09-24 04:46:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2f3d4ab4-8cba-33bb-b76c-78447b260875 | -9.58296 | -46.51195 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ad78b10-cc96-30db-ac23-d3233f1f42aa | -8.1291 | -54.82267 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| baacf5ab-42b8-348e-a32c-73773fcda26d | -8.75762 | -45.82903 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83ad7670-c98d-3dac-9449-cb7d0a995bfe | -12.53623 | -50.06888 | 2026-09-24 04:46:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2cbed79e-9aac-34fe-89b0-4c38f90d737c | -12.12236 | -50.74461 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a152d44-3a10-3b64-9467-79cf3bae419b | -11.39577 | -47.35661 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a74f1e7-99c5-3ed4-9159-89b477d9b435 | -11.41282 | -47.35932 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7f4b4b4-9d8a-353f-8b0c-0abd54ea4493 | -6.44458 | -59.94987 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bd91241d-3aa1-3655-8b1a-2f1a5472c1d4 | -11.12803 | -48.32881 | 2026-09-24 04:46:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab053da7-a666-30e0-a796-bed97323a302 | -12.159 | -50.75396 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a1d69c70-5033-3d79-953b-8fa380d64341 | -10.61822 | -53.98802 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2460b236-8d27-3e22-9d8d-750d456b724e | -8.46203 | -51.47864 | 2026-09-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a2c7c4d-1058-3b53-b903-26011e8dd7d0 | -10.43735 | -46.26288 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b915ad2-16ae-3184-978d-ffe1e52d6724 | -10.72038 | -48.73329 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac58fd97-6b6a-3b30-8001-734ee28b6511 | -9.14841 | -49.95816 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2dcfbac-7e65-3498-9c82-42597e24af03 | -8.24428 | -48.21758 | 2026-09-24 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13a89028-810e-39ff-b572-ee2eaa563211 | -12.14558 | -50.75238 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f1fa7e97-5e1c-338e-8d85-694c2c02dbde | -12.70514 | -46.99779 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d4e997c-0220-3423-aac9-e5f6e9f84306 | -11.41223 | -47.36316 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a49510df-c92a-367c-a7e6-4bf234125afa | -8.3098 | -46.88079 | 2026-09-24 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28e171ea-d044-3889-9737-460736c5819a | -10.09655 | -46.0629 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f68ee8f-fca6-321f-9a27-58578b12655f | -12.13455 | -45.63032 | 2026-09-24 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c4f2ed8-4960-3518-8a70-f2c704c6e566 | -11.79364 | -50.99736 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80a7bcc2-51a4-3c28-88fb-c9c91770f033 | -12.05016 | -50.28799 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README50.md)
