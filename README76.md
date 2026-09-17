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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5a05daa-6d27-3e7d-b5c4-594f48c99112 | -6.33261 | -60.00798 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fcf849b-e83e-3d7a-b6a3-7b30926709ab | -9.10018 | -60.9758 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dd14c4f-3944-36d6-8fd4-83b45cf3c921 | -9.10418 | -60.97256 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 342e0f01-70c0-3811-b316-9bd858471c13 | -9.69357 | -58.18021 | 2026-09-17 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3568b20c-71cf-38f3-aa39-b6357eb938c3 | -4.52823 | -55.66202 | 2026-09-17 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5804a2c-6239-338a-9035-79d6e0f522b5 | -7.11276 | -55.12513 | 2026-09-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9706451d-ab66-3ac8-be38-afa3eceac2ab | -6.8457 | -62.89854 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa2b8465-1869-3bb6-90b6-a632493d39f4 | -6.31066 | -62.67409 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a172ace-9a49-3b86-9c18-23f011d6712a | -8.1145 | -54.80965 | 2026-09-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa3f4608-5270-30b9-817a-2567c5961e97 | -9.08766 | -61.01221 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76ec0f18-d7d4-3963-b47f-52758db1818c | -9.59123 | -60.52133 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01a835c4-e0ff-3cf5-a1dd-1ef1dfba7b24 | -9.2846 | -60.6134 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c2353f4-816f-36d3-ac44-82818f7d8582 | -9.09675 | -60.97526 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4c8d0e5-9263-3ee0-b6a4-72f4512bdb09 | -9.09222 | -61.00526 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc7c96fa-8847-30e3-871e-4a761a8173d7 | -9.09615 | -60.95596 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8034e6cc-fdb8-3407-aefa-164621cf4b43 | -8.92128 | -62.40335 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34b8af86-c11e-3b86-aa95-41ee30db28a3 | -3.70287 | -60.62777 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfdc87c7-2f3f-39e4-82b0-ec2f232bc809 | -4.4897 | -55.5013 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2567e4bd-edce-3940-b870-379d9b1f8645 | -6.94115 | -63.0247 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f6fe0c3-99e0-3d8e-a3b9-6f5310f918f7 | -9.38898 | -60.30295 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eef1579-ed33-384d-ac2f-19e9670a5318 | -6.11709 | -59.88166 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92455a8d-ef0a-3474-836b-a2ff6b904b1b | -5.8338 | -52.08995 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0198ea18-b59f-3107-bec6-c54836804ada | -6.9334 | -63.03061 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57415cef-0d98-3286-9fb6-a04be79dcab1 | -6.13962 | -59.94419 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9ce922d-b436-31fb-a232-2625f34595bd | -3.70063 | -60.6202 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28cbe8b6-b4c2-312f-b3e8-31972eb55622 | -5.90538 | -59.94072 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c886c1f-a5b1-3531-b4e4-b452626a9f64 | -6.43386 | -55.60582 | 2026-09-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac348df7-9e64-3f47-b771-ebfe0a01d725 | -8.49124 | -57.65083 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7df456ee-61ee-3186-80ce-6b23104b3cdb | -6.4348 | -55.60835 | 2026-09-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f05aca7e-e3dc-3416-a7b7-2d8032579b58 | -8.48519 | -57.63559 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 7d28ffff-36e3-3710-b80e-a61a5cbcb31f | -8.70131 | -66.54974 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bba0629-1786-33fb-8e9e-14b91fecc01f | -6.69108 | -58.84911 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80a60ac5-62f6-30d7-b7c1-e3fbea6e4a35 | -9.10302 | -60.95701 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64a3de4e-79bc-3a37-bd74-f2f8ce5af1c4 | -6.93727 | -63.02766 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b777878c-0f30-39f4-ad20-4f90739b675b | -6.90108 | -59.03946 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a685909a-308e-3868-b54d-90647affa827 | -4.49801 | -55.5007 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcdeb46e-caa6-313a-9cb8-d1250856504d | -9.09961 | -60.97955 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36dd6480-6216-3e7a-8fbc-fb80706f39ed | -4.53878 | -54.93132 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03291cf0-63df-3259-8f97-d1032667ee57 | -5.15217 | -55.93852 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 092cd93a-e445-35c8-b7ad-f1a3c8d6b23b | -6.79325 | -58.79155 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5793b224-d69f-3339-ad57-027003c1288e | -5.85623 | -52.06713 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73614e78-be23-3ab6-a901-79e411e6e911 | -9.27763 | -60.61233 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30d18e06-028e-3e4b-8f3d-55894cbec8ab | -3.7023 | -60.60963 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63c80623-ed93-39d9-b4b8-26aca7ecd900 | -8.49333 | -57.63668 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed610ee1-a523-3e09-9995-057a2f6f580a | -6.36675 | -58.28807 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bfcff38-d4f2-303c-83e6-6b493f947f96 | -5.15279 | -55.93433 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d42f0563-d838-3c45-a042-b25fd2c045c5 | -6.36296 | -58.2875 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fca225a3-5854-3235-9e4f-4e55a35bebd3 | -7.06266 | -63.05064 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83479ec8-96f8-354b-8963-1192b93a3d8b | -4.49103 | -55.49257 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22213a29-3392-3933-8d54-d210e40a46bf | -6.79085 | -59.17626 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 031fd857-b6dd-3696-88d1-fdef9e1a0f44 | -4.53096 | -54.92055 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3ddcdd9-1caa-3734-acb6-e1e9e702a672 | -8.7732 | -61.39497 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fac5c515-218c-350c-8163-d011996949fe | -6.89933 | -59.02603 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f00b4b0-079f-3d53-ac2f-ab21b7555294 | -6.32855 | -60.01126 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2da5baeb-8c26-3763-a80e-9fc45f365d3c | -6.12288 | -59.89049 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f3cc4f0-5278-3cbc-b6de-fc265382a79f | -6.90538 | -59.03574 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bf08775-29f9-3094-8ce3-c7e7f22bc9b6 | -6.90665 | -59.02715 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 159f5483-bd5a-3488-b1e0-88f8685fa725 | -4.88198 | -56.06686 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db5183fc-a8bf-39fd-a1e0-009220ae6a65 | -4.49037 | -55.49691 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ae01ec5c-f89b-30d2-b998-59332821fb9f | -6.79448 | -59.17681 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0569e29-3fe3-3f5e-ba59-3d77e573a362 | -9.4063 | -62.70979 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d84b55b-0a0d-3be9-9beb-989dedc01a90 | -5.85672 | -52.06354 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| baba96b4-f56b-3c53-acd7-7cd6075961eb | -9.59533 | -60.5179 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc97ac0c-d73e-3058-8b59-be4ac2fe2813 | -9.09502 | -60.96347 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49ecef04-e8e3-3681-8bbf-609844056f6a | -4.87827 | -56.06241 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56bf1c04-75aa-3766-bbf7-6f1c3d075c47 | -8.75243 | -66.5752 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8755fdfd-0f8d-3c7d-9f50-80ac2036b043 | -6.02881 | -59.93535 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7b19439e-5229-3959-847c-cd314af41c55 | -6.31452 | -62.67115 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8239ef97-44ec-336b-af76-6323632c9e2b | -8.64337 | -66.57643 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 974aea8c-ad65-3d25-8dd5-4088eb16b331 | -8.48467 | -57.63909 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a7c233e8-a70b-3f66-aa71-1c4886940506 | -6.90363 | -59.02229 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8eff1d1-10b8-3f97-8d62-ac8afa87626e | -5.15155 | -55.94267 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 765e115e-33da-35e7-bbc9-5d589bbbd6e4 | -8.07987 | -61.53106 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffe872e0-1e5f-3e25-a634-b134c23fa643 | -9.00814 | -57.13012 | 2026-09-17 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7062492-4719-3899-b03f-90d239d28632 | -6.93395 | -63.02713 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21e91946-ce4f-3a55-a27f-0b94749de1fe | -9.38423 | -60.31044 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e3332d9-8b0b-39b1-a445-54a96e54408d | -9.09391 | -60.99403 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 449bbf48-05da-331b-8a2d-6041f422eb2d | -8.65149 | -66.59615 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb8b01d6-d180-3225-bd48-bcf0e8d75856 | -9.2817 | -60.60899 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fdbb6b3-17f1-3d72-9934-28e5ec781735 | -7.06654 | -63.04768 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3a36cfa-dea0-3e0f-98ce-4ac18cdbdea6 | -3.72741 | -60.59536 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d543cd5-52b0-31ac-8bab-36951dd0a95b | -6.45809 | -52.83789 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef48ccc5-0186-3ac2-8603-920a8a9dc46c | -9.09335 | -60.99778 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60264413-7d42-3710-8f67-4f337d4f5b2e | -5.90191 | -59.94018 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c92001f-a207-393c-b59f-cf753402c077 | -6.83717 | -55.76197 | 2026-09-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6606faba-fc41-39e4-9125-5bbd4d223a71 | -8.54262 | -64.03419 | 2026-09-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6e9b860-6e86-37aa-9849-db273ea22e00 | -6.8987 | -59.03031 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3592d6b-1fea-3c3f-a4b8-27c550e816ae | -6.32738 | -60.01891 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0dfb42d-8435-36b8-9923-d413e74abc72 | -6.79874 | -59.17316 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2dec208-c11c-34a0-ae3f-b689925d5818 | -3.69673 | -60.62321 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cffe02e9-0b23-3633-b956-8add429eb64c | -9.10188 | -60.96453 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 484dcc7f-3a5b-3840-8de5-70cd6fb9fff0 | -7.99879 | -61.37529 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a9ba09e-9ec7-3a5b-a59b-ead6223be9f2 | -8.48925 | -57.63617 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 815ae693-4fb3-366e-a832-2632b15d5f59 | -10.72246 | -54.01176 | 2026-09-17 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e967d16d-8f3a-393f-8cac-692d7cdfd2f7 | -5.90943 | -59.93743 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 037008ed-6944-3334-980c-7c8987fab3f2 | -6.79811 | -59.17736 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a87f032-b0fd-3261-84cd-d78b165b872d | -6.80047 | -59.18634 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20eff63f-6a96-31fe-8024-d6f9181949db | -6.43698 | -60.01091 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e70c8593-bcf0-3a67-9064-a385e8503266 | -6.68238 | -58.8567 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 410d0e19-b4c8-32ab-bc73-53ee393da963 | -6.10734 | -57.63019 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README77.md)
