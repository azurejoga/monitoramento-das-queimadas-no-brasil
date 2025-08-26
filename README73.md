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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdbc8309-0b61-3094-9c52-21b4a06aa884 | -16.23027 | -58.73004 | 2025-08-26 04:49:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 70c03925-430c-389d-8202-63957b9f6896 | -20.88302 | -49.02808 | 2025-08-26 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b72d4b65-3a08-31a6-b72f-7453b7889d6c | -16.23769 | -58.71222 | 2025-08-26 04:49:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d3f9d5f6-1119-3128-b2c4-7734c56352e5 | -21.38597 | -45.49628 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 59fb19bd-5289-34b2-88ce-064a64b5c874 | -18.14016 | -44.42422 | 2025-08-26 04:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 786f3f42-3f09-3858-9afd-710e7ae54f5b | -19.48774 | -46.12355 | 2025-08-26 04:49:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87389ab4-1a69-357a-ae07-ebaec27f3895 | -15.63261 | -52.72297 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a195e0b-2b89-3224-a775-aab459e33cb9 | -20.38268 | -42.19913 | 2025-08-26 04:49:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 88c8137d-cc3b-382c-8360-e202ca4f9e6a | -18.71747 | -41.27575 | 2025-08-26 04:49:00 | NOAA-20 | CENTRAL DE MINAS | MINAS GERAIS | Brasil | 3115706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e2f170a5-f99b-36bb-8fc2-0ac881b31f1f | -14.7571 | -59.71805 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f53942c1-fa36-36be-8cab-1049b897fad2 | -19.92421 | -44.6238 | 2025-08-26 04:49:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dff18151-98c2-3e08-b09e-36887bfd1578 | -15.62985 | -52.71883 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc7d8efe-5b06-31fb-975f-4cf7f61cd2d6 | -19.03451 | -46.91708 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e406463-4a0d-335e-ba4e-faa8c5d5db3d | -16.10842 | -52.05085 | 2025-08-26 04:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 529f80e2-2ac0-380c-be7d-2cdf4fe042b4 | -15.62269 | -52.69921 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3835f71a-d00e-377b-8b6d-4539a807aba0 | -21.6141 | -49.69689 | 2025-08-26 04:49:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 20bee5d6-70c3-3cf5-9607-bb57450efdae | -18.85168 | -47.00523 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e04134e5-e8fc-30ab-8df9-9e8e0985ebdf | -15.62653 | -52.71828 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0153305-997c-3d67-9ef6-76ed342465f0 | -14.28679 | -60.36576 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a29c90a1-898f-3d9a-ac3c-f0b4e7646b3e | -16.74464 | -47.59888 | 2025-08-26 04:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c68876ab-d292-39e7-8478-543ea6a664b3 | -20.37617 | -42.20125 | 2025-08-26 04:49:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0e66aaa5-8d41-316c-8420-34aba32dd8ea | -16.2431 | -58.72872 | 2025-08-26 04:49:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 170a0cea-e7be-33b8-8eb1-d14e0d8bbe14 | -19.17557 | -48.73271 | 2025-08-26 04:49:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b71fc1b-2051-3159-8770-75f7a072422e | -20.3785 | -42.20007 | 2025-08-26 04:49:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 371dbcb8-bb8b-39f8-9789-81401d75fafd | -18.49344 | -40.33495 | 2025-08-26 04:49:00 | NOAA-20 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 99ebfbcf-6d05-33c4-a8a0-c9e7a3bcf2ca | -16.80413 | -51.9124 | 2025-08-26 04:49:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e42815f-f5b4-3ea6-887f-95f86fd977c2 | -20.38241 | -42.20229 | 2025-08-26 04:49:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2163151e-92fc-3517-a693-bb362f7e5828 | -18.85065 | -47.01391 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6079d6cf-27de-376c-8a57-e4eca31bf0cd | -16.80752 | -51.91295 | 2025-08-26 04:49:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9bdec1b-821f-35ba-b054-a263cf56e3c0 | -15.63869 | -52.72766 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92c290d9-cce7-30fa-857b-3e4969e0afbc | -14.63261 | -59.55615 | 2025-08-26 04:49:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87f0749e-4d84-3d55-a12d-63f53d4ec633 | -15.61825 | -52.70586 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15010166-faf5-37b2-8f93-d3cc5a1494ee | -20.04542 | -44.46821 | 2025-08-26 04:49:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8e8669aa-f0bc-30d3-8e30-8d5d24067dea | -18.80712 | -47.59495 | 2025-08-26 04:49:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2d2a3f3-4088-3db8-87a1-b7ae8828acb7 | -17.78314 | -44.48783 | 2025-08-26 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd06df4a-a926-35e4-8c3f-6fbb66652739 | -20.87797 | -49.03525 | 2025-08-26 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2055d71f-cd82-3108-8b19-186dac48b572 | -20.88351 | -49.02421 | 2025-08-26 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bad744c6-3e6a-3e1e-83ae-09c4f2d5bf15 | -16.74411 | -47.60303 | 2025-08-26 04:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edbf2cd4-6aa0-37d4-9e56-7903cf19c649 | -21.19707 | -48.92805 | 2025-08-26 04:49:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 6a7cf511-eefd-3b4a-8b97-eb1926bfc582 | -16.7827 | -47.57059 | 2025-08-26 04:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cfa1a25-301c-3603-afd2-259ad0da4f07 | -16.40545 | -49.48031 | 2025-08-26 04:49:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b7b00df-d5b0-3fc3-a17c-9199b410f74a | -17.35206 | -47.85779 | 2025-08-26 04:49:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f17ff78-855c-358f-84e7-6ec83c44e7a5 | -18.71698 | -41.2812 | 2025-08-26 04:49:00 | NOAA-20 | CENTRAL DE MINAS | MINAS GERAIS | Brasil | 3115706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 856a7503-58e8-3658-ad9b-cd6ad415c939 | -17.68293 | -46.3121 | 2025-08-26 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 86b7ccfa-b8e9-3cce-b19d-2469783eb220 | -18.86637 | -46.99757 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81731049-fa59-3618-bbe5-164d33d9ac0b | -14.76313 | -59.71026 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d41eeb2-9851-3ed9-bb5c-dea80b1a55bf | -20.37645 | -42.19803 | 2025-08-26 04:49:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5092e94f-b060-3832-a67a-dfff5128a0f7 | -21.61342 | -49.7023 | 2025-08-26 04:49:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 57bf5ab3-abeb-3127-9295-57ba475622b0 | -21.42591 | -45.47835 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e4d74622-9344-3076-a1c7-7e1ef0d2840f | -15.62929 | -52.72243 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36b7192d-e352-36a0-af9e-19b0dac2b4f4 | -17.79286 | -44.49636 | 2025-08-26 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e3feb9c-e9ea-3565-bd9c-6b046cdc6f16 | -14.29153 | -60.36625 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b793f3fc-b419-329d-b157-95987a255470 | -20.20475 | -47.01236 | 2025-08-26 04:49:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc7625f0-cdbb-31b4-b96a-15153c7dcc8c | -15.64508 | -52.72881 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| feed1084-7f19-39c4-b8cd-1f668b1a70d4 | -16.80864 | -51.90549 | 2025-08-26 04:49:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 755e5b31-18eb-3c89-9205-bf485e1bb5e1 | -15.64784 | -52.73294 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9f44320-e46a-3c0e-a0b1-b4e995583c81 | -16.74041 | -47.59836 | 2025-08-26 04:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e5e170d-1f16-3a43-8e45-9b33d3aec3fb | -18.14487 | -44.43059 | 2025-08-26 04:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 140d36f7-00f7-3fc9-87b4-8601af1d4ab0 | -17.60448 | -46.69026 | 2025-08-26 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8bcb6fa0-a823-3eac-9f19-0b87fdfecdbb | -21.08959 | -40.93827 | 2025-08-26 04:49:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 57f38c89-0975-32a2-af8b-4743dac2f15f | -18.8109 | -47.60001 | 2025-08-26 04:49:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 948b75ea-980a-3b72-a6a2-6111e7607723 | -21.43083 | -45.48144 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 38a94005-0f8f-3101-be2e-a98152868150 | -21.64285 | -49.75554 | 2025-08-26 04:49:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9531a728-7a9b-3cb6-8f35-1fbc9e6d3d51 | -17.78377 | -44.48214 | 2025-08-26 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2baf128a-c35c-3214-870e-45c48a4766b6 | -20.18952 | -44.58191 | 2025-08-26 04:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2ca8c31a-431f-3bb3-bd8c-4224ac7cb424 | -17.56607 | -49.75776 | 2025-08-26 04:49:00 | NOAA-20 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd279f88-6e00-3e5f-81d5-d2789c3642fc | -14.28769 | -60.36102 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0278bd6f-9d72-3d21-9148-1cbf2d09fe93 | -19.92112 | -44.62299 | 2025-08-26 04:49:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 483a4773-2647-3e4f-8a2b-3187b3f944f9 | -20.04937 | -44.46737 | 2025-08-26 04:49:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 11c339db-25c7-31e9-9949-19f72381e0f5 | -18.85117 | -47.00953 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9793bbf-01e2-3ca2-9f2a-3e49affc26ca | -21.42935 | -45.48142 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c68c1bfa-7ffc-38bb-b82f-20177f88e9ee | -19.82823 | -45.89391 | 2025-08-26 04:49:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb50cd01-a7cf-3f2e-bcda-bc49572e0f72 | -18.87036 | -47.00257 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| be1207d4-6090-326c-aac3-6d375ed15ed4 | -20.37914 | -42.19306 | 2025-08-26 04:49:00 | NOAA-20 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d8a5ea3c-543b-3bd9-9c27-e5f8292b6624 | -15.65172 | -52.72989 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db08ca0e-433e-3655-ae6d-8141d91ab592 | -14.29416 | -60.35229 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3358877e-3b2f-3c06-98b9-b939a7ffe08f | -18.14455 | -44.43355 | 2025-08-26 04:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2671f58a-ee21-3bd9-8970-1b41cb9de3d5 | -15.62709 | -52.71468 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45a6c634-86c4-3e14-8772-1f656dd04f23 | -20.37878 | -42.19696 | 2025-08-26 04:49:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 116ab1d5-e31b-315e-8696-4f78dcdc7c61 | -21.61014 | -49.69632 | 2025-08-26 04:49:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 5d34a3ea-9e1e-3e12-8735-2ecdb9c121b7 | -15.63537 | -52.72712 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7622fe15-5f12-3086-86a2-e4542d49b426 | -17.68698 | -46.31776 | 2025-08-26 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 61365f93-0a06-3d42-a421-1322f92c2bb8 | -20.87846 | -49.0314 | 2025-08-26 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 10bbfe7f-8f94-3ec2-b536-bb8f41204380 | -20.18989 | -44.57826 | 2025-08-26 04:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f28e7723-d384-3b7d-982f-aedb37096626 | -21.09638 | -40.93886 | 2025-08-26 04:49:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1dc30c64-21dd-3ae8-bd59-b1f60f3736a8 | -14.2924 | -60.36163 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53d107a5-fc1c-3221-8dfd-bc7a38c1bf1f | -18.34771 | -44.96426 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d054388-fcff-32b5-9c2d-b444def77601 | -14.30097 | -60.36747 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16d053fe-4dd2-3369-83e9-996ba8e2aba9 | -17.76139 | -48.63293 | 2025-08-26 04:49:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2729e4e1-0231-3400-a10b-f60be3afe511 | -18.80658 | -47.59928 | 2025-08-26 04:49:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4df14797-ddd9-318c-ba50-2bbe28b501df | -18.34806 | -44.96107 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86631634-22c7-39f6-9c83-a954db7650e6 | -18.24253 | -51.26352 | 2025-08-26 04:49:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9434fbc0-9ef0-39e0-a3c5-e96d988a7dc2 | -17.68759 | -46.31272 | 2025-08-26 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e5d07353-9ef6-3155-8f31-76ad5037ab83 | -16.80018 | -51.9156 | 2025-08-26 04:49:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d47b43af-372a-3a48-96c3-a13eb5ac6273 | -14.28858 | -60.35629 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 177a39cf-c049-37b9-ab8c-b5e634017498 | -20.37676 | -42.19441 | 2025-08-26 04:49:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 7e5bf56a-7275-3add-b0a9-01aaf7f40738 | -14.29328 | -60.35701 | 2025-08-26 04:49:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7e11d96-dac6-3e0f-bef9-4998588bb702 | -20.38473 | -42.20114 | 2025-08-26 04:49:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 53760454-eecb-3fbd-b70a-1a58c6754ada | -21.4256 | -45.48146 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9ea2867f-ea86-3232-8ed5-4df3f886c4b6 | -18.98615 | -47.08154 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README74.md)
