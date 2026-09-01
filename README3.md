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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 823017a7-84de-3f35-a8ce-98ca1c783307 | -6.756 | -44.572601 | 2026-09-01 00:15:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e15a93f-04b1-3341-b2cf-432b4774acc3 | -11.6651 | -47.611 | 2026-09-01 00:15:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2e8475c-5fba-30b4-a9c3-168883a9badd | -10.5387 | -46.164799 | 2026-09-01 00:15:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8097699-2c8f-37ea-9688-de68cfe1322d | -10.1978 | -50.387199 | 2026-09-01 00:15:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5447aa4e-caa6-359d-8510-b4c6e95a8963 | -4.7664 | -41.792999 | 2026-09-01 00:15:00 | METOP-C | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8a7d73b6-20ac-3caf-a6a6-d75e8518d840 | -6.3502 | -44.0928 | 2026-09-01 00:15:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13c79ac9-56b5-33b0-89fe-f62b35d7a2ae | -11.2527 | -50.616001 | 2026-09-01 00:15:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0434bb89-22f9-3d7e-8d77-04d2f5a6eccb | -11.9414 | -45.0583 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8aa72f8a-aaaa-37b9-99a5-7595f4f83105 | -14.9831 | -48.133999 | 2026-09-01 00:15:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fd8d22a8-fb85-35fc-81d1-604a38fdf7e8 | -5.5877 | -42.317299 | 2026-09-01 00:15:00 | METOP-C | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 149e0def-11dd-39b7-a387-5ee401098dd8 | -11.2446 | -50.5746 | 2026-09-01 00:15:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cbef062-5bf0-3d60-b927-873b175a639c | -9.4109 | -45.676399 | 2026-09-01 00:15:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f6020fd8-da51-3368-bac9-6a6c0c87e9f1 | -18.4855 | -50.923302 | 2026-09-01 00:15:00 | METOP-C | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 17ab7317-daac-3c87-98fd-3c10a4864a9f | -7.2685 | -46.8069 | 2026-09-01 00:15:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f67d719-fab9-3cf8-aee3-53d09020fb5a | -5.8802 | -52.253502 | 2026-09-01 00:15:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6815d38-a3a4-3802-89cd-5446b4b2e8d4 | -11.4911 | -45.106701 | 2026-09-01 00:15:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5e0e670-c461-3216-8e97-851e29df27ee | -10.1435 | -50.318298 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b5263ea-2626-3a08-aa04-d8fcf86991f2 | -18.500299 | -50.891998 | 2026-09-01 00:15:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 48c073ac-de57-3b38-acce-a2ed1e669c01 | -10.0268 | -44.683701 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| afba530f-f619-3641-8e7b-17513824a0d5 | -1.0308 | -47.5616 | 2026-09-01 00:15:00 | METOP-C | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd28a5b2-abf8-34d6-bda5-15b0345069ea | -10.7393 | -48.0084 | 2026-09-01 00:15:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6307f944-4711-30bd-bac5-7d92a9f442af | -10.0108 | -44.704601 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ceae90a-d649-3e57-888c-c1ffc5c7704b | -4.935 | -47.661098 | 2026-09-01 00:15:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a90bd4d2-6277-37e2-9b4d-22252ac7cc51 | -6.2134 | -42.529301 | 2026-09-01 00:15:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4dbeb595-3f74-393d-a330-a206f9e8d04d | -7.2707 | -46.816898 | 2026-09-01 00:15:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c191a9ae-8492-3c8f-9ebe-a4840727cc83 | -10.1765 | -50.331501 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee214e22-04bb-3213-a6a0-8cd5f50c207a | -3.9718 | -41.522202 | 2026-09-01 00:15:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b806bdb-494d-353e-8fb3-039b372607e3 | -7.2748 | -49.834202 | 2026-09-01 00:15:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51ba9d9a-2951-389e-ba69-6643229b9b88 | -3.1812 | -48.0299 | 2026-09-01 00:15:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8606afdd-93c8-3ccb-a46b-838c5bcc8f0f | -12.0904 | -44.987999 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 321f545e-514c-35ac-a4e8-3d2e7107589a | -8.8653 | -38.647999 | 2026-09-01 00:15:00 | METOP-C | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| b374bf9f-887a-3433-88d0-90e531ed1f9a | -9.4128 | -45.6856 | 2026-09-01 00:15:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b05929d5-6166-315b-8f1f-781d696b4657 | -18.265301 | -40.560001 | 2026-09-01 00:15:00 | METOP-C | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3409f744-750f-3059-9981-1f91519a1bc6 | -8.4931 | -44.759201 | 2026-09-01 00:15:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e170bade-4ca0-38e3-98d8-41d374e164f8 | -4.3576 | -47.785599 | 2026-09-01 00:15:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d548137-083d-3337-8e75-5bda6ce822ac | -10.0362 | -48.693901 | 2026-09-01 00:15:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed720976-14bb-352d-8ab0-23eca9427f71 | -11.4892 | -45.097599 | 2026-09-01 00:15:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba2ae15-feb0-35a6-845a-08c4116b9799 | -15.7806 | -51.0644 | 2026-09-01 00:15:00 | METOP-C | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ac61f13-aa9d-38fc-83a5-97db34a75bf4 | -10.1396 | -50.299301 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 193e69e5-e3f0-39de-ab22-7d043211f0b0 | -5.3434 | -45.1562 | 2026-09-01 00:15:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e00b5ff0-4afd-31b4-bda8-f5c54333a42f | -4.8166 | -43.186199 | 2026-09-01 00:15:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 865767d1-d7db-33ba-8099-ddfa6e435430 | -11.2389 | -50.597198 | 2026-09-01 00:15:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83c468ca-fcec-3c60-85ed-ca621cac3b54 | -5.5892 | -42.3241 | 2026-09-01 00:15:00 | METOP-C | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d49d1cda-9b19-3f0d-b354-33367408566a | -11.2071 | -45.119801 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e1d1d66-0328-3c22-8525-4c261d8efb4b | -4.3651 | -47.773102 | 2026-09-01 00:15:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4128e185-429b-3003-89ef-ca7c501e11a8 | -10.0072 | -44.687901 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f55a95d1-9756-328e-904e-ae9ac03688b3 | -4.5025 | -46.4077 | 2026-09-01 00:15:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 80815340-8577-3455-a33f-08c2d1d905ce | -12.1513 | -44.214699 | 2026-09-01 00:15:00 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94031e80-f72a-320e-9788-cc2e7c42aba6 | -8.843 | -36.526001 | 2026-09-01 00:15:00 | METOP-C | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af72ac35-95b6-34e8-a8ad-5347deb3cdef | -10.1299 | -50.301201 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a2a7578-fe71-3292-877f-1fed8c9ecab7 | -2.7163 | -47.057899 | 2026-09-01 00:15:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad0a2c3d-11c2-387c-aaa0-9f461cb9ff7f | -7.8996 | -44.258202 | 2026-09-01 00:15:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2da30f96-d9fe-390c-a324-f431448d12ec | -10.0304 | -44.700401 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a873f08-b72a-3263-a5b5-06530e167951 | -10.017 | -44.685799 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c35dbe67-f8e6-392a-aa6b-9dc6edf8ffbf | -10.0264 | -48.6959 | 2026-09-01 00:15:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6cb660b-3a48-37b4-be87-3354e758b2a1 | -4.4988 | -42.560902 | 2026-09-01 00:15:00 | METOP-C | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3fd13c8e-106d-36c7-81a5-865e70252664 | -7.8962 | -44.243 | 2026-09-01 00:15:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8573d449-7837-3d4d-95cd-3a69a8f879b6 | -10.0206 | -44.702499 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f506b896-265b-3409-88cc-178b22b63fa1 | -11.9434 | -45.067501 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77c98d74-d89a-3470-b3df-45c4c2f83a2e | -10.4616 | -46.574799 | 2026-09-01 00:15:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30db86d9-d6e9-37e4-a2d9-0a40258f7098 | -3.9702 | -41.515099 | 2026-09-01 00:15:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6d7a5a1d-1998-3010-a067-ab4e81c10f42 | -17.3883 | -42.371601 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 739cecc5-5a29-326d-bf93-95f6e7e40301 | -17.376801 | -42.365799 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5b58bbde-0f98-33e7-b107-312f8dc098a3 | -17.372 | -42.392101 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| da5d572d-ed48-37cc-b45f-ae5ba3bcc292 | -15.7852 | -51.090599 | 2026-09-01 00:15:00 | METOP-C | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1c32a2d-0ac6-3962-821e-405669060392 | -16.131399 | -52.412701 | 2026-09-01 00:15:00 | METOP-C | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f658a56-a3e3-34be-9257-aa373bb9069d | -16.304501 | -42.048 | 2026-09-01 00:15:00 | METOP-C | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 51aac86d-c52b-302e-bdcd-af413c04be04 | -17.3141 | -42.703899 | 2026-09-01 00:15:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e51d6625-4b7d-322b-a29f-4820a1352bf2 | -11.2084 | -46.1418 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3df833b8-06f7-3e1d-bb20-f34aa5cd9fc0 | -13.3487 | -43.6768 | 2026-09-01 00:15:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1221304f-ec8f-368d-8aee-ecb7e4a94fd1 | -10.824 | -42.371101 | 2026-09-01 00:15:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 922f1ab6-9518-3a24-8e6b-2997c21e88f4 | -11.0975 | -51.523701 | 2026-09-01 00:15:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c95d783-8ca5-32d4-a90d-6f30e970b879 | -10.5485 | -46.162701 | 2026-09-01 00:15:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dcca1a85-7a55-3010-84bd-4877f3d6a3d9 | -6.4266 | -41.7463 | 2026-09-01 00:15:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b69f3d9-8646-3545-97d2-1790012b61a3 | -4.768 | -41.7999 | 2026-09-01 00:15:00 | METOP-C | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b4f65790-6f5a-3ecc-a349-8e5b26e1ccc6 | -18.4998 | -50.9496 | 2026-09-01 00:15:00 | METOP-C | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8f8c9737-c2e9-3e79-b96b-e6f1a8b71aa2 | -16.3013 | -42.0327 | 2026-09-01 00:15:00 | METOP-C | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 599ffb88-54df-3406-b883-402584100ef2 | -18.490601 | -50.8936 | 2026-09-01 00:15:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f4e158b8-98d9-32c1-9152-15d055c86834 | -7.2109 | -42.746601 | 2026-09-01 00:15:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c3436ed0-fd28-3391-9f80-4d4054ea52ba | -4.3674 | -47.783501 | 2026-09-01 00:15:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1566fda-4267-3b46-b921-3218be1124f2 | -6.2103 | -42.515598 | 2026-09-01 00:15:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 53ce0ce7-e8cc-346a-bbe8-2331c54a9f74 | -21.522301 | -48.646198 | 2026-09-01 00:15:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ae96c5c9-71d4-3a1c-8d31-b5c476d69a44 | -7.5501 | -46.123798 | 2026-09-01 00:15:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c844224-7a82-3406-ba35-668a864b4a14 | -11.2349 | -50.5765 | 2026-09-01 00:15:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 354a0828-0586-3d7d-a5a2-f931b7d4ec90 | -6.4083 | -52.215 | 2026-09-01 00:15:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f060c38-99ae-36c1-a8c5-69a6bd334534 | -7.5154 | -47.3325 | 2026-09-01 00:15:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2d3ea41-93b9-3ac3-a5ad-21853a0e0f86 | -7.5403 | -46.1259 | 2026-09-01 00:15:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 242c723b-0618-3e4b-a24d-bb7c463c7747 | -1.796 | -47.716301 | 2026-09-01 00:15:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7681c32a-7296-3b48-901a-01ddcd62ff1f | -10.6768 | -46.286301 | 2026-09-01 00:15:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1c8d4d1-66bd-3eb2-87ae-38f9dc1ee3f8 | -10.009 | -44.696201 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 757c3b72-c00d-3c46-acd3-83e1e3fe18dd | -10.0332 | -48.679298 | 2026-09-01 00:15:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0458c883-9016-3321-9c20-69f43fcd046b | -10.8198 | -50.722301 | 2026-09-01 00:15:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 400a3276-ac14-3612-9ad8-f45836199627 | -4.2904 | -49.1008 | 2026-09-01 00:15:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51937b5f-365d-381d-8a23-de8d193e599a | -4.3553 | -47.7752 | 2026-09-01 00:15:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b23f8c4e-5d84-3bb4-85af-51700be1ef35 | -12.1495 | -44.206299 | 2026-09-01 00:15:00 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87dbe9fd-4cef-39f7-a3e7-095d301f515a | -11.2095 | -46.098301 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff747322-15b4-31cb-9e0f-2c2cc79b4909 | -17.3818 | -42.3899 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8de67abe-2997-33bb-9236-dffc7c8252dc | -15.8387 | -47.689201 | 2026-09-01 00:15:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 95b36d66-4394-3b6d-91ff-76a171841e6e | -7.5178 | -47.343399 | 2026-09-01 00:15:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57157c0d-f64f-3f64-abef-43add301affc | -12.9764 | -46.003399 | 2026-09-01 00:15:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
