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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1aaf635-3c91-340e-ae75-39cc67fa81a8 | -9.33126 | -55.21682 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbd62fc0-3474-39ee-94c3-2517301bf61e | -12.92818 | -57.00343 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15fec8e9-2467-3ca0-b582-d8948c1bea18 | -12.9327 | -56.95015 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37f028aa-3f16-3f18-a9c0-da59597a9de5 | -11.58678 | -52.13253 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 5866652e-aa8d-3ed1-b38a-2048cff54849 | -12.89385 | -56.95168 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9eccc07d-422b-38a4-aec8-8b1e4994532a | -12.94473 | -56.98678 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c13360ec-ee5a-3628-86da-e844638de28b | -11.81061 | -50.63558 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a24241c1-1558-392f-9e32-395ef5f6ee18 | -11.64099 | -52.05801 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60c08d44-84f2-37a7-b486-2c02dd6d601b | -8.08288 | -47.59906 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7662fcc0-962e-37d2-8947-037d78fd8ddd | -11.4763 | -54.6188 | 2025-09-03 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73f50579-7713-369b-bdfd-bc8e0e2b8515 | -11.90453 | -50.6212 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 608bfb67-9817-34ee-a249-7b8fd0c13d8d | -8.37014 | -48.31244 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c5917e3-cb91-3073-9a18-37da70ae648d | -12.8814 | -48.03344 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60fd3d14-dc6a-3e24-9e8d-6bbedc053290 | -7.7691 | -61.1998 | 2025-09-03 05:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f2b3767-2e65-3110-92c2-370fc47b838b | -9.33482 | -55.21733 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aae3acc9-7d43-353b-9baa-e3b4b37e40d1 | -9.13856 | -49.64225 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8a3c3a60-ba25-30a4-a3e8-ef10fb3cfa46 | -12.92354 | -56.94094 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6d7cc87-f87f-3ee3-9a60-f9353e603fd8 | -14.56567 | -53.04915 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dfd18db-6e67-38ce-ad4f-d7a512e155a8 | -11.53333 | -54.40785 | 2025-09-03 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff47e768-d6f8-38b1-b401-b439393f5c18 | -15.00176 | -50.05853 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 166c8cb0-0f6d-3743-bbc1-328e62f02303 | -14.78106 | -47.51454 | 2025-09-03 05:14:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea4a981a-3c7d-3acd-96e0-b74dd5a265ee | -10.5406 | -50.44094 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6789620b-fb3d-338c-84b1-791190cdc704 | -12.94471 | -56.96365 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ab8b9e6-a2ae-34d4-97b8-cfec0dcf52bb | -12.63966 | -56.9982 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e54ec8d5-125e-3a08-882a-b0c4a572853d | -11.59737 | -52.12076 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 62627a5f-bb95-3b1a-b687-c5a968ad554e | -11.21712 | -55.069 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5873ff6d-7fac-3bd0-9247-01ec80f341f9 | -12.99568 | -48.09284 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7879628-adba-3c93-9f63-2414515a25c6 | -9.62541 | -47.07061 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f98c00a7-fd1f-3873-9378-2f4c31a690c2 | -9.34722 | -55.23153 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1af3426-c2b9-39e7-ab54-9828f839e138 | -11.85215 | -51.41328 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e983791e-06a3-3dcb-afcd-2e348d754f4d | -8.88702 | -45.83316 | 2025-09-03 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 146bccaa-35a6-31e5-9b9d-1d3cb26b4e25 | -12.91505 | -56.99749 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efe71ff2-8485-31cf-a1e5-d57136155049 | -7.69786 | -50.26532 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81d95472-93e0-329d-a1ce-c21f9cebd3dd | -12.91848 | -56.99805 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 373925f0-5c22-3578-896a-ca707d8717df | -10.24897 | -61.76525 | 2025-09-03 05:14:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a4403c9b-54ae-3869-bce8-ad14ead3c53c | -7.70802 | -50.29974 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3dab27e5-5442-33ec-80ba-f1818948a11d | -15.02255 | -50.04489 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e491cc7b-54d2-32b4-844c-db9c1176c27e | -11.868 | -52.4311 | 2025-09-03 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f9d4d6f-abef-3a4f-bb0d-8b023715ad64 | -14.81082 | -48.37777 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7d47ec6-49c2-3fb1-a2bb-b94e12acada1 | -14.57969 | -48.05323 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da2c8070-4e55-3c57-9654-f35210a1e25d | -14.83397 | -46.69856 | 2025-09-03 05:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cac62ed5-7017-3d64-bb08-408323e13a21 | -9.99575 | -46.8885 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8779bf2-ad0b-3365-b986-48672bee3a4b | -10.14754 | -46.27834 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 893a5580-685f-36f8-b207-ef047f0a782c | -9.09051 | -58.89167 | 2025-09-03 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34536834-b2e0-35dd-a6b0-7fed2a50770d | -12.51352 | -49.56832 | 2025-09-03 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0e2bbe6-2e01-3e99-a23c-b0a0923c59a6 | -12.02949 | -50.59346 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d5032254-7499-3bfb-bcbb-3142cd366dbe | -12.97758 | -54.76957 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c6fb2a8-5d5f-370a-b38b-5d1ba0ee7b6c | -12.90526 | -56.94578 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b8bc0ff-3f32-3b62-a456-09917057b564 | -12.94815 | -56.98732 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 70e3385c-d942-34a7-805f-9679843e6faa | -11.31299 | -55.22573 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71d9badb-3b5f-37c7-8e9b-b51c447ea1a2 | -14.78097 | -48.15152 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30bea18f-75fb-3813-9d2f-c86fc053f586 | -12.18221 | -53.89124 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdc23b1a-bafa-38ff-a8c9-00e9cb6c9344 | -6.75841 | -56.39478 | 2025-09-03 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19dd3d2e-efe4-3a95-845c-d9c8131a5709 | -11.00803 | -46.93533 | 2025-09-03 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 208bdabb-eef7-3970-895f-8ff83333f751 | -10.45278 | -53.62307 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 141cd2d3-d2bf-3417-a856-d2ca773af19d | -13.31323 | -51.77113 | 2025-09-03 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05244196-65a7-3b84-bf07-e3d190a1072a | -9.63343 | -47.85471 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1a13630-0415-3bcc-981c-205e6df08aa0 | -11.12041 | -44.63868 | 2025-09-03 05:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 518447da-4cd9-3a15-b294-cd8ea1bf0f5a | -11.60452 | -52.06824 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d2784ce-d1c0-3168-bb24-527ad0d60966 | -10.48872 | -50.33316 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e79e3062-0f70-3768-abe0-fecaee622005 | -9.76796 | -46.92249 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 437e0aea-40b6-374e-9d4e-27bd4a807048 | -11.64658 | -52.04983 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce24488a-8fa6-3750-b394-b4f760da8a56 | -15.02441 | -50.07547 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c05f2e4-9ff4-346d-b724-7aa7bb5d99e7 | -13.69146 | -46.9559 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf022530-8c74-3eac-b2e1-99189fb81efa | -11.67196 | -57.35439 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 74305406-17f0-346c-ba6f-ca6aeaf39948 | -8.12819 | -55.55806 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 325d617d-9a89-3e2c-bdef-4cdc4da3080f | -11.58971 | -52.11093 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 189b5263-7f98-3e30-af39-3c485bad0da2 | -8.07483 | -47.60763 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5055779-3a77-32a5-a697-c1798479d25c | -11.87347 | -52.42344 | 2025-09-03 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8aff78f9-3e81-3344-93f7-684676552fc1 | -6.44586 | -58.13762 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b641d0f8-104d-3ebe-9e4a-3fc295206c24 | -10.96604 | -50.93016 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5b675a4-7487-34ca-80ce-c3d7c081bf65 | -13.28428 | -46.83626 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42c91fbd-e2ad-3203-ae6a-7d73f806dbdc | -13.49349 | -47.01965 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51727c4a-d27d-353e-bd28-dccb12631680 | -10.24527 | -61.7646 | 2025-09-03 05:14:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9ed1fbab-3e10-3c25-b6fb-31e4e6e6cac9 | -9.77449 | -49.97588 | 2025-09-03 05:14:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7691d364-ad50-377a-8b03-168058a8c423 | -11.21585 | -55.07753 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de6578eb-67bc-32a7-b4fc-75a3ec848541 | -9.96 | -51.62785 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9638617-187b-3770-bfee-a2242cd3fd9b | -13.71273 | -46.93894 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 380b96df-7e99-32b8-b84d-5e4ae31d920a | -12.91678 | -57.00932 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e2050dd-8734-362c-8eed-67fb9fea748c | -14.57228 | -48.06481 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f6cb6b6-7a8c-3aac-91e1-56a252569635 | -14.8337 | -46.6899 | 2025-09-03 05:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d5e32fe1-71ff-364c-8192-4e4ef4ef779c | -11.02745 | -51.48419 | 2025-09-03 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7854d0bb-08c6-3789-91c7-26947ce84cf3 | -14.7842 | -48.16361 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5f1a2c0-d125-33b0-9d7a-e0532894d332 | -9.63334 | -46.12141 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0eeb10fa-808d-3c67-988c-7ee667a6853d | -11.91089 | -50.61079 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1afb595-109e-3fc2-9129-40cb1a2207e8 | -12.99763 | -48.09143 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94279101-4b8f-3357-a03f-30e76ed05f28 | -14.57479 | -48.04258 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc0530c5-ccc7-355d-ad99-e1010eea81f9 | -14.6078 | -48.02139 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68cddb56-c7a5-3fe8-9cb6-9e9b7ebdecd2 | -15.00255 | -50.05202 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fdf77e89-9238-3f95-838a-c6b433c795ef | -6.67469 | -58.86229 | 2025-09-03 05:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a56988cb-cdb6-3ce2-a7c6-0359df2e607a | -9.63267 | -46.12676 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d889c14-f56a-38fc-8b08-ad309f4189d6 | -10.44958 | -53.61742 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 60bb1a74-58e7-37cc-bbfc-7e42afc12015 | -8.43402 | -45.08729 | 2025-09-03 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83fe95a7-7f52-3c53-9643-93a194310631 | -10.95272 | -50.7705 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7160098d-c726-3226-a23c-e6a0f84d9dc9 | -8.06107 | -52.36381 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f765429c-4f80-3475-a9e4-d594535c007a | -11.6062 | -52.12198 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0bd8310-0b30-364b-9b5a-0513a3a39a4e | -11.59951 | -52.07192 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fa89d0d-3fd5-3873-8eb5-c962a32d8892 | -10.14417 | -46.26262 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 376c4687-fdee-3cb6-a951-75114f9b9890 | -11.6714 | -57.35802 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6d27ee1-ee1e-353d-bc13-b8c4545e8745 | -8.0958 | -47.58904 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README94.md)
