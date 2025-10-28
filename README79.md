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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 937befa6-03e2-32ab-805e-0ceb8a6c25ef | -7.25891 | -44.99749 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa65ce69-e500-399b-90bf-6c5e9146be2f | -7.26912 | -45.01238 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c679c22-8fff-3668-b06f-ab926f5aa05d | -8.2029 | -46.93648 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff3727d6-356c-3df9-871c-d6b433ee0347 | -13.31956 | -48.34234 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8262d542-6754-3ce3-8d83-8c105e24de48 | -9.54442 | -46.95622 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 275e1cf1-10c5-3149-b1ab-31cdad48f97b | -7.89452 | -45.69636 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34fb5b8b-2f88-3cb3-b50c-3425b2c84d42 | -10.23505 | -52.1492 | 2025-10-28 05:04:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fac419d-d676-3cc1-8fa2-21db2f405e2c | -7.96066 | -45.46118 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f98dcbe-e1b1-3ff2-a2bf-6056b2a1d66d | -8.70031 | -50.80569 | 2025-10-28 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d8c78fe-ddcd-35e8-9876-8c640aae5f7c | -9.27581 | -45.57716 | 2025-10-28 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7be04c23-54c8-3c90-8647-29294f552fcc | -9.55715 | -46.97279 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5b3eb5c-0fa8-3b45-a021-7fb152b1abcc | -5.89864 | -53.8556 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8111c1fe-a777-38d4-892e-39c350a487c8 | -7.5093 | -46.2837 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31eb11c3-7b29-37bd-ac16-c09c70fd02b7 | -7.44999 | -49.40779 | 2025-10-28 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e3c9eed1-be3f-3e97-b514-496b4c313bb2 | -7.81273 | -46.45193 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6781d6e5-12b3-3817-9cfe-b5c5cdb66b32 | -7.95855 | -45.52255 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5271e08-509d-3525-875c-df9df0cca60e | -10.30216 | -47.17413 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc7cbd00-b9f3-3b2f-90be-b9a8378d2466 | -9.55841 | -46.97642 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16994b75-3081-34fb-bfed-6d8f2b353b15 | -7.64835 | -45.24183 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9171fed6-dd09-3ac2-b5ab-a248b6895d52 | -7.81393 | -46.43673 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 228498fc-3c9b-3ba8-a305-578f7d0390db | -11.07418 | -48.33203 | 2025-10-28 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa005eb9-7659-3aa9-a01d-e6210a3bb90e | -7.77611 | -45.38283 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 791e687b-06ec-340b-8678-a192784c7254 | -11.73112 | -49.33184 | 2025-10-28 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4f4cb0d-a4a5-3137-8e90-619594abdcdb | -7.95493 | -45.50481 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4fa1d0b-8ec1-3e20-9f78-82aca71787ab | -11.21676 | -49.76778 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86d7a31a-206b-3f12-a68a-12eeb6fec48e | -8.70972 | -47.97887 | 2025-10-28 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e2dc083-4352-318d-9c2b-94e58139387c | -8.16324 | -46.99796 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcfcf1ea-a1ce-36a0-bfd6-eb8ebb7ca91a | -11.04854 | -49.9064 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62aa2056-5fe8-3d3e-b082-5c28f88af2c2 | -11.74482 | -50.21917 | 2025-10-28 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b945f9c2-d71b-3370-8a24-72f70184ee04 | -10.9285 | -50.25708 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78c14bd6-7165-36fa-a64b-c7c56f148b57 | -7.97323 | -46.72797 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e8818b6-a207-3784-99e7-3f3f16c9b26f | -7.99905 | -46.1925 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97d91963-0ba1-33dc-a411-07082ebe6085 | -10.93958 | -47.62024 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3f6726a-37b7-3636-aaa7-287b4c605ecd | -7.49404 | -47.03521 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64626581-d830-308c-a3ab-4892df7432ec | -10.93555 | -48.0253 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f800fce-c3ca-30e7-b81e-bc9657c0a2c2 | -10.79617 | -49.6651 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68bb6468-de6a-324a-b41f-9404ff64d194 | -10.93029 | -48.02552 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c3e953a-0637-30cf-b448-7f95180fb3a8 | -6.63672 | -47.20122 | 2025-10-28 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cfbf45b-945b-3fa0-afe7-5cb36659b9e2 | -7.95166 | -45.52974 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e87b5c70-4c73-3f77-adc7-8161f85619f0 | -10.58692 | -49.79897 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3b85ebdf-9398-35a4-945d-ebf8ba00414a | -7.67477 | -47.42186 | 2025-10-28 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21f05f8e-6203-33d6-a2c5-3c4ef9c195a4 | -12.98127 | -47.92753 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c43b5dc-3d53-3910-87d2-ee82276a0ad2 | -9.95633 | -47.11638 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d21067e-affb-351b-b47f-f85081b87248 | -10.9235 | -50.26083 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 230d40bf-34ad-3b17-9563-2a195984d792 | -9.89177 | -44.9109 | 2025-10-28 05:04:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2d6c4f6-f8df-38cd-9f3d-95b777b691fd | -7.49359 | -47.03839 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07b99b98-e1ac-3521-a580-4fbd52cd417f | -13.63002 | -47.03424 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7d82c298-7445-3012-a61f-c3e18cf8186b | -6.84667 | -50.11585 | 2025-10-28 05:04:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80aa59ae-81f1-3f6a-8b5d-e2158536530b | -9.14858 | -51.30077 | 2025-10-28 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f20b058a-ed43-38c3-8bd1-16fcc27a9ef1 | -10.94884 | -50.27333 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7607fa1d-cd3a-3428-9879-c85cfdc5df00 | -13.25862 | -47.96281 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47993bf8-375c-39b3-b744-fa9cdb65d2e8 | -7.30636 | -47.1958 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 893c8064-0ecd-33aa-98a0-77eb33120ffc | -7.85388 | -46.39513 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64abe5d5-7973-32b4-ab63-099c23ce7c54 | -9.96264 | -47.09417 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c775d3c-0f43-31c9-81d9-696741ddafe8 | -11.79995 | -52.50343 | 2025-10-28 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a93aa11d-c690-3640-978c-23204c7ce133 | -7.51581 | -46.2774 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f46f2bf-d3eb-3724-9924-f3bbbdb6ba7f | -7.81787 | -45.38381 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a49832bb-6757-3b22-93b8-92e0041aa56f | -10.92176 | -50.27396 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dabd78b2-75bb-33e1-9a2b-b1f38355dc4a | -10.68808 | -48.02521 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a54fce7f-9b12-32df-9dfc-151b478750a0 | -7.81638 | -46.46644 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a745a419-603c-3c56-8928-56a6f17d0cae | -7.40453 | -47.77513 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cc7ee4a-cb19-3af2-8da3-80b34907291b | -10.22392 | -49.8468 | 2025-10-28 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1db7d61-8573-33c8-bd9a-fdd2e39b09da | -10.5861 | -49.77045 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 609ad096-0c11-3999-b7e9-d26bef6a2389 | -7.83083 | -46.39982 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c74afcb-047f-32bd-bd88-f19d38703031 | -9.22431 | -48.60197 | 2025-10-28 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b450ed56-bd1f-3624-82e9-67b363564586 | -7.07089 | -44.94955 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 98dc6c6a-ee42-3174-9e37-4adbadee90d0 | -8.19159 | -44.44801 | 2025-10-28 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c88d6f3c-8cc7-31f4-9c04-88edfb06b1e0 | -9.05659 | -46.94439 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79a3d0b7-edbd-3877-8cfb-7d7ed3e0ac4f | -7.51564 | -46.2769 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 183eb430-8c23-34eb-8d18-8bbd4378e972 | -10.55995 | -49.78408 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c543ba75-e2d9-37de-a97e-fe42fe46d1af | -7.46623 | -47.15739 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1eb96fd-c240-3e44-b472-10db0b99bd48 | -7.81732 | -45.38787 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e895143c-ca98-340e-886e-bfdd6e62e1a9 | -6.63366 | -47.20229 | 2025-10-28 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 230dcd46-10f1-3200-bad2-22bc660dfeaa | -9.45342 | -46.86677 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24b52898-2419-3f0f-8bf0-6a090c45cc94 | -7.84087 | -46.40854 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a0c4f00-fc2a-318b-b3af-830a7751671d | -10.76053 | -44.7571 | 2025-10-28 05:04:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6da78879-c21a-3dda-8407-0ca1be68308b | -7.81465 | -46.43739 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 337b22a5-f9b6-37a7-b1e8-3ffef07dfa99 | -7.94952 | -45.54608 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6cdf5840-7377-3cb6-a39d-1038e944154e | -7.98181 | -46.7461 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e315f83-7974-3e9c-9821-d19097e289b0 | -7.93834 | -45.49885 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9dd04475-1269-319a-a565-46a968bca1c9 | -9.29146 | -45.21901 | 2025-10-28 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1e11f3a-3ba7-30b2-a078-7c6e4298e3b6 | -9.29084 | -45.22385 | 2025-10-28 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d296935-18e1-3135-ac90-acd608d5cdd2 | -9.88801 | -44.89049 | 2025-10-28 05:04:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ec42793-e087-309c-b9a9-a3ee8990be07 | -11.13706 | -47.04957 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2923d290-63ab-37e3-a0ad-3818a32574da | -13.61273 | -47.03365 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12e74ef7-25ef-3e35-be8b-de2b009b68de | -8.09651 | -45.68466 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1513663-68a6-3752-ade7-dd79ff8bbd1c | -9.91071 | -47.68299 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d95f5bbf-caaf-3190-8bd6-72f34a0a0613 | -13.63561 | -47.03596 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7581bab4-609d-3950-925a-1d1f762d1d10 | -9.46134 | -47.72795 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c131170b-9b4f-3f26-90e2-dc3266a7c6af | -13.39385 | -48.51793 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53249a83-f866-360f-83a0-19b49a4d13c0 | -9.17328 | -44.57915 | 2025-10-28 05:04:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 562cb304-9bf9-3c0a-9a8a-0160dfcc6f60 | -7.81046 | -46.4615 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c70720b-7c62-3ee7-bb86-a3b770b2057c | -10.58238 | -49.79834 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 344bf0ed-c783-348e-8cc3-c6e20702e5d8 | -10.56255 | -49.79862 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e9f2dca-b5f1-3852-a145-bd775612b6a1 | -8.0771 | -45.95596 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e2f82e9-247a-3b13-9ab5-a3ca93b5d37e | -7.10282 | -47.27031 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0da9812-c728-320f-af9f-db998519c951 | -6.58224 | -44.63034 | 2025-10-28 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9728884d-5217-3a92-ba20-22248c362408 | -10.56774 | -49.76147 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6d6f2d9-89d7-3408-8b4e-04a828ba2927 | -9.97765 | -47.16446 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2709ad59-8a93-3dd2-9d51-4d25875a721a | -8.62785 | -44.79528 | 2025-10-28 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README80.md)
