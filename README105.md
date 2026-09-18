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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e27a76c3-a96f-3a8b-9cd8-78c509afad91 | -12.0267 | -50.0231 | 2026-09-18 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 7a44ffab-a4a9-3c70-9d0d-487a80f3c7f1 | -8.6817 | -45.4359 | 2026-09-18 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| b5ca6257-fbbe-3f7d-89d6-5155a3264d00 | -12.3954 | -48.4727 | 2026-09-18 15:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9d9b3dea-ae64-36fd-b2cf-8c23ae7cd5b9 | -0.803 | -48.6611 | 2026-09-18 15:00:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 0e7f97cb-681e-3f49-a334-249ba6fe8e84 | -9.9509 | -46.6026 | 2026-09-18 15:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| aa5729a2-bfc6-3b0b-810b-3a87244ed28f | -10.6944 | -50.26 | 2026-09-18 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| bbf4e644-47b5-3c0f-8099-e7a898d3f0de | -9.5695 | -45.4729 | 2026-09-18 15:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 183.2 |
| c46b77f0-5f04-38e7-8450-c7a4ec219410 | -7.8598 | -44.8595 | 2026-09-18 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2251b6b7-fd9e-32d5-9b6c-b25cf86dfa04 | -11.2979 | -43.3614 | 2026-09-18 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 204.2 |
| aa06b9c6-6672-3a7c-b259-ccf13a77c4b9 | -10.6376 | -50.266 | 2026-09-18 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 7fb8cdf8-4ffe-3630-8633-85db0ecbdf14 | -10.8186 | -50.8648 | 2026-09-18 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 60a95bcf-edb6-3638-9850-27d4a942c6bd | -12.0902 | -50.8521 | 2026-09-18 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 370bb0c4-26b6-3080-b7c2-6d375d3f60b9 | -11.3442 | -43.9906 | 2026-09-18 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 243.7 |
| bb2107f2-1124-3afc-9dcf-6dc5cb3dfd21 | -15.6557 | -52.7366 | 2026-09-18 15:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c6fc0d64-68d3-3009-842d-ac44b431d00a | -10.6522 | -50.5845 | 2026-09-18 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 678b6c6f-0d4e-3750-8fed-a7518c68c2d2 | -10.6187 | -50.268 | 2026-09-18 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 367f2c53-56ae-337d-9a4b-f14e8199c7f3 | -12.998 | -46.9381 | 2026-09-18 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ead9a610-679f-3838-afa0-1d3e274c12e2 | -14.1737 | -45.1641 | 2026-09-18 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 241.9 |
| 171bc31d-6ccf-3414-85a2-553eafce2034 | -10.7276 | -50.5979 | 2026-09-18 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 136.7 |
| e6058607-eac1-3cb3-88bb-f242e3c5b6b2 | -11.2975 | -43.3851 | 2026-09-18 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.4 |
| aeadf069-55c5-3c05-baee-ca0b5a8bd2c5 | -11.0617 | -49.7261 | 2026-09-18 15:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| efd00aa7-ec7a-3874-a018-b7a7bf1c0615 | -15.6752 | -52.7339 | 2026-09-18 15:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| cd79dda7-3f56-3fdf-bcb0-25ad07fd2f63 | -8.3769 | -47.236 | 2026-09-18 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| b1fb5fe6-d84a-332a-a8cd-b1cfe56fa55c | -6.0168 | -52.182 | 2026-09-18 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a9e0c998-549f-3bc1-bdde-3af59104b640 | -2.4999 | -49.3992 | 2026-09-18 15:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 7000ca7b-b8ab-3b4d-80d7-1466230419cf | -9.5502 | -45.498 | 2026-09-18 15:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 31a4083e-c413-3bd2-bc8d-ca14d4d17f8f | -10.3704 | -50.4644 | 2026-09-18 15:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 10bf08bc-355e-34a0-9f04-b08bbefca651 | 0.1747 | -51.4805 | 2026-09-18 15:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 570d5de2-0aed-3e4b-89a7-f3710f198a0f | -10.6187 | -50.268 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 42ce273a-f952-37e7-86c0-81664bdf53c8 | -0.5442 | -49.1324 | 2026-09-18 15:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| e5db5cd8-5929-32ca-9ae4-aebe15199c11 | -9.9509 | -46.6026 | 2026-09-18 15:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| c17b12e8-e578-3c51-8b3f-1ec4423f2491 | -10.6723 | -50.4972 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 5a7ba9d8-c66d-3d42-8f5e-baa4f469bcb2 | -12.0238 | -51.4763 | 2026-09-18 15:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 6f9f916c-f556-373a-ad1f-5baa44defb3f | -11.875 | -47.5902 | 2026-09-18 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ff003c22-23ef-3b5a-94ab-8eefb169774a | -2.9395 | -50.3994 | 2026-09-18 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f1e61680-00cc-308d-af4c-2e3e7855d45e | -10.3307 | -45.3112 | 2026-09-18 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 886e3239-a818-3b0f-83ef-8de1157e5d13 | -10.676 | -50.2192 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| a8ef2f04-b1d4-308e-aafa-374c1bff9813 | -15.5923 | -56.5559 | 2026-09-18 15:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 2877656b-bb6e-3087-b782-1d77ee69867f | -14.1542 | -45.1675 | 2026-09-18 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 231.9 |
| 74bda575-0956-37e0-acb0-66747db673bb | -11.3437 | -44.0141 | 2026-09-18 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| fcaceb59-f09c-3f3a-81cf-9413f56dd310 | -0.6185 | -48.5982 | 2026-09-18 15:10:00 | GOES-19 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2bad72eb-d0bc-397a-9e33-7d3a08c4713e | -12.1448 | -44.243 | 2026-09-18 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 34f801fd-4077-3878-9ff7-d672fa92bb02 | -10.7733 | -46.1869 | 2026-09-18 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 7299b3e4-53a6-3f09-b535-48a3c9b7cdb1 | -12.5688 | -50.7308 | 2026-09-18 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 28b7dc25-db9f-304e-b2e9-06477ca3ff6d | -7.0352 | -44.6396 | 2026-09-18 15:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a9498f67-c681-3169-870f-961428dc4f7f | -3.7516 | -54.6494 | 2026-09-18 15:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 20322564-9a42-3e29-b15e-e8663c43480e | -0.803 | -48.6611 | 2026-09-18 15:10:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| a418b4a2-b50b-370f-9ca2-ba9249e73022 | -12.3954 | -48.4727 | 2026-09-18 15:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| abc55dc5-783f-3033-b0f8-cb314b96f9eb | -10.6189 | -50.2466 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 4ab0ed2e-4d72-37e1-a78b-2bbb4e94c63f | -2.4815 | -49.3996 | 2026-09-18 15:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 78893ed7-32fa-305a-8921-41f07a6034f6 | -9.6816 | -48.3139 | 2026-09-18 15:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 2cb40a49-b21c-3ff8-ad21-752ac3ddf218 | -11.4541 | -51.4754 | 2026-09-18 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 3a5771bb-969e-3b76-841a-d1e9c0313c20 | -9.5698 | -45.4501 | 2026-09-18 15:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| cae50ed3-87a5-31cd-bc25-54d517e0f069 | -12.998 | -46.9381 | 2026-09-18 15:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 361926bd-9aa9-3c1d-8a06-73fc7764d07f | -11.2975 | -43.3851 | 2026-09-18 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 233.3 |
| a7f690d8-a673-34bb-899a-5f09efdeb408 | -1.6042 | -54.415 | 2026-09-18 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f7819243-8c15-3d07-9c58-3b564eb00155 | -15.6752 | -52.7339 | 2026-09-18 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 154.5 |
| d361f996-80a8-3c80-ae12-24f1c23def33 | -11.3621 | -44.0582 | 2026-09-18 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 914f5685-4dbc-34fd-a59d-44952a20d403 | -14.931 | -49.9322 | 2026-09-18 15:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 42.7 |
| b26c1d63-f4cc-3ede-af6e-a358ee0cd84b | -11.3809 | -44.0788 | 2026-09-18 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| ec6442e1-84cf-383d-8418-3d6ed37e8475 | -9.5695 | -45.4729 | 2026-09-18 15:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| bfbb8fbf-0be4-38e4-a04e-83acfc51b7f3 | -2.4999 | -49.4204 | 2026-09-18 15:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 77140357-12bc-3756-8762-0e3e8987d992 | -11.2979 | -43.3614 | 2026-09-18 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 88bcf4ad-4a78-39bd-817c-4e76051cb539 | -11.3442 | -43.9906 | 2026-09-18 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 8ed791b4-611f-39a4-97a0-abfdfc95eadd | -7.8601 | -44.8366 | 2026-09-18 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 110c56e3-f8df-3d3f-a3ef-53721281b26a | -14.8026 | -48.5622 | 2026-09-18 15:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b0cb500b-6d9d-34f9-9fa9-32fee9932fc6 | -10.6758 | -50.2406 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| c107fa70-e588-3aaf-902e-0eceda8fed84 | -9.5505 | -45.4752 | 2026-09-18 15:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 9cd2a1f1-c38d-39df-bebc-c1b72bdfaa7f | -14.1547 | -45.1442 | 2026-09-18 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 2712dd31-6f4e-3d3d-a453-df23aa3efe42 | -9.3251 | -48.1758 | 2026-09-18 15:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 12b8646c-da6a-3ab3-975d-96d2d2337dbd | -10.5838 | -48.696 | 2026-09-18 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| dee5b571-c53f-391f-9d8b-c66379be6845 | -5.8965 | -53.5178 | 2026-09-18 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4f8b86db-6da7-3379-b280-a2fc707d6eb2 | -14.9509 | -49.9073 | 2026-09-18 15:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 4ff45b09-54d1-37fb-884c-59e7896d7525 | -11.8115 | -46.8158 | 2026-09-18 15:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 187.7 |
| e4a9c895-8384-30cb-a036-c8b5b8eccc05 | -10.7923 | -46.1845 | 2026-09-18 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 10d842a3-3cf5-310a-81bf-7a571e85cb3c | -12.0086 | -49.9606 | 2026-09-18 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 289.9 |
| 9ca7fe5a-2200-3eb3-8505-16c39d788667 | -9.9136 | -46.5621 | 2026-09-18 15:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| d612a9c5-7667-3c3e-8515-88ca3425b2bd | -8.6377 | -44.4798 | 2026-09-18 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 87c6d8c3-2b1a-3299-97cd-f9c00a0ff706 | -10.6729 | -50.4545 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 6718bdfe-a71a-317b-a871-1cd2f06e61ad | -9.7497 | -46.1089 | 2026-09-18 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 08cde32f-a96c-37c8-a10f-3c7c45cc2b36 | -14.1737 | -45.1641 | 2026-09-18 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 65076961-619c-3990-8414-4cbd132dac20 | -9.5692 | -45.4957 | 2026-09-18 15:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 1e8418c4-6cf8-30b6-ae22-ca5e71cb5b47 | -12.0241 | -51.4551 | 2026-09-18 15:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 3b3f5bd0-0947-3705-a1da-acd7d76c91c0 | -10.7276 | -50.5979 | 2026-09-18 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| bdc73cdc-02e0-306a-bc02-3b5c95ef440c | -9.2417 | -45.9185 | 2026-09-18 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| eeb5bf16-76fe-31bd-a0fa-0285d3f42046 | -12.0464 | -49.9776 | 2026-09-18 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 5bb971bf-4435-3f4c-b1a4-a6f2be13676b | -10.6525 | -50.5631 | 2026-09-18 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 4b4d8306-4836-3f25-97c6-9820a1b36e54 | -2.8101 | -50.4658 | 2026-09-18 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| cff3e99a-7965-34f3-83bc-1d66f2eb39eb | -11.064 | -48.2898 | 2026-09-18 15:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| a45af026-dc00-3624-a3e0-250dd755092a | -12.5879 | -50.7285 | 2026-09-18 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 7a143c60-43dd-358b-bb3d-c9530b7c8a79 | -10.3769 | -49.9723 | 2026-09-18 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 6be16045-94f5-31ce-917b-11ec8d160342 | -10.6944 | -50.26 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 4d93e572-a5b7-308b-a4ad-e74c7d06397a | -11.9898 | -49.9413 | 2026-09-18 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1092eb47-eec7-3334-84f0-6c8324fdefca | -9.6016 | -45.8777 | 2026-09-18 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 34f82550-4c52-3104-81b0-a54328b3e214 | -10.6533 | -50.4991 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| a948ffaa-448e-3ded-873d-695bbf1329fb | 2.2187 | -50.8769 | 2026-09-18 15:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e52c7e87-1936-3ce9-9c0c-eee43d1bd36a | -12.4933 | -50.6758 | 2026-09-18 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 113bb62d-2065-3000-bd34-0a2b544f76ad | -14.1742 | -45.1407 | 2026-09-18 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 94bffdba-fb5a-3d13-bf90-7e53fdf3be25 | -12.0902 | -50.8521 | 2026-09-18 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 143.4 |
| b3e9e160-7167-3677-a831-848d73a0ad43 | -10.6536 | -50.4778 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 170.4 |


[Clique aqui para ver as próximas entradas](README106.md)
