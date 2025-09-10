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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ef35a07-ab3e-3266-98ad-2c150fff7f2c | -8.02265 | -44.50388 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ebac205-3e10-3527-899e-457e1b5cb3da | -10.48461 | -49.37513 | 2025-09-10 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f0523b0-3e6c-37b9-a420-15293ce0033b | -11.11222 | -48.45931 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b12941ea-0468-3209-8b91-6f5134700ce8 | -10.00057 | -51.70124 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8837b1fb-3be4-33c1-8f81-817d78c66f89 | -7.67209 | -50.27488 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b552229e-bae2-386f-a7bb-6edb3f0b3f5e | -7.00022 | -45.64993 | 2025-09-10 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6eaa843-fbf4-3674-b266-4d6b7b257180 | -9.43538 | -46.71166 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7324a437-7457-395e-b8ca-033d21309b25 | -10.00337 | -51.70546 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d71bd8d-afc6-3c7c-b914-6eec3305a33a | -9.66427 | -46.64545 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e802d7a5-50e0-307a-b103-a65dd59d1d44 | -6.88413 | -47.89166 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7490ebc6-2905-3f0c-9145-427d38924054 | -8.78585 | -44.40701 | 2025-09-10 04:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f8cf804-7f5b-389f-ad1b-7eec8199c511 | -7.44572 | -49.26312 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5468b2a1-8d6d-3814-a13a-57034b15a5cc | -12.41819 | -44.72683 | 2025-09-10 04:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 200015b6-98fb-397d-b272-b28114b4f084 | -9.70698 | -51.00719 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ba97950-edaa-3000-a143-d072194cd92f | -9.07256 | -45.7097 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e6c05a5b-21a0-3de7-96eb-0685a82afa02 | -8.42055 | -47.27849 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 099977fc-3226-307f-bbe1-58849acbb9a1 | -8.06505 | -50.1834 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a32662c4-7076-3318-ba70-13419db3667e | -7.67042 | -50.26387 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ccee4cd-6760-3e65-951f-0acc3a6a205c | -9.44213 | -46.71684 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e220f636-d317-3018-9d95-44ebb69d6f5a | -7.84339 | -45.41362 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba559e8b-182a-3809-9839-ca480d1a517b | -11.95401 | -46.65833 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb36d945-d572-38bc-8f5e-6b5e46a40e82 | -9.83162 | -46.05258 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f1742d7-0892-3129-b45c-877e23388733 | -7.79577 | -46.0682 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58cf9291-1515-3211-ab70-25418a091419 | -7.7792 | -46.05186 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 935ea912-188b-3a87-bc10-aa6e147f274e | -7.54934 | -44.65258 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e30a0d14-7d16-3127-9b7f-1fbe747ff9e2 | -9.45134 | -46.7051 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e180256d-4576-3b54-9b34-62a21707c9bd | -9.06955 | -50.48098 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6b030de-d590-3555-84a6-bbf1bdf0658c | -9.04252 | -49.80211 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1eae11cd-d5ac-3a78-b8a9-abed57f505a7 | -7.68229 | -44.76467 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb75f5a7-6b2e-342e-8626-dd357905506c | -8.03014 | -44.50052 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed1db2ac-f9ce-321c-9ddf-345fb3c7c24e | -8.46427 | -48.95463 | 2025-09-10 04:42:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8476c760-6baa-3cf4-ac10-12e110a025f0 | -9.22102 | -50.53044 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a5e3439-1d31-3257-8d8c-87097679b490 | -5.73241 | -51.68721 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 234e808a-3cfb-3c09-93c8-90868f5f9cd4 | -8.07172 | -50.18443 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80ffe725-5a1e-38db-969e-89fa66359d2b | -7.74211 | -50.74129 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f81c8730-c738-3629-a448-b7e8edb4c72a | -8.66833 | -45.74352 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d86d02f-09b2-3b82-afa1-7db633d6411a | -9.01755 | -49.78738 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b32f75f-3308-34aa-8567-841ca1d02b66 | -6.84771 | -47.9231 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f274fb8-5010-3f5c-b7e9-21686a22cbf8 | -8.20938 | -47.15122 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d86ba977-bea0-3530-82dc-598524689e94 | -9.61223 | -48.03907 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14dd529d-e0d4-3edf-9ef8-b018329cc8b0 | -7.76216 | -50.76656 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3cb05317-cd02-3766-b864-b9e6911f5255 | -9.05528 | -49.80773 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f227275f-a5a3-3bfb-8ba6-038f7ab88dbd | -7.74717 | -50.73124 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e67fa29-5bda-363c-8115-f798d834602b | -10.04393 | -49.16033 | 2025-09-10 04:42:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea330166-fc9c-3c0a-bf18-ade79bae649e | -9.06703 | -45.74794 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1aa7c8d4-23bc-3385-a309-b962c826cec3 | -11.45218 | -43.62704 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01c35d8d-c83f-31d5-9e7f-37aeb5c7f177 | -11.19221 | -48.37445 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66e9e892-a17e-3fd2-82b0-3c92655b70fc | -10.57398 | -52.04072 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bd9a7a6-4239-3b63-a0d6-527d19b5e462 | -8.34402 | -45.04727 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a4cdcfc-6c20-3122-89f7-0a7e862cd77f | -9.69686 | -46.85754 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6edd8123-c749-3876-b02c-2c649be224ae | -8.04358 | -48.68945 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 91a6a32e-4eae-3c72-8d8a-22c5b371612c | -7.98177 | -46.33198 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 148e702b-61cd-3752-93f4-51e84e191692 | -9.07344 | -50.47802 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dddf5edb-c522-32f0-a929-01407ed8b615 | -10.0149 | -51.67727 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6365832-7e54-3330-bd98-6e4775de70b0 | -9.43906 | -46.71218 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91273cdf-57ce-33e9-9212-aec984a8f048 | -9.74601 | -51.09412 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 284ded9b-f399-32b9-8b73-17a05bb9788f | -7.74111 | -44.75624 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 842e0e4d-3808-3f9a-8f22-f6fcc4c5c1a8 | -10.14689 | -46.17648 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7efdb68f-c973-3f18-9dc6-9eb6c4c6f3c4 | -6.84941 | -47.91217 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 007c910a-4b31-3f6b-9131-91fbb75f4242 | -7.85396 | -46.01984 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cded5698-47f6-3b73-bab9-77df55173ff4 | -9.31223 | -46.71905 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 057a1aa6-7820-39ef-a687-5860a1a64823 | -6.39244 | -44.44388 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30bd1de6-13c3-34f5-840d-18abc6b3a43e | -8.85413 | -47.26712 | 2025-09-10 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1d5ae53-5c46-336c-9d2d-fc65f47287ef | -8.31457 | -44.82513 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b5a06e4-310f-36a1-8774-552879e241fa | -8.05033 | -48.70102 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2fa86a51-d975-3f7e-b78d-6c23afaa96df | -6.8596 | -47.89148 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d189012-5192-36cb-bd41-c19f0f1f979d | -8.47872 | -47.29968 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8639569-d955-3b9f-9bec-9d3f75c7dc04 | -9.75382 | -45.4048 | 2025-09-10 04:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d56ffb9c-9ea4-3a3f-b08b-164684caa239 | -8.47934 | -47.29567 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8daa3b97-c215-3a46-9649-20bf5c0ae2f5 | -10.57738 | -52.04131 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 834599ff-a68a-37da-a7a2-5328c9e50648 | -6.87619 | -47.89797 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60aab7b4-90e5-3069-a34a-ce73e92fb032 | -9.51651 | -54.64935 | 2025-09-10 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fb0dc99-df40-3df2-b802-058db28e4e95 | -10.88432 | -55.69708 | 2025-09-10 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2a4fdf8-41bd-3782-8f7f-034d3750f908 | -10.65228 | -48.60278 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f21931e-79ba-33d8-968d-c5986214a8c4 | -10.57458 | -52.03701 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 240950c0-1dcc-3f2b-a3a2-0fa0a2000a77 | -9.66189 | -46.62013 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4c91abb-4fb4-3a72-9e7c-bc150fe555c4 | -7.86414 | -46.25556 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c18afe3-72ce-318a-9cd7-e04158509a4e | -7.49089 | -48.23293 | 2025-09-10 04:42:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a297a2f9-7edb-33d4-91ec-799836e5052a | -10.41348 | -57.18199 | 2025-09-10 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09952004-d53d-33d5-9190-74fdd4632ea3 | -9.66005 | -46.62242 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37f2766a-c6c3-3568-9f6d-b5258156f6e2 | -10.83869 | -47.75819 | 2025-09-10 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a5de39a-2d98-3476-a128-0c2883529606 | -8.02731 | -44.50077 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f993220d-99a7-3f1a-9f43-e9e3523641d0 | -8.27443 | -47.43799 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5599483d-ba60-31e6-bd51-3ea07f5ddcaa | -8.57243 | -48.95312 | 2025-09-10 04:42:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e80dbdf0-7e10-3576-9fdf-13ad48eb40b1 | -7.44239 | -49.2626 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a6cb63f-44d9-377e-8d95-4018aa0b7309 | -8.02321 | -44.50014 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e547ea4c-ae9c-3307-980b-a64758450aed | -8.69755 | -48.88919 | 2025-09-10 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2b611e4-b731-3278-87b8-977fb280b538 | -7.55743 | -44.65379 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b54b1381-62e9-3eae-ac54-a9274c4c5e42 | -11.15931 | -45.28373 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdf58358-5086-33de-8e80-804bd95652c7 | -7.73701 | -50.75154 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff2005e5-3156-351f-a79f-03ff7a5af1dd | -10.01686 | -48.103 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ad89782-5811-3811-8b12-233938941cc0 | -6.99644 | -45.6494 | 2025-09-10 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5366f8f2-1336-3bc4-93e4-eeafcafb797a | -7.35577 | -44.30677 | 2025-09-10 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63be6a6d-8172-3bda-ae6c-9d222b36e1b2 | -6.92157 | -44.93109 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 819b5360-e838-381c-b11c-103cd62f0fe0 | -6.88128 | -47.88751 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ca4a1eae-56fc-3f59-9cbc-69007f68f6b1 | -8.87118 | -51.04009 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd712d2a-b1fd-3481-a8e9-3442445adce4 | -6.64405 | -51.98458 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4129d0bd-577c-3f89-8a21-a09de69a29e5 | -9.52238 | -48.32952 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59bb59c5-327c-363e-a8d9-0399df3612ac | -9.71593 | -46.82996 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d1384d8-68a7-39c5-adea-40b8df36958c | -9.44519 | -46.72149 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README62.md)
