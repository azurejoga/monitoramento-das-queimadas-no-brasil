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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2719bdc-1c69-36bd-8213-1fc23b9543d4 | -11.09839 | -45.7338 | 2025-10-26 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e358c157-5eb8-3069-9eae-01440b49090b | -13.62481 | -48.44015 | 2025-10-26 12:00:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 4748ef2d-5b09-3600-81ad-8faf0fdcceef | -8.0871 | -43.99979 | 2025-10-26 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| bf213ffa-9e7d-3f4a-9c9e-605ecb656235 | -13.05678 | -45.90728 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| dc2e643a-f3b7-3e94-bafc-37c4bd579570 | -6.37909 | -43.99992 | 2025-10-26 12:00:00 | TERRA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2fb6e860-7847-37f6-9906-4f7becd798c6 | -10.61762 | -46.60552 | 2025-10-26 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 1e53d15e-7e74-3118-847c-3e9d993eede5 | -13.03921 | -45.90858 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b66a9da8-e2d4-3885-908b-1be7cf421cd9 | -10.83148 | -47.62474 | 2025-10-26 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 3fca6c2c-22f0-399d-a0c6-b8a3fa26e9c9 | -13.24615 | -47.98373 | 2025-10-26 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ef4e5d48-0661-3174-9be3-fd50de97a00d | -14.62714 | -48.39079 | 2025-10-26 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 2dc93891-5064-32b0-8ec1-9697290d6256 | -9.24668 | -45.57745 | 2025-10-26 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 24e3f1a5-f277-3993-adf6-28a41b0c935e | -14.43121 | -48.08151 | 2025-10-26 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| dd185715-6304-357f-a82f-69b751c12f2f | -12.74272 | -42.92561 | 2025-10-26 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 595b5ed3-322c-37c8-a082-d1be2833df01 | -12.00901 | -46.77423 | 2025-10-26 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 3671c68f-0623-3397-bd53-ffcf4f151638 | -9.98157 | -47.08084 | 2025-10-26 12:00:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c5d725bc-08bd-392d-b275-94f14f45a76a | -7.14489 | -38.77645 | 2025-10-26 12:00:00 | TERRA_M-T | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 52445dda-2418-384d-b7a9-cd186d475d0f | -14.06772 | -41.78878 | 2025-10-26 12:00:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 6f30c7ac-13d5-34dc-98e9-9caa0220b856 | -13.04067 | -45.89879 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 491fd798-ea62-3f31-b32c-8d49fc23810b | -11.42096 | -46.04482 | 2025-10-26 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5eb0ee89-74b1-3fcf-8c11-ba8887d1c32b | -12.19394 | -42.96198 | 2025-10-26 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 68e7db8b-0ed2-3c06-94a7-6b7b3c8abbe8 | -13.06446 | -45.91848 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa7cf1de-f74c-3521-8f16-70ad644526f0 | -8.49633 | -44.73244 | 2025-10-26 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e11ac6da-fbc3-3d21-a446-866ce46e7265 | -7.85717 | -46.42057 | 2025-10-26 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0c14e368-134a-30d0-8f1f-8f43d6912461 | -11.4069 | -46.0743 | 2025-10-26 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2eab8d35-fab0-383e-ac7d-1044f159fc37 | -14.22682 | -42.3035 | 2025-10-26 12:00:00 | TERRA_M-T | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c4933c53-d287-31db-9b49-962eb8a4680b | -11.39751 | -46.07273 | 2025-10-26 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 63ec3f2d-5f38-3706-9aef-25628ca7b49b | -7.69347 | -42.18568 | 2025-10-26 12:00:00 | TERRA_M-T | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ad13a8d7-5f8d-3007-9952-a488894cc69a | -7.85892 | -46.40897 | 2025-10-26 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| ca08e1e6-59b2-3ccb-be57-fce6dc575e7d | -16.21564 | -45.65071 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ce93686d-6988-31d6-a1e7-6144ca1c00aa | -8.78704 | -42.78669 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 38addc65-7205-3859-a8a4-650fe017b594 | -12.31236 | -47.46048 | 2025-10-26 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9812f082-4b43-3481-aa34-f91b154e5a12 | -11.87178 | -43.28666 | 2025-10-26 12:00:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| abacef08-cef3-3516-8bdc-ad6f3ae0d2f0 | -7.6184 | -45.68204 | 2025-10-26 12:00:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9f2a2ab9-dcd7-3741-adc0-6fb90e939db4 | -16.6207 | -44.57732 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| a7501066-18ff-3fec-81f7-d73783e9e1ea | -8.03792 | -45.14634 | 2025-10-26 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b2df1a02-7754-3317-a619-1d8e26f0685c | -14.0462 | -43.02498 | 2025-10-26 12:00:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6826556d-a4f9-3665-8431-6730bf2ccc11 | -8.66751 | -44.76059 | 2025-10-26 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c2f452f5-9bf1-3d8c-934f-13b7483b3078 | -6.93324 | -44.86996 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b41a65e4-a916-300f-998e-135f747c448d | -8.66611 | -44.77009 | 2025-10-26 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e4a40879-68d8-39c2-83f4-28808bb270cc | -8.08577 | -44.00883 | 2025-10-26 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 29c8760d-1d50-36b1-a9d0-1a0613a6d7db | -10.40948 | -45.33835 | 2025-10-26 12:00:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| e16bbd74-5b06-370a-ac3d-08ec227bf506 | -7.80588 | -45.3999 | 2025-10-26 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 70b9409b-9744-361c-85b3-0a51aa943c36 | -7.01637 | -44.69173 | 2025-10-26 12:00:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 25e1441b-d6b7-393d-b751-13cd8608281b | -10.51049 | -46.57007 | 2025-10-26 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 016f52cf-9e2d-3dfa-860d-47a84bbdb255 | -7.27203 | -39.20544 | 2025-10-26 12:00:00 | TERRA_M-T | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6bb00d5b-0248-395e-bf21-4ce3eaf65777 | -8.05189 | -46.75392 | 2025-10-26 12:00:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 8bed4d7c-edb7-3cdb-86af-f0f86a7126e3 | -8.04346 | -46.74021 | 2025-10-26 12:00:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d7850b01-36ac-3821-81ba-abdf1b7f94a8 | -6.39492 | -45.77881 | 2025-10-26 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 195.5 |
| b45d6996-76f7-3fef-89cd-a2b111550246 | -14.62919 | -48.3781 | 2025-10-26 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3bb4f2ab-3cdc-377c-9fd9-371e722e2fe6 | -7.81204 | -43.98734 | 2025-10-26 12:00:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 68b0cdc7-c564-3d16-aacb-f86cf53fd68d | -16.34557 | -46.6399 | 2025-10-26 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 87f1e950-f93d-3d7c-9311-4724b5a2fd6c | -14.19845 | -48.1848 | 2025-10-26 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f51ce52d-f641-34d8-b343-986bbe5ac011 | -11.59058 | -43.31941 | 2025-10-26 12:00:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a38a685b-d1d2-30f7-9745-6465ed9d797b | -15.55911 | -43.00589 | 2025-10-26 12:00:00 | TERRA_M-T | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 24.8 |
| cae3c865-4043-313c-ab02-3ffb0357fa41 | -10.83652 | -47.63221 | 2025-10-26 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 33448a58-33a7-300a-a9bc-8f96405006da | -16.1535 | -45.94779 | 2025-10-26 12:00:00 | TERRA_M-T | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8b80517b-0b03-38c9-acfd-f673d1ca5c85 | -6.74645 | -45.33901 | 2025-10-26 12:00:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 20be5a9e-7f89-3e2b-9e1c-164b7c39262b | -6.55026 | -41.5904 | 2025-10-26 12:00:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| f6794c17-7057-340a-a0ec-86b7ab004904 | -14.42533 | -46.265 | 2025-10-26 12:00:00 | TERRA_M-T | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0dd4f825-6af6-38b6-8d2a-1a5c116db976 | -8.00933 | -47.38736 | 2025-10-26 12:00:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f5bbe2d6-9913-3934-925f-6ffd68786cab | -10.35595 | -47.11423 | 2025-10-26 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 54ce9d76-26b2-3765-96cc-3fe1c9741fe4 | -13.18669 | -46.86113 | 2025-10-26 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 03965374-4eae-325c-a6a9-be11271004c9 | -6.84763 | -44.01363 | 2025-10-26 12:00:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 81032944-c522-38f8-931c-61163e5ea7e0 | -7.3393 | -47.11587 | 2025-10-26 12:00:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 60806323-0182-3075-9a1e-2940d9f37b15 | -13.07066 | -45.93947 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 2b4ff6eb-819d-365a-a2cc-8fa3702407ce | -8.53597 | -47.2038 | 2025-10-26 12:00:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 88121dc0-c6d3-3876-8f91-75f170de2ee8 | -7.97141 | -45.10003 | 2025-10-26 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| bd6139d2-137e-3372-b2bd-51e06a3d62b3 | -13.07363 | -45.91989 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| bdfafba1-70e0-37b4-802f-67d12956de59 | -13.51207 | -42.07374 | 2025-10-26 12:00:00 | TERRA_M-T | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 2c60dd27-e9c4-3ba6-8a96-0b9880e44572 | -12.70151 | -42.28915 | 2025-10-26 12:00:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 43.0 |
| cba015ca-2ba4-3c1c-aad1-2a4ee82674b7 | -13.88491 | -43.12371 | 2025-10-26 12:00:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 4e5f553e-1848-3759-b12b-d09f4f81768b | -12.90699 | -42.27039 | 2025-10-26 12:00:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0cd59c31-3c19-3909-9c97-328b2ecdaeba | -10.41091 | -45.32874 | 2025-10-26 12:00:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9bc9f044-6ea6-3e65-aeaa-d0773fa34d33 | -11.38964 | -46.06118 | 2025-10-26 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 213a0cfd-b91a-3be7-98b7-eff79af42d5d | -10.4138 | -45.30934 | 2025-10-26 12:00:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fca84dbc-2c27-33d2-8679-ff2b1209d98e | -6.38505 | -45.77732 | 2025-10-26 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 09fcf165-be1b-3505-9879-9bcfb81450f3 | -10.16502 | -43.47138 | 2025-10-26 12:00:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 82a6a636-2822-3b8f-ba30-775e72192659 | -15.71988 | -44.04477 | 2025-10-26 12:00:00 | TERRA_M-T | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6e7ac8dc-aac9-3830-ac8a-cc93979e07f6 | -11.87305 | -43.27765 | 2025-10-26 12:00:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 05e4669f-25b7-38cc-95a0-977219aff7e4 | -7.2422 | -44.97417 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2228d39c-3668-3748-bace-024c9f8856ff | -13.32466 | -47.93807 | 2025-10-26 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ac223b02-11e3-3f2e-a30c-3c590e937035 | -7.97287 | -45.09012 | 2025-10-26 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c463f25d-2148-3c03-b966-d390c5a7f5de | -13.90034 | -48.44886 | 2025-10-26 12:00:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 18765619-7a05-3ed9-bb27-cc7a4d7eafa9 | -6.56169 | -43.63818 | 2025-10-26 12:00:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c123ff5b-d40f-3967-a153-36cfe1d20ff4 | -7.7885 | -45.38681 | 2025-10-26 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 20ab88a9-f2ae-3540-a479-caadab7ad90a | -7.8453 | -46.43084 | 2025-10-26 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 8f29883e-a4f9-3a8d-adef-7fe0d194cfaf | -7.81071 | -43.9964 | 2025-10-26 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 61cc6c6f-9e58-3ab4-ad19-c97ce83facba | -19.88019 | -46.95674 | 2025-10-26 12:02:00 | TERRA_M-T | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| da157a6a-0eed-3856-9608-515dd6a22709 | -17.33067 | -43.65045 | 2025-10-26 12:02:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 04ec912d-a956-34cb-8813-b8d3af93c65a | -19.32623 | -49.8111 | 2025-10-26 12:02:00 | TERRA_M-T | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c71a7121-6e3a-3e6f-ba97-1dc564b95c32 | -17.32298 | -43.63943 | 2025-10-26 12:02:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c54ff3ab-5bf1-32f7-9087-ee5a2f8e0c37 | -17.41611 | -46.88827 | 2025-10-26 12:02:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 71669d00-3900-3036-9d7f-d144f1279a7e | -18.47572 | -44.42945 | 2025-10-26 12:02:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6d0dac17-a236-3be5-b1fd-c2f0511b1c09 | -18.47404 | -47.15721 | 2025-10-26 12:02:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a1b3e557-8d04-3fb4-a428-98529ab7a948 | -17.43486 | -46.87751 | 2025-10-26 12:02:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 2881aeb5-7c6d-3de6-8370-8c55090e30a8 | -19.87873 | -46.96643 | 2025-10-26 12:02:00 | TERRA_M-T | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b2388fee-1e77-3cfb-9e10-47ff648a4f37 | -19.16117 | -49.12679 | 2025-10-26 12:02:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 96945032-8c69-3137-a584-45b6d32443d0 | -17.32031 | -43.6588 | 2025-10-26 12:02:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0c502a03-dcdb-39c3-8f18-b5d4973c58a7 | -19.98623 | -43.751 | 2025-10-26 12:02:00 | TERRA_M-T | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 66e2aeb1-9d02-37c2-bf06-1f16017f382d | -17.42723 | -46.86615 | 2025-10-26 12:02:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 29.4 |


[Clique aqui para ver as próximas entradas](README57.md)
