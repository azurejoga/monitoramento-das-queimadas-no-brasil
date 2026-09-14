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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 184f4d2c-5a5d-399c-aafb-89b50fd19daa | -10.65217 | -54.14652 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 68bf8d19-70dd-3d62-aa95-ea524c3e462e | -8.37776 | -50.72178 | 2026-09-14 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cee7042-e049-3efb-9ae6-8bd011227faa | -11.05285 | -49.57471 | 2026-09-14 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da1ac582-4359-3782-b7d8-0eabc7028e5e | -6.32406 | -55.17945 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8b8fb68-895d-3b90-81e7-f77fba7c19ca | -6.74009 | -50.92667 | 2026-09-14 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d7a7460-851f-3dbd-8737-ade133904e56 | -7.47134 | -49.78332 | 2026-09-14 04:53:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0dd123e-301d-3b38-881c-f4bdb1785104 | -9.37726 | -50.2073 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c536bb7e-0e14-3ef5-b8f2-59248c58c564 | -16.48275 | -43.4233 | 2026-09-14 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c4cddcc-a8bb-3a4e-9328-3b70c59c9117 | -7.29617 | -46.7552 | 2026-09-14 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d408ef71-e91f-3590-ad62-0abe31378fe3 | -9.39711 | -50.16878 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 870a0a4b-fdcb-31c3-8a5e-64dfe0e195c1 | -9.13469 | -51.57048 | 2026-09-14 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63c6f107-5bd6-3e70-8136-b061c86fd0df | -9.71353 | -50.84268 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f026a499-b902-322d-b57b-a09330430259 | -5.61794 | -45.249 | 2026-09-14 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe19df9f-7bcc-3a44-bfec-5a096898a02c | -6.87082 | -55.29737 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b947b79-c574-3738-8cc6-0bf64e1e52c8 | -6.7394 | -59.43521 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b46c8470-03c8-31b3-93a4-e70ffe3f2e7e | -5.75968 | -44.05599 | 2026-09-14 04:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43982747-6d6e-368f-b816-ed67185551ea | -8.54291 | -54.69995 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e416bda8-eccc-3a85-81b8-757a8a5fa9a4 | -7.15517 | -55.31491 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d0789ae-4b31-3ea2-bc63-f6c65e16e057 | -9.12202 | -51.58631 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfa42539-d008-3f35-b57a-793ee912b8b3 | -9.5547 | -51.36197 | 2026-09-14 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3c0f3a6-3d3d-3b31-a906-c3514ed28336 | -10.67246 | -54.14939 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a2311bf-546e-33ed-8e90-a4f1a8246f7d | -9.12533 | -51.58683 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b327789-3b87-3ee0-ac0b-1a4619d3c4cf | -11.22728 | -46.43216 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6dd0078-1ab0-3685-a9c2-ee6220363271 | -5.5925 | -60.1873 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bada905-7fc8-3449-be96-7c49b2423335 | -10.6622 | -54.14763 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b6c47ab2-06df-3e5f-ad04-273cab40411d | -3.35568 | -59.62464 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f9b07b6-8dcc-3be0-bb59-3b51d86f64f5 | -7.86836 | -54.72175 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b263062-0540-34ac-87c0-0b71af9c9c54 | -10.76724 | -48.97151 | 2026-09-14 04:53:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c63750da-15b9-3739-a46b-b96cffefc1b6 | -4.13224 | -54.01013 | 2026-09-14 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 954e2057-b45b-30c8-bb49-67b197a23946 | -15.55344 | -48.78976 | 2026-09-14 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd338f90-068f-3dec-87e4-2def303c59a6 | -6.11036 | -57.66513 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 32d0871f-acc9-3945-9799-720302f2ea57 | -5.75898 | -44.06081 | 2026-09-14 04:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eae7a97a-a879-3b25-8f75-3b837caa37fd | -11.83508 | -46.38981 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9b777fe-11fc-34e8-84c9-c0d960151dae | -9.44583 | -50.12693 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3999c951-42eb-3784-b325-a367b74381e2 | -5.59193 | -60.19065 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de2136c9-1870-3f58-881b-9c022af33499 | -8.82734 | -47.17965 | 2026-09-14 04:53:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eb67e09-b9df-36dc-b30a-86d60de77144 | -10.6793 | -54.15055 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 967b8a63-5f51-3ab6-bad5-12aaa882ed60 | -5.11972 | -55.95657 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30f998b2-d748-31f0-9a5f-37f06d0e351f | -6.31133 | -59.96195 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 722b386e-744e-3cb7-9796-26ee2dd0243d | -6.31022 | -59.96819 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4c22624-6ccf-309d-b505-cbe4c2c10b65 | -9.45958 | -47.85142 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c588042-eaeb-3e13-914f-3a2f555110cb | -3.59817 | -59.07872 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe75ef45-0a8e-3882-85f4-d6c505634621 | -6.31782 | -59.98547 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb22a86e-6483-37b3-9053-ed1633069a38 | -10.11157 | -49.03514 | 2026-09-14 04:53:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08ae8ce3-4b04-3761-9b68-16ef4364b983 | -11.21082 | -46.42556 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adf1ce26-a3fc-3d82-bfaa-0e72408aa34d | -9.37612 | -50.16931 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 05185673-9924-346d-92cd-cf8ab13cdb9c | -7.86906 | -54.71755 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9249605a-90a6-36c4-9271-6aef4065761a | -4.34519 | -54.78302 | 2026-09-14 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f5f9795-803d-321e-a447-eb28ed663ac6 | -6.2964 | -59.95596 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 814e2fa7-146f-3cc1-8b2b-262895d4ca6d | -10.65095 | -50.70998 | 2026-09-14 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed59631e-ed3d-3a03-9832-ac4928519257 | -16.3008 | -53.84276 | 2026-09-14 04:53:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bda1e3b5-b147-3959-a26f-0a3de9b01e8b | -6.73247 | -55.63566 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fe59ca6-f6c7-326a-a7f6-f8c7c525983d | -10.74629 | -54.08486 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d40be2e0-8344-3feb-abb0-1d65655b00b6 | -3.7201 | -58.87125 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6edcc39-58c1-3e49-94ef-73bed7353605 | -11.26095 | -54.13509 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43865cc6-bb94-33c4-ba32-3a209d2781a2 | -6.11067 | -57.86461 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e489ed9f-87e1-30f8-8e8a-718f842deb32 | -7.09877 | -55.63074 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d44fb237-6890-32f8-8628-32195483a0d5 | -10.07067 | -48.78199 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 531c00f1-8f9f-3381-8191-304e06a106d5 | -10.67775 | -54.13871 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 668bb0e9-01dd-3128-82ac-98c23ca3ce58 | -10.36612 | -46.66716 | 2026-09-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17288c13-e38b-3770-b0f0-24daeb5de698 | -7.53502 | -44.89384 | 2026-09-14 04:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8850e68e-350c-3c2c-9737-093b98eb48ff | -9.70974 | -54.3734 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4a226afd-6e8b-3610-8b31-4ad73dd7e76c | -8.46234 | -50.77129 | 2026-09-14 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 708ca1de-629e-3f96-913c-b356bc7c6495 | -6.23354 | -51.67985 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a2ffcaf-727a-37bf-b83f-f61099b15fd5 | -11.26217 | -54.12761 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c38ac58-5610-3aa7-aaf2-881ab935f9c3 | -9.41815 | -50.12276 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 423d13c1-ad02-34e4-adfe-b834a587ccbd | -6.86781 | -55.29423 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55276425-3b60-3f40-99d2-b8da066b54ea | -15.54503 | -48.79325 | 2026-09-14 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 41d7861c-5ce2-38e7-b56b-81df03d1d0e8 | -5.08206 | -56.25631 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fffc61c-1ba2-3b41-8c64-b22ca5339c5e | -5.13127 | -55.9618 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d7b8c70-407d-38b5-b8cf-c8dfc1dda621 | -10.68086 | -54.16238 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 80d23713-ee8e-3402-8c20-c69a4371549e | -9.44129 | -50.13382 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e82dd065-51b2-36f2-b4b3-84b70617ea05 | -9.37499 | -50.19938 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f3376ab-06b0-3a46-aeec-9fe2461dd0b7 | -16.47864 | -43.42677 | 2026-09-14 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a53d8cce-5dce-3ee5-bddf-52116fbf4d1a | -9.98841 | -59.86493 | 2026-09-14 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 403ded85-e0c7-3636-8ebe-f67d6d7fd631 | -6.29285 | -59.93751 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2edf7eef-88ac-3ab5-8bdc-b775d21e1f64 | -10.68211 | -54.15487 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| ebc7bf9f-dc25-3d41-a654-4800363c8ba5 | -7.10413 | -41.80249 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 156f423d-cb06-3aad-be3d-d42eb45d6ad9 | -4.5346 | -55.61877 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51cff3e9-b2ec-3b03-b266-8989b90e1423 | -10.54911 | -51.29842 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1da3f9c6-c0b4-34b7-9bac-63bc810630a2 | -11.29198 | -47.67917 | 2026-09-14 04:53:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38c3d54b-d5fa-3bc9-87c7-24e74d6cf6ec | -9.40109 | -50.14288 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6eb8162d-b5c8-3a1b-953b-0c39c8c069e8 | -10.18825 | -48.46915 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f33fff55-dc33-39dd-a4a3-8924147ec5d6 | -10.11174 | -48.8606 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc345021-5ef2-36c7-a9ff-3347972ff6a7 | -10.67868 | -54.1543 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| f2d90910-3e89-3a99-bf46-1a3b607ddbfe | -5.85444 | -51.94739 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce1c8463-c5ca-31aa-a9fd-addae3d15070 | -6.74435 | -59.43613 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8544f83-dbc5-3c1c-84be-f9650b54bbb0 | -6.58139 | -58.8526 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5db25c1f-1698-3e18-b062-d8fd28580e90 | -6.3213 | -59.99603 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 430902a7-7ca7-3fc7-ae8f-420ad0555a8b | -10.68242 | -54.17426 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98554e87-154c-3208-affc-7c31e797772f | -10.54689 | -51.31266 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8770a600-6c89-3d91-80a5-878692510e3e | -4.09277 | -54.43261 | 2026-09-14 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79ad0f10-f7d2-3a3a-9969-d266ed091e6f | -6.11406 | -57.67027 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d1544de5-14fa-3acc-91d5-58e9e14e5a87 | -10.10812 | -48.86008 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41982120-1c68-345b-8913-5bcf2a1e3741 | -11.37092 | -43.95222 | 2026-09-14 04:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0a02313-a1b8-3946-88dd-894fe11e47da | -10.19793 | -54.24367 | 2026-09-14 04:53:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 866841df-23d2-3827-8336-9c01db8013a2 | -6.68072 | -58.87561 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea71eedd-6cef-3676-8df9-52f5a00f73fb | -7.09113 | -41.81577 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a7684e0-298a-3e43-8160-8c5b4c38987a | -6.30212 | -55.2894 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce04b8e7-a360-38e4-b9ba-829d4dbd4dda | -10.67029 | -54.14129 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |


[Clique aqui para ver as próximas entradas](README41.md)
