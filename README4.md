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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d7287ab-5860-3364-9b72-2df4df9586da | -7.18855 | -50.83229 | 2026-09-13 00:05:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e32d36d0-70ef-30f5-acf3-81c182845a5d | -5.2892 | -49.02399 | 2026-09-13 00:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 38ceab4a-4122-3dde-b8f1-0ee8c0adbf19 | -3.04511 | -51.25696 | 2026-09-13 00:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 0a0be157-c127-35e4-a78e-e6e7f455663c | -5.7539 | -51.73319 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| da5e4bdd-d231-3c92-a7db-f9351d7eab53 | -6.86318 | -55.58712 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 3f650267-228e-3751-ab32-039e8841ab85 | -2.96712 | -50.42854 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2d0c8eba-c2a2-3196-bb55-8126077dcc87 | -7.52178 | -47.33474 | 2026-09-13 00:05:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0974a787-fb49-39b4-9df2-34c181a61778 | -2.96591 | -50.41975 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 44fbdbae-ae9c-3149-98db-50d97209c0f7 | -6.16823 | -57.72131 | 2026-09-13 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| afbda126-b934-38cf-a38f-19ae485ed5bf | -6.71751 | -50.95594 | 2026-09-13 00:05:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2523199b-35ee-3c98-9c45-16ee5803ee2a | -2.95468 | -50.40342 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 77a8a5e7-7792-34fb-8d38-c46f36aa633a | -6.86102 | -55.57006 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| cf34f7bb-3535-3fee-b4da-4a20b571d143 | -6.0797 | -51.75975 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 222125c6-4a4f-3b29-96c1-6c482fd184a3 | -6.24732 | -51.70534 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ac56427e-7802-3ff1-9686-0ac88bdbefdf | -2.93586 | -50.39711 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 08ca3c4b-f734-37b7-b7b5-45d5c6405d60 | -6.67381 | -58.87061 | 2026-09-13 00:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 190a274b-5b16-37c7-89a9-13e560353b40 | -8.84909 | -50.71423 | 2026-09-13 00:05:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1db326c6-c181-3dea-b7cf-cb2a9f6f923a | -8.02074 | -54.85831 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3b6cfded-22c3-398d-b76a-61ed5ce34683 | -3.04752 | -51.27458 | 2026-09-13 00:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 78672484-070b-33b2-ad30-0a41ca2e7f78 | -3.79397 | -48.94514 | 2026-09-13 00:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a7a98133-521f-3045-81d7-77eb851e18c8 | -8.43973 | -46.03797 | 2026-09-13 00:05:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3091b223-8579-36b7-9a66-497003c51631 | -6.66298 | -58.87733 | 2026-09-13 00:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a8e5bd7d-3a68-3366-8f6b-f450ad91636a | -8.42767 | -46.02697 | 2026-09-13 00:05:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 517d474d-7aee-3872-be6e-aa8740640262 | -9.70944 | -54.36203 | 2026-09-13 00:05:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 7954b329-fc2e-3bea-b46e-d73b46f12cba | -3.21812 | -50.58669 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 91f2d1d9-d9c6-37f8-a31b-02994187b815 | -4.35199 | -54.77721 | 2026-09-13 00:05:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e3865a3f-0504-31d9-802f-813be48cd0ec | -3.04631 | -51.26577 | 2026-09-13 00:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f5ec7a87-05d8-3df1-bd8d-08ac9a03e70e | -5.54832 | -44.46473 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f6a7500c-8d12-306b-a081-e32ec8b0b1b4 | -9.13303 | -51.59465 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37a882de-14d3-3425-be32-33e3e14bf209 | -3.79265 | -48.93565 | 2026-09-13 00:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 2b6f99ae-6fc4-3951-b187-67e46a046799 | -2.67165 | -57.55095 | 2026-09-13 00:05:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| aa20a72c-891b-3460-af42-dfc1d7a0fd96 | -2.95711 | -50.42099 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4d9973bf-0635-381e-a35c-4cac95826285 | -6.17254 | -57.71572 | 2026-09-13 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e9f97f4b-a509-39dc-9098-a4b72f4185ef | -8.5791 | -54.57107 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8b191010-7f8d-3e4d-8063-b2e6ade904ff | -7.37049 | -45.36069 | 2026-09-13 00:05:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 595816d9-f300-3d4d-94d2-7c549130feab | -5.02844 | -49.99897 | 2026-09-13 00:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| c46736fc-f147-3ec5-98d4-99e4aa6254bd | -7.37224 | -45.35396 | 2026-09-13 00:05:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 9b354981-e0a4-3cd6-b243-a46284c20fe2 | -2.82505 | -51.34192 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b01ff390-560d-308c-922b-cb3969210bed | -7.60097 | -46.11945 | 2026-09-13 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bdf01c70-a438-33a0-a209-65716a4e74f8 | -3.39113 | -50.76428 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 783c7dfb-72e0-3342-a53a-1c2f6b8e8fc3 | -2.78336 | -51.36569 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0bc27c5b-500b-36d8-a500-76d7352b909c | -8.53755 | -54.69167 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 59cb0772-60b2-33cb-9b52-07fae87f9fda | -2.9647 | -50.41097 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2cf005f0-a1cc-33c1-8ae1-ead23272e4dd | -6.00793 | -44.26638 | 2026-09-13 00:05:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f472e4aa-cf11-37a3-a5c9-97df3ac915d4 | -6.50735 | -47.60487 | 2026-09-13 00:05:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 31675a4b-b894-309a-a0d3-d5c0db504639 | -2.82816 | -49.2256 | 2026-09-13 00:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dbdb1271-a439-3522-aed5-4480db634410 | -6.23822 | -51.70657 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5897f80f-7713-3eff-b349-405ee1bb3122 | -6.34723 | -49.4046 | 2026-09-13 00:05:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ca53198b-968c-34a8-8f83-390dd5551b4a | -2.54073 | -54.65606 | 2026-09-13 00:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| ffd01bce-ae59-346e-a3ab-1a82efc9645c | -7.37438 | -45.36802 | 2026-09-13 00:05:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| c1f5db7e-d765-3e10-8816-d373777412a3 | -7.36128 | -45.3555 | 2026-09-13 00:05:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d0d0dbe7-1314-3042-bd41-74ff8b20cd33 | -6.36551 | -54.91757 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f5591f4e-488f-3d7a-b716-6142287deed2 | -5.76665 | -45.09724 | 2026-09-13 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1d5afde8-d1ef-3d6b-850b-cdc804fba6b0 | -4.93176 | -45.83647 | 2026-09-13 00:05:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4bff135c-1bda-320e-b3b4-26aaac590a43 | -9.711 | -54.36821 | 2026-09-13 00:05:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1b375a74-24d3-3940-9ad6-cc2864e83e6d | -2.72214 | -57.64629 | 2026-09-13 00:05:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 1ca7f7bd-b6e6-3256-8f8f-a39813483186 | -1.22748 | -49.18521 | 2026-09-13 00:05:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ccb9d832-4d2f-39ef-a613-ff24250f0eff | -7.32899 | -49.77243 | 2026-09-13 00:05:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a82cc6f8-8d9b-3e59-8750-4ce209a14943 | -3.95649 | -47.61449 | 2026-09-13 00:05:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 55b917c3-f06f-31c3-adc6-5bed992d0eca | -8.32146 | -49.6816 | 2026-09-13 00:05:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fb16f35a-49d6-33ad-ab00-bbea0e1a2487 | -1.22883 | -49.19493 | 2026-09-13 00:05:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a4f9072c-fdc2-3f86-ba04-0fd81225fa42 | -5.20318 | -49.32988 | 2026-09-13 00:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bca9d87b-1842-3d48-958b-f24fb6cf9683 | -6.22656 | -51.6856 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| d46f6288-9af0-3b61-83ef-48f397c3df32 | -2.59092 | -54.71276 | 2026-09-13 00:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 768110d0-5481-311e-9d53-440d52e1aa31 | -7.37283 | -46.03899 | 2026-09-13 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 05b1f4d1-de47-310d-9534-3eda560c2b0e | -3.87391 | -51.18586 | 2026-09-13 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 6982da27-5003-39b1-9b85-c5ea3f2c507a | -4.13111 | -54.02006 | 2026-09-13 00:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d73b7cb5-b0ff-3abf-ab22-aac07a97c287 | -5.81789 | -53.80028 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| e6b054e3-e041-377b-8adf-da9223ed8d4f | -3.83104 | -51.89052 | 2026-09-13 00:05:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a9d1c23d-8d04-3899-9b31-209e48d53cc3 | -2.9559 | -50.41221 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ba317ab6-7103-3bfd-855a-c61f20534f0e | -2.1323 | -52.07434 | 2026-09-13 00:05:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aa4d424f-34c3-3181-a9b1-134b0b7f71b5 | -2.82946 | -49.23498 | 2026-09-13 00:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 8b262e75-d87f-3547-b355-32b43211f20a | -6.10593 | -55.68132 | 2026-09-13 00:05:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 548959d8-69de-380a-97b9-dd289bfa6c05 | -9.59066 | -55.14593 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5294adf2-5309-3316-a286-9db15e564ddc | -5.16949 | -49.35939 | 2026-09-13 00:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2ab27fd5-945f-34b0-a690-c29fc732b2a4 | -1.85153 | -50.96712 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e0eb93c0-a034-39b9-8b2f-ba9d6ea22129 | -1.2196 | -49.19624 | 2026-09-13 00:05:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 77deea93-bf8f-3226-ad89-178a4d85d579 | -3.29556 | -52.08549 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d19e5b7f-4469-3eb6-99bc-2099248b500f | -3.988 | -51.08266 | 2026-09-13 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e74d370a-1e34-36c6-b2e9-9544d4fa9d4d | -6.346 | -49.39569 | 2026-09-13 00:05:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c79535a7-448f-39d7-aa0f-239785792a7d | -9.5808 | -55.16551 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e2408080-31a8-3b6d-b40b-164699a33ea8 | -5.8195 | -53.81246 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| d07a5c17-5d72-3f0a-b459-c4c0a48d7f6c | -2.86636 | -49.63448 | 2026-09-13 00:05:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 787c8856-fce6-3d29-b6e8-04f2295ebe70 | -6.9579 | -59.7571 | 2026-09-13 00:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 0e814781-d973-3f34-8c5f-e53708382fd0 | -6.67858 | -58.87534 | 2026-09-13 00:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 279b3afd-0865-3c64-9616-bf87308caada | -4.12951 | -54.00826 | 2026-09-13 00:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 634d641b-bb2a-3c0f-b489-fd6c14bd5465 | -5.96641 | -47.20974 | 2026-09-13 00:05:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3f920a32-2655-3c68-8374-a9e1ec8c29b3 | -5.20443 | -49.3389 | 2026-09-13 00:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b6e28744-a630-38e6-b2df-1d6500443287 | -6.6775 | -58.90211 | 2026-09-13 00:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 2e7e2ca4-a37e-32c7-ae92-01dec675b281 | -6.74206 | -55.64348 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 5aa8ed55-6873-3ff4-a198-6b472f70a625 | -6.09797 | -55.67048 | 2026-09-13 00:05:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 0635a11a-73a2-307a-aa1e-c3fc8d2e15d9 | -6.50585 | -47.5945 | 2026-09-13 00:05:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| cb763f7c-e0f5-3d6f-b400-95abffbe15e9 | -3.87512 | -51.19471 | 2026-09-13 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 9f5755e0-7288-3209-9ca9-5a8b033bfa48 | -3.76521 | -50.45865 | 2026-09-13 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9aa55e8f-04dc-3ad2-952f-e9461023e976 | -2.94467 | -50.39588 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7e7b8904-6ad2-32fd-b37d-bcdba60bdf6d | -7.02007 | -44.62621 | 2026-09-13 00:05:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8ba41ea9-d606-3068-9d40-1bce12e68781 | -2.6848 | -57.54918 | 2026-09-13 00:05:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 31.5 |
| e535313d-923e-37e0-ba47-0502e9ec641f | -5.73567 | -53.48606 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3ca4f610-150b-357d-83db-39b5ebc712a1 | -9.72083 | -54.36071 | 2026-09-13 00:05:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6b634a40-60d2-33ef-99f2-8162c6b0fc22 | -8.53954 | -54.70716 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |


[Clique aqui para ver as próximas entradas](README5.md)
