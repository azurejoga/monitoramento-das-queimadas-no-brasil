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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d91e876-0c8a-384d-ac0f-71e93535dc79 | -12.66857 | -48.21219 | 2026-07-26 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf5d76a0-07a6-33a1-8050-cd036950a9c8 | -9.53737 | -47.11255 | 2026-07-26 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bc5213b-89c0-33bb-b3b3-42c86fd18888 | -14.66071 | -46.95941 | 2026-07-26 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 980b3938-7bea-30f2-aa9a-a1bf226cabd0 | -13.6866 | -51.90153 | 2026-07-26 05:10:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e3fcfcb-0bce-3ec5-bed3-bc0c296ce05f | -11.58645 | -50.14394 | 2026-07-26 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73500ac9-6714-30df-aa7b-e4e1e66f2e04 | -11.01823 | -54.31922 | 2026-07-26 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db7583ed-3689-3e19-9833-1b8961415ed2 | -11.02831 | -54.3208 | 2026-07-26 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 459262b6-4248-3373-b969-0e0a8f5545ab | -12.03218 | -47.808 | 2026-07-26 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e8b94390-dac0-3088-9a6c-64e65712c98f | -8.83351 | -47.08035 | 2026-07-26 05:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 374b7771-ba03-394c-bb18-80e1154086b4 | -13.80241 | -53.86253 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ace9d52-d215-3aa3-a03f-94522d3f8a0b | -13.33867 | -54.29536 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86aaaf8a-2b96-3141-9b99-4589957627cf | -11.76643 | -46.57007 | 2026-07-26 05:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3156ee63-7416-320a-a415-574495574ad8 | -13.93041 | -53.88063 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e984d9f-f1d9-35cb-9faa-d635ee37365f | -11.58592 | -50.14771 | 2026-07-26 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1b2d003-1cff-3f94-96fe-f154311c84f7 | -11.01767 | -54.32281 | 2026-07-26 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65c03a92-26be-3be5-acea-24f1a9b81961 | -14.02995 | -54.07854 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42ffc9d7-8943-352f-92a4-93183a312792 | -13.69044 | -51.90189 | 2026-07-26 05:10:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19c17ac7-eb8d-3988-b660-5cccbfb49686 | -9.53167 | -47.11754 | 2026-07-26 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57849c55-b708-3467-9f97-a13c2db47f85 | -12.32243 | -47.17447 | 2026-07-26 05:10:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94e8f87c-a04b-3edc-901d-08a46639a1cb | -13.92752 | -53.87615 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e012946a-95c2-356d-8c11-4e674342009e | -11.30847 | -54.47535 | 2026-07-26 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cc323cf-a5bb-3d16-9dfa-e1fd60e05991 | -9.49048 | -64.08669 | 2026-07-26 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91ebfdb6-a3dc-318b-8360-2050b1d354cb | -9.92937 | -47.9053 | 2026-07-26 05:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd1fa75e-5107-398b-86ad-817abbbc4b4f | -12.5427 | -57.21633 | 2026-07-26 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78835b0a-9080-33f4-878f-84bbe94f683d | -12.53932 | -57.21576 | 2026-07-26 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9ec205d-539a-372d-a8c5-1955add327b5 | -6.57183 | -55.15088 | 2026-07-26 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf1fe8e8-6b8e-3cd6-b44c-cdabd7f93959 | -13.19686 | -48.32529 | 2026-07-26 05:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9be616d3-cd4b-336f-af8a-4da687fe34f4 | -11.58178 | -50.14711 | 2026-07-26 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c59f6c6-8798-3b44-9a97-78f07d7fd468 | -12.43933 | -56.54219 | 2026-07-26 05:10:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1446450-804a-3592-a60c-38c95ca1828a | -9.84128 | -62.21741 | 2026-07-26 05:10:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ada6139a-faf1-3423-a6ec-c9dffbe3b340 | -9.93499 | -47.90754 | 2026-07-26 05:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92fbc693-d4ae-3f18-a9fd-0713b2b816fc | -11.76112 | -46.56948 | 2026-07-26 05:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f3d9aae-8d1b-35e9-98e6-632561992e07 | -12.66749 | -48.21318 | 2026-07-26 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7a2a717-80cb-375d-b58e-9a4b7398608a | -9.83583 | -62.22125 | 2026-07-26 05:10:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95385211-2d8f-3ca9-9180-c5124caff8e8 | -11.84931 | -50.22309 | 2026-07-26 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bff7e90b-f788-37c9-a4d6-fcdec261811c | -11.59059 | -50.14454 | 2026-07-26 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02a77867-2e75-3f1f-85ff-f52f3827ce35 | -13.36763 | -54.28849 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8439e668-3308-3fd8-9b50-d100e1c084cd | -9.53661 | -47.1182 | 2026-07-26 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f41f4277-2c66-32dc-9f27-9b5a4fb8a582 | -13.803 | -53.85864 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cecf5185-69f7-3094-a3ef-f06e6e23ca27 | -13.20165 | -48.32603 | 2026-07-26 05:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c2e8c55-222b-3423-b066-f4fc319f4a34 | -11.02551 | -54.31668 | 2026-07-26 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98d01f13-b546-3f59-b1ad-d1a58c36e9c8 | -11.30791 | -54.47894 | 2026-07-26 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72ef99ef-4e68-3d9a-9e69-2203f387b46c | -12.32283 | -47.17139 | 2026-07-26 05:10:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78ed942a-957a-338f-9a91-ea7c2d235eff | -13.36024 | -54.29117 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5fabdf6-bef6-3364-996e-3a441fc82ab0 | -9.84042 | -62.22213 | 2026-07-26 05:10:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abbf685d-e201-392d-a75a-a7de08fcdae6 | -13.80359 | -53.85474 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5e98f04-a903-361c-a3e1-9cce2ae424fd | -12.77124 | -59.79068 | 2026-07-26 05:10:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa4b1019-9d12-3974-8bf1-580a217f6094 | -13.37103 | -54.28904 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da1ce109-cdef-3484-a81d-7e4a336e95fe | -9.53243 | -47.11186 | 2026-07-26 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 544fab8d-5e2c-3117-a594-7ea2062a2143 | -11.02495 | -54.32027 | 2026-07-26 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d15bcdab-113d-3471-bbfa-4b644a3b5dcd | -11.5854 | -50.15149 | 2026-07-26 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b06cd432-cc3b-37ce-ada3-feaaea19aedc | -9.73185 | -63.43006 | 2026-07-26 05:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e0c3627-5a4a-3d83-9335-289ab0e30bae | -13.80376 | -53.86156 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dc4f12c-e5b1-32ea-9d53-47263f59ca65 | -8.82785 | -47.08504 | 2026-07-26 05:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edfbd3a3-d7fa-3bd8-9f29-c70fafa4f930 | -13.19618 | -48.33068 | 2026-07-26 05:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa568c76-06a3-3559-9a4d-d91597c58e64 | -9.80194 | -48.92189 | 2026-07-26 05:10:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6bb5c3aa-8146-34f9-af1e-cfaac7ba71a6 | -14.03341 | -54.07907 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d50449ea-4d99-3139-951b-66d6615deb64 | -12.67228 | -48.2139 | 2026-07-26 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1aed7d70-74b1-3c4b-9fe2-d93a73658188 | -14.66111 | -46.95599 | 2026-07-26 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53b8c9c5-c810-3cbb-b95a-20fc35774c8d | -11.01431 | -54.32227 | 2026-07-26 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41f3c4eb-c02d-33c9-900d-310caef261b0 | -14.2804 | -53.38467 | 2026-07-26 05:10:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 67f2e578-92dd-3e88-b5bc-3c93441d6cbf | -9.94513 | -48.69414 | 2026-07-26 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d356028-30c1-30e2-aa56-8aa478c9bbca | -8.82861 | -47.07961 | 2026-07-26 05:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3d6ec7a-a369-3946-bfbb-4c2adb6ee7fe | -13.37444 | -54.28958 | 2026-07-26 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cfd5f60-b976-383b-8f8d-feeb8e42ec26 | -9.80252 | -48.91767 | 2026-07-26 05:10:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c19020a-1ceb-3f3f-9964-91e5253ed187 | -12.66271 | -48.21246 | 2026-07-26 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c812490b-9544-3832-89cf-80ecf6da291a | -11.15005 | -44.48244 | 2026-07-26 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fd91651-8bba-3b78-be1d-52808151d3ee | -17.27989 | -46.50367 | 2026-07-26 05:12:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c34c893-f2a9-3acb-abf5-14049255a70b | -18.02893 | -54.35653 | 2026-07-26 05:12:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23345cce-16fb-3843-a454-7f01f5961542 | -17.13049 | -47.21379 | 2026-07-26 05:12:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d87f92bf-97ce-3672-95d7-b4ca6c93db76 | -15.8126 | -56.72371 | 2026-07-26 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26f9c9f5-a290-3eb7-99cb-804216c1d316 | -15.40508 | -53.90322 | 2026-07-26 05:12:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04caaffe-5772-3321-ab4d-ecb8f3b28b12 | -17.38834 | -49.19557 | 2026-07-26 05:12:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 361bfb08-00e1-309a-8dd3-e492d073c2b8 | -15.81592 | -56.72427 | 2026-07-26 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0bc0780-0402-3520-9014-f269d9234274 | -18.49724 | -54.10013 | 2026-07-26 05:12:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d80379b-cd37-3df3-af7a-26e9d0b1abba | -15.28328 | -46.88334 | 2026-07-26 05:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e0fcf1c-8bb9-3227-936a-75e6ae566cd3 | -17.28561 | -46.50434 | 2026-07-26 05:12:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2aed04a9-8928-3abb-8a15-6f83797856b3 | -15.81867 | -56.72842 | 2026-07-26 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1902535-b6b4-3eef-88d3-1133bf1dc25f | -19.11923 | -57.76476 | 2026-07-26 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| aab919bd-e919-312b-8570-7e9c4df886b6 | -18.49302 | -54.1039 | 2026-07-26 05:12:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ef13220-434c-3f3a-b8e6-f527357aaa0b | -18.69607 | -44.55038 | 2026-07-26 05:12:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16347f9a-f949-368f-bd3d-8fa02ac6baea | -21.27723 | -56.03194 | 2026-07-26 05:14:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 008f693e-8c4f-3097-9f73-3ab57ef5b44a | -21.28065 | -56.0325 | 2026-07-26 05:14:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29628928-bd4a-32e8-8620-1359c071d2aa | -21.28008 | -56.03643 | 2026-07-26 05:14:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caff5d0d-18a6-3475-8d38-af28ec9d493e | -1.5281 | -52.62346 | 2026-07-26 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce743c74-2a1e-3835-9212-7b1381696aec | -3.24081 | -47.917 | 2026-07-26 05:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff46274b-5b15-355e-9be2-aad042752037 | -3.41382 | -49.11738 | 2026-07-26 05:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7c9fe4d-f717-398a-9a75-4748faf6cc1a | -3.24644 | -47.92359 | 2026-07-26 05:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 977836e6-312e-34a4-81a2-226f091da68b | -3.24002 | -47.9224 | 2026-07-26 05:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e082810f-a100-3e88-a7f4-2ab7720df4cd | -9.80167 | -48.91824 | 2026-07-26 05:27:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8ed7695-51d0-31b9-bb7b-4b3a74ff7ee7 | -4.41387 | -54.86445 | 2026-07-26 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 550868ce-b0d6-3ccc-bd13-bc1d1a3632c4 | -5.67565 | -49.8186 | 2026-07-26 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 267ee265-c5ea-36e0-8fbb-0e3ab178267f | -8.70118 | -63.67214 | 2026-07-26 05:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a6caa41-8822-324a-af51-1c4d54f8013c | -3.26493 | -54.87589 | 2026-07-26 05:27:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fdb1ec3-2f57-3933-a6b6-4588ad2ac9a4 | -3.72553 | -48.87886 | 2026-07-26 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 621a85e0-bc1c-3ae4-8679-768ddd1add07 | -3.79977 | -51.188 | 2026-07-26 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c28d4ff4-d51d-3aca-9e1d-8134e313a138 | -9.80097 | -48.92393 | 2026-07-26 05:27:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30fce47e-b0e0-3912-a701-0f11eadce953 | -3.73165 | -48.8798 | 2026-07-26 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce867b09-2fc0-3dba-bd7d-070902e1a9f6 | -2.98167 | -54.09362 | 2026-07-26 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef1afa49-fa16-33eb-9127-9a34582c4e52 | -3.80021 | -51.18493 | 2026-07-26 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README7.md)
