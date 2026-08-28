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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81c1f372-f8bb-3752-90c3-86e540c13794 | -11.70452 | -51.54065 | 2026-08-28 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 322bc871-662c-3464-a530-918e299e2b1f | -9.23277 | -51.54864 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 617265a8-26ba-392d-aa0e-e339d702b95b | -8.22382 | -54.95642 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c7f34bc1-dc89-3db1-a9ad-60e8fb5bebfd | -10.93333 | -50.53852 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 30dfa850-65b1-3396-828a-ca5ea09ac73c | -8.58979 | -54.75635 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 551bd782-6eac-3a7a-b210-60a3c4d19e20 | -8.33219 | -45.7212 | 2026-08-28 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49d6e9a8-4313-33ec-9805-c994c45b06e0 | -13.87018 | -54.11593 | 2026-08-28 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3ad8cc6-9be0-3d03-bbcf-57506f213dc3 | -8.03051 | -48.02096 | 2026-08-28 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da7f914a-f59a-3f04-893d-1f0d99ccab38 | -11.733 | -54.52863 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e663a9c8-47c8-37b8-8ce1-22f3cb4c6655 | -8.95152 | -62.40646 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba3ed997-5119-3051-b611-eee03c5b049a | -10.77689 | -50.63236 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5e33b62-57ad-3944-941d-d093a01ebbc7 | -11.23285 | -53.99588 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd99027d-bdf3-361d-81cb-8109683d793d | -8.7795 | -50.06279 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9ec79fc-b2ee-3165-869f-00b27ea762ce | -12.43343 | -43.40627 | 2026-08-28 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 10461279-9a4b-345a-85b2-ac057d18e566 | -6.84045 | -55.61475 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3e208e1-a381-3c3b-b1c3-270c1bc54e2c | -11.72106 | -54.5311 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e5322daa-e7bc-374c-8e94-9ad4763586ee | -12.26001 | -50.57967 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 1421aa9f-8420-3038-9a0f-042b8a1bab85 | -10.57804 | -57.48588 | 2026-08-28 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c77333f-82b0-3cf3-8553-a294a94fe1ff | -11.7285 | -54.53245 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51acfd09-48ae-3a28-b5a1-a370a5eab73e | -6.97999 | -55.63927 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92e4c8b1-bba2-3b8a-ac59-5eca1777b131 | -14.87177 | -52.63697 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c01b6df-34c8-3519-9b88-39e235244a34 | -9.86938 | -60.25993 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9e3c648-3e19-3634-b01b-8f9eeeb3c89b | -8.58895 | -54.76139 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93c5f64e-0757-343c-96a3-aa9cd1790513 | -11.64782 | -46.7308 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8be61901-b8c8-37ef-998a-1c8f101f63d2 | -9.44512 | -51.57555 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e10a352-a0e7-3925-8a16-f7b6c7024cf1 | -20.34263 | -47.59373 | 2026-08-28 04:53:00 | NPP-375D | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e83351a3-169f-3409-84c0-a05e5ed52101 | -20.82652 | -54.95199 | 2026-08-28 04:53:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ca5d7ed-5a27-3ecb-ba03-e30318355af6 | -20.43335 | -47.52557 | 2026-08-28 04:53:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 42db4500-23a7-3313-abe2-292431278a30 | -16.15155 | -58.60317 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 206f7c92-0494-3509-9c71-8776bb6d8c22 | -15.82094 | -48.09382 | 2026-08-28 04:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efd303e4-a3a9-3f84-9ee5-9aa8b6760129 | -17.94172 | -45.95208 | 2026-08-28 04:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67aa0a27-48f2-3aac-a227-6c7f4112b782 | -16.51859 | -47.73123 | 2026-08-28 04:53:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea406a52-aeb0-385b-89f8-9d97a105e228 | -17.25425 | -53.30716 | 2026-08-28 04:53:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82082aa8-e7b0-3def-9fb2-838fed6a40e1 | -16.16307 | -58.5915 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.4 |
| b9b91c8f-90ed-3558-8733-6b3c95790adb | -16.14719 | -58.59024 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cc9be982-7c7b-3391-9468-894c12370c02 | -16.15591 | -58.58065 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 898c5588-9b34-343e-9f8c-311ec42d115e | -16.42387 | -49.00764 | 2026-08-28 04:53:00 | NPP-375D | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 113c77b3-bcf4-31cc-8033-61563489191a | -20.8973 | -50.50276 | 2026-08-28 04:53:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 45af8545-6bdd-3825-8b73-2f43583465c1 | -16.51684 | -47.73261 | 2026-08-28 04:53:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf0ee895-31b9-3e0e-8c89-3b93531e2299 | -19.96877 | -49.9906 | 2026-08-28 04:53:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5ebcfa61-c698-3368-bc26-850245373af7 | -16.15687 | -58.59959 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| dc6106e1-06f9-3bf1-8163-e181afccbcce | -16.16394 | -58.58697 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.4 |
| e1b33b33-583a-3b8d-a483-f1303a807141 | -16.15863 | -58.59052 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.4 |
| 093d2f0d-c639-359f-b342-eabc8bfd0733 | -16.15418 | -58.58957 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 85e15f22-b2ba-307f-8314-66d8f51ec136 | -15.31991 | -52.75851 | 2026-08-28 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6034a788-3d73-39b7-b4d0-b3cabdda01c5 | -16.14799 | -58.59763 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 708d68cb-0dcd-3d04-859f-95a6c7ffeeac | -16.14887 | -58.59312 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 1e470351-a9c9-33b5-9c62-f523ec79ad8f | -15.76799 | -56.45292 | 2026-08-28 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7dd16f0-1c14-348e-81f0-8c6257575d8f | -16.16036 | -58.58158 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| 16b06cac-deb8-31b9-a34e-e78dc46d89ca | -16.71593 | -46.40604 | 2026-08-28 04:53:00 | NPP-375D | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7bca2a5e-1a22-3aa1-83dd-f8f1f6772229 | -16.16123 | -58.5771 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| 66cbec70-9504-325a-8b9d-79f3fb961743 | -16.79142 | -49.27359 | 2026-08-28 04:53:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ad05ed8-f93b-33dd-bae6-870abeb88ae2 | -15.76554 | -56.45076 | 2026-08-28 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bf4cae3-5f66-34ae-b35f-923b59e86496 | -15.34638 | -52.83443 | 2026-08-28 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86e414ff-6a1d-3535-ad29-b3c47d475aeb | -15.8215 | -56.42622 | 2026-08-28 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a2f3002-a53e-3024-8603-87f79629fe66 | -15.76895 | -56.44767 | 2026-08-28 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3e0818d-8221-3e84-bdc5-60b88e4ad5f7 | -20.41393 | -54.97079 | 2026-08-28 04:53:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7719ada-2b40-3636-9f21-af5165f971c7 | -15.51222 | -55.95217 | 2026-08-28 04:53:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5f265589-d991-361a-8290-f8a03950d0c1 | -20.4288 | -47.52887 | 2026-08-28 04:53:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed30e136-dcdd-3aed-908b-a40df4f0b2a5 | -16.46087 | -54.05923 | 2026-08-28 04:53:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acc8a551-4a98-30ad-8020-32141d65bf1f | -20.41737 | -54.97145 | 2026-08-28 04:53:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 554f97df-bf8d-3fac-81de-d46c78d0bb9e | -15.62474 | -55.9757 | 2026-08-28 04:53:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9ffb0679-88af-3efa-bfc8-5417ea3529ed | -17.77518 | -51.7233 | 2026-08-28 04:53:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8aadc263-8e55-3121-a746-7999b5d0b3e3 | -16.16567 | -58.57801 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| f2ac8940-74dc-311c-aed3-8062fc55d8ab | -17.59171 | -52.50013 | 2026-08-28 04:53:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac07d1fd-328f-3baf-b08d-40f46dfa35ca | -16.08187 | -47.91063 | 2026-08-28 04:53:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3348b320-d4b9-341c-a519-730384bbb4c1 | -16.15505 | -58.58509 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 63143753-c007-3d5d-b333-6b8a771942cf | -16.14974 | -58.58864 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 1b1504bc-7f95-396f-83e4-8e593c62e88a | -15.81843 | -48.09638 | 2026-08-28 04:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fcfdb561-4645-36a2-9098-4a7ec3719e65 | -15.7704 | -56.44624 | 2026-08-28 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea8c6b6f-b362-3cd7-ab62-da8613524bb4 | -21.08834 | -46.3427 | 2026-08-28 04:53:00 | NPP-375D | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3127187d-0a41-3fa7-a97d-7f85f83eac83 | -16.15331 | -58.59409 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 8dd785f4-296a-30d6-8b48-af84f32ffd95 | -21.08917 | -46.34106 | 2026-08-28 04:53:00 | NPP-375D | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3e908e51-48c8-387e-8e0f-0845156f6efd | -15.84495 | -56.43085 | 2026-08-28 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d493d63a-c18a-3096-a55d-486611d2faaf | -15.81724 | -48.09325 | 2026-08-28 04:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c52ae7d-2942-334e-ad73-42e4c4c2b8eb | -20.34216 | -47.59744 | 2026-08-28 04:53:00 | NPP-375D | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9694a552-6290-3428-b082-9c7d91504edc | -16.6671 | -50.16227 | 2026-08-28 04:53:00 | NPP-375D | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a50408bc-1d80-3502-88cb-11083f65c110 | -19.52939 | -47.6285 | 2026-08-28 04:53:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6ea088e-6b65-35cf-9554-018c08200fc4 | -15.62856 | -55.97642 | 2026-08-28 04:53:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7bf76292-2d7b-31f3-86e3-1d1aedf062ad | -16.16481 | -58.5825 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| cc26ce1e-9af7-33be-a5fa-f3938d1c2760 | -17.40486 | -50.81477 | 2026-08-28 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d0a6f2e-6f3b-3bed-81fe-c3fdb899131f | -16.15243 | -58.59862 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 3e659116-63e5-39cf-9e8f-c3a984e41cfa | -17.77851 | -51.72387 | 2026-08-28 04:53:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51ac3eac-9895-3cd5-8fa3-42f53b43cb91 | -15.293 | -53.1993 | 2026-08-28 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a0f34c2-1efc-39d1-8448-e6f0ee8186e3 | -16.67225 | -50.15135 | 2026-08-28 04:53:00 | NPP-375D | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b062870-b2d9-3b1b-b811-e67afece5c84 | -15.8176 | -56.42543 | 2026-08-28 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79b7572b-2894-3304-874f-67aa799ccba1 | -15.85068 | -56.42146 | 2026-08-28 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd038de9-5518-3d08-aeba-9ce54f07fb1d | -16.1595 | -58.58602 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.4 |
| 0e86eed4-14ee-3135-a6f9-3fc2d274df07 | -19.96781 | -49.99311 | 2026-08-28 04:53:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4e3b6dc7-7558-3caf-85bd-87ac575c5255 | -15.84036 | -56.45639 | 2026-08-28 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 242e3954-48a5-3b3f-9c8c-21bacb7ef128 | -16.14711 | -58.60217 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d82d15d8-a4e4-3964-b2d0-11fd65d7324d | -17.40824 | -50.81532 | 2026-08-28 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f747d062-42b1-33de-91b5-ae9841f154f0 | -15.62316 | -49.39026 | 2026-08-28 04:53:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f5f9a0f3-4e7e-35cb-96b2-b8f43d9c4f31 | -16.18094 | -45.6357 | 2026-08-28 04:53:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05ebc691-6e65-384d-b15d-a7f25468d4a4 | -16.67566 | -50.15189 | 2026-08-28 04:53:00 | NPP-375D | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 42748e29-47c8-3deb-8ddd-a30bed2c06b4 | -19.52541 | -47.6279 | 2026-08-28 04:53:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b4a976e-7bad-3e57-bbd8-de1bef3d0700 | -16.15775 | -58.59507 | 2026-08-28 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 5a2b9eb4-abb2-3224-8be3-da63ec15673e | -15.31655 | -52.75787 | 2026-08-28 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7c937ad-d108-351e-816a-f67b97152a2e | -26.5835 | -52.79678 | 2026-08-28 04:55:00 | NPP-375D | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b9948722-0332-33db-b1a7-ac0c9d097267 | -28.66526 | -49.89907 | 2026-08-28 04:55:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |


[Clique aqui para ver as próximas entradas](README46.md)
