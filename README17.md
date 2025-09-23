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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66f9e9ec-76d2-3f56-8e35-21585dcfdaba | -7.8885 | -44.01669 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e44dc65-aaad-3809-a627-6961635461cf | -11.53441 | -43.62226 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00dc413f-bfe6-3bd8-93b6-6f7268fade7b | -11.46811 | -43.53038 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f499168-a74e-3d79-88fd-1d1ee71a99b3 | -6.44721 | -45.66278 | 2025-09-23 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 916c9042-a20c-3773-8fe8-f13312168de5 | -7.33402 | -44.60934 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c490b281-7eb3-3915-83d0-578a28230237 | -7.86027 | -42.95424 | 2025-09-23 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e7d2ea4-5545-3345-9bd6-b27e4d87c4ad | -10.9526 | -45.74116 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c10a560c-b4d3-3868-954b-5bb00f1b0d94 | -8.52096 | -44.94386 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e91cc15d-2a9c-3e1e-99cf-140c4272fae5 | -7.15482 | -48.29549 | 2025-09-23 04:19:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86e10c3f-86b1-32b1-93a5-bad6ad3ee6a3 | -12.00008 | -47.74979 | 2025-09-23 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 2aaae763-c07c-382c-848c-abfe2754ab65 | -10.85205 | -45.4305 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81b8f5a2-cad2-3eaf-b0c5-fec4996e07d7 | -8.80827 | -43.07286 | 2025-09-23 04:19:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cf95c10f-daba-3902-9838-80f92ca227f5 | -11.02699 | -45.89306 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b32e92cc-427b-384b-b7ef-4b998c6a6690 | -7.88461 | -44.01971 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10ffb261-0cfa-33ea-be07-f7b6de70e8ff | -9.31666 | -43.36369 | 2025-09-23 04:19:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 190537c3-3de1-33d1-b9e0-56c78e24d8ad | -11.50156 | -43.55825 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d8623d9-e06a-3f57-b703-bb25ade957d7 | -14.64567 | -42.49495 | 2025-09-23 04:21:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 541514a9-3921-34cd-bd27-e9095fa2ac4f | -19.88701 | -52.96522 | 2025-09-23 04:21:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92f193cb-1980-3ebc-9ccf-076338215cb9 | -15.81804 | -42.09129 | 2025-09-23 04:21:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 491957d7-5c88-3faf-ae00-f8d1639eb72b | -15.67616 | -41.3149 | 2025-09-23 04:21:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f2268979-930b-3ba5-9915-b2d6c91a7114 | -19.88634 | -52.96884 | 2025-09-23 04:21:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e450fc2-7dc0-33ea-b656-538383161caa | -14.95937 | -40.89489 | 2025-09-23 04:21:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2a31971d-f340-32c4-a085-a626334dfcea | -14.18905 | -53.29823 | 2025-09-23 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c6e8659-230f-3e61-8171-953d01fa2bdc | -14.95884 | -40.89882 | 2025-09-23 04:21:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6854b651-46dc-3da9-818c-0db792b5b527 | -16.84439 | -40.74195 | 2025-09-23 04:21:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fba6dbc6-e2ab-31eb-a228-61f5dfadce40 | -13.80811 | -48.40517 | 2025-09-23 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 186aa8f0-217c-3d25-a5df-7164e4aae773 | -15.81872 | -42.0862 | 2025-09-23 04:21:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2abbfd10-63ba-3654-943b-29a75742fef2 | -16.8395 | -40.74581 | 2025-09-23 04:21:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 21d5f298-f912-36fc-86cc-bfacbb226bc9 | -21.01151 | -49.98763 | 2025-09-23 04:21:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2771107c-039b-30f9-bb1f-b46d1ee68920 | -14.19264 | -53.30382 | 2025-09-23 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcf2c30e-be59-3141-ad9c-974a972c1d16 | -15.45592 | -56.1594 | 2025-09-23 04:21:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 44beb32b-a40f-3ffe-be81-1e70bfd6b8a9 | -21.00136 | -50.0059 | 2025-09-23 04:21:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6203b0fa-9e94-32d3-bd8b-3bde4d025738 | -14.19351 | -53.29926 | 2025-09-23 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10b0e068-b016-3d6e-a4f8-af61ffc9cccc | -17.07885 | -54.06683 | 2025-09-23 04:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc29da9e-fbf1-3819-aa36-a79167d3408a | -19.87909 | -52.96336 | 2025-09-23 04:21:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b87aab6d-fe80-357c-a783-d04bfc6f14a1 | -15.45524 | -56.1628 | 2025-09-23 04:21:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3502eb12-eebd-3378-9c64-6203ba101125 | -16.84005 | -40.74136 | 2025-09-23 04:21:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3e73a9cd-1e2c-3c0f-819c-f7f258798348 | -19.88238 | -52.96793 | 2025-09-23 04:21:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3e5b6d47-17f9-3f6f-a857-fd1c14c8fa67 | -14.62469 | -42.53208 | 2025-09-23 04:21:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3914b89e-dafc-36ea-ae76-e308d2d75003 | -14.19137 | -53.30069 | 2025-09-23 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06e89995-b6ab-30ee-bb6e-b0816710bda0 | -15.67314 | -41.31457 | 2025-09-23 04:21:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c6aaa2ce-e6f2-33f3-9599-7d8fa8c279e8 | -14.1869 | -53.29968 | 2025-09-23 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fecbf700-b322-3e23-9865-1800bb9abd60 | -17.07351 | -54.07042 | 2025-09-23 04:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dac434d0-8362-3e0a-8686-beee822e8870 | -14.64506 | -42.49704 | 2025-09-23 04:21:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a6184e44-fc2d-3ded-aca0-2e7980c59482 | -15.67207 | -41.31419 | 2025-09-23 04:21:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b7c521f4-269e-3dd9-8f0d-904343ab1127 | -16.61361 | -40.58008 | 2025-09-23 04:21:00 | NOAA-20 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 56606cf9-3e40-3cd0-afe1-b9591a5e2c06 | -15.59301 | -42.39236 | 2025-09-23 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6325fc5f-9239-3ca7-97ac-943457b65e82 | -18.75042 | -49.54576 | 2025-09-23 04:21:00 | NOAA-20 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e1c38c2-a99a-3465-9b02-dffa8fdd64a5 | -19.88305 | -52.96429 | 2025-09-23 04:21:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| fbc5a44c-1c35-330d-b409-1b60d9b2ad81 | -16.61305 | -40.5844 | 2025-09-23 04:21:00 | NOAA-20 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| de410d30-8241-3993-810d-007bd84bc76b | -14.62535 | -42.5274 | 2025-09-23 04:21:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9f7060c5-689d-3f94-9212-230c86efa911 | -24.20633 | -50.41956 | 2025-09-23 04:23:00 | NOAA-20 | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| f930d16a-ce12-39de-9975-0a7c5a2f79c3 | -23.98253 | -48.94366 | 2025-09-23 04:23:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6d10768-7f74-38fb-82e5-fb4487ae0e8e | -21.55035 | -49.70631 | 2025-09-23 04:23:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 38563d84-f844-30f5-b5c3-004bdb3bab4a | -14.7719 | -60.2305 | 2025-09-23 04:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f195fc4e-f2a6-36a1-9b41-e2773d6aa83f | -7.6681 | -35.04031 | 2025-09-23 05:01:00 | AQUA_M-M | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 11695fa0-52ea-3927-a515-e992e6213fad | -7.03246 | -34.90891 | 2025-09-23 05:01:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| a7941922-ff61-3b6c-a88f-723162a07891 | 0.93397 | -51.20951 | 2025-09-23 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc56cb70-f179-30ed-a980-10d828f85e5a | 3.29031 | -60.67897 | 2025-09-23 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ad4a5fb-1a35-3001-aabd-77e321e7ae3f | 0.81322 | -50.69639 | 2025-09-23 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 728b07ce-ae02-35c6-a6e0-c5388a952531 | 0.9377 | -51.20643 | 2025-09-23 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9a480a26-f3ab-37ea-b42a-b908fc816726 | 1.12124 | -59.59616 | 2025-09-23 05:08:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf26fff0-ce47-3b4d-a494-f7a36d8f9e33 | 0.81378 | -50.69996 | 2025-09-23 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89b7ed0a-c78d-3b7c-9e97-208f0eaf1b71 | 3.83484 | -51.73983 | 2025-09-23 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5359892-c899-3f5a-9cbb-31de39423a4a | 0.93712 | -51.2039 | 2025-09-23 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6573de5c-db94-3c23-9a2c-b1c826e880ab | 4.28526 | -60.47493 | 2025-09-23 05:08:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e775691a-38e3-391f-9c0a-646acf267cee | 3.83416 | -51.73555 | 2025-09-23 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 443cbdd2-a86f-380c-8a6e-171b45ff3dda | 0.6941 | -51.44735 | 2025-09-23 05:08:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 534a95d5-5c38-3656-8d47-35388240117c | 4.31501 | -60.73223 | 2025-09-23 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95fa934d-90ed-3fa5-a179-a25e751aa3b4 | 3.29152 | -60.67862 | 2025-09-23 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccb84749-b688-3c05-82d0-4579e15b7830 | 4.30526 | -60.75334 | 2025-09-23 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 314152e2-054a-3a64-807b-4c561a468cda | 2.40738 | -60.70677 | 2025-09-23 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf519ecd-81ff-3af8-b724-335d080e32b1 | 2.41145 | -60.70613 | 2025-09-23 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4aee0c4-76bb-3829-bd10-daee91b7c1db | 4.63413 | -60.69512 | 2025-09-23 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06f1c06b-bbfb-3ef9-9cac-7724561b80dc | 0.95355 | -51.20643 | 2025-09-23 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 939d9eda-07b2-3384-8ee2-b8afd521cc4f | -3.36028 | -59.43711 | 2025-09-23 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8df2c29-bb65-3326-8011-102456f2e866 | -4.08344 | -48.0394 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74fdd22d-09db-31c4-bd03-57337b8069bd | -6.33368 | -56.19493 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad2da848-6fbb-3013-8c66-b514902c8c56 | -4.23875 | -54.72548 | 2025-09-23 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6f62626-4841-3152-a9c0-97e7337e7f32 | -3.64353 | -51.90829 | 2025-09-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87d4396a-47b8-31ac-bd76-71534638d354 | -4.51079 | -55.75837 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78d93172-9bb2-3be7-8782-6006d4f20dcf | -6.33422 | -56.19138 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 116328f7-57c3-351b-b4af-bdaf33f65449 | -2.38374 | -47.72227 | 2025-09-23 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4f3b588-6541-3d79-a963-4cf721786d9c | -4.39618 | -49.34905 | 2025-09-23 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9891664-f6db-3a85-8483-603da64d5602 | -6.34318 | -56.20006 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3174d8e1-ec8d-3f77-85a0-62c9ae2a4ed0 | -4.9667 | -48.0147 | 2025-09-23 05:10:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61a20320-b260-3bc3-9c7f-69f6125a68fb | -3.58613 | -49.42807 | 2025-09-23 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f35f658-bd68-34e7-ad44-bd79581d8796 | -4.27228 | -48.18414 | 2025-09-23 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77516ac5-da7f-3d2b-8935-52c8cc3cf5b9 | -4.10609 | -48.74461 | 2025-09-23 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c3a0cdf-1bb6-3f0d-8b22-2ede4d48f1e1 | -3.35326 | -59.43603 | 2025-09-23 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21617223-aa09-3155-ae50-126352f2c471 | -2.37851 | -47.72145 | 2025-09-23 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f4fbc1e-4299-3092-983c-f799fb88d304 | -5.92291 | -49.29652 | 2025-09-23 05:10:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a679141e-a6f5-3cd2-982e-6bfdef6aab35 | -3.03286 | -51.45004 | 2025-09-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 242ba9dd-db1f-3154-bac3-a5029258149f | -3.86408 | -53.53077 | 2025-09-23 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b816e03f-916d-3eb2-8aed-b2bba0c37339 | -4.60114 | -46.59257 | 2025-09-23 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b4459d8-2a03-3775-b2f8-a0ac4a77b6a5 | -4.08346 | -48.03881 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92f87d77-399f-35f1-9b4b-96118438a1f0 | -3.38794 | -50.25686 | 2025-09-23 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec7990d2-66dc-3591-9429-3b4e9369494d | -6.71745 | -47.20677 | 2025-09-23 05:10:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7784919-329b-3f78-b668-4a4603d8ce56 | -1.08465 | -54.10678 | 2025-09-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2698834e-5ceb-3473-bcde-647867397363 | -6.35431 | -56.19451 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
