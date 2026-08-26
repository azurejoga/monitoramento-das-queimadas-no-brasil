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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82543469-c66d-39bc-9cc9-558df3fbb9e5 | -15.34228 | -53.87349 | 2026-08-26 04:53:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1f62ff2-242a-34f9-b8e4-e628dfeca08e | -13.66616 | -51.84846 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c72d764-1943-354a-9f41-60139b131139 | -11.6416 | -47.15755 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc081774-28b5-36e4-9c9a-dd3166c30731 | -13.23758 | -51.41191 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8986ad9-b3cd-3e71-9d0f-b30e0abf2f6a | -9.96815 | -53.94324 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dc85463-addf-3965-a88f-4157cf316c91 | -9.48472 | -56.92044 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5fbe5cb-33d7-3cf9-8b97-01ce9460d82a | -13.87251 | -54.08836 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 105f5075-12f8-3c49-86d5-14c1362aa083 | -14.30001 | -51.1127 | 2026-08-26 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6245bcce-622a-3df4-896c-e15fb8f204aa | -10.77133 | -54.02661 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c584376-0cbb-3218-985b-bb611d275abc | -11.19937 | -55.085 | 2026-08-26 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5559ad93-f0b0-366c-a60f-92ad7ecfd28e | -13.86341 | -54.0363 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8a75335-b169-3604-823c-591c69cc821b | -9.66412 | -55.13457 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01424435-c01b-39ea-8fef-422209429f25 | -12.89763 | -59.91703 | 2026-08-26 04:53:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b68933d1-38bf-3814-b576-9b6d4b2a93cb | -13.85619 | -53.99504 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 272c4ddd-9cdd-360d-9d32-f08c373ccb2f | -9.0973 | -59.40308 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3ab025b-2bf8-35f6-8081-afe7aea5774b | -14.32279 | -51.72672 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 632d53fc-062e-3d5d-bb0d-a93b716d2aa7 | -12.73459 | -48.373 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0320c713-fd9f-3ab3-9f28-aec71d34961c | -10.76414 | -53.98599 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ef11da9-e266-3325-81c3-2130fa222464 | -11.28391 | -47.07362 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 302ff321-bf97-3fd9-9f61-939a9cd1559b | -13.65872 | -51.8438 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b28893ad-ace2-332c-aec1-24a0b2ffe982 | -8.82157 | -62.33307 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad69c37a-2054-3778-953b-c46ea323ae9b | -14.79831 | -48.80075 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 177c112d-c1fd-35e3-83b0-2d8a07a7abdb | -10.44066 | -61.2258 | 2026-08-26 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 734c7396-fe94-3927-b9b2-35e78a507f65 | -9.99931 | -53.96247 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b0c518-3c4b-34e1-80b7-95e1ee704386 | -13.24813 | -51.51394 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8fbe8572-ada5-3266-90b7-0649b81cddc7 | -15.58118 | -53.14128 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b83fc95c-e417-3538-97a4-dfb39c467f64 | -10.16348 | -55.30598 | 2026-08-26 04:53:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba3c45b1-d0a1-3f56-a833-715b907f8e75 | -14.13553 | -52.3535 | 2026-08-26 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 238333d4-0cb4-3c97-903f-c96d88f4a3ce | -13.24754 | -51.51801 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 832efd80-0076-3b7f-bcb8-32ef40fff1fa | -11.16275 | -54.0036 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f4f0d61-ecbc-3f97-9881-119dd5fc4679 | -10.30101 | -49.95929 | 2026-08-26 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c2ddfe2-3585-337a-b082-b790375f6693 | -13.66674 | -51.84446 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03c7ddba-3d97-3ef9-b3f4-460a085ef4f8 | -14.55412 | -52.32048 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1570b6c-c2d0-30ab-8ac3-0c39f4480321 | -10.76692 | -54.03308 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9ce81446-b002-33b1-acda-8ffe7a497203 | -12.63968 | -48.40866 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a512fce-4248-39b1-9730-27420c28cc26 | -11.16109 | -53.99256 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25ad5543-b927-354b-8d26-e22ccafadf2d | -9.60888 | -55.11045 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b4e6da05-ad12-3215-b232-7d2a54281a0d | -11.01862 | -45.07188 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e41dc250-8f0f-3341-8ae5-07d64e74c3ab | -15.60037 | -53.10567 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 43505f9f-cff2-3e25-9026-dea4ba34c4e6 | -12.69219 | -48.40061 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77b892b6-9bba-3286-954a-411dc251fc21 | -11.50027 | -45.06073 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1d1d01f-58e4-3060-8250-788247c5c1ca | -11.80765 | -47.66753 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7ef0101-b52f-3474-9db6-dc1c0b1102f1 | -9.48543 | -56.91608 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31b8a559-b156-32e5-83b0-248268c8350d | -14.53792 | -52.28596 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12f73988-91f3-3b1e-859f-03e652732c35 | -13.34789 | -48.23248 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cf20bd6-4625-3920-a985-21d7904ae5d6 | -13.25243 | -51.38469 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 811ecbf7-c3db-3138-8c58-c61ace47cf14 | -13.25659 | -51.38111 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c5e5e2f2-b23c-3056-a687-1363c0e5d91b | -8.82098 | -62.33635 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49497a5f-6337-3480-8b2e-72cca9eebb40 | -13.35263 | -48.22969 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abee0df3-9e81-3c5b-b990-60d9858af681 | -15.6856 | -53.89491 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4ab7678-0456-3690-b91b-2de6397c49e2 | -13.1859 | -51.34079 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1ab5a1bd-eb40-32a1-a266-fcd348204430 | -9.48909 | -56.91675 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59ba6ab3-6143-3f4b-9cd6-9a651889ddff | -13.60418 | -48.99094 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55a0a0a8-aa49-31da-8fdd-a796ac337b41 | -9.20266 | -59.57473 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d85b2aa-c3c7-38a5-9de9-304d7b140d34 | -7.90321 | -63.68362 | 2026-08-26 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a214ed1-45d2-35d6-93b2-7b162a6736a0 | -13.85735 | -54.05351 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bea464b-4fb1-3755-896d-b6991c22b322 | -12.76077 | -44.25316 | 2026-08-26 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce9674b7-a439-3822-ba6f-132e8663e217 | -12.7659 | -44.25764 | 2026-08-26 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79ed382b-c664-3bf7-b0a8-1f8a82d71e28 | -9.66074 | -55.13401 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41dc7b75-2d65-3223-90ab-3f710d053fba | -11.15944 | -54.00307 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17e65389-48f8-369e-86af-f1fbadc846b4 | -11.12012 | -49.88157 | 2026-08-26 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fd329f8-6c00-36d7-864e-da8bb0d02443 | -12.02592 | -46.02715 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21546331-3ac0-3d45-bcbc-3c6946a4dfcb | -12.6639 | -48.41983 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 88536162-5155-38f7-b05e-9f4ed8d270d9 | -14.35885 | -51.7532 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 750ba155-cbcb-3f53-b59f-d8144a5e016d | -13.23398 | -51.51178 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff9b91ca-bcf0-3bcc-a89c-f32b3d8f1924 | -9.60828 | -55.11412 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ca4ed7f1-2b51-3b57-aae9-ca9b67c5f1ea | -15.57951 | -53.15257 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f15586c9-59e8-3119-8744-6eab1f1f7ffd | -10.99114 | -60.79094 | 2026-08-26 04:53:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98fc1ad5-664d-311e-8f9f-24a6221fe560 | -12.76685 | -46.44544 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00da08fc-7a16-3685-b8aa-7e0d8853ee58 | -11.12121 | -49.87908 | 2026-08-26 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39100068-6122-3500-8fc8-cb95957129dc | -10.07834 | -58.54175 | 2026-08-26 04:53:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3209927f-3220-3cc0-8a80-27a9a91240f3 | -11.48816 | -45.11545 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 329718f9-0c81-3145-a673-526c060c5165 | -10.76304 | -53.99299 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6519772e-f7a3-3e9d-ba9c-fba5f1ca1568 | -14.76178 | -48.78404 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d166a293-32c3-31c3-9d19-ed3cb7577853 | -9.67233 | -55.08306 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2cbc165f-49c3-3f46-9f0a-5683069bfae9 | -10.75036 | -54.0089 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f1e7761-afe7-31bc-ba94-0efdbb302e31 | -12.76674 | -46.44897 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c2cc6907-3390-34f3-bc0d-8f2ab8c1603b | -16.17812 | -49.32817 | 2026-08-26 04:53:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe6e011f-c879-3b14-be68-346adf5f3554 | -9.47813 | -56.91477 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98891142-924f-3a21-8d85-f4c66b0ee98c | -13.85729 | -53.98793 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1b78e82-30fd-3d9a-91ef-323ff4e2191c | -9.996 | -53.96195 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af181f93-0aec-33f1-bb3c-9d1de3684b59 | -12.66909 | -48.41304 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 59ff3465-4893-3e72-bbce-c0e42844e734 | -12.02876 | -46.0048 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3e467f8e-1def-397f-824c-abb4f7a1ffc1 | -13.28401 | -51.4636 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fa5e2aa6-d594-3104-8a94-1f0646aebb5e | -12.76127 | -46.45344 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b4bbccd-7a0d-3128-b4e4-a491c7480ad4 | -11.82191 | -47.66077 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45f27eab-c176-395a-9960-dfbbc0a5e8ba | -14.0667 | -52.17717 | 2026-08-26 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6415a203-25b1-3bc8-b2e8-d521ced886eb | -9.18894 | -59.57666 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50a959d1-2943-313d-95a2-519fd202338d | -12.16281 | -50.59751 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c591fc8-cf39-31b2-ba38-d5a7c8706284 | -11.01346 | -45.0712 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38fbbf19-cd19-34c7-a9b8-c1110c5d32b6 | -12.95666 | -56.61777 | 2026-08-26 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3873e33-007a-33c7-9788-8525ac228c77 | -11.16937 | -54.00466 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39fe193d-d7e2-3926-94b5-adcfd64c0c73 | -12.6503 | -48.42546 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65828dbc-5481-323e-ae0e-f38fb58fa796 | -10.75478 | -54.02396 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e84d8e38-40b8-3a2e-a6e1-5a962d4171fc | -13.86116 | -53.98491 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f604d82-c106-32e1-9873-f61d0ed63cf9 | -12.76458 | -44.26893 | 2026-08-26 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8144bdb6-c55e-39b3-a70a-01e42a4a53f6 | -12.89669 | -59.9136 | 2026-08-26 04:53:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0412bb54-1ada-3f7b-ab5f-a7de54bdb251 | -9.66953 | -55.0789 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 68645500-69e1-3893-ad0a-9d1efa1f3105 | -11.21531 | -55.08445 | 2026-08-26 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a586a24-ce1e-3b1b-9f76-5a1ba40d3b21 | -10.76582 | -54.04009 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |


[Clique aqui para ver as próximas entradas](README42.md)
