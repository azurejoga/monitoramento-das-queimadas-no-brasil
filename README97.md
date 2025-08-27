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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b4adb8b-88ba-3f3c-b25e-21f04ac6a9ad | -11.9208 | -47.1375 | 2025-08-27 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| eae2030c-1bda-3a11-837b-6b74b070df7d | -12.7259 | -48.1846 | 2025-08-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| dc5a7e88-7a33-349b-9d59-b88896f33f12 | -10.2743 | -64.4907 | 2025-08-27 14:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 3aff1d00-4762-349a-b82d-9007377bed72 | -8.8842 | -60.7507 | 2025-08-27 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 183.9 |
| 244a9d89-a11a-3e57-9386-739c90dcab92 | -13.6291 | -48.2097 | 2025-08-27 14:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| d8bb5f3e-9919-3c11-8621-310cd2264b95 | -9.1004 | -49.605 | 2025-08-27 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 0097aef0-f2f8-39a0-b77e-06885a4c4c74 | -12.7067 | -48.1873 | 2025-08-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| c5f4efc8-0cc4-3257-a721-206b6eb9d9d5 | -11.3146 | -43.5008 | 2025-08-27 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 343.5 |
| fb4735b3-9b84-3e08-840f-88ba818a5bab | -13.4036 | -46.876 | 2025-08-27 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 2d621433-5261-3ec4-9947-6507ec5300a7 | -12.8036 | -48.1294 | 2025-08-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 4d4267c5-3039-3063-9350-847039c7c2fb | -15.6362 | -52.7393 | 2025-08-27 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e0707126-97b2-3818-8895-885aa5ef9032 | -11.8119 | -46.7932 | 2025-08-27 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| a56d9d13-5a9d-3030-aa10-a4bebd069b68 | -8.2707 | -45.1377 | 2025-08-27 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 335.7 |
| 60313015-edaa-31f7-acb3-b2331222dde3 | -8.271 | -45.1149 | 2025-08-27 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 6deb0063-00ca-35ab-b1e5-a93c816c71ce | -13.3843 | -46.879 | 2025-08-27 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 9ddfb43c-6f4d-3a90-94da-b70424ba5d0f | -12.7843 | -48.1321 | 2025-08-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ba598655-8450-3b9e-8693-3968ffd75997 | -8.9026 | -60.769 | 2025-08-27 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| fb4eb9d6-9917-392a-a208-a6af50062dfb | -5.663 | -45.136 | 2025-08-27 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 48cde22f-b257-3676-9d5f-341ed722920f | -12.804 | -48.1072 | 2025-08-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4fb29d04-dd8d-3a2d-8f16-caaeb6d9eb39 | -11.1583 | -44.7859 | 2025-08-27 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 13ba11ec-6e01-39b7-89af-1d19d4d26575 | -11.3338 | -43.4979 | 2025-08-27 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 315.7 |
| b8259295-800d-3678-bbd7-709bcc35855e | -20.013 | -46.4277 | 2025-08-27 14:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 97e56130-97d2-3d66-9cea-144e24589a2f | -9.0816 | -49.6068 | 2025-08-27 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| eade68e2-93da-3f4b-8a57-6b469007fcb2 | -13.4032 | -46.8987 | 2025-08-27 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 4f550078-1613-3548-a055-256aaf79ad30 | -8.4785 | -43.6624 | 2025-08-27 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| b4400526-0864-3ae8-aad0-b22322caf9a2 | -9.0821 | -49.5638 | 2025-08-27 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a001b99f-baba-3859-97df-e11c83018d8a | -11.5694 | -47.6081 | 2025-08-27 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| ee1d5c80-9605-3dfa-ad98-c63a81e0e16e | -9.418 | -48.2756 | 2025-08-27 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 76317071-e192-3d5d-889f-d8f8fd160a67 | -9.6574 | -64.9845 | 2025-08-27 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 85d62815-9cdb-39ad-a198-f18de9d5fd8c | -8.4593 | -43.6879 | 2025-08-27 14:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 339.5 |
| ac094adf-08bb-32fb-b122-82ddff7db489 | -12.7639 | -48.2014 | 2025-08-27 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 30a005cf-b6e7-38bb-a9cb-c1327087bb3c | -15.6362 | -52.7393 | 2025-08-27 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9e9166cf-af26-305a-ba1e-831a63819af0 | -8.9567 | -64.1272 | 2025-08-27 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 229d8256-84a8-39d2-9434-e2c841de90c9 | -9.0821 | -49.5638 | 2025-08-27 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 632febf0-a699-3d33-a9f5-7784b18d8f7b | -10.2742 | -64.5096 | 2025-08-27 14:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 7f6a8ed1-ff46-3944-8f11-6ffb26edc6cf | -6.1785 | -44.0226 | 2025-08-27 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| db4c1c5a-afd4-3b37-83b5-b6e517e20ac1 | -10.6628 | -47.1881 | 2025-08-27 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 103a236c-ff9b-3f44-a482-0df5492f668d | -11.1587 | -44.7627 | 2025-08-27 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| e25b59f0-a019-3584-9870-31194e2d7242 | -15.6168 | -52.742 | 2025-08-27 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 542c3de6-5668-3393-85f6-54635eb40c64 | -13.6097 | -48.2126 | 2025-08-27 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 955da01d-8f6d-3eea-9081-3410eaa3f07b | -6.6759 | -58.846 | 2025-08-27 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 905fcb5d-b240-342d-81af-1821baa55de4 | -13.067 | -46.3382 | 2025-08-27 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 9929bf19-816d-3462-9532-33c4470ed371 | -9.5705 | -48.1505 | 2025-08-27 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| adebdbdd-21a8-36db-ae60-b5412f803b95 | -12.804 | -48.1072 | 2025-08-27 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| c1d49c79-e62f-34d0-9994-d9fceaf1acac | -9.6574 | -64.9845 | 2025-08-27 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 1dabe944-0b15-3265-8dc0-3d5ebcb1d891 | -10.6632 | -47.1658 | 2025-08-27 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| afa32ea0-57a6-317d-a1a1-38e3fae0be30 | -7.1106 | -44.6099 | 2025-08-27 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 54e658d2-8c25-35ab-8821-40e8d7884d9b | -12.7263 | -48.1624 | 2025-08-27 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f345f021-4231-381f-bd7d-758bc9c658f1 | -14.2954 | -53.0631 | 2025-08-27 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 390e807f-f121-34cf-9822-d6cb0e0649a8 | -8.4596 | -43.6645 | 2025-08-27 14:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 234.5 |
| c27ba7b1-8a54-3d30-b5d7-8490f6a25ed9 | -11.3338 | -43.4979 | 2025-08-27 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 244.9 |
| 48fd3a4c-eda4-3ddd-a45d-23e25d8ae76b | -9.4062 | -60.5326 | 2025-08-27 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 7339ae51-072a-3564-85be-470e8a9d6b68 | -12.8036 | -48.1294 | 2025-08-27 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 32fdff22-28f2-397e-91a7-0e3a2f789215 | -6.62 | -53.3373 | 2025-08-27 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| f7c52201-1577-3082-8d3c-614faa2e25cb | -8.459 | -43.7113 | 2025-08-27 14:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 9b4539ca-610c-367d-90aa-1152fa620238 | -9.0816 | -49.6068 | 2025-08-27 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 36a70042-4db8-342e-acaa-d7a4bba66d76 | -7.6411 | -42.6955 | 2025-08-27 14:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 133.6 |
| 3ace7d22-31a7-3191-beb3-ba885dcabfa9 | -17.8471 | -47.7428 | 2025-08-27 14:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 2a090d32-ae88-3d99-9aaa-8fd1d9a06398 | -9.8286 | -64.2824 | 2025-08-27 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a56c865d-b03d-3a77-9abf-601e7497c753 | -13.3843 | -46.879 | 2025-08-27 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 0dd0a784-6924-3dd7-b98e-1f247767c1fa | -12.7643 | -48.1792 | 2025-08-27 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ee8cf403-e724-36ce-843b-a726f46fd665 | -7.7741 | -51.0512 | 2025-08-27 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| bd524b87-b1b5-3696-8821-e12973e0b9b0 | -12.784 | -48.1543 | 2025-08-27 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f7fec5a0-60d8-38de-ac0a-93e6062f6c46 | -7.6414 | -42.6718 | 2025-08-27 14:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 158.8 |
| e021f544-a6e7-3cc0-b02c-8d94673b9dd9 | -11.1583 | -44.7859 | 2025-08-27 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 296.4 |
| 71ac540e-0b05-3b2d-b16d-9557a62987c6 | -6.1783 | -44.0457 | 2025-08-27 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 255e2e86-3c62-3b21-987b-3e747d662b50 | -11.1579 | -44.8091 | 2025-08-27 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e54b56c7-1b53-3d9d-98d6-9eb37189725e | -11.7966 | -51.4169 | 2025-08-27 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 19c3697a-5249-3d00-84c1-d62021ec22e1 | -6.4357 | -44.5535 | 2025-08-27 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 403a566b-c3be-3b3e-9d87-a948f2f1bcc5 | -9.0586 | -66.07 | 2025-08-27 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fc9861f2-3e05-3aee-9f1f-aa345167480b | -9.4064 | -60.5133 | 2025-08-27 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| b2691642-38af-3881-bfaa-63d6cf6b3475 | -15.0756 | -48.5181 | 2025-08-27 14:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 111.4 |
| bd9ad863-febc-31e2-973b-13e1f2b50750 | -7.5673 | -47.4851 | 2025-08-27 14:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 2904772d-2e48-30bd-92c2-bb351c11b716 | -13.4036 | -46.876 | 2025-08-27 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| cd6a3b8f-c802-37df-9e50-6b90747826e1 | -13.6291 | -48.2097 | 2025-08-27 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 8d36c9e1-897c-3eee-ae8b-a6cbf41a8989 | -8.271 | -45.1149 | 2025-08-27 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 63af60c3-b11e-323d-bc68-4f8fa5e2213b | -9.0819 | -49.5853 | 2025-08-27 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 33b18b48-f63e-30b3-907c-f2695cd5ff58 | -9.9352 | -46.38 | 2025-08-27 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 30a9aebb-c368-3bc2-9c63-b034f2579c2f | -13.0674 | -46.3153 | 2025-08-27 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| f94d29cf-dbac-3d07-a74f-e426c42dc4be | -11.3481 | -63.2672 | 2025-08-27 14:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 291739af-829c-314e-aea4-ad42e71d8916 | -7.7359 | -51.1379 | 2025-08-27 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a9208556-35cd-3441-a36e-59462ea40396 | -7.4414 | -42.0501 | 2025-08-27 14:20:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 105bb38b-ad98-3f66-b73d-aec4b051c6bb | -6.4355 | -44.5764 | 2025-08-27 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 193.3 |
| d358a130-9090-3377-9554-207c2cf0922a | -8.1398 | -45.0599 | 2025-08-27 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 229.0 |
| fac6066f-226c-363e-9c20-dcaef761b098 | -9.1715 | -59.5599 | 2025-08-27 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4154d3be-a205-36da-817e-bce64feda373 | -7.6603 | -42.6698 | 2025-08-27 14:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 71950297-8dfe-3c28-b512-ae79ec513873 | -15.6171 | -52.7207 | 2025-08-27 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 8b98bfc5-6887-3e33-9eea-cab0647f8b1f | -6.4353 | -44.5993 | 2025-08-27 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 0e03ba46-4fd2-35e8-b01c-43ad547befe6 | -11.3146 | -43.5008 | 2025-08-27 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 7c037384-1b2a-34a3-879c-25bbe24294fe | -13.4032 | -46.8987 | 2025-08-27 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b5b1104c-418b-3546-85f6-d6358d2321f5 | -8.1587 | -45.0579 | 2025-08-27 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.5 |
| f6bda803-1ad5-3840-8052-ebe2d516224d | -12.7843 | -48.1321 | 2025-08-27 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 7c467bbd-2f7d-3269-b65c-56b4ef694e56 | -7.3383 | -46.1073 | 2025-08-27 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 53212c6c-caf4-3c49-a2bf-8e75df7a0c10 | -5.7887 | -43.6134 | 2025-08-27 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 22161c15-66b4-3ec5-854c-4daefd0592c5 | -10.2557 | -64.4915 | 2025-08-27 14:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2f51bf83-6e3c-30aa-824a-7e4c5996b06f | -12.7259 | -48.1846 | 2025-08-27 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 32c1db00-c410-3a43-88ee-8bbb61dddcdb | -9.2092 | -59.4997 | 2025-08-27 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 67357971-f9b7-369a-b301-b3607988b919 | -10.2743 | -64.4907 | 2025-08-27 14:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 719751d2-6a79-318f-aefc-4ee6c286b721 | -12.7067 | -48.1873 | 2025-08-27 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 3749bf88-8b83-3c93-a5b7-1625161eb83a | -9.418 | -48.2756 | 2025-08-27 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |


[Clique aqui para ver as próximas entradas](README98.md)
