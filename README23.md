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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2aed849-5e63-3b9a-8783-d9836ee27e7d | -14.69446 | -46.98464 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3610848b-38d5-33b2-bed9-bbc5da6f8e76 | -15.53376 | -45.22895 | 2025-10-01 03:32:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1b59100-7fbd-398c-8c7a-a99c597695de | -15.81781 | -43.32555 | 2025-10-01 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c89c134e-7198-35f4-b603-9ce9cf3fb035 | -18.96264 | -43.71459 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcb16555-3afc-3557-bd1f-da7c95db9240 | -13.9418 | -48.11999 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22ad6863-d445-358e-8def-1377ce7fa4b5 | -15.54152 | -44.33177 | 2025-10-01 03:32:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 93d38533-2cb8-3d75-9f45-fcaa6925bd19 | -15.44337 | -43.64273 | 2025-10-01 03:32:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e16d5394-60e2-32f5-ace0-fee3479e7e99 | -14.68388 | -46.96939 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7ee4218-6af2-375a-a148-96b77ed0515d | -19.93316 | -43.89003 | 2025-10-01 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| edfdae6a-5015-3ec4-ae30-df8ed2ecb324 | -20.49304 | -43.94374 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| bcc2a9a3-56fd-35f4-99ed-57c0af65c7c7 | -15.80233 | -43.32104 | 2025-10-01 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eec54c09-9164-3fbf-b18d-3a4a488b018c | -20.62737 | -46.2302 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 685e986f-5ce5-3507-bdfb-8203caef2d44 | -20.6297 | -46.21957 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0c6ae573-e1c1-38dd-b191-31f062754d3f | -14.78692 | -45.77166 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6936868e-b166-3d55-94b4-2fcd7e8c82a9 | -15.33965 | -47.93821 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b37be633-4115-373c-8167-af2efa0d76c2 | -20.02218 | -44.53813 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c32c8284-4cad-35aa-84ff-c70cd08bfb05 | -20.6003 | -45.8847 | 2025-10-01 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6ad2098-fda1-3f18-8f4a-59443259120f | -15.28399 | -46.41181 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22f20851-7c20-38b3-99df-5852aa5e6a18 | -14.79067 | -46.97342 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac674108-bf3f-3222-bdc3-4cd414e24d27 | -15.94479 | -48.12177 | 2025-10-01 03:32:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95e4eca2-c067-31f7-8884-76a7342180eb | -14.68189 | -48.24113 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b2531133-5472-3b89-a24d-a57ab24ab4f9 | -22.23902 | -43.41133 | 2025-10-01 03:32:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 59b8904e-0247-33d9-b2f8-a6896dd03a10 | -15.7535 | -43.71978 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d89e9817-9d9d-3dcc-a852-44f3a22e6283 | -18.8027 | -47.55785 | 2025-10-01 03:32:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f05e7476-0fb8-38ed-95a7-8d4aa49a7cd2 | -14.89677 | -48.11212 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac758f07-dbe1-3df9-9884-566ebe6954b2 | -14.62447 | -46.98694 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff5d3bb5-70aa-3080-b7c8-cd54e8291ae0 | -22.06154 | -43.07552 | 2025-10-01 03:32:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9a583dca-5343-32fb-bdac-56210fe7b475 | -14.03435 | -47.97202 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab3e267c-2ed4-356e-97a5-add5ce4d931c | -20.47711 | -43.94411 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 29e85214-755c-3efa-ba4b-a81af6234a0d | -19.86325 | -43.82496 | 2025-10-01 03:32:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 8d4d9809-2b8a-3553-8669-b3da0061c45c | -19.93173 | -43.897 | 2025-10-01 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 21c2c190-a5e3-317c-bcee-a0bf6761c923 | -19.9985 | -42.19578 | 2025-10-01 03:32:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ab5d4354-4c05-3112-94bc-d284d7f27625 | -18.70058 | -49.17845 | 2025-10-01 03:32:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a8f142ff-4394-35af-ab8e-3f4fbbc1ada8 | -14.8717 | -48.31998 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 34855a3d-aff2-3767-afdd-7e68002effad | -18.33122 | -41.80263 | 2025-10-01 03:32:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b90dc2a6-c628-36c7-bee3-894e1c782f9c | -16.40036 | -47.04689 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adad2bdf-35f4-360d-a86c-08e9f7f0e044 | -20.62845 | -46.22526 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 22e80bb1-e0ac-3d18-86bc-675ceebff693 | -14.03866 | -47.96825 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35cbe8e9-c210-3e6f-bfed-a05611e17f13 | -14.70111 | -48.22194 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f72d8922-7ca0-398e-a128-5c9549d0d370 | -14.52243 | -48.37135 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7f21008b-8866-3b7f-b586-282e6641381c | -22.06195 | -43.07505 | 2025-10-01 03:32:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f40fa6d7-cba6-3c73-86a0-ad34bcdb053d | -14.34733 | -45.92844 | 2025-10-01 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f75636e8-e8a5-3aab-95e1-3776428a6d6d | -15.31078 | -46.41092 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 933a8647-5133-3687-9950-1ad9f46fab95 | -20.59488 | -45.88269 | 2025-10-01 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66702261-0280-317d-acc8-6634705978d1 | -15.47139 | -45.87616 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6086f151-9b25-3714-ac06-b85822e948ed | -20.59211 | -45.88463 | 2025-10-01 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34ea90a3-ecb6-379f-bc5b-0d9669a8802f | -14.89817 | -47.21198 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09e95f8d-8e3d-38c2-a3a9-45b901d0c57c | -20.49421 | -43.93822 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| da4cd772-bad8-34a0-8efa-7b95ad7cd87b | -21.66142 | -45.33481 | 2025-10-01 03:32:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 64351d9f-22c6-3c57-ae35-1e7987745043 | -15.2892 | -46.4114 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a719d939-a1e4-3006-a734-9d14e3576794 | -20.43593 | -43.59943 | 2025-10-01 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d9eef2b6-a44c-3b67-9a4f-20ec4fbb8f0a | -18.91914 | -43.12028 | 2025-10-01 03:32:00 | NOAA-20 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5b26be4e-53d2-36e2-84f7-a16472c83525 | -15.80221 | -43.32214 | 2025-10-01 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3614af35-9d1b-3cf4-be4f-17dcf4a0c749 | -17.3847 | -47.14983 | 2025-10-01 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef9c44c2-09df-3b88-a68c-d1e869764dc2 | -20.03264 | -44.54091 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4331ef17-211a-3bc5-a8bf-5bc543d4c9ce | -19.6907 | -43.68167 | 2025-10-01 03:32:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e5cb957-b1ba-387f-ba7b-492c1dcb1a62 | -18.33023 | -41.80769 | 2025-10-01 03:32:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ca0d03d-ef9b-3884-9935-8eac4d408b53 | -15.62965 | -46.25617 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc28cf09-f5a1-3fe5-9f50-32e52266f565 | -14.89997 | -48.11189 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ddea958-ef63-3e78-ad18-e6bae87d1fee | -20.83876 | -43.01963 | 2025-10-01 03:32:00 | NOAA-20 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ad1b911e-797b-34af-a3ee-0f9637575a13 | -19.68945 | -43.68766 | 2025-10-01 03:32:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75eabddf-44c5-3b74-9901-aadbab8af00a | -20.02757 | -44.53919 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f74bd395-b9be-3817-b207-a296913b8897 | -14.3524 | -45.93549 | 2025-10-01 03:32:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 86524373-7151-31da-8032-510c575ad032 | -14.87734 | -48.32798 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e44b7bd0-3c20-363d-b898-809db602ac0a | -14.35407 | -47.13929 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1465ca30-34d6-3e81-a354-33ec6e1eb1c6 | -15.33868 | -47.93739 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a331a7a7-a88d-3983-921a-48cbe8a0e73d | -17.00205 | -40.02504 | 2025-10-01 03:32:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 10b1f54e-3946-3bdd-aae4-32e0667cb528 | -15.92659 | -48.13804 | 2025-10-01 03:32:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1ea19ca-e31b-33f7-a242-cb7ed5ce3804 | -14.60698 | -48.30731 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7ea9a484-f116-3751-9e35-6c569131d76a | -22.23788 | -43.41678 | 2025-10-01 03:32:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d4a869f0-83fc-350c-a59d-c3d2abd9f1a3 | -14.98712 | -46.96637 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6a72c83a-0c60-3ee0-b6e5-bef82c8f32ff | -14.7551 | -45.76947 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9d64633-624f-3877-ba99-6e8cdca876d5 | -15.7735 | -43.67658 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 115ba39f-6215-3bca-bdd9-95532b4c7228 | -17.80923 | -43.42291 | 2025-10-01 03:32:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5ac5f55-82d0-38a1-9fea-5760cf7b15e9 | -14.54678 | -48.25123 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71751495-6efa-3a82-bfd7-1d948ea8958f | -15.33761 | -47.85028 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebb96b7f-f0bf-3236-98ff-0dd3d0007ac1 | -19.93528 | -43.90119 | 2025-10-01 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 53101edd-0815-3bbe-8443-076f9fd26079 | -14.78409 | -46.9718 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c5bacfd-2fd9-306c-915b-cd4f4d88a0c2 | -20.62107 | -46.21195 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ded86a54-22eb-368a-9675-74ae0f3c87e6 | -14.35201 | -47.14858 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6c4b359b-60a5-32da-8cd6-9552843278f0 | -15.41824 | -42.0172 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 82bbffe4-a7eb-339e-afaa-746d087a9211 | -15.62699 | -46.25244 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19abf27a-b300-34f6-a14a-0f5e28c27c92 | -21.01788 | -45.1814 | 2025-10-01 03:32:00 | NOAA-20 | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 870172d7-ac49-3af6-a1c6-661014aaf5a2 | -14.89496 | -48.12006 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee2c7275-8af6-3293-8370-3d395b28f42d | -15.35299 | -47.0897 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e6ebc44-2d77-3bad-9d57-87607af57a74 | -20.69303 | -43.3706 | 2025-10-01 03:32:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5220e9db-b8f0-34bd-9471-4edcd3e600ac | -20.61901 | -46.22096 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 63fdc2f3-3a96-37cd-880c-07a18a9be4a0 | -20.2303 | -43.88267 | 2025-10-01 03:32:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 96b179f5-2935-3889-bd0e-609109badf57 | -15.29177 | -46.19616 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 039ccbb9-c069-3ca6-a5ab-85a733a0a9c8 | -14.75105 | -45.76652 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3823d6f9-93ad-37d5-8cb2-6a37e54cfeb8 | -21.57225 | -44.22385 | 2025-10-01 03:32:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c7a50493-b091-325a-8eac-90ca5d911f45 | -14.70199 | -48.13579 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4190afb-0e65-3edb-9714-c178459edee1 | -15.29806 | -46.1974 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72ec6186-8e99-3938-9178-43a9cb978675 | -15.31685 | -46.41362 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 746e5415-0c4c-3c8e-a490-7f17c2f577dd | -14.69971 | -48.22816 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f1f4d492-c808-363d-ba33-6fd38604ea03 | -14.90251 | -47.21283 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8953208-62ca-3ea3-9578-6fa15ad19119 | -16.40383 | -47.06325 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5eb71a77-0703-3910-bdc8-566cf768f4ec | -15.27725 | -47.89697 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d8fedf6-0cb3-3a13-9a6e-9932aabfcbe2 | -21.34076 | -45.87973 | 2025-10-01 03:32:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3ec35839-3777-3379-8207-62a26347321c | -14.62937 | -46.97955 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README24.md)
