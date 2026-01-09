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
| 9cec0658-1bd2-374f-b7b5-1b597eb744a7 | -5.2881 | -45.82911 | 2026-01-09 04:46:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a58444b3-cb08-34fc-8193-e24991b1e6ea | -6.06342 | -43.25564 | 2026-01-09 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 94294661-5721-3763-90d9-c0d460328a3d | -7.72287 | -45.63099 | 2026-01-09 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46eb65a9-ebb8-30a1-8a23-0d20d8c066a6 | -6.05862 | -43.74224 | 2026-01-09 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4a646a0-7035-3780-bd53-cdc78fdda872 | -7.71892 | -45.63103 | 2026-01-09 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efc6bb8e-d173-39d6-b56e-0786f59032a9 | -9.05182 | -46.985 | 2026-01-09 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb6f3acf-0c31-33f3-acf1-7a9aa451b45e | -7.72316 | -45.63167 | 2026-01-09 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 125b6d34-b33b-397e-8ab9-08c312496f7d | -7.71863 | -45.63034 | 2026-01-09 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b7281e9-0f5a-3e83-92fb-45e240cfe857 | -5.28407 | -45.82842 | 2026-01-09 04:46:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3849e95c-4c8b-35c2-97af-e440a6f7d2b6 | -3.79035 | -54.40718 | 2026-01-09 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b354bb5b-461d-32a3-8f37-99632ea7bb45 | -5.88127 | -48.29218 | 2026-01-09 04:46:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 389eb72e-d046-3701-ab66-a37857635f14 | -6.29071 | -43.13386 | 2026-01-09 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5de8e34e-6ccf-36b0-978b-1f3222a3e048 | -3.58741 | -40.97558 | 2026-01-09 04:46:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bbf85a51-700f-32ab-9832-74b37a8143cb | -7.50538 | -45.55326 | 2026-01-09 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48ba13da-ef1b-38ba-86f9-114517ac2475 | -5.66907 | -46.28608 | 2026-01-09 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1c6bc21-8753-3627-ae60-58b2bd148f1e | -6.56529 | -44.46712 | 2026-01-09 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6519b6d0-ba3f-3869-ab2f-843a4b0cc5a4 | -3.49489 | -47.16815 | 2026-01-09 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41c01605-26b3-3253-8291-3674cc41e202 | -3.79408 | -54.40783 | 2026-01-09 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a97fe36d-07f2-376a-8889-d52b9ab94d9d | -3.58202 | -40.97402 | 2026-01-09 04:46:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 967e82aa-0006-3bf7-bc09-0ce866a357e2 | -5.91764 | -42.65568 | 2026-01-09 04:46:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 87c990e4-02aa-3cd4-a02b-57425a8bbcd0 | -5.89807 | -42.54896 | 2026-01-09 04:46:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be301f25-6cdc-3d56-a461-cd9b4eef3dce | -5.90125 | -42.54912 | 2026-01-09 04:46:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fab230d8-1511-3b73-8b93-64ae4ca80651 | -3.50565 | -54.67543 | 2026-01-09 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90d66fe4-7aa1-3f50-9064-bad6fd1bb745 | -3.85637 | -42.25791 | 2026-01-09 04:46:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c64a978-464c-3952-a174-383397a9e335 | -9.05066 | -46.9863 | 2026-01-09 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a9990d9-911b-31e7-b031-e12d542155e3 | -5.90477 | -43.84792 | 2026-01-09 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c9f5359-3e49-3872-9d3c-f433d17f9ece | -5.67278 | -46.28386 | 2026-01-09 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59ee807b-31b4-350c-8666-288bfa05cb65 | -6.58691 | -44.62104 | 2026-01-09 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ef63c79-334d-36f1-9359-5fa11fd3bb4e | -10.2163 | -50.80135 | 2026-01-09 04:48:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41b26a3b-791f-3814-9f96-1ba106f5e845 | -12.40069 | -58.04992 | 2026-01-09 04:48:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a262415e-6aa1-3bc0-9995-c83d92c5216b | -12.40211 | -58.04961 | 2026-01-09 04:48:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 359dce9d-bd35-3e3f-acb4-35df3ad8165f | -11.83037 | -46.61304 | 2026-01-09 04:48:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab016937-ffae-3a06-b588-d927ea1c1ffe | -10.55133 | -48.72509 | 2026-01-09 04:48:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61f288f6-7c60-3bf2-bd6a-317425f8e2b9 | -12.4048 | -58.05066 | 2026-01-09 04:48:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6f9d8d5-7bf8-3e10-a0fe-0d8ffa7956a6 | -13.48885 | -52.94475 | 2026-01-09 04:48:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8df78c9-34fb-3610-98f2-9b900d344beb | -13.69142 | -52.58371 | 2026-01-09 04:48:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97b06881-2630-37e9-9013-a6db86da9444 | -13.48555 | -52.94421 | 2026-01-09 04:48:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30611e18-4c22-3294-974b-c42090a49fc0 | -13.69087 | -52.58725 | 2026-01-09 04:48:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 259fb75b-6cd8-3174-8ef9-91d512d8b733 | -11.82615 | -46.61242 | 2026-01-09 04:48:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20b28b65-0a9a-3c47-bd4e-fd8e6c2d7b8e | -12.40548 | -58.04689 | 2026-01-09 04:48:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5ed50eb-bbb1-387b-bd19-26bd92ab98c9 | -17.66121 | -56.35887 | 2026-01-09 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 61d54c68-4f16-3af8-bd4f-eb063d3efdb6 | -15.78406 | -59.74198 | 2026-01-09 04:50:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85c89a3b-3409-3be4-a108-dcb2c6d05488 | -16.10767 | -56.75289 | 2026-01-09 04:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daf5697c-f02e-3a55-b54c-e5292d2a9812 | -20.55374 | -57.95385 | 2026-01-09 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e6d748a3-8c5d-3ebe-b42e-c30c47ebacd6 | -15.04511 | -57.83393 | 2026-01-09 04:50:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b82fdbb9-a6bc-375b-9cc4-69c318f0c6e8 | -19.30256 | -55.26159 | 2026-01-09 04:50:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7196b753-425e-38ad-8d3f-226e8b27bc67 | -20.55295 | -57.95831 | 2026-01-09 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c82bf60f-0bc7-3848-8810-1ee074db0dfa | -19.80017 | -57.37518 | 2026-01-09 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 58acc103-d60d-31fa-b739-c3ce95c60a10 | -21.2301 | -56.25114 | 2026-01-09 04:50:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dc091e1d-4eb6-3cff-aebe-c4668f0c2f53 | -22.94595 | -54.17496 | 2026-01-09 04:50:00 | NOAA-21 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 48957df9-2c34-32e6-bfa3-937b569c25ac | -19.57905 | -53.50721 | 2026-01-09 04:50:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4a4220d-8555-3f5f-a27f-f5fd378b8cd6 | -16.10406 | -56.75221 | 2026-01-09 04:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13f33895-3482-32cc-8f99-5bdeb9ac7cc7 | -16.10841 | -56.74854 | 2026-01-09 04:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 748d860a-5b0e-3d2d-8d32-d28aa5d060f2 | -20.55814 | -57.95011 | 2026-01-09 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e12f0ac3-2314-31c4-8e79-671f1a80fc06 | -16.20965 | -59.32609 | 2026-01-09 04:50:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dab90b6-4983-3eba-9287-ab53f526d50d | -19.57849 | -53.5109 | 2026-01-09 04:50:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25de1c5f-12d0-37c0-8348-f646410acb18 | -21.19473 | -56.14219 | 2026-01-09 04:50:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7e5551b-e9b9-379f-a768-8ee5c27e15ef | -21.23347 | -56.25178 | 2026-01-09 04:50:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a877d76c-9c9b-31d7-a50a-37d795f65177 | -17.65354 | -56.36164 | 2026-01-09 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d3778b13-0d18-33ae-9986-21f07606c4ce | -16.10332 | -56.75657 | 2026-01-09 04:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50079568-c7b4-35eb-8b6c-e6c79e75d5b2 | -15.78327 | -59.74629 | 2026-01-09 04:50:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f772ef56-8e61-32b6-a5bc-29e9b3565c08 | -22.74371 | -49.34445 | 2026-01-09 04:50:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43a707f8-66b2-37a8-a2b9-d6dba0916218 | -19.57516 | -53.51033 | 2026-01-09 04:50:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83cb7d9b-dbf3-30fb-9d17-b26375c203de | -16.1048 | -56.74786 | 2026-01-09 04:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7aa96704-43de-3e82-b4e8-9ee590c02e55 | -22.82381 | -49.29411 | 2026-01-09 04:50:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85f2e820-a3b6-3fc4-bb6a-6bd17a54642c | -18.47097 | -54.95087 | 2026-01-09 04:50:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b18b24d0-59c1-3cf6-8f67-aded7424fcbc | -16.90641 | -53.02979 | 2026-01-09 04:50:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 636c0ae9-809d-309a-bb64-b78f29bddbc7 | -17.65772 | -56.35823 | 2026-01-09 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3824122e-aa12-33f6-9ec8-3710b0be68fd | -15.77894 | -59.74543 | 2026-01-09 04:50:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7117f17b-25b4-3c19-a9ff-e03d962dbc9b | -20.73146 | -55.16122 | 2026-01-09 04:50:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b571648-56a0-36e0-bfb8-9bc62420b5da | -19.43494 | -54.77618 | 2026-01-09 04:50:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e102f073-85cc-31a7-a3b4-4b9fbc806679 | -17.66052 | -56.36293 | 2026-01-09 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 23841635-f89e-32d0-9836-8e0f3cc4f411 | -22.74323 | -49.34837 | 2026-01-09 04:50:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0b6bc2-c2da-3870-82d2-0b6c53929714 | -22.7396 | -49.34392 | 2026-01-09 04:50:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c60574b-5ff2-3e93-bac2-717d2ebc3a48 | -17.65424 | -56.35759 | 2026-01-09 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fccc85f3-54d4-33f0-b156-71357a10b96b | -19.29922 | -55.26098 | 2026-01-09 04:50:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 365d25b2-23ee-3b00-8118-33f10e291347 | -25.57068 | -49.83268 | 2026-01-09 04:53:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 54475727-c1f5-3d6d-8cc6-4620cb5a80c8 | -27.24641 | -52.26287 | 2026-01-09 04:53:00 | NOAA-21 | ITÁ | SANTA CATARINA | Brasil | 4208005 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cf2995a3-6939-39d2-8092-a61f7b07397b | -25.57895 | -49.83394 | 2026-01-09 04:53:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| faa7c31d-a6c2-3e95-9a53-d59e26ab182b | -25.57482 | -49.83331 | 2026-01-09 04:53:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 4e0ddc18-348c-3b7f-b420-3008754b6305 | 2.55101 | -60.58102 | 2026-01-09 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e4e39ab-007f-303b-9879-cb9674e74aa8 | 4.52148 | -60.66931 | 2026-01-09 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69dc106e-d9a1-30f4-9edb-63158f6e55fb | 3.38201 | -60.24449 | 2026-01-09 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47ad5c50-30ee-34b1-b7ff-e36ffdb367e4 | 2.51479 | -60.98479 | 2026-01-09 05:14:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a474da3-2494-350c-aabf-003c70e87143 | 2.54694 | -60.58167 | 2026-01-09 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2db78284-7121-337a-87d5-004b750bc543 | -3.4922 | -47.16669 | 2026-01-09 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6de8cb8-ae14-363c-8c2d-ef897977d494 | 4.34228 | -60.39498 | 2026-01-09 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8cc35f2f-7323-3156-8ad8-e2e251c75b35 | 3.88275 | -60.07379 | 2026-01-09 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66865897-2d61-325a-81f3-f268a736ba27 | -3.49402 | -47.16814 | 2026-01-09 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3deae8ae-f4cc-3345-a55b-cdea425cb349 | -0.88118 | -52.0013 | 2026-01-09 05:14:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44737938-943f-360a-9f91-99bff13f5acb | 4.32399 | -59.86235 | 2026-01-09 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8514df8a-d486-3f84-b98b-6cecad2a443b | 3.37798 | -60.24509 | 2026-01-09 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc34cf1a-f148-3819-9c15-960f7df6bbdd | 2.55157 | -60.58461 | 2026-01-09 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a980bbe6-a19f-31eb-8699-f1afc0988d8b | 2.42463 | -61.15428 | 2026-01-09 05:14:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6fe2244-5f4d-3129-a3f1-5d5914dbd838 | 4.51726 | -60.66993 | 2026-01-09 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad80aabf-d52e-3a18-8a43-89ccd4f731a3 | 4.32322 | -59.85719 | 2026-01-09 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56f0aa5d-e0c5-3c5b-b5cf-0703ab128111 | -2.62374 | -51.95065 | 2026-01-09 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8a80b664-981a-3639-a670-fea8ef2a8126 | 3.88678 | -60.07324 | 2026-01-09 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12c49d44-1f8f-3cbb-9b93-068d12bbaa2e | 3.38147 | -60.24099 | 2026-01-09 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebcc0be8-c8b7-325a-b800-f7f2ab194243 | -3.49168 | -47.17027 | 2026-01-09 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README6.md)
