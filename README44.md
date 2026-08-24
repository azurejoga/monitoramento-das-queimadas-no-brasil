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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68ab96cb-94f0-3d6d-ab21-9c08f926dbfb | -13.18096 | -51.39283 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aa1b6bd3-fe4f-3635-8e57-d981aa4d1778 | -12.11211 | -50.60155 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 027cae7f-9b25-3482-9f5c-09992399728d | -11.91299 | -55.90449 | 2026-08-24 05:31:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 882a702a-4fe8-35ed-9d25-db90113011df | -9.90592 | -60.26423 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c51b46e-a1e8-33da-b1a7-71ee36c5f9d4 | -15.23028 | -52.78583 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c6a7582-09b9-38e6-be60-cb7a2d604803 | -16.41827 | -51.84647 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 17cfb095-92b7-3288-b4a3-757622749db1 | -10.80366 | -50.94723 | 2026-08-24 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2272b56e-c877-3be1-a9dd-421f2cc8fe80 | -15.3234 | -53.94324 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cb068230-34a9-3ec4-82b0-a9a7e4b65704 | -8.67935 | -62.84271 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64a4215f-30cd-3665-a496-111a5ccd5bfe | -12.12815 | -50.57902 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 970f9a4a-0c85-3b12-9451-c85e53e778d0 | -9.07041 | -60.43542 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 463b32c8-28c9-3798-8bc8-2624d3d50847 | -9.67889 | -55.09415 | 2026-08-24 05:31:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a85085a8-51a5-3620-b734-70361471dbc6 | -13.27512 | -51.43747 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c212251-db9f-3923-a27c-89b244bf18d7 | -8.82459 | -62.36685 | 2026-08-24 05:31:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c1cd4dc-118e-353d-9db4-aa21bcc8a274 | -15.49141 | -53.97975 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ac48c01-26b4-32f9-b455-7d629aff2642 | -11.60008 | -56.28831 | 2026-08-24 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84041f8d-394e-3517-b32d-95ab53c7639e | -9.59109 | -60.5108 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5d5fb2b-17d9-3ea7-a240-d1b277b627a3 | -14.32234 | -51.75896 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ee6d011-dbb3-32ca-9769-724976130897 | -15.27051 | -52.8149 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 623cb16d-0d3f-314d-ac97-a05303392fa2 | -9.87191 | -60.10117 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a3600de-15ca-3ca7-aec1-05b0d080c580 | -16.06277 | -50.44849 | 2026-08-24 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 864b8845-5609-3bd4-9337-f74e23cf2dc8 | -8.82399 | -62.34888 | 2026-08-24 05:31:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 131a5acf-dfa9-3c1e-8e85-9001c91b8610 | -11.6713 | -54.54484 | 2026-08-24 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d9bca27-29f2-3ed9-b618-da4059d95501 | -9.06635 | -60.43877 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfdb2ce7-526e-37a3-aa35-ced86bff89b7 | -12.13879 | -50.54312 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0614dd1-0fc6-3773-97ae-7b72d8c21d71 | -11.6047 | -56.28901 | 2026-08-24 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87c6d8e2-b911-389c-9f9f-c65079e747c0 | -12.09544 | -50.60405 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 49a038bb-312a-36c2-8001-a99370c5fd1d | -14.44322 | -51.80055 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5a5d531-4881-3dfc-8a1b-d2bb6777ef90 | -16.38179 | -51.82289 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8c2b4075-f6d6-38c9-bd6e-0c58790abbae | -14.5981 | -53.18304 | 2026-08-24 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5d650c19-910c-3a8d-9aad-1f18161090e7 | -11.67089 | -54.54802 | 2026-08-24 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac1afdbe-056b-31e6-9850-3463a8cb5e5e | -9.50884 | -60.50263 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bad71602-68e8-3cd2-a0b9-54b38036456b | -15.44166 | -52.84548 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c207d5b-6965-3131-8681-02971fa95506 | -15.65396 | -56.10517 | 2026-08-24 05:31:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03dc2ddd-2a6c-369d-9224-6ce378b14630 | -15.40781 | -55.77917 | 2026-08-24 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 83279fbc-17d6-30ed-b72e-2b480b932683 | -11.59945 | -56.29319 | 2026-08-24 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 273c4c27-284c-37a9-aac5-18fb8988f387 | -9.39843 | -60.58617 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86eee4f1-acd6-3bed-978a-18f0914d2577 | -9.2155 | -60.89418 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4c273d3-a5ca-358f-abc4-7a1aa9b6f392 | -15.27665 | -52.81525 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43cfc23b-c963-340d-b083-fbe8adc96b1e | -15.26643 | -52.85963 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d7fd56d-56d3-3ba6-8d89-ea2a4410cc99 | -15.34976 | -52.7719 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 249db7cb-4e7d-3ae3-bba1-20f8005aca1e | -11.91389 | -55.90012 | 2026-08-24 05:31:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08e17ae4-52ab-3642-a825-7cdc0c2e518e | -8.66005 | -62.83611 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ef3f588-a014-3545-b9db-f933838fa32a | -14.32847 | -51.75477 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3cc8bfcc-3571-38ed-8ab3-921eb4c8876b | -12.12176 | -50.55185 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8f3c4b6-ce1f-3f54-9c2b-0bc92e36c861 | -12.10149 | -50.61094 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| faf0b075-ffca-3766-9ce6-fee4f3e336a5 | -15.40817 | -55.77608 | 2026-08-24 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b22d94e6-45a6-3886-ba6b-4f3a8df7f63c | -13.17415 | -51.39661 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5ca7a0a1-64ce-32a3-b484-84318207e052 | -15.27753 | -52.81114 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 859942f3-d9a5-3910-bd3e-1270d0be24b1 | -14.41725 | -51.7872 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 26e7ca73-70a4-34b2-b916-3854622349ca | -9.97542 | -57.88491 | 2026-08-24 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60d1dea4-9fb4-3db2-be7a-394b629e96f3 | -8.66335 | -62.83664 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da1f818f-6848-3811-9260-66bf1e6bc321 | -14.44966 | -51.80132 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35c79132-4f4e-39e0-8b8c-8c1e71bc8099 | -14.41081 | -51.78643 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4b10d3f8-190c-3cbc-940a-9872c56520b7 | -12.08465 | -50.57811 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 91466173-968d-3c8d-a980-dbf5ea1ff566 | -15.50237 | -53.98506 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c86a8f96-8b1c-393c-8cc6-eac27ba02800 | -16.06216 | -50.45537 | 2026-08-24 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8796817d-79d8-374d-8957-19ada7aa83e7 | -11.91369 | -55.89916 | 2026-08-24 05:31:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1cbc8482-d9b7-36a9-b45b-840a70b49830 | -16.40037 | -51.82445 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 878bfd3e-bfc0-390a-8a5d-98dd9d28dc98 | -12.10889 | -50.60575 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c666a94a-5e83-3c25-af50-c239e652b7d7 | -9.67642 | -55.09577 | 2026-08-24 05:31:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c2535bad-1186-33e1-936e-b6ad800d33a1 | -16.41924 | -51.84716 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd7baaca-cfb7-3a9d-8482-c2123a6ced3b | -12.12658 | -50.5291 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7e63735-b260-3d10-9434-8ec5ba35f8dc | -15.26596 | -52.86424 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b06e3860-ccb5-3015-8379-02375613ef58 | -12.09678 | -50.59193 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 48b00aeb-fe28-3206-9449-4bc44d60b635 | -12.11092 | -50.58756 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7cf9cd95-db5a-3cab-b2c6-0b892e1784fa | -12.10474 | -50.60674 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| b7066299-ced9-3225-87d6-c70487ece535 | -12.11467 | -50.57726 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6fabe1e9-da76-3926-880e-29c987a6fc08 | -13.16146 | -51.3904 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5f874aed-3b2b-35e8-9aca-570c7ec95305 | -12.13057 | -50.53432 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c430500-1493-3cba-9282-cf9133b96af7 | -12.1292 | -50.54656 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f39617a-6600-3a34-bf42-be37d68bbaa6 | -8.67382 | -62.83472 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f735d89e-c7b7-3678-a40c-dfadbed855d0 | -14.25843 | -52.13715 | 2026-08-24 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 97d6b015-a954-3140-a584-19159042280d | -12.09072 | -50.58501 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 86b077ad-fa17-398c-b015-5b4d26c99066 | -9.14713 | -59.38076 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3496c01-3f76-3a35-b1a5-584d9533e98c | -9.40249 | -60.55908 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03a04010-9e12-3673-bc57-b2e6551b3805 | -9.38859 | -60.58073 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35bd4ecd-9495-3387-8000-b3490f757c14 | -14.30095 | -53.2145 | 2026-08-24 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d2c887a-e797-3afd-8fd1-2d25f5650228 | -13.17446 | -51.39202 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 11102744-d928-37d1-8efb-d842e260b5c0 | -9.39785 | -60.59003 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c7a824c-ba87-3784-84f3-bf79924d5fe7 | -15.32295 | -53.94724 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 64bdfbcd-a3c6-3249-9216-33b41177cc03 | -10.80397 | -50.94402 | 2026-08-24 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9cfe1e4-745d-3e15-bb20-e94b41411c95 | -12.13945 | -50.53698 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dee23d37-2d6d-3631-b8f3-d8438acfb439 | -15.33299 | -53.96079 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 172d3742-6dd0-3379-a888-49935d948ef2 | -9.27887 | -60.91469 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97a48b74-710e-3914-a88d-4f8356a2e222 | -12.10411 | -50.6128 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| ded80ac5-a0e5-3e1a-be60-290f1f34c7fd | -8.6755 | -62.84566 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e42cc6c-3a03-304a-9c6a-1a62cd2a243c | -14.34136 | -51.75635 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bebc8a29-b6ec-3320-b4a1-16dc35ce92b7 | -9.39496 | -60.58565 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90c0d48e-64ed-3bc3-9f00-7aa8c8805656 | -15.33254 | -53.9648 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4b9ed355-3ff8-3f52-8fe8-411c8c79ed63 | -12.08398 | -50.58416 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 973eba4b-786f-32ca-afac-f91b8014c3d3 | -11.6815 | -54.55412 | 2026-08-24 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 759284d7-5e8c-3157-88e3-c1a41e81b3f2 | -12.0577 | -50.57462 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb7538f5-e767-3e9b-ad9e-bb7826d66533 | -9.06983 | -60.43932 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0374998-854a-3db0-87b9-58fcb46fea10 | -12.10351 | -50.59278 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cdd30ce2-6335-3b1f-a17a-51ea07d90dc2 | -11.20813 | -55.04693 | 2026-08-24 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c21a992-7ae2-3e26-8b06-132118946f8e | -15.27299 | -52.85575 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49c06376-78e6-3f38-a3ff-b87fadb3d74f | -12.11756 | -50.61454 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 131d6385-521a-3fa5-9a9e-22ed1ed537cc | -9.40481 | -60.59106 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63e5c26d-60c0-3d09-980e-100ecb676382 | -9.18096 | -58.07059 | 2026-08-24 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README45.md)
