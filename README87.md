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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5281a00-0fc8-3b2d-b244-1b8b09d5545d | -9.73219 | -64.91031 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 12fd7fc2-daf5-30f9-9186-7331d5d8d5bc | -9.22076 | -71.83894 | 2025-08-29 06:22:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47f071e1-97f0-33e7-8ab8-4f2325ba9577 | -8.93198 | -71.27199 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b547df75-e1d2-3257-a468-6cb1b1346f5e | -9.12618 | -65.78931 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c64e83e-61b9-3f0a-9cd8-f0331ed6f4e7 | -8.85817 | -68.5076 | 2025-08-29 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a978b63f-c804-397c-9a82-396aa0372f46 | -9.11233 | -65.7644 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 08772d09-f0ad-3b86-8a02-a451a48b6b96 | -9.78732 | -64.2424 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5be3dc24-9c40-3d60-8087-47b741dd70d6 | -8.8588 | -68.50284 | 2025-08-29 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fd4af1e-ec80-3d3f-87ff-5c3328568fb0 | -8.64948 | -69.57125 | 2025-08-29 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 655df1e6-94d1-3442-9e0c-7cc861ed6183 | -8.95269 | -65.95667 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a90409bc-a042-3833-95a1-76513066f40a | -9.78554 | -64.25689 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc60fce7-defd-30dd-bd69-040ddef499f1 | -9.18734 | -65.79798 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 742e1893-6f47-3854-9160-b8113aa455d8 | -9.77994 | -64.25121 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 44f657ad-f5cf-3c82-bae1-0455f75d08e4 | -9.11967 | -65.79598 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46e6d64a-4d99-37aa-bcfc-483ad6c85e4d | -9.10446 | -65.73676 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8104d60-90f5-35d7-81f2-40833de26b8b | -9.12253 | -65.77343 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7230cace-4a0b-39cc-a533-117c0385a1c8 | -9.12475 | -65.80053 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eca5ca1-86b6-39ca-babe-442f5a564a0c | -9.11043 | -65.77951 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ad816e7-3155-365e-ba91-d62f4e15dc92 | -9.10903 | -65.79062 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 037fd9dc-3c5f-3223-ad48-f91dd8eb4c47 | -9.54735 | -65.69595 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a268f90-31a8-34a0-99cd-59f3c989dcd5 | -9.11365 | -65.79884 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a0ec7af-328a-3f9c-951f-0d6c98216e51 | -9.80703 | -67.84319 | 2025-08-29 06:22:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9b1a8755-b8b8-32d1-8b1f-fa4b3fb9de23 | -9.28578 | -68.25826 | 2025-08-29 06:22:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33a7872e-7d1d-390a-87f6-da5d21919b06 | -8.65375 | -69.57189 | 2025-08-29 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9378a722-b81e-38b9-8512-ca0267bb2d29 | -8.53856 | -70.74644 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8ad1635d-ede7-3b12-b9e5-c461b3844ecb | -8.92809 | -69.43774 | 2025-08-29 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50084319-a0c0-3d3d-bb37-87dcb28e062c | -9.76696 | -64.25439 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 277b37c0-c02d-304e-82bb-011c866b4b5d | -8.58497 | -70.29005 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08db0565-b49c-3824-9337-50b9fa6871c0 | -9.76637 | -64.25924 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| abbd73b0-eb79-3dc6-8ec0-388e81306198 | -9.67086 | -65.03272 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaf8d88c-e40d-31ee-b12a-f39bde66b6d5 | -9.12205 | -65.77723 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 736c0727-ba19-3099-a490-3fd5c7f3ff3b | -8.95675 | -65.96816 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76358e6e-c2cd-3ceb-a975-c624c617267a | -9.11263 | -65.77008 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 58add01e-ee2a-3371-821e-bfa2fa3f05fe | -9.72849 | -64.90921 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d12e10b1-0d17-39ed-86c3-f01b0dca9d3c | -9.11458 | -65.79147 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1189b31e-aa0d-3fc3-a4d0-9390d56a2ecc | -12.43765 | -63.91621 | 2025-08-29 06:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7f55c9fb-e1bc-3a2c-b43a-929566275fb3 | -7.83797 | -71.83112 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab97889-9e5c-34df-86bf-8d1102a619a2 | -7.82602 | -71.93906 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30432928-74f2-3fa0-ba59-232c957c9f28 | -8.95024 | -67.71404 | 2025-08-29 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35ee6cb7-5111-3cde-b01c-46681698a311 | -9.72626 | -64.90942 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 77c9f8a6-e9d4-3018-8f00-b2d5ea9e9a59 | -9.1081 | -65.798 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f544306-3ac7-3e5b-a3a2-da1974163dfb | -8.77723 | -71.30385 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43269ebb-3b6a-3cfe-bc56-f02ea43c4387 | -9.11003 | -65.7376 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8888b4b-212b-3aff-bc9d-6c22c2f33274 | -8.58474 | -70.118 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2f9ba5c-e34a-300e-8ade-b61ccbec64d1 | -9.17164 | -65.78811 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c1bd239-9006-3368-ae4f-47fa072e433d | -9.77435 | -64.24551 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 32cf478c-7ade-33c9-a054-5292e6c00716 | -9.11016 | -65.78865 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 987fa9e1-c978-3ae3-9221-0a1c1d2ef2c4 | -8.44381 | -70.14326 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2493a282-6cb0-3d28-9276-ef60b1ea0ed5 | -9.67139 | -65.02847 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12662dab-4ecd-3ba8-a67c-2054cfb0dd3c | -9.18179 | -65.79714 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98e94275-dea1-34f4-960b-ee9ec93d93b0 | -9.11695 | -65.77274 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 38868ae8-840f-3ee2-8e41-765575c97a76 | -9.12301 | -65.76965 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6658c2ef-c449-3827-a9f5-9bd7c5eff43e | -9.11412 | -65.79514 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb351539-49fd-3bb7-b5c2-afc4ff649b37 | -9.53862 | -65.69279 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 679f242d-6102-32b3-828a-b82119cd5c02 | -9.10547 | -65.7386 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aef13cf9-7b27-318f-9252-5e7ea3b734db | -9.53611 | -65.69426 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f07e066f-5464-34a8-b77b-2dcc9a966f04 | -7.8544 | -71.84685 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8617c270-543f-3ced-985d-dd9624996aff | -9.1091 | -65.74503 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 226c172b-ab6d-31d6-9a4a-3ba33a956d1a | -9.77875 | -64.2609 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 54609f0a-300a-3907-825e-452a052fb619 | -8.77171 | -70.57804 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc4310f7-221e-3510-b1d8-68aca45398b6 | -9.11513 | -65.74218 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b9c90ee-a831-33b0-9a2c-2a6d5cec0b8d | -8.44791 | -70.14386 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3eee9bd6-c145-3d47-8150-512aadeb2e8f | -8.95175 | -65.96376 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf329398-dd52-322d-8fe4-d6b32bb4be94 | -11.08946 | -65.15724 | 2025-08-29 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bfc1188-8977-3b3b-bdd8-8ba21ab9ccf3 | -9.11315 | -65.76624 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e7ac7f56-3b09-387b-8133-d3f7283e9004 | -9.10857 | -65.79428 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 059119fd-7fc0-3aca-a2d0-c6644441d694 | -8.3568 | -71.18913 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 609f470d-39b0-397e-90be-665d660c2614 | -9.77935 | -64.25606 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 65cba45b-a554-3c50-ab7c-d5da033b9d92 | -9.79986 | -67.84399 | 2025-08-29 06:22:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5b5b3adc-3faf-3c8c-a1d9-10b055bdf7ad | -9.1109 | -65.77579 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cec70a18-f825-364c-b050-bf65613c7b34 | -9.16559 | -65.7911 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ceb6a45-c86a-38f4-8ca0-89a223b468d7 | -8.95913 | -65.95026 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43cbaf3f-d0d5-3a5a-a106-98f3281c1086 | -9.15543 | -65.78204 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 702021a9-f834-37f8-a27a-82d3b97da450 | -8.39546 | -70.76488 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72208d41-a8ef-3424-8d7e-8bc857c8a31b | -11.08998 | -65.15276 | 2025-08-29 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73a2acf7-8a57-3059-b233-bd5c9b1ec164 | -9.1257 | -65.79306 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b92dcdd-bf1e-329c-a1a2-7f3382485b75 | -9.80215 | -67.84248 | 2025-08-29 06:22:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e6e81c91-5eb8-37e3-be8d-3a2f96d9c21c | -9.10629 | -65.76744 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ca256bc-56ae-3718-9913-e7d84fce2af8 | -8.95808 | -65.9645 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f1815cd-365d-3c76-ba23-f9af9ff71967 | -9.13684 | -65.79449 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 919efad1-b123-3c92-8d23-b92b8610eda6 | -9.78673 | -64.24726 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f23faa7b-3299-3801-a817-c6f366baf731 | -8.94851 | -67.71412 | 2025-08-29 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56b66423-1bfe-36ef-89cb-ad2ae4e612e8 | -9.08826 | -65.73991 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96d47ee8-f557-3714-a2c0-0d9c40b146b2 | -9.12157 | -65.78104 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3faff35-03ae-3296-a160-a016d656342b | -12.43704 | -63.92183 | 2025-08-29 06:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 452b1f49-bc51-3786-bb2a-8ed0d6470a22 | -9.77256 | -64.26009 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 66bcb7bb-62cf-352e-a680-c324dcc199ea | -9.08876 | -65.73618 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9072d096-a57b-39a2-ba43-3621120beed1 | -9.8014 | -67.84794 | 2025-08-29 06:22:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d3bf4085-1ac2-38cf-9308-53e43745f75d | -9.13514 | -65.29227 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8aa7e2e-4594-3932-b764-ad889407b6d8 | -9.13587 | -65.80206 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 93b85023-0e15-3f99-afc6-a8bf8bd30205 | -8.09644 | -71.24703 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cab59102-fe3e-3518-ae45-8294a218016b | -9.54374 | -65.69746 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d89cd3c6-7f1d-3582-baf9-d855fd8cc162 | -9.5422 | -65.6913 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0bc6ced-5389-3b62-8e55-0a0499af8264 | -9.80475 | -67.84473 | 2025-08-29 06:22:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a278abe3-db71-3761-a71f-821e07106068 | -8.95771 | -65.96094 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d13d9ef-f4a7-3b18-a6d8-372513e70fdd | -9.12992 | -65.28742 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5134d547-6285-3069-a4d4-461ad358a934 | -8.95364 | -65.94952 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f28339db-2c28-3388-bc69-966cb4aecd34 | -9.54474 | -65.68983 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7becc9f-671b-3f2e-9d47-0ce7db02181e | -8.94767 | -65.95232 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53f9ea25-5a4a-38d6-90c2-ce93b65738d9 | -9.67621 | -64.9898 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README88.md)
