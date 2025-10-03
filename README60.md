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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f015240-912a-3452-a00b-567e5752aa07 | -13.29505 | -46.98381 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da284e5f-d7c6-3160-a6d4-d9adf52665e8 | -12.7592 | -50.55051 | 2025-10-03 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25617526-a8ff-3ca7-9b6e-8729e5a418aa | -12.67839 | -46.85665 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b8c84b8-a389-38b7-a3e7-6a1a3c8a1aa6 | -14.20271 | -46.05395 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1481ca36-d34d-386d-a5ef-11315d442aae | -11.55503 | -47.66201 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 44c661a4-0a8b-37ae-84d3-d1a024db8223 | -11.91441 | -46.28448 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ad5cf76d-a070-30a3-8d7e-c2ad1ecf730e | -11.80861 | -45.01416 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2158176-000e-38cb-bfac-1a000632bd53 | -12.67917 | -46.85221 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c386cb0-0844-37fb-babb-90a35f8eb463 | -14.09929 | -44.3074 | 2025-10-03 04:12:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37c60f5b-4443-31d1-a188-c8b4d407c85d | -12.24964 | -47.83393 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3aebbd1-d000-3c84-872a-bfc128d43f0f | -10.28026 | -44.32379 | 2025-10-03 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13e98e02-9d5d-3116-ac05-f607a8f3d463 | -13.54818 | -47.28786 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7358a667-d394-3113-bb08-1dda40c6fb18 | -9.92401 | -43.72037 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d8432e3-33f2-3ef6-8869-f1bdb80133f1 | -14.42068 | -47.14399 | 2025-10-03 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39f4d815-9b17-3c34-8e3b-f518e87ddddf | -12.7217 | -44.8431 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3e77de1-22bb-336e-ad5a-b97a8866fec7 | -11.87927 | -45.01851 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec5e4cf6-6d22-3a8c-931c-1964a532312e | -13.31681 | -47.19172 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5f64939-3f0f-35a6-b35a-41c9ad678a5f | -8.73342 | -47.35209 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 976c450e-9da1-37b6-9686-244e4310ca4d | -13.3273 | -47.59077 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bf78f4d-bc9a-33fe-bc25-1487c455309a | -13.16912 | -47.89402 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6157ff4-5c83-3984-801c-7717aa3b1772 | -12.87586 | -44.63024 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8b40bce-3619-3703-9360-25da54f933fa | -13.93768 | -48.08979 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6911a69-3eab-310e-ba01-3bd167d2ce6b | -11.79235 | -41.19328 | 2025-10-03 04:12:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3cb4fffd-fa78-3be5-b021-93972a3f6a13 | -10.85667 | -47.22028 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c48768d-a753-39d3-95fb-430442825ee6 | -14.44301 | -46.12348 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cfb3d0a7-86df-309c-b709-9a19642e4440 | -12.35045 | -54.15877 | 2025-10-03 04:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0efca439-9a4b-3028-922f-614192ce7e6a | -9.06656 | -46.64392 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ab45f834-984f-3052-b282-444b36381f08 | -10.85937 | -47.25196 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a825343-d8df-37e9-a99b-65fc28bf82a1 | -11.79482 | -47.93476 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 698df5f9-60cc-323a-a361-fef8821b9bbc | -14.20015 | -46.11281 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5683a15c-3e1a-39bd-89c4-e931944db16e | -12.40004 | -45.01689 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de84b09e-6c47-317a-ad51-c08306cd312a | -13.24682 | -48.50325 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50134d9f-2293-3809-a549-060323dde40d | -13.30684 | -47.59153 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac7d14d9-6e57-3fa6-9320-114c317c6370 | -13.13665 | -47.89306 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cc7b9cde-ad1b-386d-b739-b23f589edd2c | -12.64463 | -46.96169 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 416311e2-3c3e-307e-a635-0e610baa30a1 | -13.96373 | -48.11705 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bced4dfa-721e-3e76-ac35-50dbe9f37b1f | -13.68274 | -48.63007 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35a3311e-c48c-33c6-875b-44f9fbbffbf0 | -13.33417 | -47.20412 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5788884c-422f-394c-adc2-1bdd347397d9 | -13.15628 | -47.82928 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99a09269-cd55-338f-8f26-331d1a7c3e14 | -11.07097 | -48.35955 | 2025-10-03 04:12:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7156554d-f61a-3d76-89fd-f81e9604f5d2 | -9.06962 | -46.64948 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 55e99483-ea4b-3962-9cf0-889111e6741c | -14.14098 | -47.05687 | 2025-10-03 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a815f53a-80f3-3258-a212-76957de3bc4f | -14.43311 | -46.11746 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cd8d743-d733-3755-9a13-489c3daa5c75 | -13.33719 | -48.12052 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d055ef49-fc72-3458-841e-f7ca2580d5cc | -10.34126 | -43.73558 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15c2fc7d-323b-355c-a25c-c2d12309f866 | -9.91372 | -43.74112 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d4953e2e-b5fc-3f0d-a680-57c6bf32f775 | -11.05676 | -47.80008 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76971f0f-54b5-367e-85f3-f80b1a3ce264 | -12.22322 | -43.76994 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2252bf44-72c9-3e99-91fa-4d59d3833446 | -12.63255 | -46.96419 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b72462d-69f2-3a1e-996c-47d35dcce6c4 | -13.13572 | -47.89821 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 458d7427-1ace-3285-a4d8-78d5f8baf786 | -13.77308 | -48.06285 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67d5c6bc-1cc2-34aa-920b-c949adce267d | -9.57398 | -48.44625 | 2025-10-03 04:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 648eff00-852a-3a1b-ba18-f64283a7f459 | -14.30734 | -45.88062 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f22b24fd-aa32-33ee-b523-9cc9b3da3249 | -10.27964 | -44.32755 | 2025-10-03 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 145bb34a-ed54-3864-9c9b-281051ef970c | -11.8696 | -48.00769 | 2025-10-03 04:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ea82f46-fc67-3723-b737-8c789718909d | -14.23163 | -46.11294 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 522c3523-07cc-3b7b-9511-394acbb9f36c | -13.57343 | -47.27742 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fba573f-48a2-3368-bfca-2ace99e93897 | -13.32446 | -47.60676 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd032de0-95d8-3305-88b3-a6ca69ff49ca | -11.62781 | -47.98351 | 2025-10-03 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 825fd300-d389-35af-8fd7-c17a44fc7dbd | -13.77504 | -47.57874 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6f3b7044-bc30-3197-9012-5af80512bdca | -12.84082 | -46.94519 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d36d416c-9ce4-3d29-ba58-2ccf4b4b3d32 | -11.85359 | -44.95807 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1cc73948-7d8c-3a7e-a62b-57a5d2e9bdca | -12.60538 | -49.89959 | 2025-10-03 04:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17706400-7892-3bbc-ab5b-b7b0c55ede93 | -14.46839 | -48.41055 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9afa9247-3348-3d8e-b6c9-1912cd81a395 | -12.37967 | -46.51966 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17098b47-a548-351d-8631-e107c9008782 | -13.14762 | -47.83226 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61c7c935-60cd-325c-b79f-38d045130ec2 | -13.12435 | -47.87931 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cfffea9-4e2e-3fc1-94b9-a44d5d6ed622 | -14.28776 | -45.88963 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6dd46174-d43f-34f6-9766-6739e0ac447e | -13.7018 | -44.34211 | 2025-10-03 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5755d1c2-a383-322f-851c-2ffbd2beb340 | -8.76059 | -49.92776 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 110a5938-58e1-3f80-a20a-ac4505a098ab | -10.86644 | -46.67904 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a93275b-c6cf-39b1-94f0-bf2c580234f7 | -11.06486 | -47.80166 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b4aef9c-9497-35e4-9b3d-e15cc332eb0d | -13.74653 | -47.94506 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8c47cab-2feb-3fe2-b035-81afc62438c7 | -9.44467 | -47.58692 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d5d2e1d-87af-3396-8d89-4a57801cfe84 | -11.63077 | -45.06044 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf1b20f8-3c66-30b2-bab3-084a80cec8b4 | -11.13734 | -43.39457 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9abb50ea-0b73-3ee3-a6b4-aa2c51583ce1 | -14.18984 | -46.68234 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e02db677-40b7-3b07-9f99-b2b81f3c1509 | -13.75163 | -48.07862 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 115b4fac-66a8-3467-85f4-18211f055302 | -14.37869 | -45.9508 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b90da54-9b92-33db-8930-1d6b76e5aeff | -12.67464 | -46.85598 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4240d2a3-3b0e-3ee3-bae3-21d92b8b3072 | -11.81011 | -45.02651 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6adbf73-52f1-3b8b-a794-ff35a2cca78f | -11.47582 | -44.96849 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abcd12f6-c0d1-32b9-a9da-9467dbe7e09f | -13.28963 | -46.9899 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30c2fa8c-f312-3c40-8f33-8072257be26e | -13.33556 | -47.21865 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 92df6339-71f5-3e59-9a83-3a15481cbb43 | -12.81369 | -47.01262 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fa5ee0f-9d89-3717-953e-dad8f47ea3ad | -9.95355 | -43.67324 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98ec71ee-8818-3bf5-ad26-ca9e5d5c5e73 | -13.14092 | -50.0292 | 2025-10-03 04:12:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51265da2-f837-308a-8134-eb82bd4ac9b6 | -13.75739 | -48.08171 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b832fb43-df78-31bf-8553-4b117229b3a0 | -14.59765 | -46.72327 | 2025-10-03 04:12:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7b7fae8-e45b-3b3a-9ed5-43a33cbf1e92 | -8.76244 | -49.92914 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d5ef367-8cf4-3956-aab3-e467762a0ca4 | -13.74157 | -47.99633 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6aa847a-94c2-3b6a-82a7-c0c8814c8b08 | -13.68197 | -48.03354 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3b236ca1-26a8-39e0-ba49-2e9815dfc6fd | -12.69162 | -48.54515 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3cc7806-326d-3de4-a695-81eb24550268 | -14.68921 | -45.18512 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b336ac3f-4556-31de-ac57-0cf6dfa2976a | -13.22696 | -47.35606 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0fbc1da-e0e5-3aa0-ba6e-d4d848256a47 | -15.26317 | -44.12513 | 2025-10-03 04:12:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9fd0e211-fd86-3156-968a-08a62d477bc0 | -12.63513 | -46.99469 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22a43d29-6f64-3ee2-955a-b353b0b3a458 | -9.95414 | -43.66962 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1960ccd-2e0d-381e-88d3-5d0809045e63 | -11.63188 | -47.98422 | 2025-10-03 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13a2a261-a8c9-3d44-88fb-de84af16110b | -13.27777 | -47.25835 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README61.md)
