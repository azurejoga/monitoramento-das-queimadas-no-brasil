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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c175ad0e-d233-3342-9c1b-759429e267f6 | -4.2832 | -59.6554 | 2025-10-30 01:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 75891cf1-27d5-3b1e-a8d1-2fe8c7793082 | -12.495 | -50.5684 | 2025-10-30 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 737e702c-8f57-3d06-a53a-c8946e37b543 | -3.2317 | -46.8716 | 2025-10-30 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 71a301bc-e7a6-3e01-9e7b-faa3d9587c82 | -11.137 | -51.1071 | 2025-10-30 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7709ae4d-a136-3ef3-9e95-c57e4b86189d | -11.1563 | -51.0839 | 2025-10-30 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 71f40070-996f-379f-8bae-845a71fc9331 | -11.1376 | -51.0647 | 2025-10-30 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ade7e6c0-81ad-3fd5-b0f9-9d0281dc3f67 | -13.5316 | -44.341 | 2025-10-30 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 630fd49a-d8bd-33de-a439-684e912a139d | -4.2648 | -59.675 | 2025-10-30 01:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| d098cbb3-061a-3f8e-a887-eec5c2eee568 | -6.0296 | -41.9692 | 2025-10-30 01:20:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 0b91657f-9dd7-3a80-806a-342f1d30290e | -8.3313 | -47.9219 | 2025-10-30 01:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 177.9 |
| f17efed3-9c58-364a-b5ac-1166d21f9e01 | -10.6502 | -52.1873 | 2025-10-30 01:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f75ecb37-bc4c-3dd4-9e49-c8eadb2d32bb | -4.2833 | -59.6362 | 2025-10-30 01:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f3a9757f-475f-3eb7-8b89-37834e7189e4 | -12.4947 | -50.5898 | 2025-10-30 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 5045dc2a-0e6a-35e4-ac12-717df749353f | -8.3311 | -47.9438 | 2025-10-30 01:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 015c9178-0d8c-34dd-85ed-4c628c64fb1b | -8.3125 | -47.9236 | 2025-10-30 01:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d3342c9e-3e73-3f23-a652-11306dec10f4 | -4.2831 | -59.6745 | 2025-10-30 01:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 379d2b12-e3e6-3edb-955d-5ade1b347d94 | -4.2649 | -59.6558 | 2025-10-30 01:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| acd72d94-7327-382b-8e19-361183615775 | -12.5141 | -50.566 | 2025-10-30 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 68917f48-9e64-3d75-94ce-3f7a9a639134 | -15.6064 | -46.5242 | 2025-10-30 01:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 73.1 |
| c97167fc-6eeb-3ce0-b918-041b25ce53d5 | -11.1566 | -51.0626 | 2025-10-30 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| decc32f1-864c-3fc5-a4fa-62e166043558 | -4.2649 | -59.6367 | 2025-10-30 01:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 9ce5c421-37c7-351f-8b03-55e30526bc7e | -10.6313 | -52.1891 | 2025-10-30 01:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b66e0a20-219c-3215-89d2-5da651df7215 | -11.1373 | -51.0859 | 2025-10-30 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 666b4174-3ab9-3199-8100-370e01811a47 | -3.8054 | -43.9002 | 2025-10-30 01:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| e437cee2-5c88-307c-b013-98fd73083965 | -9.4952 | -40.3834 | 2025-10-30 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 40b0747a-007e-37da-a172-8831bd2b85f5 | -15.6261 | -46.5205 | 2025-10-30 01:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 78ea944b-3180-3cfe-9827-5534a9afdc43 | -6.0108 | -41.9708 | 2025-10-30 01:20:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 2e3e094e-3d4c-3e45-811c-1847e975d995 | -12.5138 | -50.5875 | 2025-10-30 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 25dde942-f94b-3d10-ae16-b4612def7c07 | 0.2852 | -51.2114 | 2025-10-30 01:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 33.6 |
| a54c03bf-95bc-327a-ad93-4f2da2a895c0 | -12.3273 | -50.3096 | 2025-10-30 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 6918bfcb-cc54-3917-bd6a-aff7800541b2 | -4.2833 | -59.6362 | 2025-10-30 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 6580c69b-8403-36b4-a9ef-fe6fd0255b00 | -19.4701 | -41.5708 | 2025-10-30 01:30:00 | GOES-19 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.4 |
| dc46a86d-fa0f-3dbb-9e45-9b1c6316c903 | -12.5141 | -50.566 | 2025-10-30 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 425743a3-908f-32d9-b19c-0bf50c91dfd6 | -11.1376 | -51.0647 | 2025-10-30 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ec7d2b6d-88b7-37d7-89e9-26e28bdd9e75 | 0.2852 | -51.1906 | 2025-10-30 01:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 60a00463-5d39-3675-9f1a-3bce87342744 | -12.3082 | -50.3119 | 2025-10-30 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ae18dc6f-de59-3db8-97f3-007d2b6e1979 | -12.1958 | -46.717 | 2025-10-30 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 9c18dabe-236e-3d8c-85af-04bf59935619 | -18.2451 | -42.6313 | 2025-10-30 01:30:00 | GOES-19 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.5 |
| a6450b5e-f96f-3a38-8381-a20354f1c7d9 | -19.4914 | -41.5393 | 2025-10-30 01:30:00 | GOES-19 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.2 |
| 344bd63a-77e1-3032-8c63-2e9abeec40e6 | -3.2317 | -46.8716 | 2025-10-30 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 746e4316-72bd-3565-b659-8a4bda4ea79f | -11.1373 | -51.0859 | 2025-10-30 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 83ffae87-ec8e-3df6-bef9-063678549c3a | -6.0108 | -41.9708 | 2025-10-30 01:30:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| cdea85c0-026f-323b-bf53-82377e05a932 | -19.4709 | -41.5451 | 2025-10-30 01:30:00 | GOES-19 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 138.1 |
| 82b6645c-2196-300f-92b8-9da39d626772 | -8.3313 | -47.9219 | 2025-10-30 01:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| cb92a6ec-d20b-392c-bcde-845631b1d504 | -4.2649 | -59.6367 | 2025-10-30 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 9238f5fe-4e49-3c1e-92be-7e884dc13d1b | 0.2852 | -51.2114 | 2025-10-30 01:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 09b325cb-cf6d-361c-8c7e-6a961839699b | -14.762 | -44.9636 | 2025-10-30 01:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 658353f7-60c3-3781-990d-f024964650eb | -8.3311 | -47.9438 | 2025-10-30 01:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 5351f3c2-d48d-3841-8894-c71635fd9b23 | -12.8152 | -43.4481 | 2025-10-30 01:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| c65d008b-9fa8-3fcb-b0a3-a753504f31e0 | -4.2649 | -59.6558 | 2025-10-30 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 6cd615b0-862e-3764-97dd-12696d870aec | -11.137 | -51.1071 | 2025-10-30 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 77912a14-a5bc-3237-bf88-7b88ef81109f | -4.2648 | -59.675 | 2025-10-30 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b42ae3c5-960e-3207-9ec9-42d485746485 | -11.1563 | -51.0839 | 2025-10-30 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| f608b0b4-9c13-3986-9287-7b392fcb6f7c | -10.6502 | -52.1873 | 2025-10-30 01:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b77ea14e-10e0-3bbb-8a05-9863918abc37 | -11.1566 | -51.0626 | 2025-10-30 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| db00f966-a464-387e-ab66-af11907cbc4f | -4.2832 | -59.6554 | 2025-10-30 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 75774793-2fad-3876-b3cb-c2431421c418 | -13.3743 | -54.3159 | 2025-10-30 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6497744b-30d8-30af-8064-59ddd36b3de3 | -12.5138 | -50.5875 | 2025-10-30 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e0a11fff-5a0a-335c-a268-12500bfd520f | -3.8054 | -43.9002 | 2025-10-30 01:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| f0ad7376-dbb2-3378-8785-17da944f86a0 | -6.0296 | -41.9692 | 2025-10-30 01:30:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 3ea3ea35-9f66-3718-9445-a5c7c9b54c7d | -4.2648 | -59.675 | 2025-10-30 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| cee17cd9-adb8-33c7-b2fb-9d5028f5a144 | -3.2132 | -46.8723 | 2025-10-30 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 25e33e3d-5ecb-3db6-9078-12272419cfb7 | -6.5254 | -46.9074 | 2025-10-30 01:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 388cb2f4-2033-30e1-82e0-4ce2d62b1f2b | -10.6313 | -52.1891 | 2025-10-30 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| fa7a2afb-4d5e-3c81-9789-e6d81ea0152a | -14.762 | -44.9636 | 2025-10-30 01:40:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 3b0a67fa-05c9-33ef-a65a-7dbe63008217 | -11.1563 | -51.0839 | 2025-10-30 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1e4e1f10-5310-3f54-ba27-b70a9eff556b | -8.3125 | -47.9236 | 2025-10-30 01:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 311f014a-e28a-32d4-ad14-6b7fafd03bb2 | -12.8152 | -43.4481 | 2025-10-30 01:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 5aaae7a0-67a4-3e4f-b721-a3c3ed4e3e6c | -3.2317 | -46.8716 | 2025-10-30 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d411b9aa-9456-3ab8-8fe3-be4b2b2eabbd | -4.2832 | -59.6554 | 2025-10-30 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 420bd8a1-8e36-318e-a382-45acf99eb2a1 | -11.1566 | -51.0626 | 2025-10-30 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c84ecaeb-38ea-3f62-b909-e9c50b780494 | 0.2852 | -51.2114 | 2025-10-30 01:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 36.1 |
| b3b9a4cc-58b6-33c2-b4c1-eaab8c668afc | -19.4709 | -41.5451 | 2025-10-30 01:40:00 | GOES-19 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| e48217e2-a509-329d-8460-3d269a649e8e | -15.8161 | -42.6922 | 2025-10-30 01:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.4 |
| 6978efbd-f614-3183-8c9c-91cd7ebebc75 | -12.5141 | -50.566 | 2025-10-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| bacdbb2c-a8e3-38db-9353-f5c165cbd68f | -12.5138 | -50.5875 | 2025-10-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9d7d0c4b-0837-3fbb-a624-e6d79b3c859c | -4.2649 | -59.6558 | 2025-10-30 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| bb7a59c2-ab7b-3c91-b9d9-ff07dd60ad2d | -15.8167 | -42.6676 | 2025-10-30 01:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.7 |
| 8b6ade97-269b-3adc-a6a5-471e24d83c70 | -12.495 | -50.5684 | 2025-10-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d6440839-8431-3804-ba8f-604fed667326 | -10.6502 | -52.1873 | 2025-10-30 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6e3f8f56-af06-3671-ab67-1959601a2406 | -12.4947 | -50.5898 | 2025-10-30 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| d579413b-c628-3e59-b62b-517de96990cb | -8.3313 | -47.9219 | 2025-10-30 01:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 216aa51f-e0e5-3648-80e4-60b4fa6c3980 | -2.7741 | -45.3989 | 2025-10-30 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 48db7ac2-ccbf-3751-b1c7-2e0b38e891b3 | -6.0108 | -41.9708 | 2025-10-30 01:40:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 5ffa6911-825d-3348-a768-7c9db0443b49 | -8.3311 | -47.9438 | 2025-10-30 01:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 038c0345-70f2-346f-9c03-ae6083fba38e | -3.7867 | -43.9011 | 2025-10-30 01:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 339974db-f4b9-368a-97c1-e99500ad3c39 | -11.1563 | -51.0839 | 2025-10-30 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 41d4ae29-9ba4-3e0d-8217-9d20c83c36bc | -3.7867 | -43.9011 | 2025-10-30 01:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 38209b83-f882-3f1e-a40e-32574b245c22 | -4.2832 | -59.6554 | 2025-10-30 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 98a441bf-0aaf-32ad-aaf4-62dba6888576 | -12.4947 | -50.5898 | 2025-10-30 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 79cbce69-656b-34e2-a2ad-916e3e29fb3c | -12.5138 | -50.5875 | 2025-10-30 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| db7bb930-5d86-3383-b174-28ec5df426d7 | -2.7741 | -45.3989 | 2025-10-30 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 5c1ae98b-f7b9-3a5d-b11a-a6537ce197aa | -3.8054 | -43.9002 | 2025-10-30 01:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 2524b522-4e95-3d24-9599-5ae0d048d80f | -4.2649 | -59.6558 | 2025-10-30 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| a83b1c89-7286-3948-a915-abb046f0d07c | -8.3311 | -47.9438 | 2025-10-30 01:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b9bb2549-2ef1-3ba0-8473-ee8c58074dcb | -6.0108 | -41.9708 | 2025-10-30 01:50:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 34773dfa-290e-32b3-a550-652db0064968 | -12.5141 | -50.566 | 2025-10-30 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 70da5c85-2ab4-30b5-b146-c1b847cd7528 | -8.3313 | -47.9219 | 2025-10-30 01:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 2e3e1850-128e-3bbf-a76d-2ec58ac517a5 | -4.2648 | -59.675 | 2025-10-30 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 21fd2dff-ef92-3ead-a9a9-aca8bcd516f6 | -11.1566 | -51.0626 | 2025-10-30 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |


[Clique aqui para ver as próximas entradas](README10.md)
