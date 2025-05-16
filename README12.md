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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3318ed64-bb92-30c8-8d4b-3a62ca4d7189 | -11.30608 | -54.01112 | 2025-05-16 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3ee51db-5a7e-33cd-b672-b8b55734d49b | -10.68662 | -57.59248 | 2025-05-16 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f0676be-7b82-398c-a8a8-0a9eeff19f0f | -11.63 | -48.47179 | 2025-05-16 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d101c9a-4867-37e0-a841-a9de662b91fe | -11.38825 | -57.82428 | 2025-05-16 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 373bce4c-9712-36f0-92a4-311051d69ecd | -13.58687 | -47.37942 | 2025-05-16 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c3de1a8-d305-36c3-befa-c7299559246b | -11.87533 | -56.41443 | 2025-05-16 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62008e6a-a579-324b-b33e-a929eb91c810 | -13.96122 | -56.80147 | 2025-05-16 04:57:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f34c2a0c-6360-3c72-8a83-6ea6159ffb5e | -11.65261 | -58.26368 | 2025-05-16 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b2989b5-e626-3624-a860-95fc1cc043b0 | -12.16482 | -48.80822 | 2025-05-16 04:57:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5edc9c58-d2f3-332e-a105-d01b25a50fdc | -11.66469 | -54.93951 | 2025-05-16 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dccbb68-e682-3604-80e9-d9a38d55e375 | -11.30553 | -54.01474 | 2025-05-16 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbe195e7-6f5f-380d-986d-1abad00f3a0e | -10.46339 | -54.98063 | 2025-05-16 04:57:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0b90ea7-4894-3346-bc9a-5f19d1d95745 | -11.41744 | -54.32662 | 2025-05-16 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8c76381-6824-3e01-bc7a-2bc9fa278a44 | -11.58106 | -47.6117 | 2025-05-16 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55c47afe-f560-305d-be26-79d8c676c4a6 | -12.62576 | -54.87148 | 2025-05-16 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91e89817-aca0-3576-ad26-ff9db5d18aee | -11.64837 | -58.26716 | 2025-05-16 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 94f449e3-a1c2-3ea1-aef4-7d6604fbc348 | -14.00842 | -53.04081 | 2025-05-16 04:57:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eff61f8-563a-3f6a-b2bb-708df9a1de69 | -11.3911 | -57.82882 | 2025-05-16 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae69aff9-6625-391c-8d26-b59c389caa5d | -11.66051 | -54.94615 | 2025-05-16 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc03fc55-147c-3ffa-b9d4-82df7c8a0304 | -12.12248 | -54.66043 | 2025-05-16 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 625dfce6-53ab-3696-bf1c-68a84da4d0f2 | -14.01719 | -55.13442 | 2025-05-16 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e4ba8fe-5f65-35a5-aa94-d9e37671eb79 | -12.03974 | -54.64358 | 2025-05-16 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d57ea38-084c-3d47-8643-aaa8f9a4378b | -11.91691 | -54.40874 | 2025-05-16 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c54c181-7c4b-3a28-b56f-431bebbacb20 | -23.07207 | -50.34804 | 2025-05-16 04:59:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba295017-9b59-35b3-ab0c-6c8fd4065488 | -22.04178 | -56.64618 | 2025-05-16 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c007a998-e5bf-385f-b2bc-6439e9deacae | -19.06298 | -53.45093 | 2025-05-16 04:59:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 634c4f14-cdf2-3608-a42e-06a525244a34 | -18.33458 | -51.45582 | 2025-05-16 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cc5619e-ffcb-333b-8b36-b741b88e2ded | -20.19051 | -55.04585 | 2025-05-16 04:59:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 249e0159-4297-3d48-a270-21b4c102fab8 | -23.42217 | -52.29944 | 2025-05-16 04:59:00 | NOAA-20 | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 635a8b4c-99b0-34eb-a50c-ff599394a90e | -23.28966 | -51.59719 | 2025-05-16 04:59:00 | NOAA-20 | SABÁUDIA | PARANÁ | Brasil | 4122701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8deee5b1-728c-3d1b-a19d-34a8133f4882 | -20.1911 | -55.04183 | 2025-05-16 04:59:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 153585d2-44fc-368e-900f-da536cceb0a5 | -18.33411 | -51.45956 | 2025-05-16 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c96fc1f-4d53-3ed4-b712-67a4fcf24390 | -20.58774 | -56.04944 | 2025-05-16 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d39f68e0-e3c6-3cb1-b48b-e81a54b12187 | -19.15475 | -47.81708 | 2025-05-16 04:59:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16709f82-54a6-3a9b-a3e2-4767048b2390 | -20.47688 | -53.67653 | 2025-05-16 04:59:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4dba07d-8a26-3fa9-a163-176e08554945 | -19.06667 | -53.45148 | 2025-05-16 04:59:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54ead109-f2ce-329a-bbe7-b8ef7890c3de | -17.4845 | -53.82232 | 2025-05-16 04:59:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 010fea07-bf75-3bf2-b01a-f4862abb2eec | -23.42264 | -52.29546 | 2025-05-16 04:59:00 | NOAA-20 | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a26d24bb-8dc7-35c6-a6fe-193b8739538d | -19.11336 | -52.70837 | 2025-05-16 04:59:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba4176e5-fcac-3bb3-80fb-9e5f5c462499 | -19.06605 | -53.45599 | 2025-05-16 04:59:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 220c89e9-99de-3bbb-a5fe-7cb33f69bc74 | -18.3307 | -51.46037 | 2025-05-16 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cb7686d-a75a-30c4-9fd8-fd60c08c19c1 | -20.18763 | -55.04125 | 2025-05-16 04:59:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40f99df3-da04-316d-87f5-01bbbdec8348 | -23.07676 | -50.3487 | 2025-05-16 04:59:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 28d8c169-27ba-3a08-9f6b-d8d5d2080aea | -20.18821 | -55.03724 | 2025-05-16 04:59:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71b0b6b1-29a9-30f3-ac2c-eb32ce90e965 | -19.05869 | -53.45487 | 2025-05-16 04:59:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d62dea3a-75b4-32f6-97a8-5f834b77f7f5 | -19.06237 | -53.45545 | 2025-05-16 04:59:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 92320b3e-e472-39f4-bcc3-276fc9040490 | -22.04514 | -56.64676 | 2025-05-16 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40acdd8d-cc7a-3e4b-848f-a355122d9459 | -21.5806 | -53.81203 | 2025-05-16 04:59:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f99f26b-8a81-3450-826b-6460476c8b57 | -17.48391 | -53.82647 | 2025-05-16 04:59:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7277eb67-6fae-3356-b4e2-adf411f8220f | -20.1096 | -55.23818 | 2025-05-16 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 559f0fcf-58eb-39e2-b168-04451741d6a3 | -21.13485 | -55.96796 | 2025-05-16 04:59:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d660067-0a0e-363e-b7e3-319c908dd177 | -17.48333 | -53.83065 | 2025-05-16 04:59:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e549ff41-4cd0-3d7f-9158-42543d1b74c9 | -19.16006 | -47.81734 | 2025-05-16 04:59:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2d7df91-225e-33d4-b3b5-7559d320092f | -25.1971 | -49.32344 | 2025-05-16 05:01:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f6a2e9bd-e512-3375-b0f8-6e0509b4b089 | -25.19369 | -49.32749 | 2025-05-16 05:01:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2db47e76-5dad-3431-94c6-a26104da3ab4 | -25.19163 | -49.32626 | 2025-05-16 05:01:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ea8ca075-f252-361e-99df-f4845a05d52f | -25.19915 | -49.32457 | 2025-05-16 05:01:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3b42b79c-1677-3ba4-afef-f51956533a34 | -27.11491 | -50.57371 | 2025-05-16 05:01:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 519512c2-1ffc-30df-9fdc-68fc763e2321 | -11.96308 | -63.51968 | 2025-05-16 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67fac602-d7b2-36a3-8bc0-5dc690a3bf0e | -14.0206 | -55.14317 | 2025-05-16 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62fda4b0-57ae-385a-8e56-d94d64212efe | -11.96628 | -63.52531 | 2025-05-16 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 76979ecc-ca77-374e-aa81-14c094eeab97 | -11.41976 | -54.32596 | 2025-05-16 05:50:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3842cd66-edcd-3655-b421-f38f6b280ea4 | -12.45836 | -57.2038 | 2025-05-16 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83f66ad4-984c-3d71-8212-a390c8caf6b9 | -14.0275 | -55.14403 | 2025-05-16 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d3bbe84-36e0-335d-b31c-421208309a48 | -12.36589 | -64.22567 | 2025-05-16 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0844e1a6-6e0e-309a-8467-9a8f9fdecf36 | -12.87374 | -55.05825 | 2025-05-16 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| baf93a24-e103-3c50-98af-e0f0470ebeae | -12.87305 | -55.06475 | 2025-05-16 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b013bd6b-0402-32db-a16e-fe3ee3a9e101 | -10.52229 | -59.38574 | 2025-05-16 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17448dd6-9595-3c52-9d24-2a9ac882d461 | -12.09835 | -64.2547 | 2025-05-16 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47cecaef-f86c-3550-b09c-5399dc08890d | -11.94007 | -61.99321 | 2025-05-16 05:50:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52fd186d-a649-347e-87d3-3e231ac0ed09 | -14.01438 | -55.13549 | 2025-05-16 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7513c77c-5e02-3f0a-bc9c-452611561165 | -13.95945 | -56.79979 | 2025-05-16 05:50:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cf0de18-d309-3da1-b155-86a9d39a9832 | -12.45508 | -57.20764 | 2025-05-16 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7cf27c76-cb8c-3208-9a57-e623b025e7c1 | -11.38927 | -57.8239 | 2025-05-16 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cb4db40-fb9e-3807-8eb5-e1149fa509da | -12.29792 | -63.72728 | 2025-05-16 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdcfef0e-e33f-3e0c-a29b-5955dc2e15c3 | -10.03959 | -64.97623 | 2025-05-16 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcc2cc54-9d43-3f83-850d-5b3974776037 | -11.42447 | -54.32845 | 2025-05-16 05:50:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b7a5859b-a536-3d52-8a97-36c75a137547 | -11.96699 | -63.52028 | 2025-05-16 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 63ec3c0f-2104-3515-890a-185ea3e860cf | -10.51726 | -59.38485 | 2025-05-16 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 234e5e4b-8213-3b6a-a60b-0706ea06eeec | -11.39446 | -57.82867 | 2025-05-16 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76b2a364-4153-3ff8-b1bc-caf58582cf3d | -12.45739 | -57.21262 | 2025-05-16 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c63589ed-0ebc-3854-b450-b77bdd2d793a | -11.91934 | -54.40869 | 2025-05-16 05:50:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87aaa598-bbf6-3ed1-9447-d32928b2748f | -13.96056 | -56.78952 | 2025-05-16 05:50:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05620959-d436-3168-8d9a-c50b5dc43354 | -11.42604 | -54.33351 | 2025-05-16 05:50:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b7f7588-7c43-3de5-aeff-7e5bfb915626 | -10.39369 | -57.53967 | 2025-05-16 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 628f5a31-e5dd-3c92-ad24-c1edbb6f11ae | -12.68511 | -58.1291 | 2025-05-16 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a60aaa79-ad9e-3cce-a445-9f26bb11f618 | -12.45788 | -57.20823 | 2025-05-16 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de7de3f5-a413-3747-9726-f3c9e0e58b0f | -11.89949 | -56.40988 | 2025-05-16 05:50:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0086b17f-cb5b-3c26-b649-752ea4166edd | -10.3932 | -57.54361 | 2025-05-16 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbdd2f60-1b96-39bc-8362-e9dd309d3189 | -11.4268 | -54.32681 | 2025-05-16 05:50:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c5be379-be00-3229-b288-eb0cb04a6c03 | -9.92618 | -59.92824 | 2025-05-16 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 116d729a-aabc-3ac4-8a65-de5a7dc89d6f | -10.52267 | -59.3828 | 2025-05-16 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a430231e-5fec-3c0b-8882-322924b318ec | -13.04422 | -53.7145 | 2025-05-16 06:08:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dcb06db5-e3b6-3b4f-8c92-fb340b6fd1d4 | -14.87211 | -51.98232 | 2025-05-16 06:08:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fe04a7db-229b-38bb-8920-ae520836dae6 | -11.15863 | -48.67573 | 2025-05-16 06:08:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9aaf5319-26df-38d0-9762-3aed11b1ea6c | -11.57902 | -47.61266 | 2025-05-16 06:08:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| ea920a6f-9c21-31b1-bb91-647e59911016 | -11.57289 | -47.60136 | 2025-05-16 06:08:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1c873476-bed6-3124-bf6a-64207b57926c | -10.3411 | -51.69236 | 2025-05-16 06:08:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5fb855d5-588a-3ee8-bb0f-a90d7d6d9af2 | -11.16021 | -48.68124 | 2025-05-16 06:08:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b75073fd-0948-36fb-8691-0e21e1c07324 | -11.1621 | -48.66679 | 2025-05-16 06:08:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |


[Clique aqui para ver as próximas entradas](README13.md)
