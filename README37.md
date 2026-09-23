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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58d66aa3-34ce-3586-8a09-1af470a789b2 | -12.8153 | -50.8504 | 2026-09-23 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 81369bc2-6113-349d-bfd1-d54ee85526de | -8.4726 | -48.6927 | 2026-09-23 02:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 51.2 |
| bddb1c5c-8136-3031-a565-79e9c5343e2d | -12.815 | -50.8718 | 2026-09-23 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5679f52b-8b35-3222-8d41-c4cb033da027 | -6.3784 | -42.7933 | 2026-09-23 02:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 6df53551-b2e0-3d52-8402-a824ae14e08b | -11.3043 | -51.3434 | 2026-09-23 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| d072bdfb-4f32-3999-b800-dcbe50b41526 | -8.9351 | -61.4759 | 2026-09-23 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c6b392ac-4fcb-3186-96ff-061b971842ba | -12.3488 | -50.1563 | 2026-09-23 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 496fae27-48ae-3656-9019-2e42f9f49b6b | -12.3867 | -50.1731 | 2026-09-23 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4f116006-3eb1-3789-a336-614db6b68c7d | -12.7958 | -50.8742 | 2026-09-23 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 46f5afd5-f3b8-3f61-979b-7e9008df1a66 | -11.2856 | -51.3243 | 2026-09-23 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 479b3aeb-1496-36ba-80bb-8bea4f292b2c | -8.9164 | -61.4958 | 2026-09-23 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 3c9f1322-d246-3c82-a993-822bcd086c59 | -11.4201 | -44.0262 | 2026-09-23 02:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 1a76bf56-956f-3089-8c68-6c6eaca19170 | -8.9165 | -61.4767 | 2026-09-23 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a43b8090-48c2-355a-90bb-25bf98bbe1d6 | -6.6815 | -55.0703 | 2026-09-23 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 4d180e93-a939-3171-aab8-e8c703966b40 | -12.3484 | -50.1779 | 2026-09-23 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| dc7809d6-1413-319c-bd16-0a52ee1771db | -11.2853 | -51.3454 | 2026-09-23 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| f1b486d8-3b01-3dbe-80b0-d2d1e6bd20b8 | -5.7754 | -45.1053 | 2026-09-23 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| fd60e827-15b6-383d-addd-ee2bbeb268b0 | -3.6947 | -60.5645 | 2026-09-23 02:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6e36731a-57e4-3909-a8f2-fbd1f55a2bb8 | -11.3037 | -51.3858 | 2026-09-23 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 474dca92-a81f-3cdf-8853-eea3bfdac97f | -11.304 | -51.3646 | 2026-09-23 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| e056f0f1-29c5-3414-bdf9-4b785100004a | -5.7567 | -45.1067 | 2026-09-23 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e2747a74-d0f4-38a2-a0ab-3fb07645517e | -9.1024 | -61.4491 | 2026-09-23 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| d73c112c-5dcc-3e55-aad5-6f2dd5bdf448 | -9.1025 | -61.4299 | 2026-09-23 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b657de58-7fc3-3365-9739-44de52bd7e75 | -8.935 | -61.495 | 2026-09-23 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c88bd380-1220-38bc-bd63-e84edafbe260 | -8.8105 | -44.2757 | 2026-09-23 02:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| f746031c-fe57-31bc-93c7-13d7b828a57a | -11.4009 | -44.029 | 2026-09-23 02:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 6b2d3ca6-cab3-3691-84b3-e5106004d064 | -11.4005 | -44.0525 | 2026-09-23 02:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| e7e0e134-c7f0-36bd-b876-dc7e61174169 | -3.6763 | -60.5839 | 2026-09-23 02:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 0209efcf-82fd-3db6-a47c-84af8da725e4 | -11.711 | -50.7677 | 2026-09-23 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| a681a2cf-fa1e-3e5f-b143-3a0bb113d294 | -6.6146 | -59.9272 | 2026-09-23 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 213.4 |
| a26d84df-350d-3765-ad5e-d16c82c28a1b | -5.8166 | -49.1504 | 2026-09-23 02:40:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1657defe-66e5-3968-8347-fe99b06e43f0 | -8.2616 | -54.7776 | 2026-09-23 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e10c801d-b16b-3370-8c81-e367620d085c | -10.0463 | -36.2664 | 2026-09-23 02:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 73.7 |
| 833a8d84-f3c3-348b-852b-8813b8f9619e | -3.6764 | -60.5649 | 2026-09-23 02:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3562a94d-3a34-3639-b5b1-bda479ad0388 | -6.6145 | -59.9464 | 2026-09-23 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| be203d50-5302-395d-8905-d2ebfb7e68a0 | -6.6148 | -59.908 | 2026-09-23 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| dd87bfcc-d800-385d-8de3-5902c2336c0a | -12.7767 | -50.8766 | 2026-09-23 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| fd1d27d0-ab2b-36e8-ab4a-73151efae298 | -14.7536 | -47.1548 | 2026-09-23 02:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 6c3784c4-bb64-3c0c-bbb1-6735822b70fd | -12.3676 | -50.1755 | 2026-09-23 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 3964ccdd-e977-3229-9e06-f84c47e6d4b8 | -3.6946 | -60.5835 | 2026-09-23 02:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 1a8a88d1-128a-3cd8-a11c-19947a98c58b | -5.6246 | -45.2518 | 2026-09-23 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 78e8ef64-4d03-3457-8ea8-adbc9d8533f8 | -12.387 | -50.1515 | 2026-09-23 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 6179dcff-e041-36e8-bd61-a126a3154aee | -3.2314 | -46.9376 | 2026-09-23 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 24d6e958-eaa7-3296-aca2-ae0dc6f6b71d | -11.7107 | -50.7891 | 2026-09-23 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| b5102782-144d-3f62-8835-7caff6e3abce | -11.3046 | -51.3222 | 2026-09-23 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 4315a053-4ab1-3627-9bb2-3fcf3f8b2a98 | -1.9271 | -58.2587 | 2026-09-23 02:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3c6346ca-a31a-3551-b187-ffb5ec5b896e | -12.4212 | -46.9777 | 2026-09-23 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4f4eadf0-7d7d-3e4d-8dc6-6541c4c27b81 | -7.4313 | -49.8303 | 2026-09-23 02:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a6e147d0-622d-3a8c-a22a-07e8314ad758 | -3.8648 | -58.8211 | 2026-09-23 02:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e0d10253-b6f2-30b2-b9c8-846b23e3e7e4 | -12.3679 | -50.1539 | 2026-09-23 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 281.6 |
| 180e829a-24ed-3a6b-bad7-fe45600bec81 | -11.8871 | -45.7623 | 2026-09-23 02:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c18e3205-7c0b-3271-990e-389f578e8c1d | -6.6331 | -59.9265 | 2026-09-23 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 129.6 |
| e884a04f-bcd3-398e-a47d-67120d3c35de | -8.4538 | -48.6944 | 2026-09-23 02:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 3d88c4da-46c1-3fdb-b9b8-56a16517a47c | -3.2313 | -46.9596 | 2026-09-23 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1cca3ba4-c524-3f55-a9c8-56778fdcec43 | -4.3357 | -55.6659 | 2026-09-23 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| a61e8392-e670-3608-895f-821784121b95 | -6.61 | -43.79 | 2026-09-23 02:45:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e383fe85-c112-3c27-ad21-bd08cbdc1073 | -6.64 | -43.75 | 2026-09-23 02:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1774d3c3-ac23-3f1b-a739-7741e8769783 | -6.58 | -43.74 | 2026-09-23 02:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08b571ee-1a1c-392c-9e24-f62f7a727094 | -6.61 | -43.74 | 2026-09-23 02:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb61c573-8b29-3ffd-8df9-5711e5b4d022 | -6.58 | -43.78 | 2026-09-23 02:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 475dc6f1-0bc3-33be-8a91-06a3478f47f9 | -6.58 | -43.69 | 2026-09-23 02:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14d1bfde-23d2-332d-bcc4-55f996ab1053 | -6.61 | -43.7 | 2026-09-23 02:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53b153eb-292e-369e-a7e7-abae45a3e538 | -12.35 | -50.14 | 2026-09-23 02:45:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf220541-25bb-3f8e-a32e-a9ab72700579 | -6.6148 | -59.908 | 2026-09-23 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 62e00ece-4319-3fb5-9812-ea03020213ed | -8.2616 | -54.7776 | 2026-09-23 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 22cc4585-bd67-3582-b25d-50fef306558c | -11.2853 | -51.3454 | 2026-09-23 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 96f77b50-f642-3afd-8394-509b8897cec4 | -3.6946 | -60.5835 | 2026-09-23 02:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 731ff050-bd41-3d6b-96f5-68f92fcda5d3 | -12.8143 | -50.9147 | 2026-09-23 02:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 3b367c12-040f-331b-b0bf-4e563d19e615 | -8.4538 | -48.6944 | 2026-09-23 02:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7c3d7c98-7471-3953-9643-8f2b64260887 | -14.7475 | -45.6191 | 2026-09-23 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 55984edf-515f-3812-a9fd-1d72b4a0bcd0 | -6.6815 | -55.0703 | 2026-09-23 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| e56a2214-4587-3301-9efb-3a6261eaafcd | -11.2856 | -51.3243 | 2026-09-23 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 6f2429e2-79f1-3933-8a87-2186cc112976 | -14.7284 | -45.5993 | 2026-09-23 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| ee738977-d6c8-3016-ae3b-e6c5c3edd4f6 | -14.748 | -45.5958 | 2026-09-23 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| af40c72a-ec0c-39c5-9d86-9eb00f739c57 | -11.6514 | -50.9449 | 2026-09-23 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f898de78-23e8-3a0b-80e5-b5bdad020086 | -5.7567 | -45.1067 | 2026-09-23 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b290fa11-6b86-3097-a04a-e2a85f41130a | -7.8811 | -61.1779 | 2026-09-23 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| bbc4b50e-a1ad-39c8-8f77-04ffbd0e64c2 | -3.6763 | -60.5839 | 2026-09-23 02:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| df7501bb-205d-33bc-aa0f-02b566e4e969 | -14.7089 | -45.6029 | 2026-09-23 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 42982447-96d1-32c7-955e-3210a1a85454 | -6.1109 | -57.684 | 2026-09-23 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| fcf7e2bc-debb-3e06-8003-8a5915256dc6 | -9.1025 | -61.4299 | 2026-09-23 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 1e8c471a-7de2-3dfd-a419-ff7f205967cb | -11.3229 | -51.3626 | 2026-09-23 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 3b03e179-358b-3d45-b0c9-e6126d49f9c2 | -8.9165 | -61.4767 | 2026-09-23 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| dcef098f-9fbd-38b6-a47d-d983c238dd83 | -11.6321 | -50.9683 | 2026-09-23 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 13ac755b-7f1d-3993-b90d-d4f529adc3cf | -3.2313 | -46.9596 | 2026-09-23 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 5f826fe6-8c90-3813-a5c1-22a5b1b5b695 | -11.6511 | -50.9662 | 2026-09-23 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e97712c0-d7b6-3672-9fad-33c18a71e996 | -10.332 | -50.5109 | 2026-09-23 02:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 62d54f08-45dc-3718-8f77-da5eea6cf836 | -3.2129 | -46.9383 | 2026-09-23 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 72d527b2-241b-3f4b-920c-8f02083bb8e5 | -14.7094 | -45.5796 | 2026-09-23 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| dd810a34-24d5-301d-97e8-dc761bced6b4 | -3.2314 | -46.9376 | 2026-09-23 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| ffc99bcd-b05a-333e-be5e-525a5f8ce004 | -14.7731 | -47.1515 | 2026-09-23 02:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 3040c5dc-4966-3173-a535-a089034bd374 | -5.7754 | -45.1053 | 2026-09-23 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5387863d-f9cc-3e3e-be41-4a3d943df24d | -12.738 | -50.9027 | 2026-09-23 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5f08d042-ce13-36cf-a865-162fbdf8f31a | -11.711 | -50.7677 | 2026-09-23 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 8f2d9217-2655-3bc3-b719-a04cb4c9dab3 | -8.4726 | -48.6927 | 2026-09-23 02:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0f37fbf7-a64e-3968-8bb3-fcc45a1a0f45 | -11.3043 | -51.3434 | 2026-09-23 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| dd99c9d5-a0ea-31af-ae6a-2968f183ddb1 | -12.3679 | -50.1539 | 2026-09-23 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 321.7 |
| e5304e32-12d2-3506-8363-a9857e168db3 | -6.6331 | -59.9265 | 2026-09-23 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 4d4b6c7d-b9d2-35b3-9542-31a476e249ef | -8.9164 | -61.4958 | 2026-09-23 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 4a03aa8a-c12d-3abe-8880-2955fb58ea9f | -6.5939 | -43.7565 | 2026-09-23 02:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |


[Clique aqui para ver as próximas entradas](README38.md)
