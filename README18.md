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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28d16216-2662-3be8-9bc2-0fff8fc71fa5 | -10.05268 | -59.3644 | 2025-07-04 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b681f17c-39ed-380c-bfe2-9767aa8935bd | -11.20131 | -49.00016 | 2025-07-04 04:40:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb4d8d6a-db03-39f4-9ac0-1bdc99464cb8 | -11.91986 | -45.39598 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ea32811-42be-39b0-9dd6-4de5a20d86c4 | -10.2624 | -48.14895 | 2025-07-04 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c7c3122-b326-3942-86a1-851487c1a3e7 | -11.9322 | -45.39776 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8cc7b21-8d10-338d-9145-be1589932862 | -12.42283 | -43.72155 | 2025-07-04 04:40:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fea81e85-c3c8-3249-a31f-552f4309606c | -9.34017 | -58.84895 | 2025-07-04 04:40:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54da5767-3d67-3c89-b1cc-536564e12f3d | -9.62791 | -61.46703 | 2025-07-04 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5fc1e5b-d832-33a5-9994-f3d1b345eb07 | -10.38644 | -49.9223 | 2025-07-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f24379f-7dba-3748-8509-ea0965bf5e63 | -9.63002 | -61.46487 | 2025-07-04 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d78cf10f-01fc-3868-a420-d7663915fa70 | -11.91526 | -45.39892 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c900dd0e-9571-357f-afd5-2ecdc3d28561 | -15.17332 | -42.37899 | 2025-07-04 04:40:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9803faf7-8811-3024-afa7-68e442d8aec0 | -14.47878 | -46.35865 | 2025-07-04 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c59d3de2-e006-32a6-a689-ddfe852ab5e0 | -12.42684 | -43.72708 | 2025-07-04 04:40:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64ce76bd-ee9d-396d-bd6c-cafe87759777 | -13.39626 | -47.80345 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8727fdb-d8e1-3c06-bb3b-1dcb427a9320 | -10.23124 | -56.7682 | 2025-07-04 04:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2aa28ba-f193-3462-b860-6f87985a1d3b | -13.23968 | -48.03569 | 2025-07-04 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8089b4f2-1358-34c9-94d8-e52b1401595a | -11.53815 | -43.24666 | 2025-07-04 04:40:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6073f6f-6de5-3653-8a0f-9405a5cd374d | -17.92198 | -45.55766 | 2025-07-04 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de9c2aee-0e43-3e9e-ab0d-3fa5b418ab5a | -11.91682 | -45.38766 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fe882da5-cfe5-3ca0-9f60-d9a649674ae7 | -15.17372 | -42.37555 | 2025-07-04 04:40:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5f9c334f-ff6b-38a9-a5ee-4467da6da11f | -13.4503 | -47.81806 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9995fe3a-4786-33a4-9b06-889d210aa26d | -9.24532 | -58.74606 | 2025-07-04 04:40:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1fa4519-59bf-3ed4-880e-7326789e9355 | -15.98351 | -43.61217 | 2025-07-04 04:40:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2364d4fb-e430-3186-9610-503fdc1cb62d | -10.2595 | -48.15286 | 2025-07-04 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ee25e07-5518-3130-93a8-bb655f74c9ed | -11.92966 | -45.38592 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7d41bc6-c839-3eec-965b-df6513afa9b3 | -9.62875 | -61.46254 | 2025-07-04 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28b37eb2-5cee-3abd-93b1-56893011d5e6 | -10.70738 | -49.67008 | 2025-07-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76d0d4e8-f2cd-39d5-9b55-692c4faee25d | -15.57021 | -47.85765 | 2025-07-04 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c096dc9a-30e3-3469-8aaf-432cff12744e | -10.89002 | -56.45291 | 2025-07-04 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01ac7767-4621-3ed6-b968-ce15355809f1 | -10.05327 | -59.36124 | 2025-07-04 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23653e04-2b17-3efc-9626-e5d9bed32296 | -15.07854 | -48.94403 | 2025-07-04 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3199de0-dd47-3975-a9f6-1fb13a3bb3a0 | -11.92292 | -45.4041 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08477716-cbd6-37a2-bcfc-3e50695b1189 | -12.17041 | -56.54189 | 2025-07-04 04:40:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 65bff798-cca2-31a5-9e85-2ca941fe6ca1 | -14.88336 | -48.35457 | 2025-07-04 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5c1bec2-c796-34f8-bc31-ce060d6fcb68 | -18.0399 | -46.05106 | 2025-07-04 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b12543b-0572-3e17-b74a-50a2df129de2 | -11.91841 | -45.37627 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ebd7f7c-6fa4-30d8-9c2d-6c23c6dc7b9c | -9.52083 | -63.575 | 2025-07-04 04:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c317fd9c-54f4-300d-87e4-3a618ea244f8 | -10.23199 | -56.7639 | 2025-07-04 04:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 848fd6d1-31c4-391a-bf4c-c426835e5fcc | -14.60555 | -48.24471 | 2025-07-04 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36d19782-902a-34f4-b133-9c045e3be9a3 | -17.65195 | -46.83069 | 2025-07-04 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49ae111f-1513-34fc-a15c-572ce88b1cb2 | -15.02391 | -49.24378 | 2025-07-04 04:40:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24e5bea9-6272-3fc7-ab45-9d5ca7e0adc5 | -11.92703 | -45.40472 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed9cb0fb-c6f9-37b2-8733-54a7ff5d2271 | -10.55932 | -49.13005 | 2025-07-04 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 56bbc74f-7caa-3d8c-99ef-b123f63cd0dd | -15.55207 | -55.24554 | 2025-07-04 04:40:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c97ca88-3649-30f2-bbfb-dbd3129b8dae | -12.16624 | -56.54116 | 2025-07-04 04:40:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7082559f-fc12-3055-a540-c973f476af92 | -12.13259 | -44.91308 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bc22902-0be4-3e3a-b423-65280f88e4f0 | -10.55877 | -49.13366 | 2025-07-04 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 0fb24f4f-54b9-37d3-b02f-acba9c421328 | -13.39619 | -47.82967 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efee865f-f5da-3a79-9fe5-67c0694358cd | -12.13385 | -44.91153 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9636c76a-327a-34f2-981d-10349404c80a | -15.13789 | -47.47422 | 2025-07-04 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4abb036c-07ff-3cfe-8875-bd46706f1036 | -12.57689 | -48.88521 | 2025-07-04 04:40:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33455c7e-62cd-3ac8-bc12-96c0eb271de5 | -13.4459 | -47.81932 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebcf2cae-1a5d-3f82-9d54-ae59a957dd67 | -12.03662 | -48.75399 | 2025-07-04 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc8df3dc-5ec7-3f8a-ac0e-589b3669744c | -16.67983 | -43.88265 | 2025-07-04 04:40:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91a2dfbd-5c96-3730-98bc-63f6a75d8b64 | -11.91934 | -45.3997 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e464a94e-6405-3c2a-95f4-080cbe74d148 | -12.58242 | -56.98467 | 2025-07-04 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b844101f-310b-3121-a9fd-b94582c6d2b7 | -10.22764 | -56.76305 | 2025-07-04 04:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fee88d1f-5bde-37d6-bf44-268a18d69a37 | -10.87586 | -49.54719 | 2025-07-04 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47aa94b5-5e7f-343f-a938-6e5e41bba031 | -9.52762 | -63.57645 | 2025-07-04 04:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ef058dd0-731e-3827-83c3-0402b94d047c | -10.98855 | -44.50089 | 2025-07-04 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bacf66f-f008-3944-bb81-07e42a2aab04 | -10.59171 | -49.45515 | 2025-07-04 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99ba877a-dd1e-3ff8-92a5-7d933183b16e | -13.45524 | -47.8355 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bc25276-250d-3b75-a518-1c8fe43d90eb | -9.33962 | -58.85204 | 2025-07-04 04:40:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb3419b4-0479-3d09-9b2c-db7ac3d5f8c0 | -12.19668 | -50.93985 | 2025-07-04 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81735f60-2061-3933-8799-272836a560d7 | -11.92397 | -45.39663 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58da513f-2c8d-3a12-99a8-8f4c35bc4a13 | -13.4497 | -47.82228 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bce6078-89a9-3ef6-84ef-d006d325c08b | -10.08481 | -52.74284 | 2025-07-04 04:40:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cf01eae-fdd7-33e4-9e75-5264d8961012 | -16.03933 | -51.16578 | 2025-07-04 04:40:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 637459a1-b9e9-3da1-bf74-e1cb24d6afff | -14.87977 | -48.35402 | 2025-07-04 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e96348e0-cf3b-39e1-b864-30b7810960f8 | -9.24477 | -58.7491 | 2025-07-04 04:40:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 853d2d54-ec67-34d4-9a05-f24c9f3d05f6 | -16.94808 | -46.08907 | 2025-07-04 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ec02639-ed98-34f5-839a-e24b77389f9a | -12.26863 | -43.65752 | 2025-07-04 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe6bb9d2-1181-3b94-93bd-649ab41d301e | -12.16665 | -45.52807 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ee75a97-f69f-323e-9568-ce320f549131 | -11.48512 | -48.44535 | 2025-07-04 04:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2535a8f-2915-3910-baee-849064b746cd | -11.92196 | -45.38094 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72124794-124c-35a1-8bec-26b9886cba18 | -11.87905 | -58.73413 | 2025-07-04 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46edfe58-e5e2-31b3-a38f-569bbad5fbec | -13.39255 | -47.82919 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5cb67edb-5282-381c-9d8e-5c36eebb3d82 | -11.92344 | -45.40037 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd136b9b-dbfe-39f1-ac24-49f6487c3451 | -10.24479 | -47.67948 | 2025-07-04 04:40:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f45e6693-a5f5-3027-9642-248c4fd868b5 | -9.52639 | -63.57763 | 2025-07-04 04:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 31fe56d3-a919-396f-84a6-7eaeb8cbd102 | -11.52637 | -48.95909 | 2025-07-04 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 296051bd-7564-3109-9730-c264ad6da493 | -9.64002 | -63.50837 | 2025-07-04 04:40:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a535f72-85ee-3247-ae5b-1d769f79a3ba | -9.62915 | -61.46936 | 2025-07-04 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9ad051d-ab0f-393e-a688-e1eac23f1ed4 | -14.60914 | -48.24533 | 2025-07-04 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dad3ba6-dec9-3ebd-8234-d12f24e8eb80 | -11.85513 | -44.86655 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e11d6060-6a7a-3f14-a82e-d0aac968fee3 | -10.88931 | -56.45686 | 2025-07-04 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dcf8746-dba5-3731-9bcc-2b06c96d433a | -11.91735 | -45.3839 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e143e298-ae08-3670-91fd-f0c690ff351b | -9.63089 | -61.46038 | 2025-07-04 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49dc7150-33b0-3d4c-adcd-25d17103dcb6 | -10.98158 | -45.10567 | 2025-07-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9645d64-8fc6-3d0f-93d0-4a965c1b5a59 | -10.79129 | -48.28436 | 2025-07-04 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 936f3338-2f6c-363e-b443-a485c48ab5a1 | -11.92913 | -45.3897 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 885a7cd8-c03e-3668-83ba-c23342fdc4aa | -16.54436 | -45.13141 | 2025-07-04 04:40:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d0d914c-2b12-381e-b50b-b442f0749c3a | -11.92861 | -45.39346 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b5d07cb-d57c-38b9-9428-38d17c106e81 | -12.93598 | -47.13297 | 2025-07-04 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63a2e367-adaa-36a6-80e8-c502ba5505b5 | -10.58781 | -49.4582 | 2025-07-04 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 516ab60c-9a6b-37a0-b63e-987be5e4b8d2 | -11.54183 | -47.31137 | 2025-07-04 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6395869e-badd-3e17-95ad-c70f58451d32 | -10.89354 | -56.45762 | 2025-07-04 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 595372fc-6891-3b71-8f17-f8b411ac0414 | -13.22832 | -49.82921 | 2025-07-04 04:40:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bda31bd3-7c13-343a-823d-2bfe96d2aed9 | -10.25893 | -48.14841 | 2025-07-04 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)
