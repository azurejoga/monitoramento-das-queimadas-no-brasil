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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5bc7cd8-d121-3f9d-bfb9-95c44ed6ffe6 | -10.38472 | -46.64944 | 2026-09-15 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73ae7d46-ed7e-3c72-a0d4-a17366d00fbe | -11.2332 | -43.45685 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96ceacd0-8060-3fed-8299-694502397ebb | -12.92736 | -44.7323 | 2026-09-15 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abecdfc8-8775-3c6c-83be-6b91cb70b600 | -7.56616 | -44.91761 | 2026-09-15 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a42d520-0089-3516-9f00-d98c6e799cc3 | -8.39725 | -42.2185 | 2026-09-15 04:14:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 15d973c3-fbca-3ce0-9d65-bb3a0c8a7957 | -7.09211 | -43.53936 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 48e5b377-b6a0-347c-8971-ad854690f17c | -10.0624 | -45.48374 | 2026-09-15 04:14:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3180acd5-1936-3f13-9473-3dc843dd9b93 | -7.09519 | -41.82431 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b6f8bba5-0fd2-3ce2-8ed9-e86c01d96fcb | -11.88674 | -43.82304 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 9e79b776-c0c4-3832-9e06-bf78ac7c5da7 | -9.36369 | -50.08749 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e65d1b5e-05d0-3a1a-a215-1e75754594ef | -10.09632 | -45.5593 | 2026-09-15 04:14:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc396d29-dd88-3c4a-8c62-b7ede3d79f29 | -13.51634 | -44.16727 | 2026-09-15 04:14:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fbab463-8663-344f-bca0-28fcfb00a644 | -11.1867 | -42.82812 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 76ee5369-663e-36df-991e-84b75afe2af6 | -9.3584 | -50.17036 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adb11aea-4ccc-3184-b487-7daff2da883e | -10.24356 | -50.91308 | 2026-09-15 04:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b81701f0-8856-35db-bcfe-dbd6e3060be3 | -12.85122 | -44.38682 | 2026-09-15 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aef466d9-4b99-3ef7-af4b-415f2f41516d | -7.01638 | -44.63224 | 2026-09-15 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5120289a-9948-36e9-a497-64d3e8ac7f75 | -12.55739 | -47.11647 | 2026-09-15 04:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a1322de-3947-31e1-978e-cf3656f21ee4 | -6.74076 | -43.09191 | 2026-09-15 04:14:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b0cf51b-3335-335b-80d8-11568b519541 | -9.35307 | -50.1433 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34f672bb-9c9d-336b-95ba-499cc0eb39db | -10.66782 | -54.13483 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7857ec4d-ab86-342e-bb3d-80025597ebb4 | -10.7075 | -47.50392 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c2a90db-7f30-39bf-9274-f7be5a73d151 | -7.48371 | -42.1222 | 2026-09-15 04:14:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8dcc40db-ad8f-3849-b55b-905ffb5ea466 | -10.70826 | -47.49957 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6ef0276-9bc7-30dd-ab97-3ae3f7b1eef4 | -9.35204 | -50.14357 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c95b2ae-e8f8-36a8-886f-abe675e472cd | -6.95095 | -42.55947 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3339ab28-5cee-3d19-93b2-3600973cd275 | -11.89026 | -43.82365 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 5c630860-8e9e-3959-947c-b250266646de | -12.85052 | -44.39097 | 2026-09-15 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b544c93f-c6e4-3b8f-99d3-5b2730de2b06 | -9.35653 | -50.11901 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 326a5ea2-3fa9-3759-8a15-ee7fdb47b84f | -10.67076 | -54.15498 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2ca1368-cc39-34d7-bd8c-01052b53028b | -6.95446 | -42.56006 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f3925df1-866b-30a5-a79a-fa68cf42aab2 | -9.41103 | -50.10386 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f477fb60-0494-35f2-85f8-5b8950be703b | -11.21551 | -43.43369 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 588c04fe-f102-3e07-b9f7-d854c81a495c | -6.96009 | -44.54021 | 2026-09-15 04:14:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7e60b7bf-e74b-3a12-a29a-141e786d4081 | -9.3566 | -50.18403 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3e30b95-15fe-3246-8bd2-1103fa177e96 | -9.3586 | -50.17347 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 62f37da3-9f96-3dc5-a5db-27592d103b65 | -7.12902 | -42.08939 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d1e94f5b-801e-33b9-90b4-d2e32817dad2 | -10.89882 | -51.54113 | 2026-09-15 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 489864bf-b254-3209-87f7-4cc7bb5d85e5 | -8.50338 | -50.14442 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81e3e380-bff3-3304-92f5-b771a8ca51b3 | -6.30001 | -41.68675 | 2026-09-15 04:14:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f22a6c99-5946-3695-ad4b-790f8f15a2b0 | -6.32843 | -44.12778 | 2026-09-15 04:14:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 622f68e9-4115-3799-a759-89c5746c623a | -9.35712 | -50.17743 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| caabfff9-712f-3e5c-8631-64f582f4121e | -6.10739 | -44.07344 | 2026-09-15 04:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e29f4ab-9caf-3917-83ab-4aa6eba137b6 | -5.29632 | -49.09249 | 2026-09-15 04:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8d6d686-b200-3d58-b091-48fb42f8ecf4 | -6.83108 | -43.51846 | 2026-09-15 04:14:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1554602a-05a4-37ea-a746-bb8472b36ceb | -10.7546 | -44.82228 | 2026-09-15 04:14:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b46ed431-a76f-32c3-82b3-0f89f1f75dbb | -12.55667 | -47.12049 | 2026-09-15 04:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 301f5f58-45b6-3e71-9351-6a92aae32861 | -10.67326 | -54.14272 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86bc679c-8016-3fe6-a570-3af7d4977042 | -5.15677 | -49.43993 | 2026-09-15 04:14:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bccfcc13-bae0-32c9-a55e-e4e67af97e75 | -7.16887 | -43.52352 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bac31c03-2af5-3991-ab1d-600322902ed9 | -9.25759 | -48.54181 | 2026-09-15 04:14:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8687e673-1e9e-3324-ae9d-3b51da85d822 | -10.71291 | -47.5396 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91f5d16d-b48b-31bc-bbf3-702592176699 | -10.99107 | -48.32598 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3921f6c0-a8c6-3c05-9cf8-60827c991fdb | -11.88436 | -43.81979 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 15c35128-e847-36a8-bd78-2ab12651b4c6 | -8.804 | -46.90514 | 2026-09-15 04:14:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00b25917-3952-3add-85c4-6d2ed6e09247 | -9.32253 | -44.35117 | 2026-09-15 04:14:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de8ab074-626f-3921-a990-49882b5891e3 | -8.60742 | -44.46266 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec5f94fb-139f-3fc3-9f15-b9fa8f2bb7b7 | -10.98961 | -48.32347 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0360bcd4-8ed4-3f12-9dbf-22a88678a3ab | -10.47225 | -50.99488 | 2026-09-15 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99f855b4-9fba-390e-b7e5-eff154a868cd | -7.07966 | -42.13157 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bd9936db-8a0d-3856-8e96-2ad4fe42b5b0 | -7.01723 | -44.62725 | 2026-09-15 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f91076fd-7507-3839-832c-c62b14b8b2c5 | -6.6456 | -43.55146 | 2026-09-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0e96d43-eb94-3dbd-81cd-8e05c5d957ba | -12.49471 | -41.42488 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a7f7edb9-55be-33e7-8a85-457aca53e20e | -6.19546 | -43.02487 | 2026-09-15 04:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11e6c984-2f07-3cc6-8138-43d6d066dff1 | -7.48088 | -42.11791 | 2026-09-15 04:14:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5fdaaf94-a73a-327a-8a5d-22a0c609071a | -7.46278 | -46.14957 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b94581e-9501-3165-8360-1fd4bb7bac05 | -7.55136 | -46.87006 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76a52f05-7359-36ec-8001-533a203b95f1 | -7.09067 | -43.54799 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 487be422-885b-39ce-ba18-d371e3d2fab9 | -7.19534 | -45.91971 | 2026-09-15 04:14:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 305556b7-68f5-3d5f-9958-9c5b3e78cdb3 | -7.1679 | -42.11123 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51786875-204d-38d1-8dcf-a7019b7596b5 | -11.12478 | -40.48322 | 2026-09-15 04:14:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e1fd6ff-61e6-34f0-bcca-a7906016f09d | -6.78858 | -43.18523 | 2026-09-15 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9de85de-94c2-34ca-b765-d3b3312b5921 | -10.05123 | -44.88749 | 2026-09-15 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d27a4ab0-467a-3b26-a178-604b8d59f009 | -11.4963 | -45.74647 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f14b94a4-b0c0-3e95-bd16-ce27538d32db | -7.61766 | -47.29513 | 2026-09-15 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d4d487e-0421-3dbe-84cd-9094467a38a7 | -11.23669 | -43.45745 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d993144-eeeb-39aa-8f9b-1cd499240a73 | -11.17657 | -46.38173 | 2026-09-15 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c27a19a0-b565-3a98-aea4-d998769c5eb6 | -7.10438 | -41.81073 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 26e3b916-303e-3fd6-a9f1-8db8837b28f7 | -12.3865 | -44.39595 | 2026-09-15 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 947579f0-0d4d-3f59-a96a-c9a4bb1b72a4 | -12.49083 | -41.42787 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2dbd2bf-7804-3adc-be66-afdaad42fd73 | -7.47805 | -42.11363 | 2026-09-15 04:14:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e885060b-d7f8-343a-827b-1e637c9ead5b | -10.46951 | -50.99342 | 2026-09-15 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ee959f4-ccce-3e3d-ab66-f2118df26c3c | -11.80388 | -46.60282 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9c41898-bd37-3db8-8b34-8808eba6b5d5 | -12.4876 | -41.41258 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1c11001-f9ed-3a03-8094-8cb8b592885b | -7.96975 | -43.97968 | 2026-09-15 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93d1b1df-90c9-3a9c-863e-b5ac3d1c69e8 | -9.41709 | -50.10141 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2d3bef2c-7393-32db-94c1-a9cb87f5e5ab | -7.55098 | -41.83699 | 2026-09-15 04:14:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b8d7f74-8b47-3c9a-8b73-1fc8b7146666 | -13.30771 | -43.7152 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94ff9b7d-af91-36be-9da9-8e91ffcec33e | -10.03551 | -52.09766 | 2026-09-15 04:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93ff8f4b-cb2c-3ce4-9b66-90beb077c48a | -11.50496 | -45.78969 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0c29a1d-55e8-368a-a821-26c6235ada65 | -5.8707 | -43.51012 | 2026-09-15 04:14:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99960982-3e8f-3a8f-bcc6-2fa9173060dd | -11.79697 | -46.5939 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99d00a36-8ccf-33e9-8919-0c7f1dba350e | -9.36039 | -50.10487 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f820eff-0e64-31e0-9c38-ebf19a6250cf | -6.61671 | -44.20185 | 2026-09-15 04:14:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ff2b7d4-0837-3f41-92f8-317f11742845 | -9.28722 | -50.3113 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b44de24-94b2-3d68-8710-a997f70509d9 | -11.89162 | -43.81565 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b9fa82e-97ea-3404-baf7-10a9ecd0ccb6 | -13.55351 | -43.52803 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ec4adc2-1956-38e8-8a90-9a02c216c21f | -8.02927 | -39.00506 | 2026-09-15 04:14:00 | NPP-375D | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 206ef973-6488-3073-8fdd-3f39e4e5413b | -12.17384 | -38.59585 | 2026-09-15 04:14:00 | NPP-375D | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 70179122-484f-3b1c-98fe-0d3c6f8815a9 | -10.95611 | -39.26799 | 2026-09-15 04:14:00 | NPP-375D | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README26.md)
