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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30179538-8bb3-3fb6-861b-32f559e5d427 | -14.33752 | -39.94594 | 2026-08-31 16:48:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 79fff0f1-2dbf-3069-bcd1-464a4ea371a7 | -19.1271 | -57.39378 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.9 |
| ecc79a57-6061-3101-aa5a-62a9fd16d1fb | -15.98839 | -55.9503 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 2ceaaef5-67ac-3654-b59d-4375e3118f2c | -17.2836 | -45.99594 | 2026-08-31 16:48:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 05d2ed7b-7114-3907-aeba-97f09c73fd45 | -14.32125 | -42.21995 | 2026-08-31 16:48:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| c2644b18-e94d-3be6-885c-cfa2473e1887 | -16.0007 | -43.54983 | 2026-08-31 16:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| c7964517-61ed-3921-9669-b26469ce4eb9 | -16.28624 | -42.57614 | 2026-08-31 16:48:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e9b7d0eb-48a4-3c4d-adc4-12b4b35c43dd | -18.26989 | -40.54994 | 2026-08-31 16:48:00 | NOAA-20 | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 44b08df1-109b-3c09-bc18-c20efeac09e2 | -14.62638 | -41.45953 | 2026-08-31 16:48:00 | NOAA-20 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e78e7d14-a21c-3169-b9ed-8d19a15d9000 | -14.48138 | -49.03616 | 2026-08-31 16:48:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8274afd3-3e25-3b2e-a54a-05aa79e99be2 | -17.71867 | -44.27299 | 2026-08-31 16:48:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b2200d9-a5ed-308a-a7ec-ddeb7b57e168 | -16.55515 | -52.51731 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 2636cd9c-012f-30a3-bbab-b7e0edca57e5 | -13.43186 | -39.87833 | 2026-08-31 16:48:00 | NOAA-20 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 968cff90-b7b0-3c99-9dba-d65ed85cf237 | -18.4171 | -47.96106 | 2026-08-31 16:48:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 6df85838-12f0-3d0e-aad6-b0c8ea571735 | -17.8714 | -52.11151 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 187.2 |
| f077095e-2dc3-3235-9cca-d23168cee33b | -14.45818 | -53.16273 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6bb2a40e-4dc7-378f-a713-94a88b641c32 | -19.23031 | -57.34207 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.7 |
| cee7c58d-3f01-3ac7-9c2b-4360e3ca2695 | -14.51477 | -41.17954 | 2026-08-31 16:48:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 79daf214-2794-3f65-8e3f-61b3e77090c4 | -18.40922 | -47.95452 | 2026-08-31 16:48:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 24ebe66f-5330-3578-8fb5-d193920f242d | -19.23465 | -57.34914 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.0 |
| 84ca7d21-6db3-32f5-9f73-8cee8cbb76f9 | -15.02012 | -48.17722 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 0a245e91-c6b9-3671-a6b2-80e99016ccab | -16.97416 | -53.2808 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 47f1f2eb-654e-336c-9838-8f7fa7866b14 | -14.59796 | -44.90973 | 2026-08-31 16:48:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e5ef2f3-2fdd-396f-9b15-fd463c3408b8 | -16.35455 | -51.00776 | 2026-08-31 16:48:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e939eaad-b48d-313e-a828-5d5413e3a098 | -19.17092 | -57.41222 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.3 |
| 2f03b6d3-c86c-399c-b4c4-35441ac446bb | -17.85821 | -50.49836 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 296.1 |
| 040f3d8a-fdb9-3c7a-90a2-eec73dc5e41f | -15.66972 | -45.9225 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 40996ee3-74a0-3e67-b769-f202690415b0 | -18.90909 | -50.87772 | 2026-08-31 16:48:00 | NOAA-20 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 0bc27cd5-7937-3b1e-beba-dfb97900adf1 | -19.10043 | -57.3992 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.0 |
| fb33fcab-94ce-3304-8689-291c79a6923c | -15.40769 | -52.71541 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c05a826b-d56f-3ffe-9870-bf4cdfa417ce | -18.39888 | -49.30907 | 2026-08-31 16:48:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9c872f53-2bf6-3d75-8c10-55f2f2f28d41 | -14.21482 | -48.64508 | 2026-08-31 16:48:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 281f4abe-4e3f-312e-b3ca-2e238d7735a3 | -15.11173 | -48.15537 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5c14a416-5cd3-3fa8-85a4-a674a0e61628 | -15.90186 | -56.21893 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 28bf2a94-7c49-3c05-91bf-659344081386 | -17.00065 | -51.8385 | 2026-08-31 16:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01bf5dd2-88fa-3535-a827-0d2b6a6f06b7 | -18.26357 | -52.71217 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 62a76221-d61a-3b59-8107-aefb7d8f7eea | -14.11384 | -42.13429 | 2026-08-31 16:48:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d453e994-316a-38a9-a565-f0dda2ef60cf | -17.22748 | -53.26874 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3e88da94-e1f4-3d52-9ca6-fc9548204e50 | -19.10462 | -57.38042 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| bf225a32-ab8f-381b-8378-dfeb84967d81 | -16.27541 | -49.02528 | 2026-08-31 16:48:00 | NOAA-20 | CAMPO LIMPO DE GOIÁS | GOIÁS | Brasil | 5204854 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1d7b624c-4b1f-3ac2-88f0-88cd187cdac8 | -15.41607 | -52.7146 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2b17b03-a69f-31c0-8c25-6e2179755b60 | -14.47797 | -49.0367 | 2026-08-31 16:48:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 3a642d46-fb28-37a0-b59a-abc5a415f2ad | -16.57696 | -52.51123 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fd94a0c9-2182-3835-b9fd-1bf447380c94 | -15.21511 | -56.36379 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5807dcec-0cda-351d-a663-a873d0b0fb4b | -19.11088 | -57.41385 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| f4074eb1-43e2-3a9a-b49e-ccfa57c3786a | -15.42927 | -52.68498 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 00256270-9a46-3a7e-9629-ceeab00c6152 | -17.13701 | -55.94207 | 2026-08-31 16:48:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| c346a6d5-3fdd-3da3-8f94-9df7b089e5f3 | -17.22303 | -53.26914 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90032025-834b-3d84-b082-ed37172be436 | -14.18957 | -45.30594 | 2026-08-31 16:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b507705c-8148-3fec-9ff6-c815932dda2c | -19.10726 | -57.40766 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 9486b7c1-9c1e-38dc-8c29-f40e7b4f7a7b | -18.92792 | -46.29414 | 2026-08-31 16:48:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f88f1917-0534-355e-9283-d9c51b6bb34e | -19.15435 | -57.36352 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 25a46d39-e5db-3593-9c52-f650fa725d7a | -14.46532 | -53.35217 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1b6f7b7c-d941-31b4-ac51-ee10475bfeef | -15.99361 | -55.94966 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 01495dfe-c18e-32a2-9335-bded8a401bef | -17.89529 | -52.10046 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 15372589-75b6-3632-a04b-12e0858f28fc | -18.90586 | -50.88337 | 2026-08-31 16:48:00 | NOAA-20 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 55d456ea-e833-3ca1-bfe5-e1bb731e4c54 | -16.56197 | -52.50436 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ed7bc51c-6bd5-350b-b619-36966a931c76 | -19.22276 | -57.35038 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 2f82b933-59cc-33ce-b6d9-c909a50e71c7 | -19.11608 | -57.37474 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.7 |
| ce93dc30-0293-39a3-8189-658795b3508d | -13.54809 | -48.23644 | 2026-08-31 16:48:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4a0ba2cc-a6bb-3555-aaf1-21cdef503602 | -14.39836 | -52.96517 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ad48d0b-95bb-3b1b-a6c7-8fe89265c4c5 | -15.87674 | -56.48028 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e512148d-11ca-302a-82c4-71eb365b0d67 | -15.42407 | -52.67728 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f6a7c274-a559-39a9-a62c-9735cdeae4c4 | -16.57327 | -52.51579 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| dc41e24b-839f-3299-a6b7-8be5a8839648 | -16.08138 | -48.02204 | 2026-08-31 16:48:00 | NOAA-20 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b6a858dc-2cb6-3a56-a586-fe1b76cbba8d | -19.13794 | -57.41374 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 13f36d7f-21af-3eca-8746-91fa72bc87ad | -15.00794 | -48.16419 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4bfa9fa-b8cc-3490-8f33-4f90068f268b | -19.08939 | -57.40952 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| ac49c9ca-668a-3067-a9dc-e81d18425655 | -14.5936 | -54.1109 | 2026-08-31 16:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8df36204-09d4-317d-9739-57c4237cc1bd | -19.24017 | -57.34397 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.4 |
| 6e650c9b-e5a6-3e0f-bf97-181813e351c3 | -19.12114 | -57.36507 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 222.1 |
| 4396f0a0-335a-3e10-9cb2-012c30e69d23 | -17.85132 | -50.50421 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a9414ca7-a4a3-36dc-8873-f7b5a0362120 | -15.49574 | -56.01488 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dfbf85b4-9100-3799-89ea-a0930fd24cdf | -15.46002 | -53.95785 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 13c48c6a-1bc8-339a-a2b9-93832ca2467c | -17.72145 | -49.2261 | 2026-08-31 16:48:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 58cf0b97-3b1e-37f0-bc1f-c030d631ce99 | -15.18714 | -46.2437 | 2026-08-31 16:48:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02a56641-45b0-3a61-b60d-89b3a1ecb9ae | -17.37611 | -44.88501 | 2026-08-31 16:48:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| dec8022a-a4fd-3e02-b7b8-68fcdcad68cb | -15.68655 | -56.10492 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0610480a-515a-32b4-be2a-6f5997e3768f | -19.20611 | -57.33996 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.7 |
| b441a688-340b-37ef-b758-11240b9a56fe | -15.03808 | -41.40178 | 2026-08-31 16:48:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 109e5b16-2477-3c40-9efb-3f37afbef599 | -14.95402 | -54.5696 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1c23f832-2575-3090-a0de-874842218f6d | -14.48532 | -49.03939 | 2026-08-31 16:48:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8e206a0e-5ffc-3cbe-963b-1e4fe3b29cb6 | -13.37455 | -40.35801 | 2026-08-31 16:48:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 3fe771c0-520e-3c48-8b46-2614c9bb3632 | -17.72556 | -49.22968 | 2026-08-31 16:48:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 329e45a5-9193-3b03-99c2-c50ea8e4b564 | -18.72077 | -44.50186 | 2026-08-31 16:48:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf89a563-7c49-3297-9028-956a89755f98 | -17.72758 | -46.85471 | 2026-08-31 16:48:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02c5d5a2-8b75-30e4-957c-32903ca11176 | -18.07122 | -41.27761 | 2026-08-31 16:48:00 | NOAA-20 | OURO VERDE DE MINAS | MINAS GERAIS | Brasil | 3146206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 292292e8-d3da-3176-937c-e3f3be526ad6 | -14.46647 | -53.32717 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c6db3de4-cf23-38ae-96e5-ad41677f1148 | -17.84554 | -52.10688 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 70ca7e8d-4bea-39b2-9d9f-d946f6e596e3 | -17.29081 | -45.99846 | 2026-08-31 16:48:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aec60387-6609-3c3d-bc23-a5e1dcee84fd | -15.98945 | -48.04025 | 2026-08-31 16:48:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2dd217ce-9573-353d-ae9b-082e7bf5c9cf | -19.18407 | -57.36044 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.2 |
| ce003ec1-c1c2-3e04-9211-9976226706b4 | -16.57277 | -52.51175 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 444bd21f-4bb2-37a2-8930-c695180e1e78 | -16.44028 | -51.4004 | 2026-08-31 16:48:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3f7a9c55-ff36-3f49-accc-f1a45c51cb3c | -16.68661 | -49.89833 | 2026-08-31 16:48:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 44b99891-aba0-393a-931c-5a7c0c074e7b | -13.54863 | -48.24001 | 2026-08-31 16:48:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3af2dc1b-b80e-3ee4-a07d-b9d323c53fd8 | -18.40978 | -47.95833 | 2026-08-31 16:48:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d8c9176c-812d-3ad4-b551-f2be1247652d | -19.16199 | -57.38102 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 099893e8-21d9-3f79-a76a-83d8f9a07ad6 | -19.17517 | -57.39341 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| b64521fa-ded1-3a82-8b44-726fdefbd4d8 | -14.82454 | -55.73417 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README146.md)
