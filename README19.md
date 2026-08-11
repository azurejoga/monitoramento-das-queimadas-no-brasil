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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e71a0e0-332b-3396-b9a8-c01e79a26721 | -20.391 | -49.30867 | 2026-08-11 04:38:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 4a378d7f-97f5-3595-a5bb-44ff4cf7ab77 | -23.29523 | -52.2117 | 2026-08-11 04:38:00 | NOAA-21 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8447b998-d650-3f53-b2df-46d8b3d12775 | -22.34699 | -43.04196 | 2026-08-11 04:38:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a9c37e71-a708-37d4-bbc6-ce46932ec806 | -21.93313 | -48.96211 | 2026-08-11 04:38:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 0a9c3dbb-0ff3-38b2-abd0-e0e39db04303 | -21.36998 | -45.52798 | 2026-08-11 04:38:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 91a01c74-7bb3-37cc-a708-0c887256dc61 | -21.46937 | -48.61264 | 2026-08-11 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed63c5ef-52db-3534-aff8-2181999fd919 | -21.92905 | -48.96571 | 2026-08-11 04:38:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 6cce0a01-0736-3adb-9869-7dd0dc519ed3 | -21.92963 | -48.96154 | 2026-08-11 04:38:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| e750eb1f-6f91-30aa-b7b6-f9de23641e6e | -21.49788 | -48.64126 | 2026-08-11 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dd3774a-4a36-3d93-ac23-881c5945d5d4 | -21.14837 | -50.46614 | 2026-08-11 04:38:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6d335121-b032-3e55-96ec-69626d4732b0 | -19.84904 | -49.06451 | 2026-08-11 04:38:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dafa646-3d88-33bc-b9fa-400d622cd3f2 | -21.46878 | -48.61684 | 2026-08-11 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcc4a4ba-f3b9-3dac-9fd0-de5f92ee03da | -21.46525 | -48.61626 | 2026-08-11 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f44739e4-ac4c-30ba-9a0a-44e9b04d8c78 | -22.18488 | -43.24193 | 2026-08-11 04:38:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b9dfe34-9a67-34f9-ba1a-b048b5218518 | -22.18978 | -43.24263 | 2026-08-11 04:38:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 25ca6ff8-bf4d-302c-ba83-2fe28a7f491c | -21.46584 | -48.61203 | 2026-08-11 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72149b13-0991-345e-801e-2b483207d5a0 | -19.84561 | -49.06397 | 2026-08-11 04:38:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5815ae09-3c89-38cd-93b7-df87fca904f5 | -20.38759 | -49.3081 | 2026-08-11 04:38:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1b5ceea8-f374-3b98-810e-163b083b17ca | -23.29582 | -52.20795 | 2026-08-11 04:38:00 | NOAA-21 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5a6bae86-a29f-3298-9b5f-10c997d0711e | -21.93255 | -48.96628 | 2026-08-11 04:38:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 2be96f33-feef-34a8-824f-b074b4155362 | -13.5502 | -46.2844 | 2026-08-11 04:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a06324e5-7fa6-3a71-aa28-ffeddee4174c | -4.2635 | -48.1799 | 2026-08-11 04:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e936e3c2-ff32-3f45-9be8-6ec3112770c3 | -9.3906 | -47.4878 | 2026-08-11 04:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| b837c3fe-5e3e-3699-8283-0c4239c5f33e | -9.3714 | -47.5119 | 2026-08-11 04:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 9c44951a-7a40-30ad-82ea-b92b26624884 | -13.5894 | -46.2553 | 2026-08-11 04:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 27c534d1-78d3-31c9-a746-a7b6b28ff60e | -13.5701 | -46.2584 | 2026-08-11 04:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 20bf6ebe-b557-39c4-8160-d1209fdd381c | -13.589 | -46.2782 | 2026-08-11 04:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| cba7e3cc-d318-391f-890b-0d6e12374bb1 | -13.5691 | -46.3042 | 2026-08-11 04:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8be1c464-f166-3514-a27a-2486bb8ff444 | -13.5696 | -46.2813 | 2026-08-11 04:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 356.0 |
| ad45f883-d65c-3a51-afcb-b6d496efdcdf | -13.5691 | -46.3042 | 2026-08-11 04:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 16420b8e-4db5-3650-9f7c-01005f37b65b | -13.5701 | -46.2584 | 2026-08-11 04:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 140.4 |
| dc32d9a2-3e2c-3c59-b0e6-d28fe722d3a6 | -13.5696 | -46.2813 | 2026-08-11 04:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 271.1 |
| f7ae8db7-5f62-3f8e-a3d8-ab0fc4a7f512 | -11.451 | -46.6846 | 2026-08-11 04:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| c3bb138c-5035-378f-9b24-cf77d5095f59 | -13.589 | -46.2782 | 2026-08-11 04:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 93e89d0e-d2b3-391c-a79b-07323d96c995 | -4.2635 | -48.1799 | 2026-08-11 04:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 51e3dc3c-b908-3c4b-a2ce-e01188176277 | -13.5894 | -46.2553 | 2026-08-11 04:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 13b186d3-92a5-3920-8936-d352aa6e6825 | -13.5502 | -46.2844 | 2026-08-11 04:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 93f29d36-26aa-3b95-9685-22ad10bcb588 | -12.4515 | -45.3107 | 2026-08-11 05:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 586af0a0-f756-3ec8-bfcb-d894a398dd47 | -4.2635 | -48.1799 | 2026-08-11 05:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 741acbea-5dab-321e-ad7c-280159d6e64e | -11.451 | -46.6846 | 2026-08-11 05:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 1df40eff-ff9e-3f08-bfd3-c8d38feacca9 | -13.5696 | -46.2813 | 2026-08-11 05:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| c814a6e8-7683-379a-a567-63f16b80949b | -4.2634 | -48.2016 | 2026-08-11 05:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 245a7bb3-a90a-3216-af15-9a5b084251ae | -9.3906 | -47.4878 | 2026-08-11 05:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ed62065c-4cc2-3a52-ad36-d96f63d14bfc | -1.94868 | -51.56981 | 2026-08-11 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66aa5886-f8a8-3cf7-a0fd-c817aee0addb | 1.6434 | -60.14183 | 2026-08-11 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89b4df77-d157-379f-8a4e-f464e7f7ff5b | -3.49177 | -50.05622 | 2026-08-11 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b6ae44b-654f-3068-a2a4-ba5aee857f22 | -4.45278 | -47.91855 | 2026-08-11 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f7c46afc-62ce-39f4-90b3-ecfbd6b452e8 | -3.02838 | -54.52717 | 2026-08-11 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 835a24ca-1452-3a66-bf30-fc22e4c1c142 | -6.01263 | -47.4041 | 2026-08-11 05:08:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 882c12c6-e873-3fa5-be07-49142b4da1cf | -5.32339 | -43.56066 | 2026-08-11 05:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d1deffe-e14a-324e-9dc4-ede43653b4a9 | -4.40206 | -54.78637 | 2026-08-11 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78373a58-98eb-394e-85af-ed7c1d264499 | -0.86892 | -47.93002 | 2026-08-11 05:08:00 | NPP-375D | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ee301610-3af9-37c6-917a-208a1b8ceb2d | -4.39875 | -50.9715 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b091719d-b16c-3f89-899e-facf58e6ce31 | -4.7109 | -56.02084 | 2026-08-11 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0eab96b4-d5b8-3169-b04d-7075e311d599 | -1.78517 | -55.53154 | 2026-08-11 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82376e04-3eda-3140-8216-ba0805457e78 | -3.70242 | -55.95373 | 2026-08-11 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8730a8d-9c6b-3597-b889-1caa2d058d0e | -4.26158 | -48.19402 | 2026-08-11 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 527c5f7c-4ab3-3531-abf7-2c563ac7a057 | -5.73841 | -44.50384 | 2026-08-11 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15dc0186-3d24-32d8-aead-0d23c5d29284 | -2.9583 | -49.25968 | 2026-08-11 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b95d4215-bb96-3e0c-921b-114c9f6275ec | -4.26278 | -48.18621 | 2026-08-11 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 9dd3a3a8-4411-314a-bbf6-c9b1e3cb6be2 | -2.65353 | -54.62298 | 2026-08-11 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a5a039-fdfe-3f36-a574-f2c3ea79e448 | -2.09038 | -54.44447 | 2026-08-11 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 905a5f7d-81aa-3bf3-9906-aef579fb0f19 | -6.01231 | -47.40594 | 2026-08-11 05:08:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3faf381d-d38e-34e6-a6d8-6034058fae8c | -4.39358 | -50.96782 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d318e21f-975e-3c87-8dd6-cd1ed4228096 | -2.97044 | -52.15687 | 2026-08-11 05:08:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dd9914f-90e7-39fc-9588-3b8485b6c7b3 | -4.26761 | -48.18293 | 2026-08-11 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 60b69b4a-ecc0-33e5-a1f2-678024355d44 | -4.39813 | -50.97559 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d95187fd-2857-3f21-b423-b8c5a6ac9ffe | -3.48872 | -50.05127 | 2026-08-11 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a3b71c0-0ad1-382d-ad7e-f14744d01825 | -3.37385 | -57.69667 | 2026-08-11 05:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 573e2642-1093-3117-b930-9cf31b2ee3bb | -4.70684 | -56.02407 | 2026-08-11 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2770eb5c-8551-3918-a6c0-b0caf5693761 | -4.39781 | -50.96425 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 708ceb87-b9c3-3893-a4b7-f9dd947647d9 | -4.39 | -50.9673 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b47155be-4b57-3079-96bb-184d54b1ade3 | -4.40233 | -50.97204 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a15c4541-a5a1-3009-9d7f-1c60938daa52 | -1.67821 | -55.23428 | 2026-08-11 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8068ce9-2b80-3b33-9bcd-e2debc4e440f | -4.39517 | -50.97098 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf5ecc7b-e645-31d1-8602-70522b46c64c | -2.96216 | -49.26027 | 2026-08-11 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| cb2110af-1053-3997-a36b-feef876db425 | -4.70745 | -56.02032 | 2026-08-11 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 066c236d-66b7-32d6-aa82-41c5cc12a8f8 | -4.52638 | -49.30127 | 2026-08-11 05:08:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b411ded7-b3b7-32bc-8f1d-78c56eb0a421 | -4.40296 | -50.96795 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbd5db01-9e1f-38d0-9340-1f79ebe85f26 | -2.96069 | -49.26989 | 2026-08-11 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 60748b0e-f5f0-3f8e-acff-bac69bc541d3 | -4.45901 | -55.43749 | 2026-08-11 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91de42c3-a361-3211-90de-02b38b0bd2a6 | -3.54651 | -54.71663 | 2026-08-11 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 777a0bb2-fd64-3ea1-97d7-4ca0bc542a89 | -4.26701 | -48.18683 | 2026-08-11 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 1982d722-c8c4-310d-badd-c16cacb4a891 | -4.39588 | -50.9765 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5aa75ea-76f8-3335-8517-cc0930ae65c5 | -4.39579 | -50.96687 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab753933-693b-3f8d-97df-9a123a4e624a | -4.26641 | -48.19074 | 2026-08-11 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| cc66c867-1d7f-328e-8e70-17d6aed81747 | -3.94995 | -59.613 | 2026-08-11 05:08:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b32a520-627a-3b27-b02b-303e83ef7bcc | 2.44607 | -59.93874 | 2026-08-11 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb658b0a-323d-3b8c-bed8-03cf36fc4042 | -5.3453 | -45.16584 | 2026-08-11 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3b1adba-fd71-3fab-897c-3ebe637d13ea | -2.9629 | -49.25545 | 2026-08-11 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fb54a71-f359-31d0-b9b5-072d09b85883 | -4.26218 | -48.19011 | 2026-08-11 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 68658ee3-c61a-3260-a68e-f79a587ade62 | -3.00552 | -49.55334 | 2026-08-11 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccc95fdb-a2fd-3631-80ba-9a0a78ce0f58 | -3.00622 | -49.54875 | 2026-08-11 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66b83222-cbcf-3f71-8607-102d45e044e5 | -3.00933 | -49.55391 | 2026-08-11 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a19e2846-6b20-3bc9-80c2-d79e247687d6 | -4.39221 | -50.96635 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf84b96d-9db2-33a0-956f-079a0aadda6d | -4.39641 | -50.96277 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbdaba22-1187-3cb1-acbc-2dab23062e02 | -4.39653 | -50.97243 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3746539-a943-3f1f-b61c-a4c38a60eacb | -3.66498 | -48.97439 | 2026-08-11 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3aacaad5-094f-3cd8-baca-c119018337d5 | -6.00843 | -47.40061 | 2026-08-11 05:08:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e53f0de-c185-3316-b253-b4827939acfb | -4.83759 | -49.85379 | 2026-08-11 05:08:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README20.md)
