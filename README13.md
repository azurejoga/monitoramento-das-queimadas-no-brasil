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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b90d8581-c61f-3101-ad17-776a52644cca | -12.32887 | -53.14679 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cd848629-7df3-38de-af62-fd31a84400d7 | -14.31911 | -54.93271 | 2026-08-09 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae384d4f-6d39-35d7-a16b-7e47fbd4e44c | -14.92203 | -48.22979 | 2026-08-09 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b990d7a1-9557-3894-873d-29dfd1076ebb | -15.36778 | -53.78217 | 2026-08-09 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 063241d0-1143-343f-a415-5d68738c353b | -14.06837 | -53.8074 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a24c116-9cb9-35fb-af17-f13f1a1e5d25 | -14.86635 | -43.89872 | 2026-08-09 04:27:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8a30eddf-42d3-38e4-b4e9-4912a4cb636d | -14.06934 | -53.8279 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e7230292-fdd0-3942-bc61-f515e28dc14f | -18.93546 | -43.48188 | 2026-08-09 04:27:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9a2653f1-462f-3fff-856e-263962ffc97e | -10.92263 | -57.12132 | 2026-08-09 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f07afca9-89bd-3e3b-8c88-5f4296ff5273 | -13.83281 | -53.75254 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f96984c9-f511-36e0-af2a-709fc3521f43 | -19.69619 | -46.93288 | 2026-08-09 04:27:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f8663ac-32f6-33d4-83a4-44fb8301fed2 | -14.08642 | -53.98533 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 359e27a0-e1bb-377f-8048-accb1ca778eb | -12.35121 | -53.15892 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a10276e8-103e-3447-807f-bb68bfddbfd8 | -15.38816 | -53.77198 | 2026-08-09 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d20e17c-6f66-3d6d-9eee-270b29c1e55f | -14.03816 | -53.84232 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 747aaef2-666a-368d-a008-2ce9f268b0eb | -12.34976 | -53.16052 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b5c0ad29-8f37-3140-af19-eeb45deeba85 | -15.14554 | -52.71878 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8ae5b65c-a1c8-3e5b-8aec-79a430f6d60e | -18.65175 | -49.85118 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| be4e4a3e-2f89-320f-905e-56f8f55336d0 | -11.84243 | -56.9467 | 2026-08-09 04:27:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3c07a59-264d-3043-8c39-d6b2d194fd20 | -14.318 | -54.9384 | 2026-08-09 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faeeca9e-231e-32a9-a8ec-3398d57b6476 | -15.40768 | -41.79973 | 2026-08-09 04:27:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 6ad16749-9d99-3862-b3f8-9026fe2e18ca | -18.6278 | -49.86703 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2b9786d0-49e5-3956-9ca0-c0b346a79f7e | -14.04551 | -53.82838 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce016577-33c3-394e-b94a-1b2fef0bb4eb | -16.31713 | -49.42686 | 2026-08-09 04:27:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d64090c5-59a5-3632-8ec2-5dc6f9316d4f | -19.58891 | -42.59058 | 2026-08-09 04:27:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 79911f28-797b-3f5d-80e3-4e20899e42c5 | -15.1371 | -52.72036 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9eac3ca4-8d7b-3c1a-bc9d-5305b6b7ab19 | -18.64078 | -49.85319 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| d4478fe4-b159-3d7c-93f7-7c02a0b032ce | -15.76172 | -47.74785 | 2026-08-09 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc94b420-1951-36a1-a723-b8a2cbbd9fe9 | -15.09706 | -52.74706 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d07f1b3-b629-381a-8d46-f1fc68e0a5ec | -14.04826 | -53.83913 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e40e4caa-2d93-3b45-8350-9bd5492ac189 | -14.92143 | -48.23343 | 2026-08-09 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b724c0c-44be-352c-962b-8b8eb0788549 | -13.86077 | -53.6783 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f2b5bae-78a7-314c-89ac-b7390bd67b13 | -19.95419 | -43.95794 | 2026-08-09 04:27:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c1808e01-53ab-367e-9732-31d4ca4c4644 | -13.86356 | -53.68873 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 425bb425-9989-35b3-b5b9-1358bc63650d | -20.69659 | -42.31914 | 2026-08-09 04:27:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cbbb3dca-37af-3e20-ba7f-82c67800f6f0 | -14.08919 | -53.99609 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4df46d2-fae4-33af-82ad-9bf67ee226a6 | -15.08793 | -52.74951 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63b593a0-be53-3d62-abce-a53746fda9a5 | -15.14479 | -52.72292 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7d8ae48-4d91-35c9-9470-f1a1c548c261 | -16.31647 | -49.43077 | 2026-08-09 04:27:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ffa9fb5-f155-3f6e-85ef-b2bcb82eeace | -15.1406 | -52.72216 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48eb9ff0-07d3-33fe-aaba-ca6bbdf5242e | -20.69611 | -42.32314 | 2026-08-09 04:27:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 068c3b72-a63c-3703-bd5d-f9f758394549 | -19.57673 | -42.58878 | 2026-08-09 04:27:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d23d174e-128d-3a15-9057-06079fd81b8b | -14.08176 | -53.98461 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeaf59b8-5182-3594-b837-be210922859d | -14.07025 | -53.82293 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 190e0e56-f86b-39d5-9075-d47f35296fc7 | -12.34306 | -53.15253 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08b3f564-2c19-364f-9612-793dc270d33c | -13.8408 | -53.70958 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 903fe7d7-10c2-37cd-8e0b-b8f9e95edbb0 | -14.04091 | -53.82756 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef9a354c-6f7c-3fac-9f2b-b51d564f6756 | -12.33254 | -53.15233 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a0de796-c511-3aa8-acb0-5177142fed56 | -19.58033 | -42.59312 | 2026-08-09 04:27:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 74e8b1d3-6153-3887-b870-5348ee9951e7 | -14.06566 | -53.81903 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bdc7589-3b9c-3f6d-9010-c95ead0f1cbf | -19.58437 | -42.59382 | 2026-08-09 04:27:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 492e64c2-3062-387c-8e69-a658daa8e7e9 | -14.16955 | -53.99439 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0c58c1d-1ed3-317e-a256-680d59e522b7 | -18.64555 | -49.84597 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d7bb8d72-8cd1-3de4-b6bc-c30799bec977 | -14.07025 | -53.8199 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0752bef7-4a50-3472-8dce-c7f3e161f0c4 | -19.57721 | -42.58502 | 2026-08-09 04:27:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cd9a5444-9384-3a04-94ba-2f1993f4f13e | -14.08549 | -53.99029 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdef4816-18e5-3d34-91a4-9ea89e7dd762 | -15.36863 | -53.77757 | 2026-08-09 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e61d5af-2239-3ab1-98cd-d722208dc050 | -16.71758 | -46.40313 | 2026-08-09 04:27:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f27e0fd-2a0a-3dbd-8417-b1127624360e | -14.03267 | -53.84628 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| abfedd37-7732-3932-ab54-a8dfecb405e1 | -18.63468 | -49.86829 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d5e90add-9b40-3041-b1c6-b2d31ea798c7 | -18.98277 | -43.36133 | 2026-08-09 04:27:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 305c58a4-de75-3437-96bc-ebe922d0349a | -16.31368 | -49.42622 | 2026-08-09 04:27:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d0b1a369-0e12-312c-9221-2a09866d5f35 | -11.84337 | -56.94755 | 2026-08-09 04:27:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01f1cbf4-4bb0-3eff-bfd2-9319ea4adeaf | -12.34692 | -53.15031 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61db592d-491b-34d9-98f2-4004c5699d8f | -20.37923 | -42.00295 | 2026-08-09 04:27:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b219ac8e-86f0-3d00-9068-7f63403ae625 | -14.32131 | -54.92147 | 2026-08-09 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64b71a2a-3fda-36ae-bc76-53ec395fc13e | -12.3506 | -53.15585 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 392294b4-d28a-3ed3-9e91-edbd679ebfad | -11.28488 | -53.95021 | 2026-08-09 04:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21037524-71c8-3955-b771-c2e42c0f0fd1 | -12.59301 | -46.99562 | 2026-08-09 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b893111-2eed-37ed-bc7b-ca742edfa914 | -14.01982 | -53.83868 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3443c785-b90f-3884-a70b-8141cd8c4dd3 | -18.63735 | -49.85255 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6b42b71c-4bc0-34c9-97d9-7a1fe1044024 | -19.93992 | -44.37073 | 2026-08-09 04:27:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 685128c0-683a-35b1-943a-7f4a65abc833 | -16.31992 | -49.4314 | 2026-08-09 04:27:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e248cc6-e618-37c4-b840-0cbaac17ff17 | -18.0027 | -43.31509 | 2026-08-09 04:27:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6eb9134-ed5d-3102-b7d5-84b313447c2b | -15.65356 | -43.29145 | 2026-08-09 04:27:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a9b5bd3d-cc0c-373c-a5c3-dffefc83dad0 | -15.37223 | -53.78309 | 2026-08-09 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 156eaad9-c0e0-3ada-9027-2c25b50ce50c | -16.31434 | -49.42233 | 2026-08-09 04:27:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| fe4af25c-06ec-3895-a9b6-dde657d9d9d8 | -14.17049 | -53.98952 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aeb6a79-b0f3-3e01-b3f4-44999ead7575 | -16.71814 | -46.39949 | 2026-08-09 04:27:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70f5a257-bd5b-3496-9cf1-8b6315387cb9 | -20.19414 | -41.65911 | 2026-08-09 04:27:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 94e4be0e-77db-31ca-a588-92741a9277df | -13.86163 | -53.67364 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7de59d48-2972-31e7-b8a8-bb4519e9d97d | -19.93928 | -44.37535 | 2026-08-09 04:27:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ca7dd861-381c-3fc8-bbbc-51ffdb327be8 | -15.09138 | -52.75436 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c44287f2-950a-314b-8845-e61e63257825 | -13.96952 | -47.37471 | 2026-08-09 04:27:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d09b65f7-417d-3833-a638-6235b203c55c | -14.07987 | -53.99458 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c40250ef-c191-3bc2-9467-e3240be448ab | -14.08454 | -53.99529 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a115cfa-f9bf-3f42-919d-d5ee43da5ef7 | -15.76114 | -47.75145 | 2026-08-09 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f30a8f3-7204-3806-bf4f-3bd6dd64e20b | -15.36247 | -53.78579 | 2026-08-09 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3344ee79-2998-357c-a4e1-a033fe4e0746 | -12.35486 | -53.16447 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 43efdf90-1b17-35c9-8f73-2c5a610e8e6e | -10.92482 | -57.12075 | 2026-08-09 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bc4f2e5e-7139-30ed-9f2d-9b07f9ddf967 | -19.18782 | -47.19294 | 2026-08-09 04:27:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ef6c93c-d6cc-3ca4-a20e-04d3d8a35ca1 | -11.17407 | -54.8122 | 2026-08-09 04:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fe6edfa-e55b-3617-a17c-e42c9b59e3d1 | -14.0693 | -53.82484 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5c176082-f40c-3d96-b2cd-4b508b64cb1b | -20.38294 | -42.00792 | 2026-08-09 04:27:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1529ab97-b49e-3da3-9410-63add8baf9ac | -18.64087 | -49.87351 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a793b485-6ac6-3a8d-8523-84f6c62736b9 | -16.31779 | -49.42297 | 2026-08-09 04:27:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29615488-df50-3915-84cb-ddde4435eeee | -15.83291 | -42.23186 | 2026-08-09 04:27:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d58984cc-0df8-3c68-bd5d-ccd87a981d53 | -14.30974 | -54.95454 | 2026-08-09 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d971e444-87d9-368a-9445-c7c42bcb9109 | -11.17273 | -54.81054 | 2026-08-09 04:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebb3ceb3-dbef-3921-ace0-59701a2d9522 | -14.9129 | -48.24328 | 2026-08-09 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README14.md)
