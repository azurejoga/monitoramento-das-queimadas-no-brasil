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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4ecb376-035a-320c-90ff-b23d81a8cf37 | -13.44301 | -47.37507 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1320e0-8bc0-3d3e-93bc-76d815d7451f | -13.50793 | -42.50224 | 2025-10-30 04:27:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4b2fd235-972c-30d6-b455-0a89ede1d849 | -13.34572 | -47.67097 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3eee6d8-a3d8-3274-b9cd-f65483e0ee23 | -12.52211 | -50.57455 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04632223-52a6-3841-9bbe-118580abbd9f | -12.85105 | -48.62121 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 350f0dff-8865-3a7f-aac2-665956972ca5 | -12.01186 | -47.79185 | 2025-10-30 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af612650-36aa-3be6-a23a-bf610d612388 | -15.02658 | -46.31249 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02f5b20d-67bc-3c76-9c12-ebbed3078105 | -14.29463 | -47.33411 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37fb6407-a279-32ee-956c-c5e6118402ae | -13.61355 | -47.60929 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 063a2e83-cbb0-3e33-9741-6b4ef97d9469 | -12.68611 | -46.3013 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9bff21ed-824e-3fc7-949b-ba2ee4c9ddfe | -12.51568 | -50.56915 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7b4ba5f4-16d3-3289-8cc8-1b1c4d0fc63b | -12.51924 | -50.56978 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 915d443d-20af-3987-b872-647f9626da41 | -14.22424 | -48.13066 | 2025-10-30 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd4edff4-a976-3c33-84d2-03560f579324 | -13.22684 | -47.04168 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72887fce-74f1-360b-8b0a-770123b81d07 | -13.38067 | -47.42676 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04243ff5-5773-3447-a77c-8c554a79024b | -13.31777 | -47.48183 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43c0dc5b-f981-3f94-a7f1-ee7df316b33b | -15.85575 | -44.89203 | 2025-10-30 04:27:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d8c5937-4b79-3a02-b993-b577ff48efda | -12.14655 | -48.01296 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e030016-ac33-3594-aa8d-f6697906d022 | -12.51637 | -50.56501 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5673e3b5-cb55-3396-94d0-1d533577ef24 | -12.88993 | -48.27311 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae77def7-a9db-3b6a-aec5-ec1ea27d974a | -12.71021 | -46.30123 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd6ba318-6f34-34f7-bf46-ac3d49f2c027 | -12.91599 | -45.04639 | 2025-10-30 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2a93daa1-f9b7-3dce-b7eb-1e3bd6657e3c | -13.60937 | -48.40736 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5602d11c-1343-38e4-a96a-2622a436ab96 | -13.36062 | -43.08702 | 2025-10-30 04:27:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| dba98919-a26c-321e-bb51-9bd8319d9824 | -13.48829 | -47.99449 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74777c50-1742-3204-8c79-f91bf3cb2e6e | -13.43854 | -47.46894 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce7e50b3-54de-3c02-bb1a-3aa7c6ae420b | -13.61611 | -48.25904 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a29ea61d-129f-35f6-aca0-0616c2351254 | -14.64863 | -46.88791 | 2025-10-30 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 811bc4c5-f159-3d70-b169-97967b45add5 | -13.5321 | -44.34346 | 2025-10-30 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ba013b9-ade8-3dcb-b8d1-136745189e32 | -12.0329 | -49.94676 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b0a4264-c61a-3913-9936-50074fcc70e3 | -19.32806 | -43.06778 | 2025-10-30 04:27:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f25a3ec9-119d-3b92-9fa2-dae926a16f6e | -19.33706 | -43.06513 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 00cf1782-e62a-3bd9-b7cb-1e339fc5e130 | -13.2918 | -47.36484 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 976a9b77-5136-3a8d-8fed-4f3a5e5fbb4a | -15.55696 | -42.98204 | 2025-10-30 04:27:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 630798af-8afa-3eac-9115-437e5be4b35b | -14.38935 | -43.7197 | 2025-10-30 04:27:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cf7fd0b-d1db-3600-a996-ab9e03e6acdd | -13.17628 | -48.43762 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c60e786-85b8-3c6d-8c76-d332b4112341 | -14.03049 | -42.2919 | 2025-10-30 04:27:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 493b5b3a-6cb0-3081-a885-bc0e08e40337 | -13.27346 | -47.7206 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67bbb145-3088-356f-a293-98320e6c50fd | -13.70399 | -49.90958 | 2025-10-30 04:27:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c314e551-63c1-32d0-93b2-5214541cdd4a | -14.77611 | -44.98529 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60f82743-2762-37e6-99d7-a4a2725aa6ac | -13.42811 | -47.36182 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a527d8b2-08cd-3bf8-9a2f-22a337b638bb | -15.6303 | -48.88122 | 2025-10-30 04:27:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64d2d309-d9d2-35b4-a43d-fc879b627472 | -15.61102 | -43.98255 | 2025-10-30 04:27:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ff458b8-1e20-3f81-a6d5-190952b5d6a3 | -12.68892 | -46.30539 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2763a9fa-17e8-3aee-baa1-0c9b81cf1c6d | -13.85302 | -48.49903 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d3eb41d-d8a0-3c08-813f-90a9c9d19cb3 | -15.02885 | -46.32064 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e02e9e34-0611-3847-a670-014342f7c670 | -13.13432 | -42.50558 | 2025-10-30 04:27:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d2855a2-aa02-314e-bba3-cff5a17b98bc | -13.93783 | -50.33631 | 2025-10-30 04:27:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6e28812-5a77-3104-8db1-7c35a1c03530 | -13.95314 | -44.19033 | 2025-10-30 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50bd96ae-87bc-323e-a961-83508db5ed75 | -12.30684 | -50.25793 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3985c85e-5c2a-33eb-b5b4-1997f412e1fa | -12.21535 | -47.90113 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3679b375-6601-34f6-95bb-a1eae0eb3b15 | -12.25331 | -47.93985 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a55d36c-7c67-3ad2-9904-f2982f9cf43c | -12.608 | -43.20162 | 2025-10-30 04:27:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91aeb0c7-8fe9-3219-b12f-bbac05576581 | -16.8881 | -41.99664 | 2025-10-30 04:27:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e6e9d18a-db82-3773-8dc2-b9f5ec1efb69 | -14.90331 | -43.10211 | 2025-10-30 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0ff7898e-4dd0-3b2e-94ce-af38fcf9102f | -12.66706 | -47.34335 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5e7a062-cf58-3a0a-bac3-9a8e4a594bd0 | -13.17228 | -48.46245 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0665d5f-edbe-37a7-8bc8-b975e0759769 | -12.23477 | -46.47812 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a39adab-29a2-3b9e-9f01-9e38c9bb709c | -12.11768 | -47.14263 | 2025-10-30 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6fe7ad8-718b-302d-9da0-bfce13af6c04 | -12.87871 | -48.64071 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6ab18fc-6e45-306a-8f8c-8ccaa8ac4012 | -13.17571 | -48.44112 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dc60083-18a9-3234-b732-16172fb3d160 | -13.6088 | -48.4109 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da248b05-156e-326c-a186-dccc479defa6 | -13.38583 | -48.50853 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 168002f0-d171-3afd-ac35-111fe2a433c4 | -12.85047 | -48.62481 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6675541-c58d-396c-a89b-8781a9101f51 | -13.57508 | -47.33435 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c75c8be8-2ee5-351b-b012-ee3b53fa1035 | -13.27677 | -47.72114 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47d220c1-0035-3e5d-9beb-d78592881b56 | -13.61687 | -47.58818 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3e88cc5-2274-375c-aa7a-da2c52f85900 | -13.93252 | -48.48988 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5b2eb1c6-b7fc-3ba2-a85d-52d6d8f3e7fc | -15.94393 | -45.21746 | 2025-10-30 04:27:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ee61c65-1b9b-361f-96c7-bb95c69d2975 | -12.30155 | -50.33194 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d75ed8c3-db86-34af-9d77-7e55c6ae37a9 | -12.30332 | -50.25732 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b06dde5-f26f-3d8a-9255-e7f0aa574969 | -13.38122 | -47.42325 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d77f596b-d226-339a-a08c-ef566a9f9511 | -15.02601 | -46.31633 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c245799-dadc-3088-8b35-c32a34024f73 | -13.37626 | -47.38983 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 238468dd-5708-3348-a49e-966862afa067 | -14.23314 | -44.31726 | 2025-10-30 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed4cee75-5322-35b9-a1c0-0706a2e9f58b | -18.23135 | -42.37722 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9135d3a8-2947-3325-9f44-932d2bd54d28 | -13.32218 | -47.47529 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff2f7035-da80-39ec-95a6-f69ab4a40335 | -13.41597 | -47.3744 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19f37d72-0dbd-30e4-b2dd-e6f5bf1468d3 | -13.28373 | -48.57248 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91b955df-a810-39b0-ac9b-eb1ed355846a | -13.62293 | -47.5928 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25d10ab6-00cb-30d3-9e71-7c8cb4fed3d3 | -13.94816 | -48.45601 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1a49518-61fb-3e9d-858a-b04f2ebb3bce | -13.16566 | -48.46127 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0243ab08-8342-32e7-b2d5-55c801dcab15 | -12.8719 | -48.66191 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1edd67ff-ce67-3aaa-8e7b-7be4c65fcd9e | -13.30326 | -47.70377 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df00c3a0-e493-3bdf-bd90-4c966a94f50e | -13.33046 | -47.46569 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 302b3101-3f9b-378f-ba0f-70d43be035a2 | -13.9422 | -48.42949 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6d2c73e-18f9-316d-9bb0-a5c203a19139 | -13.46347 | -48.00124 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93e2fb70-f56c-37f5-9a39-e58bdfd25982 | -13.02445 | -48.80965 | 2025-10-30 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd33c714-e444-30ed-813f-cda106dcb2b6 | -12.71487 | -46.30524 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42a1d714-87ab-3a07-a853-0073bf3c733a | -13.67632 | -47.66306 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc481546-8681-32c5-989b-3621899cfdf1 | -14.30553 | -49.88229 | 2025-10-30 04:27:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2fff78a5-e300-3576-aa41-5a1cdea02ee1 | -14.9022 | -43.09855 | 2025-10-30 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86ecaca2-b5e8-3b0a-bf77-fc5eb0920b88 | -13.87178 | -43.55898 | 2025-10-30 04:27:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19371a4a-fd41-310b-a1c3-32377579c519 | -13.67357 | -47.65897 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63e1f622-fe66-332b-97a1-c0c01bdee1ca | -13.67096 | -47.17486 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7916d9f-d15f-3d31-a1a5-c6e61512ab8c | -13.4077 | -47.38408 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7ed7094-062c-3fa8-8f9f-92115bc89ed6 | -12.5626 | -48.88903 | 2025-10-30 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcbdc6b0-c5ee-3ad7-a1f0-8cf788f2c4c2 | -11.9982 | -49.84517 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6815916d-022b-33b2-a0bc-6387e93ce0ec | -12.17761 | -47.75424 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b08fd3e-5792-321f-b7ea-dcc14a15bbfc | -13.4239 | -44.05767 | 2025-10-30 04:27:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README59.md)
