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
| a10b822d-82b8-332c-86de-0d7eceaaa05a | -13.41518 | -51.38143 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d44bbdf-bf33-356e-89e9-3968050011f4 | -15.03172 | -52.76459 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10402a45-d49a-3ee6-89bb-8614b65b1d7c | -17.31285 | -54.94095 | 2026-09-01 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e97245d1-c76f-3bac-a0b4-c3ede5756ad1 | -14.44093 | -52.50426 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fab73b58-fb6f-36e8-9e6d-cb90c63c30a6 | -13.40497 | -51.83419 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d850a6ca-3ca5-3378-95b6-ddf824eaeda5 | -15.60024 | -46.57664 | 2026-09-01 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3e48e5ae-fe2b-3280-aac1-d2ca251a8b13 | -14.66873 | -53.54061 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca3602f0-fefa-35a6-a896-9d6637794291 | -16.18489 | -49.32439 | 2026-09-01 04:42:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e729d0c-55bb-3645-9ab1-e0b2b4acc4be | -14.58381 | -54.07888 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45d913a8-c234-3b53-b91c-3b30dbe4740b | -15.43618 | -52.68699 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0fef980-6595-3ef8-aea8-f62ab04e37f2 | -17.38424 | -42.35735 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b1c918c-36fb-386f-83dd-b9fb9da90bc7 | -12.91222 | -45.83149 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7843f922-1db5-37fe-81b9-19a0f2205d5e | -12.78766 | -46.46094 | 2026-09-01 04:42:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02f274ee-a4c0-3b2d-91e9-59831724415e | -15.25263 | -53.87857 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78f445b1-7e5c-389c-aeee-56474f2568b0 | -14.26421 | -52.85798 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 797b4ac3-0c83-3de0-9b6c-62620d8d11e8 | -13.95225 | -54.40335 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 846121e5-3b8b-3ce8-9e2f-8dbb24692efc | -17.3918 | -42.35043 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0565600-e1e8-3078-8d3e-f19d2fc084e6 | -14.44427 | -52.50481 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aed061df-0fd0-3dd8-b373-54d7448307e6 | -14.39481 | -52.51915 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fad59298-b5ae-3db9-8d52-e4b8c6188a55 | -14.46591 | -52.51967 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a197c01e-d493-3693-b9b5-0a60d4ef5ee9 | -14.38797 | -52.54041 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 353fabc0-68e9-331f-b319-8b025c918f0f | -15.6624 | -48.71031 | 2026-09-01 04:42:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b4cb294-f579-3695-9416-811c7bb1dd27 | -15.43677 | -52.68332 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 477dcb03-673a-3362-8138-bda5f9f3707d | -14.11707 | -52.80637 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7020b0d2-e4e9-3c65-9ba0-fa79df4743d3 | -17.90625 | -52.10078 | 2026-09-01 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fea73f22-ba3b-3eb4-ba4f-f5a181d49f01 | -14.72585 | -53.57727 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eafe897d-7c0c-3dbc-a657-7e36c6de3881 | -13.3257 | -51.77681 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5119bb82-874a-3d2a-bf50-97c798e97d06 | -14.39058 | -52.48124 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e18e6fa-ce32-3633-8ff3-3d002be782d4 | -14.38855 | -52.53678 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c46312c-3daa-3482-85ac-7f5e6aefa563 | -14.39392 | -52.4818 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c03072dc-3d0b-3e9d-a44e-88460b1f804b | -14.44979 | -52.51315 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f753d829-c9c1-30c1-b10c-3a1fd2fc0abf | -17.38602 | -42.35288 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 145d3fda-8d85-325a-95f3-4638051d28e2 | -13.38692 | -51.75462 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0a6739e-a0a2-301d-9426-6bdd8cf6b385 | -14.4559 | -52.51789 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1272a937-0533-3180-9a2b-1db9696d7d89 | -15.2468 | -53.8494 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c98a4af3-ab4c-3bc6-bed5-f1d9f5ed4151 | -14.67496 | -53.54567 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5ffd528-7c17-3952-aac5-ce2f79edf84b | -15.55535 | -56.27847 | 2026-09-01 04:42:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 175446cb-e2f1-36f9-b939-c666236df3e9 | -14.37662 | -52.56837 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11b08a92-8e7d-3528-805c-2ddc56d21f83 | -15.4052 | -52.73035 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12e016da-0942-3b3a-b456-b128a4912452 | -15.60511 | -56.38486 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6a668132-01cb-3c12-a259-b7e2339e05e1 | -14.72179 | -53.58048 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e71e46b-691f-3cb7-bad9-df1f79c1fe4a | -17.38312 | -42.36753 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 960965e6-2042-36ba-8831-e0e0ac92bb40 | -13.27652 | -48.5492 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3611d5a-98e5-3aa7-9775-78ddfc882133 | -15.40304 | -52.72245 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e820b3d9-d745-3f33-bf7e-aaaf8a3afb8a | -14.71554 | -53.57559 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fed6d0e-ad8d-326a-9f13-3ccf5b497d8e | -12.9558 | -45.96738 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4548523f-e5a1-3c47-93f3-f6a38f24ab5a | -15.67515 | -45.91967 | 2026-09-01 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41503f19-4cc0-3288-9dc3-6588f107eda4 | -14.437 | -52.50731 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e3ea234f-47ad-37b1-a441-a390da891abf | -13.48245 | -57.06273 | 2026-09-01 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d793d271-1961-3789-b525-e6ecd680e50c | -15.76605 | -56.09849 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 9a42e8c5-1c36-370a-8607-39e022e344ac | -13.62669 | -51.83041 | 2026-09-01 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0aeb360-194d-31dc-a0fe-31c900bc0cf8 | -15.66597 | -48.71082 | 2026-09-01 04:42:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec0802ea-1736-3200-a2b9-77902d7868f4 | -14.13015 | -52.78964 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d52029cc-5974-3fe6-861b-40fa1bc3e825 | -13.27485 | -48.55447 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a54b2af1-3b3d-3b15-9dea-00da5091962d | -15.76694 | -56.09356 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f1621144-2c3f-3781-9071-fa09f47480b3 | -14.46039 | -52.51128 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d23fd80-2c1e-37d6-a2de-d474c84ba4ae | -14.46649 | -52.51605 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f1cdbbf0-d822-3105-8272-245ee570e044 | -13.28003 | -48.54978 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83187daa-5009-3372-92bf-8a2fab04f019 | -13.38136 | -51.76827 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 754bc5c2-1821-3a24-ba23-17abe2b36e3d | -17.13217 | -46.85159 | 2026-09-01 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 041eda9e-db97-33cc-8354-2b4d7f8129d9 | -14.72673 | -53.59332 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f337772-bb96-3059-9447-4dc0f7ac68d6 | -15.98225 | -48.07185 | 2026-09-01 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8c0ee12-4e88-3c62-a5d6-43d772ca9628 | -16.05126 | -54.38315 | 2026-09-01 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 771d9274-715b-3c63-974a-33b571db8f88 | -10.9519 | -61.65903 | 2026-09-01 04:42:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b8342bab-b4c8-3043-b04b-05c9c16fd692 | -14.70418 | -53.60147 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f32aae11-70b5-3899-8182-42b19384ec34 | -14.57963 | -54.08239 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7da1314-98fa-3fd1-9979-8814e768edeb | -15.01428 | -52.77327 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5ce7408-330a-388a-9575-ee55ad117e48 | -15.64218 | -50.10764 | 2026-09-01 04:42:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4dc0d74-c00c-3b02-be18-1933ccd81ce1 | -14.67735 | -53.59283 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13e84b93-81eb-3a8b-ab4a-e6b3e4763cc4 | -15.61772 | -56.38185 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a083b675-cafe-39f6-b337-221e4c232338 | -15.6294 | -56.38398 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0591c964-d085-3c69-bc12-e1578b5beaf3 | -15.43285 | -52.68641 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0136702-6afa-3f3d-b71f-ae19a490202e | -15.23645 | -53.84756 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cbf633b-6011-3a6f-97f5-441e1c3ce0d6 | -15.40638 | -52.72303 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc0d22b5-cc0e-3d78-83cb-643ac60de261 | -13.48316 | -57.05878 | 2026-09-01 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c7dcd32-820d-3322-8b19-21f24044cb76 | -15.76222 | -56.09786 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ebb1ee4d-becc-347d-a430-65bb68d27e9e | -15.25433 | -53.84677 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89276fd4-42e4-34e2-8be6-96ebb91e3632 | -15.25497 | -53.84286 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8511ed0-d0d4-3cd8-bee0-d8f2ae7efd36 | -12.78308 | -46.46525 | 2026-09-01 04:42:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8813aba6-dde6-3cc0-bc9d-44c8745323a4 | -14.28021 | -52.8873 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 833d5b9e-4937-3781-9d64-82af35fdab97 | -14.29129 | -52.90441 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 681928cd-5159-36b9-a65f-6845991ab90f | -15.7545 | -56.10453 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 7adf3eb0-0f0a-3f06-8cbb-aefc884be851 | -15.30313 | -53.84642 | 2026-09-01 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23ccc305-d106-382a-b57b-c6a9ab583c14 | -15.06074 | -47.99316 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| c94483b3-890d-3e7c-bbbc-1333ecca3e87 | -17.18724 | -54.29148 | 2026-09-01 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 559323be-cc06-3acc-af07-9ed0807e3e32 | -17.50214 | -48.87108 | 2026-09-01 04:42:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b434c59d-07d2-3896-9f5e-5c40a4a0db9d | -15.65507 | -45.90972 | 2026-09-01 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2d6461f-9f4e-35f6-9d90-1fb23ef3f309 | -14.46924 | -52.52024 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 76011034-747d-30fc-ae0e-d1b57b8f7eb3 | -18.53407 | -42.16104 | 2026-09-01 04:42:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42d7923d-d782-3b10-bd50-b18dc68f2039 | -14.27769 | -52.86023 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c6f6323-0397-31cb-b210-f8e935427e5e | -14.27961 | -52.891 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff007ee8-eec0-3ebb-b9a5-e93e069e92a9 | -15.02561 | -52.75982 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8eb67505-58e6-3d2f-a6f1-64291f9f2513 | -14.57307 | -52.10501 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c392f768-e20e-3b14-a56d-89fe91ef4d1e | -14.263 | -52.86537 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d97c5e59-fa2a-3f24-8f6d-050ae396e451 | -13.62337 | -51.82986 | 2026-09-01 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a441443-2e53-3c91-bc2c-a1305145d3b5 | -17.85256 | -50.48304 | 2026-09-01 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c53d024-bbd6-37c8-923f-f6dae479aa3b | -14.5057 | -59.83884 | 2026-09-01 04:42:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd07ee1f-50d9-326d-959d-a6107302dc84 | -14.6756 | -53.54179 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c13a604b-bd1a-3eed-9f62-93b72716223b | -13.38804 | -51.74755 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d00e7695-4a94-326c-a893-96e371e69685 | -14.67153 | -53.54508 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README50.md)
