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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97e876b9-c973-3562-8dad-edd9a47bcc0d | -15.27909 | -53.78554 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24978d80-ae78-3c1b-86ac-4d7613002dcb | -15.78358 | -43.12891 | 2025-09-10 04:17:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b2857595-474b-389b-aef0-0c1eb0cb2e26 | -12.40894 | -43.21095 | 2025-09-10 04:17:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9d0b817-aa1d-353a-88a8-3f6113ed526a | -11.82489 | -47.54775 | 2025-09-10 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd3696dc-2a22-30d9-a5b4-efc2fe7d9ba0 | -11.11302 | -48.41383 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2fc52fbe-d66c-361f-9a9f-5ff9c6747e59 | -15.93772 | -50.23198 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5db9b325-a3f9-3f3a-a680-49c89e7a84bc | -15.22147 | -44.0423 | 2025-09-10 04:17:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 610448b7-9500-37b8-b7c0-a64c0818170a | -11.81411 | -46.75351 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b618834b-e7fe-3b7c-a0df-d17d7cb1855e | -22.88053 | -48.13671 | 2025-09-10 04:17:00 | NOAA-21 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f3a18e9c-bdf3-3f71-a6c0-836bb206181f | -17.56165 | -44.53821 | 2025-09-10 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb48e0fb-871b-377e-b4da-c317ab714c54 | -11.20694 | -54.9849 | 2025-09-10 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63f732fd-2a18-37f4-bcd1-18e9adaca070 | -11.8312 | -46.75189 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e91d9d4-d302-3476-8dad-a9f1428333aa | -10.02442 | -51.67424 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ac3ffb18-c937-3d1e-a9c9-3d418bab0d88 | -11.86691 | -47.53816 | 2025-09-10 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 914b9360-ff7d-3208-a66e-a1639c5de1e2 | -20.12254 | -47.69146 | 2025-09-10 04:17:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b69c645e-4b38-3220-8620-192b0979d558 | -14.86269 | -49.5319 | 2025-09-10 04:17:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3cb1d0fa-1591-3717-9c31-dd3fc6857a3b | -15.09025 | -50.06757 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 65a5f24a-74dd-3dfd-ba36-e7cddaea4209 | -10.95459 | -46.80042 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63c3eb9c-0483-38bc-99a4-c3610f19d819 | -20.8538 | -54.98971 | 2025-09-10 04:17:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00e2aeee-70a1-3bd1-a5dc-09fda44a99e3 | -11.15061 | -48.3532 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30094977-1dbc-38ff-846d-41b801ba9ebf | -14.90313 | -50.1211 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8be6c139-47a8-3b78-b4f1-39d1e9bc88f0 | -10.84304 | -47.75319 | 2025-09-10 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a6eb8d6-fef2-392f-b4f8-7388e0689c03 | -11.3423 | -46.54094 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6173c2a2-84f3-33a8-9570-25a697de738c | -11.66219 | -46.90831 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57fd0d92-1d8c-3b9b-adf5-656191ae3925 | -9.76525 | -51.12085 | 2025-09-10 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e96353af-d829-371f-b138-c7f5a0fb53d8 | -21.18643 | -47.30367 | 2025-09-10 04:17:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 903e4f29-e71e-354f-9ebb-a11e1eb94838 | -12.92795 | -43.44072 | 2025-09-10 04:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f65ef42-a39a-3949-a888-55969cea0a46 | -15.81098 | -52.26083 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5abd365d-9e4d-3614-a28b-bc6520943684 | -21.31168 | -43.88894 | 2025-09-10 04:17:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 6f012797-c044-3674-8ac8-e8cdb7fdf9b7 | -11.4733 | -49.26696 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2567b1c-2107-3e85-8053-e6578c027b42 | -11.9466 | -51.04539 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09092abb-4ed3-33d8-b8b9-3af777a8ea15 | -11.4561 | -43.66743 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f069eaf-c769-3caf-9f94-9246696dd371 | -10.8394 | -47.75247 | 2025-09-10 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd817a1e-fe24-3d05-9c7a-73fd7f1c2daf | -23.20075 | -47.34813 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9544aae6-b887-3d7e-b29d-fe512d190b76 | -11.81614 | -46.75712 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ee13165-e589-3f8e-90de-49440ede8c66 | -20.37764 | -46.63152 | 2025-09-10 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 590041f7-1950-35fc-b7c1-98d37d622ecf | -11.16184 | -45.2835 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00c20c9a-0672-39cc-99d4-dcbac4fa41ab | -23.36331 | -47.20102 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5b847fce-f788-3df7-aae8-9e05dcb82fa3 | -12.86576 | -47.97033 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f84c39bb-3ae0-3625-aa2a-99e9dcd7884d | -13.27487 | -43.75039 | 2025-09-10 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9875b7e-d744-307b-9bcf-f08d437afe2c | -11.33449 | -46.52402 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 14dfb0e0-0ca6-3ac0-b711-b1c0a4edf4e6 | -11.39759 | -43.53878 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 68f8b1e1-c61e-395e-aab3-5c1ba2ab83cd | -16.62496 | -49.76983 | 2025-09-10 04:17:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5c05fcc-458e-396b-8618-6f93625289c4 | -13.94709 | -48.2632 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3c12c457-03ed-337a-a7f7-7c8f71a6f0c5 | -10.74276 | -48.91693 | 2025-09-10 04:17:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ae46502-9fe3-3918-abdd-e479e85fa4cb | -11.44685 | -49.27853 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0299de48-02f2-3d0b-91fa-e4566094459c | -19.81105 | -47.78689 | 2025-09-10 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a877e4e7-aca7-3e81-90da-5089fc8aa0df | -17.19963 | -50.1563 | 2025-09-10 04:19:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b293cfff-0b66-330b-9a03-518eed7ffcde | -19.17215 | -48.79085 | 2025-09-10 04:19:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8072e49f-bdee-3a40-8310-4dd54f66540a | -17.41113 | -49.88779 | 2025-09-10 04:19:00 | NOAA-21 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 521362e8-082e-3596-8073-e1f20bb1f34a | -20.46426 | -43.95752 | 2025-09-10 04:19:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.6 |
| 7bc826ec-c43a-3af9-b3b0-53cce31ff2d8 | -18.02798 | -47.14758 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c6dff4bd-fc84-39f4-ae10-6d6f07a4c86a | -17.20259 | -50.16188 | 2025-09-10 04:19:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5015ac65-4409-3c19-be17-a407b7408e51 | -18.00723 | -47.10612 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb34eb30-b69d-3626-b8cf-b272c9781f34 | -18.64998 | -46.54038 | 2025-09-10 04:19:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3d9fac57-d27c-3866-9f15-387cc97b3a6d | -19.46567 | -43.70868 | 2025-09-10 04:19:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e1c58c2-8abb-3775-9ca0-65c59878ab80 | -16.51493 | -55.13445 | 2025-09-10 04:19:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d9861ba5-4142-3f91-974f-1afae461338b | -19.91755 | -46.15786 | 2025-09-10 04:19:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27534aa8-0226-3042-b4b5-6578a782c5d9 | -18.02033 | -47.1312 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baab8c53-9f93-3bb4-9296-4db622375f21 | -18.03801 | -47.14927 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0b4b0aa7-d6a9-398e-9f29-fc9f1c363a53 | -23.50435 | -51.72811 | 2025-09-10 04:19:00 | NOAA-21 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 74b170c5-cd10-3070-b167-055d49870a52 | -18.00269 | -47.1129 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd5f115b-86bc-391d-8b5f-02c9e4f869ac | -20.46371 | -43.9614 | 2025-09-10 04:19:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.6 |
| 8ba78e7a-578b-347a-96e3-61dfd73664b0 | -18.96411 | -42.39023 | 2025-09-10 04:19:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8398cb3a-f79b-34c0-b66f-1ea7053f9ae2 | -19.7768 | -45.79179 | 2025-09-10 04:19:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d18a3ba3-03aa-318c-bfe4-aaebc3b56a29 | -19.80148 | -43.92015 | 2025-09-10 04:19:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ca0b785-7b02-3e5e-b428-67daa2555472 | -18.02463 | -47.14703 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 81a70a4c-792b-342c-817b-a5fccc073d29 | -20.4672 | -43.96199 | 2025-09-10 04:19:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.6 |
| 83af1d84-e0dc-3373-8d40-5ed1eb0fef18 | -19.73274 | -47.90509 | 2025-09-10 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e4996943-a1bb-38ec-8614-83f76176041a | -19.46626 | -43.70461 | 2025-09-10 04:19:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 345ead11-717a-3a96-9ad6-7c87397e336d | -20.15324 | -43.65396 | 2025-09-10 04:19:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 78871d4f-4fa4-3706-9825-b9d2f885ca20 | -20.08967 | -44.47318 | 2025-09-10 04:19:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a1ead075-f003-3a8f-9e16-2ee1eb596267 | -20.29878 | -42.16626 | 2025-09-10 04:19:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b8a1f59e-2d23-359b-a098-f99d80740432 | -19.66402 | -44.89367 | 2025-09-10 04:19:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d82fe29d-a9bc-3894-8cd0-a7250f0e25ed | -18.45176 | -49.56346 | 2025-09-10 04:19:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3251da5f-c7ae-3a32-9e84-2348b82e7080 | -20.00793 | -47.6209 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67ee2102-d6fa-36d1-a8a7-e1b05a4ad400 | -19.45612 | -43.93791 | 2025-09-10 04:19:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0765b14a-ae5d-3a40-a976-352242503544 | -18.14234 | -51.72997 | 2025-09-10 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fbb29839-7636-3391-b159-aeb3d9088d3f | -18.02522 | -47.14337 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3cba4cac-6a07-35d9-9942-754401dbdf60 | -16.51883 | -55.14226 | 2025-09-10 04:19:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 393f243a-6318-3722-b5a7-4a82dcb5f037 | -25.46169 | -49.40441 | 2025-09-10 04:19:00 | NOAA-21 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 57db2144-702b-3d2d-8f2c-3a1e3c93e5b6 | -18.3346 | -49.32657 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2047147-0367-3bb7-9774-b01ece5169f8 | -20.01003 | -47.62907 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 246fb3ad-7019-31df-af14-e6bac3efa2fd | -19.17632 | -48.78745 | 2025-09-10 04:19:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f20d646-c76a-3efd-ab6f-e033d82168e4 | -18.03251 | -47.14084 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e588137f-1e49-3d49-8f70-622b0e4909bc | -18.46687 | -46.47186 | 2025-09-10 04:19:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76def639-75ce-3edc-8615-ca3252de4d59 | -16.12223 | -55.86074 | 2025-09-10 04:19:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 41981124-789c-33ef-a51e-f67c078d2cb6 | -18.46241 | -46.47854 | 2025-09-10 04:19:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48a4e854-2608-35bf-8bac-5dd2c4badddf | -19.24864 | -43.66041 | 2025-09-10 04:19:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72db5606-558d-34e8-9932-acac24b15417 | -18.34466 | -49.33286 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0545dedd-c0d2-3113-a259-f6f91f1a97c8 | -20.06591 | -47.53915 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ede22c3f-97b6-3e3b-a51b-0c9b2b62f273 | -18.03861 | -47.14559 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8fc4dfea-c72e-39fb-9224-671f19986fca | -19.64112 | -45.048 | 2025-09-10 04:19:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 90bc2c4f-5593-3f70-8da1-8cc727df0a18 | -17.20553 | -50.16753 | 2025-09-10 04:19:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa979286-3303-39d0-8691-a346764d352f | -18.35572 | -49.3419 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 007a7ac6-518a-368e-85c3-4baa10f7a7e7 | -20.03249 | -47.61792 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2189a429-a01c-366d-89e9-550b0f94cebb | -16.12398 | -55.86193 | 2025-09-10 04:19:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 68c5e5c6-f6ee-3fc7-8a14-ef517eeae04d | -17.97089 | -46.89114 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4612124a-63e4-3397-936c-8c7498b206d9 | -19.91482 | -46.15363 | 2025-09-10 04:19:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35dc600e-de51-3964-9d3f-2e3ba90a0900 | -19.29735 | -47.98405 | 2025-09-10 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README49.md)
