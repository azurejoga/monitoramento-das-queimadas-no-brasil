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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 963b39e3-1187-3642-a9f7-68f515f414cd | -12.21699 | -50.79145 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0fd941e-ba96-372d-ab0c-023660907f45 | -9.01905 | -60.55614 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b3a95e5-cd66-3d49-9827-9b0087724508 | -11.2898 | -51.28228 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25e09fa8-4027-392c-8a86-3a11824f0800 | -9.63072 | -49.02178 | 2026-09-25 04:46:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca21e468-2ae5-3e31-81e9-201a42920c12 | -9.15335 | -59.47604 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 44b0e743-2bc2-37ae-8a5b-2efc155aa23d | -12.22085 | -50.78848 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f6c0ed9-9c40-321c-8e59-2d4658aa5bc0 | -9.11179 | -59.50289 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35781ec1-4a65-3902-b1fb-a9cc07777c3d | -12.22803 | -50.78603 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fd0f526-2028-3ccb-8c15-079a23bf75ef | -9.15144 | -59.48622 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8df89f0e-841e-3041-af76-a35ad04ece91 | -12.22807 | -50.74269 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2010432-881a-3c76-9d96-9304019a6243 | -9.50728 | -49.23067 | 2026-09-25 04:46:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1cf39056-ea94-3e63-a5a6-260fc1a9e910 | -6.31645 | -57.7504 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 197f05c4-0913-3df2-8a30-ede0cc709b80 | -10.29068 | -49.95585 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c91e4c58-39b5-3080-bd2c-2a3d0bfc4ae2 | -9.02389 | -49.63285 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8984f973-53b8-3d5c-97cf-b43e0404cd8a | -6.66174 | -58.56674 | 2026-09-25 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b54fc1f8-c51e-378f-ae82-333d169ab626 | -9.16094 | -59.47407 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7a181304-a826-39d9-b06f-f6447f247439 | -6.19731 | -57.78699 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eebd479d-c82a-3c5a-bdf7-d2c3c45b0c1b | -11.28974 | -51.30397 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6644dd77-7e28-33ee-90be-1aa0fcf65fb2 | -8.09358 | -54.98534 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32e21a7b-181b-3f47-baa7-bfd061693332 | -11.15516 | -50.65521 | 2026-09-25 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| f24a7fe6-be46-37ef-a648-263634e57033 | -6.23409 | -57.75326 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6bdc8fe-743e-34e2-bf09-84affbd83aab | -9.15865 | -59.47706 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f8cd4ab5-8a41-30c2-bcad-222ffff63b31 | -10.57182 | -51.28742 | 2026-09-25 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 498a8ad9-f188-39ca-bbb8-d14d2b6eb66b | -11.71054 | -50.55796 | 2026-09-25 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d886f3f8-5329-393f-804d-46b5692808d6 | -8.25124 | -54.69219 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 35fa360b-29f5-3488-a11e-5fc89e270b82 | -10.90381 | -53.93559 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7b210c3-6770-327a-aa42-b6eb53df8859 | -12.22254 | -50.75625 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| b19e15d8-7585-324a-a47b-f595826de6c2 | -12.20264 | -50.77468 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 877ea6f5-0c8c-3e08-826c-e2970f692075 | -9.02002 | -60.51941 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e614efb-fe44-338b-8bf8-3ad97cdb73bb | -5.31544 | -49.05005 | 2026-09-25 04:46:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49eb7794-8e16-38a7-8a9f-936acec29b26 | -12.21702 | -50.74812 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fec27c6a-7748-396c-8a3f-89f3bbea7b04 | -12.21258 | -50.7763 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 08acb185-c5c3-3c24-bb8c-f9a1d7cb63ee | -11.27862 | -45.37712 | 2026-09-25 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4347a51a-82cc-3ea2-9f4e-31bb940d4418 | -12.22583 | -50.77846 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0f441b4-62b6-3719-a716-ffc88f7469ad | -8.32609 | -44.14352 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 84451577-ed26-3af1-ad55-2e4d15001fdf | -6.67623 | -58.57598 | 2026-09-25 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bceb70e-4914-3f04-8c8b-279b4cb79abf | -10.88187 | -54.04174 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 745de356-6f9e-38f2-aca1-b00f5353f804 | -10.61651 | -53.99074 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6738cdca-9ef8-371e-81d3-cde31fae7de8 | -8.92225 | -44.53031 | 2026-09-25 04:46:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39e67be1-3894-327d-97ed-0ecec3747fc8 | -9.15993 | -59.41904 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1505f359-2f2f-341e-9843-3b49d4a261b5 | -12.20871 | -50.77928 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed86259c-f815-3258-8416-22332c79563b | -6.44583 | -57.7752 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 239ac648-d14b-33a6-bba3-bf6366f13167 | -9.63125 | -43.95528 | 2026-09-25 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0ed39646-cd27-3742-a6d3-d8490dc68dd3 | -11.27427 | -51.29419 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3641c6e-5919-3ce5-8d76-ca4f6a9a0e43 | -12.54905 | -50.07798 | 2026-09-25 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52fd9fa9-d58b-38dc-99b4-78f5097806fd | -9.01857 | -60.52718 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 603207ac-6410-3db6-8158-4099dd99394c | -12.22365 | -50.7492 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 317eacee-55ac-3c0d-a4b5-6ac29bfa79c9 | -6.66059 | -58.57324 | 2026-09-25 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 819f11a5-ede8-31fc-b27f-4b055443d977 | -10.41524 | -53.80567 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5aeb635d-0595-356b-830b-2406ce823866 | -10.61578 | -53.99504 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b72d3b4a-2d5f-357e-af49-2f3ced10cd24 | -12.24462 | -50.76707 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8f353ba-50bd-3ad5-bedb-84a01f244d06 | -6.67674 | -55.04996 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bc4355a-34df-3acc-b788-6339e5136007 | -10.41881 | -53.78452 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4938c949-d2f9-3eaf-b12c-d212f16a4151 | -6.68024 | -55.05432 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28ad6f57-235e-310f-a8e8-6b3b2553f422 | -7.1187 | -41.7291 | 2026-09-25 04:46:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7bd45286-88cc-3a4f-b3b1-43ab9ce3e115 | -12.22144 | -50.74162 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9c0bc674-30da-31b0-9dec-0b5a0f0edb12 | -5.47069 | -48.43213 | 2026-09-25 04:46:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff91d820-043e-354a-9a5f-a21e9379a27d | -12.20707 | -50.76818 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05270c57-4df3-32e6-a964-4e8c9e292411 | -9.15081 | -59.48956 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 620006c4-4d5d-3613-a88c-27198e10e857 | -6.67474 | -55.08758 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef6660dd-4b95-33cd-9160-3aff9ce0db42 | -12.21312 | -50.79444 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b65f6f2-9d71-3df1-9bc3-c41995b0db8c | -10.61797 | -54.0043 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e50095a4-d981-3ae2-bb90-3d5222caee3f | -10.27408 | -49.9532 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b7c0c2e-c934-3c9b-ac90-8d1921938444 | -9.02721 | -49.63338 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b1e92e1-2220-32e9-8019-703093271fe3 | -12.19933 | -50.77414 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0173fa83-3059-3631-a962-e8fe90be0d44 | -9.02057 | -49.63232 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a57e8b27-b166-3562-a966-8a77600cc9f4 | -9.02349 | -60.53234 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7bd8e47-6728-3aa3-86b9-0bb1fb32d3fc | -7.59095 | -41.79047 | 2026-09-25 04:46:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 97349e4a-7af9-33dd-93ca-3f5438cc2d1f | -8.27262 | -54.75371 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf2528a4-01c7-34e2-93e1-decd8d722337 | -12.2297 | -50.77547 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0dbf7ca6-5399-3466-aa95-8c9f661353cf | -12.23135 | -50.78658 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ea879a6-a695-3072-9f25-f7abd5c30e68 | -12.21756 | -50.76628 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| aee82a68-6bf7-3820-bb57-d9237126fb0f | -9.1455 | -59.48856 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 173d7397-749a-36d9-8f4f-4abbeb45c355 | -12.21978 | -50.75219 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e5d2f077-51b3-3593-b248-c62899b5d5d6 | -10.9009 | -53.95258 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9937e61-8833-39c7-8766-a5f406a0cd0d | -9.15991 | -59.47037 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c67e4b2-9fdf-3e9f-8d3c-37c062b70a6a | -9.02495 | -60.52451 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 84189612-71fa-3024-9224-d156b456ff4e | -12.22531 | -50.73863 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91f7d55c-2984-302b-8f09-585e8870819a | -10.41952 | -53.78033 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f35f345-6b96-34c7-bb02-176474c9ef26 | -10.72461 | -53.9952 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4110f759-4bf1-331f-86bd-5aa0041c24c0 | -12.21371 | -50.74759 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 91d07ebc-b615-3569-8ca5-62a6621e7d35 | -12.2275 | -50.76789 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c496581f-ddbb-31c4-828e-f4588f6ecf2f | -10.66092 | -51.32739 | 2026-09-25 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99d9b367-0852-3230-ac1a-7378089d49c2 | -10.90091 | -53.93076 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ffc6283-e6b6-3d5f-8a6b-cc34a6e2b210 | -9.41513 | -60.46413 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 457a254b-ebba-39ba-81bc-faffea349e81 | -12.21643 | -50.79498 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e96cbe4-ff95-3ca9-9c2f-40329d5291f6 | -9.00474 | -57.13748 | 2026-09-25 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08760f39-2398-3166-8927-6ddd387f0156 | -10.63977 | -51.35292 | 2026-09-25 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec9b0524-4e4c-3d18-90c7-16c26d82c43b | -9.62946 | -43.96836 | 2026-09-25 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 296a6b6d-8dd2-3932-99fb-2f744fe7baf0 | -12.20982 | -50.77224 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c427ce76-2dc6-32a2-932e-6b9e3bd5d1ad | -12.21646 | -50.75165 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 587248e4-afb4-3fa3-8d68-5de894b11829 | -12.2032 | -50.77116 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0aeb235b-6c6f-3ef4-a57a-29074ef54cfd | -9.73363 | -54.80153 | 2026-09-25 04:46:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 653d26b9-53ec-3891-b6cd-28f8149e7d14 | -9.42149 | -60.46135 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 648e5fd3-8dec-3ce8-9641-4bf17ea80a0c | -11.8732 | -50.75406 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 13c99771-111c-3262-87fe-3103531d58c0 | -6.19141 | -57.79079 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a06b5e61-91e1-39f8-9585-013b3368c52e | -6.31149 | -57.7495 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f74999f5-d805-3278-a614-5c4035919000 | -10.42242 | -53.78516 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9261ea32-90e9-3308-9103-3d58e9fb8b2a | -9.62683 | -43.95469 | 2026-09-25 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 855d8059-c126-37e2-89ab-cbd6cad567a9 | -11.27881 | -54.04416 | 2026-09-25 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README27.md)
