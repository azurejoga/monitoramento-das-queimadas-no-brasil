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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6cee814-1cf8-343f-8508-bd02d0611dd5 | -22.4158 | -46.616501 | 2024-10-08 00:57:29 | METOP-C | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5acc4aac-be59-3a8f-8bf1-04c0bc1fa336 | -22.572701 | -47.124199 | 2024-10-08 00:57:29 | METOP-C | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b95699bc-75ed-3033-84aa-0783a7c7361a | -23.8964 | -54.2192 | 2024-10-08 00:57:30 | METOP-C | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3380525a-4ca5-3b1d-987e-e7f13f451037 | -22.650999 | -47.7047 | 2024-10-08 00:57:30 | METOP-C | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 777040be-8065-3671-9206-da60e5632f13 | -22.652599 | -47.712101 | 2024-10-08 00:57:30 | METOP-C | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aeef66ec-e459-3b19-a663-6e0dacc089a6 | -22.805401 | -48.456501 | 2024-10-08 00:57:30 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4ee5503d-e9ca-3bfb-a711-512f2c280dbc | -23.9062 | -54.217201 | 2024-10-08 00:57:30 | METOP-C | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 096debc8-e721-3b26-8523-08f6cfad19c6 | -23.908501 | -54.2304 | 2024-10-08 00:57:30 | METOP-C | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11d44b7d-d488-3ef4-bb5f-47d6bd06ad26 | -23.898701 | -54.232399 | 2024-10-08 00:57:30 | METOP-C | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 12bd38c1-5cc3-3876-9ff5-4b0b02f4f968 | -23.900999 | -54.245499 | 2024-10-08 00:57:30 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ca1c5f54-c341-3b40-b98f-fb917a575a32 | -21.1961 | -42.107201 | 2024-10-08 00:57:31 | METOP-C | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0dd54033-b219-3aad-a2d1-dbb8f8f836c4 | -21.167601 | -42.197701 | 2024-10-08 00:57:32 | METOP-C | LAJE DO MURIAÉ | RIO DE JANEIRO | Brasil | 3302304 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 558f6af2-784b-3a63-ad1e-83f225fa04f0 | -22.475401 | -48.358601 | 2024-10-08 00:57:35 | METOP-C | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 650964b2-3472-379e-9dd7-5a2ddd82520f | -21.822001 | -45.666401 | 2024-10-08 00:57:35 | METOP-C | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1f6227c-10df-328e-b775-80ce5418653c | -21.8239 | -45.674599 | 2024-10-08 00:57:35 | METOP-C | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 76e4e9c6-eaf5-3665-b090-ca36dfd99a08 | -21.000601 | -43.0429 | 2024-10-08 00:57:38 | METOP-C | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c30cff08-a962-391f-9196-f85daf2bc47e | -22.2652 | -48.527802 | 2024-10-08 00:57:39 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cad2a2e9-0793-3d3e-8b9a-271c06a66f40 | -20.6595 | -42.084599 | 2024-10-08 00:57:40 | METOP-C | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 02da06bd-ec06-33db-889e-4cabc47eb795 | -22.128599 | -48.514801 | 2024-10-08 00:57:41 | METOP-C | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1396ad89-9039-3405-a4bf-e45e9dac5627 | -21.855499 | -48.395802 | 2024-10-08 00:57:45 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6566cad6-6735-32ef-85d1-d5785e19a3a3 | -21.8571 | -48.403198 | 2024-10-08 00:57:45 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a26cf57f-506d-3420-a786-5eaa8e37682f | -21.8587 | -48.410599 | 2024-10-08 00:57:45 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 513aebd4-b750-3c0c-a7ab-8964153f037c | -23.235001 | -55.460899 | 2024-10-08 00:57:45 | METOP-C | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92e48fa1-411f-3443-b180-b149f80ede48 | -23.2376 | -55.4762 | 2024-10-08 00:57:45 | METOP-C | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 520a380e-2fdc-3a44-9cb3-dfbfc10a1764 | -21.8473 | -48.405602 | 2024-10-08 00:57:45 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 01a931e6-291d-3a76-9203-0d2da55bd038 | -21.8489 | -48.412998 | 2024-10-08 00:57:45 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fc29885a-91ca-3a1c-bfe6-d5a99583c064 | -22.899 | -53.679199 | 2024-10-08 00:57:45 | METOP-C | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 99d4b454-c30e-3ac7-a362-7b7f77ba2afb | -21.6416 | -47.709801 | 2024-10-08 00:57:46 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 29a731c1-f3e6-38e2-a589-6146af1debf9 | -21.599199 | -47.704899 | 2024-10-08 00:57:47 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cc2b2795-d06a-35bb-b016-912281b001f0 | -21.6008 | -47.712299 | 2024-10-08 00:57:47 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6661f62b-8852-3452-ae53-6feab5773a6d | -21.153999 | -45.818802 | 2024-10-08 00:57:47 | METOP-C | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 134bbd05-384f-39c3-bdc2-b24be6a39c19 | -21.5935 | -47.9562 | 2024-10-08 00:57:48 | METOP-C | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4b854ca5-f653-3482-9d74-3bfa6b0b4bd4 | -20.4009 | -43.918598 | 2024-10-08 00:57:51 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b74785f-bc10-35b4-882c-8bd34945e28a | -20.4035 | -43.928902 | 2024-10-08 00:57:51 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c58822b8-0e5d-355a-bbf1-6bd5f03a16e8 | -20.391199 | -43.921299 | 2024-10-08 00:57:52 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b9eba37-619e-3b44-86c1-eab502868b23 | -20.393801 | -43.931599 | 2024-10-08 00:57:52 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 297cb73d-a2fb-327a-b8b6-28b570fd2a1e | -20.396299 | -43.941898 | 2024-10-08 00:57:52 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b114b312-e819-39af-bca9-e6f70272d8f8 | -20.3815 | -43.924 | 2024-10-08 00:57:52 | METOP-C | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1f09337-a23e-3106-8833-3569b0cb118a | -20.384001 | -43.934299 | 2024-10-08 00:57:52 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1b3a6b51-76ff-3332-b973-f5c35fd0461e | -20.3866 | -43.944599 | 2024-10-08 00:57:52 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 572ac221-549b-394b-b5c1-59e179bcf261 | -20.371799 | -43.9268 | 2024-10-08 00:57:52 | METOP-C | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 261aa1b6-30b5-36ba-9012-b5b5899e90a3 | -20.3743 | -43.937099 | 2024-10-08 00:57:52 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1748c3c3-2783-3f4e-b1f8-9826c6880c0b | -20.3769 | -43.9473 | 2024-10-08 00:57:52 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d518c093-3beb-3142-ac57-dd4745263ebf | -20.379499 | -43.9576 | 2024-10-08 00:57:52 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 918e7edb-7310-3b7f-aa58-e42e44b221ad | -20.362101 | -43.929501 | 2024-10-08 00:57:52 | METOP-C | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36148707-c7a8-3843-abba-af016a91eb65 | -20.364599 | -43.9398 | 2024-10-08 00:57:52 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ceff5b8-33cf-3e39-a194-4cd1e90783a7 | -20.367201 | -43.950001 | 2024-10-08 00:57:52 | METOP-C | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a65835fa-7fdb-351c-88fd-86de62eeff9d | -21.0851 | -47.2118 | 2024-10-08 00:57:53 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b8e647e4-8bfe-3568-b70f-f084a641a53a | -21.0868 | -47.219398 | 2024-10-08 00:57:53 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 177dd809-5717-3cfd-a970-6b5715f7d2b2 | -21.0886 | -47.226898 | 2024-10-08 00:57:53 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c419f32b-9d33-3d67-9486-fb07b2722d51 | -21.0753 | -47.214298 | 2024-10-08 00:57:53 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5099bb26-7d1a-3437-8870-1fedba709d63 | -21.077 | -47.221901 | 2024-10-08 00:57:53 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 567d1f7c-45c1-3738-afe7-f6508d05d9df | -21.065599 | -47.216801 | 2024-10-08 00:57:53 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cb742d24-63b6-3791-920a-64e81c1c1e2e | -21.067301 | -47.2244 | 2024-10-08 00:57:53 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d7c497a3-8437-35b7-bbd6-0389fd75d62e | -21.069099 | -47.231899 | 2024-10-08 00:57:53 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| df2e077d-a89e-39e7-8ada-bf15f5e45908 | -21.070801 | -47.239399 | 2024-10-08 00:57:53 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 458ead91-5b6f-3849-9802-7e2ef9d9c3c1 | -21.0725 | -47.247002 | 2024-10-08 00:57:53 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ea1c59cd-ff38-3da0-bff8-0c0a8b674ae9 | -21.059299 | -47.234402 | 2024-10-08 00:57:54 | METOP-C | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c9dda187-4c83-3c75-b21d-b9c078da2983 | -21.061001 | -47.241901 | 2024-10-08 00:57:54 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5e486c20-752d-33ec-85e5-49974326883f | -20.7624 | -46.353001 | 2024-10-08 00:57:55 | METOP-C | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c5a71813-927b-3bbe-8c57-6e5fdf3eaca3 | -20.764299 | -46.361 | 2024-10-08 00:57:55 | METOP-C | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f3effa0e-7c3c-30e5-9383-69aa478e44c3 | -20.766199 | -46.368999 | 2024-10-08 00:57:55 | METOP-C | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1a023b48-c199-3d0f-a83c-c6a05ef5e2f0 | -20.743299 | -46.315701 | 2024-10-08 00:57:55 | METOP-C | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d696a06-09aa-31ba-8ab6-42128e5f3f6f | -20.1341 | -43.848701 | 2024-10-08 00:57:55 | METOP-C | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39ab27b8-dcba-38fd-8ab3-21ecba155130 | -20.124399 | -43.851398 | 2024-10-08 00:57:56 | METOP-C | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5260487-0a48-3260-aebd-9cbd6fdeeb67 | -20.236 | -44.4245 | 2024-10-08 00:57:56 | METOP-C | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 599369ac-a7dd-3e02-9dfd-ed90d1fa1832 | -20.2384 | -44.4342 | 2024-10-08 00:57:56 | METOP-C | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 51f44827-0445-3654-b91d-3f02fea1ab40 | -20.2262 | -44.4272 | 2024-10-08 00:57:56 | METOP-C | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8ec46c2-089a-3ef0-9d9e-22210a5775ff | -20.2286 | -44.436901 | 2024-10-08 00:57:56 | METOP-C | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c853d4c-44ff-3418-8765-4da130af2d37 | -20.722799 | -46.893902 | 2024-10-08 00:57:58 | METOP-C | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba3252ef-a169-3aac-a295-9c135d648028 | -20.683201 | -47.1707 | 2024-10-08 00:57:59 | METOP-C | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8aa8b4d6-4edc-3d16-ad66-60e2ee6c2df9 | -20.315701 | -46.257401 | 2024-10-08 00:58:02 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 98570601-08dd-3f99-bd21-e1134988770d | -20.435301 | -47.622601 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f163a3ab-a3c3-33bc-9a91-cfd8555cf566 | -20.437 | -47.6301 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 12e660ab-6505-38d7-b4a5-5ecab29dd066 | -20.4256 | -47.625099 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8a7304a6-d14a-3464-a941-d2f0ea10b9bc | -20.427299 | -47.632599 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1ab6ef99-4f94-3c61-828b-474e334a07f8 | -20.429001 | -47.639999 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8d06897c-8913-3e24-a158-18bd817b7415 | -20.4307 | -47.6474 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5eaa4ea2-84b5-3b7b-b700-61e5d9c9f39f | -20.432301 | -47.6549 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a184112f-b73b-3ab5-8aaa-446121ec05ad | -20.434 | -47.6623 | 2024-10-08 00:58:05 | METOP-C | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 36f75fb7-b443-3c40-b3f8-4a1aacf6d75b | -20.4175 | -47.635101 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 16d8cfe0-27d3-3809-ab36-736259112a6c | -20.419201 | -47.642502 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0ce66f03-d38f-3208-9db6-b1d8e9089ecc | -20.4209 | -47.649899 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4ac55de6-d94c-385b-9b23-fb292e6fdb1c | -20.4226 | -47.657398 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ec646727-930d-319d-8e5b-adb6e09f1a72 | -20.424299 | -47.664799 | 2024-10-08 00:58:05 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aaaf6861-245d-3246-b995-126388c840bd | -20.4259 | -47.672199 | 2024-10-08 00:58:05 | METOP-C | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9993b801-d1b6-3145-a4d0-117ffba0900d | -20.427601 | -47.6796 | 2024-10-08 00:58:05 | METOP-C | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 76f391cc-7ec9-3737-9afd-e6e3fc50dd2d | -20.085199 | -46.730202 | 2024-10-08 00:58:07 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 50f2b6bd-88db-3045-9615-bd2a1444738f | -19.8675 | -45.678699 | 2024-10-08 00:58:07 | METOP-C | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 713056b2-9a01-37f5-b220-717a636b1a73 | -20.453501 | -48.810299 | 2024-10-08 00:58:09 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8636f75b-2034-3027-ab79-727de778c1a6 | -20.440599 | -48.7981 | 2024-10-08 00:58:09 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9f8da457-954f-3f5f-a551-98c3302e701a | -20.4146 | -48.773701 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3853b83e-a91a-3628-b6d3-82179a3d810a | -20.416201 | -48.780998 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f163f090-6c9a-3778-a417-a7740303dff0 | -20.417801 | -48.7883 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0b4162ef-427f-3960-a9b5-69442a12e1df | -20.419399 | -48.795601 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d86a9014-35ac-34b4-9bc9-6d91053fe16a | -20.421 | -48.802898 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0da79f93-844c-3555-a819-1c20818976f7 | -20.4226 | -48.8102 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6737bd7f-01bc-3105-b4bd-2a70c43e03fb | -20.4032 | -48.768799 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2171a1a7-fa0c-3bac-85ef-91ce6a5e4219 | -20.4049 | -48.7761 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 92372d2a-3758-3777-b639-cca914bfec3f | -20.4065 | -48.783401 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README15.md)
