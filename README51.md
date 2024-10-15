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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e061580-d572-3fd2-8854-e56a8a68045f | -6.5878 | -48.2381 | 2024-10-15 04:25:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 2d9aa468-379b-3a3f-803c-7a57379ae987 | -9.01 | -54.5042 | 2024-10-15 04:25:57 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 113d7ceb-28d3-302b-81df-0a4018e9d6d3 | -10.3711 | -61.1935 | 2024-10-15 04:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 018271b0-545c-36f7-9eb5-6a861560a631 | -12.515 | -63.263 | 2024-10-15 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 044ddd3c-c3b6-3a8f-8c37-132f44a008ca | -13.9274 | -45.8091 | 2024-10-15 04:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 34d38740-9037-3bda-8c93-b053e9fe5877 | -13.9079 | -45.8124 | 2024-10-15 04:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 62f51215-4d40-3a5c-b044-bb0b6b835365 | -13.9075 | -45.8355 | 2024-10-15 04:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| aef15b86-8dd2-33d2-ac42-d6eb75c14384 | -13.9269 | -45.8323 | 2024-10-15 04:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 16bbaf89-a1c0-3bd3-bc9a-9d824d22db07 | -13.59308 | -49.79091 | 2024-10-15 04:27:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 646a2c62-e9a5-3a9d-be03-c0d69b99e7ac | -15.07733 | -48.94319 | 2024-10-15 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| afc12ffa-2594-3028-b55d-03bfe9f5421f | -13.59715 | -49.78767 | 2024-10-15 04:27:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fdbaa90-4704-3d71-93b8-853222000a6c | -13.59371 | -49.78708 | 2024-10-15 04:27:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ea611a9-096f-3222-9352-d659fc7bfa4e | -13.64474 | -53.10682 | 2024-10-15 04:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d19d5eb3-3a51-38d5-bb04-31cd7da14856 | -13.64066 | -53.10608 | 2024-10-15 04:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc54c426-b6f2-3e9d-a0b8-b518ae42b621 | -12.38166 | -53.11832 | 2024-10-15 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9e5b309-0be4-3788-9b6f-3883acd46fdb | -12.38099 | -53.12217 | 2024-10-15 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b45f73dc-30a4-3acb-a652-65a8be1af668 | -12.3775 | -53.11754 | 2024-10-15 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96508d71-a34c-3878-938c-e32a323195c8 | -12.2713 | -54.55529 | 2024-10-15 04:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45d70c08-067f-3f60-8160-0225cbb433a7 | -14.86332 | -57.96607 | 2024-10-15 04:27:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7164f308-03b7-3694-ba9a-b26a61e204f9 | -10.62392 | -61.43404 | 2024-10-15 04:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f3ffcc4-7bdf-3361-87af-dfec9f1048cf | -10.44556 | -61.26643 | 2024-10-15 04:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3eb9dbe-aa71-3ba2-b2ab-3d753e97653c | -10.44416 | -61.27323 | 2024-10-15 04:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b435a36-446f-397e-8e47-19d25a36cd0f | -13.3629 | -61.34693 | 2024-10-15 04:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ace8b72-94ae-3006-831a-ffdaaa6e55db | -13.35607 | -61.34532 | 2024-10-15 04:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a30a4a70-a981-3e1d-93d2-4de202e1321c | -15.58903 | -43.21275 | 2024-10-15 04:27:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce1b23b1-548e-31a1-8e5b-fcaa37b0caec | -15.58501 | -43.21215 | 2024-10-15 04:27:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0233a291-e8fa-38da-9f5e-1cdd21c4a148 | -20.43839 | -46.17018 | 2024-10-15 04:27:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 469fadb6-1911-3fef-a277-faaa497e2b45 | -20.43477 | -46.1696 | 2024-10-15 04:27:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af7cd219-4b2d-33d6-9633-77ec5a95e582 | -20.43415 | -46.17403 | 2024-10-15 04:27:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b49e14c-6748-3bbc-b02e-337ae528e038 | -13.58073 | -46.58969 | 2024-10-15 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 798c8a0d-24c5-3e85-8bc9-666a00bb6d7b | -13.57736 | -46.58915 | 2024-10-15 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe4b975c-6a56-3cad-98a8-eb2443e69121 | -13.57399 | -46.58862 | 2024-10-15 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c11fadef-40e4-3ce0-a808-9ef0d73c2df5 | -14.30883 | -43.86918 | 2024-10-15 04:27:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 836433eb-9d2e-37b0-8ac6-64861345b519 | -14.30726 | -43.87088 | 2024-10-15 04:27:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4ff7e97-b7f4-384d-bec4-a16618cb660e | -14.09417 | -44.60621 | 2024-10-15 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 192a3f42-9bc0-3633-993d-7d147bb5aff2 | -14.09388 | -44.6087 | 2024-10-15 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb230144-8b79-3016-8d31-6cb33682ae0a | -14.09353 | -44.61056 | 2024-10-15 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f27e0cf-0105-392c-9747-2b1bc50c5fee | -14.09084 | -44.60384 | 2024-10-15 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0c3401e-d5b5-3fb9-a46b-a4489e4bf57b | -14.09052 | -44.60571 | 2024-10-15 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9746070-9dd3-364c-bef9-9daa5e72c258 | -14.08058 | -44.78148 | 2024-10-15 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d674ea4b-0980-30ff-b3df-95c6120bc8e8 | -13.92273 | -45.82384 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c69f51f-1c8d-36cf-a87b-9df620f9e095 | -17.77859 | -42.80791 | 2024-10-15 04:27:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f7db947-8827-3d8e-b2b1-a8f3b44c0741 | -19.2235 | -40.14014 | 2024-10-15 04:27:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 26094a48-81a6-3cc0-9c74-74682e0160fd | -19.64742 | -40.47269 | 2024-10-15 04:27:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e31a0811-1d0a-314b-85f5-37dd58c51ac9 | -19.64703 | -40.47617 | 2024-10-15 04:27:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 997ad38c-ca08-339b-a7ad-8efccda357a6 | -19.64489 | -40.47216 | 2024-10-15 04:27:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 64f01302-0bde-3150-b043-eca9d9dc5300 | -19.64453 | -40.4756 | 2024-10-15 04:27:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c12a8f61-eac2-3f39-83d6-e3699658159a | -19.64417 | -40.47902 | 2024-10-15 04:27:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cde60335-9bac-3d72-a968-281efe1e88ad | -19.64234 | -40.47194 | 2024-10-15 04:27:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1ff86541-86ec-35a0-8ac1-391e2ea774d2 | -19.64196 | -40.47534 | 2024-10-15 04:27:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cc9771bb-0df7-3f7c-b5a3-43b2aa01c84f | -19.64157 | -40.47878 | 2024-10-15 04:27:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 68b26d63-13af-3f33-a26a-b013c3a005b6 | -19.63979 | -40.4715 | 2024-10-15 04:27:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e182ddbc-5bc3-34a5-a858-17d1b080d1da | -19.63943 | -40.47498 | 2024-10-15 04:27:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 27c9eb8e-55f3-3d08-81f7-ae677027cfc7 | -19.63725 | -40.47129 | 2024-10-15 04:27:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a281789b-fa43-3084-8b40-3c62ce15ddc8 | -13.7438 | -43.59011 | 2024-10-15 04:27:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b58b643-b0cb-3e32-a5cf-864a7158c793 | -16.34857 | -43.69513 | 2024-10-15 04:27:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12963d17-954a-3d89-a641-eee0089dfa94 | -16.17898 | -43.86089 | 2024-10-15 04:27:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cc7ebc4e-708e-3ecd-ae53-b314b0219d8e | -17.28236 | -43.84676 | 2024-10-15 04:27:00 | NPP-375D | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eefaec06-39cf-3ab8-bfef-c85b9514b1cf | -19.19228 | -44.75689 | 2024-10-15 04:27:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7cfc9f54-09c8-3634-b044-750c04f4715f | -18.68831 | -43.69289 | 2024-10-15 04:27:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7c7138af-1b2e-31bc-be2f-9009830bf522 | -20.02022 | -44.59749 | 2024-10-15 04:27:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ea1add4-686b-3da2-8389-ce1e8f77c5a6 | -19.86385 | -44.95014 | 2024-10-15 04:27:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16b45ef3-8297-3bb0-a1bf-831b7772cf66 | -19.70973 | -44.05238 | 2024-10-15 04:27:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4d8a5e7-d2ac-3e5c-8d21-45892e26c8f6 | -19.70927 | -44.05599 | 2024-10-15 04:27:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50f29597-f26e-38bd-84c8-26619e4109d6 | -19.7088 | -44.05963 | 2024-10-15 04:27:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12e6fb6e-c1a6-3d76-bde0-f9aac55c27a0 | -19.51349 | -44.27419 | 2024-10-15 04:27:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4485b40b-ac9a-307f-aff9-71894e371dd6 | -13.82575 | -44.15331 | 2024-10-15 04:27:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd74ee9c-3430-353a-bb9c-125b361cc5cc | -17.63992 | -44.88358 | 2024-10-15 04:27:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5738ff94-f985-3d62-b6af-05b2adbf12fb | -17.24315 | -45.31456 | 2024-10-15 04:27:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 650a15a9-7072-3c71-a3fe-c9a0d1d1d0d9 | -17.10152 | -44.58302 | 2024-10-15 04:27:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0378438e-9381-3890-bba3-d3b39f5bd3d5 | -19.73137 | -45.62196 | 2024-10-15 04:27:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28f938e1-a96a-3580-86be-26ff6598297d | -13.90998 | -45.8227 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d754d360-ae6b-3fce-a07b-a5d67ab78196 | -13.56113 | -46.64994 | 2024-10-15 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 058100e8-b85f-3d08-85ea-59e03f43862a | -13.55777 | -46.64941 | 2024-10-15 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e38e6ff-c67f-32f3-9892-c8e1ca3c5658 | -13.2456 | -46.54858 | 2024-10-15 04:27:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c261f01b-5123-3c9f-a0d2-ba994af9542b | -13.92216 | -45.82769 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be9cfdce-7146-3b24-9db2-7010b0c97ac2 | -13.9216 | -45.83154 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44362807-f050-3af9-a579-334b5b246613 | -13.91985 | -45.81946 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35935d61-9334-3cd9-adfb-21e2fad785f8 | -13.91928 | -45.8233 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d63ed839-44e5-39a2-bcae-b462016257c6 | -13.91872 | -45.82715 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 88cfb896-27e8-3260-92d3-e192a5f3204a | -13.91815 | -45.831 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c0343548-e5ac-3f68-b898-8aa86e647806 | -13.91746 | -45.81993 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30873462-dc25-3604-b7cf-c2bccf0b48f9 | -13.9164 | -45.81891 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e14ed1b1-a0c3-37f3-b689-2d38e615ff50 | -13.9163 | -45.82763 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3bc98dcb-ae63-3a98-a686-f91cac472770 | -13.91583 | -45.82276 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| e4edb2f8-efe8-3f56-a6ca-39cbe2e09a24 | -13.91572 | -45.83146 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ae1bd0d9-f7f8-3f2c-a745-6662ea067ebb | -13.91527 | -45.82661 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 5acaa45b-b19d-363f-80eb-26e759bc7d96 | -13.91514 | -45.8353 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 00a4a456-e098-3fa6-a6cb-6520b433c315 | -13.9147 | -45.83046 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 52263b14-23d0-3229-bda6-30234b4a1bc9 | -13.91414 | -45.8343 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 55256708-03df-332f-bb74-12addf6a6aae | -13.91401 | -45.8194 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4b1e616-c3d0-39d5-b8a5-75850d6d94d5 | -13.91343 | -45.82324 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 928c2e6c-85cf-3339-90ee-73c644bc1bb4 | -13.91285 | -45.82709 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| d53049ed-d6da-30a9-83c1-69540ed4caf4 | -13.91227 | -45.83093 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9ac40c52-8022-3105-ae40-c9d32ca59d2c | -13.91169 | -45.83477 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 852492d3-95cd-3e0a-b407-b2492710ecc3 | -13.90883 | -45.83039 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1cd27c65-8641-3a20-a615-12e8f65eadf4 | -13.90825 | -45.83423 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| caaebde6-21b2-3b2d-b78e-ab6d2937804d | -13.90767 | -45.83807 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ad075d15-1392-31f8-9c80-f6aa05ae7495 | -13.9048 | -45.8337 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4d274195-57db-3a48-9b34-a25661a59a70 | -13.90422 | -45.83754 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |


[Clique aqui para ver as próximas entradas](README52.md)
