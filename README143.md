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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eae78372-f816-362b-b8d1-b3641b2834f3 | -13.18415 | -47.997 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b7e29cd-5c78-3036-9532-55437e8ecba4 | -13.18357 | -51.17497 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f5094f6-65e2-3f61-91f1-ddbdb0caf581 | -13.15686 | -51.67936 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bf30518-e7c2-39fd-b125-6a83894f7690 | -13.15629 | -51.68296 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9d050d7-4762-37cc-8db6-6c0943a7ce96 | -13.1541 | -51.67521 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6e9569c-2993-3699-8adc-d5b5e78c6768 | -13.15352 | -51.6788 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4212ea1-47d8-33c7-adea-c75270a70c6d | -13.15133 | -51.67106 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec7bd075-dc9d-306f-9b99-e128a41ef50a | -13.15075 | -51.67465 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e6d7666-6b43-379f-b21e-14b2d847104c | -13.14799 | -51.67049 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c537f714-8abf-32c7-9e15-49e650a0e4fa | -13.13865 | -51.64319 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e335b60b-743f-36ec-a31c-b41b97de371b | -13.12907 | -51.65998 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f63995c7-7459-34b4-8465-cb64f6ab63a1 | -13.11522 | -47.16487 | 2024-10-09 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a319dcdf-eaa2-3c01-9b1f-1b614818bf77 | -13.00305 | -53.66131 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ff920c4-cd58-3161-955e-6b050e8695b0 | -13.00053 | -53.66225 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ff36f7f-234b-3e8e-9772-45b60295616c | -12.99948 | -53.66071 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 678bb802-a985-313b-a515-02d50b41e26e | -12.99765 | -53.6575 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ee35ba5-c477-3057-b51c-133eff517ee0 | -12.99696 | -53.66164 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99ff86a2-7dcd-3474-b594-19e634f0d745 | -12.9934 | -53.66101 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2aaebbf-d45e-3103-a957-f4b553448807 | -12.98472 | -62.46941 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f05fe97f-25b2-32b5-8498-d8fa76870e23 | -12.98304 | -62.46811 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa8d21b3-66ca-3a7f-aebf-7c3bd77d2b83 | -12.97762 | -62.47288 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99bd98cd-dc8c-3edd-829c-735b044d8bd4 | -12.37562 | -47.67702 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86ef880b-a3a3-3a88-9ef1-0bd71b6f207a | -12.9759 | -62.47158 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64c15f2c-144c-3f5e-b9dd-5794bda86339 | -12.97441 | -62.45705 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb52b7ab-4704-3589-9911-0990ecc6f9c1 | -12.97343 | -62.46188 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae0c6141-a848-3a4a-aed9-518a89c98ef2 | -12.97178 | -62.46062 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2377191-37ee-3733-8067-efb6fe6720d3 | -12.97148 | -62.47153 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ba3d2a9-8375-31d2-b17a-18e09fd11d06 | -12.96977 | -62.47025 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6a976f99-28ba-335d-9522-dc3eb1b4b8ac | -12.9673 | -62.46052 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c57fee40-7f42-302e-ac86-924e55f2fbaa | -12.96572 | -62.48954 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e310165a-2bcb-34f2-a81c-c23333dfd505 | -12.96565 | -62.45929 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8f5e905-7781-393c-ad39-aa9825c68807 | -12.96241 | -62.48467 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8c36f3d-ab3f-32e7-856f-aade5f7630e5 | -12.96143 | -62.4895 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3245254-535b-3a0d-8623-d10c8b8d50ac | -12.95959 | -62.48819 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa5845bd-2f1d-3343-9f5a-5a34f07e9915 | -12.95529 | -62.48814 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6080eb67-4767-3ae3-8043-1b90c2304684 | -12.9543 | -62.49302 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f67b6e4-5311-39ca-8dff-551e37a816ec | -12.93665 | -62.45379 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 558f8a81-cdee-30c7-b054-2c2e9ecf92e7 | -12.93053 | -62.45242 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6ea830a-7918-3db4-a594-8a245bc56536 | -12.92953 | -62.45726 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06c6e3e2-40e6-3246-a03c-fec766f0ac84 | -12.92341 | -62.45589 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 345a1766-9a77-3197-b881-e396d2d003a0 | -12.92113 | -62.73294 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0153d47-5a94-3bb6-a355-006e085498ad | -12.91837 | -62.73362 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c928b1d-6a5a-335c-8579-5c29a7907b80 | -12.91489 | -62.73159 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25303b64-1b09-3344-94ae-356f86bf4fc9 | -12.91419 | -62.72213 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96d91852-09dc-3754-a90b-79fcf1a3600b | -12.91316 | -62.72719 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a599b4f5-c021-3005-a35a-db58954a1691 | -12.90971 | -62.7252 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 71c1152d-8356-313b-b34f-8aaa80dae467 | -12.90904 | -55.64398 | 2024-10-09 04:40:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dea328cd-85bc-3ab8-8ed9-d8e1689ec7a5 | -12.90795 | -62.72081 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 249b5986-ebe8-3800-a582-ee08825e29b3 | -12.90692 | -62.72586 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b13f1e7-4c65-3bc3-9206-933ae37e7df5 | -12.88491 | -55.44112 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89d6d03a-fa15-3b0b-9c8f-f45539cd6b59 | -12.88398 | -53.47132 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e29161e8-1f1b-3145-b7c2-9db6bb8a2c41 | -12.88331 | -53.47535 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c4c3fa0-3e39-3103-bdd2-02fdef4e1075 | -12.88095 | -62.78898 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff35247d-2d8b-33e9-9a89-965d2a47591b | -12.87978 | -53.47472 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12cc090c-1771-3281-a421-1bd6c266eabd | -12.87886 | -62.79916 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27c551d8-2315-3dc0-9463-384d44e1446e | -12.87782 | -62.80426 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3824429b-3e1d-32b6-b0b5-ba2b4d0a007c | -12.87537 | -54.03283 | 2024-10-09 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d67fcc5-9591-3300-86c2-6528b65510cb | -12.87155 | -62.80291 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 15363e68-3e81-3728-b434-a0cf6665e9ec | -12.8705 | -62.808 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d163ea01-f0da-334b-b8a1-3d4f6ce37e0b | -12.86423 | -62.80661 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 393ef586-15e8-3be6-a996-e070fa434bf7 | -12.86006 | -62.79507 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3211a862-e434-3f97-8c02-12d33e05aa85 | -12.85796 | -62.80527 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ed00cc4-185e-321a-a0bd-15b1260ecd03 | -12.85274 | -62.79879 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94011c66-3477-308a-8dcd-6cca4dd23339 | -12.8475 | -52.82285 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f971d1e4-e90a-31a1-9865-6e6fe3d515d4 | -12.84686 | -52.82668 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61e8978b-54d7-3530-924c-28a9f8974a15 | -12.84435 | -62.80771 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a9817cf-39cf-3045-92d3-2a38851c0727 | -12.84405 | -52.82226 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc9cdea8-247c-3c16-ac7c-c6010e149480 | -12.84341 | -52.82609 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7b71903-6b0c-3ce2-931e-fb448ce07fbe | -12.8415 | -52.83759 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7a0df07-88cb-3e2a-9a38-5d970f917ddf | -12.84124 | -52.81781 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80a3be09-084f-358f-8a18-4440a539b6bb | -12.8406 | -52.82166 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cafbe85-619f-31eb-9381-25ccd795debd | -12.83996 | -52.82549 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b504587-cea8-3602-8780-eda3b0f88b5e | -12.83932 | -52.82933 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4d96023-91c5-3608-af3a-e5f032ec77fe | -12.83869 | -52.83316 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe7cae2d-f143-3ed1-a7c4-ed045e1a4f39 | -12.83807 | -62.80634 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e56a89c-5735-3d29-9460-3280f4fecac5 | -12.83716 | -52.82104 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c935776-b27b-3217-badb-abc5bca8b969 | -12.83652 | -52.82489 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dedc7af-eeaf-3a00-bb9c-9c7cf3a4d086 | -12.83588 | -52.82873 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15ef3356-1df8-3111-9d6e-c7c4f6a72113 | -12.83524 | -52.83257 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 850675e0-5e45-3c01-9a23-604080fab769 | -12.83307 | -52.82428 | 2024-10-09 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b04e55d8-89a3-3ddd-8da1-5b5a3fb54abf | -12.77918 | -48.2109 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 075932ff-f71d-3ddf-9109-6d73121afd0f | -12.77722 | -51.389 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c77c99c6-ed5f-3d57-bfa2-7b738bc6ca39 | -12.77389 | -51.38845 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| abad93ae-950a-3f41-afd3-bd186eeafccc | -12.75997 | -62.26709 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7461231-d9d7-3f53-8e31-3c6184d0fee8 | -12.759 | -62.27183 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d56da5a5-72b0-30b2-9853-81ac53bc667f | -12.75805 | -62.27653 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d4fc5b5-14f0-3072-aa5a-dfdfb1e384c6 | -12.75581 | -62.25629 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22c52cd2-4016-3ebc-8f9e-df33603cc54b | -12.75389 | -62.26576 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0396a837-241c-305b-b22a-606cdc0905b1 | -12.75292 | -62.27048 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9539e4da-6d4d-3235-8490-579a6a9fdc97 | -12.75198 | -62.27514 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| edc17d17-786f-3f63-a5cb-f91e8a170c5f | -12.74877 | -62.2597 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6de4f806-aad3-3e36-b572-02237b83e5b2 | -12.74269 | -62.25835 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c6a696d-2a93-38b1-ba53-a127458f5dee | -12.72933 | -48.42295 | 2024-10-09 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c0e8dfe2-d8d6-3b5c-bf02-46e025314549 | -12.72821 | -51.99448 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aad3abaa-3af9-3ea5-9739-9d77fc52171f | -12.72762 | -51.99813 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dfa8ee5-7ce9-341f-965d-5d445a3de13b | -12.72585 | -48.4224 | 2024-10-09 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41ce14c6-9eca-360f-9eb2-6f2872ecd3fa | -12.72425 | -51.99756 | 2024-10-09 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3150e3b-4475-3540-accd-e9751b05c747 | -12.70429 | -54.11729 | 2024-10-09 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0d79c4b-a296-3b02-b533-177e9b2891fc | -12.69777 | -62.96378 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| abf67799-e4e9-33e5-8617-f1052ae257fd | -12.69699 | -54.11597 | 2024-10-09 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README144.md)
