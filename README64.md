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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a98511a9-2f94-3ffb-b1a2-7f5bbe8c7653 | -7.47577 | -61.34542 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41f23983-ab9c-3952-b7bc-ba8042a93324 | -7.5408 | -61.38826 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37dc60e9-993d-32c5-8a73-2eb29f3336d3 | -10.50123 | -46.87828 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cefa38c9-19f0-3b21-a2f5-0385d57ca25f | -9.19291 | -59.62106 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f10528c6-6740-3f92-abff-9c039dedd81c | -12.7474 | -48.09631 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6791d777-b32f-3328-b544-003ca8113baa | -7.28876 | -59.66967 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0775d99a-5d57-3bbb-8b6e-cf9588be1196 | -9.16012 | -60.78329 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b14353d-e3b2-325c-975b-f6a8ef84acfb | -11.91441 | -47.59857 | 2025-08-26 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3594b5f0-40a1-3aed-bbfe-9eb216809d11 | -9.16893 | -59.50554 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1e4621c6-f2e6-30ac-91cf-8ae8ad8d9e36 | -13.61163 | -48.15119 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d833e81a-b6e9-3c51-bf3b-f6970b80e7a5 | -11.3086 | -55.11097 | 2025-08-26 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| bdebbce4-be70-3d80-8612-949d99a37ffd | -7.88294 | -63.0162 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca44a67e-537c-3603-b8c9-3e01c601d202 | -12.49078 | -53.83221 | 2025-08-26 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddb11804-1db8-3f13-99f7-aed3028a492b | -15.31725 | -53.83767 | 2025-08-26 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49749e63-49f1-31e5-973a-2ddc9a1a1666 | -10.38662 | -57.69608 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b7a5b4f-9390-3c88-9809-f648d0731011 | -9.5541 | -48.17115 | 2025-08-26 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36ee8e48-d5e7-3d7c-9dba-d82c5fcfc8fd | -6.78815 | -59.67381 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c149399f-20bc-3ae0-85ea-0460dcddb4e7 | -9.18724 | -59.51438 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a7953d77-f69c-39f5-91bf-24bd982e2197 | -15.11536 | -48.72001 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| accac2da-76cc-3b6c-a534-e3904495ab0a | -9.20459 | -60.9231 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be620015-5ef0-366f-92a2-0c79f55a7c83 | -9.23282 | -60.91835 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dbf1378-b840-37aa-b816-55bc735b305b | -8.4056 | -49.49226 | 2025-08-26 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 271f9555-84f0-310e-89f8-a617c89268f5 | -9.1607 | -60.78002 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c5c04a8-9606-3da1-ad35-e1722818a7ae | -11.29111 | -53.95947 | 2025-08-26 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b69eb47-1e99-3f80-a0ef-b09b646bea0e | -6.76279 | -59.66906 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4231f0f1-c1b4-3e09-bc83-d7d649286376 | -13.05251 | -46.30696 | 2025-08-26 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12691c55-fd35-3fdf-a884-088278153f89 | -8.12257 | -62.87947 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7892a49-b754-33d7-9d99-2f1f4afdc913 | -11.52551 | -52.13262 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 03c98ccc-63a7-321d-848c-941e7e3d463e | -8.57249 | -62.63417 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2fa5489-bd1e-3170-b559-f90796adad0f | -11.55255 | -52.13339 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c1f8ff9-d56a-3b2d-8d6d-5f5b9a899796 | -11.56028 | -52.12745 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a6d94fe-ddf6-3f7d-bf27-a3c1fae1f7a6 | -8.3308 | -50.56801 | 2025-08-26 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11cb6269-e4a3-3521-b8fe-7284c01c80a9 | -8.24487 | -61.45408 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 889714a8-8fff-3cad-83c6-1ce821130156 | -10.77784 | -46.38316 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a78fabec-dece-346a-bff7-01543e375c9b | -10.24397 | -59.6635 | 2025-08-26 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fa99056-6afe-3b41-ab2a-51fbcb52f5b7 | -9.17436 | -59.51049 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc2c4469-4f63-3b5a-89f8-3daf7fd4b868 | -6.82034 | -59.43378 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6278b611-9595-3df1-9244-ef9342d034f0 | -7.53658 | -61.37965 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d67a3a6-ab28-3478-a2ca-4fc3c0517e9b | -9.61168 | -55.37105 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e227a073-8a82-36e1-8c3b-6f5f42850bac | -8.60927 | -62.64828 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4de9249-0215-33fe-bab0-ea9d222ea611 | -13.16206 | -45.28788 | 2025-08-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74ecc331-c04f-3efa-b610-5e11fa68bb8b | -6.78253 | -59.6759 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7c77455-5670-3c75-b456-ad98b23d5140 | -8.1028 | -62.88246 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0aaf5846-18ed-3061-a738-587e0d107f51 | -11.53532 | -51.91823 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f007354-b31c-38d7-ba66-d34d3e755d65 | -9.69369 | -48.33633 | 2025-08-26 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5daf2bd-b4cc-3293-9dc6-7d4e60125068 | -12.92692 | -46.31034 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c3bb6898-182b-37b2-98a3-1b2ae1148f44 | -11.62304 | -46.21365 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8604604b-829e-32c8-8a33-d49315aafb89 | -9.10601 | -46.06825 | 2025-08-26 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2f0ffe9-5553-3b48-8905-053b5b5ef958 | -10.82113 | -46.38033 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efbc5498-ba03-37df-8eef-40796b69f6f4 | -12.38916 | -45.00346 | 2025-08-26 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2b2830d-66f9-3c62-af16-8695570d96d1 | -13.51844 | -46.91045 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3cf8e22-326f-32d1-8bc6-98ab657f994d | -13.71641 | -52.01319 | 2025-08-26 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2fe9e99-678a-3c31-a394-7e77ca3e2af3 | -12.76167 | -48.14433 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2c3ffaa-349f-356a-a1d7-fe1503dcf637 | -11.0448 | -52.01582 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 130ded0b-6383-39c0-a440-f28f57bf6aa7 | -11.54868 | -52.11477 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc271e60-2439-3e71-9c5e-e092fff508d6 | -13.60521 | -48.19625 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85098d2c-50f9-36e8-9447-62b0d7baab75 | -13.4549 | -46.87021 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 973d32c3-5b6e-34a0-8b23-c96cf9058683 | -13.42494 | -46.93186 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce3c5a70-e831-3543-81f2-1d97bb77fba0 | -9.18818 | -59.53663 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3ee21a1e-f25f-3cda-84b5-fc2106e10218 | -9.15042 | -59.55197 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dab3461a-8607-3318-b42f-d8697f37488e | -11.5513 | -51.88112 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82384a96-e8bb-38de-9148-29dcc5b087b7 | -13.83076 | -46.69274 | 2025-08-26 04:46:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4e57934-e3d0-31ab-8112-f559c8df1a45 | -9.16098 | -60.77523 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c496d473-c76f-3c18-9845-6a2eabe5a214 | -10.76297 | -47.05426 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e67745a2-a8e5-39d1-be7c-e1113a90c408 | -7.41887 | -60.62063 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e63d8f39-a46a-393c-9899-8d120e897d59 | -9.27069 | -59.7904 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4e63030-d946-3732-9079-550dd79989b8 | -9.17954 | -59.50197 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ff70f22-0b21-356c-8574-e39c6cdc37fe | -13.60843 | -48.14731 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 229b62a7-94ab-3a79-8620-ab8c6ba55377 | -9.17529 | -59.5052 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22f0f839-e090-3bc4-85e8-0cd0e7f21dcf | -13.60776 | -48.1504 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52e74c13-a982-3017-9021-ef4573e39a7e | -13.42077 | -46.93103 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0f4b89d-0c61-3c0c-9ffe-71b391e59737 | -12.76623 | -48.13989 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 02032f37-ae03-3658-9549-6214f1de2143 | -12.40715 | -46.50124 | 2025-08-26 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d83fe62-0a5b-318e-93e4-465c91059532 | -15.10107 | -48.73813 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55b6db9c-e9df-3834-8708-8276e670994e | -13.82129 | -45.89697 | 2025-08-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5572575-a9ce-30f8-b2d8-724ec2109009 | -14.28194 | -49.13426 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 79bbe812-891b-3e22-959c-710106e26aeb | -11.30179 | -43.29061 | 2025-08-26 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a1e776c-f0f1-32aa-8397-39480551ad15 | -13.41448 | -46.8823 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 145827ac-7c38-3e7d-ba8d-ae73a6271d6f | -13.43656 | -47.00321 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36830ba1-953c-3170-bc2c-08d0e47c65fc | -8.56201 | -55.26065 | 2025-08-26 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d392e1c4-8bf8-30b3-93ed-c3269eadf585 | -11.52992 | -52.12614 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1d7119ca-fbf7-32f3-a90d-4a132ed33357 | -10.53498 | -46.78677 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 64913549-65b4-3039-9267-8a40548dc41a | -11.14925 | -44.75622 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a67e2e9f-bc92-3666-ad88-375d6705af5a | -7.47084 | -61.34068 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b78fa054-668c-32d6-b1b1-1ae732757cfe | -9.65457 | -59.62934 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 484bb44e-4cb4-3583-8924-a63fb3a4489f | -9.20265 | -59.51181 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fa8d9e6-894d-3cc0-9481-6333db5c9edb | -13.41226 | -46.89869 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e77abb0-3463-34c5-9c9d-4fc6de59e0a7 | -13.52267 | -46.91101 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acc7a0c6-dade-3a06-99f6-c0cc49cd945b | -10.01137 | -62.39152 | 2025-08-26 04:46:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99d94dc3-7e6e-37cd-96f1-d47d44a34921 | -12.93513 | -46.31542 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 858598f9-85a6-3306-96f1-45663522dedf | -11.56193 | -52.11691 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 901c6283-a8e2-3700-af68-144351b02ba2 | -8.55041 | -62.65308 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e689c778-2d52-3b99-bbcb-45ee066fc180 | -9.5629 | -55.374 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ab85f67-fe10-389d-9235-64fe5f3b379a | -9.27157 | -56.90352 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54eb7959-1568-3d91-85f0-96ea42398525 | -9.17566 | -59.52326 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d315466d-f714-3272-b25e-5624f52e438c | -9.18244 | -59.51341 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c341025-bc2a-365c-ba15-fec56b81c25b | -14.34741 | -51.95195 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc1a8dda-3800-322c-a6d5-f9d07b2e5836 | -8.12523 | -55.55205 | 2025-08-26 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f2b4460-d7c7-3bd7-8fab-11bf295b45c7 | -13.81673 | -45.89647 | 2025-08-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46db84a2-b7cd-38b4-914c-304d25371a78 | -15.1049 | -48.73874 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README65.md)
