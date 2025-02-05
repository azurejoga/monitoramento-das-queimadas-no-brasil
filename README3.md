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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e88245c6-2d00-31ec-af70-7e1ce7485492 | -6.03587 | -46.25915 | 2025-02-05 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc5908c1-8e03-3db1-a480-e9ceddb6a695 | -8.70979 | -36.163 | 2025-02-05 04:08:00 | NPP-375D | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 056412ba-fa6e-3055-8b94-aa7a23cc20a6 | -10.34005 | -38.03005 | 2025-02-05 04:08:00 | NPP-375D | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13bcfc31-c957-3532-bcc4-4ed5628c003a | -5.62625 | -43.62995 | 2025-02-05 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d82d3d9-ed1c-3dba-af8f-55673ac5f662 | -6.23293 | -42.79411 | 2025-02-05 04:08:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eef8779d-4dd8-3af8-b9f6-7d438a63d2ec | -5.25554 | -45.2415 | 2025-02-05 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12e85421-a4c3-38e5-bf4c-e93f15064b88 | -7.04642 | -44.39281 | 2025-02-05 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 764fd953-f1ce-34e8-8b30-64d35a8db95e | -7.05475 | -44.38616 | 2025-02-05 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69e7c768-035c-3b4e-bca0-f0c809a00bbe | -11.12333 | -43.36151 | 2025-02-05 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 502b9c7b-3a7f-3c18-9174-1093523c99c0 | -15.64794 | -39.19183 | 2025-02-05 04:10:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7c19e4ec-13d8-39c7-90e9-52801c176b36 | -12.54034 | -48.32583 | 2025-02-05 04:10:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ebd7f04-feec-3afe-a07e-9132033d8e0b | -12.53968 | -48.32946 | 2025-02-05 04:10:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54c76f61-8731-3860-9784-68c7504bdec5 | -12.4873 | -43.78557 | 2025-02-05 04:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35bf4223-f602-3cc2-b96b-900feec292ee | -16.6794 | -43.88482 | 2025-02-05 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5407913-2b26-3b59-bd9b-552b958a344c | -17.71664 | -43.45228 | 2025-02-05 04:10:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf3a674e-d5a0-3f6a-8ac7-a6e08563ed00 | -14.13549 | -41.69224 | 2025-02-05 04:10:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb24e83f-8b04-3a99-a2d4-0d0f18bf3263 | -12.87824 | -43.47717 | 2025-02-05 04:10:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47a0c515-ba05-3d9d-b5cf-563f13d8bf64 | -17.09392 | -43.80552 | 2025-02-05 04:10:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe7195ac-3b03-3ca5-afe1-471ace19d289 | -16.0364 | -42.13702 | 2025-02-05 04:10:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 962e0c44-2636-3e3a-a400-27374c7c0420 | -16.87111 | -40.69697 | 2025-02-05 04:10:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 75bba20d-b457-38cb-aa71-cce40c10ed6b | -14.12016 | -41.67784 | 2025-02-05 04:10:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7269879a-f65d-3912-a2a1-db62a3a95020 | -11.45744 | -40.7129 | 2025-02-05 04:10:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 005f2813-7a1d-351c-8e52-52a1833784e1 | -14.25662 | -39.15215 | 2025-02-05 04:10:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 328764ea-0374-3460-aabd-69b7b9048b1b | -11.47117 | -44.9579 | 2025-02-05 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22fcc057-35f7-3dc7-ba5d-daee8ffa5433 | -16.88145 | -40.62454 | 2025-02-05 04:10:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a367d634-28fe-348c-a30a-1529fb2993e9 | -17.37839 | -42.48404 | 2025-02-05 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3d21712-48ba-32f8-9993-1384e91197dc | -12.53626 | -48.32511 | 2025-02-05 04:10:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36b26cc2-ddd2-3c28-b2b2-052f9564daf6 | -11.02455 | -45.05285 | 2025-02-05 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c35bfa5-846d-3bbe-bad5-5611f9223e10 | -17.59432 | -43.19887 | 2025-02-05 04:10:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a86bb818-5456-399c-b9ce-c8d01b6d04da | -12.65108 | -43.81587 | 2025-02-05 04:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7353ae14-5582-3ee4-aa70-728141245e6f | -17.14584 | -41.40361 | 2025-02-05 04:10:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8cfd7742-cef3-3b04-94d9-277cf17105a0 | -17.71329 | -43.45171 | 2025-02-05 04:10:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e4306a0-1105-34f7-bdd1-45b8946d1ea5 | -10.95149 | -40.73509 | 2025-02-05 04:10:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67adae7f-76a2-385e-b130-63b5624dba8d | -15.75103 | -42.64765 | 2025-02-05 04:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5dd57b09-f096-3734-b403-9da8ff2d06b4 | -12.49064 | -43.78613 | 2025-02-05 04:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b7bba2b-25b0-3afa-a5b0-ac7edf67dcbb | -13.98233 | -44.08794 | 2025-02-05 04:10:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1a85873-876a-3e2b-af95-82320a19a08b | -12.65051 | -43.81944 | 2025-02-05 04:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf88d36b-401e-3063-8600-9084cc46afbf | -11.02472 | -45.05588 | 2025-02-05 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 825c83e1-d771-3a23-9432-b1a2446d1a78 | -17.20413 | -40.32623 | 2025-02-05 04:10:00 | NPP-375D | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0e587207-3299-3f8d-a352-c91a939c7d0e | -12.48673 | -43.78915 | 2025-02-05 04:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f45b7fab-3246-376a-9fa7-da19bceddb6b | -15.7544 | -42.64822 | 2025-02-05 04:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 49e7ef26-a30f-3e63-bb16-13b43988c6df | -18.00898 | -41.94781 | 2025-02-05 04:10:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7910641c-8268-321e-b29c-9f1a41e3b3a5 | -11.02391 | -45.05676 | 2025-02-05 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bfbbdf3-5777-3c42-84e2-78841a8e42c6 | -11.46957 | -44.95863 | 2025-02-05 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be434c40-7a78-3dbf-a4d8-f0163e3f0f1b | -17.77904 | -42.81038 | 2025-02-05 04:10:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69b4266a-34d2-3ea3-8e24-9edb6459be5a | -17.1494 | -41.40408 | 2025-02-05 04:10:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6dde91d3-da21-34bc-bd3f-06a5c29518f8 | -11.11999 | -43.36096 | 2025-02-05 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6c0d8644-7aea-330d-b8db-bf70340dbada | -17.82036 | -45.31755 | 2025-02-05 04:10:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a9cf131-b3c4-3ebb-8e78-5ebd57e56a1e | -10.94804 | -40.7346 | 2025-02-05 04:10:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 45be2efc-d397-3251-bf76-3ba3647a2c9a | -21.88557 | -41.08991 | 2025-02-05 04:12:00 | NPP-375D | SÃO JOÃO DA BARRA | RIO DE JANEIRO | Brasil | 3305000 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17c67ad9-57da-3452-9e76-86eac8f03f30 | -22.8573 | -42.58027 | 2025-02-05 04:12:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2c8b99fb-8b3e-3a16-aa15-c3f5933f1ae9 | -20.41597 | -43.55335 | 2025-02-05 04:12:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3006ef30-c1cf-33fe-bca0-77ba19b25213 | -21.07524 | -56.39391 | 2025-02-05 04:12:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2b686f5-f0d5-32c9-851d-c697c74a0ad2 | -23.59069 | -46.31647 | 2025-02-05 04:12:00 | NPP-375D | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1884a7ad-eec9-39a9-a183-5808e92d0a2e | -19.1465 | -40.52544 | 2025-02-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c060c933-02d0-38e7-bc44-1eb50d87ef83 | -20.34651 | -40.35936 | 2025-02-05 04:12:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4d2e0868-1d7d-33b7-abd1-332f9def9c7d | -21.62672 | -43.46796 | 2025-02-05 04:12:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 98ec8bcf-6fb2-3426-9a96-d7edec9c514c | -21.88238 | -41.09272 | 2025-02-05 04:12:00 | NPP-375D | SÃO JOÃO DA BARRA | RIO DE JANEIRO | Brasil | 3305000 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 30fab75e-4927-3780-8608-551ca6c09f87 | -21.17787 | -43.98064 | 2025-02-05 04:12:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 30870a45-25fc-3e97-b02f-d87fd43aee50 | -20.00864 | -41.42144 | 2025-02-05 04:12:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c57d15ad-7694-39ef-ad6f-ad5c00683187 | -22.67449 | -42.85437 | 2025-02-05 04:12:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| caa7b827-1670-3c21-9b27-f483fe8c9cba | -22.7851 | -43.75606 | 2025-02-05 04:12:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 141679bd-3ddc-3ee3-9a3e-66fbd6986ced | -27.08584 | -50.5085 | 2025-02-05 04:14:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5b86ab48-5534-33f2-82c1-7347e22909cc | -29.75755 | -54.76438 | 2025-02-05 04:14:00 | NPP-375D | SÃO VICENTE DO SUL | RIO GRANDE DO SUL | Brasil | 4319802 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 65e61318-9136-39d4-aaa1-1b505f3bc0de | -29.88814 | -51.23539 | 2025-02-05 04:14:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 213c9770-8d59-3789-bfc4-068ad60f0ef9 | -29.9526 | -51.61653 | 2025-02-05 04:14:00 | NPP-375D | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| c8a764ab-e71f-3b96-b5fb-a6a1f998120f | -27.08949 | -50.50941 | 2025-02-05 04:14:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6d8943d2-fca9-38c1-a69e-d0b08550af25 | -27.96761 | -51.63673 | 2025-02-05 04:14:00 | NPP-375D | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c2bd89fe-3b3e-39b6-a7c1-6b8d4ce7d0af | -29.89178 | -51.23629 | 2025-02-05 04:14:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| cf82e4f1-04bc-3c8d-8131-12828f8c440d | -30.51288 | -52.05256 | 2025-02-05 04:14:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| e0b5b0ce-df21-33de-9f3a-a5bfcbf2e1ec | -31.73201 | -51.56649 | 2025-02-05 04:16:00 | NPP-375D | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| b3c9d683-9601-35c9-b966-88bc9c0452c9 | -2.58312 | -51.93851 | 2025-02-05 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95a0cbb7-9cfd-3fc3-b636-2755b1360154 | -2.79595 | -54.14715 | 2025-02-05 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e373855-b588-325e-b7f9-66492ab8c480 | -6.38265 | -43.66818 | 2025-02-05 04:29:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 255a8d05-5474-3861-bfd4-2d6196a6755b | -5.86013 | -46.25032 | 2025-02-05 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a356255d-b5e8-3137-8e1a-ea5e467bfd35 | -2.12031 | -47.12709 | 2025-02-05 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09fe9ba5-fd0c-34ba-b5e8-549caecaca6f | -6.03375 | -46.25448 | 2025-02-05 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 259b04ca-6777-39a5-b618-c6c20febf711 | -2.58595 | -51.92109 | 2025-02-05 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ed4d1da-4157-3505-bd97-0676929578f2 | -2.58539 | -51.92455 | 2025-02-05 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9788957-5cac-3dd4-b19d-8a5bcd01b478 | -5.95134 | -43.36307 | 2025-02-05 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 81782d9c-587f-36bc-b6aa-bfa62a8a6fef | -6.03319 | -46.25808 | 2025-02-05 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbfc8dcb-b6f0-3f62-917c-9635d10699fd | -5.85619 | -46.25343 | 2025-02-05 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1655c44b-e1de-36ba-881d-148435160aef | -6.41408 | -35.64738 | 2025-02-05 04:29:00 | NOAA-20 | LAGOA D'ANTA | RIO GRANDE DO NORTE | Brasil | 2406205 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ae82b739-617e-3eba-a1fa-bbf6a5cc3b72 | -1.87834 | -48.71553 | 2025-02-05 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d942ae1-62e7-3adc-8e69-c34484aa1e6b | -2.58139 | -51.92395 | 2025-02-05 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36fa6e1f-0f3d-381d-9836-db53dd40a027 | -1.87893 | -48.71187 | 2025-02-05 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9aaa3904-d312-3cf7-bdc2-557f0b1babc6 | -4.83507 | -38.40599 | 2025-02-05 04:29:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ede2f0b6-f740-3e85-bc0b-f217de6e876b | -6.97614 | -42.99128 | 2025-02-05 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd9cc05e-6960-334e-b143-9501e4db8b00 | -3.01258 | -46.70393 | 2025-02-05 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10964c13-adaa-33e2-b182-303341936180 | -6.98017 | -42.99189 | 2025-02-05 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6f738bae-9ef7-3700-940f-265ce44799db | -6.41325 | -35.64842 | 2025-02-05 04:29:00 | NOAA-20 | LAGOA D'ANTA | RIO GRANDE DO NORTE | Brasil | 2406205 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2be2449f-9361-3dba-9fbf-1005867ac0e6 | -3.00927 | -46.70342 | 2025-02-05 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 935c0e5c-3f0a-3df4-9da1-a9542de64531 | -7.66894 | -46.09888 | 2025-02-05 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e321a0a-c079-3dba-8027-cc7e225bd1ee | -12.48772 | -43.78942 | 2025-02-05 04:31:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 835d6f74-4090-3b59-ac1b-a9155f79b2e2 | -10.95272 | -40.73682 | 2025-02-05 04:31:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0df9fadc-c9c4-34c2-ac66-7354ad641561 | -10.9477 | -40.73642 | 2025-02-05 04:31:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 46b9e02b-1dd8-3b01-98e2-3b799fc79eec | -12.53526 | -48.32363 | 2025-02-05 04:31:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31b3cc89-9ac0-33f6-a6f7-aebc5ac24626 | -7.0446 | -44.39223 | 2025-02-05 04:31:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75ab9fdc-f858-306d-96e4-bdc00c9a4186 | -7.04327 | -44.4011 | 2025-02-05 04:31:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cdbef21-495a-3ac8-885b-711320e53e7f | -11.12068 | -43.36263 | 2025-02-05 04:31:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |


[Clique aqui para ver as próximas entradas](README4.md)
