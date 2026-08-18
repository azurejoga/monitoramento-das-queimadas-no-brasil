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
| b35b57e4-8a60-3d5c-981e-1e742b015da7 | -11.38108 | -46.40076 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59e3415d-0cd7-34f4-a5c9-bba2aff6cbe6 | -14.49671 | -45.67656 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e13a677e-480a-363d-b4e3-6382599a82d6 | -14.35555 | -51.93202 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5d3a355-f53b-3df9-a19d-3400cc360140 | -12.26493 | -51.54108 | 2026-08-18 04:04:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be59b918-f2da-329e-b5bd-11163dd0f842 | -13.41228 | -54.33326 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae736f41-37b4-3c9b-b3ee-abcbfb5c2b3d | -12.39965 | -54.96384 | 2026-08-18 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50362569-3dce-3f01-b47c-38fceff8c24e | -15.06964 | -48.72521 | 2026-08-18 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66f3c83f-291d-3521-b19d-28ab58d2d8c5 | -12.70556 | -48.5177 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bed02fa0-a2b6-36bd-afc4-b1e8061a8d20 | -14.49749 | -45.67204 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bbe1d33-d501-3e98-b270-c0f4d44c5e68 | -13.5636 | -51.69721 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9db1e1a6-4fd9-3a9d-9355-0e4f8600fa25 | -14.8586 | -46.63631 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b947e216-9c1a-3675-895d-ac2b7d186c54 | -13.55332 | -51.69127 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43d3f08c-d8f3-3e1a-bf0c-9b94788efaf8 | -13.41351 | -54.32755 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83c39083-273a-38c6-b5e0-7bd2f59972dd | -12.52131 | -47.87868 | 2026-08-18 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b8ce74b-5f00-3037-9d67-06ae806d939a | -14.46032 | -51.83808 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87110d34-a5c4-32fd-9eaf-f5836a2e98c4 | -17.47646 | -48.87432 | 2026-08-18 04:04:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97ef2e2e-acf3-3afe-97a9-639972fb1b07 | -11.19941 | -54.81354 | 2026-08-18 04:04:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 66f1e6cc-950a-3a28-a089-90ea984386d6 | -12.25998 | -45.87552 | 2026-08-18 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0c21631-8e34-336a-9d3a-df007c39856e | -14.81219 | -46.64705 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 07e7cabc-c937-32ab-a179-8134529bf402 | -12.46599 | -54.18314 | 2026-08-18 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cee2e175-f9a2-32b5-9182-a05a5a63f583 | -14.16193 | -52.90765 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1d3b0f9-059c-305c-b4cf-e27436b297e6 | -14.36143 | -51.87598 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dca2d182-3137-38a4-8ba5-4f9054f2549c | -12.26084 | -45.87053 | 2026-08-18 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a0ffe28-f5c4-3744-9c16-c925ba55caa9 | -17.10937 | -46.57356 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d0bd2c6-5ec1-304f-bc23-64bd70a25e8c | -10.1199 | -54.28 | 2026-08-18 04:04:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e6b34e41-6d6a-32e3-98ac-903657edb19b | -14.25983 | -51.9249 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a5cbe08-4e72-323d-9c4a-e1a6328605b0 | -13.66764 | -52.19893 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 291aefb4-8120-32d5-a352-a12867dd1b6f | -17.45336 | -47.85704 | 2026-08-18 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d05cf3bf-9de7-3ca5-8a6a-f3eeb1844ec8 | -12.72077 | -48.4855 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 11305900-a928-3cd0-b0d4-d0581dac9678 | -11.33619 | -45.92121 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d5820e1-628b-3a2a-9fb2-00f0ed6f4106 | -13.4408 | -43.84192 | 2026-08-18 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc2dc11f-ce21-3079-a3b0-7d0aba51fa9b | -14.3566 | -51.87083 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df203957-8d4d-309a-9c1f-cd69716fd6d2 | -17.4567 | -47.86149 | 2026-08-18 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2545c4b8-33a2-37b6-8882-d66c8a877be5 | -17.0971 | -46.57373 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00fa37a3-90ea-3658-8430-cf6cf2f093be | -17.1025 | -46.56497 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93302329-5d21-3ef9-9748-8e9b59caf180 | -14.25907 | -51.92865 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dd41520b-9377-3f33-b098-64cd0b60991d | -11.12956 | -47.27595 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b07986f1-3bef-363d-ae6c-52ee2fbd1488 | -11.38511 | -46.4016 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb7ececd-3f45-36fc-a175-04171c8e0280 | -12.4005 | -54.95649 | 2026-08-18 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 53c8701b-75de-3282-b921-51e440bd2f3a | -11.5288 | -46.63606 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 41f9d759-7a22-37ac-ae0d-f67b685018bc | -14.17052 | -52.8954 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a6a8863-ca20-3102-b5d8-d74bd11b3220 | -13.40333 | -54.34335 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d458017-4677-3268-af8e-8de6291e1ee7 | -14.87901 | -46.63448 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9e5b9f7-56af-331e-9296-a877c2c3d0c1 | -17.98223 | -44.43671 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d0e40b6-09cb-3b83-86e5-683d8043f0fb | -15.38797 | -52.80025 | 2026-08-18 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36d47116-762a-33bc-b96e-78ea5f3f5c2d | -13.42002 | -54.32876 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f853610b-131e-36b3-907d-cf83ecd36f86 | -15.30326 | -56.44084 | 2026-08-18 04:04:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8eb6bd4-61f7-3907-b96c-4a82168ce804 | -14.17015 | -52.91761 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 088374d7-f27a-3e62-862a-f46363153830 | -14.35708 | -51.92455 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fe5ceff-796b-3992-9537-5a8058347f8d | -14.36134 | -51.87566 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce231107-da3c-3f99-b37e-be9a22f6b8a7 | -13.93673 | -53.93454 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54ae05d4-0bad-3b4c-a911-1004a8d4ec30 | -11.1214 | -46.49931 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c731c478-e94e-3bf9-ac67-aec57cc8f005 | -13.33444 | -40.48219 | 2026-08-18 04:04:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3ad0aa71-de41-3ac0-837b-09999739d118 | -10.56209 | -51.97391 | 2026-08-18 04:04:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aeb665ec-575d-3d37-9e44-8721e6ac0ba7 | -12.72083 | -48.48859 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 880eaf63-8d22-3b67-80f7-c4b8da6922a5 | -12.70011 | -48.52178 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8ebbd9f-554b-3d67-9783-4bfda8d01f13 | -13.57486 | -51.78509 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e422ff3-7b17-3620-afe1-c4eb9ba792c6 | -14.83453 | -46.63606 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c810632-faeb-30f4-9fa2-5fb7837c986b | -11.33792 | -45.91135 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 608492b4-d62d-30ae-bc1c-4d3b12258687 | -14.54859 | -48.15791 | 2026-08-18 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7e2ff1a-26d3-324b-bda8-9b5c9708c771 | -14.85001 | -46.63945 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72c63822-fef3-327f-9a6b-3f0ffe022f98 | -14.2804 | -51.937 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe4fed91-6490-3798-9eb5-91ba72323686 | -14.85778 | -46.64094 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 485c9c0b-5be1-3b7e-a5e8-1de8bb5517d6 | -14.30068 | -47.18011 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c16b9f61-cae6-3942-b1b3-c6316d9b7b9a | -14.84139 | -46.64269 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 787b3587-9a3a-38f6-a0e8-f8ac71da2a00 | -14.17694 | -53.06345 | 2026-08-18 04:04:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b86f4df-af41-3ca3-8baf-1bb4b62cdf1a | -14.16956 | -52.90015 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1a0fa91-6495-31b4-abe4-3ad146726fea | -15.43841 | -41.38892 | 2026-08-18 04:04:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fdb94400-efe6-3eb7-b919-7d791f3d5f5e | -12.5175 | -47.87632 | 2026-08-18 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa40f27a-282b-30b4-aff4-0b405969371b | -17.97946 | -44.43232 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3618ce9f-eabb-3672-9ef0-8f401df714c0 | -13.55257 | -51.69497 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9732c76b-1034-3115-962a-a0be4c0beded | -14.16103 | -52.91214 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2deac467-67fe-30e6-9320-acea1b5fc616 | -14.35823 | -51.92131 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd7b74c7-8281-328b-8c4c-f78fc4469442 | -10.77842 | -50.32771 | 2026-08-18 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37cff5ef-a2b3-36a4-ad11-c0faf9f95238 | -13.58008 | -51.75879 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecb1d308-61f6-358b-929f-f92f9eb606ac | -14.17602 | -52.91892 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a0426f56-5478-3210-957a-f5aa777737bd | -14.83753 | -46.64181 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e0a9c04-560c-3116-899e-afdbf36356d3 | -11.36278 | -46.38621 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7ea438a-45ff-35e4-9167-39dc6c720b68 | -14.83653 | -46.64738 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09b21770-f876-3079-9a81-bfbe75b7aed8 | -13.42731 | -54.38974 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6fdaf23-4474-3a17-92bc-7fe30248cb25 | -10.56474 | -51.97395 | 2026-08-18 04:04:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2818918f-9c3f-33e0-9760-89f1acab568f | -11.33796 | -45.91373 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e87d445f-97e8-3d94-b1a3-d8aa094c583a | -14.2606 | -51.92114 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7908c993-aec1-3aa2-832f-a863ca34f34b | -11.33713 | -45.91866 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d26b0cb-1b62-33ad-901f-360f531f9a07 | -13.50811 | -46.28352 | 2026-08-18 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd1654cf-1976-3bbd-a8e4-5db284eee327 | -17.98625 | -44.43348 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4deb2b9-5595-3951-8015-c9449a9b25f0 | -14.16681 | -52.91389 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 72f4b34e-298b-30e2-aa68-284ea75d3adc | -12.46361 | -54.19435 | 2026-08-18 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f4771bc4-db47-34c4-8be2-bc2a63efd5dd | -15.44173 | -41.38946 | 2026-08-18 04:04:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5b219a2a-8303-3338-9abb-62b86a0f98d7 | -17.98499 | -44.44115 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acb9a45f-f269-330e-8a30-8612695ce0ed | -14.03617 | -53.67982 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1a13f59d-8bd7-3d6b-a6af-9cad65dceb31 | -11.46893 | -46.56771 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01d54fbc-ae64-3f95-a954-ceb12fac227e | -14.2684 | -51.91103 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2546865f-ae50-3808-aa0d-a5b3c77a9694 | -15.07242 | -48.72861 | 2026-08-18 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d1629f2-a130-3ea9-81de-49ced87250b3 | -14.29195 | -47.20512 | 2026-08-18 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9e4f7ed-9a99-36fc-b532-72a88e6e9727 | -17.98349 | -44.42907 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae89a46b-30ca-38a8-bb31-e346541da567 | -11.37473 | -55.42268 | 2026-08-18 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2b61381d-e6d9-3fc9-8553-7146f10d4d10 | -14.17426 | -52.9274 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 63f53b22-350e-366c-8fea-07506fdc92e8 | -13.42607 | -54.39552 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9cd4c6b0-0c70-32c6-92b6-35122fc31007 | -11.71564 | -54.6334 | 2026-08-18 04:04:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README15.md)
