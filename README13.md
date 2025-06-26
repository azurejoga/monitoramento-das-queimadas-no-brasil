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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b96c8cca-0544-3d61-ba83-8c21e23453c9 | -11.58922 | -44.64399 | 2025-06-26 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e15a4996-b229-3468-81be-98699bde71d7 | -9.33293 | -47.83076 | 2025-06-26 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49a04275-9a8d-3320-99a9-97c5a267a5e6 | -10.65104 | -44.49099 | 2025-06-26 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cbcd4e8-4ded-33f3-9170-57be9f41e6a5 | -12.80743 | -48.73346 | 2025-06-26 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d0c26c56-586f-3896-aa93-0770ed41cf24 | -8.26148 | -47.0244 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f71d3059-34a5-3302-9440-f94f8325fb72 | -7.20316 | -43.09084 | 2025-06-26 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 430dd34e-639e-3449-8d04-86c464032b79 | -8.67413 | -49.95314 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb2d6067-b9ef-32c8-ace4-84d0bfb182b4 | -11.4356 | -54.47985 | 2025-06-26 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c0b4514-fefd-329e-9f06-66f9792abbba | -6.17835 | -48.07988 | 2025-06-26 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2b2e6d8a-41a4-3fd3-b2b8-ad997f4bdb6d | -10.86747 | -53.76787 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ab09f5f-009b-3ecc-ab31-678b4a12763a | -10.55943 | -52.01322 | 2025-06-26 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58c39800-a5f1-3018-b7ea-f8c77c770b08 | -10.35015 | -49.91274 | 2025-06-26 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b67e714-da05-3f78-b4ee-215a0fbcf4f6 | -8.06315 | -43.1046 | 2025-06-26 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9ad87acc-3b17-3bc5-92aa-c14ca9332c26 | -11.06149 | -55.38235 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cfa7bad9-2803-39fb-bbef-fe03ca24e9fe | -8.44483 | -49.63235 | 2025-06-26 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72002b57-45ef-3456-98e1-26babf530382 | -9.7064 | -49.47956 | 2025-06-26 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bbfa8c6-961c-3923-806c-ca60347a4f17 | -11.81913 | -47.55218 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20a16ffa-7661-37c4-ba83-a7e03389dee7 | -10.30433 | -57.14029 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9e871f6-043c-319a-be25-868eeeda7ece | -7.19805 | -43.09465 | 2025-06-26 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c6c40cc6-d2f0-3445-9a8d-050a5ed994b3 | -7.75003 | -47.61588 | 2025-06-26 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cae86c0b-8791-36f4-9aa6-37b77a4445e4 | -11.60672 | -55.54213 | 2025-06-26 04:40:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b01b015f-c31e-32ba-8a88-71b7937cc3f8 | -9.11764 | -49.43817 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0e3bcdb9-df9d-3848-b9fe-cea848160000 | -11.86967 | -54.69304 | 2025-06-26 04:40:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c2224b9-b290-3912-b2b2-8adce2223530 | -9.5147 | -56.10346 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cbdd6e1e-4477-31cf-891a-921861af0e42 | -7.74886 | -47.60009 | 2025-06-26 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e81ffd7-adfe-3701-9474-7fffbae0d891 | -6.17889 | -48.07631 | 2025-06-26 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c0220581-727d-386f-80bb-2d4bad2823b4 | -9.50697 | -56.09803 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 733d311c-a832-3063-baca-485068e9e24e | -9.875 | -48.45121 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d34a73a-f6d3-3690-bf09-2b8880037f3e | -8.72462 | -48.01193 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33a1c490-8a0d-3c9e-ad31-3d2338814680 | -11.0711 | -55.37363 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 508f27dc-68ba-3e07-abe7-9299138394ad | -11.136 | -53.91866 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf021bc0-22b5-36b6-93e0-dc96b43266e5 | -11.7772 | -47.40562 | 2025-06-26 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5c1eb4a-5111-3ffd-9c7e-d076ddf2a3fb | -8.67797 | -49.9502 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35f28db3-dfdf-3f78-a9d0-d66fbc4a4ba5 | -7.09582 | -49.16378 | 2025-06-26 04:40:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc926484-641e-34c5-861c-ad87e9cd5a6e | -9.32945 | -47.83025 | 2025-06-26 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4c6143c3-0d25-303c-b5b2-668481d42345 | -7.36414 | -46.23222 | 2025-06-26 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1210b5a3-7369-356b-9706-16a0acb6e429 | -12.4214 | -46.66856 | 2025-06-26 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87465a7e-3726-3b92-a014-519fa71ff978 | -9.67139 | -48.77507 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f556c22-3c1f-3ac4-984e-fac932a5fa1d | -9.67195 | -48.77143 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c033b59-149a-380b-b121-bc5cf14a14a0 | -8.99475 | -47.93878 | 2025-06-26 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea53580b-535c-32a3-8663-576d4ce74bb7 | -14.4147 | -47.87785 | 2025-06-26 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac52526b-e562-3d54-a70d-3a4072f11d67 | -12.90725 | -56.98538 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 508688c4-d659-399a-b3a7-4f6324e9e431 | -14.19865 | -57.41015 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae2409a4-2546-31ad-9d23-bf2db36651ed | -17.23049 | -46.08028 | 2025-06-26 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a00e05f-fcb9-33ce-bedd-a8d8c683855a | -13.5203 | -56.57542 | 2025-06-26 04:42:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c910eca-e0e7-313a-9d86-2fc7c98c2121 | -15.57189 | -47.85423 | 2025-06-26 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 345382f7-4677-3bb3-acd5-125a081c99bf | -12.61947 | -57.87857 | 2025-06-26 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dac4bd4-48dd-3a7f-a8e6-58d56225ba2a | -18.60935 | -44.26432 | 2025-06-26 04:42:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb102551-81d4-3b43-b378-31e73d2f5ca1 | -13.29466 | -57.08371 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d73bcd4f-762f-3d38-b786-3cb9531a0b6c | -13.91929 | -49.52675 | 2025-06-26 04:42:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3cd0e91-2092-3223-96bb-8b9e341fa764 | -16.04414 | -43.81813 | 2025-06-26 04:42:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 811a1327-8517-3b89-a182-621588566e80 | -15.07991 | -48.94647 | 2025-06-26 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 065ab20b-6522-3f96-9a5c-71457fc014c3 | -12.58643 | -57.38625 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84b5b179-6912-36e7-ba72-2e0fcd20b748 | -12.58001 | -56.98907 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e14347e-765a-364f-b012-90cc94a1be06 | -14.4038 | -47.87549 | 2025-06-26 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9997c140-3e74-368f-96ae-73017e04244f | -17.19199 | -46.85338 | 2025-06-26 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbdb4c0c-8adb-3f2d-9761-21ec433320e7 | -15.73738 | -48.26984 | 2025-06-26 04:42:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e73f28d-9a73-30e5-bf26-6d1ef12dcfed | -14.48836 | -47.96394 | 2025-06-26 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 952f3f8c-54ac-3305-8448-f6673b9c271d | -13.78183 | -54.30085 | 2025-06-26 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d48dce0-4f7c-32f3-a5d7-15121af1e68b | -12.6158 | -57.87321 | 2025-06-26 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cc7c435-ca8b-3891-8067-fd73d1c87a67 | -14.48889 | -46.49685 | 2025-06-26 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 371d68aa-4f11-34e9-bc05-db2c58b55e30 | -13.65547 | -50.19186 | 2025-06-26 04:42:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84b2246c-4679-3737-b097-f51a85b8b370 | -18.61423 | -44.26493 | 2025-06-26 04:42:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bee349a-5927-353e-a5e2-7fa1c4095fdb | -13.2932 | -57.0918 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aca46626-8d02-3816-a794-16b5e2919bab | -12.61496 | -57.87776 | 2025-06-26 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1153877-030e-3720-a3e6-a05e0b960384 | -17.18793 | -46.85303 | 2025-06-26 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3f2fb5c-398e-3d16-bb9a-b49f707aed34 | -14.37861 | -50.3283 | 2025-06-26 04:42:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 436c63b0-e945-386e-a2cb-6884e2165179 | -19.03535 | -47.91138 | 2025-06-26 04:42:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69721346-711d-3c39-8b5c-71ea0b2c74b5 | -12.59157 | -57.38273 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13932091-785c-3ac9-b1be-3b3685e7f6f2 | -19.06588 | -52.45363 | 2025-06-26 04:42:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ada60a83-5f3d-3b46-8674-de9642017391 | -12.58073 | -56.985 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5b81ddd-0784-3546-9090-5d95c53507bd | -16.68311 | -43.88658 | 2025-06-26 04:42:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b4fa95c-f7fd-3ba4-a1c5-01fbf581e740 | -14.90764 | -54.32797 | 2025-06-26 04:42:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c46d207d-76c7-38bb-8282-89921ad6074a | -12.58721 | -57.38196 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f342f18f-f273-3e42-a941-7c601082a074 | -17.23017 | -46.08199 | 2025-06-26 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cd542dd-5172-3722-a02b-e7fbe2039a43 | -14.81015 | -48.28026 | 2025-06-26 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4024e49-607d-3c39-a79c-a29c9717e5a0 | -14.48664 | -46.49446 | 2025-06-26 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2bf17ba-d76f-3571-aeb1-2a78fd3869a4 | -15.27657 | -50.70491 | 2025-06-26 04:42:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba0d273e-9d07-34e9-a8d3-58cefa8c67f2 | -14.38195 | -50.32883 | 2025-06-26 04:42:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27e2cc23-91fd-3bdf-8c56-14f7a6efcc54 | -13.78253 | -54.29672 | 2025-06-26 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7b6d6a4-f988-34f0-8795-af37c2514a83 | -19.06531 | -52.45726 | 2025-06-26 04:42:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 419f5543-565d-3936-9a4a-60d7bdd10c0d | -13.29119 | -57.07883 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7358e45f-636e-3ad2-9bf6-140fa7a4d802 | -12.53118 | -57.18835 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 120d2e92-e91b-3762-a779-07c212e3aad9 | -18.09203 | -54.2761 | 2025-06-26 04:42:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac58fee8-99b2-3649-811c-d401bfaf40e9 | -17.14494 | -52.4892 | 2025-06-26 04:42:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 221ef6ed-1541-312e-88e6-d9d8c12caffe | -20.25147 | -46.7342 | 2025-06-26 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9cc23e7-9026-3a11-99ab-d928ea082383 | -14.40744 | -47.87624 | 2025-06-26 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e53c338-3b9d-3704-b7e7-dbf6e8209808 | -17.5999 | -48.42771 | 2025-06-26 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e81a9332-bf3f-38ec-b028-54a41b50fa49 | -16.25538 | -52.15396 | 2025-06-26 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4867072a-ed59-3d3c-909b-2733b51afd08 | -14.66955 | -53.12837 | 2025-06-26 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85f1f028-c3af-3566-be7e-8bd2e7dc7cde | -14.04084 | -50.51786 | 2025-06-26 04:42:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11547a79-8591-30de-94d9-38780ffe8ecd | -18.0914 | -54.27995 | 2025-06-26 04:42:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2258420a-330d-3428-ae35-effa927202a4 | -16.30225 | -53.8277 | 2025-06-26 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cf10d8e-1b5c-32d9-83b7-3ab77a3a2a05 | -14.40345 | -47.878 | 2025-06-26 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51fecb3e-2732-32b1-8795-76bddd195a33 | -17.58091 | -47.482 | 2025-06-26 04:42:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc85382e-3c7f-3223-8990-06407aef45f1 | -13.29741 | -57.09266 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 376abf32-6500-3e7d-904c-8660536b83fd | -13.29393 | -57.08775 | 2025-06-26 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 912966e6-ebeb-3d55-aeb4-513c61a99185 | -14.74255 | -48.43058 | 2025-06-26 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71debb22-813b-3421-a150-85321365f542 | -18.09417 | -54.28442 | 2025-06-26 04:42:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ab72e48-0454-322f-bf1e-b9b9c8d4793c | -15.31822 | -46.90774 | 2025-06-26 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README14.md)
