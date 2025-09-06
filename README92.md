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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66906fb6-1afa-355d-9995-439b9dd068d1 | -7.6881 | -50.2991 | 2025-09-06 13:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 15cc207d-a310-326a-9d43-67c2370f6b77 | -10.3324 | -46.445 | 2025-09-06 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 89e85f30-37e1-351f-a363-f5c00df8522a | -9.7029 | -51.1013 | 2025-09-06 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 693cd9ee-1f73-3065-ba0e-4215d25a76fb | -9.7031 | -51.0802 | 2025-09-06 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 66f46f8c-328a-3a94-b6f6-d874bf1a04a3 | -10.3327 | -46.4225 | 2025-09-06 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 1de53cca-bfea-3a8a-8c06-8ee3395320b1 | -6.2125 | -42.4769 | 2025-09-06 13:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 185.0 |
| 9ae77ab9-0492-35de-9f8f-ace5159dcd72 | -14.1057 | -51.7327 | 2025-09-06 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| e215bffd-13c7-3b8d-9f9e-f135e25c0876 | -10.3137 | -46.4248 | 2025-09-06 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 206f9ec0-ae57-3559-9c9d-783a8ae461b3 | -6.2203 | -43.5791 | 2025-09-06 13:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 86be8bc8-ad3c-3796-8ec0-208adecb3887 | -5.73 | -43.8958 | 2025-09-06 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d47faa2a-b539-338b-a469-a0e63e1807db | -11.0242 | -45.9729 | 2025-09-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 723545ca-77b8-3c49-85bb-86a82048cc2d | -6.2036 | -43.3709 | 2025-09-06 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 86c26b6c-a7e2-3366-bbc9-c9fd015cd49e | -15.7377 | -53.5928 | 2025-09-06 13:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| a23b4a78-0757-33c5-bf97-d75cabb11596 | -5.7298 | -43.9189 | 2025-09-06 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 236.4 |
| 860bcbd1-6645-3b90-a5a6-a41034e5dc35 | -15.7182 | -53.5954 | 2025-09-06 13:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 2de23faa-65e3-3f22-9add-77debe3fd15e | -9.0951 | -47.0093 | 2025-09-06 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| d719b044-afe9-3590-854d-91c244817c24 | -9.6841 | -51.103 | 2025-09-06 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 158.4 |
| cca31c31-9e70-3869-8c37-2f7d7fade5ea | -11.0055 | -45.9527 | 2025-09-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| b39cf16b-66c1-3663-a7ff-4a12b4eb6fe8 | -10.314 | -46.4022 | 2025-09-06 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 88d1d400-287f-3cc6-928f-a7df0bacdb4c | -4.8011 | -43.054 | 2025-09-06 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e0a6a0b2-edc4-3535-be19-3620070ceff1 | -9.8079 | -46.0118 | 2025-09-06 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 7f3a7c2b-dbad-3558-ae6e-a86b2add6432 | -11.2302 | -46.1949 | 2025-09-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 2505c0ad-79bf-32b5-8e06-6d9df6aa27ae | -5.73 | -43.8958 | 2025-09-06 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| acf39959-78be-3585-9310-f2676c813bb0 | -13.0161 | -48.0549 | 2025-09-06 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| aa5330e2-68a2-363e-ad71-59612a4bd4b9 | -9.6843 | -51.0819 | 2025-09-06 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 234.0 |
| 85dc5e87-585e-3035-82f7-baca2e4e03e4 | -15.7182 | -53.5954 | 2025-09-06 13:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a7f68769-af68-3612-9f68-f080de6427a0 | -9.7029 | -51.1013 | 2025-09-06 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 42144e90-1bf5-3630-b187-966ac230f74c | -7.8593 | -44.9053 | 2025-09-06 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 186.9 |
| eb99fa3b-8d34-3d5e-8698-106d0191b9d1 | -5.7183 | -45.2226 | 2025-09-06 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8dac2569-e437-35b1-84fe-141c96b65540 | -15.3067 | -52.6995 | 2025-09-06 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| a818e2fb-8195-3915-b736-7f5f1ba1cfda | -6.2038 | -43.3475 | 2025-09-06 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 91fcdea6-abcc-34df-ab25-2397dc1cd99d | -9.6841 | -51.103 | 2025-09-06 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 330.4 |
| e690311b-be3d-3af1-b21e-24ac657cce5c | -12.8028 | -48.1739 | 2025-09-06 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| bfb81b62-52a7-3f7f-98e9-dcacd0dcb504 | -15.7186 | -53.5743 | 2025-09-06 13:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 8134979c-2acf-3693-89b0-4dfe63a064e6 | -11.2306 | -46.1722 | 2025-09-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| da3f1b28-c629-390f-aa54-3159afe6932f | -15.7377 | -53.5928 | 2025-09-06 13:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 34bc505d-e8aa-31eb-8713-6c3d27ebe704 | -10.3324 | -46.445 | 2025-09-06 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 9184a99c-fdde-3390-a19a-afe579fe20c3 | -10.2187 | -50.5223 | 2025-09-06 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 2238622b-b0d8-3fd8-96e0-269c76ca30f3 | -6.2036 | -43.3709 | 2025-09-06 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| e2ad636a-8402-3e32-9eb1-6f456bcb95f0 | -11.2651 | -46.3938 | 2025-09-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a1609ef1-dea6-33c2-895a-5d7139625f7f | -13.8006 | -52.7454 | 2025-09-06 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| bc093e99-8196-38d0-a455-2ec33a6650a9 | -9.7031 | -51.0802 | 2025-09-06 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 6d030db0-b3ff-3429-b24f-5ad67fdd98f0 | -13.0353 | -48.0521 | 2025-09-06 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a0ec0af4-d363-3b26-8613-17e60b144f7d | -10.6128 | -44.3284 | 2025-09-06 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 197.5 |
| c9cf0be5-ffcd-3f6b-842d-4a42843c08cf | -11.3567 | -50.3161 | 2025-09-06 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 6f5f8205-4bec-3d5a-b299-bcf6f3f28290 | -6.2203 | -43.5791 | 2025-09-06 13:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ac1d3d21-c0c5-31c9-b709-2e03ec6d319d | -6.5138 | -42.4266 | 2025-09-06 13:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 036018c2-43cb-380c-81db-8705b1c9070f | -10.3327 | -46.4225 | 2025-09-06 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 48ae1ecf-23f8-34cc-9987-25aa213aae93 | -6.2421 | -43.2743 | 2025-09-06 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 87e102ae-8346-3d4d-a365-4a1a5e9e29a0 | -6.2127 | -42.4532 | 2025-09-06 13:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 144.7 |
| cb8c1862-007a-3d6e-94fd-bc240dd256d8 | -11.2298 | -46.2176 | 2025-09-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5e02d65c-86ca-37cb-b80b-dbe8cf93abda | -5.7298 | -43.9189 | 2025-09-06 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 8ca92d23-1da7-3b45-b416-a6404f7b4781 | -6.2125 | -42.4769 | 2025-09-06 13:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 178.4 |
| cf95db70-8a58-333f-a21f-abe334ebbe64 | -10.2184 | -50.5436 | 2025-09-06 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| aa037e7c-a8e5-38b4-9060-b840b371bc61 | -10.314 | -46.4022 | 2025-09-06 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8b067c9c-1002-30d4-ab79-0693edad6b04 | -15.7381 | -53.5717 | 2025-09-06 13:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 5f310a76-74ac-3c3c-93c6-3484b2392058 | -10.5937 | -44.331 | 2025-09-06 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 3fab7574-d72b-3409-8064-1f6a87904744 | -7.6881 | -50.2991 | 2025-09-06 13:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 90e4e280-8924-376f-871d-4ced6585bd90 | -11.2111 | -46.1975 | 2025-09-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| ab184a88-78fe-356c-bfad-df349e5af2ea | -9.0948 | -47.0316 | 2025-09-06 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| af54428d-1fac-3627-86f3-365725e7c522 | -10.2373 | -50.5417 | 2025-09-06 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 6ec84be4-8f67-39ee-b5a9-1b1eb0724d43 | -11.2302 | -46.1949 | 2025-09-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 344.1 |
| 440d7aaa-75a8-308a-8be2-82f37a876ff8 | -15.3064 | -52.7208 | 2025-09-06 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8689124b-23f9-3a36-974a-57b21184261a | -6.2418 | -43.2976 | 2025-09-06 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 7e83deeb-01cb-311f-832f-e427e9e0ca91 | -9.0951 | -47.0093 | 2025-09-06 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 7258d86b-3ca4-3abc-baaf-9d06855a04aa | -6.4021 | -46.0944 | 2025-09-06 13:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 30aab3c6-27b1-3794-a734-9e4973e69843 | -5.7296 | -43.942 | 2025-09-06 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d1a57dac-1287-3f0c-b4a6-451a304840a4 | -10.3137 | -46.4248 | 2025-09-06 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ad965363-0e9e-3da1-a024-42bf7b440c36 | -15.7186 | -53.5743 | 2025-09-06 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 0e7b0a63-47d8-3273-8bbc-d39761c28dc7 | -15.3067 | -52.6995 | 2025-09-06 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 9bc6ebe4-b41a-39f8-a53a-29ad3c7617fc | -6.2421 | -43.2743 | 2025-09-06 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 82ff0eeb-449a-3154-aa3c-6f9fc32a7eb1 | -5.7296 | -43.942 | 2025-09-06 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 545c986f-2c00-3997-a444-58c76286621f | -15.7182 | -53.5954 | 2025-09-06 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 4b7feac5-2e42-35de-98a1-2c5cd3122d12 | -15.7377 | -53.5928 | 2025-09-06 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 58082866-2c07-30c1-90d4-a3606eb946bf | -11.758 | -47.739 | 2025-09-06 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 623621bd-785c-3ea4-8224-76cfc1a0fa27 | -9.0951 | -47.0093 | 2025-09-06 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| bb2ab805-9d5d-311e-97c2-52e536172d4e | -5.73 | -43.8958 | 2025-09-06 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| b724827a-9853-35d9-97eb-36f5cd0d7a1f | -10.3137 | -46.4248 | 2025-09-06 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 9916078a-c2f4-3439-85af-c6fd078f07d1 | -5.7298 | -43.9189 | 2025-09-06 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 364.1 |
| df21e96d-36a5-3e50-9733-56c7927bc2b2 | -11.2651 | -46.3938 | 2025-09-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f91a8606-b639-3315-af50-7c1c0f2e886a | -6.1577 | -44.2317 | 2025-09-06 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d18027fa-a36e-32a3-aa1c-6506cadc1520 | -9.7031 | -51.0802 | 2025-09-06 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| e622be32-2ee0-39d8-99c9-b4bb4701b1c1 | -6.2125 | -42.4769 | 2025-09-06 13:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 9bb069f5-5573-3956-ac35-88e938b7f57b | -13.8006 | -52.7454 | 2025-09-06 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| fbdad838-63ca-3706-ae91-d32cde3185a9 | -10.6128 | -44.3284 | 2025-09-06 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| e0117698-c6d5-313b-8573-55263d9a2089 | -12.8028 | -48.1739 | 2025-09-06 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a422dba9-40d7-3833-93e1-c279bb4b639f | -11.2306 | -46.1722 | 2025-09-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 09d6d298-ae75-3199-9d16-5cb99e0f4cf8 | -7.0316 | -43.2507 | 2025-09-06 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 1faf4e59-d46c-34de-883b-dc66df885adb | -6.5138 | -42.4266 | 2025-09-06 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 818199f7-4cb1-39ca-a890-b8d0c3e46791 | -10.3324 | -46.445 | 2025-09-06 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 630863e6-b1e7-334e-9944-d6dcb0a9e7a9 | -6.2418 | -43.2976 | 2025-09-06 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 3d94400f-82a2-3e32-8b0d-34bf094d7e50 | -6.0948 | -44.9455 | 2025-09-06 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e4fb4c06-30c3-3bb0-90e8-525de855f148 | -11.0051 | -45.9755 | 2025-09-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 811438d2-098b-3183-8c1c-b5b0cf620d8e | -8.099 | -45.3144 | 2025-09-06 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 30b0f315-8519-3c1d-9579-c4a983b80948 | -6.2203 | -43.5791 | 2025-09-06 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b7967316-15f3-3e21-9343-7fab472dd866 | -10.3334 | -46.3774 | 2025-09-06 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 00fe6a1c-020a-3728-9ff2-78ea02203fd2 | -6.2127 | -42.4532 | 2025-09-06 13:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| a7fbd9fd-2102-30a6-937d-782596ebec1e | -9.0948 | -47.0316 | 2025-09-06 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 97d1818b-cc58-3920-b2e8-e4f60dd066a8 | -6.4021 | -46.0944 | 2025-09-06 13:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 492fd7cf-53e9-3b5e-9842-08cd388a1dc3 | -15.3064 | -52.7208 | 2025-09-06 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |


[Clique aqui para ver as próximas entradas](README93.md)
