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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a13b2176-2835-3dcd-9139-8ea21d008f44 | -12.2498 | -50.3835 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 5e415d50-a86a-3ebe-9996-003e92be5385 | -12.7032 | -47.2964 | 2026-09-27 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 6a17b317-9a02-3618-95cc-650f22f22bff | -12.1366 | -50.3112 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| fedf40db-c678-3bc6-b8b7-bac1b89a0150 | -17.0529 | -56.59 | 2026-09-27 13:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 9e60bed9-2b70-3ce6-bb06-eb8f99c5e840 | -8.3589 | -44.1406 | 2026-09-27 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 345.6 |
| c2d14b75-efae-300d-b009-25e96486a7f6 | -12.1178 | -50.292 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 4cedcdd0-0bc5-3e8f-9472-b6aec107b81c | -12.1185 | -50.2489 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ca7d95b2-93a6-35d1-a634-d2a4f8c914d9 | -7.3842 | -42.1039 | 2026-09-27 13:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 138.8 |
| 0cb328bf-6f48-3f66-9f0e-9cb446e189e1 | -12.0806 | -50.232 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 98e0f4b4-7bd7-32a4-9efd-7d76a2d26538 | -12.0178 | -50.6041 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 07c1e202-ffe1-3d35-b7f2-06f13f4fdbf0 | -12.1171 | -50.335 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ece98568-4aa2-3a55-8082-f2a644cdaf21 | -8.3778 | -44.1386 | 2026-09-27 13:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 192.7 |
| b1b2f8c8-7436-3754-a993-e5a43a07742d | -6.8405 | -43.5254 | 2026-09-27 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 5415db75-b12d-34c6-96e4-18a9b0617601 | -11.8014 | -49.8129 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 426ddbb9-3688-31d6-bec0-ebb034cd0e0a | -12.1175 | -50.3135 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| c84c94a1-1d76-3f46-a35e-ec88b6cfe7d5 | -12.1744 | -50.3282 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a1647a78-4143-3b48-b74b-bd5b6a544ebf | -12.2307 | -50.3858 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 3fe966f4-c72d-3403-8598-f5b65049c901 | -8.3586 | -44.1638 | 2026-09-27 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 447.4 |
| dfcb23ae-1f7d-3188-a24a-584ea848bb10 | -7.365 | -42.1298 | 2026-09-27 13:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| c0cabfc6-d82a-3435-8aa6-15c2adb91f4b | -6.8596 | -43.5003 | 2026-09-27 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 254d4d2b-9cbf-3aa0-94ca-19003ddc3ab1 | -7.055 | -42.849 | 2026-09-27 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 159.0 |
| f67b2dbf-00ba-35b3-a127-08ff1093f761 | -11.1183 | -54.0062 | 2026-09-27 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| cf99375c-7ca7-36a1-b831-6af1ffb5a81a | -14.1105 | -46.3293 | 2026-09-27 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| effa0a6a-d7ae-3c57-9c3c-b35c8d303b65 | -12.2311 | -50.3643 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 43370772-7b49-3319-8867-57482bfe3475 | -12.1362 | -50.3328 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e40dc657-a4b5-3ccb-ac1a-771eaf350560 | -12.1188 | -50.2274 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 888665b4-8335-3cff-a4f2-86fde5cdd085 | -11.0233 | -54.0559 | 2026-09-27 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 2d9f84a2-2a9e-3328-b8e3-280f61b4b8b6 | -17.0533 | -56.5693 | 2026-09-27 13:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 8c65b60f-915b-3115-8811-fd446072bf7b | -7.3653 | -42.1058 | 2026-09-27 13:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 295ff6e3-a219-3942-96be-597f7b2bd6f1 | -11.9415 | -50.6131 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f8d19376-ef29-3b72-b952-abd17dafdbaa | -7.2102 | -39.3549 | 2026-09-27 13:30:00 | GOES-19 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 76edd956-7d3b-34a2-8eb5-2d66e2e66bbd | -6.8594 | -43.5237 | 2026-09-27 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| b6759e81-e37f-3c95-a9dc-b0ec232a55e0 | -12.7225 | -47.2937 | 2026-09-27 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8b9e00d2-b6eb-3639-a583-332c544ff13e | -12.6647 | -47.302 | 2026-09-27 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 07a80928-309c-3e65-9e05-39c35b50c133 | -17.0529 | -56.59 | 2026-09-27 13:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.0 |
| 5c4177b3-4882-3ea2-a34f-107f8d9b781a | -12.0178 | -50.6041 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 8b29afd1-9f12-3e7c-9564-accb2aaf1011 | -7.3842 | -42.1039 | 2026-09-27 13:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 5f7eaa92-a456-3096-bc85-766091567105 | -12.1185 | -50.2489 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 62abac67-e40c-31e7-9c6a-a3ef3bd6048e | -8.2525 | -49.9572 | 2026-09-27 13:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| fcd1da0a-119e-3c8f-93f5-8c38553b013d | -17.0533 | -56.5693 | 2026-09-27 13:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 762dcb42-9a99-344b-93c2-f71672b7b767 | -12.0369 | -50.6019 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| eca92745-c268-37cf-bed0-488b24041ed9 | -11.9415 | -50.6131 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 858fbc89-86f3-30e5-b186-409f6e54b064 | -6.8405 | -43.5254 | 2026-09-27 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 8b6844dd-472e-3e7e-ad14-5dbe77d95478 | -9.9318 | -49.3733 | 2026-09-27 13:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 4f85c99e-9a5c-384f-99d7-f534897294bc | -7.365 | -42.1298 | 2026-09-27 13:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 127.0 |
| dca7b554-94ec-349c-b2ca-cdbd972da05d | -12.8059 | -54.0255 | 2026-09-27 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 87e3978f-a610-30a1-9535-8db0c082a69e | -12.0559 | -50.5996 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 4effe40c-1db0-3505-9f91-2a911bfde6c7 | -11.1714 | -50.0151 | 2026-09-27 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| cff2c05c-8ef5-3346-8f41-f3bfb154b797 | -12.0806 | -50.232 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 10143765-eb69-34bb-ac89-b0201180d7a1 | -6.84 | -43.572 | 2026-09-27 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| c9c63669-9157-312d-9785-b3f945b9dd3b | -12.2699 | -50.3166 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| d16b2339-ab94-37f1-b96f-61360c3006d0 | -6.8596 | -43.5003 | 2026-09-27 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 3383aeba-0d63-3abc-be83-7fab32474986 | -11.1183 | -54.0062 | 2026-09-27 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e915ee53-1091-3748-b8ac-9b2b460aaabb | -12.7225 | -47.2937 | 2026-09-27 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 2a2f5270-b499-380a-8334-2b22822a505c | -9.8427 | -44.937 | 2026-09-27 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 8f340c6c-db94-3c22-bacb-a645a3d4b25b | -7.3653 | -42.1058 | 2026-09-27 13:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 151.0 |
| e28f42fa-c720-3f42-99b4-2c152ab17948 | -11.1524 | -50.0172 | 2026-09-27 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c3596c67-c30d-3413-822c-58b69030c47f | -7.055 | -42.849 | 2026-09-27 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 3fe6b533-91e7-3b17-bb90-01360196c648 | -11.0991 | -54.0285 | 2026-09-27 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 439661b6-69a6-3903-a8e7-912de0b6ac26 | -12.1188 | -50.2274 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3b8057bc-40e2-37b9-8bf6-ae5e09afde0c | -12.0372 | -50.5804 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5f4e40cb-fc05-335d-b8c4-6030b1817a7b | -12.7028 | -47.3189 | 2026-09-27 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| d4c43e61-bb9c-3c09-bd13-81550c5afd5b | -12.7221 | -47.3161 | 2026-09-27 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 2483dacd-b61e-3818-bccb-3d5a5e5f2ecc | -6.8408 | -43.5021 | 2026-09-27 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 212.9 |
| fbdb315f-d34a-3f27-8e67-7a0db10cfc1e | -8.3422 | -45.4487 | 2026-09-27 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b6679f47-8a5b-39c7-9771-4cb79d5bb4e6 | -12.4157 | -44.1529 | 2026-09-27 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 8fdb7f9f-2d52-3252-95cc-eb7b556b3c36 | -11.9845 | -50.2864 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| bf0e91d8-0499-3547-a057-e1815a3fc23a | -12.0997 | -50.2297 | 2026-09-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 71f81f30-d13a-3564-8cf7-a6038c2c2621 | -12.4351 | -44.1497 | 2026-09-27 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 49a52597-aa9f-318b-96df-705f39417666 | -12.6651 | -47.2795 | 2026-09-27 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1150d518-8f18-3408-928e-1ed914257f48 | -11.1183 | -54.0062 | 2026-09-27 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 51ba6b09-4608-3e91-abd9-158d3a930a30 | -12.2884 | -50.3573 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0c5f6990-2d47-36d6-8045-0c3d4b221547 | -12.2502 | -50.362 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c6475b81-a719-32ea-b9bd-57ecbf3bfe5a | -11.0583 | -51.327 | 2026-09-27 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 72bd8627-f3bf-338a-a68f-7897af06463d | -12.2307 | -50.3858 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a181bbcc-14fa-3e88-b953-de6ba853029d | -11.9434 | -50.4844 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 619d619a-b72f-300d-96a2-29b49189f757 | -12.2498 | -50.3835 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5ae92864-4e40-3bda-ac12-521098d518bd | -12.288 | -50.3789 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4fe2bfbc-4fa2-3afd-9897-1f4c91b7fdea | -12.7221 | -47.3161 | 2026-09-27 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 283c4cdc-fdf3-31b7-960a-26bff51839ab | -7.3842 | -42.1039 | 2026-09-27 13:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 61e4f260-dadd-31d4-af91-0f780f872e51 | -17.0529 | -56.59 | 2026-09-27 13:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 597a0392-e90a-3a4d-b7fc-46aaa03eb271 | -7.2102 | -39.3549 | 2026-09-27 13:50:00 | GOES-19 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 9b42ea57-5d28-3643-abdb-282007b65f1d | -12.2311 | -50.3643 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 85451f67-04ce-39db-9dbe-43e093e3bbab | -6.8408 | -43.5021 | 2026-09-27 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 214.4 |
| 3078c274-259a-38e2-ad38-a8f4a1713f8a | -8.3586 | -44.1638 | 2026-09-27 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 530.1 |
| f6d82622-a0c2-3f14-b34d-20fde4206c5f | -7.055 | -42.849 | 2026-09-27 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 149.0 |
| 0af2f91e-2e06-3093-bd8a-7b8a782bfcd1 | -12.6647 | -47.302 | 2026-09-27 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| f3664303-e212-30ac-9510-bd4ef914e745 | -11.9619 | -50.5251 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| d82edd0d-b23a-3acc-8ca0-3007379ce2e2 | -7.2755 | -43.321 | 2026-09-27 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 184fd3e5-cd0c-38a3-9d74-aceb1834e55d | -12.2304 | -50.4073 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 5f5d7cc6-e346-38c2-9c67-a4f42bcee656 | -15.9869 | -54.9419 | 2026-09-27 13:50:00 | GOES-19 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 8d96806a-8180-3a3c-be14-fe9c45c5a8ee | -11.8014 | -49.8129 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 76776743-4b37-3c5b-9740-9a322492ab08 | -8.4483 | -54.725 | 2026-09-27 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 110f7e18-1e27-3f35-85f9-233ebdb2de37 | -6.8596 | -43.5003 | 2026-09-27 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c3a75a52-1a43-364b-9eec-2d99ca7fa4ee | -12.3488 | -50.1563 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d1d4a63b-6c57-31b4-871e-756e5b475e8c | -7.3653 | -42.1058 | 2026-09-27 13:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 4cf5cb3e-691a-30b7-af41-a09a5911f25d | -8.2525 | -49.9572 | 2026-09-27 13:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 87635330-b7f1-3beb-8fdc-6d665ff6e37b | -7.365 | -42.1298 | 2026-09-27 13:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| aa61b6f6-b14d-393a-9a6b-fa16373bbf05 | -8.3589 | -44.1406 | 2026-09-27 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 433.2 |
| a63e9a42-d1e7-35a2-9e89-e442e77bafdd | -6.8405 | -43.5254 | 2026-09-27 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 168.4 |


[Clique aqui para ver as próximas entradas](README58.md)
