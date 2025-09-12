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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2517aecc-bc4a-3cb3-a8da-17d21b969917 | -11.48404 | -49.26554 | 2025-09-12 06:10:00 | AQUA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b4251397-1cae-3beb-a56f-087117bb4140 | -12.91809 | -54.75447 | 2025-09-12 06:10:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a089c2ea-85e9-3265-a3b5-bfe6c6ea3ca3 | -11.68946 | -46.60705 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 563be76e-27b1-38d3-9a0b-1d96dc599305 | -19.99011 | -46.91674 | 2025-09-12 06:10:00 | AQUA_M-M | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 2675ed6f-6049-3818-b54d-672d99446e5b | -15.21683 | -49.67685 | 2025-09-12 06:10:00 | AQUA_M-M | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3297282f-1b75-3397-9aee-28b2fb1b8fdd | -15.08223 | -52.43697 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8effdd5d-4c72-375e-9834-9f9e04dd4b62 | -11.67017 | -46.59081 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| cd27cbbb-a9f8-3488-8830-4d43dcbbefee | -14.3253 | -54.13013 | 2025-09-12 06:10:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 67ce7113-29e2-359e-ae9c-8313ba7ff27b | -17.37853 | -52.9552 | 2025-09-12 06:10:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 449a17ba-7fd0-3b73-878f-23e3338b6d71 | -11.53976 | -50.39892 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 4e81ed52-ceac-3cb2-9412-954a1cb046f0 | -15.92074 | -51.78622 | 2025-09-12 06:10:00 | AQUA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c4a21f56-e7a5-3d09-b7f7-f58fbaaa04f6 | -14.32707 | -54.11917 | 2025-09-12 06:10:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 24c48691-da4e-30dd-a57a-8b346cbeb76d | -11.68789 | -46.58541 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 91e1f176-3e26-3d53-85c2-644debf21ac1 | -11.9381 | -51.17613 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d61d7c37-7824-37a6-ba33-bfba3742395d | -12.8929 | -47.9589 | 2025-09-12 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bb4bdf84-ce43-3d7b-a768-889144e950ba | -10.08095 | -50.38844 | 2025-09-12 06:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 32dbee82-578f-3fe6-bcc5-055c994ba810 | -11.68072 | -46.59243 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9756dc9b-4991-3402-86a1-254cb67a8099 | -11.93946 | -51.16716 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6f3307b1-35e0-37b7-b727-8fa0679f2223 | -9.89114 | -51.87144 | 2025-09-12 06:10:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| da841bc1-be7e-3f26-b3f6-6499e56f84a3 | -16.2581 | -46.78539 | 2025-09-12 06:10:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 06222a91-8906-3f14-8ce1-4d8ba48f047d | -9.9637 | -51.69688 | 2025-09-12 06:10:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ee64f169-c6e1-34ed-9142-e51e1cf87c33 | -11.64982 | -50.57731 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 011d307a-15f8-3b76-b2f1-ee160b7b2280 | -10.54422 | -51.53079 | 2025-09-12 06:10:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0cfd3782-8d34-30e8-963d-9af158dde104 | -11.52349 | -50.38734 | 2025-09-12 06:10:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8e2b0527-d9e6-33ea-ba41-73b60a1240c0 | -11.94691 | -51.17749 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4c83e181-06cf-3fcd-9a89-21d1bb395299 | -13.53562 | -43.00737 | 2025-09-12 06:10:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 85c928f6-1c9d-383a-88bc-bf234c1c6ce2 | -15.52152 | -48.544 | 2025-09-12 06:10:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 77c724af-17ca-3197-ae0e-0bc5e82b48f0 | -16.25788 | -46.78012 | 2025-09-12 06:10:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2ad5f45f-b586-3bfa-834a-3817cb111570 | -11.70336 | -50.6003 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 72ccba3a-02c8-3e8c-ab83-2936b05def82 | -11.80017 | -50.56697 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ca59ac84-8a18-3dd9-9b8e-7d82b0ad73ee | -16.49567 | -51.96743 | 2025-09-12 06:10:00 | AQUA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02ae5b6d-abb7-340b-8b72-a1fd27544ba1 | -14.43206 | -52.93296 | 2025-09-12 06:10:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3196bbc5-f110-39ff-83d6-485e718167fe | -11.19064 | -55.06818 | 2025-09-12 06:10:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7766861a-ab19-341f-939c-da245e74be25 | -16.60835 | -49.79886 | 2025-09-12 06:10:00 | AQUA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4d493394-a925-35a2-9c67-308dabfbbb7c | -15.15406 | -52.39719 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d8b9933f-d911-33ed-ae96-9935ca3c5d54 | -16.24933 | -49.47607 | 2025-09-12 06:10:00 | AQUA_M-M | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2f767f56-98ea-346a-a6d6-19d3d403bea4 | -16.30128 | -50.07978 | 2025-09-12 06:10:00 | AQUA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 393f6132-3e94-31dc-9b6c-4a24421b0dcf | -10.41114 | -50.59022 | 2025-09-12 06:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fb9ebd8d-818b-3687-8776-78a28ac4802a | -11.53676 | -50.59906 | 2025-09-12 06:10:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b8f4b90a-8059-3474-a571-987b9b5ee220 | -15.60124 | -52.73674 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f72cfc88-6302-3e91-b2b0-1551c8421fb8 | -11.66837 | -46.60392 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| adbb69fd-206f-397c-97a9-69b0886761c7 | -15.91057 | -51.79391 | 2025-09-12 06:10:00 | AQUA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c8bd3291-a6b0-33ea-995a-e8594d3f1bd2 | -16.26702 | -50.06822 | 2025-09-12 06:10:00 | AQUA_M-M | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 37dc8c27-b234-3515-bbbb-1dd93c39f28a | -10.67778 | -48.65394 | 2025-09-12 06:10:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4411a4db-faf2-380f-9031-460d2ff41f86 | -15.53279 | -48.53442 | 2025-09-12 06:10:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5f563323-a3f7-3922-843f-b970769bbd85 | -17.1312 | -48.49727 | 2025-09-12 06:10:00 | AQUA_M-M | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 198cbfb8-0d66-3c1a-995b-8d7683c97d5d | -9.89729 | -51.8918 | 2025-09-12 06:10:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 56cbb724-99b5-35f5-86d0-8cbbc21a2429 | -11.67891 | -46.60555 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 5a87311c-294f-3f6c-895b-4b51d766c74c | -12.93034 | -47.9766 | 2025-09-12 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 71a378c9-b512-332e-a090-a26dd4f221ea | -11.52931 | -50.58882 | 2025-09-12 06:10:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| fce48c24-74c3-3040-b838-e3d13af0c0c7 | -11.68614 | -46.59875 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f858fc0e-f365-3b2c-b0df-bd1674570484 | -12.92584 | -48.00901 | 2025-09-12 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b0d27159-c21f-3b7c-a014-05e594341f27 | -11.68272 | -46.62475 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 79ee1236-a70a-3455-9c96-98afd8ea34b9 | -10.84965 | -48.15515 | 2025-09-12 06:10:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fcbdba96-1ed6-399e-9720-ed79e47856a9 | -15.60273 | -52.72731 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7ca51c9c-50b9-3151-ba43-29eb90d14de4 | -11.79137 | -50.56563 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3dba0ae1-d22e-343c-994f-7c3701ea482b | -11.68964 | -46.57215 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 0e7f0c5e-63da-3844-b179-72d147e4feab | -11.78258 | -50.5643 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 18c7586c-52c9-39c9-b590-18e4695680d8 | -11.42882 | -43.54213 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 15aa2623-01e7-30c7-a96e-c3cc620169c7 | -12.0827 | -47.59668 | 2025-09-12 06:10:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4d5804e9-6140-3e0c-9118-4e853189f47f | -11.68444 | -46.61165 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 18f2e648-adc3-3f3e-bebc-428a979d5008 | -11.9195 | -50.69124 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3dc1813f-33cb-392b-ae62-f93eb64fef92 | -11.11436 | -50.71029 | 2025-09-12 06:10:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0d3c57a4-e56a-390e-b54b-f0a3e91bff65 | -16.09884 | -49.62482 | 2025-09-12 06:10:00 | AQUA_M-M | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c0f763dc-e858-34c3-b3af-7e33baec93ae | -16.43602 | -49.03884 | 2025-09-12 06:10:00 | AQUA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5a39c1e1-43c2-32e0-ad41-847ed1c28d70 | -14.44885 | -47.31495 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f33e285-2033-3551-a378-e6e546963feb | -13.19108 | -51.75961 | 2025-09-12 06:10:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c0cd0f88-355b-37ef-9a20-61860641ac19 | -13.90248 | -48.27217 | 2025-09-12 06:10:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 43.5 |
| f4492c70-2e58-3376-be69-2dfc1ad0dbf2 | -12.9273 | -47.99851 | 2025-09-12 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 760c9c42-b6d4-3d18-a51d-7c086ff8008e | -15.11635 | -48.59837 | 2025-09-12 06:10:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3ec57262-6a34-3f52-a07a-ac858554b176 | -17.37547 | -52.91618 | 2025-09-12 06:10:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c93c2e2e-8dc8-3aa4-8efa-8f7d8eb0ff34 | -14.43285 | -48.43017 | 2025-09-12 06:10:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 18d88afd-5ab6-3065-bc0d-d9170e256802 | -13.22041 | -51.7456 | 2025-09-12 06:10:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1eefdd56-d4d0-393e-ace6-06e8890cd679 | -11.53229 | -50.38866 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d2fab8dc-6c2d-3e9f-882f-bd2d0e8e51d9 | -11.64848 | -50.58623 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 07db726e-3eff-3c0e-9e7d-d1281b608572 | -11.69499 | -46.61321 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 9b502c15-5559-3bba-b3b7-4bc4b2a13ab2 | -12.98553 | -46.73991 | 2025-09-12 06:10:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 13b1151d-812c-32af-ba33-f42535de89ac | -16.25176 | -52.65031 | 2025-09-12 06:10:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2402f21b-54c1-3db5-93bb-6bf1b49c2797 | -19.24004 | -48.03455 | 2025-09-12 06:10:00 | AQUA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 9a77a698-9313-325e-9e20-0fea1c290db1 | -11.53543 | -50.60798 | 2025-09-12 06:10:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 214098ac-eab5-3383-913b-df345bf702b2 | -15.78826 | -52.24139 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d85e86ea-d6a0-3d28-aa83-152648a29aa6 | -14.17081 | -46.1754 | 2025-09-12 06:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| aec3f937-2887-3e06-b4bc-53c458d30b23 | -15.81016 | -52.21664 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fc8a34df-ea77-3923-b3f2-1dad6594be26 | -14.56014 | -54.51365 | 2025-09-12 06:10:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2f1a32f9-b20d-3034-94bd-8446d42c8f50 | -9.9878 | -51.71989 | 2025-09-12 06:10:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d7cd8e6a-7db9-3f79-8245-2a6fd22fee96 | -10.07675 | -47.16782 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 55c65d70-1199-35b3-b2b5-6abfc8f78289 | -23.13137 | -46.75484 | 2025-09-12 06:12:00 | AQUA_M-M | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| db5aeaa8-27be-3752-bd54-32d34310477c | -21.61015 | -53.98898 | 2025-09-12 06:12:00 | AQUA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 15018a7f-e374-3130-9abd-f9ca51353f0b | -21.63687 | -53.99367 | 2025-09-12 06:12:00 | AQUA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f3a7de6e-0d63-3e90-aacb-c3121b457340 | -22.6173 | -53.086 | 2025-09-12 06:12:00 | AQUA_M-M | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| d38e4496-5a10-3c02-ac41-f2a994bcbd37 | -23.13352 | -46.73449 | 2025-09-12 06:12:00 | AQUA_M-M | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.9 |
| 07137da0-83a1-3977-9b9e-b42410068844 | -23.11042 | -47.50061 | 2025-09-12 06:12:00 | AQUA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 646cfb25-6828-3832-8856-4dcf0db8c135 | -22.17313 | -49.73896 | 2025-09-12 06:12:00 | AQUA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 8abb6e4d-311c-393b-b231-10dc06dc75f3 | -21.63838 | -53.98405 | 2025-09-12 06:12:00 | AQUA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 95bb2fd2-2bb1-39cb-b8d2-e84b4b862cfa | -23.11745 | -47.50668 | 2025-09-12 06:12:00 | AQUA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 61332b4f-5dca-3005-8aca-f2c1ad5ee5ea | -23.13189 | -49.66058 | 2025-09-12 06:12:00 | AQUA_M-M | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 7aa3f523-b1d6-3eca-8b54-3f644006b88f | -21.91754 | -50.49922 | 2025-09-12 06:12:00 | AQUA_M-M | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| c738ebe6-97f7-3907-8611-0fbd85a54cc2 | -23.11938 | -47.48907 | 2025-09-12 06:12:00 | AQUA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| a5f8d3fe-4824-34c8-a2b8-e661ba080ca8 | -21.92244 | -50.49561 | 2025-09-12 06:12:00 | AQUA_M-M | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| c7501834-3cf2-3842-8ca1-3dd799024308 | -22.17471 | -49.72684 | 2025-09-12 06:12:00 | AQUA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |


[Clique aqui para ver as próximas entradas](README119.md)
