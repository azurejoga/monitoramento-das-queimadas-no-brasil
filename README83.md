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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50b7976c-ee68-313e-9e24-019713df9143 | -12.5795 | -45.6591 | 2025-09-14 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 6c811068-9080-3815-8490-11e84d8edc21 | -10.5262 | -51.5495 | 2025-09-14 13:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| be3498a2-faaa-382b-9267-49d3edee259f | -8.979 | -45.7892 | 2025-09-14 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 63aa80e3-e7f7-3346-811c-8987365d2640 | -12.7671 | -48.0236 | 2025-09-14 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 81bcc53e-977f-3e5e-b53d-ab7201afeba8 | -11.483 | -50.772 | 2025-09-14 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 55825d77-b9a3-38ca-ad3d-55d5a9fa15c3 | -11.4827 | -50.7934 | 2025-09-14 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 3d492d2f-957c-3f32-a347-5667ff115268 | -11.353 | -43.495 | 2025-09-14 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 485cbfb3-8953-380b-8c1d-eb33e48e9eb1 | -8.6436 | -44.0396 | 2025-09-14 13:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 0f326526-c1ef-3680-9fa4-d04c7f49d045 | -11.5017 | -50.7912 | 2025-09-14 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 78d5372f-de53-393b-9df6-7ea24d6c7ee4 | -13.9278 | -44.8576 | 2025-09-14 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 1d413b30-9a6f-3789-8ff4-937a9257133f | -11.8294 | -50.4763 | 2025-09-14 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ec4723cc-47bd-36e5-9770-d895857aa35c | -18.9851 | -48.5844 | 2025-09-14 13:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a92603ac-fa64-31b8-a6e6-d1a6bee07f40 | -11.2927 | -50.8143 | 2025-09-14 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 01e2bd8b-499b-3d53-b5a6-af3ce53c5c71 | -18.9845 | -48.6073 | 2025-09-14 13:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 27160803-f0b5-3957-acec-1e8593356a91 | -10.5451 | -51.5476 | 2025-09-14 13:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| dc9e5c3d-29b3-3fa2-a20c-d1c93c34e9be | -10.8991 | -45.4656 | 2025-09-14 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 9e8d546b-f48f-30ba-8866-b212cb00a878 | -11.464 | -50.7741 | 2025-09-14 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| bb2fba1b-ded4-3ec6-a446-9dce82b93a6b | -8.9976 | -45.8098 | 2025-09-14 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 218.5 |
| b242ac67-0e45-3a54-b35e-dc5065bab389 | -11.8103 | -50.4785 | 2025-09-14 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 31da6ac9-9616-303f-b46c-45351265897a | -8.9979 | -45.7871 | 2025-09-14 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 049e5649-bde7-3fa6-bfcb-fdb64df8a086 | -10.9262 | -47.3561 | 2025-09-14 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| de292a80-c80e-3bcf-9444-08ee0e282daf | -8.1386 | -43.653 | 2025-09-14 13:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c95ca506-2e61-33ca-b9c0-c923ff7f6f8e | -10.5459 | -51.4844 | 2025-09-14 13:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 77317209-9910-32ee-8132-bed5100cefd2 | -12.9294 | -54.7333 | 2025-09-14 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 3eb87537-70cf-3975-8466-47e74a41897e | -9.0166 | -45.8077 | 2025-09-14 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 85f0c913-f3ad-3046-b5be-df991a12a865 | -8.4334 | -47.2306 | 2025-09-14 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 107af75a-1e33-3c61-8672-60f7e1d993f5 | -12.9292 | -54.7538 | 2025-09-14 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 002791c2-1522-3632-ac95-0cf019aea819 | -14.1492 | -45.4009 | 2025-09-14 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 9f47b3b9-7d4a-3f5c-90ab-a1ded7bd5338 | -10.9452 | -47.3538 | 2025-09-14 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 84b8cdd7-4257-3cde-b8d1-fe662543f26a | -14.3747 | -52.927 | 2025-09-14 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| c1a51329-3a30-384a-9cc9-b3d19866f4ac | -13.9473 | -44.8541 | 2025-09-14 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 184.7 |
| b38ba2a4-efde-3f56-aa38-6f4e08f2d602 | -8.9079 | -45.457 | 2025-09-14 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 533ed0bf-50c1-3502-b322-8bbb42ae88b8 | -15.7516 | -49.7821 | 2025-09-14 13:00:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 21c07c22-b3e2-31b9-a708-95090138c93b | -12.5603 | -45.662 | 2025-09-14 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 5f3090a4-d8a4-3a90-839b-59b7e4554907 | -8.8109 | -47.1272 | 2025-09-14 13:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 99418a8c-ec73-3181-b69f-9046567999a6 | -8.9176 | -46.1565 | 2025-09-14 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 3a2a5b1e-5534-344f-ad5a-8cd1a1c9bed5 | -13.9478 | -44.8306 | 2025-09-14 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| dfbd17e4-0f7e-3a55-ba70-9d3add29e9f1 | -8.4334 | -47.2306 | 2025-09-14 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d9ec85b9-e807-325f-bfcb-66dd83162fe1 | -11.502 | -50.7699 | 2025-09-14 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 133.2 |
| c63a8883-54ac-3969-bcb4-b9b2fed0dcef | -12.9292 | -54.7538 | 2025-09-14 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 65b14a1f-7ba5-3264-a5aa-ad11c28d29c2 | -8.7683 | -46.0373 | 2025-09-14 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 01e0a525-f12b-3cd3-9a5c-3e198bea2894 | -14.3944 | -52.9034 | 2025-09-14 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| b8611736-d052-3d6d-9469-8f69f94f22b4 | -12.9103 | -54.7352 | 2025-09-14 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| cb483639-23d6-3646-b06b-5acc3f05c9ab | -8.9359 | -46.1995 | 2025-09-14 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| cef9ac6b-9554-35ac-909f-577278259a50 | -12.7671 | -48.0236 | 2025-09-14 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| fae7f1e6-6d1c-3c82-96c0-992063134323 | -12.8019 | -47.1474 | 2025-09-14 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| ff0266a2-d2da-3c24-82b2-9364caa0aa90 | -8.9079 | -45.457 | 2025-09-14 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 240.2 |
| 7a8b730a-e94d-3a7c-bac4-d004b5d58468 | -14.3744 | -52.9481 | 2025-09-14 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| ea22d522-9880-3a15-8ae4-b5588f7868e5 | -14.2912 | -45.1198 | 2025-09-14 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 9a6ed408-67a7-3840-bfd0-387bd6d61dbf | -11.5017 | -50.7912 | 2025-09-14 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 394c55c9-5bb6-3e91-8676-6e94aaee9ca5 | -14.4137 | -52.901 | 2025-09-14 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9ed2e24a-5556-3469-83ab-a51a7d44dcf9 | -8.979 | -45.7892 | 2025-09-14 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 7101f150-364c-3900-852f-35734cd76de6 | -10.8991 | -45.4656 | 2025-09-14 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 09af7f94-094a-3436-8cb3-d441134abb9f | -13.9473 | -44.8541 | 2025-09-14 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 297.1 |
| 25e6d0db-f6ef-32a0-803f-ca89c4c086c7 | -7.2069 | -44.3946 | 2025-09-14 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 1f239e4e-254a-33e8-852b-80c92824e6a0 | -12.7014 | -54.6949 | 2025-09-14 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 863a0e70-e282-3ae6-9183-f85347083b1d | -8.9548 | -46.1975 | 2025-09-14 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 55d77caf-f2fe-3bbc-b2cc-50d61b98d16d | -12.6633 | -54.6988 | 2025-09-14 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 7b0de933-7fb0-3fc9-8772-8fdfcc489f77 | -8.9976 | -45.8098 | 2025-09-14 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 221.9 |
| f05b1cde-641f-3b32-b6f9-041b94d171f8 | -12.6824 | -54.6968 | 2025-09-14 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 18ea84d7-5499-3421-a223-2b64f015ba0c | -15.7786 | -53.482 | 2025-09-14 13:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 7262211d-d502-3be6-9fd6-2be470ad3c26 | -8.1383 | -43.6764 | 2025-09-14 13:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 3cefa836-dbc5-330a-819c-ccae06a586b5 | -14.2917 | -45.0964 | 2025-09-14 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 68495407-20aa-322e-b8ec-d8de6abe4c5d | -12.6636 | -54.6782 | 2025-09-14 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 10eb2087-8d62-33f4-ad05-e22a7d857117 | -8.9179 | -46.134 | 2025-09-14 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 8bd1e075-5f56-3c61-bf56-c50236c13877 | -13.9278 | -44.8576 | 2025-09-14 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 0e096045-d95a-3404-a893-8439c6210711 | -8.8893 | -45.4363 | 2025-09-14 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4e98ff46-850d-34ef-b628-5aace0e291b1 | -11.4827 | -50.7934 | 2025-09-14 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| b6f95f9c-73c0-3d58-85db-3cf4cba10d42 | -12.8208 | -47.1671 | 2025-09-14 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 252.9 |
| ee467c7f-c345-3039-935c-210abfde7a01 | -14.394 | -52.9245 | 2025-09-14 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 6086371c-b547-39c1-9560-883b173f5cd2 | -8.9793 | -45.7665 | 2025-09-14 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8695fed5-6b93-3000-9aad-fd12d3b82888 | -14.31 | -46.066 | 2025-09-14 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 82dddf60-5c3d-30a5-a608-d019fb1adf30 | -11.2927 | -50.8143 | 2025-09-14 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 02b6a261-64c0-376b-9bab-a17053fed06f | -8.9551 | -46.175 | 2025-09-14 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c6bb6f1d-7cf6-326f-a85d-d5cd5227153a | -12.9485 | -54.7313 | 2025-09-14 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 30d2a340-8cc5-33e7-9ca1-75cb0a1b40d6 | -11.483 | -50.772 | 2025-09-14 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.5 |
| e79d8a3b-65fb-3342-b0b0-af380c02b89d | -8.9362 | -46.177 | 2025-09-14 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| ec572b4e-419e-370d-b1d6-e6d54e0346ea | -12.6826 | -54.6763 | 2025-09-14 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 130.8 |
| b8180439-c2d2-3b27-825b-e836e11eebd5 | -10.9452 | -47.3538 | 2025-09-14 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| b7dbdddb-95a4-3e02-b4ae-2d7a39fd8bc5 | -12.9294 | -54.7333 | 2025-09-14 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 210.1 |
| 19bd21c3-4291-3c28-956d-904f04a98c28 | -12.7017 | -54.6744 | 2025-09-14 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 838199df-6260-3c88-88aa-d9bedae44e77 | -12.8212 | -47.1445 | 2025-09-14 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 391.1 |
| b8981e78-4f77-3da2-a2a4-2ce7b62de961 | -14.1917 | -46.1552 | 2025-09-14 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 92d9387c-83ca-33cf-abac-6c847fd0794d | -10.9096 | -47.2023 | 2025-09-14 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| dd329eda-a88a-3917-b3cb-41ff6410d70c | -8.6436 | -44.0396 | 2025-09-14 13:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 4bb653f7-90f0-3ab9-9537-b094fd3c69ad | -8.1386 | -43.653 | 2025-09-14 13:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 6e1b6439-debb-3ef5-a2fb-9e145ec93827 | -12.7675 | -48.0013 | 2025-09-14 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e3d23333-d3b5-3bb0-a2c6-614c41e98cb2 | -8.9979 | -45.7871 | 2025-09-14 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 6be3e984-651e-36a1-b8a0-60bd5202f8d8 | -8.9368 | -46.132 | 2025-09-14 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 942f12ab-f304-3169-a5ae-8e7c603d0be0 | -14.3747 | -52.927 | 2025-09-14 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 8f672a91-2a0d-3ecc-90da-8782b703283e | -8.9173 | -46.179 | 2025-09-14 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 1302eb39-e937-3d8e-8381-8d9b738176f0 | -15.1995 | -50.1101 | 2025-09-14 13:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| b14934de-e31f-31db-bf68-a2ea9f3da14b | -8.9976 | -45.8098 | 2025-09-14 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| b3afe2b7-714f-3eb0-83bb-a34d3f31f3bd | -8.9979 | -45.7871 | 2025-09-14 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 54de0155-1cf6-3702-a916-2a2f2c5533bf | -12.7675 | -48.0013 | 2025-09-14 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 91b51b14-a99e-31a9-b82a-e5ff125640a5 | -11.502 | -50.7699 | 2025-09-14 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 148.1 |
| d11773ae-793f-3abf-b99c-5db9f27a1adf | -10.9286 | -47.2 | 2025-09-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| de2208c6-7a32-3858-ada7-a3c145d375bb | -8.9079 | -45.457 | 2025-09-14 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 0215d7c8-25a7-356f-93ef-991771068dc7 | -11.2541 | -44.7723 | 2025-09-14 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 2ce105e3-c22f-3877-9ff6-4de42594fd32 | -10.8991 | -45.4656 | 2025-09-14 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |


[Clique aqui para ver as próximas entradas](README84.md)
