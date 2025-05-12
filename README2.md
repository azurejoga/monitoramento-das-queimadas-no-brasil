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
| 33af210d-f1f7-388f-9444-9b8d5f15dd00 | -13.0481 | -53.72848 | 2025-05-12 04:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4133afb9-e529-39fe-a8a0-a7ca3503918b | -10.48435 | -46.18216 | 2025-05-12 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74812b13-350e-3b01-a54c-dfe57f3543d4 | -14.20085 | -45.47501 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbde5e66-fc5d-3f70-a64b-6f60e2284e8d | -14.19113 | -45.46933 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0156f0fa-ec3a-30cf-9b27-a4f590e4168f | -14.19804 | -45.47054 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66cbd63d-6e30-3e76-9048-576a70a59c65 | -11.01427 | -44.39315 | 2025-05-12 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83369ce0-2ee2-30c9-8c8f-0a2103c803c1 | -13.99701 | -47.96256 | 2025-05-12 04:10:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ac2b7e3-80b1-315b-bb73-598cb7b75f2d | -9.49124 | -40.35043 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9df8ef97-a2da-3baa-acf4-1198cd88f35f | -10.66516 | -46.65973 | 2025-05-12 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eaaacba-99e3-3f3a-9b55-b7c2c64d7091 | -14.20365 | -45.47949 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7558cc60-530f-37d1-900b-4cf545a7b299 | -14.19674 | -45.47828 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 446d3434-ed6f-3343-bf61-4373d30b3920 | -14.2043 | -45.47562 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e94a9b35-8bc1-320e-9218-1788c0fa76f8 | -9.49181 | -40.34667 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a8b0a014-715b-36f3-91ad-6fad782f9b2c | -10.49211 | -46.17636 | 2025-05-12 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ade99370-70ad-3674-a816-1ed88eb4d7e8 | -9.48837 | -40.34614 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9cfb3214-b1c2-3d81-9f6e-77fbdffe8222 | -9.49525 | -40.34721 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae2046a0-f8c7-33ce-97a1-66c3dac2316b | -10.73853 | -44.35229 | 2025-05-12 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bfa973e-f4e4-3fe2-8afb-45fa8d717308 | -14.19589 | -45.46219 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c16b33b-4190-3e10-9265-1b6c057f8462 | -9.49581 | -40.34345 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff3ea7eb-0ec4-3958-a263-b27c4a970499 | -14.55104 | -49.11281 | 2025-05-12 04:10:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bfc5adbf-7bc3-3bfd-b378-1bab5c3d6d7d | -13.04891 | -53.72439 | 2025-05-12 04:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2c4ef01-1164-3f24-acd9-f2fbe36febeb | -10.49257 | -46.17891 | 2025-05-12 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47eb3506-1eca-30b8-8d61-48206550972c | -14.19524 | -45.46606 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| febac0d9-c021-3095-a9aa-86a4a7dd518a | -9.49638 | -40.33969 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eb5f2b06-5d6f-34ea-adb8-4e97528c8a38 | -9.48894 | -40.34238 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| edfd6e22-e89d-3cbe-b66a-29c5ec307ff4 | -11.8895 | -56.41045 | 2025-05-12 04:10:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18357419-05f3-3453-8067-301aa0cf7f1f | -14.20496 | -45.47174 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 554d6aae-1c2f-3811-80c7-c248bd3a2f56 | -15.57022 | -47.85381 | 2025-05-12 04:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd1181b-63cb-3014-8cc6-b251c5f826a4 | -14.2002 | -45.47888 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49ada323-2447-3168-9bf1-f65313305cc5 | -14.54687 | -49.11203 | 2025-05-12 04:10:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d95ce35d-73d5-37db-92a3-37a9d21d9640 | -8.90577 | -44.78162 | 2025-05-12 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e23f13d0-fc6d-351f-9978-343ba83cf4d9 | -13.05465 | -53.72578 | 2025-05-12 04:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13f5c811-1c76-3e90-bf04-49061a5970a7 | -17.78173 | -42.80789 | 2025-05-12 04:12:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1ea1df5-056c-3c35-9bd3-1038d2a49035 | -17.77778 | -42.81108 | 2025-05-12 04:12:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36d6b416-b5b0-301c-9f6d-c61d7b28d92f | -18.19241 | -45.60703 | 2025-05-12 04:12:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1a9949d5-4923-38e7-9941-ebb8d2c2a12e | -20.31024 | -45.58162 | 2025-05-12 04:12:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3789820d-bef3-3aa7-b420-9dd5fa3a365e | -16.68128 | -43.88272 | 2025-05-12 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e750f0a-9312-32dd-9765-88eb86488ac1 | -15.76508 | -47.80132 | 2025-05-12 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51e940f1-7845-3a8f-838a-aa1160cd5581 | -17.77835 | -42.80733 | 2025-05-12 04:12:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af86b815-5910-3ecc-a0e0-e0ed5b4836ec | -17.74794 | -42.89444 | 2025-05-12 04:12:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de1f90e3-0064-34c6-9f2d-e9f2606cddba | -20.31299 | -45.58594 | 2025-05-12 04:12:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 072ed79a-641f-3905-8db3-9127c1469ff2 | -20.19707 | -46.72981 | 2025-05-12 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e265f103-d7d2-30e1-90c0-2373ca869af3 | -17.67699 | -42.74135 | 2025-05-12 04:12:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2673013-d69b-3f54-a688-b655343cb839 | -19.88277 | -43.95992 | 2025-05-12 04:12:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e7f65e29-71be-3b24-8215-e7d8e1271274 | -20.20049 | -46.73047 | 2025-05-12 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d68e5d9-2657-3839-832e-9e606f632ffb | -19.51272 | -44.27631 | 2025-05-12 04:12:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74b5bbc0-e01e-3b73-942c-8837443f622a | -16.70138 | -42.34912 | 2025-05-12 04:12:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 898b689c-1ac3-3d6f-8e54-8e590026c445 | -16.49662 | -43.13953 | 2025-05-12 04:12:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d5b327c-9b59-3a79-8fb4-aeec7d79ea5d | -17.09566 | -43.8035 | 2025-05-12 04:12:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e400856f-fe47-314a-ba80-4b04e583613a | -18.19579 | -45.60762 | 2025-05-12 04:12:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d8f5e839-ce13-314c-8838-432a86c4679f | -18.64993 | -40.58582 | 2025-05-12 04:12:00 | NPP-375D | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5d2bc63a-3cbe-359f-beae-dc2566758e3f | -19.85064 | -43.84429 | 2025-05-12 04:12:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 85042396-dd25-3804-b4b4-5278cc0bb611 | -20.17218 | -46.83472 | 2025-05-12 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1eaa4c53-9f85-3749-8a2f-3ea27b7f0b16 | -27.1708 | -49.00738 | 2025-05-12 04:14:00 | NPP-375D | BOTUVERÁ | SANTA CATARINA | Brasil | 4202701 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1f9a5d0d-a2c1-3902-a172-bfd9d415c4ff | -23.33775 | -46.77362 | 2025-05-12 04:14:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d468e01e-355a-36e7-afe2-1ff24c411ce2 | -26.93592 | -48.75484 | 2025-05-12 04:14:00 | NPP-375D | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 844ed534-5e73-3ace-bea8-c069e6910c90 | -23.98546 | -48.91896 | 2025-05-12 04:14:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb702d57-420d-3011-9083-57d77597f8dd | -23.21365 | -51.68655 | 2025-05-12 04:14:00 | NPP-375D | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5cfcd92c-e756-34cd-8ccb-acdb713ec4ee | -30.04059 | -50.75495 | 2025-05-12 04:17:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| e150994d-38ac-3fb1-8f0b-95d88803723b | -29.48739 | -51.97081 | 2025-05-12 04:17:00 | NPP-375D | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fdbeedf0-2b8b-3fbf-8d43-085a18c9de8a | -6.26364 | -48.51373 | 2025-05-12 04:29:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf4d247b-a796-3dd5-8b76-d332d47768f9 | -6.86403 | -43.22209 | 2025-05-12 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ba56c72b-8ce6-39bd-8690-b3b36ec5202b | -6.86306 | -43.22427 | 2025-05-12 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 194480ed-078b-3765-b4fd-0bbbe1093998 | -6.26697 | -48.51423 | 2025-05-12 04:29:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c1ad872-0c5c-3282-bd47-43fe09d264c5 | -5.34579 | -43.74531 | 2025-05-12 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 089b421b-c347-39e2-a637-45bcb2c26dcd | -13.04687 | -53.72335 | 2025-05-12 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d76b2db-37c6-3d8e-8db3-cbe780bf2184 | -11.40587 | -52.9477 | 2025-05-12 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed5ce182-1f6d-3a64-846e-add77100b83b | -11.40586 | -52.94964 | 2025-05-12 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a5c1ca8-840e-3a6d-a943-0c12bd333e0c | -13.04304 | -53.72263 | 2025-05-12 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1371aa75-0128-3959-a161-090a5c637c27 | -13.60291 | -47.96887 | 2025-05-12 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 148c22f1-2877-366b-9fc1-e5d55827b27e | -11.62488 | -54.93784 | 2025-05-12 04:32:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b84e15b-5e16-34a7-be6a-dbb3bc0ffff1 | -11.91424 | -54.40263 | 2025-05-12 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b77d2d2-80e8-3876-a287-b3f5c2226003 | -11.89676 | -56.41426 | 2025-05-12 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c758ef9-2878-3785-8164-ea66368984dc | -7.58967 | -45.86018 | 2025-05-12 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a277ebaf-eafe-385f-a1fa-0715beace711 | -14.19173 | -45.46385 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7fdac9a-9213-3e89-ba76-fce9253fe7e3 | -14.19932 | -45.46499 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d078171b-ea08-348b-9955-2c94506a2f49 | -13.05156 | -53.71925 | 2025-05-12 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7885b2e-45cf-3fdf-9d70-80cb843438ea | -14.19553 | -45.46442 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e26f3bc6-47d2-317b-995d-01430b3bd989 | -10.49028 | -46.17876 | 2025-05-12 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa14d5e3-4732-3cef-a489-8605ddc088a5 | -11.89768 | -56.40934 | 2025-05-12 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0990d4b5-eca9-379b-9936-062704c0223c | -12.17358 | -54.23622 | 2025-05-12 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24415225-9d33-3436-805d-600431ebe8e1 | -11.40666 | -52.94502 | 2025-05-12 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c4827c6-bac1-30d4-8075-588ff60b3486 | -11.89211 | -56.41338 | 2025-05-12 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4129c43b-5cc6-3bc3-bc7d-16f2d681240d | -10.88543 | -48.81836 | 2025-05-12 04:32:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df0e898e-f2ba-3e65-8744-ab8f1951fae0 | -11.89303 | -56.40845 | 2025-05-12 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cba678b-6b04-3d7e-acbf-cfb177e37fa5 | -14.65849 | -45.1315 | 2025-05-12 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d4f9185-8ee8-35d7-a60e-e3bc6a59bbf0 | -11.91832 | -54.40334 | 2025-05-12 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f701080c-3abc-3cb3-abe7-8935c44f38af | -13.99637 | -47.96094 | 2025-05-12 04:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 758a5cdf-212b-3773-8dd4-97b22074328d | -10.66307 | -46.65936 | 2025-05-12 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7cd82d19-82de-3940-819a-3c58dd328d4b | -14.19729 | -45.47921 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc157089-c83c-38f3-8684-59378d509036 | -11.91764 | -54.40269 | 2025-05-12 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd208cf8-1c99-3e18-9f62-a588fd50d07c | -14.20546 | -45.47209 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf0540a6-8506-3377-9b91-346760557e7b | -13.04773 | -53.7185 | 2025-05-12 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfe27a12-5b95-3605-930e-d003921449b0 | -14.20556 | -45.47559 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6499e36-3c3a-3e5a-bda0-30cb310836e9 | -11.40963 | -52.94841 | 2025-05-12 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5952f8cc-fde1-3c8d-a415-e551bcfea896 | -11.9136 | -54.40631 | 2025-05-12 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c3c9df5-5c4e-36a1-a472-c8dbf8a370fb | -14.20244 | -45.47029 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b7e1a21-c78e-3d2c-8af5-1df29fa0b427 | -10.66651 | -46.65991 | 2025-05-12 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a80a4591-1e05-3b31-871e-15a2f1e9b147 | -11.39161 | -52.94036 | 2025-05-12 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 042797ef-98df-3350-9cce-3dc9a7ed9eaa | -7.58621 | -45.85966 | 2025-05-12 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
