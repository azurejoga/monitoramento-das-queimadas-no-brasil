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
| 05715590-3af3-3770-a86b-7c62d29c746b | -25.9716 | -48.950401 | 2025-07-19 00:28:00 | METOP-B | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d35cfe0f-44ff-3261-9bd4-1b0091f520a7 | -16.0755 | -49.7117 | 2025-07-19 00:28:00 | METOP-B | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 828754fb-6b4c-30bf-891c-e67efa7aad4c | -10.8489 | -47.163101 | 2025-07-19 00:28:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe929a7a-5147-38a4-9074-bdcd6e38ecc7 | -5.6502 | -43.704201 | 2025-07-19 00:28:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f69d214d-99ff-33e8-b297-556086ac57e4 | -3.503 | -47.2132 | 2025-07-19 00:28:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 255d02da-b1a2-3bde-a8a1-aac6ec8ec4f4 | -8.5434 | -47.846401 | 2025-07-19 00:28:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f6612cd-3c46-321b-a46b-3d1ea537349a | -9.8308 | -48.368099 | 2025-07-19 00:28:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4fc81e5-987a-3ee4-9781-81c9eeaff706 | -9.7619 | -48.738602 | 2025-07-19 00:28:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74e3cb12-a551-3593-b140-b39553bc9c95 | -8.2685 | -55.162998 | 2025-07-19 00:28:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf57fd8a-d2fa-3530-bbff-7c9271362528 | -12.4963 | -57.192101 | 2025-07-19 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f204bc2d-4945-3390-a846-899ae051a167 | -7.4808 | -47.492401 | 2025-07-19 00:28:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1289a9e0-78d7-322a-8c12-4bb0481907bd | -14.6926 | -45.053001 | 2025-07-19 00:28:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f223c65-b775-3acc-9cb9-7ef1723b7b63 | -16.035101 | -43.702 | 2025-07-19 00:28:00 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 99bfa087-48e8-3aaf-a5a9-094d288c9545 | -5.5159 | -43.869701 | 2025-07-19 00:28:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed50efff-2ab0-3128-ac83-c6471df2fdcd | -3.1165 | -47.009602 | 2025-07-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09d7c264-f585-37cd-af29-35a3822f6666 | -10.3899 | -46.6637 | 2025-07-19 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e1fe3fc-3505-37d3-ae7e-cb9774c99ed8 | -8.8799 | -50.154999 | 2025-07-19 00:28:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a844e059-b455-3664-85fa-6463ce4f5fc0 | -3.1291 | -47.019199 | 2025-07-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44a306f8-d393-3c37-a0d3-8a0ea821df3b | -10.6309 | -44.755699 | 2025-07-19 00:28:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4632b8fe-c19e-3298-82bd-f3997c09b7f3 | -4.028 | -48.058399 | 2025-07-19 00:28:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4f72cfc-29ca-3123-b685-06fc76b30762 | -7.2085 | -49.607201 | 2025-07-19 00:28:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cc1e359-4b47-3e20-9d4d-6ffd42c95f25 | -9.8016 | -48.553699 | 2025-07-19 00:28:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7ec6ac9-798c-356a-a835-fe83c876c7fd | -10.8163 | -49.286499 | 2025-07-19 00:28:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f18047d-8ee4-3426-a978-004d4d4c39ad | -5.5202 | -43.887501 | 2025-07-19 00:28:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af4a6822-26c1-3fea-ba30-8505bd864bc8 | -10.7266 | -46.777302 | 2025-07-19 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6eb60167-20cb-3dd7-83bf-a2621c46bd34 | -5.6449 | -43.724701 | 2025-07-19 00:28:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 596c9130-6bb2-36d7-977a-ceaee0a7189f | -14.1767 | -58.1796 | 2025-07-19 00:28:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fab616cb-13e2-34df-8286-7ecc32eacbb4 | -3.0448 | -49.424198 | 2025-07-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 426e196d-149c-3e69-a86d-4ef5884d1942 | -6.7608 | -45.498901 | 2025-07-19 00:28:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7145a5cc-e1b5-3986-a5e1-ba0f18be06c7 | -14.6952 | -45.063801 | 2025-07-19 00:28:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b74252bc-3b22-398d-b623-b534f8a59544 | -23.960899 | -52.834301 | 2025-07-19 00:28:00 | METOP-B | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b59043f-bd20-32cb-bfc4-c55d7d2759e0 | -9.8045 | -47.724701 | 2025-07-19 00:28:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e725462-62f9-3fef-9a71-02644752a993 | -2.9221 | -49.067799 | 2025-07-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd9fe17-214e-3fa2-93b2-d8b6addf43da | -3.1236 | -46.995602 | 2025-07-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15350ec3-9f6c-3a21-9e37-9e00716320d3 | -10.3922 | -46.6735 | 2025-07-19 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 898dde7a-6e05-3f33-bf54-b2940c0ce6f7 | -12.0355 | -48.755901 | 2025-07-19 00:28:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f01958cf-5d41-3d45-a8c2-d2c3584752c3 | -10.8129 | -49.271702 | 2025-07-19 00:28:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7743ed08-7077-34b8-bec9-32723930f879 | -10.6212 | -44.758202 | 2025-07-19 00:28:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 80e787d8-a537-31bb-b8f4-ddd127955be9 | -10.6528 | -49.2934 | 2025-07-19 00:28:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56701ba8-1457-3e2a-89e6-5861f1a5a60f | -4.254 | -48.5466 | 2025-07-19 00:28:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7430741e-1106-3737-b436-d3cc2ffb8c58 | -11.4528 | -48.154499 | 2025-07-19 00:28:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a42a0961-a094-3097-874a-aec703b1d4c5 | -22.691999 | -47.248299 | 2025-07-19 00:28:00 | METOP-B | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6afd924c-cdd2-30f2-9f4d-7127b28305d6 | -2.8953 | -48.233299 | 2025-07-19 00:28:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd51ba8d-7406-3833-9418-b4c4eec7c351 | -11.7258 | -48.174099 | 2025-07-19 00:28:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66a35a16-ce05-33ce-a018-1011133e8fb0 | -6.1536 | -48.031601 | 2025-07-19 00:28:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 575ea45f-0a9a-38cc-b761-7035d8b09bdb | -7.9464 | -43.9366 | 2025-07-19 00:28:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b5ecade9-197d-31a1-bc33-19bc1a970138 | -10.6775 | -49.672901 | 2025-07-19 00:28:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cf3c670-59d1-3e38-9117-f0ad96f02fba | -8.5218 | -47.842098 | 2025-07-19 00:28:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49400def-f321-3f52-a35a-a5ccae8074bf | -9.8035 | -48.561699 | 2025-07-19 00:28:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31912df4-523f-3b72-b0f9-b502441f35f0 | -10.9819 | -49.3797 | 2025-07-19 00:28:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f91e2fc3-b852-3b64-a63e-7536f49d42f5 | -11.5616 | -47.076801 | 2025-07-19 00:28:00 | METOP-B | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4fbc42f4-6bdb-39c9-8bf3-b6aaf8ffd77b | -8.0663 | -50.067699 | 2025-07-19 00:28:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae1ca65-9835-3c6c-bfa9-cec9236e398f | -7.0869 | -49.168201 | 2025-07-19 00:28:00 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b8b380ce-d815-3d8e-88cb-2e3aefe7ca4e | -2.8975 | -48.243198 | 2025-07-19 00:28:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2981b303-1b22-392c-a270-c367d4ee03c1 | -10.8146 | -49.279099 | 2025-07-19 00:28:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a0fbdfe-1161-318f-bd0d-ff7711497ca9 | -22.7474 | -44.7416 | 2025-07-19 00:28:00 | METOP-B | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb10806b-fac0-3f9e-aae2-5cf91ca2c434 | -10.6181 | -44.7453 | 2025-07-19 00:28:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 215c6598-2541-3667-b26e-640b1cd0975e | -4.3048 | -48.098 | 2025-07-19 00:28:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77cda9cf-b794-324a-9068-12a2a3931fec | -12.0338 | -48.748299 | 2025-07-19 00:28:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c83750ab-ec2c-3356-af5c-e99b63e5194f | -10.9836 | -49.3871 | 2025-07-19 00:28:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ee6c053-f4ec-3fc5-980b-de475301d929 | -6.1579 | -48.050098 | 2025-07-19 00:28:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1eebcb85-be16-36e8-8156-307faf6ba3c0 | -4.2519 | -48.537498 | 2025-07-19 00:28:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71fd640a-1c52-3af6-aa5d-9ff76b315fdb | -11.5227 | -48.948299 | 2025-07-19 00:28:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1ce2adc-f470-3352-bd82-fab3ad41aa54 | -10.8544 | -47.142399 | 2025-07-19 00:28:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2eef5d96-e3b5-3500-9dc6-d1e8d1d6623c | -9.8114 | -48.551399 | 2025-07-19 00:28:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ae654ed-e774-3044-a190-459eedf1e55d | -11.8347 | -48.198601 | 2025-07-19 00:28:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ae8881c-2b39-3fbc-86e5-840eedabba18 | -8.5315 | -47.839802 | 2025-07-19 00:28:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7c870ca-4a32-38dc-90fc-a66cf01a4f6f | -10.6494 | -49.2785 | 2025-07-19 00:28:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 193de9bc-53f8-39eb-8be0-1b1b7e936253 | -2.4392 | -47.3242 | 2025-07-19 00:28:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af119c98-7b39-3f3c-9b9b-fc592b7596b5 | -14.7753 | -48.285 | 2025-07-19 00:28:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 27b8defc-e632-3cdb-86ee-ea93992cd2ab | -25.379801 | -49.990299 | 2025-07-19 00:28:00 | METOP-B | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f1fee5f7-b7d2-3634-83c6-9e1d146001f6 | -6.1655 | -48.038601 | 2025-07-19 00:28:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 310ab60e-6e65-3cbe-90b8-a652aa3c2963 | -10.6244 | -44.771 | 2025-07-19 00:28:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a8fa5526-2ad8-397c-bd0a-a6930ff9d12a | -12.3709 | -50.327 | 2025-07-19 00:28:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 403ceb10-c7a8-33d8-bc74-a27343f9993e | -10.6115 | -44.760601 | 2025-07-19 00:28:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 91fb809e-3583-39e1-9439-5807797089c2 | -11.4732 | -47.315201 | 2025-07-19 00:28:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5e7e704-7b36-3cff-92a7-c6588971d363 | -25.969999 | -48.942501 | 2025-07-19 00:28:00 | METOP-B | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c81cd1d-057f-3763-a92d-d05391b72012 | -3.5844 | -47.520199 | 2025-07-19 00:28:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d99f6a63-c32a-36a0-80ba-d09efc0f9979 | -22.8402 | -46.848202 | 2025-07-19 00:28:00 | METOP-B | MORUNGABA | SÃO PAULO | Brasil | 3532009 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95c94724-ddbb-3585-894b-c03db612fb7e | -11.4851 | -47.321602 | 2025-07-19 00:28:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c32de66-9cf1-3ea7-96fe-d00e78f383ce | -4.3071 | -48.1077 | 2025-07-19 00:28:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a40f3793-abc9-35ac-8896-41a1d894acb3 | -9.9452 | -48.1502 | 2025-07-19 00:28:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60556a80-6bf4-3b5b-b3c0-2b8e1005a97e | -11.5658 | -47.094799 | 2025-07-19 00:28:00 | METOP-B | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a21a2c5-2e67-31d9-a16a-ac15b41b0441 | -10.6084 | -44.7477 | 2025-07-19 00:28:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ea84ec7-b622-3802-925e-b4b04db1e6be | -22.700001 | -47.238201 | 2025-07-19 00:28:00 | METOP-B | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7e4bb84c-737c-3d78-b0ad-7a19f612d711 | -11.7374 | -48.179798 | 2025-07-19 00:28:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| adbda540-4e7d-3961-86e7-01ea858ec0dc | -19.725 | -51.678501 | 2025-07-19 00:28:00 | METOP-B | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb1b04c-e8ee-330b-95fa-050ec76af2dd | -3.035 | -49.426399 | 2025-07-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1234a99f-83a1-3d0b-9d52-f88e0aebac3f | -10.6247 | -44.767 | 2025-07-19 00:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 25aee565-0389-367c-b664-cab144f964b0 | -2.9109 | -48.2325 | 2025-07-19 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 6cf73e28-f6fa-3df9-832e-31434b7ddb9c | -6.1606 | -48.0507 | 2025-07-19 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 190.0 |
| ffc0dff5-171d-30c0-ba80-acc1e6506408 | -11.7317 | -48.1849 | 2025-07-19 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 287.6 |
| 2408baa4-55a3-35a5-ab64-83f542eb0ea1 | -7.4735 | -47.493 | 2025-07-19 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 7f8db2cc-23d5-35ce-b582-459861c5c561 | -2.9108 | -48.254 | 2025-07-19 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 0eba6855-3f93-3bdd-80d8-7fef5275ed2a | -11.732 | -48.1628 | 2025-07-19 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 1e918b2a-2114-3f30-b555-2308caf448ba | -11.4786 | -47.3306 | 2025-07-19 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| af5658b4-f487-35b4-a19a-c8b9ea673606 | -11.7313 | -48.207 | 2025-07-19 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 5277a664-1968-3894-bfd6-553b3f899942 | -11.4977 | -47.3281 | 2025-07-19 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 160f28e8-f1d4-3941-ba6b-f9a3cd7fd103 | -10.651 | -49.2967 | 2025-07-19 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 933db17e-ad4f-3165-8d10-14fc6c2d39ae | -5.6379 | -43.7175 | 2025-07-19 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |


[Clique aqui para ver as próximas entradas](README5.md)
