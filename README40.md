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
| 5a4213b6-7bde-3ab9-9ff5-7a5fd0a5de4d | -16.41346 | -49.87466 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1053e0d6-96a1-3f6b-b1c8-ade3fb59aacb | -12.85506 | -48.4978 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b981473-cbd8-3b91-9459-d4d0c8009670 | -15.24 | -52.80289 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 319671d6-222f-3611-b3a2-9782b8c42921 | -12.89014 | -48.49974 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4699b5da-aed1-30d4-b172-0213f9f712e4 | -11.77427 | -47.24163 | 2026-08-25 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e5936eb-50ab-3d78-99d5-704557c8614b | -15.33199 | -52.80039 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7587c86-51b1-35cf-8361-218772684ca8 | -11.77251 | -47.25242 | 2026-08-25 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c19744e-53ec-3645-b0c6-a889c5da305a | -14.52643 | -52.0476 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54cfffe5-f46d-3354-b673-c600901a0b8a | -12.86671 | -48.49172 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a84e0ce-1d75-35ed-9f67-b6776a0e3c52 | -14.97544 | -52.70374 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3819ba56-1c14-36f4-91f6-61b2f5829f78 | -14.35672 | -52.89031 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3543795-6360-394e-b554-0134658f4aee | -14.32325 | -51.84799 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8aab1d62-69e4-3e8a-9328-bb5fda5f4932 | -16.64194 | -49.40927 | 2026-08-25 04:27:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1bb291c-d62e-3146-93d0-6b1cd0023682 | -16.41903 | -49.92878 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50c967b7-bd87-347d-8df0-1648ec09ef0e | -14.35769 | -52.89571 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a45e7cb-b994-3f2f-9e87-02bbd3a6c7f0 | -11.43527 | -44.54459 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 430ed6c3-938d-3fbd-ba02-33040bc1cec8 | -16.41276 | -49.92314 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d80f661-a125-3a29-a4f3-eca5e2e8f60c | -10.85055 | -50.56032 | 2026-08-25 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22f547f9-745a-35f2-bc28-43c2554ccb74 | -12.74023 | -46.47539 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19a27b09-da52-3ebb-a18a-e65bc7f262f1 | -11.86505 | -51.69407 | 2026-08-25 04:27:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17117cf5-954e-3fb6-bd0b-5c41c98a8922 | -16.40924 | -49.92253 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac59adc4-b3d1-32e7-ac18-70ca74f181f3 | -17.75977 | -47.02822 | 2026-08-25 04:27:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3749753-0d1a-30c7-8a0c-0de4b539044a | -10.78739 | -50.93056 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 568cd114-ba4a-3a5a-986c-7dbfc1087470 | -14.35945 | -52.89938 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84be0ebe-1f00-3a7d-a076-fa1b7d31942c | -12.84269 | -48.49328 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91bb788f-f599-3877-a625-879b2f8af65a | -14.43042 | -51.78757 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c2b50a4-daa8-3ac0-aff6-a48e326fc988 | -16.40873 | -49.92408 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0dc531ef-aac7-395a-a877-2cce792999ea | -13.09665 | -43.36357 | 2026-08-25 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a9377a0-340b-3215-b97f-683a3b96bc12 | -16.41976 | -49.92461 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c0eae2d-55dc-3496-beb1-6f37b10dd610 | -16.40851 | -49.92671 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dee8213c-7c43-38a3-bf0c-6c6c95d3c6da | -13.87597 | -54.07695 | 2026-08-25 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 488217eb-7654-3a3f-b8dc-4669a0c4ef66 | -13.86599 | -54.00208 | 2026-08-25 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5eccae9-cb16-3414-922d-01a51d4cccc0 | -14.35399 | -52.92836 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9479cc8f-c374-33d7-8c0b-42c2fc04af50 | -11.09544 | -46.15932 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35ba37d6-0cdd-3c4c-8cde-20a3ad7e604e | -11.38829 | -45.16136 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85a89649-d76f-3837-be30-2c1d9df5439d | -11.4313 | -44.5252 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aec37bba-c0fd-300e-8397-f9eb7003cb36 | -15.32345 | -52.8234 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b5bdb2e-8c6b-3c9f-a33f-122ac2d5fff4 | -12.74797 | -46.46942 | 2026-08-25 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 891454f2-b393-368f-b02e-5e0c5d920cbf | -15.24076 | -52.79871 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3bcb0a2-2a55-38df-8ff1-72a355f0605d | -16.42611 | -49.86703 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a456171-5b00-3a8f-96bb-9517323ad4b8 | -14.73139 | -47.15462 | 2026-08-25 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 197b7d42-26c8-3a8c-a231-ba9daffa0a6a | -11.86436 | -51.69783 | 2026-08-25 04:27:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e68a3ec-675b-3eb5-91c4-c7da6b8d2d95 | -12.23481 | -43.18412 | 2026-08-25 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a130afbf-6ca3-3d88-8eb3-83be905a09ea | -11.57632 | -46.97327 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 34ed6ddf-65fd-3f7b-8187-e2bbb42a58e8 | -15.68082 | -42.47405 | 2026-08-25 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f8976a5-999b-3df3-b46f-1496f544d4e6 | -14.00229 | -44.05042 | 2026-08-25 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdcf7ac7-5af6-358c-878b-4a32d150b42d | -10.92088 | -51.07908 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c736d53-2934-3e49-9fb1-f69c37b2415c | -9.1973 | -59.57404 | 2026-08-25 04:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4e608e0-6629-3db1-8206-aa8a9bdf5f38 | -16.41626 | -49.92387 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d3e2977-0a42-3714-ab1b-64e654625cd1 | -13.08886 | -43.36666 | 2026-08-25 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8927c04e-bd9f-388e-b84b-d6f6881f0ff7 | -11.8139 | -47.64396 | 2026-08-25 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85ea9bce-ac86-3409-8e85-9953a5d7278a | -10.8067 | -50.9225 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ceb3548e-cbd6-3868-b9c1-4d4fed7fd9b8 | -15.55676 | -53.11414 | 2026-08-25 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d823682-97ae-38b7-9c9a-a845dfa264f5 | -12.71837 | -43.20313 | 2026-08-25 04:27:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2ab1df1-c932-3275-bbe9-87238f932906 | -11.81728 | -47.64455 | 2026-08-25 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7da47b5-88cb-3c70-b710-25edb448b73c | -11.98802 | -45.92714 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ea7eb88-af5d-34bf-a323-03bbc2f77701 | -10.92025 | -51.08269 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 429e875a-e46a-34c9-b091-f7a477cacf34 | -14.00638 | -44.04695 | 2026-08-25 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49eaaea9-9111-3810-815a-1b61b1cdfc76 | -10.78277 | -50.93338 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| e4713ea7-2973-3ec6-9650-7b26595d1635 | -10.93147 | -51.06618 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1e808c38-1127-3e16-8821-6ff1f0a7d8a5 | -13.10428 | -43.35011 | 2026-08-25 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6301e81-8afe-3c76-9b6d-933ca12443c2 | -12.84751 | -48.50059 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 17bfb6f9-4767-3af5-9c89-a077c494429e | -13.63686 | -49.02554 | 2026-08-25 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f6c7a29-15d6-3341-9651-660dba376912 | -13.64033 | -49.02624 | 2026-08-25 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18034037-590b-36cc-aff1-1595abd43f3c | -10.57912 | -50.40762 | 2026-08-25 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c50acac4-f800-33f2-8296-071d3a9d12bb | -16.40451 | -49.92764 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b7fe60f-08db-3dd3-8c30-ca63f3b0fe69 | -12.86882 | -48.50025 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31dbda82-7a71-3af4-a297-5aaa5d4c521c | -15.33693 | -52.79704 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6870f108-ab9f-3578-be37-c022152feae4 | -12.75851 | -46.44585 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 676ccbee-c6ec-39fa-804d-0210b0279599 | -11.77234 | -47.27458 | 2026-08-25 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da41eb1e-157f-3243-b28a-95b3937e5da8 | -14.24988 | -52.09536 | 2026-08-25 04:27:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1346420-9371-34c9-8e2b-8ccdd2976ea4 | -11.43415 | -44.55191 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79905aa3-00c8-3aca-aafc-b22b94672be9 | -14.91316 | -52.63932 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9e174bf-293d-3e5a-8b9e-d7c73818f498 | -12.73478 | -46.46737 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5527c025-7f0a-347e-8384-3634d56acc1c | -11.88282 | -43.82677 | 2026-08-25 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad576ce9-76fc-366f-bdfc-dd8315a67047 | -16.49961 | -54.67433 | 2026-08-25 04:27:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92757144-c357-3d89-b6a1-3f8285afcc16 | -15.7081 | -48.31753 | 2026-08-25 04:27:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d562147b-1afe-3fd0-92be-b7d7bec4f5e6 | -12.70695 | -48.39896 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29b33f1a-d0c8-3f14-a438-6496f5a546f6 | -16.40802 | -49.92828 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1deb9b5-49e7-3c22-bfa0-cc56b4733181 | -14.91735 | -52.64007 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23481ded-8a9f-319b-9876-4da15c141f68 | -16.41813 | -51.83319 | 2026-08-25 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efc20b90-f1f5-3eee-9194-a60f74c99f1a | -12.77507 | -44.2671 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38fa15d2-c836-3dac-891f-1ec090c3a45a | -11.42215 | -45.14129 | 2026-08-25 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ece55b3-1358-310a-bfc4-13cfd3bb4c45 | -13.09307 | -43.36304 | 2026-08-25 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58f5f94c-6a63-30c1-b65e-7317502ee42d | -11.57182 | -46.97988 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37fd4018-6dce-3782-83f2-7a1458723a25 | -14.87266 | -52.64795 | 2026-08-25 04:27:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a51156e-a89e-3e2b-946f-a74e1e5e05f9 | -14.97916 | -52.68365 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f00c6e7-7a54-3c1a-b31f-522bdd5fb1a8 | -11.57024 | -46.96854 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ffe834e6-c3b2-3dc3-b54a-2fae561277ee | -15.32833 | -52.82046 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf4672dc-5f18-3876-b1da-43aeafc4000f | -13.44691 | -43.84827 | 2026-08-25 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e911ef18-084d-39b2-8334-5440672a2fc9 | -13.34725 | -48.1997 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ecf6d58-d575-32e8-a462-13481081c204 | -15.70413 | -48.32064 | 2026-08-25 04:27:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a86bcd1-73df-3a36-b1e2-447696c44642 | -14.38519 | -52.95185 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0df2583-dd9f-3796-92fd-0086552215ff | -12.7029 | -48.40211 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55d79925-732b-316f-975d-db9d3368051c | -11.77569 | -47.27514 | 2026-08-25 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d868b38a-f2a5-3250-a128-75d984d2f495 | -10.91408 | -51.07042 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 5fa5c1e3-d51b-3682-aec5-682cd7db4ae7 | -12.11392 | -45.7311 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8030dc7c-adae-3182-b156-2b891b267b7d | -9.67639 | -55.09219 | 2026-08-25 04:27:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e93d54c-a726-3dfc-83fe-3f74730e7cd7 | -14.94581 | -52.72303 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5047a19-2669-37d8-bf02-85b3f56b73b9 | -11.97534 | -45.89984 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README41.md)
