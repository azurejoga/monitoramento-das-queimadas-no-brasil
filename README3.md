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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a31b59a-4b91-319d-a51e-e2734f567ae7 | -16.68072 | -43.88382 | 2025-05-18 03:57:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f9783dc-4ae9-331d-b04a-a05928887ce8 | -11.143 | -47.69568 | 2025-05-18 03:57:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac82d6a9-03ff-31b6-b420-d19931c63f67 | -13.551 | -43.49684 | 2025-05-18 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a4544c9-6d1a-36ca-8478-d4d4fe871437 | -12.10383 | -44.75241 | 2025-05-18 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 474ef6e5-11a1-38bc-9d49-886be733bce3 | -18.03903 | -39.92677 | 2025-05-18 03:57:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 907af98b-a019-3d40-91d7-690762b53da4 | -11.58253 | -47.62217 | 2025-05-18 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c8a8b48-4040-3cd0-81d7-acd6c4611494 | -13.5859 | -47.36763 | 2025-05-18 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d1b1935-5792-3eab-ac25-c97cfca419f8 | -12.10321 | -44.75599 | 2025-05-18 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 842c2545-ed56-3e86-8074-05f885926ffd | -13.29837 | -45.37403 | 2025-05-18 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfd384a3-a58f-320c-ade3-2a4ed053623c | -10.47164 | -49.14903 | 2025-05-18 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0be1cd52-1468-35c1-89e9-0f62699ac8fa | -11.79364 | -49.31776 | 2025-05-18 03:57:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92bee3f9-dc79-31cd-a06b-f6c0101aace7 | -11.48563 | -43.80552 | 2025-05-18 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e69aa93-30e3-3695-af4d-7f787558d850 | -10.34492 | -46.71392 | 2025-05-18 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9b36826-8b5d-3829-96ce-a20738cc537a | -13.65742 | -47.892 | 2025-05-18 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11ddb167-c2a8-3867-877b-87de0c8ed27e | -17.14312 | -44.81168 | 2025-05-18 03:57:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfef8e77-427c-3c74-a18a-f9365649db93 | -17.67814 | -42.74049 | 2025-05-18 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68f7f531-51d3-3d1b-8ea3-b44a6b1686e4 | -10.47791 | -49.14625 | 2025-05-18 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28711974-a5c5-3524-ace7-397f4b708614 | -12.25829 | -44.60529 | 2025-05-18 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cde91263-e1eb-319a-b92f-a9e48ae6f598 | -12.25938 | -44.60689 | 2025-05-18 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2afb86e-e44e-38c7-9356-69c01ffe95a1 | -13.2977 | -45.37784 | 2025-05-18 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6696073-0927-3a23-8803-61d2922d1dba | -13.04296 | -53.71742 | 2025-05-18 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60c7136f-af61-3996-84a7-b6a053f1c524 | -11.5624 | -47.87201 | 2025-05-18 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 222f66b7-3dd5-353c-bb93-4758638da879 | -11.57867 | -47.61554 | 2025-05-18 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 21777d01-d5e7-3519-b9f8-7b91f314dc5d | -12.59401 | -45.44191 | 2025-05-18 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41f37467-3502-3108-9ce5-e20f75d3a247 | -11.5797 | -47.60992 | 2025-05-18 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f90eaa37-aeae-3090-8fb7-13eb841ceeac | -11.5619 | -47.87299 | 2025-05-18 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2316ddc4-c51e-3589-afa0-083e2aaca059 | -12.16458 | -48.80915 | 2025-05-18 03:57:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaa9c887-2e35-393e-a6cd-d575bedcba6b | -13.29426 | -45.37333 | 2025-05-18 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e8feaab-445e-3589-b8f6-e3df0a741502 | -17.38761 | -42.65836 | 2025-05-18 03:57:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f585576b-3e04-3413-a49b-f6622fb97167 | -12.59331 | -45.44579 | 2025-05-18 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 735da8f6-70a8-3830-b1d5-800fb315fe33 | -12.16981 | -48.81031 | 2025-05-18 03:57:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 439e2c45-247a-3c8c-bd9c-8f07eb39f2aa | -11.1431 | -47.69435 | 2025-05-18 03:57:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6abaa25f-4638-3077-915a-b147a4084e3b | -11.57483 | -47.60885 | 2025-05-18 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 020d56fc-9806-3d96-8804-0e53785b37ba | -13.21534 | -43.14492 | 2025-05-18 03:57:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cfce6649-7148-34bc-8aef-3495d579eaa5 | -10.47862 | -49.14253 | 2025-05-18 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 012745fc-178f-3a59-b487-b469e4cb478a | -13.56415 | -43.50824 | 2025-05-18 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 289d0872-e784-380c-a934-16ce190810d1 | -11.79223 | -49.3251 | 2025-05-18 03:57:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 334d64e8-0358-35b2-aaa9-24b586c14d0a | -13.89193 | -43.4501 | 2025-05-18 03:57:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceeb81be-e98a-3f59-8c31-9bfed96a591d | -17.7817 | -42.80962 | 2025-05-18 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00bb45ea-87f2-36ac-8e6b-769c8518284c | -23.40539 | -46.55726 | 2025-05-18 04:00:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7a65339f-3d37-390a-82c4-9f78ea2c846e | -22.0148 | -47.03223 | 2025-05-18 04:00:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72b52431-0812-3fd5-b773-1c6aa44f3f31 | -19.43646 | -44.34155 | 2025-05-18 04:00:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 426832f7-beef-3286-953f-c927c3bca3b7 | -20.95692 | -56.60841 | 2025-05-18 04:00:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7cd85c12-aa7b-3280-881f-156aa4d5ac2d | -20.95516 | -56.61545 | 2025-05-18 04:00:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bd95b62b-3e47-3ba3-87e5-b2a0e3bff882 | -17.67609 | -46.83532 | 2025-05-18 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb7b4560-0438-3c09-8cc5-6ea10485021d | -20.93332 | -44.40519 | 2025-05-18 04:00:00 | NPP-375D | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9550e2f3-a12f-302d-9fa0-16e05f7a4035 | -21.71965 | -42.5866 | 2025-05-18 04:00:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e7e7baad-a8a1-3456-868c-e13a5d829ea7 | -22.78549 | -43.75669 | 2025-05-18 04:00:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2b11a8ce-bcf2-3591-a8ae-505f1e2530e6 | -20.92631 | -44.40385 | 2025-05-18 04:00:00 | NPP-375D | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| defd7404-fb59-3b8b-a7b3-b6a19363ad23 | -17.91783 | -45.53344 | 2025-05-18 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5d5e7df-e75f-3763-b9a9-f2fed0a371f4 | -23.33839 | -46.7737 | 2025-05-18 04:00:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 89b1451a-24af-366d-a62b-8f7da2919f28 | -22.77352 | -47.6239 | 2025-05-18 04:00:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 34f783af-ac24-3092-943d-e27aefffb8a4 | -19.06656 | -53.46061 | 2025-05-18 04:00:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a16bd02-b9ce-3d49-80eb-6344737803e0 | -19.97086 | -44.21748 | 2025-05-18 04:00:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 917abcf0-13e9-34b0-8dcc-131fb8d62370 | -17.66519 | -46.68576 | 2025-05-18 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43053477-b9eb-38a3-a48e-9e251e4f8c66 | -17.01056 | -49.78168 | 2025-05-18 04:00:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13d786c7-d53f-31da-9b74-bb9effb38c42 | -22.90384 | -43.75854 | 2025-05-18 04:00:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e985c39b-61b8-31d1-8905-9b3f4e050b3c | -19.68143 | -45.37824 | 2025-05-18 04:00:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efe21e26-2a95-31b7-b307-974b86b9cdab | -20.94991 | -56.60662 | 2025-05-18 04:00:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5d08eee8-4537-3388-b4c7-633f8e2dda25 | -21.18015 | -43.98026 | 2025-05-18 04:00:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4b83500c-b845-329d-ba26-9af5aadcb6d9 | -20.76457 | -46.76856 | 2025-05-18 04:00:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 75e946a3-29fd-36a3-9c55-e95805007ee9 | -17.04447 | -49.06322 | 2025-05-18 04:00:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 979c174f-0075-3b5d-a40b-92ef371366d9 | -17.58028 | -47.48684 | 2025-05-18 04:00:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e99ddacc-fbe4-3f6f-8e00-c1c9453355bf | -17.40982 | -48.1179 | 2025-05-18 04:00:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55c75759-b9a1-35a0-b261-389e9e91f03f | -21.72674 | -41.27556 | 2025-05-18 04:00:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 8d7dbb88-abfd-33b2-bb40-6c339ce44a6f | -22.90046 | -43.75787 | 2025-05-18 04:00:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cfb944d6-c53a-337e-b911-c5a0e2ddb6cc | -17.00893 | -49.78033 | 2025-05-18 04:00:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adeae60f-9ccb-3ce1-9fd0-34482212c7e3 | -20.94815 | -56.61364 | 2025-05-18 04:00:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| efaac682-97cd-3d53-bf03-b0576d23fd44 | -17.04317 | -49.06202 | 2025-05-18 04:00:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fc41c98-9865-3b06-9f5d-569bbc492c47 | -23.09659 | -45.73017 | 2025-05-18 04:00:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 31023da7-761c-3540-82ab-0ce00070d5a5 | -17.66592 | -46.68186 | 2025-05-18 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01326067-acbf-3c55-a7c0-3cb70f15817f | -22.78041 | -43.04296 | 2025-05-18 04:00:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| da78eca9-1057-39ff-9413-065576ff9761 | -21.73066 | -41.27239 | 2025-05-18 04:00:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 6bb3f1a9-572d-3624-96a5-ff455f8d5473 | -19.85001 | -43.84577 | 2025-05-18 04:00:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 12aa560f-074c-3748-a69f-9ca80a6f5ce7 | -22.77279 | -47.62762 | 2025-05-18 04:00:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| e72286b8-9d60-3a30-98cb-cc9c75291630 | -21.62681 | -43.46844 | 2025-05-18 04:00:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1f0e6d8e-ec1f-3143-bca3-bffe8018fac5 | -20.4166 | -43.55489 | 2025-05-18 04:00:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2577de07-5399-3e24-a484-3e1c97aedc17 | -7.07542 | -44.38657 | 2025-05-18 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8d7a381-51c9-3a68-a298-f22890772f99 | -6.6442 | -41.99737 | 2025-05-18 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d5878a18-c01e-346e-abe1-db46922b213f | -7.08644 | -41.43627 | 2025-05-18 04:17:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 49a481c8-45b9-3758-91f7-7e1517c3d080 | -7.07596 | -44.38308 | 2025-05-18 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95549324-50ca-3780-b4b3-2e52e7cb6b92 | -7.0738 | -44.91478 | 2025-05-18 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56a4fab7-6159-3dc7-8009-cb72ff7446f7 | -7.53754 | -43.37496 | 2025-05-18 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3d6a2aa-c780-3e16-9ab1-c40334d6cf4d | -8.11884 | -46.4523 | 2025-05-18 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66a3e2f5-9361-376f-867f-e1397feaf311 | -7.20864 | -43.0973 | 2025-05-18 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 18b427f9-f624-3fd3-b688-5acfbec30117 | -7.20921 | -43.09363 | 2025-05-18 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf416321-858b-3d35-b033-3efbe7d1765d | -7.53361 | -43.37806 | 2025-05-18 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9df6aca9-8987-3422-ae5f-798699b117a8 | -6.65781 | -43.38102 | 2025-05-18 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 958e7120-e75e-3d9e-b81c-0430bf88f983 | -7.23412 | -44.71681 | 2025-05-18 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01e08343-1d5e-30dc-bc6e-96f3f93a608d | -7.07325 | -44.91824 | 2025-05-18 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd28596e-af05-3251-855d-17fd57e89e52 | -7.55215 | -43.78534 | 2025-05-18 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b295445c-c4df-3744-9d77-bcf898120421 | -7.53699 | -43.3786 | 2025-05-18 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9067d003-352c-31b7-9865-c747e1c3dae7 | -8.00518 | -46.80523 | 2025-05-18 04:17:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42c7d742-d36e-3e35-9527-84059ed5a7a2 | -6.65126 | -41.99843 | 2025-05-18 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2a4ab5f4-e637-3020-8b1b-1b09f712ee3a | -8.11664 | -46.44454 | 2025-05-18 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f71a2063-39b5-37d7-9709-5a31c3c4da19 | -8.11605 | -46.44815 | 2025-05-18 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 420f92ba-30b1-35e4-9e2b-b1655906686a | -8.11547 | -46.45176 | 2025-05-18 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6087ffc8-2c6a-377c-a941-5cca868e322d | -7.54092 | -43.3755 | 2025-05-18 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb7a6522-3935-3d9b-95de-5eb7665c7192 | -6.64479 | -41.99339 | 2025-05-18 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d0f11119-dbcf-3c43-9994-961f79d74258 | -7.37841 | -43.29103 | 2025-05-18 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README4.md)
