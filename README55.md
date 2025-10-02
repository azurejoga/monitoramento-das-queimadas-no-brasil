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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa8807fd-4d99-38ba-806f-f15f610f0824 | -14.44219 | -46.36904 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7c78935b-f957-31ea-ad3d-9bf3bfbc4b8c | -15.24358 | -48.08458 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbf89b23-ee0a-3ff9-877f-128006cefcd1 | -15.70112 | -49.93592 | 2025-10-02 04:04:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8bc88812-a2cf-3f78-b9bb-c30b84f56958 | -12.95214 | -48.43858 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d170155d-e4bd-310e-b34a-3943471abf36 | -13.37295 | -47.28754 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad9ef051-e1b3-324a-bf51-47451547e917 | -19.98519 | -44.24802 | 2025-10-02 04:04:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 59313999-8ca2-3dd5-adc6-154820ac7c79 | -18.51077 | -44.03654 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1cb4fdd-0c45-3133-87f8-35c746c1332e | -19.05121 | -48.13467 | 2025-10-02 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a3874c53-e431-39fd-87ea-b0fb63fb53c5 | -14.44571 | -46.34925 | 2025-10-02 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3331bfbe-1ae0-3b6d-ba9c-1539395323aa | -20.35413 | -48.00848 | 2025-10-02 04:04:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 139faded-22a0-3485-a90e-850a05882d09 | -14.41557 | -46.0792 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 715f2617-d78a-33c8-80fb-f0c881ee12e3 | -21.18342 | -42.8653 | 2025-10-02 04:04:00 | NOAA-21 | RODEIRO | MINAS GERAIS | Brasil | 3156304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6c923de3-7e5b-36b8-a06b-081a2220a599 | -15.93851 | -46.21394 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 86acf611-e66d-3678-8718-9df1ea69a0d3 | -13.37416 | -47.29121 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b98c0b00-3e04-3709-adff-f6351f0cc320 | -19.63135 | -44.90575 | 2025-10-02 04:04:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d883df38-87cd-3602-8c4c-76e2dc957413 | -12.41494 | -54.36341 | 2025-10-02 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61ca8e33-9068-3974-bd89-0bc8f38297b8 | -13.23669 | -48.5068 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 322dc384-b1bd-35c2-88aa-7edec04e8aa5 | -20.73168 | -46.03489 | 2025-10-02 04:04:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 532c97d0-b056-3f47-ad17-dc15d66a4b33 | -13.53224 | -47.25636 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80030eed-6755-30ba-aa71-32411c2f54a3 | -19.70683 | -49.29147 | 2025-10-02 04:04:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3bc2760-6653-3749-8780-3c43e2cdcb64 | -14.19636 | -44.74932 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82b497ad-e65e-38dd-bce2-5757376bd315 | -17.21332 | -46.98642 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ac35299-8fc4-36bf-911a-c5f9e4e65ec7 | -14.68945 | -49.61325 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4118909-1897-3a12-ab47-c73609176f19 | -13.31686 | -47.81878 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15df0b86-2631-308c-be28-9249e065affe | -13.46609 | -47.25613 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d75a4b7-3ee4-3e35-9101-d739048f6d7f | -13.96098 | -48.11628 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| efb64f63-3326-3966-8f5e-30de78e8dbaf | -19.84837 | -43.65849 | 2025-10-02 04:04:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3a8b3a4-b9e3-3816-9a4a-df2f0d8bd771 | -18.5243 | -45.04434 | 2025-10-02 04:04:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ec55749-4613-3d28-a980-6133037e60ed | -14.21828 | -46.11771 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c69d9318-d00d-3cf3-be9b-a4931b05b601 | -14.37683 | -45.966 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9418fe64-37b8-3c0f-b171-b7b9fe93be5a | -22.5668 | -46.7869 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 70075cf8-6959-3512-9da4-471e0e8d8809 | -21.57945 | -44.95594 | 2025-10-02 04:06:00 | NOAA-21 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bad051e6-6513-38f2-ae37-2cf73379b99f | -22.62099 | -44.50236 | 2025-10-02 04:06:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2ddd955c-ecb3-3903-87b0-367ed50deeb7 | -22.55974 | -46.78553 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f7405ba7-a0cb-328f-a9e3-1cec51bdd9cb | -22.57108 | -46.78329 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 2fc4aabc-ff8e-3a08-a357-ad46bf961777 | -22.14052 | -43.16303 | 2025-10-02 04:06:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 09c2d056-d7cd-3b93-95cd-a47868c4f313 | -21.56493 | -45.27394 | 2025-10-02 04:06:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e814af87-07b5-3e34-8f33-1360f52741b7 | -21.67344 | -48.79448 | 2025-10-02 04:06:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 625e51e0-1778-32d7-b81e-924a502801a1 | -20.87521 | -46.46499 | 2025-10-02 04:06:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc5831c5-0b58-3b79-bfe7-bdee594930c0 | -21.94189 | -43.43724 | 2025-10-02 04:06:00 | NOAA-21 | BELMIRO BRAGA | MINAS GERAIS | Brasil | 3106101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0d60e982-4027-3434-bc72-66c5d5c3e25e | -23.07208 | -46.70742 | 2025-10-02 04:06:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6b40cf85-1c56-3406-b74f-f8dc652e3596 | -20.85217 | -49.47782 | 2025-10-02 04:06:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a0d5e8cb-7636-39d0-a603-8a47c5629da6 | -22.28097 | -46.71449 | 2025-10-02 04:06:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8e67b9e2-b9cd-35d4-839d-ccfd5cbd00e5 | -22.25978 | -46.71051 | 2025-10-02 04:06:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7b48d46c-c144-3fd3-abff-c8e2822235bd | -21.66949 | -48.79359 | 2025-10-02 04:06:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b7971879-e8f8-3b9c-830c-6a6ccf1fbb1d | -21.34692 | -44.89705 | 2025-10-02 04:06:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 703d2c8b-9d92-300d-b8b2-c7d23a627a8c | -23.40632 | -46.31698 | 2025-10-02 04:06:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3cfc838c-337b-3bca-881c-58c4a9ae8847 | -22.08009 | -43.09117 | 2025-10-02 04:06:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3668281b-c67b-32de-a95d-40e72d2521ee | -22.56402 | -46.78195 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5bd5740e-dfc7-3c5d-8dc0-c08d53159062 | -21.3239 | -45.66242 | 2025-10-02 04:06:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 47100b13-fe8a-3271-836e-df8ca70e8720 | -22.31145 | -49.59894 | 2025-10-02 04:06:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d963f781-cd91-3b31-b307-55955df568c6 | -22.56755 | -46.78263 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 017eef4a-ab3a-3965-ae2e-ef931cd47534 | -21.56155 | -45.27332 | 2025-10-02 04:06:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8a82c73e-631c-3386-ba54-8d3ab9c1a096 | -21.56092 | -45.27714 | 2025-10-02 04:06:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 551c26dd-5015-3178-839f-d868589cc9b5 | -23.07136 | -46.71163 | 2025-10-02 04:06:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 53b0e8c0-1b2e-312d-9d33-505521683010 | -22.2872 | -46.72059 | 2025-10-02 04:06:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5a3bb2a5-59c6-33a2-8f80-69dd2a870350 | -21.68884 | -45.60749 | 2025-10-02 04:06:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 04e72caa-6891-3732-81bd-82c4284cf38e | -21.0439 | -46.91617 | 2025-10-02 04:06:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7223701-2aba-3371-b91d-1046ab6f48fa | -22.99803 | -48.26926 | 2025-10-02 04:06:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f4cc0fca-e23d-3134-93fb-258b3587c550 | -22.36155 | -48.60374 | 2025-10-02 04:06:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 35fd06aa-4289-3bbd-adc7-1bfce2e777fc | -22.97898 | -48.35179 | 2025-10-02 04:06:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4a1b578b-a72d-39d0-bacb-c3e2d4c6b286 | -21.34629 | -44.90084 | 2025-10-02 04:06:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bbe3f921-a5c8-3c9a-8fdb-27d03311ef86 | -22.68159 | -47.64383 | 2025-10-02 04:06:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 65d7fc58-284f-3908-a6a0-672b5b8df14b | -22.28447 | -46.71533 | 2025-10-02 04:06:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| daf5438f-8f4e-3efd-b63d-fc49454ff886 | -22.08123 | -43.08372 | 2025-10-02 04:06:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75d852f9-ae55-321e-9aa9-9a247e442711 | -21.66861 | -48.79824 | 2025-10-02 04:06:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db858a42-9025-347b-88be-d15406c038e4 | -22.98374 | -48.34727 | 2025-10-02 04:06:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f13cdb09-e373-3449-b71a-e325f0a7dad1 | -21.66466 | -48.79739 | 2025-10-02 04:06:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 93b50a44-2482-373b-8348-8d680cf24ce6 | -21.78766 | -47.20443 | 2025-10-02 04:06:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8b7ae72c-9740-367a-80db-dd06243f0403 | -22.56251 | -46.79052 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f65e5b6d-a8e9-35a1-a11c-978e06643ed1 | -20.85633 | -49.47881 | 2025-10-02 04:06:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bde2c5f1-c26a-3020-b813-a08eb389d88f | -22.07321 | -48.45425 | 2025-10-02 04:06:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1426d530-d0f1-350d-a995-281764c9b2e0 | -22.55546 | -46.78912 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d6863410-0264-3c7d-9b71-a2e3791be6fe | -22.25204 | -43.05666 | 2025-10-02 04:06:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 415f7dc3-167e-3e1f-aeb5-c97da99d5cff | -22.27944 | -46.72327 | 2025-10-02 04:06:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 667e0929-33b7-34d5-b666-ec861829ffd8 | -22.23713 | -45.92353 | 2025-10-02 04:06:00 | NOAA-21 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c19005ad-311a-3165-9c30-94246c8439f8 | -20.84349 | -49.43325 | 2025-10-02 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| 42a4dac6-cff8-3dc6-8561-d06da5c045ca | -22.24357 | -43.42144 | 2025-10-02 04:06:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2a26f7de-2577-3d4c-9f1c-d4f53ba420fa | -21.66722 | -48.80561 | 2025-10-02 04:06:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 101f62d7-bd7a-303b-bae3-49f4f6285ed5 | -23.07281 | -46.70323 | 2025-10-02 04:06:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 03b609d1-aa34-3e5d-96ec-78affe972e89 | -22.23746 | -45.92459 | 2025-10-02 04:06:00 | NOAA-21 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dee0c337-3399-3979-b617-a66f536b2ad0 | -21.23683 | -44.06731 | 2025-10-02 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3c9fa876-b29b-3db0-bd10-a0334acf9ae0 | -21.78484 | -47.19913 | 2025-10-02 04:06:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cc8ef118-002d-35a1-be73-290ede624c5b | -22.62159 | -44.49864 | 2025-10-02 04:06:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 968e968f-3b15-30a3-9bc3-aeff9534319b | -21.78848 | -47.19982 | 2025-10-02 04:06:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dd3d43e3-076d-3b09-bf78-2e010b586233 | -23.12487 | -46.9284 | 2025-10-02 04:06:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7c85878b-bdd0-3b4b-bf16-98b9fd8b0373 | -22.60126 | -49.02973 | 2025-10-02 04:06:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af489a84-7819-3bf7-aaf8-837e4a6443be | -22.77927 | -42.89457 | 2025-10-02 04:06:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1d6ab638-d34f-3e79-bd41-f01cbd2b7874 | -21.23743 | -44.06362 | 2025-10-02 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5450db20-ae6b-3f9d-8298-37003dce3eda | -22.57537 | -46.77965 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 5ba3b79e-8d52-3a8a-87b1-f11917bc266d | -22.6231 | -44.51046 | 2025-10-02 04:06:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| a9bf24f9-e872-3555-8405-e96adc8b38b1 | -21.36779 | -43.88577 | 2025-10-02 04:06:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 48363507-ab48-36d5-bd30-90ff277c7762 | -21.73636 | -50.30837 | 2025-10-02 04:06:00 | NOAA-21 | QUEIROZ | SÃO PAULO | Brasil | 3541802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e39d9dc1-70a7-30a6-858c-f54ba9ae26a4 | -22.6093 | -44.12751 | 2025-10-02 04:06:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 90f627f5-6374-363f-9545-cc0173290866 | -21.901 | -47.60309 | 2025-10-02 04:06:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c28c224f-db8a-3d54-ba4d-a508456b211e | -21.66653 | -48.80926 | 2025-10-02 04:06:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f6030f6-f26d-3bf6-9393-8b3b0639bf24 | -22.62431 | -44.50298 | 2025-10-02 04:06:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 79ff628e-6b10-34ea-b914-3e23e547ca02 | -22.5683 | -46.77835 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b546d84f-fb20-30aa-bf49-47f24fc904c0 | -22.08398 | -43.08801 | 2025-10-02 04:06:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ee2aaf9f-1d08-3f58-9a6e-b77dd63caac2 | -20.87598 | -46.46056 | 2025-10-02 04:06:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README56.md)
