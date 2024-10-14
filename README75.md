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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd5ae5a0-5f46-35a2-bc99-22c6e6900856 | -4.66 | -45.71217 | 2024-10-14 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6d806eda-feef-3e79-ab8d-e19246defeca | -4.64731 | -45.71517 | 2024-10-14 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7c229d3-a281-3cd2-a5c3-bf0b95593dae | -4.62157 | -46.07474 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ac65fc5-526b-3881-a95a-1259878da959 | -4.52327 | -45.6769 | 2024-10-14 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ef5cc05-6868-38c3-8489-0d8c38f318e1 | -5.60719 | -46.372 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21682b9c-86a0-3d7a-9c56-b93e2b202bdb | -5.49362 | -45.84467 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97abe841-231f-3db6-9b48-302a1fcfabe0 | -5.47111 | -45.8308 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b881965-ed69-3f80-b14a-8505edbfb02a | -5.43693 | -45.88736 | 2024-10-14 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78bd90f5-efd7-38ee-9f69-e7616e2ff7af | -5.41223 | -45.88897 | 2024-10-14 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 688c37a6-63f2-373d-8e7e-ab9054f5463a | -5.30043 | -46.36887 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b36e9793-7e11-3d14-9fc8-bbd1bb0a2bc8 | -5.29511 | -46.37809 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8f4dac5-3006-38da-86e2-98fd4bcd51ba | -5.28639 | -46.35698 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1bb2642-f7bd-3cc0-b5bf-98bfbff8a926 | -5.28569 | -46.36175 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d81d9f3-2a84-33a1-9531-0cbaf31a0bd9 | -5.28111 | -46.36604 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81ba0127-0a22-32df-b692-c96ffda44b59 | -5.22783 | -46.02075 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e730fecf-0753-3601-9f6b-e432d60c9f03 | -5.22547 | -46.01867 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7a9afd2-f1e9-3c8b-9a9c-f57cd20832e0 | -5.22153 | -46.01808 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1a0adf0-8afe-3933-84a9-e69074e0005a | -5.18693 | -46.1651 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2501530a-7ee9-3d87-b707-66a76e1cd53a | -5.14276 | -46.1933 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a092fb6-3022-3f2d-aa06-bdb9d7783441 | -5.14209 | -46.11799 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffea4edc-e7ae-3a23-8609-8885d41ac039 | -5.13916 | -46.05701 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f4d4f969-6722-35a8-a349-7190e0709635 | -5.13524 | -46.05637 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc88793c-9f72-3b19-a829-44518c488085 | -5.13449 | -46.06142 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7fdc157-b885-3ab5-8ef6-26d8f6b28132 | -5.07121 | -45.86975 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cac3536b-d5d9-32fd-9991-efcc5d378a3a | -5.07045 | -45.87489 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d1c8ec06-59fc-3cc1-8180-e544b6eb0498 | -5.06648 | -45.87428 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5fd7222-78c5-39df-8fe9-520eb51f7493 | -6.40045 | -45.95541 | 2024-10-14 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1b6185d-e8e2-322a-a9e5-c63de839b4f8 | -6.39309 | -45.92208 | 2024-10-14 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d0693d2-4160-392c-ae8b-eefe40e8cd41 | -6.37627 | -45.72723 | 2024-10-14 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 88c97259-cdc5-3d26-97b0-1533c302d09b | -6.37273 | -45.72292 | 2024-10-14 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50f27baa-4a4e-3b0c-8de5-e6c9af837f7f | -6.3722 | -45.72654 | 2024-10-14 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 239a547d-be23-35bf-8383-cda1d748f48c | -6.3382 | -45.87455 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e841f58-e0eb-3e0c-a4a7-21acdcc3eba8 | -6.23327 | -46.45583 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8df4c38-7092-3690-aebb-430ef86c0a63 | -6.23315 | -46.4576 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a98ddeb-7ca2-3657-944d-8e13ac01b527 | -6.08792 | -45.46429 | 2024-10-14 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e239ff8e-4d9e-3941-bdd7-650a134d1c8e | -6.07896 | -45.9993 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ac09e55-8db2-331b-94e5-ac00ad0e091f | -6.07201 | -45.99962 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d3f83ea-95a6-3e94-ab71-a38acc80a2b9 | -6.07096 | -45.99817 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b56c34d-46fa-3570-b7c0-b64f6a0d3cc3 | -5.87993 | -45.55825 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc079cef-45a7-389f-956d-b71cbe376741 | -5.85122 | -46.23169 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dbe16b6-ce9d-3a03-8984-de33aa6d2046 | -5.7834 | -46.50512 | 2024-10-14 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd44b656-5f40-3827-b6fa-9504f72df61e | -5.78259 | -46.50327 | 2024-10-14 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96964502-c7fe-3708-a488-7b4452f754e4 | -5.78185 | -46.50811 | 2024-10-14 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6559d6c-8de8-36a0-841b-7c83ba06a0d2 | -5.70474 | -45.67614 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cedcb656-cab4-3f2c-9a27-8f2621fab991 | -5.61884 | -46.37363 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0fdfe73-6bd4-3d98-b9ea-69f73202703c | -5.61495 | -46.37315 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c33635e8-b573-38ad-a482-56bc2d5c9d6b | -5.61133 | -46.45113 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae90488a-83b6-39a0-83ca-252f1158bbd8 | -5.55677 | -45.75172 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4e067fd-56bb-3a43-861a-79df0f3e0f1f | -5.52538 | -45.95956 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efc09b08-79e6-39e4-bc42-1bb84ec5f4ce | -5.49897 | -46.29158 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a84377bf-3480-318b-891d-ae208fb223a6 | -5.48962 | -45.84407 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 168add69-3fc2-30b7-857b-03f5b3baaeab | -5.47513 | -45.8313 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0f5e12b-5045-3330-b76e-981526ce3491 | -5.43294 | -45.88676 | 2024-10-14 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5a93ed9-b6ae-3df4-b1c5-68254a56d68f | -5.2871 | -46.35216 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b37974b-f8c4-3677-865d-b4ae968825ac | -5.2842 | -45.60762 | 2024-10-14 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f92633f-963e-37ec-9ad7-6d44489a4159 | -5.28251 | -46.35649 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d76e11da-4814-3c41-8ad2-9dda5a8463c2 | -5.28036 | -45.60759 | 2024-10-14 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5b40427-a028-3342-84a7-d6ffca158d67 | -5.28014 | -45.60709 | 2024-10-14 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 676328cd-45bd-3ba7-b269-736dfbdccbf0 | -5.26136 | -45.51374 | 2024-10-14 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2715396-a25c-3f55-9ce7-841c5a20a2db | -5.25729 | -45.51307 | 2024-10-14 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53116f1e-17f3-3e31-ac48-008c906c510e | -5.22708 | -46.02583 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09c88933-3dcf-3c90-8a65-620f88cb9dfe | -5.22468 | -46.02379 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af33809b-4f57-3847-8f0a-4c39e3d43798 | -5.22389 | -46.02014 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfb3ff2e-10a4-3296-9136-af939ed06ce5 | -5.22314 | -46.02527 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 249c6f00-427d-3230-8fa9-7dd47683a8f1 | -5.22074 | -46.0232 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa64412d-03ec-36d5-9d85-0681e02a9f8c | -5.21995 | -46.01954 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96a0747a-0ea8-3968-a45d-2d8582cb86c1 | -5.2192 | -46.02468 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34b2b2ca-f222-3d58-90cc-45b13d32f997 | -5.19023 | -46.06477 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cdc9461-d0a4-3f5a-97a9-de331ece37d9 | -5.18639 | -46.16675 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38750b0e-4252-3586-8dd2-a006c75f0d4d | -5.18618 | -46.17 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21262758-b842-36bf-88dc-8c5704c849e0 | -5.16492 | -45.38148 | 2024-10-14 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1904707d-6ccb-38b5-9dd0-cfaf7d820b2b | -5.16438 | -45.38507 | 2024-10-14 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe89d95d-2d91-37ea-a3b3-fecdf622b737 | -5.16081 | -45.38088 | 2024-10-14 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aeb64900-526f-3ffd-bbcd-4a061893d37e | -5.16027 | -45.38446 | 2024-10-14 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36554b66-967a-3f0b-a561-2f2eddeb9ac9 | -5.14349 | -46.18846 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f0e9b4e-3444-36b6-8492-07039607a4df | -5.13841 | -46.06205 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 22f777de-1f75-3f7b-aadc-b334b804d9ef | -5.0749 | -45.81779 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98b58f82-439c-3d63-82e7-a9a31d8ff224 | -5.07058 | -45.76443 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83a566d4-b23a-384e-8bd7-8c7c713f36b1 | -5.06724 | -45.86918 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b8fddbb-06a1-3d0e-a8e3-b14eb252d2f9 | -5.06658 | -45.76384 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85f0be1f-9609-3620-998a-5cd951f4a0e4 | -5.06396 | -46.07896 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 386698b1-c45d-3697-9077-638e04ebf270 | -5.06003 | -46.07846 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ab6cdb0-197b-3e55-8b5f-d1924ccaf978 | -5.30476 | -44.96499 | 2024-10-14 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 670e0273-5559-3334-b7f3-7366a887930c | -5.30441 | -45.22723 | 2024-10-14 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 561910e4-5fe7-3547-9e2b-d72c396aa375 | -5.24023 | -45.11298 | 2024-10-14 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76000a14-4ddc-3a10-b031-52a5b32c0703 | -5.23978 | -45.10997 | 2024-10-14 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb5c9097-c1d9-32ed-af59-e02ef067fcc2 | -5.2392 | -45.11376 | 2024-10-14 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 359e6c98-17fe-39a2-abf5-ba18bdc59451 | -5.23559 | -45.10933 | 2024-10-14 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dec79c0-8414-37d3-afc4-36de2b27e90b | -5.23501 | -45.11317 | 2024-10-14 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1a91936-5cfa-37ff-b5d5-c19e3f7d26f8 | -6.40447 | -45.956 | 2024-10-14 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a8f75e6-cbcd-347b-8528-a7a0dfbc5c0d | -6.39257 | -45.92553 | 2024-10-14 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49f508e9-0dab-35b3-a021-e7701ad5df95 | -6.07601 | -46.00019 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 214751ad-7137-308d-a30a-46d1aada18b7 | -6.07496 | -45.99873 | 2024-10-14 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3718e9fb-7c82-3e1f-9ffa-e98d9cf03b96 | -7.42141 | -45.57802 | 2024-10-14 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbfdfdc0-0498-3c2d-a128-0b25d0da7da6 | -7.42083 | -45.58189 | 2024-10-14 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8fa072f-b328-3d89-8aec-8ea1590e5ef5 | -7.39365 | -46.12873 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 684c2eb8-0ab7-3d90-9d76-699503b51cf4 | -7.37048 | -46.11777 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e88bca8-6e1a-32f8-b0dd-1904e7dac7de | -7.27792 | -45.7047 | 2024-10-14 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adfa1f22-c2c3-309e-9fa7-bd4e68415db4 | -6.97394 | -45.55043 | 2024-10-14 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76124185-ac3f-3acc-9650-422324403324 | -6.96976 | -45.54986 | 2024-10-14 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README76.md)
