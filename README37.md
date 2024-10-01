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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c042442-b7f5-3039-81da-4eb85031f58f | -19.25067 | -43.34737 | 2024-10-01 03:28:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7f0b065d-e835-3abf-9949-d434717fe8ef | -19.24992 | -43.35092 | 2024-10-01 03:28:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0f1143a0-69b7-3732-a6bd-978b70ab3e64 | -19.24919 | -43.35437 | 2024-10-01 03:28:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 7c47f6d3-4414-3ad9-8b93-3194e1a3bc51 | -19.24849 | -43.35772 | 2024-10-01 03:28:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 25fd8f09-7c20-3f38-815c-8038cc705639 | -18.87459 | -43.63182 | 2024-10-01 03:28:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 067dbc51-65ea-3821-9f02-fe18d7b4c6f2 | -18.87454 | -43.63363 | 2024-10-01 03:28:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 27dbaded-4091-3042-9d1e-39abe973a5a0 | -18.8739 | -43.63496 | 2024-10-01 03:28:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a0dcd9fe-d549-3a54-a236-a8a991bb35f5 | -18.87386 | -43.63685 | 2024-10-01 03:28:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0b3130bc-0199-32da-99d2-f4ce9d35f3f0 | -18.54059 | -43.37054 | 2024-10-01 03:28:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 35d9a716-f448-3895-9772-74c6df9e0a6e | -18.5364 | -43.47021 | 2024-10-01 03:28:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| e5bd2425-d65b-3a1d-8e09-83e0a18578ef | -18.53596 | -43.36557 | 2024-10-01 03:28:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 11d77654-831b-3524-b216-dd6c43c5cdb3 | -18.53523 | -43.36897 | 2024-10-01 03:28:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| dcd921d4-7785-37d6-9958-c0a26ce13164 | -18.19239 | -43.82583 | 2024-10-01 03:28:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56ea0630-389f-32ed-b2a9-5a824a06a8f3 | -18.1899 | -43.82231 | 2024-10-01 03:28:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf3b646f-1150-3d99-9cf0-822bf7f12304 | -18.18907 | -43.82611 | 2024-10-01 03:28:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffba79f9-3e28-3e5a-a756-259b85b52e8d | -18.18764 | -43.8204 | 2024-10-01 03:28:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e641908-5fb8-3ac7-9769-3cb014988db9 | -20.18998 | -43.52107 | 2024-10-01 03:28:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 642e1716-7882-3106-a202-bdb4a2bdb4d8 | -19.99217 | -43.54245 | 2024-10-01 03:28:00 | NOAA-21 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8c5dd2c8-a51a-3da3-a8ad-ecba6e9080c5 | -19.98969 | -43.54168 | 2024-10-01 03:28:00 | NOAA-21 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ca9719ea-f179-3715-9c7b-7713023ecb97 | -19.9869 | -43.54092 | 2024-10-01 03:28:00 | NOAA-21 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e41583b8-dff8-3a3e-9f2a-5790fce7059c | -19.6082 | -44.11495 | 2024-10-01 03:28:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e9104b5-5c46-3ff3-8fb7-adf438f857af | -19.60737 | -44.11874 | 2024-10-01 03:28:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41597a80-7921-330f-a5b9-eeb85d66b63e | -19.60261 | -44.11375 | 2024-10-01 03:28:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2c88bad-d24d-3591-868a-a9b9a4e35eb2 | -20.07804 | -44.6013 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9b52ce6-8799-314f-a048-0bbbe4a9afbc | -20.07705 | -44.60566 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2b21023-f7f3-350f-91bd-86cfff881c68 | -20.07613 | -44.60242 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3744c326-a040-369a-b1eb-61fbc94cba3b | -20.01506 | -44.52797 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 4c434a8b-879f-3afa-8373-6b85b2da5393 | -20.01415 | -44.53203 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c9a0ecef-fb44-397c-b8d5-4ff19dc7d459 | -20.00949 | -44.52623 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 2ceafe91-8376-3ce6-8d6d-e82ad8c45598 | -20.00857 | -44.53031 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 13973e54-7f9d-3164-b51e-63c0c706c8d1 | -20.00764 | -44.53446 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 9b8a7d39-8f4d-3f9b-b2be-e04249917bac | -20.00669 | -44.53868 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 71c3d271-1441-3414-9cca-daa52ddb077f | -20.00295 | -44.52876 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3a5fedf0-e044-319c-9a42-f180b51ea955 | -20.00199 | -44.53306 | 2024-10-01 03:28:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 37ec68c5-444a-3930-bc8a-f41daa10ab33 | -22.20082 | -45.03964 | 2024-10-01 03:28:00 | NOAA-21 | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e4825a02-2832-3fc5-84ab-2fb921f7bca4 | -22.05649 | -45.26877 | 2024-10-01 03:28:00 | NOAA-21 | OLÍMPIO NORONHA | MINAS GERAIS | Brasil | 3145505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 19c3851d-cb25-36b9-b924-ffaa09662ddb | -23.07941 | -45.40039 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| c7b6570f-df14-3e9c-a02d-70f1324ca4b8 | -23.07844 | -45.40456 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| f2227a02-28ed-36c1-b9ce-d1705f2f4cd4 | -23.07768 | -45.39597 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.5 |
| 03db795a-e54a-3358-945c-228239af9c07 | -23.07733 | -45.40929 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| debd8526-56c3-383c-9117-62b1d3ff0ce2 | -23.07676 | -45.40004 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.5 |
| 9efe521f-d673-3792-a8e9-7608b3a04d09 | -23.07577 | -45.40439 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 084ad618-1ec0-3516-a023-6e6532876b9c | -23.07504 | -45.39375 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| a0371c3e-38e2-3183-9136-af815a69465b | -23.07468 | -45.40921 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| f361fca0-4822-304d-bf0e-f937af5b3f7a | -23.07409 | -45.3978 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| c29b2d56-9b7c-3118-9c27-bdac36f48642 | -23.07306 | -45.40219 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 27887b79-9cb1-3ed0-a20a-51c1328992f1 | -23.07237 | -45.39328 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| d018dd6f-100c-3cfa-93d4-f2f51d223b27 | -23.07194 | -45.40696 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 4d309273-ab78-380c-beb7-2580c3aee2d6 | -23.0714 | -45.39754 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 7c3ea30b-f1f9-3019-98bf-fab946a0d1a7 | -23.06917 | -45.40736 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5ade2983-f05a-308c-ab18-76b985ff5a80 | -23.06861 | -45.39587 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 412228aa-42f5-3720-ae02-39713f8ed602 | -23.0674 | -45.40102 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| b0477d41-2efe-3b0e-a00d-0afb338d382f | -23.06447 | -45.40197 | 2024-10-01 03:28:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| afb56b8a-ed55-3f11-932f-218181b8f46a | -22.54126 | -44.30736 | 2024-10-01 03:28:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 00cc7eea-4471-345f-a95c-5772167e5c60 | -22.53905 | -44.30314 | 2024-10-01 03:28:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f064aff7-7eca-33d3-af3a-a2c38c23bffa | -22.53825 | -44.30678 | 2024-10-01 03:28:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 37b96826-d6e4-3bd4-b295-ad2199ebbb33 | -18.80933 | -45.80365 | 2024-10-01 03:28:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5eb4a1da-cb30-3cb7-b692-2a3ea9feb0d1 | -18.80703 | -45.80006 | 2024-10-01 03:28:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 873a2efd-b7b2-33eb-8b70-08ecb5d4ba1c | -18.80586 | -45.80508 | 2024-10-01 03:28:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b2aadaf2-7690-32ff-928f-6369ef4c81be | -20.59773 | -46.244 | 2024-10-01 03:28:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10acd409-2744-39c9-89de-136c3a948fc5 | -20.59593 | -46.24296 | 2024-10-01 03:28:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a10ad49c-1a38-33ec-98dd-fd6fba0981dd | -20.53415 | -46.29243 | 2024-10-01 03:28:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3fca48bc-170c-3534-a3f3-768b47aed766 | -20.52653 | -46.29697 | 2024-10-01 03:28:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 85ed4c12-0031-3adb-b0a9-76c033a34bc9 | -20.51871 | -46.30231 | 2024-10-01 03:28:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7975866-5520-3d0b-84aa-1477f0815d8c | -22.1239 | -45.92101 | 2024-10-01 03:28:00 | NOAA-21 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fddc5a9d-1aaa-3f70-bfc0-bdf293447065 | -21.33499 | -46.43068 | 2024-10-01 03:28:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 13cb166e-0907-3648-8f0c-e38027663ca2 | -21.33369 | -46.43617 | 2024-10-01 03:28:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 59afc24a-5699-3415-918f-21ac0715bd6b | -21.32851 | -46.43053 | 2024-10-01 03:28:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| a0d4295f-6c66-317c-8d52-01d75a561040 | -21.31005 | -46.64579 | 2024-10-01 03:28:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| cd091255-83d6-39fa-9353-91f14087817a | -23.12068 | -46.41321 | 2024-10-01 03:28:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fb384de0-c796-3060-afd6-25e7032e1f62 | -23.10378 | -46.59087 | 2024-10-01 03:28:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1b0c9682-4e12-390f-9f92-cdeca090d3b1 | -23.10349 | -46.59798 | 2024-10-01 03:28:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e36a2e36-6284-304e-912f-a29fa1575898 | -23.10265 | -46.59565 | 2024-10-01 03:28:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9cdc9c9d-7e93-389d-b6e5-397b26178a57 | -23.09995 | -46.58641 | 2024-10-01 03:28:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8bf79397-0695-34d0-be81-ff1f0954b59e | -23.09943 | -46.39678 | 2024-10-01 03:28:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 75b9ee68-78ee-30a5-971c-640047f18de3 | -23.09808 | -46.40241 | 2024-10-01 03:28:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 77658708-02bf-3622-a8e5-38c8de197ab1 | -23.09483 | -46.38971 | 2024-10-01 03:28:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 443dff43-aece-39e6-a909-f8f01457bb23 | -23.0811 | -46.90066 | 2024-10-01 03:28:00 | NOAA-21 | LOUVEIRA | SÃO PAULO | Brasil | 3527306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 887d9f98-e7b9-3478-9843-8d8c7384726a | -23.07988 | -46.90569 | 2024-10-01 03:28:00 | NOAA-21 | LOUVEIRA | SÃO PAULO | Brasil | 3527306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c89f0ed1-8822-38ce-bad3-7b2c8a21380e | -22.95873 | -45.96331 | 2024-10-01 03:28:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9f48a9cb-05f1-38b7-96db-5ec2313d0d25 | -22.35569 | -49.32993 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c4b2d649-1f87-3e74-ba93-a42fe2013546 | -17.58963 | -46.95828 | 2024-10-01 03:28:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 88fc92a0-eb4d-3513-8f76-0edab8268757 | -17.58341 | -46.95711 | 2024-10-01 03:28:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3f3f1b7f-989c-3a8c-9f23-f983bd03bb3c | -17.58037 | -46.78215 | 2024-10-01 03:28:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91055661-8452-3945-9357-fc5bffd69f32 | -18.94921 | -46.9301 | 2024-10-01 03:28:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f04c68d8-8290-3526-9f1c-3fb1782ab749 | -18.94783 | -46.93592 | 2024-10-01 03:28:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59433387-d7b1-3693-9264-38e61ee73ed3 | -19.78661 | -47.9657 | 2024-10-01 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34ad97af-81c9-3758-a978-75811ab163d5 | -19.77974 | -47.9639 | 2024-10-01 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a6f2467f-8541-3e1a-b081-a8893da2023f | -20.09788 | -47.34885 | 2024-10-01 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 572e3d5c-7e1d-3895-a900-42c451c1419b | -20.09484 | -47.34692 | 2024-10-01 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f5fc2ca6-bd7d-3378-868b-7d6b8cbaed97 | -20.09142 | -47.34654 | 2024-10-01 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c620342e-e62a-307f-a556-283984bd9f20 | -19.76077 | -46.63075 | 2024-10-01 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57952864-c0ac-359d-b4d3-cbfc9c44afb7 | -19.75938 | -46.63658 | 2024-10-01 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c4c9d62-7a21-3052-9ed8-705d1f290c2b | -19.75404 | -46.65908 | 2024-10-01 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4c38fa2-cdd4-37e3-9d59-ad43008f99d4 | -19.7527 | -46.66475 | 2024-10-01 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb48bca8-bc52-379f-9ad2-e4f2e45f2918 | -19.70041 | -47.23627 | 2024-10-01 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3877386-b3e0-3c90-94b5-b743dd6e54db | -19.69765 | -47.2324 | 2024-10-01 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 09227a7a-2736-3c59-aec5-e441365a2988 | -19.69604 | -47.23903 | 2024-10-01 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7d21049-dab1-3550-b0f2-3d0d74c88492 | -19.69391 | -47.23405 | 2024-10-01 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a6f6804-fda8-3092-9f67-1a541caa6fcf | -19.68941 | -47.23736 | 2024-10-01 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README38.md)
