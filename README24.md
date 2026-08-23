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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 441a0b30-ddbc-3ed8-aa50-cc979fc171fb | -8.09116 | -50.05416 | 2026-08-23 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8a4b93d8-0ed6-3e01-b42e-e49baaa10abc | -5.77917 | -50.1907 | 2026-08-23 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50c0c72d-4242-3ca9-9449-b358063034bf | -8.9284 | -48.53719 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a862bf0f-34f5-39c6-bd54-f3a42938d825 | -8.16274 | -46.71682 | 2026-08-23 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d4cd608-7db8-34aa-8fbc-13d4c923057a | -6.6628 | -58.7398 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| effa51c6-c25e-3287-9f7f-0adb88d638fa | -9.74605 | -43.30529 | 2026-08-23 04:44:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 95dfb0aa-7447-38a2-887f-9ab262315d37 | -6.80891 | -58.64717 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9fa71f91-293b-3a1f-a352-3966651dd3d5 | -4.30639 | -46.41626 | 2026-08-23 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cca95bf-1427-3ee7-acf9-1ac3c4909f49 | -6.78366 | -59.43091 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b833296-d799-31c7-834c-3b4550550045 | -6.67606 | -58.73371 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6c65d44f-cacc-3307-99dd-51dc5f0b4cad | -5.77398 | -57.57392 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3696a1a3-39cb-3b7d-8e75-e353469d3a1f | -8.46228 | -46.99388 | 2026-08-23 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c151337c-3079-35e9-b758-94d9085cae93 | -6.78604 | -42.68159 | 2026-08-23 04:44:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e54a7117-3af8-3005-af6d-e84d8368cc01 | -6.39008 | -54.95679 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c7f0639-d253-3371-bcd1-2976d3e0c608 | -2.89173 | -48.79488 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ae1f2d7-edda-3879-a428-bee231813899 | -5.95875 | -51.952 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f796f11-0111-363c-bb21-e3bda03c8e7c | -8.47923 | -46.99638 | 2026-08-23 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7071e6c4-8c36-3132-b732-5996cdf9e511 | -7.0869 | -45.00642 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff379ad2-2d88-3637-b11a-31bf50efbae2 | -5.28903 | -44.70411 | 2026-08-23 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d49e6fc-0d09-33a7-aab1-58de7247e5d1 | -6.69391 | -58.72411 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f3fbb4b-d527-38c5-a68f-c1d6c2fb1f05 | -8.92175 | -48.53613 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3321847-46fe-3c11-99eb-a84678b7306c | -6.79131 | -58.65511 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb9d6865-c96f-358a-877a-6354f3849a17 | -6.81131 | -59.68205 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e0ed3f2-c136-327b-a5d2-6b6bd39b1764 | -6.66869 | -58.74094 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| d4f4efd6-305a-3d6a-9ed5-b278edfb4b60 | -2.35513 | -48.83157 | 2026-08-23 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f547ad8e-6c17-345e-84e5-d0caec34590d | -7.18128 | -55.42287 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fe0019c-a7eb-381b-b109-9fd3707744d2 | -6.80813 | -58.65139 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7baf5409-718c-39c1-aadf-fab68069877c | -6.67974 | -58.7473 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 257e7394-468e-3171-9b64-da9c73d6aed5 | -6.82412 | -59.66387 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 49f0fa77-f784-355f-b875-7894d6411cd7 | -6.69076 | -58.74121 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 956ddc48-1629-3644-83bb-9cd8460fa01e | -7.29689 | -42.97692 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 58bf6fa0-4799-35dc-b2c0-49154cc8232f | -6.87609 | -59.40541 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8b7911f-09f9-3fc1-b14c-e3544e569233 | -6.11681 | -59.92949 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fd19203-7763-33c3-a15c-bbf608f5ce4b | -6.68055 | -58.73056 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4f8e2f1e-a5a4-329f-b6c2-a85e4005094c | -6.89743 | -55.70366 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ff0fafe2-e571-3896-9624-747200864841 | -6.87585 | -60.01184 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b67ebd1c-defd-3865-9ef3-fd67cb7ece9c | -6.67234 | -58.74198 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| ad80e436-2f46-3aa1-a6a4-2c6738dc4b5d | -6.9662 | -59.05562 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ecab4e9c-d8a1-34bc-852b-53170b47a156 | -6.86215 | -59.41214 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dbba97ad-71eb-3f2a-8188-5e8feeb42dba | -6.37337 | -54.94394 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8faff3a0-b050-3d45-a8a7-84d012d526ef | -6.86855 | -60.01567 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dc75f65-8b49-32cf-9466-20f5eaf66add | -6.80138 | -58.98864 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb8a658e-5b94-333f-81a9-33ff9ed1a4bf | -8.0944 | -51.65974 | 2026-08-23 04:44:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24eb17b5-f13c-34be-a3df-7e31f82aa923 | -6.70339 | -58.73875 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bfc1f52f-cb0a-3abd-94b3-663fdf1f4868 | -6.20569 | -53.08925 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aeb0f842-98e5-3c6e-b0c8-9462c2017f90 | -7.30181 | -42.99992 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0e9ef373-2e0e-3504-a726-ca531df88266 | -8.09738 | -50.05893 | 2026-08-23 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7094fb81-aa63-3bdb-bd0b-6aaa3adbec23 | -8.92452 | -48.54015 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 876c2337-6f69-3d94-9f2a-bfe78ef3de24 | -6.79072 | -59.42707 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6e2a213-a7f6-3532-b9cb-7b3313905a14 | -6.97055 | -59.06561 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fac778ab-1c16-3015-80d0-e3b5d90d9c28 | -7.26173 | -49.9104 | 2026-08-23 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 676cb7fe-5567-390c-bc5d-9c3d863e3be4 | -6.6886 | -58.73161 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 89924d4c-d5c7-3af0-b91c-d4f2662befdb | -6.55349 | -55.10557 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 841f1677-3145-34b3-ba7e-cc759488ea7a | -6.77971 | -59.66015 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cd7490f6-c418-3dea-9d38-0bd4a9f5cebe | -7.28495 | -43.00104 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aba437c7-765a-379f-97a8-5b16d97c5c39 | -6.66717 | -58.74948 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e8e0cbe6-8109-3f0a-87c7-143d03a188cc | -6.19132 | -53.50722 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfbf92a8-93af-304f-8708-de9bd9b16e84 | -5.61868 | -45.70306 | 2026-08-23 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5e7c92f-eadb-321b-9b5a-0a21f4c7c6ff | -6.95093 | -59.07122 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6c566be-1981-3cd3-9aec-dc092fff2577 | -6.68047 | -58.74315 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b222bfc4-c527-3014-99fb-6cf26da3d1aa | -6.36982 | -54.94507 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f194e0d9-c823-3b76-b00d-65c34c57f8f0 | -6.8074 | -58.6666 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9f5578cb-ab68-357e-a648-648676b2b0f0 | -5.01877 | -47.06598 | 2026-08-23 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57185fac-523c-3e4b-ada9-a9e1f6c3fb27 | -6.86624 | -45.98134 | 2026-08-23 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 977348fc-3e30-345b-966d-c344f31d03df | -6.6124 | -58.38961 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7be21ba8-d128-38f4-92c5-ab842705e9b6 | -7.30098 | -42.97758 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20393f05-7996-3f85-8f90-ba4e4e5914ab | -8.10139 | -50.05578 | 2026-08-23 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26e9a009-ef6e-3267-8fda-3663d0d95ecd | -8.08941 | -47.2605 | 2026-08-23 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 46bb3e1a-75bd-330f-a6ce-1ad1785ec801 | -6.93696 | -59.07205 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9acd1ad-4f39-39f5-b36f-25bf95d52a62 | -7.64444 | -42.72657 | 2026-08-23 04:44:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b7868dd1-15e2-3dc8-a5ab-c31a24be854c | -6.67899 | -58.75154 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b759b6b9-db39-39a3-bb6b-32f6358b2d49 | -6.93617 | -59.07646 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3a7b0fc-999c-30ef-86e1-85925c1dc1b2 | -7.10459 | -59.77499 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf4259ad-2693-3b9e-aca3-5aeeb91219ab | -5.77853 | -50.19459 | 2026-08-23 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 883e59d6-0ea3-3fd1-a11c-909bb1a35562 | -7.47404 | -45.13172 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f121f7c-ea53-3189-b0cb-1e49c1d18172 | -6.69746 | -58.7379 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c4af22e-f426-3361-9f5e-18b1f8945943 | -4.96768 | -56.27398 | 2026-08-23 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 34c0c95f-9bc3-3dd3-9de3-2ee38638fd49 | -6.76913 | -59.44519 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8042a19-ade5-37a2-86e0-19a7eddeba87 | -6.88253 | -59.41047 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aab5f04a-da71-3158-b270-20126f8eefdf | -6.79486 | -42.67921 | 2026-08-23 04:44:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f6356547-0b64-3c17-95c7-351a6ee1557a | -6.68195 | -58.73484 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2a7b5136-87b8-3bb5-bdd7-5dc35999be35 | -8.17448 | -44.44144 | 2026-08-23 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f546f91-a263-3bb0-934f-69a8a5b23441 | -6.37581 | -54.96582 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03cac802-6b6d-3116-8f16-30fb93df8a1f | -6.80907 | -59.67583 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c145f9c-cfde-33bc-8529-39dd4d7e2fd6 | -7.03312 | -48.02441 | 2026-08-23 04:44:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9df21b7-4eb3-3708-92b5-d4805b04bb74 | -6.79944 | -59.41424 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fe124ad-7e20-3d61-8980-90582f631153 | -6.87396 | -60.01221 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8600f6a8-eab4-3a14-8d55-5302c0d7d033 | -6.80031 | -59.40953 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c4e6399-7930-3b4e-9ad5-056b61600a26 | -5.26964 | -48.21645 | 2026-08-23 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04d14a9f-8603-36e0-8bdc-a0ca47bcd386 | -6.38201 | -54.95716 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 012e5d9c-056b-35b9-8d65-a14524d2ba29 | -6.75757 | -58.67453 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb32e5d1-8042-3e48-8089-aa21941d90a8 | -6.68644 | -58.73161 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b0499419-19bf-37c1-813a-7e67760546b5 | -6.54621 | -58.52483 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f4519a5-7ca3-314f-b5f4-3d023fa983a7 | -6.68634 | -58.74442 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8140d730-489d-339f-bc6f-208adf13afa9 | -4.31406 | -46.42072 | 2026-08-23 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aa7137a-d93c-3a9a-bbee-00dd2ef87124 | -7.18103 | -42.74942 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c9c73e49-5218-3d51-896f-199f451b2def | -6.8023 | -58.65024 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 563ceb33-6a3c-3a44-a673-379ad0aa3f91 | -6.55421 | -58.51389 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1253582-89fd-3cd7-ba20-4431a3eded83 | -6.19607 | -53.5308 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7b818d46-5dbc-3a7c-bfe7-1b8e45c3d34c | -5.00413 | -56.13453 | 2026-08-23 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README25.md)
