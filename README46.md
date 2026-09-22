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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08738e94-06a4-323d-b0fc-2617c5df6ab5 | -6.30666 | -57.73714 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 65032064-025c-3625-9e67-bb9a0a6e7856 | -6.67444 | -50.94097 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cee91207-27b3-348e-9765-03e6231d30e8 | -6.14239 | -43.85081 | 2026-09-22 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cc1167a4-f315-36f3-b396-c16345ffc2fe | -7.60714 | -55.35781 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3c152e1-413a-378d-92c1-a49e25aa0458 | -6.73747 | -55.08706 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54e2120c-203b-3b81-97a4-8bd417bbad37 | -3.46206 | -59.52754 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 570c336d-d258-3be2-9681-0559971a97ed | -7.40087 | -55.22012 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfad4d77-2914-3c18-898b-972421085189 | -2.97641 | -54.15208 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a4251a3-2cfa-37d9-b8dd-23ab8430891b | -6.1232 | -57.75454 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0967498f-661e-3e5e-92c4-08e342c97dd3 | -5.79293 | -43.86844 | 2026-09-22 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a847525c-e26e-34bf-915b-d572589b0e48 | -8.32596 | -46.00985 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a6205f7f-b738-38b3-b6e8-abcf83735380 | -7.88 | -54.72728 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b8b7c3e-57f1-3c0a-b136-83f7532ab09d | -2.94353 | -51.97104 | 2026-09-22 04:46:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1308346d-6ca9-335f-87e7-3db8231ee1a1 | -4.20564 | -59.9099 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbb9bfcd-8baf-372e-abf3-24c40bf31054 | -8.18788 | -54.72812 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2535f970-2193-328f-b912-d5ef13590d90 | -5.45997 | -60.14897 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4bfc08b-15f4-3f8a-90d7-aa5f8efd86b2 | -8.81769 | -48.76614 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b469c46-3cb7-321b-95ef-fa9f63fdc04e | -9.28839 | -46.169 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3d243cce-34c0-3bd5-be30-a94f81b09a39 | -5.8824 | -53.63516 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 159a98a9-6881-3b08-a45e-9d0dca38fa6d | -8.60243 | -54.63264 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb589833-cc2c-3bb3-a3dd-a7669da3b62a | -9.54445 | -47.94131 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc1785a5-e0d8-3773-bf02-0260a7ea4fc4 | -4.41722 | -55.24569 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e223dd4-b7bd-339e-ab48-0e67bdc02445 | -5.98107 | -57.77457 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 129d9ad5-c2b5-3cc0-a254-34e73ead60e2 | -3.80728 | -55.66312 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8edae923-b63a-3a68-8772-7072f835c351 | -3.44795 | -50.60273 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6226a6b-c489-35c8-a3ee-d4d674719343 | -2.86181 | -57.81337 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54216eda-070d-3d63-b071-5db2ff731585 | -3.39483 | -50.43996 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bfc11c4-4b7c-3c99-a7b2-c0ea00662048 | -7.61163 | -55.35393 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 314b1765-7563-3a72-9bd0-cd2726bb6ca5 | -5.88572 | -52.04363 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f902720-f36a-32fc-ae31-f17fe6d54f3f | -11.09787 | -48.33018 | 2026-09-22 04:46:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8f0ffe1-dda4-3d91-9a07-ea42a2a56a43 | -6.22751 | -56.04319 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db7b6629-8de4-3f02-9bea-696b7ba11a91 | -6.62827 | -59.92916 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e50038d4-a82f-33bf-a2fe-6b22805e1c7a | -7.27368 | -57.58503 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73a12097-599b-3c31-88d6-5116944984e9 | -7.8249 | -45.25888 | 2026-09-22 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11f61cee-babf-30d1-8f03-7adaeb2d79bf | -8.24782 | -55.2521 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afdacd81-1865-30a4-adf0-cc7b04982da4 | -4.2197 | -48.61956 | 2026-09-22 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 689d6124-971e-3016-baa8-dc552197f5a2 | -11.54496 | -45.36849 | 2026-09-22 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 988b6614-c5fc-39ce-9088-2688995e22cc | -6.46613 | -59.9856 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eedc7000-afe6-374a-807a-6eddbd87737a | -4.41985 | -55.50293 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd9f24b9-a040-39b5-99bb-5f5e482719e1 | -6.09531 | -57.62889 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 737bb546-8516-38ff-a996-396448d92c91 | -4.28616 | -48.62222 | 2026-09-22 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d603ea51-769d-33c3-8b2d-00dc9a533d75 | -8.08907 | -44.35381 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac85a95d-50cb-3f7f-b7d7-5ff143fda472 | -3.89457 | -60.59142 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9244e5b8-be95-3cd4-b06b-464cc7102bcd | -4.93999 | -55.81706 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba088c05-71b1-36ad-9355-96d7cad0dd55 | -6.4306 | -55.61428 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3bac104-7589-3d4a-9cec-ec0f7de24e5a | -8.3666 | -48.53471 | 2026-09-22 04:46:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fff7085b-8544-3761-a31b-23a2ef6dbdde | -5.87347 | -51.9486 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff8886b6-04aa-39a0-a062-97b0182b0c8d | -6.67044 | -47.37383 | 2026-09-22 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc8de6cf-2935-3f59-b09e-420fd0949d9a | -4.43146 | -55.08315 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4eccdfae-850f-3770-b686-8c7b34a59b6b | -5.93388 | -59.97591 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 974c0c70-9188-38cf-a65c-deab7b00eedb | -8.23758 | -55.2746 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57a26840-e563-388f-b5cd-36264bea7309 | -5.87184 | -52.06674 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6d995cbc-0739-3cd3-8aa0-f297f558f5ce | -5.98385 | -57.70211 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd9e9b5d-3f2c-3809-8d5b-b78aed2602b8 | -3.92842 | -56.05014 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a53d98f2-076d-33a6-9111-7d38664e4625 | -8.80225 | -44.28032 | 2026-09-22 04:46:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35b13571-4077-3fe8-acb7-f88b8697efd0 | -3.12707 | -51.60638 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec157a85-b79c-3bb0-a56f-5fcecd316941 | -5.85478 | -49.77777 | 2026-09-22 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d589fa0d-9d5f-3823-80eb-f29f7d159c0a | -6.11305 | -44.31647 | 2026-09-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fcb60e1-d0e6-3c22-9f57-c1b764c6a2d4 | -3.16807 | -50.82248 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab4da56a-003d-3306-bd4e-58b2a267321d | -3.50987 | -55.48595 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c00e86a2-636f-32b6-a2f9-5ec96f7548b7 | -6.10517 | -57.67949 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ac7b4a14-7604-3388-8103-1bc9fcd08d1f | -10.74228 | -50.81209 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c238b531-1090-3ce0-b07d-550bdbeb5ae0 | -6.3148 | -57.74299 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27a49ba6-fad2-3ab6-a36e-d50361077851 | -2.85708 | -57.81265 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b285384-2159-3bcc-b656-cedbb4e0d46f | -7.24296 | -55.60694 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 903a7785-fc58-3231-8a00-019c3ac35a21 | -7.31885 | -54.94658 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0360350a-ebfc-3162-b4f1-ea86c642e9ab | -7.02204 | -42.08502 | 2026-09-22 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| e5430df6-ad5f-33fb-a298-155030e9c417 | -5.85411 | -52.02789 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8318c01c-0d27-331f-a032-8d3adad24987 | -10.26691 | -49.98687 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f47a475-e501-3c54-8d2d-0f1a99dda72d | -2.95425 | -57.72033 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a3057e46-7ba3-305f-8793-5085424e0bd0 | -3.46826 | -59.55526 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14454b37-8b96-30e7-93da-9af83f571f15 | -10.47802 | -51.29886 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91c64bd2-b260-3970-b5b4-7e8527f932b7 | -6.46046 | -59.98766 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 973f50e8-92f6-392d-acc5-ee12190ee84b | -3.44848 | -50.5993 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da386792-e725-3562-aee5-0d5885f72fe1 | -8.31773 | -49.68662 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17346184-e612-3ba3-ab6a-c5d60d9dc9b8 | -3.30589 | -57.86331 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13c0c4b6-cddd-33c9-a321-ab86c8850a0d | -7.32999 | -55.60121 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb174832-394a-3169-bb48-e412c7333222 | -4.28354 | -56.26137 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0bda8e2-c19b-314a-af60-fa345f01ab03 | -8.91309 | -50.9314 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc545cac-027d-3704-adfd-768902c41822 | -10.48961 | -51.28986 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 272c4d5e-bc99-3138-890a-9e6158c2df37 | -10.84396 | -50.1571 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f43878e-d5d4-3916-9c57-dd6702b78440 | -3.38261 | -50.40995 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32ce446c-6b62-310c-ac94-da4f10386c95 | -9.88715 | -48.46593 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf2b8f5b-e34e-3a11-a8ba-b9b2990a0958 | -7.39192 | -44.7918 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e58dec31-86a7-3da8-ba7d-80539e31c27d | -6.0845 | -57.69397 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d06071f7-b561-3804-97f4-a8db8e0b45dc | -9.95233 | -53.98783 | 2026-09-22 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7c03a83-63f4-3946-bad3-44f806e6dbf6 | -3.39192 | -59.529 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20b4fbbc-15f1-3588-bb1b-8e5ee3b0cf4b | -8.3035 | -40.59924 | 2026-09-22 04:46:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 87121cbe-85f5-37ac-b59a-4d7e8b019fdd | -5.93276 | -59.98225 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a590459-76ff-3ae8-a69e-e3681201eed0 | -6.14578 | -59.93285 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba39b955-e3ba-3634-b7fc-bb8c266f5724 | -8.13587 | -46.8284 | 2026-09-22 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6610ee20-e70a-31b7-a0a8-1f0d6288cf8a | -6.09973 | -57.67797 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 768165d7-6322-36ad-936d-822a6d5dc5fb | -7.86177 | -54.70301 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ad0d649-66d5-387b-8621-55c8e9967a27 | -10.86227 | -50.8972 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00e2b603-1917-3dc6-a30b-bc0ba745ec6e | -8.62 | -54.6146 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3103e04c-93d9-3b5b-972f-ff42ad2783d2 | -6.86833 | -42.86852 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c6bb7ef-917c-3f70-bf0b-e9bd8c38ee74 | -5.8694 | -53.64921 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e11ca0d8-db03-3f64-b4eb-73fec608b196 | -3.46625 | -59.53489 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68047d5b-77f4-30b9-a4a4-260ff792ef0a | -7.40379 | -55.2255 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc2efafe-d0f6-31d2-a6e9-13715cc04b32 | -4.55933 | -54.94062 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README47.md)
