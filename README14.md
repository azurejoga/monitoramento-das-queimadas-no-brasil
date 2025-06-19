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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dcc9829-24bc-3711-8ccd-058d56fc714f | -6.97432 | -42.79258 | 2025-06-19 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 68804962-d12c-34f9-a8b8-86927f3e1915 | -7.14701 | -43.28908 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d3eb852f-defb-3458-8a68-29a5406dc5af | -5.41487 | -47.56892 | 2025-06-19 04:17:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7da274b-5d95-30f7-bbea-0ce3a03d7feb | -7.28381 | -44.37904 | 2025-06-19 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 870bee35-3dfc-393a-8b2a-b72d9e618f91 | -6.15572 | -47.26775 | 2025-06-19 04:17:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7768dab9-530d-3295-9942-2f215ed2636d | -6.15924 | -47.26833 | 2025-06-19 04:17:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67becefe-9cca-3de3-9ff7-22abcd14b346 | -6.34021 | -43.7452 | 2025-06-19 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67afcdd9-5f6d-323f-b6c9-4a1ca6cc820f | -11.8906 | -49.33117 | 2025-06-19 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1b2bc73-bd3d-37fe-a032-591d0e25f9aa | -10.34998 | -44.30513 | 2025-06-19 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df3da1bf-9218-339b-bcb4-3ac85e0736fd | -11.3274 | -45.20913 | 2025-06-19 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae895f42-9428-3529-8f11-95d6867b878c | -11.2064 | -49.00957 | 2025-06-19 04:19:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6000663b-bc6d-3e73-80d3-f00da84a75d2 | -12.23215 | -44.1953 | 2025-06-19 04:19:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51eb6495-5431-36b0-91c6-8e8d6b88029c | -10.03193 | -48.69374 | 2025-06-19 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88537d36-e7a5-3217-becd-79a1a4975f73 | -9.88511 | -47.8107 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7fc382ce-fe3a-3366-b7fd-81132b85c714 | -10.64339 | -49.45126 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a9d2384-f8a8-34a2-b867-40135b47ace2 | -14.2148 | -45.52238 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea3f79d0-2d01-335f-bcfc-b3e50b6c8d41 | -10.65084 | -49.45256 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6b8a7ba-f662-32e5-9a7f-d32286d63baa | -8.70601 | -50.04757 | 2025-06-19 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12702231-f2b5-3f3a-afe0-95ebeace88b2 | -11.56554 | -47.43121 | 2025-06-19 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2caed15-a468-35f3-95ac-c21d8f0ce4a5 | -11.81985 | -54.49984 | 2025-06-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 796dcabb-a8fb-3f95-a9eb-7ccbf4e07e4b | -12.79968 | -48.73294 | 2025-06-19 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84737211-83df-3097-b5f4-630de4c065a7 | -10.64788 | -49.44736 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61000de6-4a4d-31c9-834c-4095df15884b | -12.47188 | -58.46768 | 2025-06-19 04:19:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d005cf7-d624-3368-8ed3-5710f78b0f22 | -11.94029 | -58.76394 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2925045c-75b7-3a74-a75a-b2ae8b189b55 | -11.62536 | -41.83572 | 2025-06-19 04:19:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 99003916-c497-3585-bede-362d73445827 | -14.82131 | -48.46816 | 2025-06-19 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 360b4c93-c20e-3c91-b43b-6a1b7e78dc48 | -11.91007 | -44.17255 | 2025-06-19 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c98f188-f657-3076-a4b6-5c94788880d6 | -12.76649 | -44.40973 | 2025-06-19 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d95be8ee-e1f3-3451-8ed2-012d586c6a27 | -11.62001 | -58.29235 | 2025-06-19 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fbeccae6-7a1d-3a29-b351-bd60cd6de813 | -9.79519 | -47.18704 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 0cf1f1c2-1a6a-3b56-ac11-e76f083b3e3c | -14.60312 | -42.88789 | 2025-06-19 04:19:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 04328dc3-285a-389a-9cd9-e21850d3baee | -3.32246 | -48.71824 | 2025-06-19 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7d38e5f-2e41-3f6d-8d2e-ca80b699d760 | -8.88405 | -47.41365 | 2025-06-19 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc668ad4-e7d0-3c0f-adac-aa3da8bc0374 | -8.19313 | -47.15528 | 2025-06-19 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56539498-2bd4-3db2-b635-48ea58be2b18 | -9.32935 | -47.83027 | 2025-06-19 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e11d2b3d-f557-3ca3-bfb1-40671ae34dfa | -10.25162 | -47.67631 | 2025-06-19 04:19:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 594aa51c-e076-386a-a6ac-6817c86e987f | -8.72554 | -47.99874 | 2025-06-19 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5832d8e-e39a-344b-8328-c46d55bcf935 | -10.29812 | -57.13855 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf8c2d3e-f202-33e4-81d4-0859ff002242 | -9.01683 | -49.58804 | 2025-06-19 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ccfa67f-2388-33e1-ac75-4df85aa0942c | -2.73678 | -47.33399 | 2025-06-19 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c7a5e8e-1011-3ec7-900f-079ee28d5043 | -10.50284 | -53.58206 | 2025-06-19 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cfd186b5-9060-35ed-8e28-a251be00ad4b | -2.58648 | -51.92473 | 2025-06-19 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79fbe1d8-19ec-3200-901c-d7ba840d091c | -11.32795 | -45.20559 | 2025-06-19 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d2adf67-1a50-3ea2-b46e-7e3931229b2b | -8.72267 | -47.99411 | 2025-06-19 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6aa087de-eff3-3b5a-97e4-0645a94d4c9e | -12.42637 | -54.87162 | 2025-06-19 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18f6a910-25e5-3bd9-b297-76f0664b437b | -8.32584 | -46.22854 | 2025-06-19 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa6f95fa-9d1a-34ae-a0f4-cecd47dc766b | -12.42579 | -54.87472 | 2025-06-19 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c87219c-d188-3010-af90-14af69290d5a | -10.58815 | -49.46022 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e562872-cf94-3c25-a3ab-6c41891b26d0 | -10.64711 | -49.4519 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6af59470-fbbb-3685-a7b3-b3ab9d83de5f | -7.28214 | -49.99598 | 2025-06-19 04:19:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34d274e0-f271-39a3-a3c6-2f6e951e431d | -10.25225 | -47.67252 | 2025-06-19 04:19:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aae8c7ce-81a2-3755-8e40-d24b6b4c9851 | -9.33221 | -47.83477 | 2025-06-19 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9beba16b-51e1-3386-b4c2-e17fa64b099f | -9.7958 | -47.18334 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 18c70e6c-c8fb-36c1-b89e-938611d0a372 | -9.41715 | -48.42162 | 2025-06-19 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c65f25c6-f4d8-386c-aefd-d5dbf394fa8d | -15.80043 | -42.03428 | 2025-06-19 04:19:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 319a7656-f6b2-39b1-ae13-224fd4f4615b | -11.13029 | -53.93678 | 2025-06-19 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 75ae9628-7a89-388c-97d7-986bb0c22639 | -12.3425 | -52.47271 | 2025-06-19 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 463c49c1-4918-397f-bbee-ff480669d5e8 | -9.45929 | -57.84796 | 2025-06-19 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f16936f-183e-3b80-a941-04c5d4ba2389 | -11.9594 | -58.73758 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f74e627a-7329-31d3-9b80-592037dc0dec | -10.62721 | -51.52983 | 2025-06-19 04:19:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef7e7c56-e5d8-3e0b-85e6-3192f8cc21a9 | -11.28951 | -48.6943 | 2025-06-19 04:19:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fa9d578-1299-38ef-8f19-7a1295568650 | -14.21869 | -45.51931 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d1089d3-bc51-3a88-b86e-6402386e6901 | -11.95283 | -58.73625 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 00e300b6-8359-3bf0-b90e-b8635737d673 | -9.89672 | -48.02104 | 2025-06-19 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| debee96d-c927-3a86-a96c-980ae8b80e63 | -8.75009 | -46.94621 | 2025-06-19 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 850e65f5-a444-310e-bbec-755a6b5df4cf | -11.64987 | -54.13986 | 2025-06-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccef643b-795c-34bc-ab9b-2eb9c7d17b7b | -11.12922 | -53.94249 | 2025-06-19 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 245b5d89-b2ce-3d5c-9896-a969929b6ca9 | -10.59109 | -49.45829 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98d8ca5b-90b4-33d2-846a-8edbfa545229 | -11.11586 | -53.9865 | 2025-06-19 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57b7bf72-208d-3202-84e9-6ac7963914fa | -14.44297 | -48.90516 | 2025-06-19 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c4c61ab-d5e0-3070-b5c4-e6577a17acc3 | -9.49152 | -56.08262 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c0752979-d6c1-3cc7-a18e-30b3d3c2750a | -11.9129 | -44.17681 | 2025-06-19 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dad6ebc1-0470-3604-9886-d1aeba2c0149 | -14.07035 | -53.39373 | 2025-06-19 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51328887-e7a6-376d-85a1-0e1f510709ec | -12.47235 | -58.47062 | 2025-06-19 04:19:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29c32b94-a0f0-3446-87b9-2b73c7c360e6 | -11.77187 | -54.37123 | 2025-06-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d6a0deb-d3fc-3576-b105-aef75926db67 | -10.87307 | -54.32057 | 2025-06-19 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 243abc7b-9e47-38cf-b1b5-f589b5660cc4 | -12.39997 | -46.35899 | 2025-06-19 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94463070-c223-32f8-9d28-2fdbfe892d83 | -11.61358 | -58.29104 | 2025-06-19 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7b143b1-c0b5-3cff-b84e-220c247484a0 | -3.3185 | -48.7176 | 2025-06-19 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f42f45b-7039-3b67-a7a5-723e1406a458 | -12.76592 | -44.41346 | 2025-06-19 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1992b09a-56d4-38c7-b663-6991aa4d0f01 | -11.41884 | -41.39919 | 2025-06-19 04:19:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd65f482-1f38-3292-89f3-5827db380dc3 | -11.13415 | -53.94341 | 2025-06-19 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc650a8a-092b-3430-8801-fd86b62b9ac4 | -11.90894 | -44.18 | 2025-06-19 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 995df3c9-d797-3155-9f24-dab131b23e9d | -11.13523 | -53.93767 | 2025-06-19 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0a93921-1e99-31e7-9632-5a71d71427f2 | -3.31786 | -48.71415 | 2025-06-19 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1b4d47e-659a-329b-860f-1560b81156c8 | -10.12397 | -47.5585 | 2025-06-19 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f8241a9-914d-376b-955d-9238edff4875 | -11.94934 | -58.75323 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| cf153c39-be02-3697-94f8-1a5858ba2428 | -10.15226 | -48.98388 | 2025-06-19 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c07b1dd4-4b25-3b3d-b0ec-b0f1816e8e9b | -3.57892 | -45.59445 | 2025-06-19 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd0baff0-715f-3352-9257-11335194f107 | -10.51966 | -47.58426 | 2025-06-19 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b5242fe-060a-3bf1-811a-26febde05563 | -9.35129 | -50.23065 | 2025-06-19 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78016035-e132-30d7-b508-d00fd142dfab | -11.95589 | -58.75464 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 1a0e0ead-9d3d-3577-bca3-8fb82a9f0ff3 | -14.21257 | -45.51463 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2e7b6c1-9900-3114-8fa0-cc37a2f6d8bd | -11.95398 | -58.73069 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6edf110-ab64-392b-a577-60bad4bc6b71 | -14.06584 | -53.39284 | 2025-06-19 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b57cbfe1-a279-3ca0-b882-2fac956c8af9 | -9.15417 | -49.64056 | 2025-06-19 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80d7d0a4-548c-3f7d-b187-a4b257e17d34 | -8.71508 | -50.26751 | 2025-06-19 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66da81d4-6d9a-3a16-b9a2-fbb7a708d5a1 | -12.75969 | -44.40866 | 2025-06-19 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3d74b4d4-eff8-39d0-8bfe-5c7b6e137ee9 | -12.26495 | -44.60442 | 2025-06-19 04:19:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6af5c16e-c3ef-3991-84c6-119b846b020a | -11.8024 | -57.35264 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README15.md)
