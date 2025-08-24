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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a9832e6-dfa2-31e5-98e5-a284f5317606 | -9.032 | -65.697701 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e668a6e-dc91-36b5-8cfa-9ca7c50f21ca | -8.8797 | -62.429001 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3e3bf81a-5a5c-3f90-bf50-90c96ea8df2c | -9.154 | -59.4786 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c847c17-f51e-3b5a-848b-5ad82da3a77f | -9.5153 | -60.544201 | 2025-08-24 01:24:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd7973a6-7d55-398e-853a-65c8609bac0d | -5.4157 | -60.152699 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09e2f7a4-af7a-3a19-9931-f345eb107101 | -9.0025 | -65.704399 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 198f1731-5eeb-369d-a6e5-384aaa218938 | -6.8682 | -59.819801 | 2025-08-24 01:24:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7c05f14-ce7d-378c-a6a0-0fd036df6395 | -7.5526 | -63.863201 | 2025-08-24 01:24:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d540940-8fb1-39f8-8722-8f1c8ccdcc2f | -9.1633 | -60.796501 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0436b13-9b44-38c5-8968-5883741b9b92 | -7.549 | -63.847401 | 2025-08-24 01:24:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c69e1f91-95a5-36e5-9274-1e5c5dd50773 | -9.2726 | -65.898102 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03de7b74-3771-33f9-8c07-a561e15b0932 | -8.9035 | -62.442299 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bb503cb8-62fb-30c2-a4e7-5e66dd5d7a0b | -12.5845 | -60.3423 | 2025-08-24 01:24:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4691cb92-773b-3996-b00d-50d02af8381c | -9.1507 | -59.465099 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c38c9d5e-85b6-315c-8774-6485e6dd0d7d | -5.4483 | -60.203499 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f3627d9a-5528-315a-8e1c-3d7b4960456f | -8.694 | -62.870399 | 2025-08-24 01:24:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 44517427-de99-326b-912f-d04188cf7214 | -9.048 | -65.723198 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 378b1aff-df4b-30c3-a44a-319d6b83c91d | -9.1701 | -59.4603 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5ee5c32-29b2-3818-85f3-fb0a4644f7c3 | -14.2989 | -58.4874 | 2025-08-24 01:24:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 669569ae-ae0f-3bc3-8296-102c640ac3db | -14.2868 | -60.372101 | 2025-08-24 01:24:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24ad5239-2720-3531-a5c4-4cb4c98ac045 | -8.5855 | -68.140198 | 2025-08-24 01:24:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e332954-71dd-3d17-ad79-48930816c51e | -9.0233 | -65.384697 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d94af4b4-dc7f-39f2-9a39-98f2f044b742 | -9.1606 | -59.5056 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1790209-1929-3e29-9e79-dab9faa5c1db | -9.1866 | -59.612301 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b76abcd3-8f50-3bf8-bd8b-5c52caab2d4e | -8.6095 | -62.596401 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6c6d6a-76ae-39ca-a0c4-8b4c400f6cea | -10.4197 | -64.405998 | 2025-08-24 01:24:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7540e672-4b6f-3ba3-822e-3a524290212f | -9.0103 | -65.372902 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68ad902c-c2ab-3698-b87e-724f23ac18a2 | -8.8971 | -62.415401 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2be57d3-8228-3c6b-9479-4aaf8161d810 | -9.5083 | -60.557999 | 2025-08-24 01:24:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d221ecae-3ef5-3898-87f3-f5d8885fa065 | -9.197 | -60.7649 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d4dafce-5ddd-34b6-aaec-10dcad04adff | -9.0123 | -65.702202 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 763a7f93-f12e-3dc4-88de-e96136a1101d | -7.9686 | -63.076401 | 2025-08-24 01:24:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f123f82-41cc-331b-8930-7a47843a110a | -4.9476 | -55.812599 | 2025-08-24 01:24:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57cda357-4c51-3569-89c6-a5f6e061eb90 | -8.8721 | -62.4403 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd05e819-86c2-3b43-9d95-a43c302e8469 | -9.1571 | -59.4491 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc5cb6d-1936-3045-bd2e-8ec0f1fa39ce | -9.5618 | -68.568604 | 2025-08-24 01:24:00 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6e7cbcd6-8073-391f-8b05-dbe576139531 | -20.352699 | -51.703201 | 2025-08-24 01:24:00 | METOP-B | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f9caaac1-36d1-3de9-acff-773ebc200438 | -4.938 | -55.814999 | 2025-08-24 01:24:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25ede945-6fa5-3da6-8d5c-f7ed15b257d0 | -8.826 | -69.391098 | 2025-08-24 01:24:00 | METOP-B | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7ffd35e7-4657-357f-b5dc-bf37c22869f2 | -9.476 | -63.127499 | 2025-08-24 01:24:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 75f4e525-271f-3b7f-8187-6074b3b75222 | -8.9069 | -62.413101 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 58fbe384-2a12-382c-b5ed-1a1aa372dbca | -9.017 | -65.723 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 557f9641-51ee-3e58-87d6-b65a3aba9571 | -8.8894 | -62.426701 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc72bb3-a2e3-392a-849a-d1466e8411dc | -8.6745 | -62.875 | 2025-08-24 01:24:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d23363a-d0a5-3a3e-8489-9a8d855496b3 | -8.6116 | -62.605202 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8857c5f2-4967-371a-92f1-c525946b879a | -8.9014 | -62.433399 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93e63105-73a8-33ce-afe5-425f0aed094c | -9.8194 | -64.260399 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8e2ef4a2-6103-38cb-ad82-09b9000e1d22 | -9.0449 | -65.709396 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ea734b6-6a09-33f8-890e-acdf708b2fc7 | -8.8916 | -62.435699 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9dec92-460c-3212-9449-02622ba2dc3d | -9.1385 | -60.778999 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee9fc7ae-19fa-3422-a811-a9a677d6e01f | -8.8242 | -69.382797 | 2025-08-24 01:24:00 | METOP-B | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c3cfb4bb-aecf-30f3-91e4-984e07a1f300 | -9.1476 | -59.494499 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 809f29fd-d91f-38cb-8c0b-5d40b6c09e1a | -10.4246 | -64.427696 | 2025-08-24 01:24:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c59f84a-db93-3cb7-9ed6-38f81b71e6ac | -8.6254 | -62.620602 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| deb7e0fa-6727-34b7-bf47-653ee7d40a38 | -9.1896 | -59.455399 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0552e3bd-66d4-3167-9a2c-d51e6e038a6e | -9.6343 | -63.098801 | 2025-08-24 01:24:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 58dd1b43-47a1-3302-8b32-110567e231c0 | -7.5623 | -63.860901 | 2025-08-24 01:24:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85dec6c0-5116-31c2-a85f-a4b4519bdefe | -8.608 | -62.633999 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d7888c13-a676-3341-956d-266f3bde1d19 | -5.4223 | -60.1805 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca88dffa-8b31-3d62-95b8-d91a150947ac | -9.7979 | -61.206799 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e47eb30-ca7b-3c4d-9f1a-76a45f99706b | -9.6464 | -59.637402 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88603b6f-67f5-3511-815b-9b792cf64fab | -7.5471 | -63.839401 | 2025-08-24 01:24:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4fdf981-5414-3f25-babb-68c2ea0216ed | -9.0563 | -65.714104 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e491bbbe-8ef8-3891-87a2-2d352523e222 | -7.9194 | -63.042801 | 2025-08-24 01:24:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43912c65-e1a7-3881-afe4-03d02a60daf7 | -5.6106 | -60.2374 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 385af76f-5f37-3a9c-8808-f6cfaf0b4ca4 | -8.6074 | -62.587502 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fef1610d-6b56-369e-b1de-e1746d9f1319 | -5.419 | -60.166599 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 429dcabd-9975-3e94-8477-661ec3472ec5 | -9.2241 | -60.921299 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 894196d1-09a0-3271-bac5-ce8833918744 | -9.1952 | -60.800499 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3b7ee76-9a2d-3d5c-80b9-745c1ccdc212 | -9.1358 | -60.767899 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e88a5c22-c32d-3aca-8171-2103276df072 | -4.9545 | -55.840801 | 2025-08-24 01:24:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de88eb53-3b0d-35bb-8778-cc76070c7903 | -5.4093 | -60.1689 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc289391-2902-31a2-91ca-6afff84e2b35 | -20.3444 | -51.674801 | 2025-08-24 01:24:00 | METOP-B | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fad4be9c-2e68-3214-a212-03ea18a16d07 | -5.7874 | -59.2155 | 2025-08-24 01:24:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28154c30-1b6a-3def-ab30-a6c25795119e | -9.5181 | -60.555599 | 2025-08-24 01:24:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de7128aa-eaf3-3169-bbd7-f18f290fa712 | -9.1949 | -64.550903 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c0e10f78-5121-3614-80b8-768b88ff80f5 | -16.7736 | -51.3237 | 2025-08-24 01:24:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25cb97bd-b108-314c-b1e6-3cdcf8dec58d | -5.432 | -60.1782 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d62a921-a0a0-3771-88da-5429f244f024 | -9.0978 | -61.43 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7600edef-00b5-3c36-85bf-b27c3f4347bf | -9.4778 | -63.135601 | 2025-08-24 01:24:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3878e6af-f8e5-33e4-bd88-6695c2631ae2 | -9.0273 | -65.676903 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4401d87-832e-3440-9613-ccc9881781c7 | -5.4287 | -60.164299 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5ca3e02-db48-3e54-91a5-5e2642e1f7ff | -9.1933 | -64.543701 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63e0619c-697a-322a-b361-49ef1defde99 | -9.0465 | -65.716301 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3a4f21b-0b01-3df7-9862-48e36f8951ee | -9.3251 | -63.188702 | 2025-08-24 01:24:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b1a702e9-0b4c-3c3f-9087-9fe6c5a1beb1 | -7.5605 | -63.853001 | 2025-08-24 01:24:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09c5d9ac-439d-34e9-ab54-d0fdb4a50d35 | -9.0108 | -65.695198 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3d87979-11d8-3170-8dc0-f39b3f621b3c | -8.881 | -62.390701 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18bf1902-96f7-3a2b-90ec-0fab1ae69cac | -6.6839 | -58.844799 | 2025-08-24 01:24:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23632b4a-0dc2-3e4b-958f-e29da71ca697 | -9.0367 | -65.718498 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d5f1b9f-6509-3b7d-8959-09755cc3f6fe | -9.1474 | -59.4515 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a251b81-666a-3b1a-82f3-a52ece9618a0 | -8.923 | -62.437698 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 64f2f383-5d44-3de7-8544-22a50108b3e5 | -9.1926 | -60.789398 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cead7750-252f-3228-89ac-439e405b3018 | -8.61 | -62.642799 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86670f2b-8e6a-3bf1-920c-db3eef8b263a | -9.5071 | -60.509998 | 2025-08-24 01:24:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46341736-602e-3852-8f3c-533169f2fba8 | -9.0578 | -65.721001 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa8afb8-00e8-3fda-a4bc-4911475b9cc6 | -9.9532 | -60.178501 | 2025-08-24 01:24:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a73aad0-34f0-3610-b398-f121efabdbdd | -9.141 | -59.467499 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 430821ae-1330-3986-b8d4-99281c14fe74 | -9.0206 | -65.693001 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f26c267e-7b83-3353-b17a-ad041d7704cd | -9.5168 | -60.507599 | 2025-08-24 01:24:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
