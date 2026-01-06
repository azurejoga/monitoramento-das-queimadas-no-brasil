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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4173b2ad-caec-3b6b-8cc7-844ce1dcdeac | -2.90807 | -46.73668 | 2026-01-06 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc054e3c-b731-3f42-8b38-b6f5536750c5 | -2.27936 | -53.7903 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 691e1e6e-9fa1-3adc-96c0-0a1b91f4c2c6 | -2.88928 | -50.22831 | 2026-01-06 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a675ef7-7d59-3e23-a494-1f4cdc20027c | -4.14674 | -43.65079 | 2026-01-06 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71060e13-212a-3d51-861d-3787d00bc6ce | -2.48074 | -46.30231 | 2026-01-06 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcd89f37-fadd-3de5-a12e-c043198a014b | -2.64465 | -45.64966 | 2026-01-06 04:29:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 120fa585-c6b2-3f5d-936e-0cdd6f169de0 | -2.53285 | -47.83199 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab2fa019-92bc-387c-9646-69b22e2f8c97 | -1.3657 | -49.41926 | 2026-01-06 04:29:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3ee0af0-5bbf-3c7f-a348-fb686be29019 | -2.73526 | -47.62258 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50132f67-c25a-3cb5-a28e-2f372de825a7 | -2.84455 | -48.65036 | 2026-01-06 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afa834be-f88e-3479-9375-08c5893635b7 | -2.52588 | -47.83086 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61c9d8af-4657-3e5d-ba1f-4870bcbe7847 | -2.16172 | -47.89449 | 2026-01-06 04:29:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad3c8617-59f5-3a14-81e3-ce0549914375 | -2.45031 | -47.78456 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd601bb6-2e12-33a1-a54a-e0dfd568a029 | -3.87317 | -42.51321 | 2026-01-06 04:29:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eb89e80f-48ce-3860-8524-c775db229e82 | -2.5224 | -47.83031 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ad0388b-ed13-332b-ac4c-1067f060a49a | -2.09841 | -53.51799 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf52b9d1-ba53-3d10-b6e8-1167b93a1d22 | -4.07382 | -42.88058 | 2026-01-06 04:29:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93d069fe-de3f-39ed-8b59-6f98e943259e | -4.14964 | -43.65516 | 2026-01-06 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 965d7d8e-3075-3f9c-a16a-2b2d56c19305 | -2.35567 | -47.67597 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4fa87e7-bf78-35c9-98a8-53430f9c58ec | -2.71901 | -49.15818 | 2026-01-06 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 487787e2-c6d9-3850-ac76-af317678b47f | -2.33963 | -47.86542 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 297c2631-bef9-3ae4-a59f-b67a1a77eb7c | -2.93404 | -48.23109 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 531b9422-4baf-3daf-8674-b8c2b1802a64 | -4.07616 | -42.88935 | 2026-01-06 04:29:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3fce02f-60c5-3990-bbc2-bc76f7253240 | -2.8625 | -48.69983 | 2026-01-06 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13767336-b571-3202-9550-996f37f6fe1f | -2.7153 | -49.1576 | 2026-01-06 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d2330c5-756d-3a5f-a1cd-4b3770f8f734 | -3.70335 | -43.43691 | 2026-01-06 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d600a346-a8f4-3a88-a907-546075e7ba1d | -2.28031 | -53.78442 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68121a74-b5ba-37b6-8e68-b1bf7cdc8f94 | -2.08165 | -47.87785 | 2026-01-06 04:29:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3374edf4-bd5d-37f0-8ed5-95abf60a02ad | -3.26081 | -42.5475 | 2026-01-06 04:29:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 28e663b3-ec6f-39bf-865f-3faf1be2ea65 | -2.53695 | -47.82874 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 152a50bd-6899-362a-9665-478fb97f3d74 | -2.5306 | -47.82376 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 857146e3-51d7-34f6-b486-579a959547ac | -2.85356 | -45.25136 | 2026-01-06 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 758b7920-e9f5-3242-a541-6b29f2ba3314 | -3.7926 | -45.07024 | 2026-01-06 04:29:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6c5552b-9bc8-37b7-866e-8c4636b39459 | -2.3667 | -47.67382 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a895f069-25ff-30fc-94d0-70b9762129d7 | -2.85689 | -45.25188 | 2026-01-06 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8379951b-31e2-38de-962f-dc8bcf93ba80 | -2.27524 | -53.78362 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1b60ba5-90cb-33bd-ae41-8476cfc13f3d | -1.81662 | -54.16584 | 2026-01-06 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 35155303-4c76-36c4-926a-e744f8e495dd | -2.52937 | -47.83142 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fe18e61-fb4a-3628-903a-f1faa8350530 | -1.59823 | -53.99182 | 2026-01-06 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6de1e03-5978-3685-b2a9-ae6addbfebcd | -2.98398 | -48.59564 | 2026-01-06 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de4b4ce7-8477-3a46-9af0-f299cd6ff1a4 | -2.09934 | -53.51226 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 768ee1fc-906a-3b08-bd05-0914114a76e8 | -3.48289 | -47.68422 | 2026-01-06 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e2f9a3f-3f36-37d2-b1b9-ac39537b321f | -2.84388 | -48.65447 | 2026-01-06 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fe0ea3e-b1a1-3c86-b29d-fba060416c69 | -2.7588 | -47.79584 | 2026-01-06 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72ca35b9-21e5-3e31-997d-fca55e6cf152 | -3.56366 | -47.17628 | 2026-01-06 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ceae28e-b704-339d-9156-dd20817c4702 | -1.14098 | -48.10298 | 2026-01-06 04:29:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a93622f3-75b2-3235-ac7a-23f9ade568dc | -4.06642 | -42.53918 | 2026-01-06 04:29:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 181045a6-479d-3d6d-a178-c2aef110f05e | -2.27476 | -53.78659 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e63d936-fb65-3801-9dd3-39dd14ff1fab | -2.27428 | -53.78957 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 776b5f9a-f725-37d5-85db-38a9d512de0a | -1.59873 | -53.98869 | 2026-01-06 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f87f77c-1d1b-39d3-aa42-3fc340b64bfb | -2.44779 | -53.81841 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ccd25dba-72d0-30e6-bbd3-81d7c42ecc30 | -1.35877 | -49.41334 | 2026-01-06 04:29:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b40b75ac-e649-35ff-a760-52b082447840 | -4.14581 | -43.64748 | 2026-01-06 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68e95e3a-5c7a-38b0-8e57-84efa6b61a78 | -3.12227 | -39.76019 | 2026-01-06 04:29:00 | NPP-375D | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| caf097ab-a983-344c-b3d1-06657190ad29 | -2.66921 | -49.85242 | 2026-01-06 04:29:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bc92435-ec7f-3e72-bcbb-1e8317d7a955 | -2.64797 | -45.65018 | 2026-01-06 04:29:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c032b37e-618f-3a0b-8bc9-9c9e664b26d8 | -4.15022 | -43.65132 | 2026-01-06 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 47547f99-d97f-3337-bc18-48d9627de81b | -2.25343 | -48.17674 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f647a6f-391c-358d-ab3f-10a4b36b396a | -2.88563 | -45.22092 | 2026-01-06 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b87131b7-b5ae-37fb-a408-aee14e50dc52 | -2.16049 | -47.90225 | 2026-01-06 04:29:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0650cf2a-9e01-30ce-a4f0-a02f6cf73b38 | -3.4823 | -47.68794 | 2026-01-06 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 244f33e5-5b62-3fbc-be36-137a05c0cb8e | -1.36186 | -49.41865 | 2026-01-06 04:29:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a66c924-67c4-3a69-910d-7cabb741272f | -2.36201 | -47.68087 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c12900d1-2f70-3898-a643-86600803b96c | -4.14733 | -43.64695 | 2026-01-06 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d60a7582-4f49-3430-a3d8-c143f8f8abb6 | -2.9276 | -48.22604 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7473dedd-7f1f-360a-b4c5-051b4ee0e496 | -1.71695 | -45.24947 | 2026-01-06 04:29:00 | NPP-375D | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e387fd98-114a-31b5-9a72-498f6c50e492 | -2.52363 | -47.82265 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e0b93785-0c6e-3fb5-a021-0b6ad92a8eec | -2.67308 | -49.85304 | 2026-01-06 04:29:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7598fa58-8c8d-3865-8e32-2dda3def1f2e | -1.04139 | -47.22881 | 2026-01-06 04:29:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f912d906-570d-33f1-a31c-1d3505abcf39 | -0.43626 | -48.59189 | 2026-01-06 04:29:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76bbbe5c-a708-3300-a3a6-7e694d5b2be0 | -2.98529 | -48.58747 | 2026-01-06 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f676d9e-6ef9-3c83-b776-9ade84540a6e | -2.92824 | -48.22211 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14b3df90-d5a9-3d07-9051-80a56d9cd30b | -3.77485 | -45.41349 | 2026-01-06 04:29:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30c625ce-6139-3f89-a60d-3a9449a447bd | -3.03437 | -46.92751 | 2026-01-06 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e7cfd57-f25b-3050-b63e-d111123549e8 | -2.09435 | -53.51145 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1983d9e8-8eaa-34da-a526-c1282ced0e85 | -1.48052 | -46.1382 | 2026-01-06 04:29:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93125317-c0ec-3e33-a4fc-21cf3caf82d1 | -2.34312 | -47.86599 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96b09707-ba34-3a38-9689-c31da1fb0aac | -2.73406 | -47.6301 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adf3b6fd-e862-380c-97f5-02993b18d532 | -1.78242 | -45.26333 | 2026-01-06 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2051b14-94bf-3654-bee4-8153b6cf369f | -3.56424 | -47.17269 | 2026-01-06 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c3a2f47-57da-32d9-97f1-b3579c9a267a | -1.14455 | -48.10355 | 2026-01-06 04:29:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 48f709f7-2954-30d6-a21a-f11a6d32cf8a | -3.25782 | -42.54276 | 2026-01-06 04:29:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85b96021-2861-3dd2-824a-3e0ac438aa8d | -2.98464 | -48.59155 | 2026-01-06 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6feae14-dfa7-30f8-914f-daa913c34e75 | -2.4473 | -53.8214 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3615fd5d-76c5-380c-acdb-4662fcae5f70 | -4.06709 | -42.53492 | 2026-01-06 04:29:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 91acd762-62ee-31e2-9f52-c01428aaa06c | -1.65669 | -52.05245 | 2026-01-06 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a84c25d-6efc-370f-9d70-639f5f7b56e3 | -2.9849 | -49.52463 | 2026-01-06 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c631f34c-be0f-3057-a426-38379e81ef50 | -4.14521 | -43.65131 | 2026-01-06 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ea91fc9-3d6e-381f-af89-772f15e28d20 | -2.88231 | -45.22041 | 2026-01-06 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbb72b70-c9ab-3a47-90fb-4e9eedf155d4 | -4.07679 | -42.88524 | 2026-01-06 04:29:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 297be764-1e1d-35a2-9512-bb3a57eca978 | -2.07806 | -46.9219 | 2026-01-06 04:29:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ff94136-81d1-39ae-ad60-43ea0ee058b6 | -2.25407 | -48.17279 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d39b494b-0cd9-3d7f-9525-906df77832b0 | -1.59785 | -53.35917 | 2026-01-06 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21e69795-eedd-31ed-885b-8acb9bdea357 | -2.88791 | -50.23012 | 2026-01-06 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b30f324-73f3-388e-8552-f85b93d9fd05 | -2.78368 | -45.43513 | 2026-01-06 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8efc7998-47d4-38be-b259-66be5159a16a | -1.48952 | -45.9611 | 2026-01-06 04:29:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 947b919e-8466-3c1b-8b14-dc2be775d0e0 | -1.3048 | -53.91868 | 2026-01-06 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ec7a13e-223c-316c-b1d6-27616865f8b9 | -3.69986 | -43.43637 | 2026-01-06 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 5752a48b-fdae-3155-9f77-886c45e4aeb1 | -2.53409 | -47.82433 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df2bc485-e73f-39b5-9b79-0492631153e4 | -3.39289 | -44.10524 | 2026-01-06 04:29:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README8.md)
