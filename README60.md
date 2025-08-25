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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7defa36-e096-3d14-b415-0afefd8d3fb8 | -6.87472 | -45.65574 | 2025-08-25 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a859d25-cc1a-3b84-99aa-c7046c0fafc6 | -7.35915 | -57.63595 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cab04c5-d02e-33de-8010-bece6ef25578 | -9.16081 | -59.48858 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da380a49-7a8d-3aa4-957f-14e6350b7c70 | -8.60678 | -62.64245 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc4f95bc-4fa7-3a24-9e03-2b1344a1ce09 | -10.41623 | -64.39277 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7eb4aa4c-dbec-3715-960a-a4931c60c6d0 | -9.24376 | -59.62043 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa21cd95-440e-3602-ae19-78360c6d3fb3 | -8.86898 | -62.4625 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28e7e7ad-4a90-31ac-854c-89a8bd05f04e | -9.20662 | -59.50053 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d768797-994e-32bc-98a0-a223fdfbf086 | -11.19693 | -48.46677 | 2025-08-25 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3958b95-cbfa-3dbe-b431-74eac2a256ef | -9.02606 | -65.71158 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f8987a4-47de-3999-b77a-49d3bb05c969 | -8.88184 | -62.46478 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20d79ad3-eb13-3ace-ba3b-3bf0d6996428 | -10.02463 | -51.07093 | 2025-08-25 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad9fde90-c2ba-36f0-9553-9cefa8591c64 | -9.14996 | -59.46557 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eaa1f48-d04c-3952-bbdd-86c5cd56ff3f | -7.57265 | -63.43322 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fca868fd-9737-3524-9dfd-3c257f8c877c | -9.64629 | -59.65039 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b186720-2ba9-3283-b5d7-19970ea0e9f5 | -9.1593 | -59.47559 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 222efd63-2107-31cf-aa7b-594b0dad1fb2 | -8.1147 | -62.87782 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db62ee27-1773-329a-8bf7-1bbc3ce3cc9f | -7.32775 | -44.53544 | 2025-08-25 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7262fac-6cd9-367d-b312-155a9e7568f2 | -8.12562 | -62.88283 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b767ef52-b9ce-375f-9aa2-71f0189cd55f | -8.2285 | -61.38715 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 110c12af-b784-32e8-bfaa-c9cb7c31df28 | -8.98336 | -65.40755 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fd2c5f1d-c252-3f34-afe5-45af2bb53d38 | -8.89754 | -62.45074 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7da17f75-5d37-3718-a6a4-4f6242599a9d | -10.88579 | -55.79633 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6922f952-1a4f-3031-a711-f7f7bdda34e6 | -9.16247 | -59.52274 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9c2e10f-c537-3fde-a045-3b5496f4a693 | -10.82157 | -48.32975 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 393755cd-2775-3b75-9f5f-818347f46825 | -10.76706 | -47.0764 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97a5b335-5a27-33ee-8afd-fed0d80c67b8 | -8.22667 | -61.39801 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d194566f-72ad-30ac-9df6-b88b32a0a38c | -8.90433 | -47.33355 | 2025-08-25 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 415440fa-04d1-3dd5-954e-3e2e8ab6291f | -5.42763 | -60.17287 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 82c6b23a-1954-3f0e-a157-a3dd68c75cc4 | -9.15201 | -59.45329 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 437eb21e-70f9-3a4d-b849-645a07bd60cd | -8.22043 | -61.38574 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33a4ff1a-dba0-3d80-bdbc-d66c47919958 | -9.19129 | -59.45988 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 683ecfd4-0633-3c9f-965e-0e0a6989aace | -8.06784 | -47.31567 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1af3a56a-488f-3eca-940d-9a134583447e | -7.90302 | -45.88758 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b2a1b03-950b-3c65-b503-aa978b756f82 | -9.14858 | -59.47378 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92dc9dce-4b7a-3f32-b5f1-7ff4111c7420 | -8.79993 | -47.31631 | 2025-08-25 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16710702-e314-372c-82f8-4e3a1415e0a4 | -8.8847 | -62.44844 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 044b1fbd-acb3-3d50-bf6c-9a5eb1540630 | -10.39651 | -57.67665 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2a779a5-dd0c-3c83-91ac-eea8d8f183bb | -8.89689 | -60.54878 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6666f598-cc91-3a56-b07d-021984e873ab | -7.44208 | -57.62314 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f3b6cd8-f690-3997-aec6-11a45ea957ab | -5.71149 | -49.10413 | 2025-08-25 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b76f2080-46f8-377b-85f5-d03d6742417f | -9.81947 | -64.26153 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ee8fbec-b08b-371f-bb37-d1acccc7a07c | -8.63515 | -62.63443 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84f8824f-8e84-3e22-aac1-dca37341f1b3 | -10.89024 | -55.78973 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5fae949-0492-3cc7-bb0f-f23463a67d1a | -9.19645 | -59.65228 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e8bd8b3-1f22-3ee7-a00f-32a241a41c00 | -7.3172 | -44.53439 | 2025-08-25 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2655684-5009-3aff-8817-19262d0f8561 | -5.44857 | -60.19156 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3b45b44-b670-3a92-9f96-97f2a7486866 | -11.64689 | -46.20841 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc2818e3-3b52-3827-81b0-c96d4cfc7510 | -9.1799 | -59.46217 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e6c50d3d-b9e0-3e13-bb7b-3e5444e12cf6 | -6.63291 | -58.55242 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f19b7c77-fdee-3fd0-83cf-75e0761c88d1 | -9.1899 | -60.79176 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b176a45c-9667-376b-9914-5b823cad09d0 | -5.79901 | -59.21325 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e0be826-f4a4-32b1-8259-8f83c6c19076 | -9.20425 | -60.91884 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00be397b-4a5e-3a03-a461-5e141c1f1a54 | -8.06345 | -49.65787 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bbb8f0e-44b0-3ce6-90ff-87d6c8d328e5 | -4.96282 | -55.82447 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a8abbb2-1ff7-3f88-9e3b-8a9b66033333 | -8.90476 | -47.33027 | 2025-08-25 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3914767e-d222-31c1-bde7-460c751b7f83 | -9.14927 | -59.46967 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96a389aa-b681-3a09-a28a-82ff41fc8601 | -6.90332 | -44.40871 | 2025-08-25 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10ff96ec-2f89-3252-98a4-cd2f2b44c242 | -8.10838 | -47.13508 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78aa0648-aef5-3104-8d25-780304f0565e | -9.71476 | -54.98612 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e63a686a-5e11-3af9-b5c3-57d4e4d54c3c | -10.25422 | -59.10106 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0cfbdf6-15bd-30c9-b55d-f4698bad1089 | -7.52178 | -63.8156 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d4154b7-de9a-350c-8f9d-acac84b28b73 | -8.8868 | -62.41113 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d49e6014-bfd9-3e69-a2fe-42fe36b960d5 | -11.64635 | -46.21286 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02204429-8a0f-3466-8a79-02ee7445df06 | -9.4717 | -57.82731 | 2025-08-25 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b0b99496-dd1c-3b3b-b7be-39dfa348e8d4 | -7.78861 | -61.57174 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59e6aaa8-6214-3d12-9a03-01a9f46ec62c | -11.03385 | -59.17472 | 2025-08-25 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6daab01-963d-34d4-8d57-578886a240cc | -8.5469 | -63.51629 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f7d80ec-6f06-371e-a938-9860d42b5fe4 | -6.63004 | -58.54789 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e54d1fc2-cf52-3ab9-be3d-6b6a2bbad829 | -8.91245 | -62.41562 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a877c0e-be7a-300f-a014-989ff1d5fd33 | -9.18687 | -60.78634 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 80d8b576-f5c5-3986-a459-14f749482e45 | -9.61183 | -55.36376 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97262706-6a65-327d-95ad-244165d7fdcf | -5.42075 | -60.16462 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c7f581e-d25d-3b3a-90fe-f7cb3d557a9f | -9.81311 | -64.26873 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72f04ecc-fc11-31c6-8d84-99312c582e4f | -7.46967 | -45.02384 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3198a17-2992-332e-9a0e-3e69e0bd07a3 | -9.19283 | -59.47279 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f21ab143-c224-322b-bd17-978aebc9bd32 | -7.5585 | -63.85592 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26fea6c4-a991-38d4-bc22-b32f6d47a92d | -8.89182 | -62.43291 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b101de69-780d-34b8-a5af-cab06ae1abb7 | -9.96696 | -60.18417 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d866e011-8c17-383d-b63d-54f3f551e38c | -12.94023 | -46.3085 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5820dee5-19c4-3a32-8dfd-45cea665153d | -10.47184 | -48.32554 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a988a372-108f-37e1-af79-38583876b47b | -10.77455 | -46.39435 | 2025-08-25 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15ad49ab-2da2-3f09-8bda-d5f19860627e | -8.12531 | -47.13016 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3b4ddbc-49fb-33ff-946a-340d99f6a932 | -7.52659 | -63.81646 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3f8a88fe-cb0d-3a9c-b0be-6e35a197544f | -9.16418 | -60.8269 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c41dfee1-1502-3ac1-b30f-666b0efbf832 | -9.16507 | -59.48505 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 732215b0-c226-3c8a-8927-4398585013ca | -8.92594 | -60.71734 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a9999a6-9dea-348c-ba37-546783ad939d | -8.12275 | -62.87306 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 947321a7-4109-3335-9c6b-1484e97a35f1 | -9.00087 | -63.63443 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03f5107e-a932-37b9-b52d-a25762368bae | -9.19757 | -60.7931 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1da9b293-1b76-3578-8510-80804e856004 | -6.79165 | -58.64593 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d48b27b6-26d5-36ba-9c74-d19afd7086a0 | -10.70981 | -48.32593 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4e52329-e487-35f5-87f7-381df1c28c34 | -10.70553 | -50.5533 | 2025-08-25 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba3dc814-3502-3cd4-a546-26affffc4d08 | -6.9785 | -56.39602 | 2025-08-25 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 896224fa-549c-30a8-8382-527daeede1f7 | -9.10111 | -61.4366 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a01a4a9f-ae7f-3829-97e4-e0396764df95 | -8.91361 | -60.72016 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20f9eb3f-2aa4-349c-8c68-7ccf381653fb | -9.20328 | -59.61065 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 804e2622-52ab-3e6d-8ba3-701cddb161d0 | -9.16582 | -60.81725 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48fe91bf-a2ab-372a-b82c-37174ea19696 | -9.03677 | -65.73109 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b0905df-70f3-33da-a765-3057f2dd6b54 | -6.35549 | -57.96715 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README61.md)
