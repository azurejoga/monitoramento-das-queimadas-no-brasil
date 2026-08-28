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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c6b98aa-e28a-3502-88a5-da8542d0ea55 | -14.87616 | -52.59587 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3f54d1ce-695e-3aeb-93aa-6bcf2f86c327 | -12.02196 | -47.15805 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5705ff0c-5b26-34f1-9451-a0bbf87f2532 | -11.00198 | -49.65278 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e38d4fd8-3267-3733-bb46-e8813c4eb886 | -12.43648 | -43.41408 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96c6d33c-bd1f-33d2-8c97-4120876a4b75 | -11.1863 | -51.22308 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b51950ca-0113-398f-a5a0-b943d969978b | -20.34074 | -47.59563 | 2026-08-28 04:17:00 | NOAA-21 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9aea5769-73ff-3955-ba96-871fdeba33d4 | -13.61181 | -45.78158 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29e02369-9776-3f5e-98b8-093794344e3e | -10.75755 | -54.03156 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c8cc8d0b-d61d-3dd1-ac31-c03ced8add70 | -16.68245 | -45.4167 | 2026-08-28 04:17:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 60807426-4e80-325d-9505-2b4b858f1da5 | -13.83893 | -54.04422 | 2026-08-28 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23d7dcfa-3677-3702-a04b-30fd8461ac71 | -9.0589 | -45.78594 | 2026-08-28 04:17:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a597d99-4b65-386b-9c8e-0d85d387d16d | -8.58839 | -54.78857 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 927a7738-9fb1-3132-91dd-855406f77e67 | -14.86715 | -52.60251 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2bdf92e4-0eb7-36e8-b2eb-24dab46cf048 | -12.13077 | -43.37049 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e36330d-29b9-3f8a-8e18-8735315d82ff | -13.58906 | -45.77417 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9361643-be10-3ed2-8b04-4189c57cf9ce | -9.96665 | -53.93821 | 2026-08-28 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 4ace474d-9a2e-3878-b7f1-fa61b03742ec | -15.52677 | -41.93329 | 2026-08-28 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8c28257d-72f6-3170-8801-fd4a9e820246 | -11.49048 | -45.06657 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bdf045e-f1bd-3d68-8675-da835e3ad18b | -11.15779 | -45.06305 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5544bcf4-09b7-30ea-8c27-2d5885b92270 | -16.49174 | -39.35083 | 2026-08-28 04:17:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f96d7ac1-b2f6-3e94-a2a3-01940f5f9eed | -9.22617 | -51.53703 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a919230c-214f-33d2-a54d-51dd9f97633c | -8.95199 | -50.18409 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df4c12ce-38e0-34a2-be7a-de893e42599a | -10.92393 | -50.5352 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 91ade13d-c121-35d5-86a2-d427f0fa9f4a | -11.48717 | -45.06601 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 663b19c9-dd0b-3d57-9e17-202d7df618bf | -12.78442 | -46.44337 | 2026-08-28 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ada77e6-86ee-3c13-847d-07d5b6588bd3 | -12.25665 | -50.58309 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9a024a4d-93df-3e22-91bd-3f9a49af3298 | -11.29701 | -41.87132 | 2026-08-28 04:17:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96008491-30b3-32b9-b6ad-b79987abffac | -11.28844 | -54.02689 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6a80032a-99aa-307c-8a0c-15ec4cf302e3 | -10.92035 | -50.5302 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0d0701cc-c40a-3453-907e-d9a14652bd1a | -16.04636 | -47.23273 | 2026-08-28 04:17:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63e1158f-89ce-3e3b-a0bd-e38b3f249e7b | -11.79866 | -47.67392 | 2026-08-28 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 969d3f4b-3789-34d7-aec6-e27b7ab50495 | -14.42305 | -52.59888 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d09bf3d8-527e-326f-85bb-1eca1da17a4c | -13.83429 | -54.04398 | 2026-08-28 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0971f1ca-3e3f-30a5-b3ce-888bdca57bd5 | -11.72892 | -54.55058 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c4b6f9a-ceef-372d-b73b-d72820e7a19e | -10.48974 | -46.18971 | 2026-08-28 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdc66bc5-e607-36eb-8756-6a8609305941 | -11.73184 | -54.5355 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c518bf7e-c19c-3fc0-83c6-d7a6eb026dc6 | -10.90733 | -50.52788 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ad26f10f-743a-3461-9f0e-e71eb13ca144 | -11.64185 | -46.73104 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cb30721-a81e-328b-8da6-d3c2115d859b | -20.28037 | -46.58553 | 2026-08-28 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0703ef5e-c6bc-3e5a-aa2f-c1e49e09cafb | -13.31946 | -48.21373 | 2026-08-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02321de2-f31d-369a-a12d-c55db724c430 | -11.20243 | -55.09325 | 2026-08-28 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d4d8776-c76f-32f7-a73d-3fb1fddbe8b3 | -12.2581 | -50.57496 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f4ebdb06-1861-383c-8216-013cdc59c521 | -11.23344 | -54.01292 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a209c24-1bd8-3854-b639-0bb7ac5f6856 | -11.20323 | -55.08911 | 2026-08-28 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f8098ec-8cd1-3e9e-8020-cf2eb663181d | -9.22529 | -51.5419 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fbf7bc4c-8bdd-363f-bcc9-e14d1d3a19f7 | -9.87461 | -46.42463 | 2026-08-28 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 104ece89-0d8a-3b05-a850-8aa30fc4016f | -11.28439 | -54.01863 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 72dfe830-f70a-3248-9ec4-4d7ed4a2aa4e | -12.7866 | -46.45147 | 2026-08-28 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35837908-30ff-37f2-8753-964c4d1a050b | -8.8109 | -50.08615 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57094aad-e3a9-38b1-a8dd-3bd6a4004ac2 | -12.24109 | -50.57187 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8a186657-5b5d-33d3-bd3a-c01a66322b5f | -14.31054 | -51.70878 | 2026-08-28 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 891a737d-52c4-3886-9cb1-eb7329795378 | -12.28572 | -50.5926 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 593cf44b-1e09-3734-8c4b-287570c7542b | -12.2361 | -50.57515 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7584d88a-9ed3-3ec8-a3e9-400b1a8e6f61 | -11.24153 | -53.9998 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b53754c-e60a-33b0-94f8-70ce444a1eac | -11.53692 | -45.51998 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e6f1635-1397-33cf-8e50-8c95999fbdfe | -14.99002 | -52.59594 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59625ba3-9340-370d-af33-ff9b9fb46aae | -11.33383 | -48.38182 | 2026-08-28 04:17:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7c5b702-9ea9-38bf-b34f-656e1d575223 | -8.6027 | -54.79157 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0eef3e13-a3c2-3509-ba25-a6bb97a936ba | -11.4694 | -46.94452 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 271695a6-19e1-3b10-b780-b6d74009835f | -14.11932 | -44.38604 | 2026-08-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7224a76-4e63-3234-8a34-1c7acfbf509d | -11.20822 | -55.09453 | 2026-08-28 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00f4dd2b-3e45-3bf7-918b-76e7e9e41f76 | -8.78988 | -50.07391 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23cb097d-e4cc-336d-b2ba-375361f0cea0 | -11.48881 | -45.07714 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec6c8633-dafc-35f3-b11b-e2f652a01a52 | -12.20131 | -50.57304 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5c31e40-fc2b-34f3-80b4-f86a4d2f53ab | -13.32172 | -48.20045 | 2026-08-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b32d2d72-4f9d-3550-afd8-b3682342b2f1 | -8.60737 | -54.71934 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b7ffb43-db6b-3af4-88b1-ee83c5eafa7e | -11.82395 | -47.21545 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 80149e8f-329c-3290-bebc-d93d1dbd66b2 | -11.49371 | -45.11043 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 470386e6-0b3b-3af7-a7fc-056d08007f92 | -11.01554 | -49.64753 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31d033ca-2760-3b27-aa08-48f8a56a895a | -11.23005 | -54.00098 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5da1c4c8-1477-3f04-aba3-9bb079ba31cb | -11.16823 | -51.21964 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7181244-20c2-36da-812d-96e97dae2843 | -10.76236 | -53.97624 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73ef2604-9efd-33a6-b5aa-387e33cbb18c | -14.44016 | -54.05437 | 2026-08-28 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14225290-aa55-3e74-bc2d-4df9da1a5f9f | -20.82762 | -54.95227 | 2026-08-28 04:17:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df7dd2b6-a052-3d77-a32f-522d027c3d10 | -11.23072 | -53.99741 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c68c277a-a1ad-3e40-bd08-1da6f35fb17c | -11.6648 | -50.46265 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65cd9599-36a1-318d-b667-daaf406528e8 | -8.78333 | -49.95587 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13965d4f-c383-3373-95fc-052e45231e3a | -8.59754 | -54.78621 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c7a889a6-77d2-3a41-9ae4-66d572c945e1 | -11.0177 | -49.65939 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb96e973-c982-382d-9d8b-69ee4d84c250 | -14.88079 | -52.59679 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| edd2ac60-454a-3bbe-8e99-aaef3ec3f5ba | -10.76031 | -54.04702 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f3811468-ccff-36c8-80a5-30a317b688d7 | -15.62843 | -45.9353 | 2026-08-28 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f924189d-10a7-3505-9ea3-b4ef331ba45e | -11.21988 | -53.99526 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbcb1196-952f-3cbc-998d-8a92e87b1950 | -9.45103 | -51.71316 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9785ee07-ea62-3479-b8b2-2890671dcb45 | -12.24035 | -50.57592 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 18627b57-a15d-33c4-bde7-e09db1aba91f | -11.82749 | -47.21601 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0715ef71-963c-35f5-ae1a-49eb8fc6a7ea | -11.20192 | -51.24033 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 7955f33b-e799-3619-84f1-f11b5f84bbcd | -14.86909 | -52.63225 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 591c9617-9c86-35d1-9831-fbe234ef25b7 | -11.82042 | -47.21488 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ba91fe34-0084-3206-83d5-6e3052d0cb37 | -11.72482 | -54.54191 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a431b4ab-70d8-37c7-bede-be52824b6a50 | -11.28232 | -54.02943 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2b3443c1-bba7-3a95-984a-3cd68e79cd3b | -13.46406 | -54.01977 | 2026-08-28 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4d2a451-ed67-39ed-8f34-f3f193fba75e | -12.28074 | -50.59589 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9f6868e6-c343-3730-8db7-26f496bcbfb6 | -19.528 | -47.62823 | 2026-08-28 04:17:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9b219c21-23fc-3859-ab90-d10a2ffd021b | -9.21749 | -51.55957 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efa63079-fc57-38f0-aa30-3a0788336463 | -12.285 | -50.59667 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a447df76-a366-3f11-8a26-c3ae03f9925d | -11.72073 | -54.53322 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4b6c8c25-1aab-3011-81aa-99796af7c8f0 | -14.15323 | -52.82558 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cf1a931-cbe3-38e5-be25-4907c607c49b | -11.72629 | -54.53436 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ddf2ffb2-07ef-3c10-8f5c-3dec22884131 | -13.33045 | -48.19309 | 2026-08-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README23.md)
