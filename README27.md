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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7ee984b-e6e4-3ab3-aeeb-dc15270ca3c9 | -8.59672 | -54.79049 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d4ddc705-de0f-3d06-9bae-442e8ac1cdaa | -8.22118 | -54.95992 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a22fc53e-aecf-33f6-a38a-7a1917d6d543 | -11.28162 | -54.03305 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 12dc36ff-224d-372e-a1a9-ad945f936740 | -14.9865 | -52.59698 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57388691-cea6-3e50-982b-f48bc9e84756 | -16.33042 | -48.06723 | 2026-08-28 04:17:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32bb0b67-ae6c-350b-a12b-21eb074264d0 | -14.88203 | -52.6001 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9b2a50aa-e56f-3061-b485-53275d190761 | -14.87273 | -52.63841 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43ae192a-4f37-32fb-b520-a2389e27fe7d | -10.80005 | -54.01697 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6a97c53-1d39-3743-aefa-d3fb22c3ec01 | -9.09236 | -48.59438 | 2026-08-28 04:17:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64b94c37-229e-3546-b12b-1160b681ee71 | -13.45862 | -43.84072 | 2026-08-28 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c101af9-84ad-3ed3-b2ce-a6b92e95df32 | -11.38621 | -45.14399 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43a325ea-8527-3a3a-8aaf-7e78c3c66387 | -11.20162 | -55.09741 | 2026-08-28 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f3f80e3-8b83-3663-a537-110304a05620 | -12.45529 | -46.524 | 2026-08-28 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 427d8e5a-12f0-3667-907a-5e30a42075c8 | -11.72408 | -54.54569 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09cac691-d140-3496-aa5c-364570ee2571 | -9.15604 | -49.96702 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5d0c54c-5df2-3172-afdb-a4956ce3a3d8 | -12.20221 | -50.5741 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3477dd49-5e91-3c3b-846e-db5ded9dd8f9 | -9.4606 | -51.71526 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 98dd2b1a-b922-3b9e-b922-9cb0cf92a037 | -14.19148 | -52.83264 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 51424829-4a59-3a6a-918d-dfc7ea0c71b7 | -11.81187 | -47.20098 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83373e0f-d6b9-355a-8222-c8b27c59cdfd | -9.98687 | -48.59607 | 2026-08-28 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5d7ad49d-2fce-3f0f-ba60-0f1ca340bd09 | -20.35868 | -46.47534 | 2026-08-28 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1079c4be-d63b-341d-afa7-aab44282f6ad | -14.41099 | -52.58562 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b93e1b8-cd68-3810-a32f-07acec53fe63 | -13.83833 | -54.04735 | 2026-08-28 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a715a74-fc52-3451-904c-96ec91310816 | -11.27757 | -54.02483 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2a763c90-e432-3621-8e2b-79ecba4cfe29 | -11.77124 | -47.66051 | 2026-08-28 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c593188-71cc-3518-9a39-2edeeec99b90 | -11.71294 | -54.5435 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aae07be8-e017-303a-9717-044c2b5acb47 | -14.93164 | -52.60765 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e020fca7-5abd-3a70-806c-bd3f06eb66ae | -14.59856 | -47.97727 | 2026-08-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3638cf5d-8cca-3736-966f-e377ad0215ae | -11.81757 | -47.21024 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7557ea21-a380-3389-8edc-21f77db9e26b | -14.86423 | -52.61813 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ddf0a685-6657-3cbf-90dd-d00c8c7feee6 | -11.57025 | -45.54752 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b46b05c-5521-373b-aa98-49f5f4dd85f9 | -9.43466 | -51.69362 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 940823fa-6ed7-39bd-a62a-4203a6dae18c | -11.28982 | -54.01964 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01aa6484-aa11-3ea5-a04c-0d8aaed84fc5 | -9.97288 | -53.9356 | 2026-08-28 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c72ee4be-6da1-3b1d-9224-889c5c705c62 | -11.22597 | -53.99277 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ce82096-a9d4-3cb4-9dd5-99736c52f42c | -14.87524 | -52.63666 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2b08950c-cd71-38b7-9c03-7826bafa1f18 | -10.96209 | -50.29799 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9608b36e-d22e-330a-b351-c5736a04919c | -13.32097 | -48.20487 | 2026-08-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e0e387af-571e-355b-9803-48f9c877d2e2 | -14.22255 | -45.25451 | 2026-08-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e95006f-0fa8-3a5b-ab61-638255d20fd7 | -12.76769 | -44.27092 | 2026-08-28 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edd6c77e-377a-320a-b913-f77bfddc61ec | -12.26444 | -50.58871 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7dadb031-e9ef-3ddc-b3d8-1782cb2595a8 | -11.81119 | -47.20502 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7ce86ea-8710-35cb-9e4a-f7640043fc64 | -12.42588 | -43.41611 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb75867a-9d9c-3ca8-b79e-e57e590d2251 | -14.9429 | -52.59898 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bc1dd076-b3c6-30ee-948b-a810d3866c3a | -14.19197 | -52.82926 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 92131da8-9011-359f-9842-495fe35f1332 | -10.90597 | -50.52874 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8040973-b3ae-3323-bff1-322b83fd18fe | -14.85961 | -52.61711 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ebf430f-edaa-3cf1-b710-dd57b4202d81 | -11.16112 | -45.06357 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 830963bb-8280-3e49-b4e6-e7b09a3e66cd | -10.79048 | -54.00751 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b6a3641-b99a-3071-a85e-487b5b5d4c80 | -10.01435 | -46.4113 | 2026-08-28 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6deb9bbf-22b3-3e07-bdd8-0be5caa3d167 | -11.20681 | -51.24525 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 844b0817-5e10-31a5-b44e-81c4481c907e | -8.15898 | -54.9531 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75a07003-5449-356f-b5d6-14178f5fd831 | -14.89008 | -52.59853 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1cb7c17b-c00a-3561-ba06-881a94fb65c7 | -16.83851 | -39.33201 | 2026-08-28 04:17:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 14b0e722-f495-3d63-af8a-15273e8fbc72 | -10.98429 | -51.08558 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db8a39fc-36db-3611-bda3-b4ac030307fa | -10.09912 | -40.91734 | 2026-08-28 04:17:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 78eaf1a6-841c-3310-9c60-627ffb776284 | -10.64068 | -44.74013 | 2026-08-28 04:17:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b3bd919-b54d-311b-867f-19695d277a13 | -11.19452 | -51.22937 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| b62f5cf1-3ab8-3626-a0b0-20e536015dc7 | -16.04976 | -47.23331 | 2026-08-28 04:17:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b919c8ab-bf14-3c50-9d21-fe71603d0819 | -11.37956 | -45.14292 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4abc7434-46ef-3d69-87a6-0e78d6e1992f | -13.75004 | -52.01984 | 2026-08-28 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7b3c0cf-59be-3085-a093-ba08593b5e65 | -12.26942 | -50.58542 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7204fba9-41e2-39b3-a2aa-aca753f450a5 | -12.27367 | -50.5862 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6225da18-4480-32b9-b68d-9bdaf9b3f0e7 | -9.45196 | -51.70801 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e55917fa-ae55-30d7-af56-0359bf83ad25 | -9.15751 | -49.97147 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3ef5db0-3abc-3931-af8a-e615aee389cd | -15.53225 | -41.92086 | 2026-08-28 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 5aecb754-0e16-3b58-8663-5e88c9e7e34c | -13.60905 | -45.77744 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33f77377-3037-350b-9b90-2dc130de7026 | -8.80298 | -50.07615 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 353f91b2-ccb5-3781-99af-ab1ac5c49a65 | -12.24534 | -50.57264 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ae7c5dda-87ea-3b62-9caf-01fcb1cd9769 | -9.79517 | -43.55876 | 2026-08-28 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c1e525d-7613-3131-8a3a-d00a4fa1cfa1 | -11.2011 | -51.24496 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2f123d9d-6f82-3d00-a63b-189b1baca50b | -11.32146 | -41.82698 | 2026-08-28 04:17:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0f0f387-164c-3148-be86-3812abf4e5b5 | -9.22609 | -51.56475 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fabce045-8f0c-38c8-b81c-2e41104a7a03 | -10.76718 | -54.04077 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 677079e7-a7f0-338c-8596-864bfb4e23df | -12.43258 | -43.41717 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| cdcd6bf4-0131-39d1-b5eb-d9b9847c380c | -11.57542 | -45.51524 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2247b3d-1707-3477-9b99-bffccbbfcd91 | -11.20027 | -51.24961 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 11a79979-3cb4-3aa6-8e29-4fece4b06895 | -11.01717 | -45.06947 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7067e20-7a8e-3e53-916e-b8c7c1effb5a | -10.76649 | -54.04442 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6eee174d-8104-3419-9472-34f23c91ad02 | -11.47707 | -46.94163 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6314e716-f278-3607-9b73-be7e4bc82b82 | -11.33759 | -48.38248 | 2026-08-28 04:17:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c8d0e573-8de5-30b8-88d2-a76a15ce4a4d | -10.91959 | -50.53442 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8317e723-e6c1-35ed-a5ff-261bd0dcc7b0 | -14.88766 | -52.59566 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 23a60efe-9fdd-394e-b132-aa2d11d28de7 | -12.27425 | -43.14017 | 2026-08-28 04:17:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e7c64c76-9ada-3040-80e3-7a2964b83503 | -11.21376 | -53.99786 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abb2da45-35c1-3226-af9b-82a9719a57eb | -13.45474 | -43.84374 | 2026-08-28 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e98ff84-730a-3925-a031-aa61acd3a9ed | -11.48661 | -45.06953 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f806cb74-0c16-33ec-908d-573bdb4bb649 | -11.23752 | -53.99892 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 58e7adbc-55e8-3cc7-ab15-f63670926fe6 | -11.23473 | -54.0132 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4729dec-7f23-3aac-9eef-d8e1bd01d5d8 | -8.59686 | -54.77617 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ce2eda1-f561-398f-b2f6-92c6e9474880 | -11.40397 | -45.13955 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b87f03aa-974b-32df-99b2-3e95baa420ae | -12.77981 | -46.45026 | 2026-08-28 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b66460fe-cc80-36e2-9272-6958481ad2b8 | -11.20274 | -51.23567 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a8b5056c-2c86-3a3c-bdbe-f1f396ed4785 | -11.27348 | -54.01679 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3042995-8102-3b9c-a737-b2e2ea33320a | -22.25857 | -47.51756 | 2026-08-28 04:17:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 73ebea75-d6f4-3b88-8795-e7619fa361f8 | -12.01713 | -47.16546 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9875678-8051-3aa5-aaaf-62bb5f01245e | -8.21498 | -54.95949 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2a0e805d-7dc1-3ef0-a597-8f59efe1462d | -14.92351 | -52.59983 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d92a2d7-6768-305d-95de-6601e988e587 | -12.78721 | -46.44769 | 2026-08-28 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09d24a7e-4b92-388f-a363-8084dd9c22df | -14.86154 | -52.60679 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README28.md)
