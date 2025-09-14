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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac32b71f-96d1-3c44-8a0d-afc60fb27818 | -12.75588 | -48.00651 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fabfec6c-7434-3902-a402-8ca5ad7f651e | -6.67539 | -45.5156 | 2025-09-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e659226-17d5-378d-929f-f62e5a2347c8 | -11.48047 | -50.76972 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 48f62b95-7185-3215-bf06-7429d06acbe1 | -12.74695 | -48.01783 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f552871b-fb15-3a7e-8ddb-3637276c6851 | -10.4017 | -50.59849 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9794d36c-3494-3efd-a6b7-63433992e260 | -13.94744 | -44.85085 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 309.2 |
| ea7250f4-a464-3d9b-a3cd-2ae6f7e76f2e | -12.25589 | -46.78943 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd296204-9a9c-3113-a627-a54f16796458 | -8.62046 | -40.20072 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 591a31a1-3460-3bac-8aeb-04f26bc26695 | -11.46584 | -43.58218 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4bc9848-4266-3226-915f-dbd315d5bf16 | -12.75648 | -48.00238 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb9881cb-2086-3a74-a3dd-b129eff8abdf | -7.51577 | -44.37283 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98b56165-550d-3f87-bb00-f9d2d425fa05 | -6.61071 | -51.04542 | 2025-09-14 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fd9b009-3b38-32c2-9cd3-b0a16642ec14 | -7.61778 | -46.71725 | 2025-09-14 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 492d7aad-a180-3a57-bf22-aa72814d2973 | -12.73863 | -48.02498 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5e71e759-2bc8-3975-b6ce-53bb663f07cf | -7.73011 | -45.31458 | 2025-09-14 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d56f735-05d2-3f79-b4ee-8d1287930534 | -13.01118 | -47.99364 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e7619fa-5113-3856-ab07-dcfef40349b7 | -7.09745 | -45.14154 | 2025-09-14 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfdc324c-119c-37eb-b0c2-02eb127181f4 | -11.4623 | -50.75604 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9d6f1988-8c87-3c6d-a2c7-3fd835251816 | -11.45184 | -50.75795 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 035c16f7-a269-3b45-9835-c0bb566b87c9 | -11.46341 | -50.77057 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd512e85-3fe0-3c86-8a89-556f7620d80b | -11.43698 | -50.74481 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eed5dd6-a993-357a-a3d2-0d4c15890a06 | -10.32738 | -48.82392 | 2025-09-14 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9afd9d8d-677a-3cb6-9147-45d85b939e32 | -11.47167 | -50.78265 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f30bc44-04f5-39b7-b29c-ac96eb32fff0 | -7.39884 | -49.97861 | 2025-09-14 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 758f295a-aabf-3274-8e51-4df90c1f2aee | -11.30775 | -50.8311 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b22ba96-a543-3ae7-88d7-56fdd142fb11 | -11.49422 | -50.76834 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d8c1078-21de-3153-9aa0-c35115d1f5a4 | -11.38449 | -47.71571 | 2025-09-14 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95f5ae47-8d99-377e-822a-32b449185668 | -6.4462 | -44.49246 | 2025-09-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5c1e9c2-6fdd-391f-92fb-49863a2fb097 | -8.79424 | -48.10791 | 2025-09-14 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5327e41-9cb3-359f-838d-fdfd6e5605b8 | -12.95107 | -48.03006 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf24e22f-9350-395c-9929-452b9b79e205 | -11.40223 | -43.52808 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ed0b530-7049-3cc9-b524-0679da49f95d | -6.8855 | -45.63888 | 2025-09-14 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c145d0e-2f40-3af4-996d-4c8a93510912 | -11.1269 | -47.65128 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e983bbde-faf1-3d5a-bb03-af93007fbe25 | -6.6593 | -46.08969 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6802a5e-39d0-3a36-9433-8fcdefe2d8f4 | -7.53012 | -47.63553 | 2025-09-14 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b6b7706-3e3f-3184-879b-6d15ed7cd5a1 | -11.47992 | -50.77322 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daf3171a-ebcb-31a8-b46a-a2bc9dc92a61 | -10.34716 | -48.83052 | 2025-09-14 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9860d405-9415-3cab-9aaa-ef9d45c23aca | -11.81554 | -48.23427 | 2025-09-14 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 142d6b2e-b437-3784-ada1-63568f469bc2 | -7.52954 | -47.63932 | 2025-09-14 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0283e8a-999b-32b7-8897-d505f05777e6 | -11.4612 | -50.76304 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26a16dfc-7ca3-3a87-b76b-cbf961faa4bc | -12.99861 | -47.9794 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5872f13-b6d7-3a03-81c4-6acedf6dc918 | -11.31435 | -50.83216 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d7d4c02-a962-32ec-849d-09178260b050 | -6.70063 | -45.52633 | 2025-09-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1aa9f37a-9229-3725-a0bd-5bb14677a456 | -9.01828 | -47.03528 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6779688b-1e38-3a50-9758-26e613b7e17e | -10.76365 | -44.77501 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 382a4ec0-ebf6-393e-a914-32346d26792c | -11.46175 | -50.75954 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 74471ff7-5ce8-3fe6-8a69-65c411e11fd4 | -12.99384 | -47.98708 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4148fd3a-ee8f-3adf-a094-68bbf9601b4a | -12.93205 | -47.94281 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da938d71-f3da-336a-95bb-53d75f35a33d | -12.78203 | -48.0275 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82e0195e-e26e-3d6c-86a4-58b84b8388cf | -11.39426 | -47.33596 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce8d989b-c824-3466-82a8-567a9a0fdf62 | -12.45403 | -48.0196 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c91ef946-e5c6-3ea0-a197-390caa82843b | -10.40279 | -50.59151 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0d3c8a9-13ce-3a84-b452-aeffbb3d67f6 | -12.14596 | -47.59656 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3271e396-afa3-3a87-a8e6-bd922dba52ae | -11.47607 | -50.77618 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b61c7f0-1153-3275-a423-5d3ee22ba95c | -11.29794 | -50.82592 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5da4a17-2b7b-3a03-8e05-95f0e875b2bf | -12.82277 | -47.9489 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 57dc484e-e087-3e3e-bf32-e0e9735fd1fe | -9.63511 | -40.61578 | 2025-09-14 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 66c09d43-4511-36fb-be39-442fef49320a | -11.46893 | -50.80013 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a043c903-42d7-3248-85db-cf6fed9ba547 | -12.14717 | -47.58807 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b47a2082-a87f-39cb-8a4a-5d1ce8d8cd8a | -6.57998 | -44.37484 | 2025-09-14 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97da09a6-236a-3138-b8b3-1692bacca18b | -11.47665 | -43.60117 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd8e65f7-c8a0-312d-ae34-afd19fbac80f | -12.75945 | -48.00705 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42c2c35d-e80c-3274-afd6-cb317aec408d | -12.77076 | -48.00459 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f563354c-4a64-398e-92b7-d7d40e00de39 | -8.35799 | -44.73843 | 2025-09-14 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83acbaf9-c9d3-318a-ad00-9251a695526c | -12.78082 | -48.03577 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c53de13b-cf15-3503-ad1c-acfdd7942352 | -12.95749 | -47.98534 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd081795-1a80-3b2c-8122-49e2da038f9a | -10.93518 | -47.35568 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2ca52ce-b17a-3c4f-8bbb-f9477bf799b6 | -8.4979 | -44.72121 | 2025-09-14 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f80c0912-5efb-3587-9625-5fae52d97077 | -6.69791 | -45.5449 | 2025-09-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a1d40d4-f943-336f-badf-b2bca6175354 | -8.93322 | -48.65306 | 2025-09-14 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3499bdaf-1bf1-3f94-99e6-b4a28ed0518d | -10.324 | -48.82336 | 2025-09-14 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 731bf142-25e8-33e2-ab56-602eddde0f06 | -10.39894 | -50.59447 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e21f38ab-0a11-3af5-8cdf-be06498b7f22 | -8.50503 | -44.72976 | 2025-09-14 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e56a1d2-b7fd-3b1e-af6a-1546e8b19413 | -11.48433 | -50.78827 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 05cd64c5-1431-384e-90a2-6375ccd7d400 | -11.67237 | -46.87357 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0094a0d4-d44b-3a3e-9358-5eee51fff2a2 | -8.03271 | -49.40543 | 2025-09-14 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c2bee49-945d-3be9-897f-cf9bcf723b05 | -12.77609 | -48.01814 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1223eb57-4420-3b8b-84f1-204f25974708 | -11.47111 | -50.76463 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b9642037-1a9a-37b8-8cf9-fa788c059aed | -10.89734 | -48.17488 | 2025-09-14 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cdee663-0d45-37da-927a-efe79641c440 | -10.36074 | -50.48849 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3c8186af-5eba-3dea-8cb7-ad6646477ee1 | -12.73922 | -48.02085 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 25e0b87e-8de4-3057-be62-fd5cf92d1b2d | -10.60071 | -44.33099 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9056def-e794-308f-a9b8-95ec6e0a722f | -11.45901 | -50.77703 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f474896-bff2-30cf-b6af-792af786e2d8 | -11.66949 | -46.50711 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd7cf50c-9532-3507-a376-5ab21a4c7308 | -11.46892 | -50.77862 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e7c4a40-641e-3926-91c9-cf213e29beea | -10.92556 | -47.19277 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 023e4b22-c0d9-32f6-8e0e-ad40de182642 | -8.95085 | -46.04706 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9590f10a-3ca7-3c2c-b771-a5db09e4b70b | -8.14549 | -43.66582 | 2025-09-14 04:40:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a67ebc83-1942-328e-b957-be55b6e68af3 | -12.56858 | -45.65482 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 733b6db5-a232-30c2-8e99-09f96b26674c | -10.75839 | -44.78186 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83d3db0b-15b8-3aab-899c-9b5bb92a03f6 | -7.86436 | -49.98587 | 2025-09-14 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59146538-1c5e-3b36-99a8-99a7e4c00789 | -11.46119 | -50.74152 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a61e9d3-d0b8-3ab5-a6af-785589778f12 | -10.75785 | -44.78569 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2819cc58-4e3b-39d8-8c47-32b53454ab9d | -11.45242 | -50.79748 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3416bb4a-91a1-38cd-9332-e7151f0f8e63 | -10.93156 | -47.35518 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4535b76-afdd-30da-83c2-1901cc2b9468 | -12.13449 | -47.59917 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d12ffab-e685-376a-b22c-109cde622255 | -10.32455 | -48.81974 | 2025-09-14 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87561e38-2e72-3986-8260-a9977e2f8771 | -11.43449 | -50.47495 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c782d9f-bbbe-368f-a113-4afb86f935cc | -12.7862 | -48.02393 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01d07fc3-0ee7-30e2-bf2c-2e6f00a9eda8 | -12.69913 | -48.29873 | 2025-09-14 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README31.md)
