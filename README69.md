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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34c23fdc-c0d5-3e22-82c7-cebe953f367b | -10.02046 | -51.07027 | 2025-08-25 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a28d28bf-cd25-3806-801d-4ad40b7f90b3 | -9.19215 | -59.47691 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9544b26-6e19-364d-92e5-3d8fa5fa6e43 | -9.61404 | -55.34939 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56642d3b-d2ba-35fb-b83c-21e766b46a6e | -8.98738 | -65.41498 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4188b34-cb22-3854-82b7-ae3ede736f1b | -8.97114 | -65.41521 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9c413fa2-964a-3169-9716-ba8ca80df2c8 | -9.82039 | -64.28326 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80b03217-7b9a-3c92-a8c1-4ce4d1fac86c | -8.21899 | -61.41879 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24532a99-419f-3a1a-b1d1-f55b69f72b14 | -10.58561 | -47.1372 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bbad06c-cfc9-39e3-b064-8bc78e41a07d | -8.10283 | -62.8665 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 181030d9-1278-32fa-bc2a-559a29157215 | -8.28627 | -47.24104 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd32e528-0bef-3d15-b5b3-bfb7d53c8ed9 | -5.74186 | -57.57564 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5092693e-f9f4-3882-aa78-634733a24fe8 | -9.05833 | -60.62505 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 188daef3-a0fb-3ae4-a076-b2d2d5b5ed0d | -8.11908 | -62.8678 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51ea1bb4-b9f4-334f-99bb-5d6dbe99349f | -10.41052 | -64.39716 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 05983d2e-638d-3ea6-b05b-c4d0223d4348 | -10.41726 | -64.4418 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e7999106-a274-372e-98bf-96bb32fe8ab5 | -9.23679 | -60.92157 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6b8af4a-3aae-30ad-a0c0-2aedcdda9645 | -5.75111 | -57.5846 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a72d983b-9b18-365e-98a5-f3ddef50c23b | -9.16918 | -59.46038 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c1d647d1-0c8d-31ab-b233-cbc55c092903 | -9.06214 | -60.6257 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd0004cd-2bfd-37ee-a685-695025398889 | -7.6612 | -42.67195 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 073a6ca8-1a03-3fa7-ae01-bb25caebdcef | -6.68851 | -58.85735 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c44ebd6d-d06e-3499-8248-81c83864e514 | -9.1527 | -59.4492 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35c21783-7113-3cde-811f-b1412dfbbcf6 | -8.9111 | -60.72202 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6b4100f-ae28-38ca-99d4-ef059965ad50 | -9.19672 | -59.78965 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efc1b3c2-d5c8-3065-9275-b0ad690b9ae3 | -9.1017 | -61.43313 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90696fef-9c7c-311c-8593-3f42879bc9b9 | -12.95554 | -46.3344 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15de89f4-0b48-36e4-ae1a-a7f097bf0a23 | -10.71162 | -48.31183 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a8f9b6f-015a-3723-9ab7-8505395f307e | -9.01297 | -65.39318 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8921cde7-a5fc-3a86-9089-bd06df110171 | -9.04869 | -65.72624 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec76c609-4df8-3a88-8344-b84a4b798b41 | -6.82115 | -58.95799 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2af6385d-6a96-3190-8008-9c6070ff675f | -9.05402 | -65.7272 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 385eee06-e67a-3bbe-bf7a-f574d655885d | -9.20169 | -59.50815 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7ac0d0f-54e0-3f4f-9813-dd941302d810 | -9.19179 | -59.43469 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fecbf632-6f54-3eac-a33e-134e4b9cd74f | -9.19454 | -60.78766 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cd8cd79-698b-39bc-aab0-0867c91813e3 | -7.90774 | -45.88849 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99637d4f-5738-3278-900e-a4f5e02cc8f1 | -9.25609 | -59.76903 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12d5771e-83f5-3bd1-9b8b-4c831d79a4e6 | -6.7704 | -59.66202 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4611e176-0067-3c03-ab1d-5553d7c87a54 | -8.22933 | -61.43159 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e320107-7dd7-34f7-a5ac-c53d6c10c1e1 | -8.54398 | -48.86471 | 2025-08-25 05:04:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a12e6249-01ca-327d-902b-a0bee9fb7617 | -9.156 | -59.51741 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea1d74db-6aab-369e-aa3b-bdddd473dea8 | -9.80899 | -64.26495 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 088298f4-dcd4-37c6-a041-fc78d2416e12 | -6.04148 | -46.29459 | 2025-08-25 05:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a7c709a-c3e4-335f-bf99-5716586be809 | -9.57274 | -55.37231 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ba8f532-094d-3c2a-8fe0-270b108a48c1 | -9.15422 | -59.46206 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 486b11cf-bbe6-3846-a2dc-4430a66c43c2 | -11.17125 | -55.03041 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f717bc4d-34cb-38c2-a2ea-e34f5855e385 | -9.20459 | -59.5129 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67ea2205-5d8c-3f2e-837a-cda41090adf5 | -7.56431 | -57.66927 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa2a7e6a-20dd-3275-9ad7-c881d000f910 | -8.58995 | -62.63176 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7712f415-da09-38a8-92ac-d3e7f0116ffa | -5.41214 | -60.16829 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 189c6433-9db5-30f6-aa08-2568471d0834 | -9.1935 | -59.4687 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 494ab75c-1663-3f07-a71f-7254f46bbd68 | -9.20354 | -59.47464 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 513eb666-0151-38c5-87a4-e41369b334c4 | -11.13624 | -46.33666 | 2025-08-25 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9a0e70cd-320f-3641-8ad0-18914e8eaa7b | -9.15366 | -59.48738 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caefdbeb-4304-3945-896c-f1fafa12c323 | -5.85882 | -51.75535 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 797df958-0833-3557-99e2-401d293ab654 | -8.89108 | -62.41184 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a18b9e4-4520-3ebd-96df-c0859dfbd941 | -9.52105 | -60.50893 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25298e07-1a95-3c3d-ae54-954ff8711ea2 | -9.13473 | -60.73088 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51097ed6-5e2f-344e-af25-83bcd1b2e6a7 | -7.91137 | -63.07922 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f643a57d-4d24-358e-849b-9dade4736a6e | -4.9617 | -55.81015 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10a946bb-7a1b-3a22-8e01-a6786e29e18b | -6.98934 | -57.32537 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a86c137-1fda-3e19-b2c9-042b24defe1e | -8.98157 | -65.41723 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0b97a3f7-1685-313d-8bd1-48eaec7a50d5 | -10.8212 | -48.33266 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e79c925-ae86-3bbc-9782-7f2b824face8 | -10.77403 | -46.39849 | 2025-08-25 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e990ed4-7f61-3b84-8be7-a8b824174359 | -9.20648 | -60.92931 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fb1bf50-099d-31ba-8f32-416f22f346de | -11.86881 | -45.12466 | 2025-08-25 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a9b8e08-64b8-34cb-9528-51216a41e1f9 | -7.53045 | -63.81807 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a7f6ded9-b592-3df8-842b-a83a0c1439e7 | -11.6059 | -46.34954 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89c1deb1-09de-3542-8d80-be8507cb9fa9 | -9.56994 | -55.36818 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 288e2e9f-4601-36e0-a190-8a6f2618dc15 | -5.43086 | -60.17646 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 16a52262-fc5a-389e-9a6e-1633345b945b | -9.19333 | -59.44757 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d6cbdbf-d1a5-3fa3-ab27-439156ea17da | -9.00894 | -65.3858 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af5ae01e-b2be-3b0f-b3f5-2265cbe81439 | -7.32341 | -44.5354 | 2025-08-25 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d8e7e01-fcc5-33af-ac6b-0f76679aa315 | -9.16493 | -59.46388 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e413d6b-8253-39d8-b828-7bb8e009c270 | -9.15558 | -59.4539 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b82f4d4-871a-3f72-afab-b9f1e9a04d88 | -8.24535 | -61.46046 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 432dd6cf-1929-31a0-b0ff-8cd90bb37278 | -8.58629 | -62.60058 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da32950b-8588-3323-9949-0ff18b1326db | -6.88564 | -45.66196 | 2025-08-25 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22a9f135-62c1-394c-b382-df9f7d03e878 | -6.76968 | -59.66642 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f112cd34-44ce-38e8-8989-9b0c31fc775e | -8.47052 | -63.9295 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac5ed999-fcd8-36e6-a42a-3a081503c2f9 | -9.16012 | -59.49268 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 713a81bf-15e8-3c6c-b6ed-1281de1e43c9 | -9.19689 | -59.44818 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd958234-955f-3845-83c9-18062d07a505 | -8.28098 | -47.24026 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79d00aea-da40-37be-8365-17cce3ab4193 | -8.99363 | -63.6482 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dc374d6-62f0-3a64-a526-f78488dceb2c | -6.65329 | -58.82648 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e484a43-e9a0-33fb-9e5d-1795a44bb608 | -10.4598 | -59.12999 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a94704c-e403-366d-a953-e5c289202ef1 | -9.19569 | -60.92241 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f65ac2f-dc63-3006-b5f5-e58c032e3187 | -7.65135 | -63.52084 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64cc46d4-aae9-3aa5-92bb-795b58d60243 | -9.21954 | -59.67646 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6498785f-d758-351d-bd63-20957c53954f | -8.11462 | -62.86701 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78e6e1db-6a4c-307d-85f0-1c5ed0d16985 | -7.67102 | -63.51921 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04bd9ccc-6b83-30bc-ac46-bdd31a40caae | -9.18133 | -59.65415 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90874846-1bfd-3111-951b-0e03af0aacf5 | -5.87692 | -57.76087 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90822cd4-083f-3118-be65-65e49e32d42a | -12.75407 | -44.41731 | 2025-08-25 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43d394b0-ed9a-33f9-bc45-71d7c558edc2 | -8.07786 | -61.53607 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd5f4a51-e650-3e98-a660-08b82175611a | -8.59897 | -62.61049 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6469546-d16c-3a4d-91d5-2ae3bac78096 | -9.25827 | -59.64429 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f5746b5-2979-3717-9a31-bf02acdc29b0 | -8.11589 | -62.88575 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcad9c6e-95ef-38f8-b4b9-dc0d44108986 | -11.52501 | -50.46172 | 2025-08-25 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2a36bfc-c0bf-3f73-847c-e793356e5b54 | -9.21098 | -59.70522 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf109187-d448-367b-bb89-9acf981ab837 | -9.06351 | -60.64061 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README70.md)
