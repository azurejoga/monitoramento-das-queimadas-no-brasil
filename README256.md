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

## Dados Diários - Página 256

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9738720-d86f-3a9b-a7e8-eb0fe529e306 | -14.59796 | -41.28675 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a235cf27-821d-3854-8bcb-546f760f6360 | -11.5735 | -43.68743 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1677af66-a88b-391c-942d-063a3cfe0a55 | -15.37913 | -41.92052 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 272.3 |
| 053911fe-46e0-35a4-9135-3a7a36f46f85 | -12.1417 | -44.74499 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eaf5517c-460e-371d-ab94-e58f2c7f65db | -14.04897 | -44.7971 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dc8f7e06-f167-37e8-8d9a-5aa84c81aac8 | -14.05589 | -44.78814 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 03af7cd8-31ff-39fb-be06-aee32d47e2ce | -12.00346 | -43.45553 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ec7c3cbc-a95b-3b78-9a0a-483ee41438db | -15.3871 | -41.89476 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 51fd4808-fe8c-33ed-865a-f7577a10cc5e | -12.18907 | -44.62794 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| b94cf56c-92d4-3180-8bbc-b0e3becd8e3f | -16.12503 | -43.74932 | 2026-10-09 15:58:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e11708b1-31f4-3e0f-9219-dac387b73036 | -17.09547 | -40.76748 | 2026-10-09 15:58:00 | NPP-375 | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 61e351f3-0e65-339a-936a-71816f66d0ca | -15.39251 | -41.89434 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| b7979ff9-02e0-3b46-bbec-5e642c5ad8c4 | -14.47047 | -42.05788 | 2026-10-09 15:58:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0ab71b46-d993-3124-bd85-6b151921c74f | -11.90188 | -47.39981 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 18fe919d-6890-30ef-a819-6f4def303a83 | -11.58645 | -43.6503 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 392.2 |
| 732a0ebe-d297-399c-99f4-e4e3cf54f3b8 | -12.25337 | -44.76038 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ce652652-fa3a-3458-a4ca-55e2311bd13a | -11.66017 | -43.67712 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 0b8aac2f-d749-3829-b224-4169722cebe5 | -12.20871 | -44.74355 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 7ed66e41-5eb2-3b67-b5cf-0942bed7c5a7 | -11.89108 | -47.38709 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 71691284-3499-3864-a000-a8d88a4398fc | -11.76818 | -44.96069 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d3a5503b-ac9f-311e-a8eb-b2c9c7b2df23 | -17.39252 | -45.47779 | 2026-10-09 15:58:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c397a93a-e79f-3db3-80c7-ad4667a23bcd | -11.57393 | -43.69094 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e167e5f0-7428-37dc-bf1c-dcd16094639b | -15.79931 | -41.33204 | 2026-10-09 15:58:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0aaa357d-bcd2-39bd-a7a0-445b35caabc1 | -12.82038 | -39.22223 | 2026-10-09 15:58:00 | NPP-375 | CONCEIÇÃO DO ALMEIDA | BAHIA | Brasil | 2908309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 31d37aaf-0b30-3f95-be55-eff99788c58e | -11.45554 | -43.38047 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| cc43251e-6171-3d4f-a8c1-afbf7b921d22 | -16.96828 | -41.15847 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 02e99dde-4512-3c1c-a43f-d4262fefa93d | -14.06223 | -44.80038 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e9516acc-7ccb-32d2-ab0d-b8480574e83a | -15.38749 | -41.89819 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 3b926d01-32cf-329b-9d34-1269fec49de3 | -12.24154 | -44.7549 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c322bb79-c94b-39ae-ab16-2890880cbcda | -14.83809 | -41.27748 | 2026-10-09 15:58:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4fd2d79a-6bd9-3c91-878f-32604a15a5aa | -14.09886 | -42.47844 | 2026-10-09 15:58:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 137af289-7bdb-3a75-880f-99bfc952eea0 | -15.38533 | -41.92693 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.5 |
| 68ebd254-82ed-340a-9d2d-c47386733a62 | -12.18493 | -44.81129 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 7510c06b-1688-38f3-bdb5-2268b780fd95 | -12.05764 | -43.41428 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 36cb8cf1-3ff3-3f27-b05a-f5aa6ce81ce9 | -11.83409 | -43.60602 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 54c59a02-2f6e-329d-91c0-06a16723b01c | -14.57336 | -43.83492 | 2026-10-09 15:58:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 79b83037-9505-368f-92b4-39de621e4e2d | -11.994 | -43.47282 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6912e5fd-6320-3a7c-b04c-7e48deb16633 | -12.9033 | -45.11285 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 952d05d7-9671-3375-a7cb-9d013452f233 | -15.84881 | -42.02962 | 2026-10-09 15:58:00 | NPP-375 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.4 |
| 9d55133b-6d76-3bc4-9c9e-c92a13a47860 | -12.02556 | -43.43614 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0fcecc20-c71f-3729-9f6d-70c9b65dd191 | -15.12228 | -43.62927 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 0365cd6d-3bf5-337a-a256-4eebe72ac841 | -11.08325 | -37.22261 | 2026-10-09 15:58:00 | NPP-375 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 0457d33b-4c1e-3c8b-89ec-5263ca1a54ec | -13.42581 | -47.26076 | 2026-10-09 15:58:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5123085b-d12e-39b8-9da0-a5f2c0b9eaef | -11.78356 | -46.79975 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 071ed9a5-1ebd-3e97-92d1-0b6611f71e41 | -11.59172 | -43.69284 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d3d5cd70-c586-378e-b3de-fd8aceca1864 | -11.77393 | -44.95544 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 35a085ea-7741-3aa3-8151-dfc0bce0ca21 | -15.25033 | -42.36548 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| b7b55fa9-901b-3450-b145-4e6c5446e0fc | -16.2439 | -44.05898 | 2026-10-09 15:58:00 | NPP-375 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 88f3f58f-46c5-3a95-8346-90fa7c60ec01 | -16.854 | -41.08774 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.5 |
| be4d4a62-48c1-3f83-be14-c4858763ba45 | -11.57436 | -43.69441 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1db4fd9f-d163-36f5-8d0b-6619fb3b0a95 | -11.66317 | -46.77245 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 507ed0d7-e34c-3e3e-a955-c243f8ac5773 | -11.60172 | -43.63237 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 401c9706-034d-38c3-9a02-1717a98387a3 | -14.24874 | -43.74063 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9ce5493c-7b1f-3970-b061-54aa77640479 | -11.60414 | -43.6986 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 065d1528-3851-3353-9679-8578d588569d | -18.28578 | -42.23895 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c86a1e71-3dbf-30d6-a573-de82e451e5cf | -11.70102 | -43.42265 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 704103f8-2916-399a-aaf8-605e8ef9b6ed | -12.16023 | -45.34821 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 076ea976-f736-3ece-a984-e71afa051f67 | -11.99463 | -43.46873 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3444f6d2-5a70-31a0-ac5e-96a8b57de66e | -14.64638 | -41.27714 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 74adccff-82a8-344d-adcd-99afbccbfd93 | -11.79468 | -40.92516 | 2026-10-09 15:58:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ceb8074c-36ff-3a1b-935f-ef6724f9e3c9 | -11.83842 | -43.59336 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 049993dd-e4c4-3403-aab8-92b5c39018c8 | -12.233 | -40.20516 | 2026-10-09 15:58:00 | NPP-375 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| ff5c789e-d171-3950-a9c7-fa9572303d91 | -13.38247 | -39.38795 | 2026-10-09 15:58:00 | NPP-375 | PRESIDENTE TANCREDO NEVES | BAHIA | Brasil | 2925758 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7c16c305-0f67-38cd-a97f-e4dc92db1978 | -12.22118 | -44.74245 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d93da672-6dc7-3c21-8c11-2259f2977711 | -18.00404 | -44.30167 | 2026-10-09 15:58:00 | NPP-375 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9170f798-cf3a-3d53-8f46-fd0ef50f20f8 | -15.25585 | -42.3645 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| 9408dffc-3544-3063-9c0d-b911f5eb516f | -12.25515 | -44.76336 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e66219ba-0995-38fc-88f5-59c8639adeba | -15.37955 | -41.92421 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.5 |
| eef95012-2e7f-32d5-81a8-0c556486602e | -12.23255 | -44.78595 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 696bc5a0-2119-3593-8a60-334254ac8767 | -11.33242 | -39.71365 | 2026-10-09 15:58:00 | NPP-375 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| a6dd5e0a-36a9-3e40-9e20-daead21abb72 | -11.99069 | -43.4847 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d47f703f-fe40-3a5a-86ce-b0630961a1e3 | -13.47464 | -42.47708 | 2026-10-09 15:58:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 73a0a0dc-4221-313c-aa99-17b691c46c5e | -12.19526 | -44.62735 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 9ea5175d-ea42-3690-9562-cfdd40276f99 | -11.59263 | -43.6496 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| f0b86b7f-3b20-3c75-b513-52a022e6dbca | -12.35945 | -40.31076 | 2026-10-09 15:58:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0709534a-2cd1-3f08-939a-f57edf133975 | -15.26258 | -42.37481 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| d31f609f-205e-34c1-9329-295c9e4b4df5 | -12.24387 | -44.73156 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 86728455-a2c6-389e-aace-1e466b4d5011 | -14.62519 | -43.68536 | 2026-10-09 15:58:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f5d5f291-3a3c-39ee-ab83-d6eeb4088b90 | -12.91612 | -45.11137 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a4957161-0d43-3dac-9967-97c08c9a635a | -15.5781 | -44.52878 | 2026-10-09 15:58:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1c850475-69f2-3a06-94db-0d7402775dd4 | -12.36584 | -46.56937 | 2026-10-09 15:58:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 591741e9-c442-3620-9405-55849d77473d | -12.19471 | -44.62264 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 145fd7db-c847-3959-972f-71b5a88d2737 | -12.21551 | -44.7479 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cd39e7dd-7819-3624-8ef7-b5043abca86e | -13.33181 | -40.38094 | 2026-10-09 15:58:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 30680de8-9a35-37f9-bca4-55b922e9cc28 | -11.46727 | -43.38286 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| c65dae32-5d5d-38e4-99d6-336141c97b58 | -11.98253 | -43.47385 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b0667edb-ffd1-363d-980c-fad3dc59bf16 | -13.25994 | -44.00486 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a1f3cc2a-8f49-326b-ab2b-a8f56ce2f4b0 | -12.20987 | -44.75359 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 151b4a44-87b7-3802-9374-e4f207c99829 | -18.32818 | -42.36773 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| aa57fd20-b553-3a9a-8fad-c85124c88733 | -16.12717 | -43.40045 | 2026-10-09 15:58:00 | NPP-375 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b52a661d-403e-3302-9b18-0b87061084b2 | -12.20764 | -44.6263 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c23d0e78-d9bd-3115-b59b-5bde6a268e2d | -17.51414 | -43.67456 | 2026-10-09 15:58:00 | NPP-375 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6ff1318c-f7d3-3cfa-ba1a-bc9b95e35aba | -14.57419 | -43.83392 | 2026-10-09 15:58:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 6ddf9b89-056c-3a3b-aa54-cf8cedc3d0ad | -11.84513 | -43.60069 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 74004596-bdc5-3063-a1aa-111cafaa75dc | -11.60598 | -43.61979 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4f97594f-bd37-3cd1-8ff7-0bc80116f839 | -11.46118 | -43.37976 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5e7b600c-6f22-32ed-9a5d-44046cd5f12f | -14.05125 | -44.81771 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| dbda1868-1d7b-32c0-acfd-954d9ad2a8d8 | -12.21478 | -43.94005 | 2026-10-09 15:58:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 3c620511-bc44-32d9-b13e-341404954696 | -10.99826 | -39.61397 | 2026-10-09 15:58:00 | NPP-375 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 6a5e9382-8349-30f7-9697-d5a493b58b9f | -11.96581 | -43.47934 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |


[Clique aqui para ver as próximas entradas](README257.md)
