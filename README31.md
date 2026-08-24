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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31936607-f525-3f4f-b246-b15d3f787bd8 | -8.92661 | -48.54016 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e290bbeb-ff39-3c40-a92a-6d7b68defa9d | -11.90903 | -55.90102 | 2026-08-24 04:46:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28cff4e9-c25d-3bfd-88a6-ce0e8dd0e86c | -11.62262 | -51.09328 | 2026-08-24 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c68e415-b821-3f2c-97bb-949e911ae25d | -9.95568 | -48.33504 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a274fb9-72b0-36de-b3da-c2b34b1ba193 | -14.32237 | -51.76 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2222d505-c6f4-3ca5-98e7-9c6e7829b6bb | -13.10414 | -43.34952 | 2026-08-24 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d700cd6-fcbf-37ec-bd1a-8824b8c95033 | -14.44132 | -51.80173 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e969737e-c3ae-3a5c-8a44-e758fd0dbebd | -12.10775 | -50.62411 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad82165c-5603-3a95-9db9-93e55d055449 | -15.36728 | -45.59459 | 2026-08-24 04:46:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21f0993c-f828-30d2-9b74-acb03d61fd8b | -8.59191 | -54.73462 | 2026-08-24 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0952ddff-69dc-37cd-bf75-b3e577f09b6a | -6.55934 | -58.59327 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f41b9735-e0a6-3338-b5e1-d87ebf56a5b9 | -20.6528 | -45.84447 | 2026-08-24 04:46:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bdfa49f-7d76-3a4e-889b-94f51f2785bc | -12.86193 | -48.49306 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86c63141-1b4a-3b72-93e3-43e784d0b9f2 | -12.11603 | -50.59301 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e16f135a-86b4-3d42-920a-ae3220c2565f | -14.32625 | -51.757 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 534d2681-3847-3dd7-a6e6-3ce9badcf85d | -12.10444 | -50.60189 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| a019f629-e9d8-3ce5-a554-f93c7483f739 | -11.61986 | -51.08929 | 2026-08-24 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25987ca5-453e-387a-8c21-bb68dc8bc976 | -12.10278 | -50.61246 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7cd3b8f6-a7d8-3d64-83b8-cc6fe5a06f85 | -13.4195 | -51.81771 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9870b20a-d97e-370d-9112-49be815d772a | -13.17454 | -51.39487 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccbe6d3d-5346-32ae-b73e-6a90179a3899 | -9.40212 | -60.59498 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0fa2f18-919a-3107-9b55-871cf445be26 | -8.10308 | -47.48046 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49d191dc-61b5-3f2a-ad7d-488fa232a588 | -14.78457 | -48.7719 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 387124a0-a204-3316-a738-75dc519bc94c | -12.27597 | -43.19532 | 2026-08-24 04:46:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 119c88a8-2052-3b4d-af4f-c4ae20a50d07 | -12.85489 | -48.49201 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5719d542-16e7-36ee-8e6a-0596642d851d | -10.69999 | -47.75193 | 2026-08-24 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca71b56f-60e7-3151-8132-7756d792a6a4 | -12.09228 | -50.61438 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a95b3da1-c883-32a5-9e8c-0daa36b644d4 | -14.32303 | -51.86236 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 506d429b-676c-3e38-a0f8-a6ac2ca8f983 | -12.86125 | -48.47321 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb69c263-bb9c-37e9-8bbc-2d6b8fb83af9 | -14.34282 | -51.75978 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| dbdc5b76-7fe8-372a-a561-6a9f93c512ce | -19.00002 | -44.70783 | 2026-08-24 04:46:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f79b8f4-5845-314c-8d09-636889080b2d | -9.86894 | -60.11088 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ada02aa0-253c-33e8-951a-7867cd25d8e3 | -9.50162 | -60.50133 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e6a872d-b106-3252-9ee2-fc23f7594c25 | -11.1089 | -49.88855 | 2026-08-24 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f15e2d0-5bd1-3f4a-8a88-75bb7a7cb7af | -10.72932 | -47.96765 | 2026-08-24 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc0611cf-ef27-36b9-ba30-c9d935d7ed17 | -12.0967 | -50.58626 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f31c480e-9c20-3c1e-821c-d8fbb06bcc0d | -8.98809 | -50.76161 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57b3fb54-16e7-3870-9e06-cd50053e0c42 | -8.59065 | -49.99114 | 2026-08-24 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2920a870-8b67-36c3-bbd5-d0b9b6902b01 | -19.0107 | -42.12713 | 2026-08-24 04:46:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3755cfac-4195-35b6-9572-5e98a2d2a904 | -6.73756 | -59.66066 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9856b8e-d2a2-3c58-8a98-15b265f6a6d2 | -10.07035 | -46.37123 | 2026-08-24 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8097b2f-2523-3298-8baf-fb29e6b48f16 | -12.60905 | -52.45801 | 2026-08-24 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef46f3b8-8f57-3d7a-a9ef-c284383c9606 | -12.10167 | -50.61951 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98f7198a-2799-3edb-a395-c9e23d6b6216 | -8.31243 | -46.8938 | 2026-08-24 04:46:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eaf796ce-fbc9-348b-ac6e-d1ecbe70265e | -7.78706 | -56.28521 | 2026-08-24 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13bfecb7-2ab0-3428-8177-44b2b11de5a8 | -7.48611 | -55.33681 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4d3fcaf-49f3-3565-af63-b1bd46e260f3 | -11.58058 | -46.95762 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74219d88-f0a5-3e92-a072-8102ddc949c8 | -13.09375 | -43.35365 | 2026-08-24 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23fa848a-a3ed-3c90-828d-a865ba362944 | -10.45787 | -46.21959 | 2026-08-24 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 687923b3-b660-3209-b7d1-3382c6e444b1 | -11.54786 | -46.96416 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 992b7079-0449-32b7-b954-eae1782b0859 | -12.27173 | -43.19804 | 2026-08-24 04:46:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77c8c4e4-1589-375b-9936-57627da4f617 | -18.53176 | -47.17352 | 2026-08-24 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02b27346-22bc-36c1-9c2a-350c9e74071d | -6.73826 | -59.65683 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d902b847-b513-32d5-acac-69dc7b7a113f | -10.72994 | -47.96357 | 2026-08-24 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b984e146-c3b7-33d1-80ff-69411c89e579 | -12.10554 | -50.61652 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce8aea39-8f0e-387b-b43b-0f30cf877b8d | -12.10168 | -50.59783 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52ac6335-8826-34f6-8fe0-8f398f7f5ddb | -14.78872 | -48.76823 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f7753a27-ccc6-359c-b846-6b72dcbb30d7 | -12.09505 | -50.59675 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0587f3f3-7807-3080-96a8-42f2ebae89d2 | -12.0967 | -50.60786 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19465366-9e50-3cd4-9afb-19e22ee215ce | -12.10112 | -50.62304 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51bcd60c-03e4-3296-a146-975473af6ca9 | -13.8958 | -54.0362 | 2026-08-24 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62d4276d-438a-3f4c-bdfd-5ed9bb40d3d4 | -15.03121 | -48.68899 | 2026-08-24 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de89d92e-aab2-36d2-a1a6-e5eba8f3ca6f | -15.3204 | -49.22536 | 2026-08-24 04:46:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3667df9b-7b4d-3afa-aa56-ed7dfc482de0 | -6.55031 | -58.52259 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cbd5e21-8fa5-31db-8781-33633582fb9e | -12.11935 | -50.61515 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29a355e7-86a5-35c9-a298-f12ed9a46780 | -12.84848 | -48.48669 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ef59757-4ae0-3cce-9bd4-40d860b25cd0 | -12.10665 | -50.60947 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 157139d4-efdc-35ed-93af-8edbf67db126 | -12.09781 | -50.6225 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b331abdb-55db-3287-a21d-db45689ef54a | -19.28097 | -46.67633 | 2026-08-24 04:46:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22e107f0-cecd-3c15-9fdc-03fa6769896d | -10.69528 | -47.73452 | 2026-08-24 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c9f1025-e937-36a0-bd43-a83e2a7cd69f | -14.78275 | -48.78447 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccb2ccd7-8fc3-3f37-9af7-a9271293429a | -8.98115 | -46.006 | 2026-08-24 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa61d645-68d7-323f-acc6-fbaaa15de0a0 | -11.68404 | -54.5575 | 2026-08-24 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c11b244-552e-3612-8411-96c9339ddc03 | -8.37344 | -46.4694 | 2026-08-24 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9505c2ee-879c-31b4-a527-d10ed84bd668 | -9.71552 | -46.02756 | 2026-08-24 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 254b6bb4-f03f-3cba-922e-d64f346900af | -12.74048 | -48.38543 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2223491-2e34-3d16-a3d6-9f671811651b | -12.1094 | -50.59193 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d35d648-cd10-39d8-a347-481aef60e4c9 | -19.98172 | -50.38053 | 2026-08-24 04:46:00 | NOAA-20 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7339ec03-a5fc-3631-a111-7c5ba530f692 | -11.55226 | -46.96025 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 036f691e-abb9-3033-afdb-16e1397a2b9b | -8.09883 | -50.05149 | 2026-08-24 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfd8729d-7e19-3cd7-824f-01179abc31ad | -6.61697 | -58.38634 | 2026-08-24 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb5228be-8fee-3d81-8ba9-bbb4f276e3a8 | -10.72748 | -47.97981 | 2026-08-24 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dac11f5-6cda-3c2e-b2dc-478b61234d61 | -8.56069 | -47.44428 | 2026-08-24 04:46:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4f098b9d-240f-3d64-8597-eb8830f06577 | -11.59728 | -56.29108 | 2026-08-24 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f22ad64f-19b9-3f39-97b0-05ee81bcc660 | -14.41321 | -51.78605 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ac3e92e0-4e81-3ba8-b117-5a185da89aec | -9.9626 | -48.33591 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18181754-809d-3ac1-b08f-9a5d37c52762 | -10.43195 | -50.44057 | 2026-08-24 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00e411db-8a96-347f-9711-d853150492b6 | -20.32687 | -46.61149 | 2026-08-24 04:46:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39a91254-7bc6-3731-94a4-8eaaa79ee816 | -12.74901 | -46.44531 | 2026-08-24 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| efc45b41-2c37-36a3-b73f-f4792239321d | -15.04904 | -48.69167 | 2026-08-24 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e835d8fa-4942-3bfd-9306-b9f379b32db5 | -12.61241 | -52.45858 | 2026-08-24 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d92cfa4-d29e-36a1-837d-9f87d9654596 | -8.56421 | -47.44482 | 2026-08-24 04:46:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fd00cd5-b687-3bc4-aae9-c061dcc776c4 | -6.74247 | -59.66536 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94cfa271-c667-3903-a69a-6eb53008399b | -9.71623 | -46.02277 | 2026-08-24 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bcfe893-9a72-3f52-b3ae-0de4c1fac1da | -12.41472 | -42.89931 | 2026-08-24 04:46:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e6f47ef0-2f8e-3830-a2ec-0a76bc07572c | -6.54516 | -58.52138 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47598463-6298-37d1-b1ed-90891e84023d | -10.29757 | -48.20113 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96fd5a60-5beb-36f2-82e1-05e8dd5452bc | -12.09505 | -50.61843 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a0b95da-fe32-3d7e-a4dc-f8f00eb047e2 | -14.79102 | -48.77734 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8959540-897b-3ba0-9940-f3168c607b3e | -8.98044 | -46.01075 | 2026-08-24 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README32.md)
