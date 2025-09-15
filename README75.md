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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22a4e24b-d915-3cd6-92e4-6af6c7869b9a | -10.9155 | -45.6232 | 2025-09-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 293.3 |
| 51e57c30-0fe7-3779-80aa-6374dc0f3b77 | -8.5947 | -46.3471 | 2025-09-15 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| e3080804-0d0e-3c73-bb34-207c7b23a747 | -7.5281 | -47.642 | 2025-09-15 14:00:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 3e5830e6-f1bd-398b-83bc-c5415fe7d74d | -14.5168 | -47.3304 | 2025-09-15 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ef5e58dd-2a65-37e8-ba72-b30a6c758f92 | -8.6507 | -46.3862 | 2025-09-15 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| bc5f8531-55b5-3ecc-974b-8767024da814 | -9.7135 | -47.3424 | 2025-09-15 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| cb3066be-c308-3894-8abe-c17145ca507d | -13.2031 | -47.29 | 2025-09-15 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 33c36068-6641-3b12-a50f-11f5a51e43a9 | -10.9346 | -45.6207 | 2025-09-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 387.2 |
| c4ae0929-fdc0-31a7-a00e-0d3d7c6a4962 | -13.8974 | -48.3027 | 2025-09-15 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 59e434e1-9597-3262-9df8-087aa9e908e5 | -11.1303 | -45.3196 | 2025-09-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 269.1 |
| fb45d253-53b8-3811-9915-db3d52861053 | -10.9667 | -47.1952 | 2025-09-15 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 766e52e4-f440-3934-9237-56d04289613a | -12.1668 | -44.0988 | 2025-09-15 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 4bc202d3-82f2-3822-9b72-51b3e4a851e9 | -12.8212 | -47.1445 | 2025-09-15 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 82daddad-23ad-3602-8907-6ceff70f30b3 | -12.8087 | -44.744 | 2025-09-15 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2ac69d78-ec75-3147-8a6d-e55070b91254 | -11.6626 | -46.5884 | 2025-09-15 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 8ecb3d5c-7082-351c-a9ff-76baa1dc7f2a | -10.7078 | -50.6638 | 2025-09-15 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 766944ce-e5b2-3ba4-9bbc-fb7c043a6772 | -12.9988 | -47.9462 | 2025-09-15 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| de9f74e5-9550-3794-b41e-666406025c8f | -10.935 | -45.5978 | 2025-09-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 2f0d2ff0-49ae-3695-b9bb-6a797f9bb4a4 | -7.7027 | -48.8451 | 2025-09-15 14:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 121.1 |
| fdd58329-02a7-3ea3-ad45-5b57e9f5789a | -8.4148 | -47.2103 | 2025-09-15 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 5299a0c0-0004-307f-a4ef-436d4bb14503 | -5.9271 | -44.8671 | 2025-09-15 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 38efe78c-61a1-31dc-aaae-eebcd05fb723 | -10.9477 | -47.1976 | 2025-09-15 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 6521182c-13c2-3513-a14c-be289356c4a1 | -11.4076 | -43.6519 | 2025-09-15 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| dabee340-adbb-3742-9db9-257179422ee2 | -6.1881 | -41.1855 | 2025-09-15 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 148.3 |
| 77a5f17a-3dbd-3f32-8db6-9aecdddec6a4 | -10.9159 | -45.6004 | 2025-09-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| e64320aa-06bb-33ea-8eab-9b3a1a1a5e4f | -12.6764 | -47.725 | 2025-09-15 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5c30a191-66a1-32b9-92e6-ca43a134c466 | -5.9459 | -44.8657 | 2025-09-15 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a3b9c369-4765-3bc4-8f0a-7a147f945818 | -7.6838 | -48.8682 | 2025-09-15 14:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 5bd3ae25-787c-3341-80b4-137b3ab37c3e | -9.5167 | -47.9369 | 2025-09-15 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 1d6d30f8-49be-3893-821d-589cfe5cd751 | -13.0177 | -47.9657 | 2025-09-15 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| c2c6d1d5-d6ac-3e49-88b6-b95cac4150ea | -12.6533 | -47.9507 | 2025-09-15 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 1eb7ea6c-024d-3c86-8a65-cc2e001d98ec | -6.1693 | -41.1872 | 2025-09-15 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 208.3 |
| 17bd9e19-67b4-38eb-8313-c2ff23d32366 | -8.938 | -46.0418 | 2025-09-15 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 21cee6ac-5ba6-3a7b-be2c-df3865c1ed39 | -13.8781 | -48.3057 | 2025-09-15 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b53544d3-900c-3179-a3bd-a2f2ad9f6d48 | -7.9631 | -45.6675 | 2025-09-15 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 4db0aa7d-757c-3ed4-b065-1ffd6f4bfc99 | -14.8218 | -51.6362 | 2025-09-15 14:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 07efcfe7-f697-366d-8b76-48fbfe181052 | -8.651 | -46.3637 | 2025-09-15 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 95208377-6dca-3973-abfc-2dbacfe6869a | -13.1838 | -47.2929 | 2025-09-15 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 18045106-a673-3bde-96a2-4034adfa4688 | -7.5094 | -47.6435 | 2025-09-15 14:00:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1c0ed65c-3bc0-3536-932c-766522bd68c3 | -6.1504 | -41.1889 | 2025-09-15 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 171.6 |
| d374a906-a854-3481-9898-924b14820eec | -12.1663 | -44.1224 | 2025-09-15 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 938c32ff-e0a7-3e9d-bf9d-5dbf017abcc8 | -6.2723 | -44.015 | 2025-09-15 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 8bdc11be-07aa-3186-9afa-aa8d92e1033a | -7.9634 | -45.6449 | 2025-09-15 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| e420f685-294e-3903-b6de-3eff79769834 | -11.4569 | -48.7026 | 2025-09-15 14:00:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1769b41e-cb0c-3c96-a08d-8781fb62717e | -6.3372 | -43.1492 | 2025-09-15 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 75369b21-2ac4-31db-b965-1d55313850fc | -6.337 | -43.1727 | 2025-09-15 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 4f5489aa-23e4-3514-a0cf-37f54dea3303 | -8.4145 | -47.2324 | 2025-09-15 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 5a23040a-75bc-323e-b244-5b0ad0c66bd1 | -16.673 | -49.7615 | 2025-09-15 14:00:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 87841768-bab4-34b7-91c6-774443111eeb | -10.948 | -47.1753 | 2025-09-15 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| c242b4f1-8894-342f-8ede-9988e3ec79c3 | -10.9671 | -47.1729 | 2025-09-15 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 54bcc8eb-f2ee-3283-8ac7-bce885990b16 | -8.7677 | -46.0823 | 2025-09-15 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 275bf57a-6fbf-3a3a-8eae-2632554bbdd4 | -9.1334 | -46.9609 | 2025-09-15 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 02b84265-55ee-3666-97c0-e65b3b19d0f7 | -5.8399 | -44.1642 | 2025-09-15 14:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| a7a1f0d8-c9ad-3680-898f-525726b0a1e6 | -11.1306 | -45.2966 | 2025-09-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 682c583f-5398-3dd7-927c-1a027e46b124 | -15.6778 | -47.7198 | 2025-09-15 14:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 79.7 |
| c55800ef-b110-3744-8040-7e2b662e0718 | -8.768 | -46.0598 | 2025-09-15 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| dde15af6-fef5-3f9b-864e-6b6a3f19f3fd | -8.9545 | -46.22 | 2025-09-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 496.2 |
| 5a0f6a38-9b3e-315d-bb72-062f78ef0bd9 | -11.0617 | -49.7261 | 2025-09-15 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 87bdcc61-bd18-3654-94f4-9542da7a25a9 | -11.0807 | -49.724 | 2025-09-15 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 355.3 |
| ef4eae9c-f6dc-3bca-a885-6dd5a0757ef7 | -14.8218 | -51.6362 | 2025-09-15 14:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 9876e37e-588d-3933-b017-b5a14cba4104 | -5.7673 | -43.9161 | 2025-09-15 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| aed52f2e-89c5-3ae3-8ef4-8b7db32a80a3 | -8.917 | -46.2015 | 2025-09-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 323.8 |
| 91f7cb0c-9e8f-3c45-bd53-6ee86c971979 | -8.9548 | -46.1975 | 2025-09-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 777ae6d5-755c-39a6-9a83-f074cde2d107 | -6.1504 | -41.1889 | 2025-09-15 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 166.0 |
| 886a16b6-d3be-3424-ad10-a5e5d4447269 | -13.1842 | -47.2704 | 2025-09-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 5920a7fb-66ff-300e-97bc-67f997d06563 | -10.948 | -47.1753 | 2025-09-15 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| b9bb4212-76bc-3768-b33a-5ebbe0737db8 | -11.0804 | -49.7456 | 2025-09-15 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 349.0 |
| 0a5d39c2-3678-301d-b292-e807b4d5612a | -7.7027 | -48.8451 | 2025-09-15 14:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 361df61c-f33d-3c1f-a727-13a80f3860ee | -11.638 | -50.5625 | 2025-09-15 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 03c057d3-074b-378c-97ee-90308b6220b9 | -13.1838 | -47.2929 | 2025-09-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 18bcc3ca-5002-37ab-8d77-f730a80bad5a | -11.6434 | -46.591 | 2025-09-15 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 816d9a19-56b6-30a7-b45f-20dec3d97d22 | -6.3989 | -42.6263 | 2025-09-15 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 52366b41-cc41-3e4b-ac38-460760229d4b | -8.8987 | -46.1585 | 2025-09-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| d25c6e8b-99a6-35b4-8c89-c455f8654d56 | -11.3338 | -43.4979 | 2025-09-15 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| d0f57a03-2f80-33b1-b41b-40378491d4b5 | -8.5944 | -46.3695 | 2025-09-15 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 72127678-c510-3af0-8c7a-487a16903082 | -10.935 | -45.5978 | 2025-09-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 51a4c5c6-85b9-3da5-a20a-1da2a13a5f56 | -8.9262 | -45.5004 | 2025-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 440534fd-bbb3-3474-bb05-fad38f706ea0 | -8.768 | -46.0598 | 2025-09-15 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e7f4a21c-ef6c-3994-a803-c92a67d7e8b6 | -8.9568 | -46.0398 | 2025-09-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3002764c-2d9d-351b-b765-8fb0dc6465ce | -8.651 | -46.3637 | 2025-09-15 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 0c30f3ab-047f-3c00-b030-c64b6a69478e | -14.348 | -46.1054 | 2025-09-15 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| a2b84533-13f0-3bd2-b0eb-be8284108dbe | -10.9671 | -47.1729 | 2025-09-15 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5234b34b-0344-3771-8383-04e4b66dd1f2 | -7.8452 | -46.1063 | 2025-09-15 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| cf31676c-3b9e-35f8-b4f8-9ccf72c4fcf9 | -11.4569 | -48.7026 | 2025-09-15 14:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 02841621-247c-3b62-981f-54115d0beac5 | -9.0605 | -49.8014 | 2025-09-15 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 03b8bd91-7f5e-3da7-9e5f-3fe563c4643a | -12.8204 | -47.1896 | 2025-09-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 59cf1116-8660-3565-994b-d640b7ee6931 | -6.169 | -41.2114 | 2025-09-15 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 155.3 |
| c9092b52-5b05-3bbf-94c8-0d35ceaca644 | -13.8815 | -48.1271 | 2025-09-15 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| ba499cca-9748-363d-8b41-95291b26f4d6 | -8.7868 | -46.0578 | 2025-09-15 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 110fe4c5-84d3-32da-8254-4d3307949d33 | -9.0793 | -49.7997 | 2025-09-15 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d0b78d02-9d1e-357b-b649-23c072aadcb9 | -10.9346 | -45.6207 | 2025-09-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 343.7 |
| caa971c9-c90b-3b65-8662-2e8bba060eef | -5.9271 | -44.8671 | 2025-09-15 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 317aa1d4-c62f-3a4e-b74c-d9bcc784e4b6 | -8.4145 | -47.2324 | 2025-09-15 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9d348e06-e0bc-3554-9e15-cc7368a14ca5 | -8.6133 | -46.3676 | 2025-09-15 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 6448d6df-b869-340a-8f94-09ca3972f86d | -11.6622 | -46.611 | 2025-09-15 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 2387a4f1-14d9-3d27-9a31-8a6ff7d69d92 | -6.3372 | -43.1492 | 2025-09-15 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| a3b8e834-6166-3eb0-b36c-5845f02f408e | -14.4973 | -47.3336 | 2025-09-15 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 0c6a7cc8-b08a-3fae-87be-41140668cf0c | -11.1303 | -45.3196 | 2025-09-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 348.8 |
| 4cc0b673-c1b7-3267-8405-777cd9c1d715 | -8.9076 | -45.4797 | 2025-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| d9da0cbf-d98c-3fa0-8011-f22ee4239292 | -8.9731 | -46.2405 | 2025-09-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 243.4 |


[Clique aqui para ver as próximas entradas](README76.md)
