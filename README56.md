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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 121ad6a3-8678-39f9-9fbd-1fabb0e4c267 | -15.35842 | -53.79407 | 2026-08-29 04:55:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd6d7534-9b5d-36cb-b417-43666d4ee0c6 | -20.94722 | -57.58327 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f2cfc838-7fac-3fa2-a4d7-c9de9c6eefaf | -14.18705 | -48.75632 | 2026-08-29 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 887152c7-bde5-31c8-840e-7ce921e500a8 | -14.90621 | -52.6166 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c640e818-81cf-32b0-8fb6-8b6a19694210 | -13.86403 | -54.12268 | 2026-08-29 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77fa5876-1aff-3a54-bfdc-869f0fd50784 | -14.17804 | -48.76483 | 2026-08-29 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a197a36-fbcf-3942-8bd0-2d159d5f8d7c | -14.20663 | -52.83463 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd330026-7043-3e99-ac8e-18bb6be388b0 | -19.2224 | -57.66876 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f8966453-4bf8-3ca1-a165-8d34038e73d9 | -14.84713 | -49.21845 | 2026-08-29 04:55:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 465d3316-101b-3ff3-89de-00557f76c267 | -23.23128 | -49.354 | 2026-08-29 04:55:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d8d744d4-6252-34b2-94d7-a415c55358fe | -23.15521 | -48.66813 | 2026-08-29 04:55:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2aed81e4-c9b9-3f95-b6ec-db78c068faea | -13.47772 | -57.05278 | 2026-08-29 04:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3061e860-e91e-3100-970d-9b44d09c1d39 | -14.17408 | -52.8256 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42402353-90d2-3654-8bf9-7b99bbf5e6e2 | -15.6486 | -45.91577 | 2026-08-29 04:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d97d132-06eb-3ec7-97f3-b585bc3d7375 | -20.93959 | -57.56415 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 7b1b570a-3baf-3349-b365-d50d26a83ea7 | -14.20496 | -52.84527 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e81770af-80dd-382e-9d47-1aff6ca778ab | -22.2565 | -47.52021 | 2026-08-29 04:55:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 820a4a9e-3221-3d21-aa01-2a6b3c2b3ebf | -15.64613 | -45.9353 | 2026-08-29 04:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2077bb87-586e-3e80-9e47-640d167aa333 | -14.1746 | -52.84389 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0068f699-691b-31e5-88d2-4e24dc46e009 | -14.75275 | -48.75316 | 2026-08-29 04:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6281fc2-1018-3bc7-87ac-e32a25f326b7 | -14.44203 | -52.61065 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a97cf71-5fca-3265-8bd0-241a6a10da19 | -14.15473 | -52.8406 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05788acc-1072-32a3-926b-164ac18ea6a9 | -23.15084 | -48.66781 | 2026-08-29 04:55:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0cac2f3d-1568-35b6-84ac-d3b0a2bcc154 | -19.22672 | -57.66556 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 377c740b-7d4a-328a-bbbe-41cb71881ac3 | -14.18774 | -48.75148 | 2026-08-29 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7657e7c3-6adc-31fa-83ef-b01c6b3e145f | -14.20552 | -52.84172 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86bffac3-2612-3aec-b9a9-590ab25fa9aa | -20.96325 | -57.61732 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 577e0c84-7a06-3739-8671-3f5c28075d38 | -20.93383 | -57.57619 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f4bd526b-e43e-39b4-8868-960ae003776c | -14.27291 | -57.04229 | 2026-08-29 04:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c2d86c-f5c1-3e85-8a36-15a71838e02d | -14.43871 | -52.6101 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9487bdca-2d3c-3c28-ac8f-ead55470ee24 | -14.41329 | -52.57669 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1904028-3ba0-3768-b460-3e6cc47b2da2 | -14.41385 | -52.57312 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6945d944-76d9-3975-b57d-bcd622f928f6 | -14.15197 | -52.83651 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3829564c-8290-337e-b60c-727ceecc6fea | -14.20109 | -52.84827 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 778846a4-1dbb-371b-8bef-d38e4d394427 | -20.9303 | -57.57547 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0004d675-8619-36ca-b394-4ddff6309687 | -14.89126 | -52.6251 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8efd679f-9852-3a06-8fba-5d46ddeeb53e | -14.15142 | -52.84005 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ce74beb-3b64-3a76-98a9-62382e8c9af4 | -21.7098 | -47.14516 | 2026-08-29 04:55:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ea97246-a029-340d-9040-d00bb86312aa | -22.31372 | -51.88822 | 2026-08-29 04:55:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2a579537-7661-32ed-8f20-cf3038140cfa | -14.17847 | -52.84089 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d51dd3d-d209-3975-bd05-b0996d48f6b3 | -20.95076 | -57.58398 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c08cc536-228d-3c14-b985-071e5b0010ca | -20.93179 | -57.56698 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 7f5e2ce6-4acf-3dd4-8fd1-123369548f7b | -20.9409 | -57.5776 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 03ceb62e-2ed6-35cf-8fe8-bb72005338e0 | -15.36812 | -52.68081 | 2026-08-29 04:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f7b4700-9fb4-3df3-8967-710cfb2d0fee | -14.16247 | -52.8346 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d3ff456-9120-3c14-bcd8-ff521c6b469b | -15.44401 | -52.80378 | 2026-08-29 04:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c915b922-8779-3a4d-91cf-67b79bada959 | -19.22335 | -57.66221 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 77c28301-e0eb-32cf-9488-9586d3461fba | -14.9378 | -56.32456 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aad11ef0-546e-336e-80c0-1a0b127cb09d | -13.4596 | -57.04452 | 2026-08-29 04:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3b1cbc9-1edf-3f0e-aa98-c8e1a7e7795a | -14.39894 | -50.05994 | 2026-08-29 04:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f840d85-4d50-3ca9-96aa-a31735d816f4 | -14.76043 | -48.75459 | 2026-08-29 04:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec5de531-2d4e-3158-8eb3-76a5307340a9 | -14.90399 | -52.63086 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfdb6235-a752-3387-a408-9f6f4d9c2504 | -13.47266 | -57.03713 | 2026-08-29 04:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e8117c4-c544-3faa-b9db-1d8b14ce69cc | -22.01796 | -55.98061 | 2026-08-29 04:55:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f29a7148-74de-307b-ad17-efd31eec7337 | -20.94443 | -57.57831 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a256c626-de5f-34cc-a0cb-8b09eae9a3c9 | -14.90373 | -47.74132 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6bf940e1-72f6-3dae-9294-e9485fc42b6d | -14.89829 | -56.33914 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 861d1cd2-3978-34a8-abea-050c80c78432 | -14.16634 | -52.8316 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31cc7e19-4d1e-3d4f-8af0-110d49a04106 | -14.19997 | -52.85537 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8e81453-bf5a-3200-9d71-42c5ceafbb02 | -20.596 | -56.99088 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c591e2a-9f07-3f11-aa78-8f6b0f73704c | -23.23542 | -49.35472 | 2026-08-29 04:55:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 89cf19c1-810e-3a3a-93e0-d83c85f351fb | -23.19986 | -46.86413 | 2026-08-29 04:55:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a309a7d1-22be-33eb-b0e1-115e05da37fe | -19.22619 | -57.6674 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cb5698ef-566f-3fd9-9170-d9b1a918a61f | -19.22545 | -57.6716 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 93413d4b-62d2-3682-a0b6-d9a45d56fbfd | -23.20161 | -46.98689 | 2026-08-29 04:55:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9b4f9f92-9d74-378e-8a1f-648652e87874 | -15.37494 | -52.67834 | 2026-08-29 04:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7dd4fc5-de26-3815-9d36-d33491eb3c76 | -14.20332 | -52.83408 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8f34dfc5-5ec9-3b76-b47b-08644df9ed7e | -14.2044 | -52.84882 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93aa0861-0529-3918-8220-b5baf5a5b9e9 | -14.92226 | -52.62291 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8187abdf-b8a5-3ea1-b011-b4b6f44c66c8 | -14.17184 | -52.83979 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9dddb8b-1a39-3575-9bb3-60f83c2debdc | -13.64105 | -51.84953 | 2026-08-29 04:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2044593-7f30-3693-90c6-880ff5024d95 | -14.89544 | -56.33425 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0805ddb1-2b68-39ea-9c64-a94a6c85c4db | -14.756 | -48.7467 | 2026-08-29 04:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2ca85ef-7291-36e0-8886-9bb4d39b3af0 | -14.41661 | -52.57723 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba9045c5-288f-37e1-9c02-1b5c41fc8ae7 | -14.41431 | -51.7399 | 2026-08-29 04:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b2ab459-5238-3765-a649-104195909dd0 | -14.42878 | -52.58652 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a650101-25ee-3ab4-b23e-3b191c2402d1 | -14.26917 | -57.04156 | 2026-08-29 04:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e12d238-c4e9-3c1a-80ca-61e781118cd3 | -14.41094 | -51.73936 | 2026-08-29 04:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7d9bacb-f6a0-377c-b808-d640bc9bd96b | -26.57388 | -51.51242 | 2026-08-29 04:55:00 | NOAA-20 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b5c68469-bdda-3e4b-9de0-97e34657da78 | -14.17424 | -48.76411 | 2026-08-29 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edab9ac8-3562-3bcb-8398-1eb1cc3c931d | -14.91285 | -52.6177 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e88d37f-2918-3b79-822c-eb046a41c145 | -14.4321 | -52.58707 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f195d219-510f-30bc-8728-fef6e002414f | -19.22049 | -57.65717 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ce348622-121d-322a-bde0-8c8a6a8bca36 | -15.65571 | -48.3719 | 2026-08-29 04:55:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0beed358-02af-3b51-a89d-640726adec96 | -20.95281 | -57.59319 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 683673fe-fb75-37ee-9bc5-678662c00af8 | -15.64735 | -45.92567 | 2026-08-29 04:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 88a55f44-de57-3dd6-8fd7-0e6912005967 | -14.75726 | -48.74892 | 2026-08-29 04:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1187aa84-9602-34a8-84a4-47563d6dcf64 | -14.40424 | -52.57174 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95c07461-060f-37ad-b81d-d529685e32fb | -14.16689 | -52.82805 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb94809b-2c5c-32e0-bf03-d5a5b47716a9 | -19.22693 | -57.6632 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 59b7d873-1a15-3e38-a51f-f4565a2e50f1 | -13.42514 | -54.01931 | 2026-08-29 04:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6a64542-2c4a-31a3-93dc-61e997b1f0ec | -14.16578 | -52.83515 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 340aabc5-b804-3ebe-9329-2b4dcdfdd571 | -14.20607 | -52.83818 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f90ccc46-2cf3-3bf7-a212-5eb2240ff59a | -14.89902 | -56.3349 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d829a890-469a-3f77-9e2f-0ad9822d38f7 | -19.47306 | -57.57059 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 27becc23-2a78-3e22-974c-d3189825e6d5 | -13.47182 | -57.04184 | 2026-08-29 04:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faeb8537-8958-30aa-a95f-f924ab2db605 | -20.94797 | -57.57901 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 29bec419-81e2-3ac2-84a9-c7e85f1c63ac | -14.18948 | -52.85728 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71c100ec-2c67-3102-a445-80f1fd19c704 | -14.30114 | -51.70339 | 2026-08-29 04:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8963cc8-9b97-3997-b5e4-98e04c207122 | -14.20328 | -52.85591 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README57.md)
