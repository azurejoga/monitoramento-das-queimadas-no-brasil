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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 633ab740-9fb2-3466-b745-3ffee3f866d8 | -19.76776 | -42.09938 | 2025-08-11 00:24:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 39d7a1bd-8b06-3af2-a533-e6a297715b32 | -21.04749 | -50.01572 | 2025-08-11 00:24:00 | TERRA_M-M | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 45836464-aadf-3121-aaf6-4556a9196eda | -18.98217 | -46.72062 | 2025-08-11 00:24:00 | TERRA_M-M | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 50401c38-72b4-3051-91ed-9ef3a36a7f08 | -19.56449 | -46.62768 | 2025-08-11 00:24:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| df91756c-8dd4-3ccc-b961-83ecf7729714 | -22.14426 | -47.5258 | 2025-08-11 00:24:00 | TERRA_M-M | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2f5e48cc-2e65-3623-b56b-30d6eef831fb | -21.04946 | -50.03483 | 2025-08-11 00:24:00 | TERRA_M-M | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 159.1 |
| 8704f200-7ba6-34a6-83c8-033b4b36424b | -19.54968 | -46.58622 | 2025-08-11 00:24:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c7499af2-b426-3047-b4b8-879abee45d7c | -19.42051 | -43.36965 | 2025-08-11 00:24:00 | TERRA_M-M | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 78f64a73-48a3-3831-acdd-b4e653bc9d84 | -20.60663 | -48.87632 | 2025-08-11 00:24:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| ecb32892-bec8-34ac-8683-0d3e0485a513 | -13.38743 | -43.71041 | 2025-08-11 00:26:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 39da92cc-ec19-36f3-b580-fa3b5787e6d0 | -12.58078 | -41.27623 | 2025-08-11 00:26:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 58b240d8-1929-3777-882b-091b9ed19d38 | -11.70836 | -50.09789 | 2025-08-11 00:26:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9ec255e1-18fc-3a35-9952-f15cf13b4cd5 | -11.75024 | -51.63926 | 2025-08-11 00:26:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 07bcac86-bd4f-39cd-a024-e201cf8381ff | -14.30368 | -51.98401 | 2025-08-11 00:26:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0adaaa6f-d3c5-3d41-8cf1-aab454565e26 | -18.83566 | -48.67096 | 2025-08-11 00:26:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 53cbce5e-100d-3f3c-a81b-b1eb6296322d | -18.30809 | -43.96578 | 2025-08-11 00:26:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 8927c8f2-5850-30e6-a478-1383b8f423e6 | -15.09963 | -46.53873 | 2025-08-11 00:26:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6262f74c-4fc0-3a11-a373-00f605f9b608 | -13.16812 | -50.50443 | 2025-08-11 00:26:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| eec3f9cf-a90d-3a34-bbec-3f5eb0e314d5 | -15.99555 | -47.50219 | 2025-08-11 00:26:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6216d83e-83a5-37e7-b1b8-c2c8c10a97d3 | -11.74815 | -51.62173 | 2025-08-11 00:26:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a558550b-cc5f-3dc9-bd78-d6cf00abf446 | -14.30494 | -51.99035 | 2025-08-11 00:26:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 8241171d-fd64-3eca-8d55-ff67f2876aa9 | -14.58058 | -47.13489 | 2025-08-11 00:26:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b789c60f-db37-3970-a51a-b5177c73140f | -12.54899 | -47.06454 | 2025-08-11 00:26:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 671fa2a3-4e49-33c8-a1ef-168eb5918053 | -11.76532 | -49.12114 | 2025-08-11 00:26:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 81de4d0d-f59e-393e-b486-029791330dfe | -12.70329 | -46.36354 | 2025-08-11 00:26:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 053c6e06-b662-3c8d-9394-9f3ece31c931 | -18.84632 | -48.66938 | 2025-08-11 00:26:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 419.4 |
| 6684b4b1-23bc-34fe-a943-8fd684bd30c1 | -13.00974 | -48.40536 | 2025-08-11 00:26:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2a25d2f9-01b1-3f50-a489-6a560ca46548 | -18.18341 | -47.00791 | 2025-08-11 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 27.7 |
| d0ed97e0-fe90-3549-ae44-e9059829c1a4 | -18.17394 | -47.00953 | 2025-08-11 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 33be6533-0739-3864-9217-de3141eb7ed4 | -11.77442 | -47.39267 | 2025-08-11 00:26:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a5bd8809-3f6e-3350-8cce-45170923a30c | -18.62192 | -46.84962 | 2025-08-11 00:26:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 40880f84-8e33-3d46-9e0b-f08446bc6a55 | -16.67483 | -47.6424 | 2025-08-11 00:26:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1a7249d3-433c-398d-bd20-b1bd1f1d021e | -16.21248 | -49.972 | 2025-08-11 00:26:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 4e84b5b6-bdeb-3a1a-b85f-3d8d790eddcc | -18.3243 | -43.68899 | 2025-08-11 00:26:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aafb755b-e0c5-38d7-90a1-f210c16d7cbe | -11.4467 | -42.22917 | 2025-08-11 00:26:00 | TERRA_M-M | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| bedc00ca-0ff6-33fb-b3a6-0ede2f3169f0 | -11.71406 | -50.10444 | 2025-08-11 00:26:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| cbd2aa84-8201-3d6d-8e4b-9fd9ee3485c0 | -11.71008 | -50.11125 | 2025-08-11 00:26:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 90911aba-8054-3634-9fdf-1cb65e5f703a | -13.80457 | -41.20235 | 2025-08-11 00:26:00 | TERRA_M-M | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 0b01851f-30b3-360f-8c1e-9fdbf7ca426e | -14.57265 | -47.1461 | 2025-08-11 00:26:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ee9357b6-c387-32b6-b0ae-fe775f52e5ff | -17.23012 | -46.95573 | 2025-08-11 00:26:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 543d468f-1f8a-3cac-87f8-e3972efb4908 | -15.04576 | -42.46125 | 2025-08-11 00:26:00 | TERRA_M-M | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 55a2195f-ff4d-3b0d-86a0-84c93432288e | -13.64511 | -48.99321 | 2025-08-11 00:26:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 427fb227-71c5-3d20-a295-f13b78c6eac0 | -18.00936 | -43.48595 | 2025-08-11 00:26:00 | TERRA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bfa735f6-1d11-3b03-8585-fb4e3e56c7c3 | -13.01941 | -48.404 | 2025-08-11 00:26:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5976fdaa-9ebd-3f52-a781-fbaf53cb9446 | -12.60571 | -47.14336 | 2025-08-11 00:26:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0e0c94d5-3b63-3623-97d4-88f53c22680c | -11.95761 | -43.38922 | 2025-08-11 00:26:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 05ef814f-8256-351c-b4eb-f925b7ba1c53 | -14.56932 | -43.72586 | 2025-08-11 00:26:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2517c6a5-6102-3789-ab72-96b8faad3dcc | -12.04875 | -45.76505 | 2025-08-11 00:26:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a1f7de18-005a-3032-a087-9cf8b6d4159c | -11.77909 | -47.56757 | 2025-08-11 00:26:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e0901ef-2e23-3df8-9d10-773b6f28afdb | -12.70453 | -46.37264 | 2025-08-11 00:26:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8fffecff-0161-34ed-b041-002649ed8cd1 | -11.94807 | -43.39063 | 2025-08-11 00:26:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cd650520-345b-36c0-ac2d-2611e1373127 | -16.21429 | -49.98774 | 2025-08-11 00:26:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5e162ddb-035b-32cb-b750-ed28e43b1bc6 | -15.40304 | -49.13034 | 2025-08-11 00:26:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 00090656-8260-308c-a1c6-7a0717c0f558 | -15.69557 | -48.28738 | 2025-08-11 00:26:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8b5b2dca-5ee6-3f4f-bde7-4b4c99fd7ba1 | -15.95942 | -43.02061 | 2025-08-11 00:26:00 | TERRA_M-M | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e0a34344-aabd-3712-abaa-e22efa670b61 | -15.9327 | -42.22855 | 2025-08-11 00:26:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 235ebd6a-93fc-337d-856e-7746c532b27b | -18.62329 | -46.86035 | 2025-08-11 00:26:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 52.3 |
| a7b48736-c17b-3513-a841-973ebbe594ee | -12.55802 | -47.06316 | 2025-08-11 00:26:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 15d28d48-457d-3cbc-aa95-6e4647c8df4b | -13.59093 | -46.94571 | 2025-08-11 00:26:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 57378eb8-c7cc-36a2-99db-cd93a820f67e | -17.8077 | -42.92408 | 2025-08-11 00:26:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7733586f-ede0-3912-9dd7-130a8b7e7cca | -18.6314 | -46.84828 | 2025-08-11 00:26:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5c9385a0-5e06-3a06-a456-135d0fe8e4ff | -17.85635 | -44.42497 | 2025-08-11 00:26:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 39c39f50-c3c4-31f1-8363-e35a2dd56b7b | -18.84799 | -48.68341 | 2025-08-11 00:26:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 09371b34-77ec-3277-b384-e9f1911342ed | -18.32294 | -43.67952 | 2025-08-11 00:26:00 | TERRA_M-M | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5d2e2951-be6f-30cd-ade0-a1361baff367 | -16.04054 | -43.82765 | 2025-08-11 00:26:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 25005c5a-dc29-36d6-ae40-4d9466ec3b14 | -11.77781 | -47.55791 | 2025-08-11 00:26:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4127f12a-37fc-3846-a518-53051f107ae1 | -12.55025 | -47.074 | 2025-08-11 00:26:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c15063f5-98a7-33cf-8911-e6896eed1614 | -18.63276 | -46.85895 | 2025-08-11 00:26:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b405bf0b-558a-3318-b66f-6a3374af817a | -16.67344 | -47.63135 | 2025-08-11 00:26:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 65fe567c-55ec-3d7d-90fa-e8b6674e4798 | -15.97442 | -41.37004 | 2025-08-11 00:26:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 0d8bdd58-fe5b-3ee9-b803-3e7990444075 | -8.78469 | -48.34875 | 2025-08-11 00:28:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0bf4f481-4307-30a4-ba24-efc08ada9ce9 | -7.62122 | -45.19927 | 2025-08-11 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a51c359b-c7cf-3950-94c0-1a6c1a6e8ff5 | -7.61072 | -45.19102 | 2025-08-11 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| acd11d8e-e688-31f1-8f31-3f40ac544485 | -6.28117 | -43.70732 | 2025-08-11 00:28:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bbcb0c28-91cd-3bea-bb7d-8f8d3ac15cc1 | -7.13727 | -39.46894 | 2025-08-11 00:28:00 | TERRA_M-M | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 301ebf09-a3c2-3624-ab7f-7b0f09c7db77 | -7.61208 | -45.20058 | 2025-08-11 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 245cbad1-a91b-33e5-8f10-3f5483cd3b86 | -7.61987 | -45.18974 | 2025-08-11 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c08e37e9-9f6c-32c3-9f0b-83463163f6f3 | -8.07668 | -46.86333 | 2025-08-11 00:28:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c10fcb07-6b25-3691-9f22-5979c812eaac | -10.36909 | -50.81136 | 2025-08-11 00:28:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 32.2 |
| a3a0a975-160b-3d2f-8a0e-ff16b56c486d | -8.78599 | -48.35842 | 2025-08-11 00:28:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6eacb6b4-2d50-34ae-bf1f-29a98271e98c | -5.48 | -44.39594 | 2025-08-11 00:28:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0aaa7b5c-8ba1-363a-86fe-37cbcf790065 | -9.38479 | -48.233 | 2025-08-11 00:28:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 46110d9c-b292-353b-81d2-1497ce1d11d7 | -9.20282 | -44.52763 | 2025-08-11 00:28:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 877accf1-e22e-3678-8503-486ef347a041 | -9.64575 | -43.83131 | 2025-08-11 00:28:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| a4387814-21f3-362b-a08d-b8a9791651ca | -9.2135 | -44.53613 | 2025-08-11 00:28:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 96eaef20-a705-3013-b731-f045eaf697ff | -9.2121 | -44.52627 | 2025-08-11 00:28:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| af181d05-4d17-313d-be99-87fdd0844b51 | -10.36451 | -46.62873 | 2025-08-11 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 486edafe-1a4d-3fd0-a4c7-d2e95e3e6512 | -9.87097 | -43.54793 | 2025-08-11 00:28:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 4ca6233b-bbb9-31bc-8dd7-4a7fa28eeb9a | -6.29303 | -43.71787 | 2025-08-11 00:28:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1ecb1fe1-f5fa-3661-ace0-457fd37fbdd1 | -8.80406 | -48.77925 | 2025-08-11 00:28:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f144a38e-6a29-3daf-9cb9-d824a541b571 | -9.22103 | -48.52832 | 2025-08-11 00:28:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9feef21d-c1c3-3ff4-8485-dd3686744dfe | -9.21935 | -44.52943 | 2025-08-11 00:28:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b3795d8a-4de5-3e9c-a851-715812c992b3 | -9.86127 | -43.54939 | 2025-08-11 00:28:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 31f23122-99d2-3e3e-a77d-868c78b4dc2c | -9.46104 | -40.39743 | 2025-08-11 00:28:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| f6ebb34b-97f7-3821-95ac-0d93490ed4bb | -7.17443 | -44.28214 | 2025-08-11 00:28:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 572de2cc-d4b0-3389-942d-0fdd795e1119 | -9.86937 | -43.53703 | 2025-08-11 00:28:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 55614ba6-377f-3294-8a50-8f34fdd97977 | -10.35688 | -46.63889 | 2025-08-11 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 75d61005-ee1e-3eb7-a04b-a9ba1a5e9be9 | -10.36574 | -46.63766 | 2025-08-11 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 53e67a1a-36da-3bdb-b9c4-e3636f9e2e58 | -7.55509 | -49.61657 | 2025-08-11 00:28:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7b82ccd0-36d4-34d8-9213-6452a0a9f86e | -10.37087 | -50.82566 | 2025-08-11 00:28:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |


[Clique aqui para ver as próximas entradas](README3.md)
