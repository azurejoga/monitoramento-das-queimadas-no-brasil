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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ed0d21f-5455-341c-b35b-ae48fbbced89 | -4.95993 | -43.00653 | 2026-09-21 04:19:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a4a6bdab-5d06-3708-b95e-2be94fcde47a | -6.61317 | -50.06041 | 2026-09-21 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5b8e046-5a45-31ea-9a6a-cd5e6d478add | -4.22448 | -48.61681 | 2026-09-21 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8cc450e-cde7-3879-a259-988aeda8cf6e | -9.44626 | -45.43333 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 347c4fb7-d00b-31ef-8fc3-99e9da554533 | -7.57597 | -57.6877 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fd9d1abe-4d9e-3f37-ab4d-557ca198f139 | -6.20894 | -53.56722 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cfab538-1a4d-381c-b60f-9e23013b6651 | -7.46053 | -46.03517 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71b4cbe9-aa8d-37fa-a62a-557fa701c4fb | -7.30014 | -46.76568 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 379939cb-ffa7-3a7e-9bb7-4d9cef4b2082 | -6.46902 | -42.76276 | 2026-09-21 04:19:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e0b26828-ffc7-3ad3-be9a-bf4669f18519 | -7.77678 | -44.81657 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf524d6c-f2e1-3d58-a197-9c801142544a | -9.46668 | -45.41425 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6f9a970-ad09-37e5-935b-807be16508c3 | -7.56742 | -57.69353 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9a8a32e5-a2f6-3591-9fb4-e9225fd3863e | -5.80562 | -52.09287 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e468ff7-e4d7-3b00-8082-c2e09562953d | -2.88993 | -49.48043 | 2026-09-21 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4738752-f669-310b-8fcc-318d8d553bc8 | -4.57879 | -42.94563 | 2026-09-21 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 390754f8-2c8c-3b2c-82f1-2f070b3d7b53 | -3.87934 | -38.43775 | 2026-09-21 04:19:00 | NOAA-20 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 897354d0-39bc-387e-82b0-3ac8b2c06ef0 | -2.82526 | -46.70911 | 2026-09-21 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b9cdab6e-b163-3cdf-9de5-318406b0214a | -6.88448 | -41.70258 | 2026-09-21 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 44b1b005-ad41-3ea6-a07b-56d6b7ab902b | -9.02007 | -49.82478 | 2026-09-21 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d605fd58-2b5b-3d62-8c86-4c4fba9aa9ce | -2.90606 | -54.14663 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2823e09-7cb3-38de-8f35-7b32042de3b8 | -7.42064 | -44.76669 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eecd5381-63f2-3f35-8dcc-0dc7c89ec201 | -3.60266 | -54.05103 | 2026-09-21 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c3a03a7-5b15-3c61-bf9f-d9624ae90625 | -9.26006 | -46.18258 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27bff091-7eb9-395e-939f-d8c6efab4d6f | -7.51657 | -46.22563 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65a733b1-45b1-3274-8b9b-05330d59d5c4 | -6.44839 | -48.45308 | 2026-09-21 04:19:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35a3968c-2a8f-3c23-8348-c108686c9fc1 | -4.85012 | -40.52391 | 2026-09-21 04:19:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63241b02-70e2-3c91-b420-5d5779d95007 | -9.45122 | -45.38191 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| ed2f9f29-d7d9-35ba-9e73-3cf5c9faf4fb | -4.34714 | -55.65336 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f8bf9eb-0c9b-32fb-a58e-a09c221e42af | -9.45716 | -45.409 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b19208b1-b1c7-366c-92bf-213b8336169a | -7.4285 | -44.76065 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70e6d950-78b3-3687-a154-fa855e800699 | -2.82796 | -46.70741 | 2026-09-21 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00626c9b-aebf-393f-918e-27825b71fd79 | -2.29516 | -48.58501 | 2026-09-21 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3065db57-8f07-3710-a4fe-ffa10615dfbc | -6.8987 | -46.01513 | 2026-09-21 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6069ff7-19ac-37a2-9a8c-df018c8c9048 | -5.81937 | -53.50501 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a7e1151-7acd-385c-b9ee-82077656e8d1 | -7.40295 | -46.16679 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5d575dc-53ec-34fe-bff5-4406c13f4a1e | -9.02785 | -49.83033 | 2026-09-21 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4196a4ef-4539-3233-89c8-4ac1b3107095 | -5.86994 | -50.16202 | 2026-09-21 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4422656-1a0a-3734-819c-ab28fb871ff1 | -8.79278 | -48.74405 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2002d1b2-05cc-33e6-b50d-78d72400b594 | -6.91913 | -43.73963 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c4cbb86-2198-35f9-ac7c-72a8d2fe208e | -6.44965 | -48.44572 | 2026-09-21 04:19:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6313d505-cda0-3041-b2a7-fa95cd12989c | -9.45677 | -45.39026 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b336b376-d8e7-3d05-bf61-56fc81aa363b | -9.02279 | -44.90493 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acbb33e6-22f9-3b04-b776-64249cb048ef | -5.20672 | -56.10531 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dedd3fc9-c2cd-3c63-915b-78e3d9364558 | -7.43799 | -44.76583 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93f0e494-ee87-37f1-ba72-7bf9fa0b935f | -5.89661 | -52.09713 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e632b31a-66d6-365e-b74a-d513cba6aee1 | -2.45814 | -49.21754 | 2026-09-21 04:19:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7974e25-484e-3cdf-81ce-9f2ae075770d | -7.00603 | -42.17611 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c35d2d67-510f-3cbd-9735-c5e604636e20 | -2.4536 | -49.21679 | 2026-09-21 04:19:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9e1358f-48df-35b2-af2e-22eba96090b6 | -7.20344 | -44.08794 | 2026-09-21 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42f7b557-447f-393d-945b-013d299c3bc1 | -7.44086 | -44.74798 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46b61504-316c-357b-a085-61e8a81ae349 | -5.15372 | -42.74664 | 2026-09-21 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71b89fcd-0910-3dd1-8cc8-0cbc0899a22f | -7.13345 | -42.07863 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 37924bb9-39f7-34d1-8771-a30dd5ef337b | -6.82893 | -55.54459 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cea55a6b-a152-39cf-bc66-e1d2bf8cb69a | -6.69532 | -43.00832 | 2026-09-21 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16775f04-229b-32c1-9ddf-5d445ca02261 | -7.41393 | -44.76561 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0de0df79-b2b7-3b4d-9e2b-89b69d2bf7b9 | -5.19764 | -56.11639 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 15280a5d-63af-313e-876a-b24ddb9fe5ea | -5.80485 | -52.09713 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c121bba-4695-34b1-9f40-0a24e833423a | -6.91692 | -43.73217 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ef0b3d3-d813-3b5e-b9a9-3bfcabb87e40 | -4.33795 | -46.36676 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 281eff9f-c9e5-303f-90d7-f1ff648c47af | -5.20347 | -56.1172 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4e187b1-36b6-3d89-ab79-74147f815063 | -6.37086 | -35.16363 | 2026-09-21 04:19:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 2282884f-abec-3df5-925e-c379caffeea1 | -8.66009 | -45.4294 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a199ee9b-04bb-3395-ac64-1f5858fcb35b | -1.67259 | -54.94324 | 2026-09-21 04:19:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 061f56ce-a0b1-31cb-98a2-919f64c22855 | -5.85545 | -49.80275 | 2026-09-21 04:19:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4cc0921-76e7-31cc-875b-1340274316b6 | -7.05995 | -49.91259 | 2026-09-21 04:19:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d66f0bb-ca6f-311a-97d4-54c278cd4726 | -5.83296 | -53.49526 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec2594ff-990a-31a4-8dbc-f7cda207836d | -6.50055 | -43.89351 | 2026-09-21 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2a514b9-bd0d-3988-bd4f-31808118fb3c | -7.07863 | -46.28841 | 2026-09-21 04:19:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd157f95-9647-3145-8d8b-21178febd403 | -7.24092 | -55.59224 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cacc1a41-a3fa-3704-8aea-6bde167084dd | -9.46072 | -45.38719 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 78556c8d-b08f-382e-862a-c79b77f8e6b7 | -4.58912 | -45.16013 | 2026-09-21 04:19:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3efd3556-b2c5-37df-b7e7-0f56ca56a8c3 | -1.5404 | -48.6523 | 2026-09-21 04:19:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd29ac7f-4526-3555-8a57-d26c196547a6 | -2.90521 | -54.15159 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0748c09-49e7-3fb0-82d0-24ba38c83f38 | -5.01434 | -56.10162 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 355ed7e2-8f9e-3e84-a6fb-6ba78ef4ecd9 | -9.0288 | -49.83112 | 2026-09-21 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91633fa6-c1fa-32c8-a32d-406f0f4209ab | -9.46568 | -45.39917 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e1713ff-68dd-3063-a0ea-af77d230c524 | -9.47023 | -45.39247 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fab43b6d-df0e-3cba-8fb5-74ad528bb895 | -9.00672 | -45.0045 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 800e97c5-4f46-396b-8eb5-991605d268a5 | -4.96323 | -43.00705 | 2026-09-21 04:19:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c4b5877-c5d6-3c69-a49a-3fb42912c12e | -6.73065 | -55.09604 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f926594-3a9d-39e6-8cd0-90c2849fb9bd | -7.5897 | -43.43132 | 2026-09-21 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c392026e-0e1e-3a06-9810-10bacd74b0fb | -9.44573 | -45.38505 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e55df178-d1dc-31b4-b863-eaafd268175e | -8.37052 | -45.63696 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e924437-1658-3834-b3c4-f7dce77296b7 | -7.58512 | -44.90282 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04fe3878-7f50-3f94-a7b1-916285b0c1cf | -5.37562 | -55.90396 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5488456-d5b3-3226-8270-c0d38a6b123c | -6.9105 | -44.90261 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63dda6f6-c55d-3b09-9c55-fc1af1fa7834 | -5.37448 | -55.91042 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f9723a7-0cf4-3d64-9a3b-b6c53abdb3bf | -5.29408 | -49.27529 | 2026-09-21 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb8124a9-7e99-3608-8fcf-25486af84388 | -6.40152 | -46.01941 | 2026-09-21 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15fc74fd-daf6-316c-acfe-a6635bb41148 | -7.41728 | -44.76615 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 82bc3467-5189-314f-9fa3-f6681cf97ee3 | -6.36062 | -43.36304 | 2026-09-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 901a9c07-abb8-3cff-b195-bf74daed7b18 | -7.88827 | -44.84172 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1ca4c63-9b4f-3258-9864-8713604c4304 | -8.75978 | -44.27748 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bde5a29-43e3-3825-9ccf-f9728aaeea48 | -9.26698 | -46.18373 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfdee017-4d84-3acf-bf65-4e626250f637 | -9.46331 | -45.4137 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b3a4861-4b62-36b7-8eac-5e8bf35b2360 | -3.15947 | -50.82193 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 939a737d-af24-3473-9118-b521185afadf | -7.97743 | -47.45024 | 2026-09-21 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa33d14b-3e9c-3b2c-9a19-94c4f31b51e0 | -6.36588 | -35.16289 | 2026-09-21 04:19:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dead5ece-e481-3d10-bd7f-1b4fd6a40b04 | -5.83021 | -52.07604 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db2229c7-2619-3bac-b4b9-05694b219d66 | -9.44586 | -45.41461 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README32.md)
