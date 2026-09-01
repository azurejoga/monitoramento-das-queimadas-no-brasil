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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ad69eb4-81f3-3953-bc0a-78cbda7573e6 | -7.68676 | -55.34126 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7dd25a3-c409-31ea-9117-27655b8908eb | -5.95017 | -57.68871 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab17428f-ffcf-3655-80d5-a146a9015e4b | -7.34609 | -60.58652 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 36d79e06-2fd1-3d38-9c10-2dac00eb3fee | -10.74055 | -47.98506 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f43f2428-a19b-3cc9-9c82-c72f4cc226ea | -8.23676 | -54.93686 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1ce35fd1-b5d8-3560-9bb3-fcb88cb43f3d | -9.95399 | -46.77253 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59d23609-dd84-34e4-901d-0f50aa8ef542 | -7.33016 | -55.14645 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 817fa18b-19c0-3ae4-8945-26df18a82009 | -4.96575 | -55.84343 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8d0e201-719d-339a-bbdc-a9c18b4f99a9 | -8.08637 | -45.45716 | 2026-09-01 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 91337ca4-b38e-3178-a99f-9400f1e1223c | -7.04181 | -59.23159 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ff5f49c-26f9-3188-8f6f-95592f0c971b | -10.2089 | -50.31504 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0b30ddc8-3287-3272-bfe6-7f6d3d2f6972 | -10.86397 | -45.35612 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eec22984-9b29-39c9-8673-60f9dc3d6da5 | -11.31282 | -45.20167 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89d4e254-1501-36d6-aab0-1509d90f5eed | -6.95404 | -55.63926 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f10ef2c2-1676-3fa7-8d8c-390a80dbb367 | -6.25033 | -55.43442 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b16f552-efd0-35cc-b459-73c2cc55fc10 | -10.15315 | -48.90807 | 2026-09-01 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc27ba73-e281-395a-b442-063f123a07a2 | -8.08324 | -45.45805 | 2026-09-01 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9705db90-0b99-3f9a-b1d5-fbd35262f2ee | -11.4898 | -45.10123 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1e48bed-59ad-367e-a5f7-e1b369b204b5 | -10.16249 | -45.76469 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7b42c1d9-214d-3b0b-a716-44def615e66e | -10.51581 | -57.44114 | 2026-09-01 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03fa8347-c459-34be-a4cd-3d575a35ecd8 | -9.17703 | -59.63266 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 655286b6-a02c-373d-a9bf-ed7ddfe47214 | -11.24763 | -45.13737 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fa44392-5483-39c4-9ef9-c79a8fa8df66 | -11.4876 | -45.09562 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9b90d42-a278-32f1-a3bd-c109d396eaa7 | -7.35275 | -60.58333 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 06947677-a05c-3e4e-9630-85fc5d075490 | -8.50264 | -55.31215 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a8b6c87-4a74-3c47-8709-f09e40b99bbe | -6.91663 | -55.70348 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b9426a7-fa2b-3b97-9506-b6d42e40f7cf | -9.89321 | -60.27596 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29727600-cb39-3dee-80f8-241bcfa813cc | -3.61203 | -59.06901 | 2026-09-01 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3efa229-1f72-34a6-8cd6-c0f3493c3053 | -8.45476 | -47.54705 | 2026-09-01 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6129940c-fbd5-356a-81c9-0daa8d8f8440 | -10.36532 | -50.00714 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8cd060c-0de3-35c4-a9c8-a2af920d5b7c | -6.68186 | -41.66422 | 2026-09-01 04:40:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07ded1f0-00a4-3e39-beb8-24cc26817d05 | -11.25907 | -45.11604 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7af1a58-763c-397a-8332-fbaeffcd6188 | -10.04985 | -48.68964 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d92652fb-1c31-37e7-9859-57713b1ebe9c | -10.43235 | -46.53109 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65243185-321b-3623-8d55-55d947e5803d | -5.9457 | -57.68492 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae6cf6c8-406f-3650-9674-7fdfad8eb77f | -9.94539 | -53.99573 | 2026-09-01 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de15ac41-ef6e-3bcf-9c15-5cfb11bc7984 | -11.65328 | -47.60696 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f29080b7-ffca-323c-8989-cb65d8d6035f | -9.99917 | -46.44721 | 2026-09-01 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b32e42c-9f85-3212-bed0-1d8307da5b79 | -3.34232 | -59.43428 | 2026-09-01 04:40:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 206689b5-7c04-3670-99e3-d72d15d03bcd | -8.27849 | -54.93275 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 55284bd1-57b4-3e04-a45c-6ad44a665734 | -11.00367 | -48.38068 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55e0927d-25ab-3d23-85d6-0d98ff8f162b | -11.71696 | -47.63655 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c51a272f-1253-37f8-aad7-b6df6c84223f | -10.03084 | -44.6974 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9d3d262d-54d7-3596-89e9-a5dafccca853 | -8.27503 | -54.92893 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 2de64d6f-36aa-3d40-bea9-2c33829a3da8 | -11.25177 | -50.58294 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61157b0c-2261-3869-be56-aeefe02154bf | -8.29796 | -55.11114 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 580ca5f9-d1a6-322a-8bed-a12278da0237 | -7.90256 | -44.26367 | 2026-09-01 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe08a319-f5ec-3db1-b1b0-230e080b8774 | -11.32128 | -45.1706 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18af8cf0-6abd-360e-898b-22018cb6c2c2 | -10.03504 | -44.69806 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5e61cb0-dd26-3656-aefd-6010622e780e | -10.75052 | -54.03263 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc6ff667-b8cc-3f99-bdc5-ce4694a47b79 | -7.55683 | -54.99426 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1df33cff-fb7e-3392-95f7-411bfc4c4404 | -11.06154 | -51.51072 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01777254-08ca-3124-a41a-e0ab344826c6 | -4.0909 | -54.09662 | 2026-09-01 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62e08863-5af3-39ab-b3ca-9d3b03ca0ae5 | -5.25459 | -55.90697 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6611075f-d0f2-334d-b7df-7c659a3047b2 | -10.74698 | -47.99007 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3e10f33-d595-3b02-858d-3b63b1057da5 | -6.11055 | -57.8644 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 959b0195-fa5f-3adc-ba45-34e5c410fd33 | -11.32233 | -45.16297 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9b4e89f-de2a-3a76-a564-3e7d0ae06a15 | -10.7569 | -47.97812 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88c1c518-7972-38b5-9203-984aadf2e98f | -11.66594 | -47.59602 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d261b119-892a-3268-a5cc-2729eafa15e4 | -8.71168 | -52.36834 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 205e96c9-af3e-30b6-acd9-e7cde3770fde | -6.26511 | -55.42445 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e50507d4-7803-335c-9b92-74698f3952cf | -6.61207 | -58.59881 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d0d139-0518-3a9d-9ef5-3f66ef714f3f | -6.18001 | -57.72917 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 26fb1439-2fa8-3955-bcdb-558896f503f0 | -5.87741 | -57.78137 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73384aa8-deaf-3d26-a4f3-4ad6ec06b367 | -8.21345 | -54.94172 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9138bb4-e13a-3f1f-8e45-7ae4cd9175bd | -9.15436 | -59.52901 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2025be7-c2e3-382c-b31b-4d9c715ba5e8 | -11.91209 | -45.07603 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 481c6d8a-2fb7-30cd-87ca-6f58dd745679 | -5.96415 | -57.6969 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bf342d3-4098-3684-a12f-b1b868bcd62c | -8.93472 | -45.04041 | 2026-09-01 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d04974ab-5f08-3460-bb03-f79f8e3b3ca9 | -5.24854 | -55.88784 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3bd82af-9727-39fd-a064-547fa21bdb69 | -6.95868 | -56.43313 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce75d2e9-fc2b-313a-bbf9-505d4d62b4b0 | -8.01457 | -48.00974 | 2026-09-01 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41355410-18c6-3639-adb4-537de5359823 | -9.89251 | -60.27961 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d1d1d4e-bdb3-346e-92dc-046e26d2ad9d | -6.15566 | -57.78068 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 607a8e74-71af-3c1b-a2f7-ed0e2eec0c36 | -11.66049 | -47.60807 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 13ae376c-186a-335e-a93f-536cc76d8d64 | -9.13617 | -61.09693 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66f7dfe5-7dbe-3a9e-bbe0-ddc9aa8a3f0e | -7.91249 | -61.33657 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0198e63b-595c-358d-b069-7d952187df22 | -10.34213 | -50.00296 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77f57640-aa85-3533-875a-413000f2c11f | -5.25315 | -55.91581 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e0502c5-38b5-3151-9686-bf8465d9a045 | -8.5024 | -55.31287 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e36cc7e3-0460-3cff-a9da-d9d319915f05 | -8.93578 | -62.36186 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f083f2c-a78e-36f5-9f4d-b61b1b7d9c87 | -10.06368 | -59.40434 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8193afac-fda2-3ded-8322-9d3073194a9b | -11.48564 | -45.10057 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f128b6b-6f09-3b45-a165-cabe1be4639a | -9.47948 | -57.02663 | 2026-09-01 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8631ed1f-2ea4-340a-9d03-1cab6b361859 | -11.51615 | -46.92663 | 2026-09-01 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3d43ad0-d9f9-357a-9679-ba195ff23ed5 | -7.03701 | -59.22705 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0fc37c1-353a-3107-ad8d-6781be3a3d5f | -10.83421 | -50.70897 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea6fe087-1ff8-35a3-967d-9635abdd0355 | -7.28988 | -49.82204 | 2026-09-01 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 856107f3-14ac-3752-aa04-cbc69ce0bdc6 | -4.97095 | -55.83982 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d84134a-e0b8-331d-b2f5-d70c944857d6 | -6.60515 | -58.60757 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4d2db93-494a-3e81-81c2-2fd7c3ad5700 | -8.24241 | -54.95175 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a94dd70-1755-380f-ab90-29e1cf120f93 | -3.63854 | -60.55638 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a012c429-d2ca-39d4-9873-a741838b81b1 | -6.25428 | -55.41085 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43485f5b-5526-38d4-b276-5c470903efe9 | -10.06461 | -48.707 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9daf5ca7-1dfd-32fe-9acf-71b8a6bd521a | -6.38646 | -55.2196 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df1ea878-fae6-3523-adb2-8fcb5a13a93b | -7.3521 | -60.57752 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b34f968e-f2a8-3520-984a-a1bb75ac8b0e | -6.75815 | -56.33694 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 092b9468-f7c4-39b5-a8e1-603768745d00 | -11.37068 | -45.22899 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5262908-7a30-3964-8064-a0c79eeb5ec0 | -6.63189 | -53.17574 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44398aa4-6957-312c-9dd3-0cb4245da392 | -10.35592 | -50.00206 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |


[Clique aqui para ver as próximas entradas](README44.md)
