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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5ac783c-4182-3839-b0b4-768c653ea11d | -9.05648 | -45.42089 | 2025-11-18 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1110e133-7f06-3e94-8b0b-1c31f6bcc555 | -12.88674 | -54.75543 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70f0460e-6b17-3675-aea4-3b57773df6a3 | -12.01717 | -46.76441 | 2025-11-18 04:50:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8e6c263-98d2-3634-b72a-ea2096017cf1 | -10.62778 | -49.02299 | 2025-11-18 04:50:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b177e9a-d447-336d-962e-fed79abff30e | -7.43215 | -48.93782 | 2025-11-18 04:50:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df8eafd8-5df2-3212-b2fc-0769735d2005 | -10.36011 | -48.91929 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ea27b48-2aa7-3433-ad85-692a24dc2a7b | -11.28784 | -48.51499 | 2025-11-18 04:50:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de29b190-a0ca-32ab-b1b6-57d09bdaf2c9 | -12.63537 | -48.8705 | 2025-11-18 04:50:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5696ab0d-1200-344a-a04a-ac640cc8ec5a | -10.87751 | -49.54415 | 2025-11-18 04:50:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bef2455-fee3-312f-8417-63e3ebf713b1 | -7.43259 | -45.20004 | 2025-11-18 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 531175d6-3246-3e51-9d29-e8b36407a68a | -6.72439 | -46.31905 | 2025-11-18 04:50:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f604ebf-cb2c-3494-8b1b-859fe988ca64 | -7.62028 | -42.58263 | 2025-11-18 04:50:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1609411-2464-32ec-b103-9144a04b85bd | -7.86402 | -46.86913 | 2025-11-18 04:50:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3009259-1e84-3eb8-bee3-2608cb896e4a | -7.14644 | -44.91985 | 2025-11-18 04:50:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73c0fdf5-ddcb-30cf-aa8d-5277b79a1ae0 | -7.69832 | -55.50053 | 2025-11-18 04:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f374896-c9de-31c7-92a9-9feadc793214 | -12.86057 | -41.4768 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c7bf94db-b437-3ba7-a95d-4b9236215579 | -10.74138 | -51.80939 | 2025-11-18 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7fd79d2a-6c65-3c55-8c98-c252bf7780a2 | -8.21963 | -48.30392 | 2025-11-18 04:50:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1225336-5903-3a5e-8739-bac67210b960 | -10.5156 | -43.95475 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1e0dfcc-ed8f-3c6f-ba17-6562ee399145 | -12.86445 | -41.48273 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0c349cb6-32ad-3b31-9bc3-477294c52f5b | -13.20579 | -48.31719 | 2025-11-18 04:50:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f1f9401-3701-3b81-be51-c97f35e3101a | -8.05831 | -46.85109 | 2025-11-18 04:50:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc43a5d8-1ee4-323d-8b37-5e92157c4b7d | -7.41529 | -42.75505 | 2025-11-18 04:50:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab1182c0-4752-3e13-8dd5-5ff8ec8313a1 | -11.52274 | -48.95804 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9daa1503-9bfe-3223-bf76-d97646eac314 | -12.71463 | -45.39 | 2025-11-18 04:50:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 614bcbaf-4782-3053-8397-d04277385e07 | -10.27821 | -47.97271 | 2025-11-18 04:50:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1b062e8-f352-3d19-9f15-b5d7dbda6d24 | -8.57573 | -46.48893 | 2025-11-18 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ed16783-6d90-35cd-bae9-9a6919ea0834 | -12.86624 | -41.48052 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4ff4c388-7bfd-3899-aed3-5cf662320335 | -9.97416 | -44.77662 | 2025-11-18 04:50:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ade86fc3-bca1-38b8-b0ad-39bc41bb6d73 | -7.69476 | -46.85185 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de28dc12-8e63-30e8-9ca4-3bcb704d739e | -8.69973 | -51.28294 | 2025-11-18 04:50:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b14f5da3-4593-38e5-ab3f-a70f513435d1 | -12.86585 | -41.48389 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b1d398f4-2ad0-3804-951f-fef2861301e8 | -9.72283 | -48.90869 | 2025-11-18 04:50:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 199880fa-8707-3d24-bf6f-e483cf3f1657 | -10.09715 | -54.01348 | 2025-11-18 04:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 749286ae-555f-3df6-94e0-c398e97cc57d | -5.9477 | -52.53172 | 2025-11-18 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c7baade-85c7-3b95-baec-c3fc5d1dc2cb | -9.40326 | -48.44916 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7cd99f49-5cae-3d24-919d-db33c699a6e9 | -11.71058 | -48.86941 | 2025-11-18 04:50:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89dc2585-cfc8-3e9a-ad36-e6a1a989d5ab | -6.99297 | -46.18403 | 2025-11-18 04:50:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f25ec0a-2092-3e2d-838a-b2ee9eb799ca | -12.89598 | -54.72108 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac2ce62f-df48-31e5-b956-489b88939bfa | -7.43378 | -45.19192 | 2025-11-18 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ea8f5c4-7e40-345c-87b2-dbd8b0587f25 | -12.86013 | -41.48067 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| d1375b60-3879-3f0b-9bfe-bfa86dfbffc1 | -11.20648 | -49.41198 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d817ad88-68be-3ed9-8e69-05c6b278f30c | -10.30489 | -54.20779 | 2025-11-18 04:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e73328eb-f4ba-3e92-83bd-38f873b49482 | -6.09251 | -51.27026 | 2025-11-18 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09af45d5-b6f9-3ff8-839c-2baf645b2ec5 | -10.30837 | -54.20834 | 2025-11-18 04:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40741639-192c-3919-b264-f3758ff1c6e8 | -9.8762 | -44.18444 | 2025-11-18 04:50:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 32bd4b7f-9aae-35d3-b3fd-987fda4e9220 | -7.43812 | -45.19255 | 2025-11-18 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b6de261-a8ba-3c44-869e-e3879761750b | -10.58597 | -49.00827 | 2025-11-18 04:50:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d200e914-4a4d-3588-ac55-8e140630c3a6 | -9.72256 | -49.13065 | 2025-11-18 04:50:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb4a60c0-87a3-3233-bdfd-3e42c53f22df | -9.39962 | -48.44859 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2736eb70-080f-3d21-9760-496af32b4268 | -12.68109 | -46.77425 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1db2700e-47e3-3795-ad0c-e5ad9507eda1 | -9.82751 | -46.93473 | 2025-11-18 04:50:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84d99143-2592-3ce8-a9d5-a40964819de9 | -10.51066 | -43.95408 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 358dcabe-39a5-3cc1-9aff-e899293ce5ca | -11.46883 | -49.72961 | 2025-11-18 04:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40fda658-7a12-37ec-9aff-ee468b2484b4 | -12.23161 | -49.38005 | 2025-11-18 04:50:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39f3a3b1-96b4-3a66-8e85-375fd0cd484a | -11.5707 | -42.41858 | 2025-11-18 04:50:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 28c83e9d-0d48-3a74-ade3-241e809e1627 | -12.63734 | -48.86769 | 2025-11-18 04:50:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebb59b23-b48e-3b7c-a1a2-5c2c57bc3e3f | -10.65919 | -49.36695 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85bc915d-54fc-3b99-9db4-fda7d5f4191a | -10.6469 | -49.73438 | 2025-11-18 04:50:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61fa3eb0-2f04-3630-bc0d-a90dff454605 | -9.39235 | -48.44746 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0e3a5833-7924-3926-9071-ec0a8de7f236 | -11.39538 | -43.31901 | 2025-11-18 04:50:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96882a8d-5eb3-3a9f-b676-4795e7432f20 | -7.30853 | -50.68039 | 2025-11-18 04:50:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd87ab38-ba19-3e03-99f4-d4fc7655890b | -10.50675 | -43.95581 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9238fa0f-1dbb-34ac-b52f-27a07aa24878 | -8.00973 | -46.57479 | 2025-11-18 04:50:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fbd2762-de36-3b81-a34f-bbb07c550539 | -7.62577 | -42.58353 | 2025-11-18 04:50:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 807e8d68-5cf4-34d6-bb70-000d48ce3e70 | -10.3275 | -50.15873 | 2025-11-18 04:50:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fd35543-f74e-3df7-b402-6cc8f0bff6d2 | -11.57323 | -48.14015 | 2025-11-18 04:50:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57f8fb82-df8a-3a59-9f6f-55b670f085b6 | -8.30184 | -44.00362 | 2025-11-18 04:50:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b82d0f0-17c3-3721-8804-4c5a59dd34d0 | -10.99784 | -50.9242 | 2025-11-18 04:50:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 089ce8f8-e033-3307-8ab6-580093af10eb | -10.61608 | -42.31726 | 2025-11-18 04:50:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 27ad9973-99bc-379c-b57c-c637d523bed3 | -12.69371 | -46.77603 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8115e45-8292-3abe-83dc-4ce7d0e77c84 | -7.70215 | -55.50116 | 2025-11-18 04:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d99e3ba-17ab-31f8-a49e-9b3981f68fdc | -9.88174 | -44.1797 | 2025-11-18 04:50:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e8976a19-e82c-35c7-ab2e-4a228d62052b | -5.96269 | -52.93576 | 2025-11-18 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 043e45e6-f459-31e8-b9b2-0db9b1ebc716 | -8.22387 | -48.30029 | 2025-11-18 04:50:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e8efa0b-17c6-33f8-b7d5-cf2fc632ec51 | -6.14928 | -57.84775 | 2025-11-18 04:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54746245-4d9c-3713-9e65-6560e86aac52 | -10.79947 | -47.63708 | 2025-11-18 04:50:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 966c30d0-9b01-3379-ad79-0a2cee438320 | -9.88513 | -44.19106 | 2025-11-18 04:50:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3ac7d23e-bf86-380c-91ea-94751cf3a7df | -7.33533 | -46.16713 | 2025-11-18 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4f54a99-457c-3843-85dd-72b712db7e53 | -11.52337 | -48.95377 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc66c666-3447-30a2-8894-8992119e36bb | -10.50078 | -43.95271 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c412184-f5e4-3a3e-a7a9-e0091a96fd64 | -11.20093 | -43.17508 | 2025-11-18 04:50:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bb1445a9-4874-3f87-87ed-aecd01c14847 | -8.21601 | -48.30336 | 2025-11-18 04:50:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cfcba7f-67a3-3a14-ba37-ed089e27ef61 | -13.9032 | -47.49627 | 2025-11-18 04:50:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abf8f9f4-6bcc-3e27-b77b-201a23c29cef | -7.07135 | -46.04943 | 2025-11-18 04:50:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b355282a-524f-3f7c-8f93-ca2da970511f | -11.40101 | -43.31652 | 2025-11-18 04:50:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3090ce66-e356-3a82-83bc-b6b02d4cee57 | -8.12253 | -55.30295 | 2025-11-18 04:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f35fd9fe-0ce2-3966-895c-a16886ac36c9 | -9.39298 | -48.44323 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 964bc1d7-7c86-37b6-b9cd-f1db0c906873 | -7.45076 | -42.76315 | 2025-11-18 04:50:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1f9a2dc3-3b1d-3c0a-9ce8-5c68bd1b0aa3 | -8.38615 | -44.06501 | 2025-11-18 04:50:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 301f7d91-da4c-3cf3-aa80-b1112694ce02 | -6.85506 | -46.11225 | 2025-11-18 04:50:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05d08d69-9cbc-3720-af81-3c5e43071ecf | -12.55585 | -52.25004 | 2025-11-18 04:50:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4b1e9bd4-6bb8-3671-a339-d577b30f22b1 | -11.57257 | -48.14482 | 2025-11-18 04:50:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28cee3bf-bec2-342e-96c9-801ecd18acf9 | -8.72449 | -48.53505 | 2025-11-18 04:50:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 779317d3-d92a-3992-b011-9e1fae6d08b4 | -7.3039 | -45.75748 | 2025-11-18 04:50:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3404069d-fce1-327a-a285-d42995e99746 | -7.34325 | -44.43433 | 2025-11-18 04:50:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9c82665-6e4b-358d-8538-2128d5d0c239 | -10.50572 | -43.9534 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed2635e8-2e09-3cf1-b1ab-64c84749151f | -9.39662 | -48.44379 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7696f2da-ab8f-321e-a665-e6fbb24b9c03 | -7.85622 | -46.86795 | 2025-11-18 04:50:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa656e14-893f-3181-a5b9-cdd78247c831 | -10.85226 | -44.88322 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README44.md)
