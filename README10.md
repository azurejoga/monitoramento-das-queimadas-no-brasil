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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66973207-4134-3deb-9fce-ebbdebd392b2 | -7.47526 | -45.58924 | 2025-06-24 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46579774-5e5b-3df8-b03f-f15429eec223 | -11.24812 | -49.4921 | 2025-06-24 04:04:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe31673c-3930-3a6c-9a97-8f49adcac7f0 | -8.05834 | -43.11153 | 2025-06-24 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 55fdc429-8028-3bff-81ea-c1c0d2e88fbf | -8.97556 | -49.87071 | 2025-06-24 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b307d81-5e48-381d-bad7-08b6a31cca3a | -14.79612 | -40.14495 | 2025-06-24 04:04:00 | NPP-375D | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 346a0aa0-1b26-3409-8d7c-ba1ec81b7b79 | -12.89702 | -43.79199 | 2025-06-24 04:04:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b6d4197-608a-39fb-b27d-400ef80fb7e0 | -11.93809 | -48.42654 | 2025-06-24 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 077f6fae-241a-3a5d-b962-504bc11b4190 | -12.49088 | -40.81446 | 2025-06-24 04:04:00 | NPP-375D | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 604c0072-7cb4-339e-8e13-268af3c226aa | -8.57657 | -51.58236 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8538d861-d47f-3311-a81b-c8676462f3ac | -10.23264 | -47.45966 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5317115f-f1b1-3d28-9e43-d95b588f7c87 | -8.56824 | -51.55308 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b31e31dc-0406-3706-bfbb-6d1d702e0c38 | -8.57826 | -51.57349 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5f89385d-e438-3ce4-8f3b-304399e07bd1 | -10.86901 | -49.54518 | 2025-06-24 04:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e3a8b0a-13d0-30dd-9803-70a12b963c03 | -10.23901 | -44.63317 | 2025-06-24 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 688c6ec0-bacc-3957-a3f4-56a2059aad72 | -12.75471 | -44.41003 | 2025-06-24 04:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| cd124bcd-da6c-3f03-83ba-81de649b72f9 | -8.97674 | -49.87392 | 2025-06-24 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d771e4d-38ee-3e5e-bf43-00bb639a645e | -9.64609 | -48.56438 | 2025-06-24 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 993f4acd-c576-34ae-bd58-4555ff321c8c | -8.56189 | -51.56113 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d61be563-b7ea-310f-a542-080a4287e906 | -8.37376 | -47.43157 | 2025-06-24 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 879afc08-f97a-345e-a4d1-db89d69de399 | -12.27038 | -41.52934 | 2025-06-24 04:04:00 | NPP-375D | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0419454e-6e1b-3b52-b08b-648a57cc1b9e | -13.25973 | -41.3242 | 2025-06-24 04:04:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0ffaba89-a7eb-35a8-8930-9477fbaad24a | -14.44112 | -43.75706 | 2025-06-24 04:04:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea5888a0-599d-38b3-9c8e-becf03580e18 | -13.54429 | -42.49234 | 2025-06-24 04:04:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1e0bcadb-a12e-367c-8be6-79815cb65a5e | -14.89445 | -40.89712 | 2025-06-24 04:04:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2adb6dba-a75a-3998-aabb-de31ce55244c | -13.73775 | -47.74872 | 2025-06-24 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20f6712f-844b-3f93-975a-4ad93160e9b2 | -8.56141 | -51.55637 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c30e78f7-613d-3789-84da-f950fa82e961 | -12.40462 | -43.80008 | 2025-06-24 04:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b06c6c13-b2f0-3c1b-882c-d756eb2a4b77 | -8.99347 | -49.87355 | 2025-06-24 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8c3ea2a6-271f-3f6a-a492-cd4418602ffd | -9.40426 | -40.31542 | 2025-06-24 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 03904af7-6ee5-32d8-bf41-35edeb5b68e8 | -16.39419 | -41.16829 | 2025-06-24 04:06:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 084ae4ec-f187-3cc6-b6df-5c0229a834e3 | -15.71032 | -47.5645 | 2025-06-24 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ed10953-e1d8-380e-af12-ba773292f196 | -16.58181 | -43.6488 | 2025-06-24 04:06:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dda9f08e-6919-32c7-96fe-9d5cae380081 | -19.83843 | -40.08238 | 2025-06-24 04:06:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 504332e9-f875-338a-9d71-74642c34f82e | -18.61259 | -44.26646 | 2025-06-24 04:06:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 67ed1a76-c359-3165-accd-109fd351e252 | -17.78183 | -42.80992 | 2025-06-24 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd269e68-8131-3763-afd8-a1c079fa0737 | -17.75471 | -42.89466 | 2025-06-24 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ede49050-c695-31cd-a9fe-5ffb0e6613c1 | -16.60518 | -43.33039 | 2025-06-24 04:06:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64c6bb93-0d6e-378e-9160-659e7a0a9dd1 | -18.03819 | -44.20786 | 2025-06-24 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 254d1f61-a6d7-3be7-9305-a80d8a477af7 | -20.50007 | -45.58463 | 2025-06-24 04:06:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54ee996c-de82-3fa2-891d-7acfa9edd50c | -19.45498 | -45.3086 | 2025-06-24 04:06:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90301857-ac33-3a8f-bae3-343431d61851 | -16.32797 | -43.61754 | 2025-06-24 04:06:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9043a0e-53d5-36b0-96e8-ae4dc79500b0 | -18.61321 | -44.26267 | 2025-06-24 04:06:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 75d70bbf-a919-3d0f-a7a3-307c05a3115f | -14.72698 | -48.41028 | 2025-06-24 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c72fb87e-4b25-3d2e-94a3-6c16612405a7 | -19.83424 | -40.11245 | 2025-06-24 04:06:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1edeab4e-900f-3c86-8f5b-16fb5be07dd9 | -21.67657 | -42.05495 | 2025-06-24 04:06:00 | NPP-375D | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bb15f74d-17ea-35b0-ad96-137b801bd189 | -20.50354 | -45.5853 | 2025-06-24 04:06:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb118cb3-0d00-310f-a317-3aaa292c1bf5 | -21.19414 | -44.93689 | 2025-06-24 04:06:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 747d2004-0dc2-347c-9c9f-a1bf65bcf4a5 | -17.04658 | -43.77526 | 2025-06-24 04:06:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3513134d-077d-32b9-8592-544899dfe18f | -16.46457 | -45.00826 | 2025-06-24 04:06:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52066ed3-22b0-33e5-acb8-5409dec6d348 | -17.75138 | -42.89409 | 2025-06-24 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27513ac9-954b-3e62-baec-7257289ef1f6 | -17.20237 | -46.07884 | 2025-06-24 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0308c763-47f0-3128-a094-9a293ba5921d | -19.436 | -44.34141 | 2025-06-24 04:06:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd3e6cf2-8aa5-3765-af21-b319a747aa7b | -17.04719 | -43.77155 | 2025-06-24 04:06:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7a26fcd-9b88-37ac-889e-f37d02bfec78 | -15.94615 | -42.00983 | 2025-06-24 04:06:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66395544-5774-3a71-af1c-98536d0d1926 | -21.40337 | -44.91985 | 2025-06-24 04:06:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dfb7c259-52b6-38b1-8cc0-cf2a6d0e430e | -20.31164 | -45.5846 | 2025-06-24 04:06:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c198a747-ea19-352d-8480-f9b096f9eb66 | -19.33963 | -42.16093 | 2025-06-24 04:06:00 | NPP-375D | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 34df559a-3cec-37c1-b350-3d1ed51b0fb7 | -18.04018 | -39.92636 | 2025-06-24 04:06:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 91743c1c-2872-3349-be47-d340ad83ee9e | -16.43192 | -44.52206 | 2025-06-24 04:06:00 | NPP-375D | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45661066-1888-34c6-b153-be48e63f4d7d | -17.33843 | -42.66029 | 2025-06-24 04:06:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f062f8c2-7439-3162-aa15-d599101f8213 | -18.38006 | -44.50653 | 2025-06-24 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e553469f-0ff6-33d3-9145-8a3d6ef797af | -17.594 | -43.19956 | 2025-06-24 04:06:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea2b1fe2-38b0-352c-83e0-302d4d55dd8a | -19.82435 | -42.13437 | 2025-06-24 04:06:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 67821164-b276-30e8-a531-8d7f1fb6d9ec | -19.84897 | -43.84558 | 2025-06-24 04:06:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5f840078-d05d-33a7-9f1c-0ca5c6b88928 | -16.68253 | -43.88609 | 2025-06-24 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82cb47e1-20a2-3846-ab3d-0a85f5bd88ff | -17.33786 | -42.66391 | 2025-06-24 04:06:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe4bc490-fb7a-3674-b033-1dfa73a04a56 | -19.64056 | -45.1901 | 2025-06-24 04:06:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b232f0d6-e06e-3791-bcaf-ca50143a8ee8 | -19.41055 | -45.14087 | 2025-06-24 04:06:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4a15720-f6bc-363d-9ac8-2b272e936c8a | -16.60459 | -43.33404 | 2025-06-24 04:06:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b19ba7c-8359-3cfd-946a-7da88a76ee5a | -20.37723 | -45.60381 | 2025-06-24 04:06:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5e9a85b8-38c5-3889-9bcc-1512def2542f | -17.34175 | -42.66086 | 2025-06-24 04:06:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7c40cd0-3b6e-3b4e-98ac-eb564293f57d | -16.32736 | -43.62125 | 2025-06-24 04:06:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6345bf0a-24ca-3ab2-aebe-d19ab95c809e | -16.48444 | -39.47692 | 2025-06-24 04:06:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e5fc7ec0-d25d-34d6-81b5-0f47e057f5ef | -17.21536 | -44.80222 | 2025-06-24 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 12ef303c-10b7-303b-8470-b83dde542126 | -17.34233 | -42.65725 | 2025-06-24 04:06:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2857a39-39ba-3fbe-a0cc-5a5390572340 | -16.5858 | -43.64568 | 2025-06-24 04:06:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d53daac-8e93-39b6-aecf-02c565c888ff | -19.41123 | -45.13689 | 2025-06-24 04:06:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95641710-ed68-3d21-98f6-0d3928b540fb | -16.43471 | -44.52663 | 2025-06-24 04:06:00 | NPP-375D | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47550552-9f70-3f91-8422-80e0803b9dee | -20.16138 | -44.75383 | 2025-06-24 04:06:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 51ddf1b7-d926-3d23-8ebb-ac354b7d050d | -16.58243 | -43.64509 | 2025-06-24 04:06:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76d8a90f-fdc6-390b-ba92-459d20a99a0c | -14.73055 | -48.41564 | 2025-06-24 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94553616-f811-340f-9735-58fd9cde0845 | -16.32399 | -43.62067 | 2025-06-24 04:06:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83b40011-0d70-307f-acd1-9e18487ab001 | -19.5132 | -44.27747 | 2025-06-24 04:06:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 833bcd3d-2213-30d5-9a0d-34f996c1b26f | -16.67914 | -43.8855 | 2025-06-24 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4fb72e6-b505-3c4c-ba2e-258afd5e8f9a | -22.67529 | -42.8569 | 2025-06-24 04:08:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b1ef0945-6d2f-3bdf-9dd2-5e699877eb2f | -25.19049 | -49.32899 | 2025-06-24 04:08:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f0fd67c1-31d7-30f5-88af-b87b77c43599 | -22.67587 | -42.85309 | 2025-06-24 04:08:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dfcb4c1c-33d8-3d9e-84bc-1e787331f09f | -22.85532 | -42.9809 | 2025-06-24 04:08:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9ae6a59d-fb0c-3a0c-b90c-7e3621a76132 | -22.57825 | -44.73448 | 2025-06-24 04:08:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bd84d23f-4586-3973-a19d-a6d88653f1c1 | -8.5724 | -51.5552 | 2025-06-24 04:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7d247489-cd2a-3283-8e99-77bbf967ca75 | -4.543 | -47.9934 | 2025-06-24 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 8b293470-d36e-3c5e-980a-c547a3416140 | -4.5429 | -48.0151 | 2025-06-24 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 280a1c2d-7242-32f8-a1f7-cc99a0b6afdc | -8.5537 | -51.5567 | 2025-06-24 04:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bac8ecf7-4cb2-38b9-b182-c8eafe650b92 | -8.5722 | -51.5761 | 2025-06-24 04:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 4a40a46c-2a73-31e9-9ed3-15eb3ace80d1 | -8.5724 | -51.5552 | 2025-06-24 04:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 976c4ada-97a4-356d-95ab-41566c13faef | -8.5722 | -51.5761 | 2025-06-24 04:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| f70e087e-d5f2-32c9-a36a-e43a60a2d97f | -8.5537 | -51.5567 | 2025-06-24 04:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b005270c-d62c-3942-9f5d-1ea46be358fa | -4.5429 | -48.0151 | 2025-06-24 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| df835d0a-9a19-3cc3-aa25-ce3bd87a167f | -8.0703 | -43.0981 | 2025-06-24 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 5bb7b3af-0c1b-3605-bc28-bc0422c1c32a | -5.14114 | -43.73206 | 2025-06-24 04:23:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README11.md)
