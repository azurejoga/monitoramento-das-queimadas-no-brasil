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

## Dados Diários - Página 263

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94768453-03c4-37ff-bf34-ff02ce2db92e | -11.60132 | -43.62426 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 54255a3b-6cae-3b4e-a2a8-e4861c1225bd | -15.9896 | -44.8587 | 2026-10-09 15:58:00 | NPP-375 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8e8809a3-2f9b-3368-bb4d-0bbb756d2305 | -11.77834 | -45.56982 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| c447fb74-6e80-3cfd-89d4-c6818d8a0170 | -15.13686 | -44.05718 | 2026-10-09 15:58:00 | NPP-375 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 365ec2ce-71f3-31d3-a813-a6d0aa350c6a | -15.32563 | -39.682 | 2026-10-09 15:58:00 | NPP-375 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 16e31104-127e-363d-8c84-7672fe5b4e6e | -11.98496 | -43.48533 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ab2df8b3-de8f-3d84-93c2-57ce8fb3c889 | -11.78487 | -45.56932 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 236a8850-2f11-3092-bf7c-099079f299d9 | -16.34639 | -41.73123 | 2026-10-09 15:58:00 | NPP-375 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9470d625-1676-3b9c-9cd3-8cd5cede3951 | -14.5064 | -40.60241 | 2026-10-09 15:58:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 854be23f-91f2-3527-b12f-96e2219aebb0 | -12.16231 | -44.81234 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2cc0c0e0-853f-34db-b86f-80bfa699122f | -15.48427 | -41.21978 | 2026-10-09 15:58:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ba0a51a0-5e55-3e9e-94a8-9527becaa24c | -12.14794 | -45.35503 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 936b12ae-4a2e-30a8-81d1-11dd351d5fab | -16.93645 | -42.10495 | 2026-10-09 15:58:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| fb8703de-aabd-3c27-8a91-8aff4e0223b1 | -18.32327 | -42.37656 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.8 |
| d53d8533-7fdc-318b-8423-5c58d7cbcc63 | -11.60222 | -43.63636 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.0 |
| a31005c2-e455-3f44-b9a7-a765d86f2956 | -15.3302 | -39.68088 | 2026-10-09 15:58:00 | NPP-375 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 66008948-2143-32fb-aea2-98365cf94893 | -16.25865 | -42.52473 | 2026-10-09 15:58:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6000cc2e-27fb-358a-b2d2-f42d4e75fe75 | -15.38082 | -41.88762 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| 776b3e2b-460e-3f6d-b792-9097d7bbbfdd | -13.9653 | -43.93564 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0eb2a0b5-b65d-3c14-b34c-25a1c5ecf122 | -12.34349 | -47.08195 | 2026-10-09 15:58:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb883dc9-7a3c-32e0-8c3c-1e4afde413dd | -11.99448 | -43.47668 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| b4475808-b622-3aa7-9190-5f6ba16b4c5d | -11.83362 | -43.60202 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6b1be741-c3e5-3507-a3e8-1186f165b90d | -11.84829 | -43.52993 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ce5a622-c647-335e-8b60-713debb2f0ec | -13.58373 | -40.01577 | 2026-10-09 15:58:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 12d94163-4fa4-304b-9b3a-99ec09b3315c | -12.24487 | -44.72971 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ebfa31f1-fa81-3b76-91db-c398fad8a6dc | -16.23766 | -44.05978 | 2026-10-09 15:58:00 | NPP-375 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| dc9fcd25-7197-39c9-b8e1-b94e679d11ba | -12.15118 | -44.71897 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 415a5690-bd1b-3d63-a487-9753f99ea72b | -11.46352 | -43.37952 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 8634ff92-535d-3835-8b0a-a6b60d0b167e | -13.72826 | -40.09598 | 2026-10-09 15:58:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| fc694684-7845-3de7-8ca0-3f04b087bf88 | -15.01016 | -46.25338 | 2026-10-09 15:58:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 03d5bdb4-06ac-334a-b139-9a9a3c442e3a | -15.53036 | -41.01469 | 2026-10-09 15:58:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6f3a01b5-09d6-3cd7-8ddf-26662ac8c2f9 | -11.59706 | -43.68874 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9e54a052-a041-3b48-b367-5bf68a6cfbba | -12.0931 | -38.66285 | 2026-10-09 15:58:00 | NPP-375 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 27db7dd9-9112-3e2b-b669-434373259a96 | -14.33075 | -41.30855 | 2026-10-09 15:58:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 10ec749a-66ff-3ded-84e7-de72a116515e | -12.18962 | -44.63269 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 289.2 |
| b948e142-cea3-33f0-b114-e9f8d25f71a0 | -15.38988 | -41.9189 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| 023f1661-2639-31ed-a868-be39dd1ef6c7 | -15.92257 | -38.96384 | 2026-10-09 15:58:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e759a015-ede3-3eda-ba22-52495f1af978 | -15.33949 | -40.84667 | 2026-10-09 15:58:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 7535e169-7ab3-31c9-9128-ff9727da253e | -13.40764 | -39.79337 | 2026-10-09 15:58:00 | NPP-375 | CRAVOLÂNDIA | BAHIA | Brasil | 2909505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 3e492dd9-75ea-39da-b94c-d682f725c760 | -11.84863 | -39.70312 | 2026-10-09 15:58:00 | NPP-375 | PÉ DE SERRA | BAHIA | Brasil | 2924058 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2fa0c3c8-894d-379b-9e15-4553ae0f2907 | -18.17243 | -41.96778 | 2026-10-09 15:58:00 | NPP-375 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0cd13edd-92d8-3f71-bb42-ab4594505bdc | -18.31758 | -42.37788 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.8 |
| cd21bf6f-42d6-374c-ad25-3ad6157e5348 | -11.70669 | -43.42196 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8c81e267-b359-3778-8da4-dd64df4af07d | -14.0506 | -44.79927 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9910dab4-0df7-352d-9356-3b0440b160a1 | -11.84465 | -43.59667 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 4be1badc-da36-3e35-b41d-af40fbcec082 | -11.98742 | -43.45646 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| cd30a35f-7ee9-342c-be4f-0d2a46535927 | -14.92681 | -42.00686 | 2026-10-09 15:58:00 | NPP-375 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 2a9eddef-0492-340e-8e83-b598ef0add03 | -16.0762 | -45.96241 | 2026-10-09 15:58:00 | NPP-375 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d5804e72-18ff-39bb-89c1-016434814dc2 | -11.98921 | -43.48104 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 607c12ed-d2a1-33b2-be73-ce920ce61fc6 | -11.58732 | -43.70465 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 09dd9a4d-f0c6-3ddc-aa49-edbfdb587060 | -15.42702 | -44.34794 | 2026-10-09 15:58:00 | NPP-375 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 69870bed-34c6-3f59-90e4-1420c351782d | -11.89832 | -47.38634 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| c0c0dd7a-52f0-3658-95e6-60a9fb106b52 | -14.2512 | -43.73465 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 9ac2c901-a2ca-376c-8267-9e8b8f78ba78 | -15.84821 | -42.02691 | 2026-10-09 15:58:00 | NPP-375 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 6693210e-fed8-3fef-8a17-60186749fcd2 | -16.82303 | -42.30053 | 2026-10-09 15:58:00 | NPP-375 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e2a3c037-98bc-3c87-a49a-149b71c3aeb9 | -17.15422 | -39.43738 | 2026-10-09 15:58:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| e058c05b-a2f0-3563-8d2e-27addf15e078 | -15.32072 | -41.23602 | 2026-10-09 15:58:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a6430041-8861-34f1-a278-c105b4f8fc46 | -11.97994 | -43.50014 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 42e63cad-d7f3-3079-b341-efd4434805a6 | -12.00467 | -43.45538 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 4dc803f1-29c3-36ae-a4f4-76c6fa4bd12c | -15.2224 | -41.10556 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 61635e3f-e745-33b1-a6e3-735a7010f87a | -12.80289 | -42.47154 | 2026-10-09 15:58:00 | NPP-375 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 7f35063d-4743-3cef-9d9b-911599f8dacf | -16.00676 | -41.2424 | 2026-10-09 15:58:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c8b77732-59b0-32db-93c7-90f407bb9d3b | -12.00302 | -43.44125 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| fca23bbf-7c7b-31d1-bfaa-fb99bc6fd224 | -12.2161 | -44.75291 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e15a5f21-194b-346a-8f7a-5f9f535b0e84 | -12.34497 | -47.3223 | 2026-10-09 15:58:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 37e4a4ed-51f4-306f-819b-788db09cdf06 | -15.06512 | -39.45329 | 2026-10-09 15:58:00 | NPP-375 | JUSSARI | BAHIA | Brasil | 2918555 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 26c020f7-51a8-30ab-8eff-b70db8830f7f | -14.04982 | -43.85166 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 084b0a54-94bd-3f56-8161-bda824b3f350 | -18.26131 | -42.22562 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 7c21e78c-fab6-3075-bf7d-902e71f0433d | -15.38325 | -41.90884 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 172.9 |
| 72675a85-83a9-30ff-90cb-34dbd14618c9 | -11.77717 | -46.80608 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 0b8a122c-7f38-3a1a-8301-abed01184681 | -11.99249 | -43.46058 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4b33e014-63a6-39c0-8858-e12ef2d09905 | -17.44569 | -45.06269 | 2026-10-09 15:58:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f95fbe59-5983-3da2-9f7f-a831729b1b95 | -12.05192 | -43.41478 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 9767d82d-913e-3cda-9bd5-1a1354d8d476 | -11.89238 | -47.37889 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 3b5f7530-5816-3d26-8848-0c1dc43c1fb0 | -16.86089 | -41.91214 | 2026-10-09 15:58:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ecd7c8e1-6359-3982-a43c-62fa2c6eeb8b | -15.00369 | -46.26012 | 2026-10-09 15:58:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6f97371d-033f-3384-840e-3837cb23c2c3 | -15.25803 | -42.37224 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| d035e4f2-0570-3ada-9b97-7a59ea8c6771 | -10.80697 | -39.36492 | 2026-10-09 15:58:00 | NPP-375 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 44.1 |
| e67078ff-bf4c-345b-b6d9-e62f5a9c5483 | -13.33241 | -40.38583 | 2026-10-09 15:58:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 0ec17d21-6b2c-3387-a126-7dd0eb9647f8 | -12.21045 | -44.75856 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 81536b44-5e1e-3b97-9fc9-4e9663d0fcf3 | -12.76899 | -47.0928 | 2026-10-09 15:58:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 0566bf35-ce1c-3bf1-aa22-8c78cd4deb50 | -11.58169 | -43.65895 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 3597871a-3abe-3203-92ff-6bfada317eaf | -12.00863 | -43.45057 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d9cc37ed-54ae-3cf8-a946-d12d2a16a1a9 | -13.56544 | -40.88993 | 2026-10-09 15:58:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 4b5660c8-7fed-3e45-a7f8-68003ea5e4fe | -16.14655 | -40.60328 | 2026-10-09 15:58:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 337ef88e-a50b-33bb-9040-224ac643a91b | -15.47869 | -41.21673 | 2026-10-09 15:58:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 35dcf816-1fa1-3800-a79f-b61070f47f03 | -15.38449 | -41.9196 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 272.3 |
| 2ffc4cd8-1d29-3b85-abfc-7200be3dca5f | -14.32566 | -41.30927 | 2026-10-09 15:58:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 30.9 |
| c0fb3a62-f660-3b45-8e34-2939d529ebef | -11.7677 | -44.95647 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5a4d5b38-f30e-344f-a882-c5871b7ddcf2 | -11.59172 | -43.64569 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| e0c621f2-0364-3dd7-89de-08da891d595f | -15.8814 | -39.94713 | 2026-10-09 15:58:00 | NPP-375 | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c7050700-1555-3ec4-b5fc-ff96a3ae71f4 | -16.34402 | -41.73216 | 2026-10-09 15:58:00 | NPP-375 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e4d3e5fa-9ffe-3c53-b6b2-81bc60b0e98f | -15.34447 | -40.84566 | 2026-10-09 15:58:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| a34608c1-c3fe-3a91-ba1b-60cb1009cf4d | -12.02964 | -43.47063 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 16cfa3d5-04e2-3dfc-930a-c48f98decd4b | -14.47316 | -42.05861 | 2026-10-09 15:58:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ef4337de-a2b5-3137-a9c4-5936b699b9ad | -11.89388 | -47.39332 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bd171d4f-39bd-3791-b7bf-e5d71a1623b8 | -13.1132 | -46.32991 | 2026-10-09 15:58:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8a7dd5da-62d7-3a45-af03-391eb7c1d84c | -15.87699 | -40.76324 | 2026-10-09 15:58:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ba4fc727-b419-34aa-91aa-c9439028231a | -15.74938 | -40.58556 | 2026-10-09 15:58:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ec5d2803-80a1-3501-8466-2ff143f83165 | -11.28347 | -41.12942 | 2026-10-09 15:58:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 30.0 |


[Clique aqui para ver as próximas entradas](README264.md)
