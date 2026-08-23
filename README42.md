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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fc4cd73-c01d-31e4-9752-f2b3ff085e0b | -6.75549 | -58.67207 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b22f859-21ca-316e-87b9-f143d81e34e2 | -9.51441 | -51.67915 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccd97a5e-49a1-3c98-b79e-7c2f80adde0f | -9.99004 | -53.9632 | 2026-08-23 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ac736de-7093-3afe-af3d-3eb341737ade | -11.93895 | -45.51631 | 2026-08-23 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6aaba02-6992-39db-8a5a-c422d31183ac | -6.68085 | -58.74249 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 3484fe1b-3577-3e39-84b5-7419ee74dee9 | -8.09167 | -50.05562 | 2026-08-23 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2feb8964-eea7-355b-af5c-42b3512d3abf | -9.06594 | -60.44086 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f72dac77-082d-391d-8861-b95519aaf7b8 | -9.04255 | -50.83276 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a00b46f-470f-367f-be2c-e77ba42185ac | -6.80065 | -58.65339 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7214d63a-2042-3947-9fb7-e7e7998dd3bd | -7.54898 | -61.17466 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64be4928-612f-345f-9455-e435950f1a1c | -6.8181 | -59.66082 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b49bea29-0360-3a96-8121-83c6311c0425 | -9.21613 | -59.76349 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e2e98a2-70b8-36aa-af7d-83bb731feb52 | -6.94255 | -59.31716 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e771666f-12bd-3c1c-ad44-d1b42364007d | -9.1761 | -59.45707 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6b548d5-eae2-38ca-a657-2307977991ba | -6.6635 | -58.79863 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d50a3c40-5029-34ab-a6bc-e9d3447a1dd4 | -10.84633 | -57.52085 | 2026-08-23 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffaa1bad-f3f7-343f-a27f-f8697e11fca2 | -6.50011 | -49.90239 | 2026-08-23 05:04:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8641de8-f8da-393f-9208-509f5a598736 | -9.85834 | -60.10519 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ed48647-1223-3002-a1cc-bbf989761449 | -9.85538 | -60.12247 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24d88159-8336-3375-aff4-ac7b520d16ce | -6.67094 | -58.73107 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a8ad98de-9183-38e9-ae3c-18482bc905bb | -9.12116 | -61.59188 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 752e1488-9a22-3710-b0e5-c25dd7a8748b | -6.12435 | -57.8347 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 0d38877b-d928-3c8a-aebe-53479f870a2b | -6.37704 | -54.95313 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d53368f-9e51-3d6d-ace2-48d248e42202 | -6.7744 | -55.6977 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2216630a-6579-33f5-8e5f-ae73899fd75d | -6.56701 | -58.59267 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb185673-21c7-3d95-aa82-fcabdb99bc4d | -6.80285 | -62.90574 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7b13602-f9fe-3cc5-92ae-159fff7d976c | -9.42695 | -51.6145 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d7ea5a9-0d4b-3207-bbc2-95c9d59a5986 | -6.7962 | -62.91372 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be04ffb9-5ddc-3ffc-a115-514eb5a43431 | -9.79952 | -46.60999 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8fab7549-d7fe-363a-9619-59aac9c5edb7 | -7.26454 | -49.90852 | 2026-08-23 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2b466248-0ab1-3151-bfac-328778868e0d | -6.8098 | -59.6854 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4c2e7df-a144-3799-8440-5245380d25d9 | -7.66408 | -63.33687 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b5ef841d-d79f-3165-a646-7050b74e5e72 | -6.86534 | -59.4109 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5dd2721b-08a8-3684-b6d3-0b1db38d2e1d | -11.93849 | -45.52024 | 2026-08-23 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fc4dd8b-455d-32b3-92bf-84569a932b53 | -6.75322 | -58.662 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5c2ba5e-25e7-30cd-a82e-5c27bbd6bd60 | -7.0155 | -59.5539 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fce68953-9b71-3640-863c-97b33c4a5192 | -8.53699 | -55.32116 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f9851ec-9cf3-3a61-899b-2f29aa82073f | -9.04321 | -50.88106 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64c1ac21-03c7-35e0-bad8-89c1b10e7572 | -6.88186 | -59.41026 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bef8ee55-07c8-3899-b35f-05954a51ab33 | -8.57394 | -54.78885 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ef7a4b9-ee52-33f5-b73c-6b15560fdd6d | -10.44481 | -50.47232 | 2026-08-23 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79b94fd8-6b51-3f13-b2e1-c7370df48fe9 | -9.45956 | -56.9053 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 907585d9-a957-33f9-8943-6d132baeabb0 | -9.46337 | -60.55671 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84b35bb2-e124-3da4-810e-8d4c7b4ca77e | -9.21423 | -60.89562 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5858b96c-e858-3247-9657-5a7f59b6daaa | -7.55707 | -61.18067 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 914f2687-e35b-38cf-a403-f0547fb272ee | -6.65782 | -58.73864 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08599936-748d-30fc-93e6-0dffcb94f28c | -6.79513 | -62.91964 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dc0e66d-3e05-33da-80f3-5033d838dda1 | -7.18183 | -55.42576 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 543dc7d9-371d-36b6-867a-6b4a8edc80ff | -7.55842 | -61.19907 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa69314b-0947-3edb-a21b-29ee8271f069 | -6.25177 | -55.39594 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b1eb662-2f2e-3f83-a496-449fb3e8512d | -9.17913 | -58.33157 | 2026-08-23 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d79d367-acb6-3814-85d2-f96476db3108 | -6.79764 | -58.64795 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 787cc768-3196-3459-bd90-92100f58d26f | -8.62578 | -54.74019 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2da450d6-38fa-3b6a-9e37-e42a0cee08c1 | -6.94911 | -59.08567 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8bae6bd0-910a-31ab-b189-6b642b9d49e9 | -11.61452 | -50.55191 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 25913fd0-0297-325e-ae96-0c09a96ae6ae | -9.65369 | -63.84026 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 770663dc-d536-368c-82e4-41f15787a478 | -11.21173 | -55.07528 | 2026-08-23 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64b4587e-2445-38fe-8942-a79fec56bf9d | -7.65677 | -63.3482 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae7a7bae-6e80-359a-84fc-c2a605a1f233 | -5.92746 | -53.65074 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2c0fedc-7eab-309e-9c5f-a6ce50bd9be9 | -6.80683 | -58.63989 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39d6eec4-5c06-3f65-9d3b-bf4e81e247b5 | -8.54143 | -54.82285 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98d3a865-dfa6-3d61-b6c0-49e8e0c46f9f | -10.7924 | -50.96793 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7b08cb4d-7daa-3ced-bb4c-f4671e03436a | -6.77813 | -59.75037 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2870040f-f919-3119-b6eb-a5218e6e6645 | -6.11427 | -59.93258 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b7b6b98-8833-3675-9560-1cb7140bde38 | -6.93517 | -59.07312 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f096acb3-e5b0-3383-9e4c-7e52be2aca2b | -6.69171 | -58.72475 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbee0157-dc5d-3426-942a-d08c6176228f | -8.68919 | -49.55236 | 2026-08-23 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e750a5ce-4a73-32ac-915e-5fe182813704 | -5.96148 | -53.62748 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d039cb7-9614-3dac-a2d1-023c876a6129 | -6.95859 | -59.07706 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1c3aafa2-b39f-32ce-b4a7-a137e8bddd5b | -6.68324 | -58.72825 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b113c57c-2279-3356-987b-e10d20e06329 | -6.11718 | -59.94098 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f448a9dd-d414-35b1-81dd-534214c185ea | -6.80906 | -58.64997 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2becbdb4-95da-372c-a5d6-c7b768e193a2 | -8.53977 | -54.8119 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7135dfe5-d82f-3f4c-8b89-9aa99d6addd1 | -6.80019 | -62.92054 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a37112c8-9bbb-33c8-ae3f-67496a029315 | -9.11198 | -60.33828 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c32db72-73ed-35a3-b0bd-8a6eade62b16 | -6.86076 | -59.41365 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1a2b9c1-4077-34f7-99d6-1718a365e420 | -7.97496 | -63.65509 | 2026-08-23 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bda42b6d-2b21-31b6-a312-1e53de2005bb | -8.52039 | -55.33995 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 75a76d21-2b01-371b-b43c-6198c9ad72f8 | -6.69316 | -58.73971 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52ed7007-c3ea-3de4-b0b3-56eb0db59b0d | -6.249 | -55.39183 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 853a4032-54fe-35e7-b741-2732462d95be | -9.58935 | -60.50502 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c45a7e6-cd2b-3e7c-9a15-9933048d43a8 | -9.79189 | -46.6082 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5357b931-405b-3058-9d4f-5c43f6fa5aa4 | -5.94931 | -52.12434 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d0058f73-f618-328a-bcad-5b0639027dcf | -6.97503 | -59.07473 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 252a8476-9b9a-38ff-985d-34c4a9f316ed | -6.79614 | -59.42008 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dad1945-8e09-3e5a-bdb8-e18fa871688e | -6.85022 | -58.97994 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bfe9b456-d9af-3c6d-a311-f02c278c10a6 | -6.3903 | -54.95525 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 296081f1-2d44-3557-a127-85e86a36545c | -7.59457 | -61.22827 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66e72de9-7c2d-3eb6-a94e-f613a7ba0289 | -9.1714 | -59.46128 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9bafb65-00f8-3649-a94c-013f81b1cc5a | -7.01714 | -59.5688 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17caff4d-971d-3c9d-a4f3-07dc94ebfa23 | -7.0125 | -59.5718 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f02491c-3941-3148-b572-5bb487ccca52 | -5.68787 | -53.74854 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebc5f8e4-cdf6-3ede-bfed-bba8e8597290 | -6.95943 | -59.07209 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f1adaef-91eb-347d-be36-b58cc6e85506 | -6.81794 | -59.3881 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a90dc79-2275-3404-aeea-903f6ed613aa | -6.37814 | -54.96758 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87fc8c90-3e70-3afd-90ca-d78f337fd6db | -6.54745 | -56.17285 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6806c04-5678-325d-91c4-98761af51703 | -6.80164 | -59.58437 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8f61020-2909-3da9-97c7-106e2bbf31d0 | -4.96382 | -56.27155 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49587cad-0feb-3460-816c-e00989012c05 | -8.53428 | -54.84663 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7386bcb7-7d24-338b-97bb-293129c29dba | -8.52816 | -55.3126 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README43.md)
