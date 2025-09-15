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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ff9d382-f635-34c1-8333-d3b4c2050397 | -9.28657 | -61.92911 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24401f9a-1f67-30cc-b661-514302fa70db | -7.64352 | -49.72012 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca82a0db-fbc0-3622-9294-21be0eeb9089 | -8.98518 | -45.81679 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93a8b5ad-2e01-3dd4-8959-71882a2b7ffb | -12.00687 | -46.66611 | 2025-09-15 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 79daed46-7317-3dd0-94e5-6c8b6ff8b347 | -8.97632 | -46.2154 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 21f588b5-e972-3677-b7b0-33850cce5c17 | -7.88485 | -63.70252 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 602c0d8e-835c-3492-91d4-437a387ec36b | -11.80028 | -50.50079 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca2ae8c9-d027-3c9f-8e74-f2726b3a2980 | -12.01378 | -46.66208 | 2025-09-15 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b2cc6cc-00f6-33a1-99dc-77debe7c5167 | -10.17892 | -46.15532 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd8306ae-1adc-3538-acb3-7274a72c2154 | -11.83741 | -50.44802 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebe0f219-c0a8-30a0-bf44-b144f6cf57d6 | -7.69613 | -44.67177 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ea1cae0-aca8-3b84-ac35-ad82fd6dc8be | -11.99933 | -47.75713 | 2025-09-15 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c2c8619-9264-3b5a-aaa2-241f1325ee8b | -10.15393 | -46.14624 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca1b2e20-9dbb-38a0-8906-74d87be4aecf | -8.63748 | -45.69237 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6bde3f51-d143-35ec-9880-f713779cc123 | -9.69371 | -61.9981 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0945626a-22c4-300b-954f-ba4ba69d0d80 | -9.68921 | -62.00203 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b5f0d53-7975-3708-9366-154d9c26e005 | -10.79924 | -45.98766 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 030260c2-09e9-3baa-a414-9ca90a9b159a | -6.96674 | -44.55249 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 35a348e0-57fc-3d2b-b9c1-2f354b4be399 | -11.2766 | -50.85466 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49df40ae-3d61-3294-88d8-1b76b7c8eba3 | -11.08723 | -49.73723 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5be33bc7-27f8-34ec-a1e9-3df26bccd5e4 | -5.84901 | -44.16748 | 2025-09-15 05:10:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c93ab864-30eb-3107-8451-990272b24091 | -8.78955 | -46.04734 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a97d080-f2bd-3041-8ad2-a6887de5b64f | -9.14552 | -62.39731 | 2025-09-15 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf8b2609-b529-3374-a0a9-fc8f31107d40 | -5.85542 | -48.15573 | 2025-09-15 05:10:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a1398bd-c971-3765-9e99-3097dff06325 | -8.50409 | -51.16511 | 2025-09-15 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac6e32eb-7542-3430-9970-ea0a7d8a96bf | -8.61782 | -45.74096 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 047cda14-3b17-30fc-bb9c-0d289c57aaad | -8.91326 | -45.49407 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c564d926-673a-3474-9cdb-b94c24e208f8 | -11.15618 | -57.189 | 2025-09-15 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c706ec64-d87e-35e7-896e-d77ba6457706 | -11.09063 | -49.73707 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9bb30cb-7ea6-312e-9538-6519206af6a1 | -11.88182 | -50.54163 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fffbdd40-170e-3146-89c6-b1479d5fa79d | -7.69401 | -44.67724 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 50fd1c31-6542-3831-b381-8339fc21acd2 | -7.78841 | -66.92514 | 2025-09-15 05:10:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e27c3eb-8ec0-3311-99ce-66ad60f4569b | -11.72325 | -46.48849 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecee400d-4cf5-3bb0-8f5b-04d93ae63b4e | -7.35773 | -44.29747 | 2025-09-15 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 97023aa5-73b1-321b-bee9-df1f2cc4ad33 | -7.68871 | -44.6757 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27101ba5-6dd6-3f9e-8e8d-ae28c684c2b8 | -8.16733 | -46.78447 | 2025-09-15 05:10:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ab7270d-cd6f-3c8c-8fde-a201c1dcc09c | -11.79917 | -50.43133 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| dafaccb4-6964-3fa5-9be5-c0ccbb0294f2 | -12.0523 | -46.5513 | 2025-09-15 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc5d2833-1345-32af-aef9-0b620e1bd539 | -10.92773 | -45.57217 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 135438d5-c78d-3e80-b83c-51aaf82dba50 | -6.30323 | -51.73859 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56be4d73-2713-333b-b122-34c18d923454 | -5.69775 | -49.202 | 2025-09-15 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6580507f-de0a-3be7-a12c-f54746d5380f | -8.5981 | -46.36039 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 445262c4-17a0-3754-b63a-421f567cc4f5 | -4.19401 | -59.98259 | 2025-09-15 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44234475-d238-3466-88bc-f73357903096 | -11.99531 | -46.65413 | 2025-09-15 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19a54c98-9c5b-373e-9cba-f65491b832f5 | -11.99828 | -47.76608 | 2025-09-15 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0dfe013-ce6e-3e08-aefc-5d45c407e05a | -10.13937 | -46.15911 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5304e10a-f9b5-3bcd-81cc-d8ec9681de51 | -7.31285 | -43.93567 | 2025-09-15 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bb7294d-d7f0-3a7f-976f-d6bf7f7a8d50 | -10.39605 | -48.61382 | 2025-09-15 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf1ee423-e51b-3ad4-8ba0-1c1c6ffc3986 | -11.99881 | -47.7616 | 2025-09-15 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d230e9ea-ac37-3ef6-85ad-1ce397c143ff | -8.6473 | -46.36064 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96c1d50d-a557-3340-9cfc-6e1b5e8d1b23 | -9.1468 | -61.15594 | 2025-09-15 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d42b1d9f-34c7-3a22-adfe-e05a75a1d3b2 | -10.88995 | -55.66747 | 2025-09-15 05:10:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd9c7fad-dde8-3722-ab25-43ec0db8102b | -11.78923 | -50.43 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 61666e88-6368-33c9-89b0-99a43bcb1625 | -12.64454 | -47.93521 | 2025-09-15 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 931649a5-7a3d-374e-b274-43b8ea0148f4 | -10.98811 | -55.31668 | 2025-09-15 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f1e66dc-8ae1-320d-8962-39aa62c61064 | -11.27059 | -50.8271 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdeba547-d73a-3570-a210-503ca1fba0bc | -6.55638 | -43.98745 | 2025-09-15 05:10:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aad6ddbd-8117-32c6-a24e-b97d160c35a4 | -11.08589 | -49.73327 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4a0cf42-18d7-31a6-8fe9-22f8f27564cb | -10.66356 | -46.24442 | 2025-09-15 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f43e966b-48f2-33c6-a1ec-04bb020fe238 | -7.63784 | -49.7249 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 613cd4b8-3320-3d97-b84f-4a4ddf47ea41 | -5.0985 | -56.15987 | 2025-09-15 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccd3ba68-b2cf-3288-846b-93762f3f6f25 | -10.78014 | -45.981 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d108756-b48b-310c-8ceb-06748ed5edd4 | -11.74492 | -50.81268 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7e490fd7-c3c3-3534-860d-943ee76a07a8 | -10.17315 | -46.14906 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a7a2edc-970c-3366-81dd-c24d9d94ea39 | -11.85647 | -50.50377 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1a747b09-6a17-39cf-9bf8-64c361cb50e4 | -8.89221 | -46.16937 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fceb0157-caff-3e7e-b565-209abac001e0 | -6.98127 | -44.547 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 562a9668-b982-34eb-8d06-722363adb9fb | -11.12534 | -45.31417 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93548cc4-6454-349f-8eef-c95d44da4e7f | -11.85785 | -50.53268 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b4129ca-3192-3efc-a483-559170901ee3 | -11.08074 | -49.73257 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba4201c9-dc0d-3342-963b-e4bd9f07357d | -8.41518 | -47.2256 | 2025-09-15 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 235d0e74-ecac-3acc-90b2-70915c34cbc8 | -9.88797 | -58.33606 | 2025-09-15 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ddc92ae3-1555-305f-99e4-68ad3e7a867b | -11.87689 | -50.54096 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3a1936b6-f9e0-3545-bdb2-af0e6ed68a10 | -9.73449 | -51.88448 | 2025-09-15 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c0f7a96-37b2-3432-b73b-61a7a6ed1951 | -7.51478 | -44.71169 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fc642dc-a54e-36d7-8c9f-83be97d06544 | -9.44762 | -67.67066 | 2025-09-15 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dd8c723-6324-338b-a79c-634a2c99416b | -8.16792 | -46.78011 | 2025-09-15 05:10:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61401e6c-19de-38e7-925b-cbd995952b76 | -8.76697 | -46.07211 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 811e4f6c-97cd-38d8-a6b8-74b4a65ac0dd | -7.89271 | -63.70808 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 482b8716-2f48-3f21-a69d-1c35f38e368e | -7.97886 | -45.67115 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e16d6989-6569-33b5-a97a-fa2b0b22f15e | -11.7977 | -50.44273 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ca1ad1d-a824-3331-a4f3-da010afa885b | -8.91182 | -45.50551 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b620f5de-f7de-3cef-a1c2-d038eea7a01f | -11.31642 | -51.13907 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fe32084-28f9-3156-9cd8-f2f9aa15c2bc | -3.51636 | -58.94806 | 2025-09-15 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10c0b2c5-7fe0-3699-abc4-1fa1e39327c0 | -9.8866 | -57.87079 | 2025-09-15 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da589692-4c76-37f8-a625-3c10fb3ca3af | -12.00743 | -46.66111 | 2025-09-15 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bc8e101-a6ee-3955-b140-8e54b65c9768 | -8.97024 | -45.83121 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6cef0d4b-2b0f-3e2b-a6b4-152f372ad267 | -9.00765 | -48.02767 | 2025-09-15 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0ff04d9-c8b9-32d9-a62a-9450cfac442f | -11.39814 | -51.36237 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2df0b7e4-567c-3243-a9fe-c28245fc8842 | -11.40142 | -51.36538 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 90ba29a2-c583-3285-b9b8-26ee6afdcab9 | -9.80415 | -59.0975 | 2025-09-15 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc4e1ee4-1f9b-3fd1-a9b3-d06c28e25bb9 | -9.73509 | -51.88027 | 2025-09-15 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e61f5a31-207a-385f-a25f-c51373f40060 | -12.64404 | -47.93954 | 2025-09-15 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49cae351-8eba-3364-8766-89e493dc44fb | -8.97008 | -46.21403 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c76be02-c26a-388d-9cae-bcca79f012be | -11.08548 | -49.73637 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f354aa6d-a481-3939-ba47-d665e19ea8a1 | -10.67004 | -46.2447 | 2025-09-15 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 683d7e6d-63d5-31c9-b0c3-fbf7fac8b139 | -9.89128 | -58.33659 | 2025-09-15 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c33cf742-4be2-395d-ba0f-435626cd7407 | -9.01047 | -47.04256 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab2f07f8-0062-3568-9f19-2fc8d772d326 | -11.85542 | -50.50238 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 09f00232-c784-36a9-be8c-277fae2fa9d3 | -6.40685 | -46.93924 | 2025-09-15 05:10:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README58.md)
