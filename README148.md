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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2768d46-0fbd-3ad5-97cd-0ec1ee0ae3e6 | -10.45744 | -57.4913 | 2025-10-05 06:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f3bb1927-8d2b-34e3-9fc1-1492c73dd17d | -14.69193 | -48.33934 | 2025-10-05 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 44589f54-d159-3b22-bc66-10f787633127 | -13.73504 | -51.30769 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8ef23659-a8b7-3d4e-ab5c-1fc651957a42 | -11.24253 | -47.78287 | 2025-10-05 06:14:00 | AQUA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1245107c-6484-3176-8af9-8b0086247721 | -12.27118 | -49.20177 | 2025-10-05 06:14:00 | AQUA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e6994b65-4fe1-3df5-9ad5-dad81f594a36 | -12.59172 | -48.15879 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c73e7167-87e3-337f-b076-22fffd8e54df | -16.03423 | -51.05779 | 2025-10-05 06:14:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bd9afcbe-f38f-390b-9075-50ee30a778cc | -13.16047 | -50.88902 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| db492f5a-57b9-3582-b7c7-9b3140445891 | -18.16277 | -53.32186 | 2025-10-05 06:14:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 82e572b8-7b04-3eee-a921-be17b1403ad4 | -13.25333 | -48.47998 | 2025-10-05 06:14:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c67af897-4dd0-38fc-a17d-36c4bb55bf45 | -11.59372 | -46.70676 | 2025-10-05 06:14:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f301f881-05b2-3fd6-96ad-9ae06bb6ea6b | -10.36235 | -48.15975 | 2025-10-05 06:14:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 27648793-5351-3c22-8278-60be0fd68678 | -11.3969 | -55.16496 | 2025-10-05 06:14:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c86af3e8-8a71-3127-b810-3e834a15dc05 | -13.28703 | -47.61654 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1b66b4d5-0119-3483-b264-fe5608781772 | -12.57169 | -48.15598 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 33b5dcd9-5538-320e-a8c9-4844e1bfb251 | -17.95386 | -57.55307 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| a26cd4f2-a30d-380c-a1af-327a89555aed | -13.48149 | -47.28283 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3b94a741-fa10-38e1-85cf-7e5dbb7c4abd | -10.95203 | -47.05645 | 2025-10-05 06:14:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c70f7215-8446-3c7d-b896-7cc81906e885 | -15.98137 | -50.9081 | 2025-10-05 06:14:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 61919af0-feb4-3ee3-af56-d67341ddfcec | -18.25547 | -53.32392 | 2025-10-05 06:14:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b68f197c-3d30-3746-b386-745ee1c42d1c | -10.01395 | -48.295 | 2025-10-05 06:14:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d86e6906-9558-3e3f-9bed-7fdc9a1ac6e5 | -11.12044 | -47.17178 | 2025-10-05 06:14:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fef9ebf5-7df6-378b-8915-935a548fc555 | -10.57376 | -48.68551 | 2025-10-05 06:14:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5a7414c9-8639-31b5-a2fe-6010ce97a4c9 | -11.86905 | -56.88012 | 2025-10-05 06:14:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 5d89a4b7-f405-31d1-9fa7-0dd3c6b2b757 | -13.27643 | -47.61572 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2494ea8c-3382-3ef5-8eff-9d66e0534b16 | -11.80743 | -46.8398 | 2025-10-05 06:14:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| b97b6fd2-3e02-35e5-960d-c395a6cdd1e8 | -14.92302 | -46.84241 | 2025-10-05 06:14:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 77aba9e4-4fb0-3805-8bf5-fe520e916f12 | -15.23479 | -49.74223 | 2025-10-05 06:14:00 | AQUA_M-M | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0fe1a026-f57c-362c-8ea6-1a9282d64224 | -11.80466 | -46.83413 | 2025-10-05 06:14:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| d99ec465-022e-3c86-81b9-71c89c79af7b | -13.31959 | -48.06493 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 33.7 |
| efa1a3b2-2041-3385-a86c-7811dd677a16 | -17.88146 | -57.62757 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 7e40fc9c-cf81-3d83-b54b-76611ea7ff36 | -16.37075 | -51.4699 | 2025-10-05 06:14:00 | AQUA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 71d6ab46-829d-397e-a2ff-11ebdf007632 | -11.81654 | -46.85491 | 2025-10-05 06:14:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 161d95b7-5a46-3f29-97af-3105a17fe1b6 | -13.2572 | -47.59887 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7e600be9-cc80-39e2-8127-4d0d23bf1b5e | -14.56833 | -52.46632 | 2025-10-05 06:14:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a1f93126-5c26-3164-a4bd-c6e1a7dfbc15 | -16.08317 | -50.90956 | 2025-10-05 06:14:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 81d3159d-a385-3acd-92fd-70bc42b1d26b | -13.26763 | -47.60114 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5183ca14-9d59-30f7-af46-b74b645c37d2 | -10.75862 | -46.60931 | 2025-10-05 06:14:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| eaf9d834-5608-3eec-9943-9620ac68c01b | -13.28166 | -47.57595 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 2d666161-0838-3429-bc6b-228394b984ed | -14.33219 | -47.68106 | 2025-10-05 06:14:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| ac16a4bb-61e0-39ed-8fe7-79fad017c0b3 | -15.91232 | -48.83112 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 239eb9fe-7bdc-31cc-bb23-9f09783b9311 | -13.35683 | -47.57635 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 8bdf6011-c290-3460-b2de-99ad13f3b0df | -11.11508 | -49.85914 | 2025-10-05 06:14:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d58f248e-037e-360f-9840-2eabb2caa158 | -13.13658 | -50.86679 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 897876fb-91a5-3e46-8934-89e6e257cdd1 | -9.33583 | -54.52077 | 2025-10-05 06:14:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 0851bebf-5d0c-30fc-ac05-86a8c09666db | -11.75995 | -44.73626 | 2025-10-05 06:14:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 3df46d4b-c45c-35c5-ad46-a82582f8d038 | -14.70045 | -48.35305 | 2025-10-05 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 68db41d5-d631-3670-8603-fce4d258a44f | -13.26136 | -47.60626 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| bad535d2-6d08-3cd0-86b9-b614e0021e04 | -12.60829 | -48.11277 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 1a3bda08-b9b3-3eb4-ab0d-9bd51fe45e57 | -12.90113 | -47.31426 | 2025-10-05 06:14:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f4c9d22a-a026-3e08-a4dd-470f5525df35 | -18.25862 | -53.36237 | 2025-10-05 06:14:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ed727afc-e0c1-3ca7-9e73-89feba6f2083 | -13.7331 | -47.95697 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1bda7253-ef27-3dc6-abc7-09e9aec10196 | -11.45945 | -51.5166 | 2025-10-05 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2c8ed155-e604-36e6-8344-dfc7234153e7 | -13.09427 | -47.91924 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6d377c0d-0146-3111-a635-9a3714685883 | -17.94825 | -57.58479 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| c41bd093-597d-383a-b9bb-d99570e40204 | -15.22649 | -49.28618 | 2025-10-05 06:14:00 | AQUA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 7b407eff-669f-3fbd-bf02-75215ce21140 | -13.29754 | -47.6181 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 416a1dd7-c2b7-30fd-b42e-bc395b686cbc | -18.25264 | -53.3424 | 2025-10-05 06:14:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 3aec5bc5-3c2b-393a-9993-988bb88cf45c | -13.33678 | -47.77821 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9c229c25-037c-39ed-a2b8-e91d9021147d | -11.62692 | -47.738 | 2025-10-05 06:14:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b06ea05a-f46d-36a5-93db-b158fd41573b | -10.94598 | -47.06215 | 2025-10-05 06:14:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 5af1dbca-956f-3c02-8b28-82ac5d1e8c88 | -11.45065 | -51.51525 | 2025-10-05 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f9105d51-aff4-37b2-896f-618815dd6639 | -13.72797 | -48.07166 | 2025-10-05 06:14:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1a9f25f2-db59-3edf-b9ae-01b7316dd6f8 | -15.58787 | -52.50151 | 2025-10-05 06:14:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5ae4ceac-5f9c-3e5f-b398-646d9b581f49 | -16.00905 | -50.84401 | 2025-10-05 06:14:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cd669b2e-c91b-3056-ad3f-90a1ae15f1e2 | -11.53446 | -47.6695 | 2025-10-05 06:14:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9e95f074-192f-3247-94b9-b0734fb16575 | -10.93623 | -47.0944 | 2025-10-05 06:14:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| f0775d81-d699-3bfd-856b-c5096708acf8 | -12.59501 | -48.13493 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 07e9ad19-d753-3d6d-895f-45252f0c34b7 | -13.1441 | -50.87724 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a8c62fb1-dac8-3b58-9708-32d86e868dd7 | -15.57715 | -52.45325 | 2025-10-05 06:14:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ebb782f5-b844-3aa3-bae7-ff982a914e1f | -13.26432 | -47.62642 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 65ecc7e2-34a5-3b5b-bf40-ea46490cac7d | -18.18497 | -53.35416 | 2025-10-05 06:14:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 411d03e5-4dd4-3201-aede-415d65728757 | -13.09298 | -47.85183 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8d769c6a-f34c-3962-8376-8f4dcb426bad | -13.26086 | -47.81338 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 02893ca6-e17c-385c-818c-b1d7c493b400 | -11.07262 | -47.90207 | 2025-10-05 06:14:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| be75a923-237b-345a-809b-7069a034685c | -14.88757 | -48.25136 | 2025-10-05 06:14:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fb746aa1-cfe2-3446-98bf-23305d98a6be | -13.15777 | -50.90723 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 4f3a6940-8f0e-3d61-9e25-7068f306a25c | -15.55192 | -46.83635 | 2025-10-05 06:14:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d9629a49-d4b2-330b-8fad-769a10f2202f | -13.26594 | -47.61403 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e3475dda-4d55-3453-ad8c-9b5d7dbff3a7 | -13.12667 | -47.97775 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 9eecb107-4e74-3d03-bd9a-0939878a77bb | -11.52428 | -47.66787 | 2025-10-05 06:14:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| e4dda21b-22c2-3bda-8146-3c905974718d | -15.59805 | -52.49382 | 2025-10-05 06:14:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 53071261-bd17-3611-b303-a55843edbfed | -10.35109 | -48.16956 | 2025-10-05 06:14:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b44fdd37-ace8-3f90-8028-5f1136c0953e | -11.87193 | -56.86339 | 2025-10-05 06:14:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2634c952-d781-3c7e-afbd-c066d767772a | -13.14891 | -50.9059 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1c05b768-674b-39dc-9d66-89fd264bcc48 | -10.01537 | -48.28501 | 2025-10-05 06:14:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9d763747-15b7-3b39-bac6-3a0e990c58dc | -17.9766 | -51.13971 | 2025-10-05 06:14:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d878f08e-a57e-3341-9f18-f5cd9667fea6 | -13.47922 | -47.27642 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a7d2886c-7fe7-3054-aaa9-50f0afa57686 | -15.98001 | -50.91758 | 2025-10-05 06:14:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 68ecffc8-2ded-3140-88c9-859407ac1149 | -11.0114 | -46.69218 | 2025-10-05 06:14:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3cae98ea-fab6-3697-b903-c71e1a9230d4 | -14.68871 | -48.36316 | 2025-10-05 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 755b6f72-d27b-375f-aa0b-8f8895d8f3fd | -13.13523 | -50.8759 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 319.5 |
| 2bb22fe9-2fc7-3a72-bb93-c88cf8b3ac16 | -19.01173 | -50.59757 | 2025-10-05 06:14:00 | AQUA_M-M | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 39c07635-bb29-3971-9b14-f5a336b98cc5 | -12.97285 | -51.04038 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 86c00648-e9ba-35b9-84d2-53f0860a28f3 | -13.26316 | -47.59317 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 63a9f42f-dba9-3bc2-bb1f-2f0fbeb63746 | -9.32756 | -54.50667 | 2025-10-05 06:14:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5118a9e1-c969-38cd-b483-c9ead5f6e55b | -14.58737 | -52.46 | 2025-10-05 06:14:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ebb674a0-c236-3b8e-9788-d64d5bfa3d1e | -10.84925 | -47.96545 | 2025-10-05 06:14:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d8faf628-1617-35d4-bdc7-9906e2e62cb9 | -12.825 | -46.8561 | 2025-10-05 06:14:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b101aa8d-9cb8-304b-bfe4-dfb3a1c15ddf | -13.13389 | -50.88501 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 315.4 |


[Clique aqui para ver as próximas entradas](README149.md)
