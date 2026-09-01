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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0f54e48-99e3-36a2-ba06-f612d67a1e3d | -4.14914 | -60.70001 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d619b32-5a7d-3741-ac58-907995158ec8 | -6.63379 | -53.17429 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf8081b-8e69-37d3-a890-23427758036b | -7.02494 | -55.63844 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9763c9c-4f8a-3a93-bcd0-6e8a9d05e109 | -6.76378 | -59.47618 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6e3f7aa-0348-3113-9bb4-72bb7553b5cd | -7.35185 | -60.5921 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82439daf-d80e-3e90-b051-cb432b0741cd | -6.88782 | -59.45025 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f6ad85f-58cb-3e83-a29c-e79e653c5789 | -7.57596 | -60.47432 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 017411a6-f26a-32c7-a530-f7f4f045e79e | -6.86215 | -59.46825 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b823757-9ff4-3277-80ac-c6e2d14b0b70 | -8.61664 | -54.78319 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e08051c3-2cf9-3f82-a6a6-cfd86e5819b9 | -7.52693 | -61.38131 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e096427-13f2-3b6c-9ea6-ab5c3d48ba6d | -8.76646 | -46.44463 | 2026-09-01 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc0db33e-9a7d-3ce6-af3d-81479e0f425b | -6.86808 | -59.4782 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68dd69fd-8f5f-3518-819c-16f264a02bc2 | -6.38742 | -55.21982 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e36ab21c-f81e-3dd1-923c-96f9eae29915 | -9.6743 | -50.85635 | 2026-09-01 05:16:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92e7c443-c8af-3052-a8d7-f3b917196f9d | -7.62706 | -55.2917 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ad064c6-3053-3109-b9fb-306bf1ac7966 | -9.2082 | -59.55585 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 097ab01c-3aa6-358b-bad2-88411111e800 | -5.87068 | -57.78358 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dafdff31-e8ef-33cb-943f-2b434b40e37f | -7.29202 | -56.68324 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e17e8d05-3d40-3abf-ac2f-4f5048406e1d | -4.95764 | -55.85091 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 921db075-f01f-3d3d-a8a9-6bfb218144f5 | -3.58589 | -55.60181 | 2026-09-01 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40826e47-a268-31da-bfbd-fb485eb6591a | -10.21304 | -50.32017 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3b517c07-b211-3ba2-942f-3b428eaebabc | -6.93966 | -55.6429 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04ff500e-4a75-3f45-9a99-80f5bda3edf1 | -7.48158 | -55.31254 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52d75059-1807-303f-8e6e-60bda047005d | -7.61927 | -55.29771 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4d0d5dd-d883-36de-a59c-6aed04c9c75c | -4.09178 | -54.09794 | 2026-09-01 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8c54b67-3b0b-38aa-8456-6cdedea6523f | -7.03327 | -59.22274 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df34f991-65a3-3c45-9e53-9a5fbd0a51ff | -6.9012 | -52.83183 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f0d3ae0-7b3f-343f-9348-1d6d77971fd0 | -6.02688 | -57.67783 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6b3ce871-9672-3821-b01f-380e1f191baf | -8.24279 | -54.94582 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5e9b0f9-2dd4-34a7-8344-5b8386611aea | -10.15185 | -45.74881 | 2026-09-01 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 289ea4e6-d393-3d7c-af74-22c57633c36b | -6.25173 | -55.43808 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d156f686-ae6c-3aaa-907c-6708d13fe1e9 | -5.85813 | -57.55604 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acbbabd0-c2e2-3005-9e58-49ef90e41632 | -7.55193 | -60.47536 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20e79642-d4e2-3f3a-b894-fa3f2ac4204a | -11.26399 | -45.10902 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d165d8a-aeb3-39ee-9122-193ea5c4e762 | -7.97365 | -52.08775 | 2026-09-01 05:16:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f962a857-5aab-3ce9-b078-a4ac3262b170 | -10.75066 | -47.98384 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3df3295-559a-3ddc-87e8-48949d26083a | -7.02162 | -55.63792 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2c6c46a-3380-3c2d-b5fd-a557307d4363 | -9.20808 | -60.90036 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b56143bd-4822-3fee-9b66-089b54848794 | -7.29123 | -60.61764 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb119fb8-bf8e-3b91-9313-b7fb9c02a2c3 | -5.96106 | -57.67471 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66011286-93da-33b5-93b0-96c743104f77 | -9.21793 | -59.76437 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b18c93a-30d4-3bbc-aec9-7ace28258c7c | -6.56421 | -58.5601 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e83199e-347e-3df1-a394-7d07bce5ffbb | -6.62193 | -53.18061 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69e5f12a-750d-3aa2-b704-96d8fe1b482b | -6.94131 | -55.63246 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2398de9b-85cb-3321-a225-d16780b268d9 | -7.57127 | -60.47861 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5eb4bca6-ff61-3c76-b7c3-eb33e3f474ce | -11.31379 | -45.17861 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 166f8c86-817c-31e3-96fd-fc4b0b609643 | -6.78164 | -55.67876 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57eba600-563d-3be0-8470-ccc9efb5c782 | -4.29712 | -49.10437 | 2026-09-01 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5bd7a9e-296d-31b8-a0a9-c057032e304e | -7.34261 | -60.5753 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9034c07c-5e2c-3c5a-bcf0-d5d1cd38fbe7 | -7.28344 | -49.82883 | 2026-09-01 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 632e247c-f096-3093-bcbd-382aa9129ad2 | -6.5963 | -58.58593 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9db7b10-b8aa-3a94-b919-386d6d2f9c47 | -6.91984 | -55.72531 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca846f2c-fb64-3ea2-a77f-7c66969d96fa | -8.61952 | -54.69705 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e7357be-0d84-3743-b966-805e9c709d85 | -6.21959 | -55.42588 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ae36ad6-0a12-321c-9c8e-3329c488fa34 | -7.62596 | -55.29877 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72e5e343-ed9e-3f35-b6cc-8fa6948c37a3 | -4.84015 | -54.82373 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63bf68e6-cb19-30ef-a1ae-2c23af02ce78 | -8.93695 | -62.36079 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3a7e6a8-3e16-3e9f-835e-8bcabab3b1fc | -9.47867 | -57.0244 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b613ed59-1fd8-3bca-9597-e9af0b97d208 | -5.87534 | -57.7766 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ce14091-7011-3312-ad36-1c508a2a8c3b | -4.2341 | -53.52534 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19b688e0-da85-3309-ac26-bb81b1e9d90e | -5.24195 | -55.89221 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 049790cd-3b69-3fe1-84dd-0abd797046d4 | -9.15115 | -59.53478 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3fda942-3e12-3d67-ad36-326955d09565 | -9.15337 | -59.54369 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40705c85-d060-3699-a6d1-04ca944d9487 | -9.14197 | -61.1003 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 335e375e-0068-3767-9d7a-db9d536ea682 | -3.11501 | -61.23668 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b928b47f-9bac-3554-aa88-4ab5c8348947 | -10.6878 | -46.25615 | 2026-09-01 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0effff18-9e9e-3404-b055-ae0da6a071dc | -7.92786 | -44.23563 | 2026-09-01 05:16:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13f4811f-9f73-3599-a857-3ca2a2b98bd7 | -6.95738 | -55.63857 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 13ab808c-fc52-3248-a27e-fd5a6cdd7e69 | -6.95683 | -55.64205 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| df78a45f-37dd-38ef-b737-22ecf2f5201e | -5.24584 | -55.91057 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f921b8bc-19b0-3981-8a0d-61946b6a876a | -7.52282 | -55.33339 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67a00626-688d-3764-80d4-4c99db3ce429 | -10.40391 | -48.22856 | 2026-09-01 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcf5a8d2-21c6-3b32-b8e6-35d57411f2f7 | -7.08377 | -45.80843 | 2026-09-01 05:16:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4429d0af-ec82-3099-bcb0-bb25de1dc662 | -7.18445 | -55.48475 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c22f733-c754-3097-9992-c03ab9bc1786 | -7.34772 | -55.20108 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3e72ce0a-ae4d-3054-b375-974ad3873a34 | -4.96373 | -55.85543 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6125c9f5-d7e9-3058-bffe-5452a209c7d6 | -7.34827 | -55.19758 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caafca7c-a57e-3390-8695-fe7daedaa54b | -7.28908 | -49.82087 | 2026-09-01 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43d1f5be-dcd9-3686-af4e-df119bbdcb68 | -6.14233 | -57.84916 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 556d77da-d006-3641-b3b9-af1eda4405ce | -4.79912 | -55.97527 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ac58260-95d1-3739-a03d-c2915b479302 | -7.54717 | -47.32282 | 2026-09-01 05:16:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 862240fb-e2d0-37c0-a8e0-8617d6cafc7d | -6.78767 | -55.64051 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45942e5e-43d4-3142-b911-094b483a6dea | -6.17956 | -57.7286 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0d1536a4-0c1b-3840-b781-b4f80c664617 | -6.56068 | -58.55951 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9461a7b1-c805-3e9b-a64a-c71999cf5db6 | -5.87189 | -57.77607 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8c1f4e4-346b-34bd-bb05-0dc386e11b5f | -8.12406 | -54.96777 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec6fb239-1761-309f-8642-7280e7d9e174 | -7.56679 | -60.45795 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2847a683-38fd-3a5f-a8e9-0f66f427f8a1 | -6.3863 | -57.46609 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fda85ca-7537-3fed-be96-68a8f356f99d | -5.96389 | -57.67896 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 222c2758-4eee-3305-8b35-5e904e4f48fa | -6.77335 | -55.66969 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8fd0c94-fb2e-3c81-b941-3c7fc837e42c | -7.53041 | -61.38563 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee55118d-f419-3dd9-a335-3b80e962437a | -8.71406 | -52.36742 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5bd73473-8051-3f57-82d1-14f93fc67fd9 | -7.62037 | -55.29065 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edc6bbd3-5fa9-3d3d-8578-21c18a917aab | -10.75497 | -47.99168 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e536c18b-e515-3246-bd84-832d8d2aa3dd | -9.46592 | -57.01875 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b802e8bc-8248-343f-9dd9-1697fbe5944f | -9.40423 | -51.68568 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d618d887-dd95-3bc3-af75-42156d4051de | -11.01245 | -48.3829 | 2026-09-01 05:16:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6977e179-7309-32fc-8dcd-1892564a9172 | -6.60788 | -58.60411 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4d3dcfe-5562-3fc7-89c2-8b2ff0137f63 | -6.93856 | -55.64986 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d0772ec-9baa-38b5-bc88-890477f314de | -7.52172 | -55.34044 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README59.md)
