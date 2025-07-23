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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13e9f6f0-80d6-30b1-a420-b5f3812f5cf6 | -7.2786 | -44.37516 | 2025-07-23 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f58db237-4c08-3aca-89c6-19ce58e0397f | -10.50827 | -44.8851 | 2025-07-23 04:59:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a04d26dc-697b-3b48-9a51-e6465ddb312c | -10.43197 | -54.37918 | 2025-07-23 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50dbf983-2a63-39f3-b416-882c6055a150 | -6.97511 | -42.7962 | 2025-07-23 04:59:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc12fc54-8f34-3c45-a81d-2507641384e3 | -9.05325 | -45.06579 | 2025-07-23 04:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4816d463-52f1-394c-a8e5-d61f47f7fcb7 | -6.88991 | -45.24656 | 2025-07-23 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a5781e2-ba13-3b02-8c52-4259ab04c2a3 | -9.33316 | -49.84227 | 2025-07-23 04:59:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 783d29e4-668f-3276-8831-719da176e508 | -10.63563 | -45.23466 | 2025-07-23 04:59:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3d2fc84-3dea-3f00-9345-36038c03e2c2 | -7.02574 | -45.84917 | 2025-07-23 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6fd4f27-2b60-30e2-a0e4-d095fdf4406a | -7.2331 | -44.78502 | 2025-07-23 04:59:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f00637da-5653-3e68-944f-cd10c802aa4b | -8.95886 | -62.21219 | 2025-07-23 04:59:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48295cee-dbd1-3920-9d23-d8ffdab4aeef | -6.60868 | -42.40801 | 2025-07-23 04:59:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9814b95b-3630-3df4-9d50-ede71f3b7049 | -9.76615 | -48.58304 | 2025-07-23 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b10a62b-472b-3e5e-a2d7-19daf3faa970 | -10.71884 | -49.48235 | 2025-07-23 04:59:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72be607c-e122-389a-a4bf-6dc23f69f1e2 | -7.54894 | -49.67063 | 2025-07-23 04:59:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13503d2d-fe62-344c-b306-1b1c1d6c63a6 | -7.04611 | -45.85276 | 2025-07-23 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 488a634d-b7ea-380e-af44-705f54df3550 | -10.7183 | -49.48623 | 2025-07-23 04:59:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03c9fef4-2c07-3696-846c-4e4a4e96fcb7 | -6.93429 | -44.31042 | 2025-07-23 04:59:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6025f86e-d7ca-3d73-b186-80e9b2bd4b6b | -7.28509 | -60.17434 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9aad7e5-f7f7-3bc9-b5a5-95fd1673323b | -7.52651 | -45.38772 | 2025-07-23 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03741b82-044b-355b-bba8-2eb7c63a6d1d | -7.27982 | -47.53029 | 2025-07-23 04:59:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b57a4867-4b8c-3fd3-9e9b-9669bd359531 | -7.75105 | -44.0291 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 75f8a08f-2884-351f-b60f-2521482483f8 | -7.887 | -45.552 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 066e2760-4cb3-376a-981a-a6e0233d46ed | -7.04696 | -45.84662 | 2025-07-23 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17d38e61-bd8e-35b0-a1f1-8cb09501d405 | -7.74634 | -44.01993 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| da4fbfbb-978f-337b-a6ed-11ba3f1835d3 | -7.29496 | -60.1678 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51a5126c-74a4-364e-811c-92066ff1f424 | -9.43223 | -48.85767 | 2025-07-23 04:59:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd09d723-b9f6-3774-8525-ec8dc3115ebf | -6.88463 | -45.2455 | 2025-07-23 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df6a00de-26b3-3817-828d-ffb40e80465f | -9.43655 | -48.85819 | 2025-07-23 04:59:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4460342-1ddd-3160-82b0-f5e99fe01d6c | -9.74407 | -48.58009 | 2025-07-23 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80ce22c7-46d5-31bf-bac8-78e41a1bdd02 | -7.89229 | -45.55272 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8466ab92-2a97-3d0a-9b59-95fc51858207 | -7.2326 | -44.78861 | 2025-07-23 04:59:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 004d0043-bf9c-3ff0-a786-3db7156e3678 | -7.52699 | -45.3842 | 2025-07-23 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 165e3094-cdb3-3193-b45d-cb5763a9f26a | -9.05982 | -45.05881 | 2025-07-23 04:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35de2774-ac4f-3a64-a2e6-7f3ef4da4d33 | -7.25097 | -44.28045 | 2025-07-23 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 531ad4d7-b242-3228-b83f-2f2cde96bc65 | -7.2766 | -60.17287 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28e9767d-01f6-333b-8758-e08a28b70cad | -7.75214 | -44.02108 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1eaad17f-17a9-34c4-918f-d6ea1893ebdb | -6.92858 | -44.30993 | 2025-07-23 04:59:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fa03e60-6c9c-3ddf-86bc-fd8f5e92bac8 | -6.60937 | -42.403 | 2025-07-23 04:59:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 10f552b3-930a-33aa-87f8-99180494bb4d | -6.97856 | -42.79314 | 2025-07-23 04:59:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| db5f0072-1378-3085-aaa4-85d740081385 | -7.72451 | -55.13444 | 2025-07-23 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1fd6693f-384e-3529-832a-ded6c5cb0459 | -7.06839 | -43.92764 | 2025-07-23 04:59:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfc03bd2-8de5-32d1-bd13-715af8610d6d | -7.89185 | -45.55599 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0f62b9f-31bb-3e04-84f7-e24606dd2d2b | -9.13864 | -50.77943 | 2025-07-23 04:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 291acc03-80b6-3fae-bcc5-2a1fd2f5d5bf | -7.7458 | -44.02398 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a44aff21-3c1a-3dde-a015-9322222a6d7e | -7.06784 | -43.93175 | 2025-07-23 04:59:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0bfdab4a-13a3-3637-a27a-05c718744419 | -7.19868 | -48.23708 | 2025-07-23 04:59:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d246e591-b588-36d5-80d5-a1c95867ab17 | -7.25458 | -44.29672 | 2025-07-23 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c6d568b-32f3-3c09-88f5-216d05fbca64 | -7.76306 | -44.02307 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e929866d-ef03-3344-9b10-730f87d75a99 | -8.91214 | -47.35954 | 2025-07-23 04:59:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d431e65-9a3c-30fe-ae34-3a36d78c46c2 | -7.7574 | -44.02612 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a6672d9-18bc-32e3-9ee8-d5d585c37369 | -8.73411 | -49.48537 | 2025-07-23 04:59:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6100f6ec-7ada-3d3d-8fee-1936d5676890 | -7.20336 | -45.33524 | 2025-07-23 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1d7b1c3c-087d-325a-87e8-26c1f1b95c26 | -7.47638 | -49.22736 | 2025-07-23 04:59:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e58eb82-e0f8-3c1d-9276-bac07f029588 | -7.26842 | -44.3652 | 2025-07-23 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d5b651f-cc01-321e-96f6-44c815fccd39 | -9.05928 | -45.06292 | 2025-07-23 04:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6afcc9bb-097f-3aba-8c36-ad231632cfe4 | -10.89114 | -44.36766 | 2025-07-23 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 331d0141-e843-3736-a57d-6d0d59f4a136 | -8.19299 | -50.21208 | 2025-07-23 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8950767e-ba75-3088-9cfd-275a8290e5b8 | -7.19269 | -45.33404 | 2025-07-23 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 854c77a9-7cc2-36ae-b96b-0225baf57417 | -7.22094 | -49.59563 | 2025-07-23 04:59:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3bef18af-e202-393e-9efa-462bd9139774 | -7.88845 | -45.55278 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cb5756b-812e-3a9d-abf5-95309f72150b | -7.91279 | -49.64449 | 2025-07-23 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c973d25-ecfc-3a05-abd3-d8dca3adb2b0 | -8.28898 | -44.96568 | 2025-07-23 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4baaf454-5fdc-388e-ad54-c33455eb8ad3 | -9.06435 | -45.06741 | 2025-07-23 04:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01f6a4c0-50c7-37bb-be68-96109c7dede3 | -10.23257 | -56.77056 | 2025-07-23 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e4d37cb-3599-382d-bc21-30b8c39c5ed2 | -8.28913 | -44.96661 | 2025-07-23 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e99239cc-6a61-31ca-9c86-9debecbc8d27 | -7.14408 | -46.10255 | 2025-07-23 04:59:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1db52d8f-7f50-3110-85b3-689547fdc10e | -7.25794 | -60.18583 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49d2f072-73d3-3f34-8edb-80a1dcd16a75 | -10.87975 | -44.36195 | 2025-07-23 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35a9d415-0b9f-326b-afb9-17df83bc8c63 | -7.76253 | -44.02715 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d6cdf6c-cfad-394e-b4ec-f1c8ae066ef1 | -8.05618 | -49.9716 | 2025-07-23 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45ef0cd1-d3a9-31b1-8339-f8ba280d0b63 | -10.63612 | -45.23078 | 2025-07-23 04:59:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a715e1c-1139-3a2f-8c8d-f4a41c82a5af | -8.28863 | -44.97025 | 2025-07-23 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f88b4da8-dfce-3896-bab7-c82597767f77 | -10.68515 | -47.21111 | 2025-07-23 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51509453-a207-3ed9-b216-cb10b7e1a220 | -7.75852 | -44.0179 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 274cccfc-731a-3aa0-bfe9-7cd659c183b7 | -7.1989 | -45.32817 | 2025-07-23 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3238b0a2-d295-3ee1-8540-b60d30a61074 | -10.88572 | -44.36266 | 2025-07-23 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33ed8627-0d99-36cd-9082-24c7dacfa728 | -9.06483 | -45.06375 | 2025-07-23 04:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2bb429d-cae2-36ac-9f29-3310dce313ac | -10.06461 | -46.8311 | 2025-07-23 04:59:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fedcfb6-c6ef-37c5-8570-89231ebb10fe | -12.28503 | -50.27795 | 2025-07-23 05:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04d3c505-f37c-319e-93c1-77f2bd42bb48 | -13.53969 | -43.70602 | 2025-07-23 05:01:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d44b35a0-f75e-3343-a3ea-b63e63e08b5d | -12.49796 | -57.77152 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bba716ea-2cce-393c-915a-b23fc9e84148 | -12.66545 | -45.03728 | 2025-07-23 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07d8ec03-d870-3593-95fb-b69353ae9426 | -17.56694 | -47.50562 | 2025-07-23 05:01:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22912a5a-dd26-3b6c-8089-a1a1ae1c9daa | -10.04136 | -59.10114 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c65ae304-af3c-3a58-87b1-ce2443890b9b | -16.03655 | -43.72523 | 2025-07-23 05:01:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd68c511-64df-3535-8093-bbfc44d8db1b | -10.05739 | -59.09904 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48687c1c-6f99-3b46-b109-3d0dfcaafe3f | -13.70392 | -45.69567 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32ac794a-5473-398f-8293-374a21551e5d | -10.0658 | -59.09564 | 2025-07-23 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77cfb38e-ad42-3df6-b571-15f5d8d6af0c | -12.50078 | -57.77599 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00be82a2-8620-3ede-8429-a3450f00c948 | -15.81487 | -48.35553 | 2025-07-23 05:01:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 979a221b-0186-3ccf-856c-a886db9189f8 | -12.34674 | -63.39468 | 2025-07-23 05:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a05cb422-800a-3a79-a261-10f1252bbe78 | -12.4945 | -57.77093 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29bd775e-23d5-38da-85e8-325033ece646 | -12.35234 | -63.41824 | 2025-07-23 05:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 44375b9d-3db3-3de6-a148-251aed6db655 | -13.72458 | -52.00647 | 2025-07-23 05:01:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dde151d7-cde8-3164-ad35-3d63545676f2 | -13.7008 | -45.69577 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3241315c-3e19-3459-9250-00c94376db51 | -12.50206 | -57.7683 | 2025-07-23 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 735226aa-535d-3558-8154-89c0e532aed1 | -13.69825 | -45.69496 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66ee954d-51bf-3ee1-9525-134bfd8e2d71 | -13.70647 | -45.69651 | 2025-07-23 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c4ee91a-268c-315e-a72a-c9577dac0d2e | -12.57963 | -56.97789 | 2025-07-23 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
