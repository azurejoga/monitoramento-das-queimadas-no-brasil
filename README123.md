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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da07c80a-49bc-34a4-9adc-8defae0f7186 | -9.2472 | -57.129 | 2026-09-19 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 44ef4e93-4c27-3f74-820e-a5011ce4b681 | -9.2606 | -45.9164 | 2026-09-19 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 4d3978eb-5dd6-305b-8507-cc627a5f7986 | -10.9133 | -50.8549 | 2026-09-19 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 1f244390-1dea-33a0-82ad-243abf0755e1 | -8.411 | -54.7274 | 2026-09-19 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| a779f4a1-da1e-3a9d-8cf8-efd91a3bd10e | -10.932 | -50.8742 | 2026-09-19 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 257.3 |
| 0215a740-ba7d-34f5-93b4-ca7d0d258b35 | -2.458 | -57.9033 | 2026-09-19 15:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1c0a136f-3f87-38be-ba1f-1b71386033c8 | -11.3813 | -44.0554 | 2026-09-19 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 0a269332-839c-34e4-9590-7e5723de4ac3 | -3.2087 | -57.7925 | 2026-09-19 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 49b77bb1-c1e5-3530-92bc-7a1ed9a8d475 | -3.3638 | -61.2904 | 2026-09-19 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 28fb86d0-8342-37b8-8608-723ba0be8f36 | -10.7994 | -50.8881 | 2026-09-19 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 42cdfd93-9cac-335e-a75d-299b0ffda0fe | -3.9902 | -41.2759 | 2026-09-19 15:30:00 | GOES-19 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 376.6 |
| c94d0664-a67b-32fc-be03-9ed217963111 | -11.1228 | -49.4384 | 2026-09-19 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 171ec0b8-ab8e-308c-adbe-aa9096f1eb1e | -8.1496 | -54.8049 | 2026-09-19 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0414200d-3938-3287-9fa9-55a38cd5cdf9 | -7.8598 | -44.8595 | 2026-09-19 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 6ca5bf48-56d7-374b-bfaa-87d87a9474bb | -5.6408 | -43.392 | 2026-09-19 15:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 256.7 |
| 8150e4a6-87bc-32b9-b7f8-fa475afaf62f | -5.1255 | -55.955 | 2026-09-19 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| eb94c08f-f715-318c-b417-a1fc884529e4 | -11.874 | -50.0415 | 2026-09-19 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| a4f74d6b-1cd4-3f88-99ef-74dc1a3d785a | -12.1531 | -46.9707 | 2026-09-19 15:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 27d761aa-3bbb-38db-9e7f-1fe3ca967e3d | -12.2688 | -49.1907 | 2026-09-19 15:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| cc0ac76b-02cb-31b4-9593-a721774aa487 | -8.7734 | -48.6651 | 2026-09-19 15:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 72da483e-537e-35a8-ba16-ec0c41697b43 | -1.5674 | -54.4555 | 2026-09-19 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 9012ec29-dd81-3309-ab20-26a510628943 | -7.6574 | -46.1013 | 2026-09-19 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| c0603bed-5732-3fea-b202-187952dc6789 | -8.8639 | -45.937 | 2026-09-19 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3899ab01-3ab2-3846-8bbd-1a270f2403d1 | -12.2879 | -49.1883 | 2026-09-19 15:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 254.7 |
| 26a9e721-ea7a-3647-b763-ec029c9467ad | -5.5663 | -45.5265 | 2026-09-19 15:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 7d729b96-999a-37b1-a9cc-2c04dd9e91dd | -3.4462 | -57.9812 | 2026-09-19 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 245c3945-0966-3597-adf2-4692d9ba0369 | -1.5859 | -54.4153 | 2026-09-19 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 7a83a462-7a27-3fff-89d4-d4527def70f9 | -11.4351 | -51.4774 | 2026-09-19 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| f2634f9a-3006-3ae8-b9f8-c211a964ddd9 | -11.7313 | -50.68 | 2026-09-19 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 554ad337-b9f3-3339-8b19-88adf8f9477d | -3.3311 | -59.8101 | 2026-09-19 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 12914e4b-4c61-3bcd-83d5-7bfc334e26d3 | -10.913 | -50.8762 | 2026-09-19 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 8d01faea-15c5-390c-a46a-4f924bc83fae | -7.676 | -46.122 | 2026-09-19 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 3b00b862-3bb4-37fe-8ad1-6d89d2719e09 | -10.5481 | -51.3156 | 2026-09-19 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 496fd726-95fc-34dd-a654-695cfeb760b6 | -8.5984 | -54.6139 | 2026-09-19 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2bc9aa3a-4489-30cd-a65f-265e365e19d3 | -11.0614 | -49.7477 | 2026-09-19 15:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 242.4 |
| 1827e480-2b62-33bc-b142-1ea3186d7be2 | -9.247 | -57.1488 | 2026-09-19 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| da30ee8b-6730-3e99-ade9-c18940465277 | -11.4354 | -51.4563 | 2026-09-19 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 157.7 |
| b7fb86f8-1e43-3cd7-a8e2-3e71194d09f4 | -9.3611 | -48.3032 | 2026-09-19 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 272.0 |
| 9c4f3c9f-743f-34d2-bc87-8d119842b8c7 | -7.7118 | -44.6451 | 2026-09-19 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 925.7 |
| 34d07920-41db-31f2-b19c-ddee4cfee272 | -7.0029 | -49.7551 | 2026-09-19 15:30:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 7239e6e7-1b15-3a77-9851-ea2efadb4290 | -11.299 | -51.7238 | 2026-09-19 15:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 474f651e-2208-35db-ad07-7f0a51813b8d | -5.7429 | -57.6009 | 2026-09-19 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 9f44cfb4-d883-33db-9b51-4a4240c5a74a | -12.1527 | -46.9933 | 2026-09-19 15:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1f1b0277-01ac-31b9-ab6f-d70f85fd3f7a | -10.9872 | -48.3429 | 2026-09-19 15:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d0ce0a6c-a26f-37f5-ab29-2b40e9f2483e | -9.0096 | -44.9209 | 2026-09-19 15:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 8002f56a-5b08-38a0-b9c4-56d884cd53b0 | -8.5986 | -54.5937 | 2026-09-19 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e6d30d50-47bf-3d18-b2b9-7cdb67c733b9 | -11.8746 | -47.6125 | 2026-09-19 15:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 3c83a298-fb10-31ce-9347-690928e84084 | -1.1991 | -55.7304 | 2026-09-19 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 48b33c3a-32eb-3043-a09c-bdf6dbdf2670 | -3.3638 | -61.3093 | 2026-09-19 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| b4518755-103d-3420-b0b1-9789d08e3a9a | -10.8367 | -50.9266 | 2026-09-19 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 9a52f3e2-8449-33b2-bc59-ffe6eb464094 | -11.4524 | -50.2624 | 2026-09-19 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| af0aefe1-20e9-35ee-a683-b740aec364c7 | -2.8975 | -57.7793 | 2026-09-19 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 9342bbf3-a835-3a92-8c9e-83d8c1b06e97 | -8.4737 | -47.0053 | 2026-09-19 15:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 68d27902-ed49-3f49-9c69-fab41e6df77e | -12.2883 | -49.1664 | 2026-09-19 15:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 3e2b7026-d37f-39f2-8114-c98a82079983 | -10.8282 | -50.1601 | 2026-09-19 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 0b3f7e8e-e67a-3e68-b343-24efeaf580f4 | -12.216 | -50.1079 | 2026-09-19 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 2cf1ba72-715b-361c-8fe6-7f6495a7c33d | -1.2357 | -55.7103 | 2026-09-19 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 788a7066-39ff-3792-881f-8bdc56c17b42 | -11.3621 | -44.0582 | 2026-09-19 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| cc0b1408-bccc-3668-b44a-762d23b6704d | -6.1836 | -47.5477 | 2026-09-19 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 92070e2c-d5a3-3c52-948a-78c73b795967 | -10.8469 | -50.1795 | 2026-09-19 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 269.1 |
| 032879ca-05c5-3030-a4da-9d1576d64e2d | -10.9168 | -50.5992 | 2026-09-19 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 0f149a80-32f7-372d-84d8-7f56e738dc6c | -12.0072 | -50.047 | 2026-09-19 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 53d85566-41bd-3d9c-97ff-6111a5c940ad | -5.7429 | -57.6009 | 2026-09-19 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| b010cde7-a6d3-32ce-9efd-fe323d2d5dec | -7.5642 | -49.6071 | 2026-09-19 15:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 5a256c84-553e-3584-a23a-0fc57661f6cb | -11.7823 | -49.8152 | 2026-09-19 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| a5029e2f-965d-3a2f-b80e-027c4beee4dd | -11.4715 | -50.2603 | 2026-09-19 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| f0a785b8-7d6a-3cfc-9005-ffb3eee1b633 | -8.9412 | -44.3995 | 2026-09-19 15:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 4f42c342-bd3a-3b9f-9199-cb8edb05d1e1 | -5.6408 | -43.392 | 2026-09-19 15:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 67ae4de6-e00d-3797-933d-b7e454a68e8d | -8.4108 | -54.7476 | 2026-09-19 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 51f5e982-f3d8-30a8-b861-a5a8d4cb31e5 | -10.809 | -50.1836 | 2026-09-19 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 27d8c76b-6292-3fa3-ad7c-7dcdb0333f00 | -11.4354 | -51.4563 | 2026-09-19 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 8d32eb24-a2d3-387f-92a1-2c7d864c1541 | -11.7313 | -50.68 | 2026-09-19 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 9ae87d30-fdc7-3f18-a9a6-e9e4a9dda845 | -10.932 | -50.8742 | 2026-09-19 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 18c48b3e-7aa2-3cb6-bc7d-27e149dcd6cf | -10.8367 | -50.9266 | 2026-09-19 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 4ed251cb-cf42-3d82-9f83-f37d84d86cd6 | -2.9157 | -57.7983 | 2026-09-19 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 261.2 |
| c0e8f134-cf6a-3b71-92c5-6721c6d86bab | -11.3609 | -44.1286 | 2026-09-19 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| a63eca05-6835-3f67-8572-93daf97786aa | -10.7994 | -50.8881 | 2026-09-19 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 6c1540e2-91a3-35de-96b8-69cbd3077b85 | -11.874 | -50.0415 | 2026-09-19 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c5ac3c12-069d-3435-908f-1b9dbc58fd92 | -12.2688 | -49.1907 | 2026-09-19 15:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 6ead3054-13ed-39c6-97e9-c9a4c5f8e143 | -10.5481 | -51.3156 | 2026-09-19 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 6c5145d7-1980-3083-9963-86b194e9a154 | -11.1035 | -49.4623 | 2026-09-19 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 297.9 |
| e6679fa6-3162-3b71-a574-6d85c7142e72 | -9.2567 | -46.2098 | 2026-09-19 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 58a4d0a9-8b42-3dc3-9bd1-d5c258f52227 | -10.8279 | -50.1815 | 2026-09-19 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 228.6 |
| a79dc9b3-3b74-3a48-8944-3de1a4e432a1 | -7.7847 | -44.8441 | 2026-09-19 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 5f57ad66-1d46-3ee3-92e7-65e3cbb77e7c | -7.0029 | -49.7551 | 2026-09-19 15:40:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 5fb26fff-f4d9-32f0-9608-f713c42194b2 | -8.411 | -54.7274 | 2026-09-19 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 17eae868-0e7e-3068-86ab-0e4c0dbcee53 | -2.0765 | -56.585 | 2026-09-19 15:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 89dafc97-cbed-30f3-be41-c80b74f38787 | -12.1531 | -46.9707 | 2026-09-19 15:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ac572d14-ce83-3bc7-9403-d697171685b5 | -2.8974 | -57.7987 | 2026-09-19 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 429.4 |
| 2123a955-9ac5-32cd-9a36-b617ba2ff7f7 | -11.3813 | -44.0554 | 2026-09-19 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 391.7 |
| 43446482-a35c-3b0a-aaf4-a6a3e988216c | -11.3433 | -44.0376 | 2026-09-19 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 172.1 |
| cef5ab2a-c387-391d-b5b5-5894144e635e | -9.1341 | -51.5718 | 2026-09-19 15:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 045ca2b2-dc3f-33c5-a29e-8190500152a5 | -1.2357 | -55.73 | 2026-09-19 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 7298b11e-75a0-305f-a9ce-286243bbfe08 | -6.9224 | -55.0376 | 2026-09-19 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 4de8ea22-d0c9-33fe-b0f7-0a2a6eff443d | -3.3311 | -59.8101 | 2026-09-19 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 145.0 |
| c05bcee0-a35d-3cc7-a717-5cbcbc6658fe | -11.0065 | -48.3187 | 2026-09-19 15:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| edd1e44b-c5a7-3ced-83b3-3547d5bda6ac | -3.6076 | -59.0769 | 2026-09-19 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a8750ce4-5bc3-3a47-9d77-466c667e825b | -10.913 | -50.8762 | 2026-09-19 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 9bbbb84f-1c0a-3779-8928-e8c421b6b931 | -3.2087 | -57.7925 | 2026-09-19 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| f957b5c1-1936-3196-9f66-c2163009311c | -10.6703 | -50.6465 | 2026-09-19 15:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 150.6 |


[Clique aqui para ver as próximas entradas](README124.md)
