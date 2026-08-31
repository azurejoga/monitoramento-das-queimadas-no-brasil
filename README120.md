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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcda516d-7a07-3677-b4f8-64f7b5961c2e | -9.30299 | -40.57106 | 2026-08-31 16:30:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8b89801c-984b-3741-b68a-243ef5c58307 | -11.68624 | -54.54516 | 2026-08-31 16:30:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| f5ee0327-45e9-32c6-8347-056fd8a1bed3 | -9.21554 | -51.57718 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d5a687c6-8c2e-36ae-9f1d-72eb41b1379c | -10.31242 | -49.99835 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 19996302-fe57-3fe8-9355-a4c2fc42740c | -14.44258 | -52.51695 | 2026-08-31 16:30:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8b6b2f52-15e2-3011-b3af-d3d223f9b8e3 | -11.25027 | -54.00478 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| cf983805-e524-3191-8cb4-f6199399baec | -12.095 | -47.27103 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 67a4133a-33f5-3c2c-87f0-5faf156a451b | -11.21682 | -46.09328 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3a9b7ad8-54c9-3ca6-aa9a-0e8072f0535e | -10.18237 | -42.22265 | 2026-08-31 16:30:00 | NPP-375 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 171c70c4-ebfc-3104-b007-54ae9118e3ab | -9.65443 | -48.26276 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7c1e271e-cdb5-31f2-9df4-be8bed684d90 | -11.09125 | -51.53405 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5397e614-ca13-31bc-859c-efce12db7041 | -14.79108 | -48.26379 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e80ad1b1-59ae-3107-a8ec-48f17275316b | -13.34343 | -40.34673 | 2026-08-31 16:30:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3d660104-b936-3ed7-b497-e39e0da8763f | -14.66739 | -53.57696 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d4effdd4-9a13-3561-9b35-872ca7df57e8 | -13.7346 | -42.4909 | 2026-08-31 16:30:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 73bd38c9-8b55-3dcd-ac60-3302227878b0 | -11.21565 | -46.11408 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 667d7070-7933-38a7-8268-1231dd1a5473 | -8.86184 | -47.09163 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6f803b13-0b12-3b93-98ab-4bed8abd6fd9 | -14.09355 | -52.19893 | 2026-08-31 16:30:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c57f0c81-dfcb-30ef-978b-3cc0e84b5ded | -12.337 | -40.3141 | 2026-08-31 16:30:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 84cdf057-33d8-3ca3-be9f-2c145f9baca2 | -12.09811 | -44.99998 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 450ebd4a-132a-3371-ad4e-76b3c353b253 | -11.91782 | -45.07993 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ed3c25bf-41cc-3702-9673-24c35bae528b | -9.98161 | -53.92951 | 2026-08-31 16:30:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| a6076fb0-d902-3e4b-8480-5ce459c27a41 | -11.7926 | -47.66982 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| e718796e-7041-3c6e-bb00-430b8f093ce0 | -9.20857 | -51.5666 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 3cd5fd32-27a8-35bc-afdc-9b313b3dca1b | -11.20209 | -46.09848 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6336c529-bc6b-3d37-91ae-077ce5cfa388 | -13.18362 | -41.75578 | 2026-08-31 16:30:00 | NPP-375 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 12cb3960-c76c-331c-bea9-d9706b4dbf44 | -12.08509 | -44.98832 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| f9f46f7c-d708-3c51-975a-2c72c2cd460d | -13.38748 | -51.76904 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1e02bccb-9d84-3fca-afa4-8ae28e5aafbc | -14.43808 | -52.51564 | 2026-08-31 16:30:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3805c463-9d66-3d31-b009-75cb2831994b | -8.73574 | -46.46565 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2c23e014-d47b-3a9c-b830-c4afcc27ce59 | -11.32413 | -45.17558 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 31881497-65e7-3a6f-8846-f728daeebc1a | -11.24834 | -45.13051 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6bdaf0ba-47b2-344d-af67-d291161224fb | -11.9129 | -45.05243 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| aa3d21ea-d6df-3ebd-afdb-9f5f4da5ec17 | -8.75892 | -46.46193 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 0359dc8f-13a0-3e0b-a822-7196ef7092cd | -13.84097 | -54.09229 | 2026-08-31 16:30:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0d828feb-7fe2-3e66-8aff-d60796834c86 | -8.86509 | -47.07993 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c2ca748f-b1b6-3624-a44c-fc7b5c17a465 | -11.54389 | -45.47943 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 34c48c19-8f41-3e6f-a328-4193bd2d4dce | -10.96364 | -48.40427 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3451f7ef-e529-3783-a2a1-3fa13c1c86da | -12.17694 | -50.55159 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92057bc1-06ff-3d16-a053-daea2daf1163 | -11.24366 | -54.00534 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| ebb13389-858a-3859-8f08-053beb1b134a | -10.81782 | -45.05402 | 2026-08-31 16:30:00 | NPP-375 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e74aac4c-2e97-36d3-9b20-2a61e93a85a1 | -11.23047 | -45.13776 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| c4afd12b-5178-300e-b81a-09e11bcf8b75 | -14.2089 | -48.64275 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 139dd61a-46a0-3aeb-a0ee-c83e923331e4 | -8.64104 | -47.31258 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 66f08028-9399-3087-8228-54396b9e4820 | -11.20281 | -50.62621 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 698f640b-3456-3a02-8674-847d9691b548 | -10.15158 | -45.77454 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9e27c583-ca88-329a-ad4a-93697045ac18 | -12.0952 | -47.18245 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bfc19997-3e6d-3845-998b-40b3385c86c4 | -11.32469 | -45.2066 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| bb46509f-438d-3148-90e3-49dedfdb6b66 | -11.07299 | -51.52481 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7c4ffd83-76b3-3391-b136-87497d1095cd | -9.67434 | -50.84961 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 30d2333d-c1d8-3388-8821-2a181efad723 | -11.07162 | -51.51339 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c432a25e-275b-3a95-972a-3c1e56fa174a | -8.60673 | -37.65133 | 2026-08-31 16:30:00 | NPP-375 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d7b4f0fe-bb49-30ae-9a14-93e72e9afe5b | -13.46839 | -51.40914 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fecaf27a-7cd3-37ae-8d9b-760fdf821be8 | -12.09749 | -44.99557 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 7ba2eb51-4ffb-33f0-8404-aeec67cadd96 | -8.86434 | -47.08047 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 3c599594-534e-3888-aa8a-ef705996c8a4 | -9.67634 | -47.93166 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5bd20180-1a4b-38d4-a97c-08615f5b2725 | -11.37249 | -45.19559 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6925fefa-f6b7-3261-8d5c-ea351f8db73c | -11.21888 | -46.10845 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 6a64d1a0-6c15-34f7-9eeb-acffa9efc93d | -12.07183 | -47.19621 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ed46ef0-fc0e-38e4-b721-19bf2d5c52e7 | -10.45403 | -39.55884 | 2026-08-31 16:30:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4a3a3897-c98d-383a-b8b3-03aa0f46e208 | -10.7509 | -54.03849 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 285f2084-0308-33b8-accc-d95a4759c7e3 | -12.09966 | -45.06437 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 8bd8f798-b30f-35de-9a98-36e729167415 | -11.37548 | -45.16343 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 27217f07-357f-37e0-a2f6-1a2cf92881c9 | -10.83363 | -46.00252 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4c50cf6e-18a6-3f87-9195-3f05e4d84916 | -14.58062 | -53.6157 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5e6b80f7-d0d6-3806-9921-7e0b8efbeeff | -11.31792 | -45.18536 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| f4d5c158-a4d9-3890-bfdc-e8179cd46f08 | -11.93695 | -45.08087 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 5f4bfd1f-604d-3aad-a92d-03af7522fb89 | -13.43459 | -39.87874 | 2026-08-31 16:30:00 | NPP-375 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| bcf87b3a-1e67-3da6-b59c-a31e47fcdf3a | -9.98114 | -53.93225 | 2026-08-31 16:30:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f2ca3ce7-dea1-3de0-8c8c-dce4ccc4dea8 | -9.19157 | -51.56477 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 678495c7-1e0a-3056-a2b6-0b0aaa82e97c | -11.62005 | -50.18221 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb0a780b-bce1-37c7-be4d-1a434bdcfbd1 | -9.45375 | -48.1985 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4701c316-bf99-31e3-b352-825e58a82f09 | -13.4631 | -51.41383 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dda607df-f2a4-3435-8e60-0afb7256b766 | -11.19055 | -50.57103 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 69139953-0df3-357a-9a8c-7e1cb2e97bc7 | -13.27369 | -51.60007 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2c6e722e-e821-369e-9e3b-bc8bd287284b | -11.92215 | -45.08377 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6b0caf6a-62a2-3f82-a638-e84135bde737 | -10.40575 | -45.08371 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e43daee4-22a3-357e-bf23-a4baeac65b18 | -11.05433 | -47.11818 | 2026-08-31 16:30:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4a375c63-2efa-3876-81df-e7c480c9f0ac | -11.20105 | -46.1192 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| f19f5119-0544-3e92-a1cd-941d8c513496 | -8.64155 | -47.3162 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7b18e2a4-fb22-3b5f-bf02-859a0cad55bd | -12.08138 | -44.9888 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 90ca2f7a-f367-3546-878b-a99723abcf0c | -14.79742 | -48.27101 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2572a5af-5421-3fd2-9fe5-a1c249e89d3a | -11.06981 | -51.52208 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 20aa4791-1f17-3def-b4d1-245a467d9858 | -8.92653 | -45.03131 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 87660c81-f3a1-3282-873e-a265159e540c | -11.71195 | -47.63696 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0d8e2f9f-bbbc-336c-af12-fb5d56533a6e | -10.79403 | -50.71446 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f8af1204-cd46-3ddd-b9c2-8712720534be | -13.41859 | -51.38219 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 34c05ab8-9ecd-37aa-9060-2da8250aafe1 | -10.84882 | -45.32239 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c6784bbc-446a-3878-8bc6-077ca299a607 | -10.93479 | -46.60704 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 60f938ba-5624-367f-9858-8375610e756b | -9.65736 | -48.28389 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a9dc8018-99fe-364f-b57c-59f8404b3538 | -11.91718 | -45.07527 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 50402dff-327b-39eb-947c-2038b7795d83 | -9.97289 | -46.81907 | 2026-08-31 16:30:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| a3a374ec-496d-3a6a-8cbf-c71d5e52bebb | -11.24826 | -45.10351 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d009e867-6220-322a-a661-ccc479d97c2a | -10.1147 | -50.31171 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 3da4a0a5-7583-311b-b4b6-db20873db8b8 | -10.82677 | -50.63369 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| dc2d3714-b661-383b-872e-ded98a77f44d | -15.27438 | -53.87814 | 2026-08-31 16:30:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| e0b3b905-e955-3e4a-882b-725e7c6b5ca0 | -11.32407 | -45.20222 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3f28cac6-d995-3dfc-9b36-f3cb68e95c53 | -11.91994 | -50.81408 | 2026-08-31 16:30:00 | NPP-375 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b8c77e6f-c375-39e2-9551-98091e875de8 | -9.68421 | -47.89293 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c550e784-3642-3837-bb48-a4eff8c95e41 | -10.86094 | -45.38044 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |


[Clique aqui para ver as próximas entradas](README121.md)
