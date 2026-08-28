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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 125d9f0a-dd44-3df5-82f7-393243ada5a8 | -6.8569 | -59.4564 | 2026-08-28 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 873aaad7-803d-3d8c-8548-7f2e563001d2 | -8.8184 | -49.6308 | 2026-08-28 15:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ce0741cb-256d-3a0a-ac39-9575d0e0db82 | -10.7598 | -54.0179 | 2026-08-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 365d73a6-b8f3-3e18-8be6-1141e31db9b4 | -6.769 | -58.7066 | 2026-08-28 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d808aba4-c371-3169-a1a7-256bd78af68b | -14.6024 | -53.1508 | 2026-08-28 15:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 179.4 |
| cf604a00-36a5-31c9-9ca6-1df19685f778 | -10.5593 | -50.4663 | 2026-08-28 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2d02f292-8b42-3d70-ad15-d0e169e0641b | -6.1473 | -57.78 | 2026-08-28 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6d7d8e15-f76f-36a8-987e-fa8d270d38ed | -6.5865 | -55.4346 | 2026-08-28 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 54e70050-cc12-38b2-97b9-fe4d4b6be031 | -10.3897 | -61.2118 | 2026-08-28 15:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 8eebaf5c-92e7-3d4b-aeca-cf01ae016e12 | -7.3478 | -55.1744 | 2026-08-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 754a08f2-6109-33ef-874d-3d993bea90a4 | -6.1656 | -57.7988 | 2026-08-28 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 276.2 |
| dcd7a9fb-cffe-3531-9bc9-be50e6097746 | -10.5166 | -64.5186 | 2026-08-28 15:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 3f418707-49e5-3007-8192-ef2863fd15bf | -6.8018 | -59.4201 | 2026-08-28 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 8a6bcc69-fa52-39af-8ca4-98b4e3695ad1 | -7.3663 | -55.1734 | 2026-08-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| d721dced-3934-3355-a439-6e0c1e707054 | -10.559 | -50.4876 | 2026-08-28 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| cac9ea19-e336-38ae-af43-50a6f49d7111 | -13.2294 | -51.2904 | 2026-08-28 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| f7be4e86-bd7d-3d46-8050-0308a3bbe63f | -11.025 | -49.644 | 2026-08-28 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 545d7946-4306-3ca5-9211-164ea7598b42 | -6.2693 | -53.1322 | 2026-08-28 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 110da0dd-db1f-31a2-98cc-15382964fe75 | -12.3999 | -48.2073 | 2026-08-28 15:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f97b72b9-2662-30ff-8cd6-d6484fd62e32 | -6.7647 | -59.4601 | 2026-08-28 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 00c7e652-8c21-3e38-835d-87ef183cdf9b | -9.2282 | -51.5428 | 2026-08-28 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| cebf0cc4-9351-3b3b-9004-3161aa5ff7d9 | -14.1645 | -52.8269 | 2026-08-28 15:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ab43b6f3-33e8-366d-b013-a70cba4bb512 | -8.8031 | -70.8033 | 2026-08-28 15:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 72.4 |
| ab050dae-a5a8-3bae-95ed-c9f094387d67 | -10.7789 | -53.9958 | 2026-08-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| bbf38692-8f63-3201-acaf-0bf350fad6b1 | -10.899 | -50.5159 | 2026-08-28 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 02ae98c8-aec3-3a27-8398-5536755db0c0 | -10.3205 | -49.9567 | 2026-08-28 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 30ac2c90-4b4a-3af9-97da-ea5cfe9347d6 | -10.7407 | -54.0401 | 2026-08-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f2fdaf01-68c0-34f8-bbb4-620b43f11c7d | -10.572 | -57.4752 | 2026-08-28 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0bdd1a53-d397-3ab5-8e07-1226eae8196b | -11.697 | -54.5876 | 2026-08-28 15:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d60350f4-18f3-33b9-b459-d7d63dff1953 | -6.7833 | -59.4208 | 2026-08-28 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0e4547cc-7f63-365e-9416-4024c8610d3e | -10.9216 | -50.2571 | 2026-08-28 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 04554406-f399-3672-b1e4-425a39123a9e | -10.3202 | -49.9782 | 2026-08-28 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 173.4 |
| af5711ae-ae97-3a93-a943-f7897470d9c9 | -6.5863 | -55.4546 | 2026-08-28 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 5b7d46b4-c809-3e5d-9ba9-a74a39f85a3b | -9.7028 | -48.1366 | 2026-08-28 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 10ee4630-026f-3aae-ba3b-d9c73d483908 | -11.0247 | -49.6656 | 2026-08-28 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0a7f36dd-b82e-38a0-8359-abde39b51cab | -6.7451 | -59.6533 | 2026-08-28 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 982d6f7d-f90d-3773-a05c-ec072d6bb562 | -9.1525 | -49.9639 | 2026-08-28 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 2c612d9e-931b-37f8-9079-7420ae183e2c | -9.9708 | -53.9419 | 2026-08-28 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 403.9 |
| 2a62b02a-87d6-38da-b71f-442c58108490 | -14.2537 | -52.0964 | 2026-08-28 15:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 2b8a9c85-bed5-39d7-b56e-e73da01b0253 | -9.4758 | -48.1822 | 2026-08-28 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| b1269a93-0e49-3322-81d1-fb56dd9560dd | -10.4981 | -64.5005 | 2026-08-28 15:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 524c28a8-df9f-388f-a662-f17ad0be4774 | -6.2692 | -53.1526 | 2026-08-28 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| ded4bda3-0ab5-3e46-94b4-e2aef5bdee5a | -7.0289 | -55.6909 | 2026-08-28 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 785634d5-3160-3ad2-b910-c6c249845f40 | -6.2676 | -53.3768 | 2026-08-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 3fd883ef-f943-391c-ac8d-82cbfb23434b | -16.1641 | -58.5851 | 2026-08-28 15:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.6 |
| b308db28-521e-31ef-80f2-993db7bca7cc | -6.9737 | -55.6341 | 2026-08-28 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cabd2eb4-3bc4-339e-9653-3476bca6bcc4 | -9.4329 | -51.6926 | 2026-08-28 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 83aa842f-dae5-3b61-b4f3-99963a05a646 | -10.7975 | -54.0146 | 2026-08-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| db8e2ecc-a160-375f-8889-3604966c8c30 | -6.2298 | -53.4805 | 2026-08-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c2fd96f6-5e9b-38ca-a8e4-a3b4137dd194 | -6.1556 | -53.5047 | 2026-08-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 7810db15-6772-34f7-9296-aa52204f0441 | -6.7648 | -59.4408 | 2026-08-28 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 981aec32-9fad-3188-99f2-e875cf8acd92 | -12.0729 | -47.1838 | 2026-08-28 15:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 688ffe89-5729-3f69-b3e4-0d7b90e13b4d | -14.2209 | -51.7602 | 2026-08-28 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| a22fc605-62f1-3d66-8b75-098df94093c3 | -12.2281 | -50.5578 | 2026-08-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| df64283c-cea4-3711-babc-4a8dacd08a49 | -14.5827 | -53.1744 | 2026-08-28 15:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 1d715e1e-8f62-34d7-bc7b-6341062d5cfb | -9.1525 | -49.9639 | 2026-08-28 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| a46092dd-5684-3dd9-b3b3-efefd3fd6435 | -8.3902 | -62.7152 | 2026-08-28 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 9d757bc1-7ba1-36f4-b7b4-f1ccb0a2d032 | -6.5865 | -55.4346 | 2026-08-28 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 6eb65346-93aa-34a2-82cb-0c25fdcc3e90 | -8.7757 | -50.083 | 2026-08-28 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 3a15b300-915a-3876-add5-81299542fe53 | -8.5777 | -54.8373 | 2026-08-28 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| d0679ae7-4d1f-3fac-bf16-c6dc161db3a3 | -6.8257 | -55.6218 | 2026-08-28 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| cbd2ea32-eb59-37ad-a2ca-921914a9c35b | -10.3898 | -61.1925 | 2026-08-28 15:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e3cfbf65-92db-30fa-a1ea-0452a85bfc43 | -8.8184 | -49.6308 | 2026-08-28 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 5e16ef45-ef60-397c-94e9-edf4fa1a281c | -10.7649 | -50.6366 | 2026-08-28 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 018ad879-affd-3ed0-abe5-eab6c71b96ca | -9.1714 | -59.5793 | 2026-08-28 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c9bfd8b9-1323-3f18-97b4-a4f1cf7ea9ae | -10.7593 | -54.0589 | 2026-08-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 798443f3-192b-3e6e-a998-fe9c3fe57e60 | -6.6195 | -53.3984 | 2026-08-28 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 0a0d8090-7982-349e-b0ab-840f9f6c222a | -11.006 | -49.6461 | 2026-08-28 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8be65f16-9697-30b1-b85b-b911e43d7bf2 | -7.3665 | -55.1534 | 2026-08-28 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 79d3889a-c0ff-36c7-a8e9-4ad40edb5245 | -11.1939 | -53.9993 | 2026-08-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7bd084e4-38d3-34c6-b45d-ddff7a517368 | -10.9402 | -50.2764 | 2026-08-28 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 89174b2a-2482-3368-a5da-e3aa80dd1e0b | -10.7978 | -53.9941 | 2026-08-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| f39a9737-2c34-3d2b-80f4-7c2c12ad53b4 | -6.7513 | -55.6853 | 2026-08-28 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 37363c63-605d-3451-82d9-480c9f5e5833 | -8.5964 | -54.8361 | 2026-08-28 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| a258dc2c-ca90-3192-9e91-cf606d35c111 | -10.7789 | -53.9958 | 2026-08-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| e2b05e35-ea56-3d45-932d-4b2d290cf2fa | -10.5166 | -64.5186 | 2026-08-28 15:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 4dffcb30-d19d-314a-9586-aac16b71552e | -6.1472 | -57.7995 | 2026-08-28 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| fa5ce83b-6488-3902-b761-563bc51745d1 | -10.4981 | -64.5005 | 2026-08-28 15:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 208.6 |
| 30cec142-bbcd-365f-bc62-cddab0877c18 | -6.7648 | -59.4408 | 2026-08-28 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8941213d-276d-3e73-a34f-e7f272fb158a | -8.5971 | -54.7553 | 2026-08-28 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 20e9093a-31f1-30bb-8715-fba6ba194388 | -11.0247 | -49.6656 | 2026-08-28 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 24056ba3-0bb3-34f1-9b03-eb3aa07da9fa | -6.7647 | -59.4601 | 2026-08-28 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c105cf38-b042-3628-80dd-a904e3bdde0e | -6.7833 | -59.4208 | 2026-08-28 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 85febf09-5ba9-3e11-aeda-77e3f6097012 | -14.2302 | -45.2472 | 2026-08-28 15:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 18fcf6c8-b9ea-3d55-adff-9d25516e1529 | -6.769 | -58.7066 | 2026-08-28 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 43067e29-0045-3c83-aaa1-990a8938784b | -6.1656 | -57.7988 | 2026-08-28 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 287.8 |
| 49b1bd7e-9d89-36bf-aae7-fdc5fce32976 | -14.3182 | -51.7046 | 2026-08-28 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 338fa7b9-b862-3bf7-a753-f85047061eed | -12.209 | -50.5601 | 2026-08-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 16201220-80b6-3710-a6a1-581c59db9fb7 | -9.9708 | -53.9419 | 2026-08-28 15:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 332.8 |
| e24d48cd-82a5-334d-b141-2047cd885f47 | -10.559 | -50.4876 | 2026-08-28 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 90601d97-e5f0-3e75-85d2-bf65e7aa883a | -10.8463 | -50.2224 | 2026-08-28 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 02a862bc-faac-394a-a656-0bd6d8ea8c65 | -10.3205 | -49.9567 | 2026-08-28 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 7066362f-12e1-3ed1-a43c-1fd26486136b | -12.2093 | -50.5386 | 2026-08-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b7c3ae4c-cda9-3fbe-bb24-8d418d0e1aa6 | -11.025 | -49.644 | 2026-08-28 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 698b9cdd-0576-36dc-be0b-e93ffa76cbd3 | -14.2297 | -45.2705 | 2026-08-28 15:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| d6222657-b526-3c23-8452-a386a08efd4a | -10.7975 | -54.0146 | 2026-08-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 6fed3c64-16ee-3da5-993b-04511c86d659 | -6.952 | -58.9699 | 2026-08-28 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 882dc9fb-8b49-36b8-83c1-a463ee7f05bb | -8.9873 | -65.4379 | 2026-08-28 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c2da1b34-ad4e-37a6-9eee-56be5e0577fa | -16.1641 | -58.5851 | 2026-08-28 15:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 165.2 |
| 9ae80194-d758-3bf7-941c-3b701c7095fa | -4.903 | -56.279 | 2026-08-28 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |


[Clique aqui para ver as próximas entradas](README85.md)
