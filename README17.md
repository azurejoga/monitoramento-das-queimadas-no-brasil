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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8152028-950d-380b-979f-ccfd6d103c86 | -12.58023 | -56.97423 | 2025-07-23 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbdf6e16-71be-389d-a7b2-d4e664c5b5b9 | -13.6554 | -45.71716 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3d60787-0e68-307a-ad38-88272ae1e52c | -12.28962 | -50.27487 | 2025-07-23 05:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3175a756-3130-30f3-8bfe-fc2f87e74276 | -10.04217 | -59.09645 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c590c56b-0cac-3a9c-9a00-14d203d2a4cd | -10.04279 | -59.09906 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a3f7ddc-77c0-3a73-8ab4-f3709fec5dba | -13.72092 | -45.69786 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e4ce0f6-76f0-3b8c-9b2f-cd2d663d339c | -13.70125 | -45.69184 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ce2346c-9e64-3f54-afa0-ae7cfd1c7ba4 | -13.72018 | -52.01051 | 2025-07-23 05:01:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2ef0910-d4bf-3870-8c7c-7b5b286cc0cd | -13.72139 | -45.69392 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b02e324-c7c8-35ff-bbbc-12b16b870a75 | -13.64931 | -45.72015 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64f49fe2-dc4f-326e-9cec-92cde713c17c | -13.70691 | -45.69258 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e63fa96-3205-352a-bb5d-415457fd7b6e | -10.28696 | -60.53173 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 714d3cde-016b-3d08-a49d-00357883f323 | -12.50488 | -57.77274 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd104b47-5317-3409-a53a-c8861805f3c0 | -13.71302 | -45.68942 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89c28faa-7b48-3de3-9a5a-f23bb4c4434a | -12.35336 | -63.41283 | 2025-07-23 05:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 810f9157-0608-3f4a-a9be-bcd5684cb7a5 | -10.29391 | -60.54084 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49ce65c3-79d8-3330-9ccd-32e70c18a782 | -13.53907 | -43.71137 | 2025-07-23 05:01:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7ac8b58-08d0-3219-9b10-a8aeec44b869 | -12.41592 | -57.4823 | 2025-07-23 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90d435f7-d753-3e81-9501-d323f347b8d5 | -13.70439 | -45.69175 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4182b3cd-0132-3fcb-ace0-a2bcc816bc7e | -12.35717 | -63.41921 | 2025-07-23 05:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 37f9048b-85c0-3de4-8bea-a67bafb5705d | -12.50425 | -57.7766 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62388bac-1f06-34fb-9065-bf816145140b | -10.062 | -59.09498 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4d5f230d-53e1-3c16-849b-9cf50753b4ed | -12.49386 | -57.77479 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1da8a73-8090-3ac3-a520-e860060d4e47 | -13.71869 | -45.69017 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3084c012-6d34-3402-b64c-59c7f023717a | -10.06119 | -59.09967 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8108a6e6-2fb0-36f4-b644-7004c3066a2a | -11.73048 | -49.71251 | 2025-07-23 05:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbf6a1bb-c22a-3922-8b0b-4ee8d240110d | -13.70298 | -45.70353 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8fe6293-127d-34cc-9744-aae9afaa4162 | -13.71258 | -45.69335 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30535074-c4e4-318d-94f6-59afa8f62a3e | -13.70959 | -45.69641 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a12a5d59-99fd-3ce2-81fa-91661129fe1d | -13.69259 | -45.69425 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa628aea-8592-3117-bd52-9919fd2bee31 | -18.39325 | -49.2942 | 2025-07-23 05:01:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5444f2a-cf4e-3736-9e31-24e25952c50c | -9.45994 | -63.15256 | 2025-07-23 05:01:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61af0cd3-e11b-3819-8f10-35ab342b2f67 | -11.79012 | -57.24738 | 2025-07-23 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb9da435-8ff4-33f2-ad55-aec927f095a7 | -13.54053 | -43.71237 | 2025-07-23 05:01:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6badaff-2746-3965-9a5a-21c16127ded5 | -12.50834 | -57.77336 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9d0d97a-8a9a-31e1-8038-c05b5e7ef3a9 | -17.78612 | -52.43573 | 2025-07-23 05:01:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 085b53f1-0af8-33d4-a666-519e82fa663c | -17.57186 | -47.50965 | 2025-07-23 05:01:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d42c3f6-b28a-3835-a91c-d911bc34760c | -13.70603 | -45.70044 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c39cfb89-3ce0-3cc8-82f0-804e827868c4 | -10.03358 | -67.74776 | 2025-07-23 05:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97c9643d-1a61-3107-8f28-c551d1ad8928 | -10.03977 | -59.09371 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d7f3906-5dfb-3c41-86e9-c98bccc4626e | -13.71572 | -45.69323 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48643140-a861-3c10-8bca-8de5f10490ae | -10.3607 | -57.50204 | 2025-07-23 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| af64da13-015f-33a1-8ee8-e7e0e64c3cf1 | -10.03836 | -59.09581 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15f89e33-48e4-3ec3-95ba-b9bebc9289f7 | -17.57222 | -47.50636 | 2025-07-23 05:01:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 537b3e48-edbe-3e9a-a4e9-7e4c1e0a6d29 | -10.04978 | -59.09775 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 783740d7-5be9-30f2-9be4-8ae98041cdaf | -12.35133 | -63.42365 | 2025-07-23 05:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e279fbef-7302-3d38-8c11-ff3cf12bf6d4 | -13.69778 | -45.69889 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf10f226-0dc6-3484-bbfe-4de9b346c332 | -12.50142 | -57.77213 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c22afbd-dbe5-37d3-b2fe-9c4ceda82524 | -9.46101 | -63.14675 | 2025-07-23 05:01:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b5bf172-eb6d-375d-be41-c00efe291650 | -13.71169 | -45.70118 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82d51bed-12cf-3da5-9edd-705692d0cd0f | -12.66497 | -45.04143 | 2025-07-23 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f726ab49-85ca-32da-9f98-95f9cf188dbc | -12.67723 | -46.83094 | 2025-07-23 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d67c2107-72b2-3881-a061-acbcb6b70451 | -12.41539 | -54.18899 | 2025-07-23 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6410175d-efe4-3840-b5eb-d047ceb532b0 | -11.88489 | -52.49124 | 2025-07-23 05:01:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4deb879-8078-33af-9a97-41ddcff9060b | -13.70036 | -45.69971 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fd5c32e-6c63-3ebc-b62f-d7518991a275 | -17.56659 | -47.50887 | 2025-07-23 05:01:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cef295a5-ae20-30dc-a9ae-e691d9c2c6ee | -13.65495 | -45.72103 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac258d8f-4123-3bec-a151-c73826bc689d | -12.34649 | -63.42267 | 2025-07-23 05:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d42bde5f-92f7-3140-ab19-090258950970 | -14.64737 | -46.83197 | 2025-07-23 05:01:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f40d20c-a41d-3e72-a0b6-8a96c577eb62 | -12.28553 | -50.27428 | 2025-07-23 05:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65291579-2e4b-3226-b7b6-e26bda2059e9 | -12.4986 | -57.76769 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6df25c1d-245d-3c76-b1ad-b6bd2e84edf4 | -17.57151 | -47.51287 | 2025-07-23 05:01:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4668371-3c32-3cb0-b72b-26e00721655c | -12.68241 | -46.83163 | 2025-07-23 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a2db21c7-f1b4-31ba-8028-10d5b77461b5 | -10.0582 | -59.09434 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2290b3c4-091f-3b96-9382-3418d964d454 | -13.70912 | -45.70032 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4725633a-c824-3e15-a6dd-9b65bbf9889b | -17.1299 | -52.69515 | 2025-07-23 05:01:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6bb5227-be97-336d-9df0-e718bd4a28fb | -10.29109 | -60.53252 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23c80769-cf97-3631-ad05-33825610c582 | -17.78463 | -52.43386 | 2025-07-23 05:01:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83c2c90a-cec8-358c-9d48-b6fe56efbc4d | -12.49732 | -57.77538 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49594ba2-fa98-3b99-9194-c50fac65101e | -10.29805 | -60.54161 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35834f93-4c06-34b2-bd24-0c5eead7a74c | -10.36005 | -57.50597 | 2025-07-23 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 898968a2-bd50-351d-83f5-f83f34606346 | -13.7178 | -45.69802 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac0dcfbf-b770-35eb-9254-9b9df242e67f | -10.69192 | -55.13725 | 2025-07-23 05:01:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 866f2c83-d243-3fb9-bce0-71edb192f4fa | -10.02697 | -67.74637 | 2025-07-23 05:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75518d83-ed9a-3c57-ba66-364b4b47aa4b | -13.71053 | -45.68858 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a43b781a-d45a-364d-8f00-dd45c6fc5d9e | -13.71525 | -45.69715 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b6e2394-079e-3c2d-9b70-0be751059997 | -13.71214 | -45.69727 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da946a62-b24e-367a-94e7-7d50527e2378 | -17.56166 | -47.50487 | 2025-07-23 05:01:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 680a872c-453d-3264-92ba-d3d3efd7b31a | -12.34751 | -63.41726 | 2025-07-23 05:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 848f4c8b-94ae-35ac-87d7-3824ead7ec5d | -14.64698 | -46.83532 | 2025-07-23 05:01:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5212bac7-5641-36df-9e9c-513cc0df60ca | -13.70345 | -45.6996 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a09421b3-37ad-3260-a96e-3cf288c0e90b | -10.06499 | -59.10033 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1beaad4-1073-30c7-af19-5c5e023e10bc | -10.93048 | -56.84211 | 2025-07-23 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2df7e9eb-f9c1-3db2-8e20-6ce2c98e6a8d | -13.7162 | -45.68932 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57dc5bdb-01d3-351a-a021-120c3cdcd192 | -11.7389 | -49.71371 | 2025-07-23 05:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 458128d8-9bba-3dc6-bf07-1557a4a14d86 | -18.39434 | -49.29153 | 2025-07-23 05:01:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b45be02-87c1-316c-9aa1-3fa6c6fe8005 | -10.03898 | -59.09841 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c0c8f7e3-b529-38c8-80ea-f613ee8bdc30 | -12.57746 | -56.97 | 2025-07-23 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac25d4bd-bf59-3474-9963-df695e8d4f30 | -12.65959 | -45.03677 | 2025-07-23 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4d72ada-af2f-3252-b3b0-face0c04b5de | -13.54111 | -43.707 | 2025-07-23 05:01:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82d4b102-61f3-3da5-bdcb-f907a722f4b4 | -13.71006 | -45.69249 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f09a850-8272-330c-a535-cb9db478ded0 | -12.50552 | -57.76889 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af7bb40a-6518-36ae-8362-8d0e6a069cd5 | -13.64886 | -45.72401 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9da06af5-dcde-3e7d-8d16-c532b6f4fe80 | -13.71825 | -45.6941 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 867046f7-8022-3ff7-bc93-6fb23e24cab3 | -19.77495 | -55.35353 | 2025-07-23 05:04:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f86db1c-3aae-3664-a5bd-8b3f962cfd9b | -20.29359 | -54.07807 | 2025-07-23 05:04:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e4d0567-d789-352c-a460-34f39c56cda5 | -18.65994 | -55.73045 | 2025-07-23 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 72cc51c2-37a8-392b-aab0-1f65208a5b65 | -22.15743 | -52.68287 | 2025-07-23 05:04:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b14faf38-2e9c-329c-9fa3-bad4f4f6dfd2 | -23.25602 | -52.19202 | 2025-07-23 05:04:00 | NPP-375D | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 77505680-1ee6-3a58-bf5c-c041950bb0fe | -20.64584 | -56.54942 | 2025-07-23 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README18.md)
