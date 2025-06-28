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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d85c0cb-cd64-359e-8b29-4ae24e39bc70 | -8.00456 | -49.71137 | 2025-06-28 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46b60942-430e-3aa8-926c-cb36511c6918 | -6.9439 | -42.88599 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 411e1a5b-be9e-3971-be0e-11e9c84be37b | -9.68969 | -48.33157 | 2025-06-28 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c886d67f-5991-3ccd-840e-5b6bdc331e73 | -6.94825 | -42.88219 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 71102e89-a444-331a-a27d-fad3d968cac0 | -8.04646 | -47.64525 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfef13d6-02f6-3873-84b8-21fe1228ae08 | -7.21239 | -43.08103 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8d43a5f9-d1e6-376a-a199-b96be2ba82a7 | -10.27178 | -44.64557 | 2025-06-28 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a9c76de-b701-3ccf-bcdd-4d794d1d8463 | -7.39255 | -44.55506 | 2025-06-28 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8860d212-2035-38e3-ba69-9aef2952378a | -9.11678 | -49.47517 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa52e7c4-e41c-3bb7-9676-c258ac34446c | -2.50151 | -54.13278 | 2025-06-28 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 795db963-9bdd-345f-a428-f09077498fbb | -4.12313 | -43.06845 | 2025-06-28 04:27:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d501d587-ab46-3bcf-95cc-a3c9e01fe331 | -6.90634 | -43.97222 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b59ca3b0-63b6-3b97-aa7d-4fcbd707b8b0 | -5.43705 | -46.5641 | 2025-06-28 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e7125dc-666f-3c57-95ef-83f17d237523 | -9.29858 | -48.54547 | 2025-06-28 04:27:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b1ebcd5-460d-35e9-bd5b-01bc5a547d1f | -4.51437 | -42.07692 | 2025-06-28 04:27:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38dec16c-9f42-3bc4-81b7-fb59f630f677 | -9.16186 | -49.66316 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a245dc28-7cc8-3d5e-8ee3-c0b1ed55b5c6 | -6.90164 | -43.97951 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7f7bb2cc-e536-3a53-b43b-50d4fa5a83cc | -4.37209 | -48.06621 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b72e2ee-ae29-3d2e-bf9f-5082b45e32c6 | -6.55038 | -54.98142 | 2025-06-28 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 791e968d-98a1-337a-ac88-1bf35f35dc93 | -6.91506 | -43.98554 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96b2247f-662e-3395-a6bb-5b0c7d70a031 | -8.03976 | -47.64417 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edb887ed-e88c-3039-b156-dfd897233e75 | -7.86136 | -44.44602 | 2025-06-28 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 410a35bd-1a7e-3037-a727-f07bd50a4461 | -4.034 | -47.32589 | 2025-06-28 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 38f7cac5-fc21-3194-b11a-4a2c471edb9e | -7.2234 | -43.08271 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| d55523f8-ca1c-3b2d-a258-5d8e170c73cb | -6.90395 | -43.98785 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6cdcd6cb-f8a2-3887-a2f3-326d22f7440b | -8.56146 | -51.57813 | 2025-06-28 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b83d5e5-1cb1-3d54-8869-93a0c7377370 | -3.31402 | -48.71601 | 2025-06-28 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8eea659b-9e38-347e-9000-74ba435540e6 | -8.84377 | -49.85432 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b314730-6e08-3ace-826d-3001f8d3d69f | -9.11414 | -49.49096 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dbaf3b65-c290-30ca-a5b9-f6c88ac54b25 | -8.10353 | -47.13846 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b3305b4-6e8f-3517-ab70-a087962f857e | -6.94456 | -42.8816 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 248b4976-535d-358e-a912-dbd7938dd8b9 | -4.54786 | -48.02412 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c510a762-8eac-3aec-9f5f-57590f3e4954 | -9.11514 | -49.48756 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 95ea24bf-ddb1-34da-8f12-0224f71e06a3 | -9.7417 | -48.33647 | 2025-06-28 04:27:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c698bb9-72cb-3c80-8ea4-ce4c43d827de | -6.91155 | -43.98501 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa29e2c7-4362-3361-bdbd-9158cb1fc00e | -9.82798 | -48.38091 | 2025-06-28 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1975239-b4d7-3b41-acae-88dad02f2a15 | -4.545 | -48.01978 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 8a745608-5e2d-353b-b244-ec24c773bfc1 | -7.21303 | -43.0767 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ee3bf760-ddce-39e4-a493-4945c87a5cd1 | -6.89634 | -43.99071 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e59d2fd1-bfa3-3e02-9216-d9f0aabd7da8 | -8.04702 | -47.6417 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06fccf2f-70a3-3117-b967-5809e57bc5db | -7.10589 | -52.58807 | 2025-06-28 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76370a13-819a-3513-afc3-acd1f444bd2d | -9.73773 | -48.33959 | 2025-06-28 04:27:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60a63959-1d98-3a09-82df-0aa029c75401 | -6.90574 | -43.97613 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01d7d304-0c7f-3b7c-90a1-204387ad8c80 | -9.11964 | -49.47969 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfe54e2e-3f9e-3d38-ab6f-c7261aedfe15 | -7.1776 | -43.72926 | 2025-06-28 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f28374f9-bc9f-3c7c-bf2b-439b625e9dcd | -8.86581 | -50.1684 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 519fcc61-c23d-3c28-a393-1f298af62f71 | -9.37257 | -47.6298 | 2025-06-28 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7adf43f1-759e-39e2-8d21-bd5f62fd667f | -6.71465 | -44.40083 | 2025-06-28 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4bbd5c8-a2c9-3a35-91f7-e0180cdf08d7 | -9.86979 | -48.45065 | 2025-06-28 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51103e01-5ee7-3e61-9670-01b68f6e6cf7 | -8.79987 | -44.99445 | 2025-06-28 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e991d09-5a73-3099-ad09-2e956df6f8cc | -5.45549 | -43.07626 | 2025-06-28 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2660bcd6-16f9-304b-8a01-a5dab64d37a7 | -5.46331 | -43.07331 | 2025-06-28 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09a68fe9-6535-30a7-a473-fc7baa654e1d | -5.77507 | -42.27817 | 2025-06-28 04:27:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 00607df6-a89f-3c5d-afb3-9d566ee7a737 | -7.54885 | -45.82455 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c123d962-f10d-3dea-81d6-9390a80dba2d | -8.56631 | -51.57372 | 2025-06-28 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 304e0feb-5b84-3c71-8331-2725c31aa3f4 | -9.47551 | -47.31912 | 2025-06-28 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07c4f000-1974-30fe-9bab-b09ece23a1c9 | -5.45844 | -43.08097 | 2025-06-28 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82b74999-0096-39f4-9c9a-74a65e6619d9 | -9.11643 | -49.47964 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 85792a6f-1b5f-31b6-95e7-aca60e6af5c8 | -8.31263 | -46.31079 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c28e3136-3b14-3533-b5dd-e105dd93d5e3 | -9.69305 | -48.33216 | 2025-06-28 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 386cf732-1b59-399c-8944-4df048eb5e39 | -5.61734 | -44.01073 | 2025-06-28 04:27:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0a7139b-65a0-3eb7-8b60-b82e48c7d57c | -7.20936 | -43.07615 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 5ce771e5-f1f7-349d-a4c7-626d09591ec3 | -6.45094 | -44.57351 | 2025-06-28 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09f83d3d-feef-3585-8429-4e0c4aeb9371 | -9.37526 | -47.88092 | 2025-06-28 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 433de070-74a7-3ed7-bfa8-437a0b30e5e3 | -4.30449 | -47.46889 | 2025-06-28 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ea758e3-e8ba-3ff2-956c-829808440278 | -9.43472 | -47.95986 | 2025-06-28 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 360adab0-6c28-3d74-b262-1c19f28f1f53 | -6.2316 | -44.52552 | 2025-06-28 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3710e97-a9ca-3bfe-ab77-3341b59d4d38 | -9.11707 | -49.47568 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 95a23bf0-8a50-398b-88bd-836c755c444d | -9.1145 | -49.4915 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9ba67cba-58a9-3973-8865-bf311cb393ae | -7.18265 | -43.43025 | 2025-06-28 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c65935d2-83c4-3494-b868-26acd24fa3e5 | -6.90044 | -43.98733 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 752f2783-ed7b-3f2e-8737-fa4a53102cd8 | -4.18631 | -48.14031 | 2025-06-28 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa63633c-ea4d-34dd-8c4e-51336344a944 | -7.55164 | -45.82861 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66e4b44e-f2ed-31e0-a6b6-26d49192f1cc | -10.27587 | -44.64231 | 2025-06-28 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e814dd4-d423-3c4d-ad95-81f2f0e390b7 | -12.10958 | -54.57988 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfee62de-e917-3afc-9606-9af209076cfd | -11.27531 | -52.75378 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 016f4c2b-86e9-37e5-8a07-2b49956bbef0 | -11.66965 | -46.72544 | 2025-06-28 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70faa0bb-e861-3bc3-b1f1-0f2ef3086546 | -11.84105 | -43.79974 | 2025-06-28 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 93916445-3a69-31ee-9265-062b2e36fa6a | -10.28994 | -57.00256 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd5f739b-0cc8-30ae-8424-e144d7a8b560 | -10.52745 | -53.62531 | 2025-06-28 04:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bbcd044-2487-3417-ac2f-1ae11569aa4d | -10.83373 | -53.75243 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 721dd763-7ae7-360b-b1ef-039c46d1622f | -12.257 | -46.77008 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 95aaac9d-0822-3c54-8a80-8c890a42dd2c | -10.03469 | -54.32692 | 2025-06-28 04:29:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65932cdd-9922-351b-954e-1775d0bc37ee | -10.0415 | -59.36035 | 2025-06-28 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7b47d94-9e73-3ee1-9a28-b14bc8fd904b | -10.8345 | -53.74812 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49a35fed-49a8-3760-899a-8bad3cca41d9 | -13.94254 | -54.48837 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 554bca84-75b9-3708-bfe3-45e4eecee1ce | -11.04817 | -55.07023 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 593e5660-c744-3bf4-b00b-16830771d985 | -11.0463 | -55.08057 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7001d67-346a-32f3-90e6-fdb41c8ea346 | -15.55236 | -42.65662 | 2025-06-28 04:29:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1df9cc75-4ad8-397a-bcc4-d43e0659bb6d | -11.05296 | -55.07121 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 923f7481-678d-3425-a074-2c0444cc3ee7 | -11.05411 | -55.38202 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6ba2a3c9-c43d-32b0-9181-ee3ce731cb63 | -11.04537 | -55.37453 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| de1ef5bc-d6bd-3340-8c61-6483a7251e3a | -11.32555 | -48.67686 | 2025-06-28 04:29:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cb3ea61-2059-3f9a-aa35-f0a968fca51e | -11.60401 | -55.54679 | 2025-06-28 04:29:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f4d8939-2c53-31dc-9a93-197a80450938 | -10.83087 | -53.74294 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22cc6c17-8ea9-3c4a-bb10-7922ea6b9812 | -10.80552 | -55.86884 | 2025-06-28 04:29:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a6a4174-f9d7-341e-a3ba-b95652dae721 | -10.30024 | -57.12919 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9bdff92-040c-367d-b565-16f9fdb6cf8a | -11.83869 | -43.79788 | 2025-06-28 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f7eb292-8176-3cd8-8edc-5ce6254faed9 | -10.03516 | -59.36068 | 2025-06-28 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f270fa7-b5ec-3332-8ead-0fdca6a90c51 | -12.10731 | -54.66487 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README17.md)
