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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f86642fc-1224-3427-91e1-a6dd803e151e | -15.56953 | -47.85654 | 2025-03-18 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 927d0b56-0bd9-3142-961d-e56b66fd36b0 | -20.44558 | -56.5559 | 2025-03-18 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f904eb16-fe6e-3dac-ac94-689ad741f849 | -12.81528 | -45.01106 | 2025-03-18 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0da3cd4d-d63e-3c02-8916-63d75389221c | -17.67728 | -42.7402 | 2025-03-18 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c586b848-78ac-3b86-8040-1d455451bb4e | -12.08026 | -45.63172 | 2025-03-18 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b81fb1c-9ac8-3352-b0f1-02daca63aac5 | -11.56712 | -47.61779 | 2025-03-18 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0155c2bf-f75f-315e-9917-c933231f0f8b | -12.07415 | -45.62701 | 2025-03-18 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81c25662-9830-3eb7-8fa3-f7c146760363 | -16.09285 | -42.28326 | 2025-03-18 04:17:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| cdd37c68-3bf5-30c1-beba-6ca32ce8a65a | -23.40525 | -46.55666 | 2025-03-18 04:17:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fa9c9b33-4f80-3bd9-a9ab-2ca447e97201 | -18.22625 | -42.35376 | 2025-03-18 04:17:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c93c342-d76f-314a-97fa-dbb808b7a1fe | -14.85765 | -45.19557 | 2025-03-18 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33fdabae-a4f0-37b6-be53-2a80cc82326b | -16.63203 | -46.94946 | 2025-03-18 04:17:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfb06acf-8c70-361f-a89c-a04544d99cdd | -16.09644 | -42.28377 | 2025-03-18 04:17:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6a79b6a4-85e1-3085-adeb-ce2061d7cb80 | -12.07749 | -45.62756 | 2025-03-18 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6272eb50-d379-392a-926a-85d62acdd85f | -18.05157 | -43.0332 | 2025-03-18 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3ce4663f-5353-33de-b30e-6fb4d16526b8 | -17.67669 | -42.74443 | 2025-03-18 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 461f5a6e-b223-399e-8ed1-e0290681adf1 | -16.63807 | -44.03667 | 2025-03-18 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5b16fdd-43dc-3aae-b11a-e687b42f71fb | -11.57127 | -47.6214 | 2025-03-18 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 296af2fa-742e-373e-b5b4-0a2d4eb4a8db | -12.07692 | -45.63116 | 2025-03-18 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 965e8742-6bf1-3b80-b8a0-c6b2d5cf5729 | -13.68151 | -42.99939 | 2025-03-18 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 784e3a95-9842-3ba4-b9af-9351abbbdc93 | -20.561 | -55.31603 | 2025-03-18 04:17:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5faead5b-1d0b-3e1b-aa1c-381da0ab7ee7 | -14.13383 | -41.69186 | 2025-03-18 04:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cd5c5f02-75ef-3ba3-ac7f-2ad7c96d2265 | -14.12316 | -47.68248 | 2025-03-18 04:17:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d966ba53-2f2b-3b1f-84bf-20083e376c34 | -12.84551 | -43.83274 | 2025-03-18 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07b8530b-3031-3735-af27-f04c60bc972a | -23.59489 | -47.43944 | 2025-03-18 04:17:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4dc497f5-9cf8-32a7-b90b-5718eb4174e8 | -14.85262 | -46.8025 | 2025-03-18 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d5b3f843-ec03-3caf-8106-a572e9ec61c6 | -31.27422 | -52.88142 | 2025-03-18 04:19:00 | NOAA-21 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 9e3b78f1-ef97-3631-98c4-c5ba0ec0201a | -20.76537 | -46.76983 | 2025-03-18 04:19:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c7d30c8a-6fb6-377a-ba34-5c682350bef8 | -18.73797 | -49.54092 | 2025-03-18 04:19:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a178714-d931-37bf-acf3-6f7333189907 | -27.68697 | -48.75209 | 2025-03-18 04:19:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 27a58a4d-b553-3387-bedf-1f39e590ca62 | -19.48755 | -54.85056 | 2025-03-18 04:19:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18904919-3241-328c-9844-e10a73018d2f | -19.70862 | -44.77269 | 2025-03-18 04:19:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3e0b877c-52de-3d17-a98d-468de2f8875b | -17.75661 | -56.31459 | 2025-03-18 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a0da62e8-dc7b-3441-a5cc-67e03d4f4bbe | -29.58272 | -51.98645 | 2025-03-18 04:19:00 | NOAA-21 | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f09019a1-ecde-3032-bf16-68527ab15a7b | -28.58722 | -49.44201 | 2025-03-18 04:19:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 90e281e1-bdd2-344d-a024-55e731c67e7e | -30.42713 | -53.52041 | 2025-03-18 04:19:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 04a7a0b9-303f-3519-8731-06bd686595d9 | -27.33669 | -50.57487 | 2025-03-18 04:19:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a1f8c9e6-c05d-329c-a6a2-3a431bdae41e | -19.07898 | -45.14535 | 2025-03-18 04:19:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e937754-364b-3fe2-a65d-15a3c8b6e98a | -17.76219 | -56.31587 | 2025-03-18 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b98cbc91-f7f0-3c11-91c5-71740ed26915 | -27.44674 | -48.44508 | 2025-03-18 04:19:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 361c133f-e97a-3acd-9d06-2344a1a5c7bd | -25.37971 | -50.70008 | 2025-03-18 04:19:00 | NOAA-21 | IRATI | PARANÁ | Brasil | 4110706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61ff341c-8ec6-303c-b37c-96fb6e3f66e2 | -14.1184 | -47.67968 | 2025-03-18 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c3f106f9-8e85-3ff3-8c4c-df38805f345a | -11.57002 | -47.62317 | 2025-03-18 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2b64558-ef5c-382f-bfa0-24ef770d7f3f | -11.96522 | -48.09236 | 2025-03-18 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e7a1fd5-6e0a-3c2f-8330-ae5e4d11c9a6 | -12.07977 | -45.63125 | 2025-03-18 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65d055aa-8855-320c-aa55-887fe0e26cd4 | -10.72869 | -49.55891 | 2025-03-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a3f3e7c-53eb-3476-a9c8-594d904b6fdf | -13.90735 | -46.5822 | 2025-03-18 04:40:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0d1401e-7627-3e22-a468-35730fcbbca8 | -12.88907 | -45.04561 | 2025-03-18 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bac677b9-c06b-3308-8bf4-63534cbd45fc | -12.88854 | -45.04961 | 2025-03-18 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed1b610a-2872-377d-ad90-7734844ce441 | -14.12145 | -47.68467 | 2025-03-18 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 307aa1b5-8050-3e4c-baeb-c44a94cc6b70 | -13.30082 | -54.36788 | 2025-03-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3f1feda-efeb-3d26-9f4e-6a082bfa58d6 | -11.18953 | -40.56146 | 2025-03-18 04:40:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 228e9bec-bbe1-31a8-b192-605d266552e6 | -12.89278 | -45.05022 | 2025-03-18 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cd415b0-bb55-34a1-9db5-6181bbaabfa7 | -13.30447 | -54.36852 | 2025-03-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dfb2e23-7899-34c6-a994-8daa4a02b173 | -13.30158 | -54.3635 | 2025-03-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a93e98f-fa95-3c6d-89fe-f8eb5b6c334b | -13.71299 | -48.44138 | 2025-03-18 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 687dd3d8-d0c6-315f-a5af-f2ca16fdc14f | -14.11942 | -47.68245 | 2025-03-18 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ba8bff6-a7ee-3951-923a-3d164a2c907d | -13.91125 | -46.58278 | 2025-03-18 04:40:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0e4e489-bb30-3dda-8745-ee6f41053814 | -12.08026 | -45.62767 | 2025-03-18 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc8d7cfb-cf5f-3d22-865a-cec9d30830dd | -10.72923 | -49.55536 | 2025-03-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43ee38e5-3ae3-3cfd-96aa-8de037287e08 | -11.56704 | -47.61848 | 2025-03-18 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44718f14-b795-3085-8d10-0ac4d0e7278b | -12.07573 | -45.63067 | 2025-03-18 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27c8f6bb-0de1-35b4-806f-6cdf19410893 | -12.07623 | -45.62709 | 2025-03-18 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd85cccb-c340-32ef-b6df-d50bc54d73d2 | -12.84685 | -43.83123 | 2025-03-18 04:40:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e883aeed-816a-3474-afbf-7d019d8eb2c5 | -14.12207 | -47.68025 | 2025-03-18 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 280dd538-2efa-3938-a7a5-970b4fd28409 | -12.89331 | -45.04622 | 2025-03-18 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04c7cba5-9b9f-337b-813f-f09bae6a7e3a | -11.19001 | -40.55768 | 2025-03-18 04:40:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8aae1fe9-8598-3645-8ba6-1c15d5b0073b | -12.07219 | -45.6265 | 2025-03-18 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e9f467a-2d85-331a-8181-ecefcf98a8ce | -12.07672 | -45.6235 | 2025-03-18 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a936947a-f0da-33eb-8339-ad50eb4e2ba1 | -16.63762 | -44.03938 | 2025-03-18 04:42:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19d870ba-1534-3000-b9df-62860307541f | -16.09689 | -42.28434 | 2025-03-18 04:42:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 96d7cb83-e9b8-3abf-bfa8-6e8094e7733d | -16.34758 | -43.69571 | 2025-03-18 04:42:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94f6c2ae-0bf7-3d92-9e13-368dabdc3152 | -19.48335 | -54.84658 | 2025-03-18 04:42:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f352172c-4301-3325-ae04-0f5a49b1554c | -15.88347 | -46.00772 | 2025-03-18 04:42:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4d9e380-9d6b-3881-9b91-a692f17160ad | -19.48613 | -54.85135 | 2025-03-18 04:42:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b19486e-83a6-329c-9415-4e0b348d847e | -19.33949 | -54.1773 | 2025-03-18 04:42:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bfdc06e-d8fb-33ea-b1e7-649c18a182af | -16.09455 | -42.28127 | 2025-03-18 04:42:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 0342bb77-3a80-3ff4-9bc8-c68ee2f14aa3 | -16.63804 | -44.03537 | 2025-03-18 04:42:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb5da1fd-260c-3282-a4ed-a24903bcc147 | -15.07729 | -48.94424 | 2025-03-18 04:42:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fefc3d4d-670b-3a18-acd6-06b351959874 | -16.09192 | -42.28025 | 2025-03-18 04:42:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d386065d-1086-3bb9-b3d8-af6ca2c9cb29 | -16.09727 | -42.28082 | 2025-03-18 04:42:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7499ff4d-c80a-34d1-a795-c5b6912ba4ff | -16.68001 | -43.88479 | 2025-03-18 04:42:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13074dab-7c32-3cfb-8556-92d0d6e09c27 | -15.63601 | -57.31275 | 2025-03-18 04:42:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f1550c2-c2f1-3d33-87fd-484ff9693b42 | -17.75951 | -56.31471 | 2025-03-18 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 437a71b1-6078-39af-aae9-20457c55c2d8 | -16.63744 | -44.04055 | 2025-03-18 04:42:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e95012c1-2261-310c-8e44-9cfb2bc41f76 | -16.39791 | -51.54757 | 2025-03-18 04:42:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2dd6ce3-947b-3c0f-820a-e41ac2b403ff | -15.56901 | -47.85656 | 2025-03-18 04:42:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 188ba423-76bc-3dfd-8925-bbc24c4d23a5 | -20.76233 | -46.77096 | 2025-03-18 04:42:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e5f778ad-b12e-3c02-93c5-ba658180e3cc | -16.62996 | -46.95198 | 2025-03-18 04:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a6c4e958-c188-3a9d-ba1d-d124be6b581c | -15.58248 | -56.01502 | 2025-03-18 04:42:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92eda1e5-b73b-3f27-aad3-09ebc39dfb7f | -18.39534 | -44.19471 | 2025-03-18 04:42:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edcf44e1-950f-32ea-b4fc-f96fcefa99fb | -23.23803 | -51.28483 | 2025-03-18 04:44:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 992c49a8-0581-31f2-87da-e82917c6f29f | -21.33269 | -48.64534 | 2025-03-18 04:44:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 74641fdc-d7a7-3723-8da5-b90ad448172d | -24.24208 | -50.73886 | 2025-03-18 04:44:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 616254cb-1c3b-3a1c-af54-925ed51f2406 | -27.33445 | -50.57569 | 2025-03-18 04:44:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9c1e1758-53bc-3539-83ea-431bdba1812f | -23.15706 | -45.77972 | 2025-03-18 04:44:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74922aec-7e58-3991-be1d-4b3c2a0d0925 | -23.21132 | -50.81342 | 2025-03-18 04:44:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a7c5b1ff-c514-31ce-b158-273fb8964e36 | -27.44896 | -48.44429 | 2025-03-18 04:44:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3e178f52-9ae3-399e-8451-4a9821702d8a | -27.68618 | -48.75182 | 2025-03-18 04:44:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99d50f52-2bc7-3ac1-8976-5fadf2fdc0c8 | -20.56126 | -55.3149 | 2025-03-18 04:44:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README3.md)
