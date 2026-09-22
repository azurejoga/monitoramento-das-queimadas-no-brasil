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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cb218fa-dd31-362a-926a-7ae4e7c84394 | -9.62183 | -43.93423 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d64c73b-1396-395f-bcea-3763d07b008d | -9.02385 | -44.91042 | 2026-09-22 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4b753e3-f763-3d59-b820-2d181c127ed3 | -5.74914 | -45.0844 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3e6b06ce-daf8-3c94-8e8b-f6712a56c2b1 | -5.81042 | -57.7342 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db487879-11d5-343a-9abc-4c86186b6233 | -4.41801 | -55.24076 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e9a77a2-f063-3021-ba7c-2b1a853ce931 | -5.84696 | -49.78386 | 2026-09-22 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b567a782-0f00-36de-9b3e-0eee8a272fcf | -3.05502 | -54.41653 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c3cf00c-b543-33c2-9dc3-9b38710101b2 | -7.08393 | -42.07368 | 2026-09-22 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8b80834a-4c67-3391-8ea0-c9d0c24212f8 | -6.44595 | -48.45827 | 2026-09-22 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 850e2b9d-03bc-3c47-b96a-59fb7a438770 | -5.8332 | -51.70688 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ce43670-4331-3a57-b60e-80d6002afe13 | -3.06397 | -54.40865 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30c1d176-9e4f-36f8-a068-5c60e3c8a4af | -6.10339 | -57.68319 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a8d181b5-de86-3674-bb5b-45f4dc506492 | -6.3104 | -60.01522 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31652abe-7656-3832-b084-c1c6cf10e4ea | -9.66457 | -54.33224 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c888a10a-d699-3098-9685-924d8f2f9864 | -8.25956 | -55.295 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2aaf83fd-c18d-3b58-b9f6-8bcd7b38d040 | -6.74973 | -59.06328 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7951ff4c-66c5-3dbd-9a64-0c627fac154b | -10.84109 | -50.15278 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea318abf-1356-3776-abf1-ed76d62ee465 | -5.43672 | -60.2304 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eacfa617-58a2-3d56-a946-ae46fa255036 | -5.89849 | -52.09244 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5268482-91c1-3d60-94ca-7892c64d23e0 | -3.16146 | -50.82145 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0f7faa1-fe28-3ff7-a390-2cee258ca503 | -6.05995 | -57.86941 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3353f540-d187-3abf-bd5e-b811fd69e312 | -5.98905 | -57.69836 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7443cfac-b01c-32d6-a2fe-8b347e68dac2 | -11.3848 | -46.78844 | 2026-09-22 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c85eb33-ef04-3047-ad2b-b5718f7214b0 | -8.60646 | -54.60823 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c9e71711-e2b3-35a6-9eeb-a58650248dfb | -6.74506 | -45.45933 | 2026-09-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 516883de-c1a5-3e1a-8e3e-6b12cc3faaec | -9.68319 | -54.32729 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2b66844-a0e6-3db4-8544-aadd7bc8321f | -3.44964 | -50.61354 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d1aa4690-b0cc-3426-b4aa-2d7f67c25f6c | -6.63908 | -59.92779 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 0c5caabb-cd72-33f7-b7b3-ccbaea682e38 | -6.22878 | -55.61645 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c99fa79d-ae75-34b5-8820-304afef681f0 | -6.62772 | -59.93227 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f7e0dc1d-f8f1-333e-802c-f0eaa1c74827 | -7.19813 | -46.55706 | 2026-09-22 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b2b2ee1-04aa-38e2-8546-dad0d0edf804 | -7.58057 | -57.67038 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e4d2f02-470c-3e9b-bb85-315e412be6da | -7.42211 | -49.83578 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 847802d5-adb6-3d12-b74a-039edd87117a | -5.87401 | -51.94514 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3adddd7-3c40-3dd4-ba6e-ed8d2c73a14c | -5.89071 | -52.09854 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e2efc1a-e96e-3a38-84b9-0cf79fcbb4d9 | -6.75587 | -59.11351 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4363a799-accb-3763-bb04-b3968e1a662e | -7.8714 | -54.73467 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed73cd7f-0b10-3c56-8edd-46a3358b4f5b | -6.19992 | -57.77953 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae160eee-6275-3c41-b498-7951356c2480 | -3.7719 | -61.19642 | 2026-09-22 04:46:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67c5c0d2-cf2b-348b-b382-6d6210854fc5 | -6.67796 | -47.73433 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75c3a171-b5dc-3ed7-926a-0157a8a47e03 | -7.58994 | -57.66768 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5db9c9b2-1ea6-3a51-935d-fa903a325f3a | -8.25881 | -55.29943 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 8df3a226-4170-336d-9a1d-79958caee7fb | -8.31527 | -46.86684 | 2026-09-22 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d635855-e579-3b0d-aeea-ae6b7cdff205 | -4.0151 | -49.17806 | 2026-09-22 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25740c4f-2104-3638-9ef9-c1b002a45910 | -9.87846 | -55.72468 | 2026-09-22 04:46:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65bb7345-e777-3c75-89ac-abec4b7372e3 | -8.62222 | -54.6233 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3891f7d0-d824-35fe-a550-7a22307c44d6 | -5.80267 | -53.51923 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 048ed1cc-9a86-3afa-a590-7d34e5dee2d3 | -6.64238 | -50.06932 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e605e529-39e6-3371-8141-b3b3b81bed26 | -9.72002 | -47.77006 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bd6ed23-4453-3801-a726-3efed5f9968b | -9.69075 | -54.32457 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9223ef90-3e08-3bd0-a729-a6b720302a9d | -3.36022 | -50.44517 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ded5882-3fc6-346a-97e3-a703067131b3 | -6.30958 | -57.7467 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b222024-a378-3418-8502-0c3b582b6947 | -2.41876 | -58.27498 | 2026-09-22 04:46:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad53fdb8-03c6-37ca-a55f-e0384b81dfc7 | -9.59517 | -47.77744 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1b0345fa-d2b8-3a55-a518-71efbd21b6b3 | -3.46114 | -58.32408 | 2026-09-22 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| baa324d6-2de5-311a-9e0c-c0e59b529228 | -6.42229 | -55.01824 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47def34e-5459-352c-8a1f-858c5e6aa15f | -6.29204 | -57.74998 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6297078e-1446-319c-8e88-719cd9f8170b | -7.94548 | -45.64731 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23d3098a-4133-3824-a3c5-add7e0445647 | -5.15417 | -48.88459 | 2026-09-22 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddca9b4e-4145-3bc7-a759-a6c489e18bee | -3.06768 | -61.27092 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c38c6fe9-59b1-3ff1-b2dc-a1eb104ce90b | -7.89509 | -44.84956 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3458714b-cf5d-3c82-9ef0-b870170a0599 | -6.78322 | -48.66814 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d9b2548-a096-37f5-874f-45c0374439f2 | -6.2711 | -47.57824 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d278c12-dc50-3624-8b9c-e9fac13ef499 | -5.87629 | -52.03856 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de695b75-910a-3776-9b0d-645ad3283974 | -4.1835 | -49.40907 | 2026-09-22 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f67b999-8f1e-3144-8a53-4c4b0906ff73 | -6.64879 | -59.93277 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dab1c52-4906-37d4-9178-0d9c0df3853a | -3.45071 | -50.60667 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a3a8be0-1e52-3423-bf58-403fcc5903bd | -3.44357 | -50.60908 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f3bbcfd-5f2e-3923-aadb-a62fea3976ef | -6.04423 | -57.82508 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4ce8ba06-7a13-3d93-9491-3283744e3bc2 | -3.67261 | -50.94787 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79773b03-c242-3758-bcf8-d3e07152e67d | -4.45122 | -55.43504 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31737522-b42d-374e-a51a-610b751fbe1f | -9.67437 | -54.33776 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0d571d68-2af5-3bce-898e-1319a0a2ea4d | -3.50587 | -55.48532 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcf3cbd6-a6df-3e09-911f-747bb1688e27 | -3.97278 | -59.6344 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c63517a4-3926-3b0c-bd78-f406dc73a65a | -7.36599 | -44.27113 | 2026-09-22 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a2c1494-c717-3f73-bb2f-6d4010913bfb | -6.38085 | -60.01625 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f62b2cb2-a975-3a02-bd2b-fc989fb87049 | -5.37342 | -56.0513 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 866b42cc-613b-3e38-b23f-50c9f2d1e907 | -3.22589 | -53.948 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| babc78b0-9662-3a25-a802-a9064d46aba2 | -5.84209 | -53.5294 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9bb4d23-18f5-3cc4-9041-bff4f299008b | -6.25421 | -57.78427 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8267a9e-8ddf-37f2-8394-d70288546139 | -9.6183 | -43.93971 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ee5e3679-8169-3878-bd55-c64ff64504ad | -10.09798 | -46.08846 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5654753e-f382-32e0-a25a-a4a0a2dbe5f7 | -3.48722 | -59.57172 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 719d5f0d-d55d-333b-98b3-8214275fcf6f | -3.44464 | -50.60222 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ce9d2be-e47f-35b8-9d35-071dfd8a38e3 | -5.42351 | -45.68909 | 2026-09-22 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba52169f-11fc-3e26-af09-9b8c67da468e | -3.89646 | -60.5924 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b071b164-6b2a-322a-b41a-50dbea2a30e1 | -10.4677 | -46.29059 | 2026-09-22 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebc8de89-268f-3c1a-a81b-001cfbca6324 | -10.4979 | -51.28028 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b40f658-c98a-3824-9bfa-3a6682a5fd97 | -6.55451 | -56.03798 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68d6daee-90e4-39ef-b4da-dbffbd4ffa45 | -5.99785 | -45.24507 | 2026-09-22 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c1e941c-6f3e-3ce7-ba0e-6319137ebe25 | -5.83128 | -53.50791 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4e80d87-be3d-3ecb-856e-6ecaa75941ba | -6.93962 | -42.91539 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c4b794b3-5b07-3985-b523-a1955c73f988 | -10.68735 | -48.72239 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdadc1b1-10c5-3cbd-91c7-963627c417cf | -7.3414 | -49.55996 | 2026-09-22 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9590b7e2-4a69-3219-b7e8-e5336f392623 | -6.36121 | -58.29271 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc9730f4-96e4-382f-9f68-aaa01bb6d4fd | -6.83918 | -55.53527 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e4deab1-76b7-3cbc-8f53-58206d46684d | -10.26404 | -49.98254 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7116946-e3ae-3543-82e7-f14cb5a01eb1 | -6.72704 | -55.08064 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a79e2d8e-bae3-3013-9739-54ad5ebe9643 | -3.38823 | -50.43894 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c359529-7b70-33c9-9d39-139b4fbbbea2 | -10.83591 | -50.14032 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README62.md)
