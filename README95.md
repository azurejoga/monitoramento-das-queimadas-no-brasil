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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2193613-f303-3783-a38f-4e60f3b5482e | -3.69753 | -60.56451 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4913a4d5-4d07-351a-bdac-e19843cab3a1 | -16.8854 | -50.59108 | 2026-09-20 05:25:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 9616dc75-37db-330c-80bd-995296cc1b18 | -11.02474 | -54.14129 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3f07461-5eb2-36b5-8155-76b992c16ce1 | -4.51208 | -55.46664 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 844af63d-4ce7-3f40-9192-cb22364502aa | -14.91369 | -49.91334 | 2026-09-20 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c92bf217-678a-32f4-bed1-0a97756e7a07 | -11.7276 | -54.55969 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b5e9a22-5bdc-3346-b18c-4cf44587bbbd | -11.94575 | -55.925 | 2026-09-20 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0573c229-b18a-3b83-813b-d50a8c60bb45 | -11.72354 | -54.55404 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7eb17d5-7d08-37b4-9b1e-8be93732e1e6 | -11.2232 | -54.07469 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9fc96ef3-ec16-3fae-b5a4-70602191d2ac | -11.38022 | -51.38487 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3bfb2bcf-7616-390c-9412-bba8fb98e5d3 | -3.69158 | -60.60245 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28f5ad89-911e-346b-a46e-dbdf21afbc05 | -12.81013 | -54.06046 | 2026-09-20 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9cba27fb-4871-347e-9811-c260e2fff9eb | -3.36523 | -61.31355 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7706f0f6-7ebe-34ec-82ba-f49fb7dd3388 | -5.86427 | -51.56649 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 550cb5f4-de43-3aec-b281-d2c58311e2bf | -13.88266 | -48.57651 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 118995bf-e810-3842-a0cc-55eca13570bf | -11.21378 | -54.0779 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e5273931-0d85-3bd2-a090-38c74da5caea | -7.16166 | -47.47042 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1cd17cf8-0361-3344-84c7-2b698d58b51c | -11.21357 | -54.07324 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| de0ca7c2-3bd3-39aa-bf20-9c24cee1e89a | -6.39381 | -54.88221 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba89e760-d59c-3732-ae91-d4a19023f04d | -11.48113 | -51.4812 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbe80447-2639-3995-98da-67eeebcefb3a | -6.33632 | -55.28742 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82591432-883e-3bd4-bbf8-d43f225d337f | -5.87096 | -51.55746 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccb8cdc8-8b7d-33b7-898c-d690a32a410d | -4.48483 | -55.48607 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83e53bfe-77e0-38ca-98d0-198ded4dfa98 | -5.87222 | -52.04353 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb12bfbb-1a4d-316f-bcad-bf208e24a6b3 | -10.56798 | -68.66696 | 2026-09-20 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afb56097-040d-3c8a-9797-ac1479962ac4 | -11.21788 | -54.084 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 70f1e3c7-2eb9-3eb3-9487-1eb4d322e0d2 | -5.81755 | -57.53953 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54e6e57f-a97e-3f1f-8c75-17125ff9c3a5 | -6.29296 | -47.60793 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52cac650-8139-3754-a47a-f2bcce8fe067 | -6.29901 | -47.61486 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c121dcf7-bc10-36ed-81af-d688de0ae538 | -11.20897 | -54.07714 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3682be7e-4414-3e18-8183-21c2d4036ccd | -11.37683 | -51.41346 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49b6289b-a38c-39b3-8d56-3fd719713835 | -12.31814 | -50.72462 | 2026-09-20 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2240a1d5-cb85-341d-9697-55a5376dbe8e | -10.92077 | -53.9687 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e14223f-4e49-3141-a2c8-511cdc74d61c | -6.31212 | -47.62841 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d1ccd4cb-8a42-3f5e-a58a-78b9352e31de | -5.32053 | -55.85811 | 2026-09-20 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6e07f64-f3d1-3bb0-84a3-8b8aa4d40d28 | -7.16098 | -47.48482 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 31672dee-c61d-3d83-ab28-b26e429e1002 | -11.01651 | -54.12936 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c492037-a7cf-376b-961b-46e041038ed8 | -3.363 | -61.30593 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15abc968-baac-3fc6-a565-449761e567a3 | -10.8746 | -57.15395 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36c7b3e3-a729-38c2-8320-f638a65a1eff | -11.73294 | -54.55532 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84aa1a05-bed4-3412-ba5e-98b801f0e6f6 | -10.89376 | -53.98676 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39f99cef-dbb7-3ddb-9953-6617bc0d0ff8 | -11.37251 | -51.40038 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 117a244d-37e4-32f8-981c-4c390ca6393c | -6.19602 | -55.45522 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 100ef27e-8177-3026-8f2a-10e1537ecfe6 | -10.87524 | -56.22428 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5eb2778-37b9-3328-83be-475478c747d0 | -3.68496 | -60.60143 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c98cdad4-2c78-31ee-bf7a-af0075577bc4 | -5.74427 | -57.59693 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 039057f8-5473-3d56-a80f-611ba54e2e06 | -5.85619 | -53.53823 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7924cd57-23b1-352d-92e4-3e9aa07d2766 | -3.79368 | -59.70618 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f2969c0-fecf-3a9f-aacb-fc3e8ad3a861 | -13.89571 | -48.58843 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| adfbb96e-3541-365b-abaf-5f3230e92d62 | -6.31097 | -47.62953 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6b592f34-2039-3658-99a4-29e7fdaa74f0 | -11.02062 | -54.13539 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9195b1f7-bedd-391e-86d2-c7a741f40503 | -5.88723 | -52.04842 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cbf3945-f97a-31a0-a8e2-a44107b5c45f | -3.59788 | -58.71264 | 2026-09-20 05:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e81c9898-1e8a-3195-9624-69b5bc41c2ad | -11.12826 | -54.01704 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3b3d9c57-c5b1-388c-90c7-37bf06fe6c66 | -12.53917 | -50.04276 | 2026-09-20 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4c39975-dd9c-3057-ab33-2d8678e0519e | -11.01664 | -54.12857 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74d60282-09a0-35d1-8e99-d09fe1c6efff | -5.85773 | -53.49402 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82db5ae8-78b2-31cd-bb6d-e21781084408 | -5.20803 | -56.04531 | 2026-09-20 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 330c575e-3576-3a0b-9f0d-e4a81a1f5889 | -6.15394 | -57.71227 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df888b7b-24f4-393f-987d-183f06c7e376 | -14.66804 | -54.46512 | 2026-09-20 05:25:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 720aea14-c512-3954-ac63-daaaffcf6fb8 | -15.86437 | -49.91516 | 2026-09-20 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43a7f91a-3d05-3f68-8504-b06f7e51bb28 | -10.87472 | -56.22813 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 736cfcda-dc16-36ac-8033-d2e79b044530 | -11.31433 | -51.72041 | 2026-09-20 05:25:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28710837-8d96-3b0b-b9cc-22d12a892489 | -5.84031 | -53.55045 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88691ce1-e414-3d70-ae15-938887b723ef | -10.88514 | -54.08869 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ae97d1a-c977-3050-8633-559d403c74d8 | -11.12759 | -54.02234 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| cab0e1aa-c848-349e-a469-32c068959cd2 | -12.77625 | -52.85907 | 2026-09-20 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f68efb7-cdea-3705-94be-326e2a1c5825 | -11.69549 | -58.83237 | 2026-09-20 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 101626e0-549d-364f-8d7b-3fd0fc2d8c3d | -4.80723 | -56.07729 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 319c5516-c822-34fd-94f1-60602979098d | -5.73524 | -51.76144 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4d1e4f0-eebe-3c11-9059-f1424b82a111 | -3.48189 | -59.59027 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbf0272b-77e7-3f81-9762-aba60f5aba80 | -16.89189 | -50.59178 | 2026-09-20 05:25:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| a20f4971-644b-3cd6-93c2-bb84957d9528 | -7.16164 | -47.42523 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 27faaffd-4c50-3966-8374-2d1c831d3d09 | -9.9717 | -59.48749 | 2026-09-20 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec3a0f93-e036-3bab-8881-8d88e362680f | -12.01888 | -51.47844 | 2026-09-20 05:25:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e34d4458-c1b1-33ea-9978-e6abce712c9b | -3.68983 | -60.57038 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 926bb2fd-8ef6-3c44-8a23-ce67c2e3cc5f | -7.16524 | -47.45223 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddc0252f-2d53-34fe-8f79-00b1a2338bd8 | -3.69476 | -60.56055 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24cea54f-eac7-3d9a-8d43-94b21e22766a | -11.13348 | -54.02129 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fde32053-0845-3820-84aa-8d28126bd332 | -5.85551 | -53.54303 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e9d11c0-6530-3d34-8a20-2fe3c767e980 | -3.68773 | -60.60539 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72c1bfde-6291-3c0c-80ed-40e87aba366f | -3.48081 | -59.59717 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6deeb33b-bcce-374c-af3b-4dde569cf7a5 | -6.294 | -47.60661 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd6f6a51-38cc-3a7a-9e6b-f51b3971bf7b | -13.88706 | -48.58154 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5bee77f7-96d6-377b-8bfc-bcc25e58b25c | -3.59034 | -59.06631 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efe06042-c83d-3dda-8baa-ee9840847611 | -3.69332 | -60.63453 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb66841b-0d8d-39e0-b3b9-90caa5031eaa | -10.92776 | -53.95325 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 55093232-3ebd-3157-9ab1-2984e3e46c89 | -3.59755 | -59.06383 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcce9c5e-c3c6-3a79-8016-d1d025af7061 | -12.33306 | -50.70253 | 2026-09-20 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bd92d86-a220-3e48-8123-019b16f18da3 | -3.88357 | -58.95291 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87383356-1d1b-3dfe-b2a7-d230c75cd373 | -13.25208 | -51.73949 | 2026-09-20 05:25:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da7f21c8-a4bd-323a-b42d-b9e3713d7666 | -3.69001 | -60.63402 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40a7661a-3a0a-3a1f-8d3d-f6dfd0fccb72 | -3.79862 | -60.72174 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d411ccb4-c7bd-316e-91af-86e2721c7632 | -12.87794 | -51.00252 | 2026-09-20 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7b08d5e-b81a-35d9-8ca3-5fa0eed3d818 | -3.80402 | -58.89736 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 633557a3-c8b8-3568-ac83-7cdff0c61040 | -12.76557 | -52.85745 | 2026-09-20 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc021f3e-079d-3192-bba6-e1ea39ccf129 | -3.6861 | -60.61574 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52c33d51-74b8-315a-be08-5cd4cafe8f48 | -5.37268 | -56.04925 | 2026-09-20 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3cf62e2-9bf0-3a8e-bd9b-ddf0404d3383 | -11.09827 | -54.02715 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| f9d286a6-37e8-3971-8099-30e03a0a3264 | -6.33125 | -55.2637 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README96.md)
