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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9336da5-6b0e-35b2-99ad-2f82b1ed803a | -14.68128 | -41.42475 | 2026-09-21 15:58:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5b3803d0-9eb8-38a1-8af1-3907f1ea4e67 | -15.29329 | -40.96936 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| d27c312b-12ca-3c45-a35f-67fbafc14168 | -16.31587 | -43.1274 | 2026-09-21 15:58:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 75f8556a-f76e-36ab-8ccf-02e36adb01d0 | -15.86877 | -49.89433 | 2026-09-21 15:58:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| acc8a448-d720-3d19-bf83-b7cc2b3bbdff | -18.86706 | -40.06121 | 2026-09-21 15:58:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| b34ab980-d769-3146-8656-e347e877f6c5 | -14.50289 | -40.88915 | 2026-09-21 15:58:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 91247cd2-96b4-3fad-ad6b-4f9a1ccf3ea1 | -14.69158 | -40.36631 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 331e8675-bdfc-38e4-b499-ee0665001276 | -14.80221 | -41.24203 | 2026-09-21 15:58:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3dad6882-5ada-341d-943f-911e69fee23e | -14.96999 | -41.75988 | 2026-09-21 15:58:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 3185785b-4d95-3879-9e53-724dccabd972 | -17.5718 | -43.70686 | 2026-09-21 15:58:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 9e45e2c2-7211-3f67-80d1-11384f9f2017 | -16.24756 | -40.41371 | 2026-09-21 15:58:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e8fb1ef3-39f1-3289-a389-cfd4de60c759 | -14.91012 | -41.46198 | 2026-09-21 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d9c38275-35f2-3579-be33-315f63c3a781 | -14.45567 | -40.27974 | 2026-09-21 15:58:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 6723acaf-17ed-3d41-ad3f-109f752be451 | -16.85156 | -45.43373 | 2026-09-21 15:58:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| efab32fd-0e08-3b98-8428-ae15745d07d4 | -14.91965 | -41.11494 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 5ecece76-db9c-3a87-adb3-fa5a9a1e0ba3 | -14.10725 | -40.72054 | 2026-09-21 15:58:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 3d3d0f7a-e4ad-3c08-941b-0e9b2d3d77d2 | -17.08672 | -46.17157 | 2026-09-21 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 2a0f69f3-ce7a-3b57-9be7-f21eed1db460 | -16.35979 | -43.29348 | 2026-09-21 15:58:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b75a088a-9225-3678-850b-8a56a48c823d | -17.9526 | -44.01014 | 2026-09-21 15:58:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8fbd1eee-d42c-39ba-8718-cc4e2e55c4e4 | -15.12979 | -48.1904 | 2026-09-21 15:58:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 84275011-400d-3844-be8c-8f6b731f3b65 | -14.92522 | -41.51377 | 2026-09-21 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 98624534-64aa-38f2-9415-471a809a8fdb | -14.39149 | -41.94492 | 2026-09-21 15:58:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ebb86331-5c83-344a-8e71-d23457bb0d48 | -15.23564 | -41.47756 | 2026-09-21 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| c510190f-d1cb-33eb-a7be-1b1eff93882c | -19.43179 | -41.08408 | 2026-09-21 15:58:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1cb32bbd-ceca-304c-a8f6-dfd750d29f7d | -14.66022 | -45.68335 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 00665888-e74c-3680-81e1-e850c0048081 | -15.77714 | -40.29727 | 2026-09-21 15:58:00 | NOAA-21 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 516ec123-b11c-3fd8-9c77-3a2114002350 | -20.11169 | -47.81978 | 2026-09-21 15:58:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 73bbc835-246b-384b-beec-d2581fbdced2 | -16.77102 | -45.62368 | 2026-09-21 15:58:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| aac242eb-b4a0-3519-89f5-2e2698570c92 | -14.76922 | -40.06171 | 2026-09-21 15:58:00 | NOAA-21 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 20e2ade5-0127-3ed9-8b94-309b4e992907 | -18.31107 | -44.13628 | 2026-09-21 15:58:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 682cfafe-d65b-3cfc-97d6-4362c9cbf8cc | -15.27832 | -42.25893 | 2026-09-21 15:58:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| dd5c6cc1-d723-3e21-b5b3-9cba3a1f0c43 | -18.37154 | -43.04494 | 2026-09-21 15:58:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 336c8918-84ab-383f-a7f0-05301fa9ba63 | -17.53392 | -43.95205 | 2026-09-21 15:58:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fba838b-ae64-33a6-9ed3-3a2439746c3d | -14.5281 | -41.67867 | 2026-09-21 15:58:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| c4fdfce1-cdef-344c-a6ce-962ca6cca2eb | -17.27559 | -44.51942 | 2026-09-21 15:58:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7916a6e3-c702-3600-bb49-7ddc85978d5f | -16.38033 | -45.10996 | 2026-09-21 15:58:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 22d095a9-a211-3c14-b84e-10d46ad7fbac | -14.77614 | -40.71739 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| cae1a86c-51d0-3093-b24c-2112bc5ddd59 | -16.85118 | -45.43011 | 2026-09-21 15:58:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5ada5ab3-4c1c-3148-9eda-5da523ffc454 | -14.92932 | -41.51322 | 2026-09-21 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 99bac20c-4577-3b26-9051-306ef980cd89 | -15.69537 | -45.3655 | 2026-09-21 15:58:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b21ea5c0-40db-3fb2-9714-26296fbbd990 | -19.7354 | -40.74638 | 2026-09-21 15:58:00 | NOAA-21 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 5912012f-3ccc-30d1-90f1-aefadeac6331 | -19.59336 | -45.01669 | 2026-09-21 15:58:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 9e5b1bff-fe1e-31ec-b7ed-712ed32747f3 | -14.44143 | -41.24086 | 2026-09-21 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ae7179d3-83e9-32e2-a040-201066566bfe | -18.05111 | -44.02815 | 2026-09-21 15:58:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 31ff512d-aa01-3a27-bb86-e5408b94f335 | -18.71527 | -43.21391 | 2026-09-21 15:58:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 15053b39-5822-3262-ae49-76f5ae1886cf | -14.86921 | -41.02725 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 0fadcef8-ab38-34eb-8bf9-37077bad9f0b | -14.70821 | -41.92999 | 2026-09-21 15:58:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 49648450-db41-30ca-ad89-c1baaa22cad5 | -15.91004 | -41.8669 | 2026-09-21 15:58:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e84e3b01-e2d2-3e72-a3a6-978ee63ba680 | -15.47322 | -48.39897 | 2026-09-21 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 31d6179d-1b03-34d3-bdbf-a9f64ef6a47c | -15.46121 | -48.41007 | 2026-09-21 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 69244555-5bd5-3a8b-9ddb-0b2e0e35fd2a | -15.25541 | -47.5961 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| ce57d5de-546e-36d8-b3ce-4eb7291d8d8b | -15.1822 | -41.76725 | 2026-09-21 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| edcaed87-6867-3bae-866a-4e059db864c3 | -16.88222 | -39.15107 | 2026-09-21 15:58:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| acf8aeab-4260-3572-8341-9341f7856db9 | -15.42385 | -47.19837 | 2026-09-21 15:58:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e51691c2-0384-3db5-9967-97e708d57562 | -14.53222 | -41.67808 | 2026-09-21 15:58:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 78bb0af8-efc0-3be6-8611-4e3e5603d365 | -14.66563 | -45.68277 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 4c6b0306-df43-3132-b962-f75b3ca58e8d | -16.47068 | -46.09719 | 2026-09-21 15:58:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b4422cab-0780-32f6-bf20-d4b5ce98274e | -15.61261 | -39.52575 | 2026-09-21 15:58:00 | NOAA-21 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| ad8200c8-fe24-3bf5-b336-21473197f404 | -20.1183 | -47.81959 | 2026-09-21 15:58:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 307c02e3-8901-331a-9c01-a4973ab5949c | -15.15603 | -49.17319 | 2026-09-21 15:58:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6a9b4f65-d644-33f0-9f99-ea4fbe8d92ac | -14.58741 | -40.45254 | 2026-09-21 15:58:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6c853086-0ce5-3905-901a-ae2699e07c31 | -16.1337 | -43.6397 | 2026-09-21 15:58:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 851b58a5-ec1b-319d-a88b-40078acbaa29 | -14.91764 | -41.11578 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| dcf52725-c6c4-3bb6-9baf-ac3e10a31cd8 | -14.6413 | -41.94725 | 2026-09-21 15:58:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f41ec075-e2db-3078-8056-a47cd3c356be | -18.03133 | -40.52261 | 2026-09-21 15:58:00 | NOAA-21 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| b9b46a2d-efdb-3dd5-8071-e4a811939fa1 | -20.11238 | -47.81737 | 2026-09-21 15:58:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 1c4a13fc-facb-3b92-acaf-242d9885a7e0 | -14.64819 | -45.67392 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6ec61fa4-5a56-35e3-9900-d3f2041c930a | -17.31774 | -39.62979 | 2026-09-21 15:58:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 6c1ffde7-e731-3dda-a762-fa6e543eefec | -14.45502 | -40.27504 | 2026-09-21 15:58:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 110aa228-15aa-3a69-9cea-54b3767c2671 | -18.11872 | -42.25064 | 2026-09-21 15:58:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 630301ed-30ef-311b-9f02-a88233422b68 | -20.11289 | -47.82334 | 2026-09-21 15:58:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 34fde165-56ff-3205-875e-b3965dba3a51 | -14.6586 | -45.66915 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 6ecf12ae-2f6b-30fa-83ba-d53311a1f8c8 | -15.68962 | -45.36266 | 2026-09-21 15:58:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d13694d3-2b9c-3d5a-ba37-9ca96017d6bf | -15.84112 | -41.62258 | 2026-09-21 15:58:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 23d96502-42d7-328e-8e0c-d813c15b5044 | -17.38019 | -46.75936 | 2026-09-21 15:58:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aaeaa9a4-d86c-3e6e-ae37-7d6da3f9689a | -14.65941 | -45.67627 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| da377576-4297-33c8-be05-2cf87804201a | -15.53917 | -41.04243 | 2026-09-21 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| d5dcdf9e-4a57-3870-86fa-34c1f5c577e7 | -15.17199 | -49.769 | 2026-09-21 15:58:00 | NOAA-21 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2282652a-03c6-3f21-8b5b-3cdf08ddd5fb | -17.08629 | -46.16743 | 2026-09-21 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| b70d7678-3351-3a23-b61a-0ed5b4af1462 | -14.68994 | -40.55492 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f489e862-1c86-334e-a151-9b0e305b3553 | -18.53794 | -44.52068 | 2026-09-21 15:58:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a235f6a8-b314-3924-a231-6df9f628101d | -15.15944 | -48.16538 | 2026-09-21 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2744d8fa-41f0-31a1-9fe5-26650c1e6143 | -15.15263 | -39.89733 | 2026-09-21 15:58:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| c42a49c7-4bea-3326-a20e-5b15c1f391e4 | -15.45496 | -40.3396 | 2026-09-21 15:58:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 47c41f4f-56dd-33ef-bd71-7945835d12eb | -15.41781 | -47.19886 | 2026-09-21 15:58:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11419897-6230-344b-844a-094e31d36768 | -15.45748 | -48.43882 | 2026-09-21 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6dcd57a1-cab4-3f3f-be49-1ba3cec6c089 | -15.53871 | -41.03894 | 2026-09-21 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| e914d005-653c-3c55-8b68-e9250fb64dce | -17.93552 | -45.21042 | 2026-09-21 15:58:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 419ce92d-341f-3d4e-b9ca-a5f8d0071488 | -15.85862 | -40.14644 | 2026-09-21 15:58:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5a68877c-d8e2-3aa4-a8ca-0752ef184c2b | -17.80846 | -42.74199 | 2026-09-21 15:58:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 5bb66f5c-2f0a-3ee5-8820-534c1eac23d6 | -15.23613 | -41.48134 | 2026-09-21 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 105431b4-696c-3d2d-8c34-fc129afe1052 | -14.10981 | -40.72631 | 2026-09-21 15:58:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8a733365-65dd-39f2-93df-ae81033323b6 | -15.38382 | -41.14827 | 2026-09-21 15:58:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| facd0827-af48-3b6d-b6ce-11b782b9c5f9 | -17.32464 | -41.82525 | 2026-09-21 15:58:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 624e20e3-2f40-3638-934b-87691a78fc50 | -15.46177 | -48.41573 | 2026-09-21 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dd118e6b-bcc7-3176-a173-724ad6799011 | -14.58709 | -41.27822 | 2026-09-21 15:58:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 54ca02bc-ca4a-3810-b4d0-54c0308479bc | -14.65901 | -45.6727 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| e1ec3790-8bac-3e3b-9874-2456cc619524 | -14.50454 | -40.96194 | 2026-09-21 15:58:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| bff58a4c-47a4-32ba-8530-49060aa5e741 | -16.7714 | -45.62735 | 2026-09-21 15:58:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 019da467-bada-3870-8346-448ff9e091d1 | -16.36016 | -45.9738 | 2026-09-21 15:58:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README148.md)
