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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db59b771-5a3f-3d59-b2b3-5f55862c2e3e | -13.2273 | -54.421799 | 2026-06-27 00:53:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c734ad9-7fbb-3ca0-943d-bb5ff042ff55 | -10.3357 | -50.123299 | 2026-06-27 00:53:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b68cfa5-4628-3389-8749-338ddf96cc31 | -12.4691 | -58.486099 | 2026-06-27 00:53:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9c0f534-f107-3375-b382-373fc166fb64 | -11.6604 | -57.245701 | 2026-06-27 00:53:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31b91524-1ab6-3546-b39b-321f2cd2ef40 | -12.5994 | -57.875999 | 2026-06-27 00:53:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0ad8313-cebf-36fe-863a-298acedca819 | -11.6621 | -57.253201 | 2026-06-27 00:53:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e83f6a19-4b67-3c77-89d1-e57fb2fb7cb7 | -12.4609 | -58.495399 | 2026-06-27 00:53:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ffc6f70-3949-368d-a8c2-97f128bf9257 | -11.9154 | -57.4118 | 2026-06-27 00:53:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55c21391-95ef-347e-ab7d-7106d16294e0 | -13.6404 | -55.2845 | 2026-06-27 00:53:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aad98df9-7863-38bc-b3db-f2c4d901656a | -12.933 | -56.631199 | 2026-06-27 00:53:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3df7a67-9c81-3edb-93ef-d9b3b302909a | -12.4562 | -58.4744 | 2026-06-27 00:53:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bbbc4bc2-bfff-3c93-af1e-04ae7ccba379 | -14.876 | -54.523899 | 2026-06-27 00:53:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1053bccf-73b7-3509-8905-ec8eb9fc2857 | -13.6576 | -53.933998 | 2026-06-27 00:53:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83a875b5-df07-3e5e-b475-69e92b026bfa | -10.305 | -57.143002 | 2026-06-27 00:53:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e806e8f-2b8b-33ee-8e6a-c64b42a3d47e | -10.6375 | -50.214802 | 2026-06-27 00:53:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d22c287f-eb67-3b89-9249-7d9e663c5c30 | -12.6123 | -57.887901 | 2026-06-27 00:53:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d241f3d4-303c-3b49-9117-8a5b117a8eaf | -11.6638 | -57.260601 | 2026-06-27 00:53:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 403da0ed-900e-3f5e-818e-7a3efb64a2f3 | -14.8685 | -54.5355 | 2026-06-27 00:53:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7d133da-3699-3a0b-8f99-921c2fba4b02 | -12.4707 | -58.493099 | 2026-06-27 00:53:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd7d35fe-e8c5-31c3-a024-f595e210752a | -12.6091 | -57.873699 | 2026-06-27 00:53:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05321085-72cf-3b3c-9b16-b712ce019087 | -9.5934 | -56.924099 | 2026-06-27 00:53:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6289348-2b38-315e-9e17-270cf4622f5e | -12.9348 | -56.638802 | 2026-06-27 00:53:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74573457-313e-3cbf-8a84-c5221f481456 | -13.6601 | -53.944199 | 2026-06-27 00:53:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48ca66b3-c7ab-3598-862f-ee8d76d9bcc1 | -10.6426 | -50.2346 | 2026-06-27 00:53:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 650ed935-4d23-3765-b326-f60705c5c73b | -12.174 | -59.7509 | 2026-06-27 00:53:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13f57e86-ec89-3ada-bb19-79305206585a | -12.4593 | -58.4884 | 2026-06-27 00:53:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73d80906-01f1-32d3-a522-21537654c358 | -13.2422 | -54.397499 | 2026-06-27 00:53:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96750b18-d5d7-37c6-9de1-918e7de80e30 | -11.3251 | -54.465401 | 2026-06-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 147d9908-9769-34ab-8aa8-644e25bc336b | -12.6107 | -57.880798 | 2026-06-27 00:53:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29d32fe7-8c8e-37af-ba6a-3bbd5dde6f61 | -13.2519 | -54.3951 | 2026-06-27 00:53:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 143e8bbc-239b-3c29-9bed-3dffdebf5ef3 | -10.8973 | -56.8479 | 2026-06-27 00:53:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03b8183c-6344-3acc-b4dd-482305889159 | -11.9023 | -57.399399 | 2026-06-27 00:53:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e0d66c3-394e-390d-9cfb-e2db18491ba8 | -9.0315 | -61.319599 | 2026-06-27 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d114855-8a87-383d-86e1-230f3f8b10c2 | -9.0259 | -59.537899 | 2026-06-27 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3fa4d8e-0c1f-3d79-8875-182381236a5b | -12.6238 | -57.8927 | 2026-06-27 00:53:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fafc4a99-4762-3332-8b88-4c6b37bb561e | -14.8782 | -54.533001 | 2026-06-27 00:53:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0dc0ed7-934a-3120-a0cd-5abebc1a77c0 | -12.1725 | -59.743801 | 2026-06-27 00:53:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3f24815-a08c-37e7-96d5-2cd413cbeb2e | -12.2236 | -56.556198 | 2026-06-27 00:53:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d76fec9-18a8-3825-8172-d900e2ec3439 | -12.4676 | -58.479099 | 2026-06-27 00:53:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e0a6572-bd2e-33fe-9259-069ef01022da | -11.912 | -57.397099 | 2026-06-27 00:53:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e295be46-57ff-32b2-b117-c9e84a5af180 | -12.601 | -57.883099 | 2026-06-27 00:53:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c1a648a-6c3d-30d0-a5c5-f42b3f76cc0a | -11.6457 | -54.8965 | 2026-06-27 00:53:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0468490-4a19-3b75-be45-25dd22416910 | -10.6523 | -50.231998 | 2026-06-27 00:53:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 182f8987-aaf4-367b-a4ce-3dbeae663935 | -13.6698 | -53.941799 | 2026-06-27 00:53:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e441807a-e54d-38ec-b59d-94eda792938f | -9.5915 | -56.916199 | 2026-06-27 00:53:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a64f1573-cbe8-3b94-b84d-5c1f78758469 | -12.2218 | -56.548401 | 2026-06-27 00:53:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b03e6e2e-38c7-330d-a874-6086991c31d4 | -13.6551 | -53.923901 | 2026-06-27 00:53:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1fee1c33-8fb2-3942-b19a-90c7f8739c4a | -13.264 | -54.402302 | 2026-06-27 00:53:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfca757c-fdaf-3dae-b9f7-c76d77cf16ef | -10.6472 | -50.2122 | 2026-06-27 00:53:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33bc835d-47c3-302f-9d3e-e3d38b265001 | -11.904 | -57.406799 | 2026-06-27 00:53:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3a30e0e-e573-3aa3-a63b-a1760a157c6b | -11.9057 | -57.414101 | 2026-06-27 00:53:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d1bb3ab-bbf5-355a-b5ec-a36f565f98c4 | -10.341 | -50.1436 | 2026-06-27 00:53:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89d819af-ca9e-363e-a3fc-596cbecfb7c5 | -12.6048 | -57.8743 | 2026-06-27 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| b8a3e9d6-6369-3b4c-b2b9-2678ccc563e4 | -7.7361 | -44.1823 | 2026-06-27 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 01d1ede1-aede-3e2a-b5e3-90839d16b9dc | -12.6046 | -57.8942 | 2026-06-27 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a06fad6e-2f0e-34e1-be29-bbd5e7fc30c8 | -10.3557 | -50.1457 | 2026-06-27 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 0650e12d-6c1c-3d58-b287-49d7f8fe38c2 | -5.7756 | -45.0826 | 2026-06-27 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 252e8f48-5a3c-3df1-ac73-9b891280e021 | -10.5634 | -46.2362 | 2026-06-27 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6b43be84-075b-357e-8955-0345e1269b5d | -10.6385 | -50.2018 | 2026-06-27 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 4eec312f-b1aa-30fb-aadf-ea9dd7cce097 | -10.6382 | -50.2232 | 2026-06-27 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 9b9a8634-a131-3356-84ba-6a0138c4bbbd | -12.6238 | -57.8727 | 2026-06-27 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| d08da697-9f7f-331d-a116-117d2e30e9f9 | -12.4654 | -58.481 | 2026-06-27 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 3893fb0f-a22c-3a7d-9c87-e5923fb218db | -10.3368 | -50.1477 | 2026-06-27 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 5c565047-4027-32cf-b568-bd5e3c9a1268 | -12.4651 | -58.5009 | 2026-06-27 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3bb45267-4cbc-35eb-8b9e-ed6d2b78e91a | -12.4464 | -58.4825 | 2026-06-27 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| b1ab4851-6585-3646-8b51-450b72320f8a | -5.7945 | -45.0586 | 2026-06-27 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| d051c01a-5060-32c7-84c3-c7ffcd58b474 | -12.4462 | -58.5023 | 2026-06-27 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 644e264d-4796-3f34-b033-c622bdda636c | -10.6571 | -50.2212 | 2026-06-27 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| fa13b5eb-be35-3d77-a676-634d51bc1611 | -12.6236 | -57.8926 | 2026-06-27 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| c2836fef-7e91-3e2a-871f-b5b7ba841acf | -13.6671 | -53.9314 | 2026-06-27 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 28acaf14-e3fb-3cf0-9f01-9ba6ee605d6d | -5.7758 | -45.0599 | 2026-06-27 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 98b8e47d-ed51-3e9a-beb7-2429af022df3 | -12.6236 | -57.8926 | 2026-06-27 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 26c6a066-7b08-3d07-b39e-4934fc748bed | -10.6571 | -50.2212 | 2026-06-27 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 249b1e4a-0bfe-3a4d-b29f-98269fbcfcf1 | -12.4654 | -58.481 | 2026-06-27 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 79d1392c-9b9c-3163-821b-dec7eb647ed4 | -12.6238 | -57.8727 | 2026-06-27 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| d136b0e7-7acc-34a6-9f90-2f56e8ff933a | -13.6671 | -53.9314 | 2026-06-27 01:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| fb193680-cbc0-3d2c-9d9d-855a07d94586 | -5.7945 | -45.0586 | 2026-06-27 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 317cfc8f-0e64-3c8b-9a7e-f76c16ff6b8d | -5.7758 | -45.0599 | 2026-06-27 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 7249abd9-b337-3e30-84de-0e13bbfd9d22 | -10.6382 | -50.2232 | 2026-06-27 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 1812b8ca-d0df-349b-bbd7-ef1647d006de | -7.755 | -44.1805 | 2026-06-27 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 8ac67b16-efab-3115-bbeb-d38fe1fbf147 | -10.3557 | -50.1457 | 2026-06-27 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 3bf59845-76a9-3318-97c0-f51c6f883eb1 | -12.6046 | -57.8942 | 2026-06-27 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 4c5f9388-588e-33ba-8373-9c53f6abfbf9 | -12.6048 | -57.8743 | 2026-06-27 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 56bd9dbc-4c7d-38c7-958d-7bb174688951 | -7.7361 | -44.1823 | 2026-06-27 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 45a352b1-2eb0-3473-a465-2a24660c002e | -12.4651 | -58.5009 | 2026-06-27 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 45034884-625f-3da3-a066-4dab1b0a8edf | -10.6385 | -50.2018 | 2026-06-27 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 39afcf5d-249c-3871-8e9e-15330e5caa8a | -12.9411 | -56.632801 | 2026-06-27 01:17:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9dd351cd-8054-3f7a-b5b1-dee4274b0424 | -13.6519 | -55.285999 | 2026-06-27 01:17:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a01a3e2-3f0f-35cf-84e3-33c7e8fc3a89 | -10.6419 | -50.243099 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 729a76d0-b92e-3c7d-a220-51df34d32e64 | -10.6298 | -50.1954 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49031bad-05ca-3389-b03f-c375776695b2 | -12.6204 | -57.903198 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8ebdb26-e159-37bf-a673-4d85e47b0269 | -10.939 | -56.853199 | 2026-06-27 01:17:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5899bad4-4c06-38cb-b253-8cceb6d0add6 | -9.0295 | -61.3335 | 2026-06-27 01:17:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b9bc00b-9ae6-3281-beb1-2585993da8dd | -11.6604 | -57.257 | 2026-06-27 01:17:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b36483b4-52c5-36b2-87c8-cfa75a4e9504 | -11.9122 | -57.412102 | 2026-06-27 01:17:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7b62479-3741-3326-9438-6086b25b549d | -13.6537 | -55.293598 | 2026-06-27 01:17:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e12ec08b-5c9e-3f5f-a678-01a9de88c9e2 | -13.6673 | -53.951099 | 2026-06-27 01:17:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd9293f0-6fc3-321d-9e34-d33639061d17 | -12.4352 | -58.411201 | 2026-06-27 01:17:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| abdd1249-fd81-3f6a-bf72-68ac9c6d0f02 | -11.9106 | -57.405102 | 2026-06-27 01:17:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edfc68e4-9c79-35aa-8d50-92966730310b | -10.6435 | -50.208801 | 2026-06-27 01:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
