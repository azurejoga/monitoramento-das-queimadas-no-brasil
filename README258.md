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

## Dados Diários - Página 258

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b54a81a5-980a-380e-a80c-d07f6281818f | -18.32464 | -42.38031 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| 0c6a3296-241b-395b-8aac-b15b296a9f60 | -13.495 | -40.72103 | 2026-10-09 15:58:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 79a89e60-722f-3e69-9607-6b7210158775 | -11.89157 | -41.62511 | 2026-10-09 15:58:00 | NPP-375 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 7611a876-9791-3a97-8667-7fabd9104f5d | -15.22436 | -41.10508 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3b765b20-4276-3928-b418-91fa0d767b97 | -17.535 | -39.94197 | 2026-10-09 15:58:00 | NPP-375 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| e9247f7e-837b-3bd2-8b9b-8b64dd7dab46 | -17.4501 | -45.06141 | 2026-10-09 15:58:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5537f333-9b7a-32c6-9106-c014781bdbc6 | -14.05155 | -43.83427 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 920521e6-8196-3ba1-953e-2205b7f7aa92 | -17.45859 | -45.05542 | 2026-10-09 15:58:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1408a56d-acc7-3cf1-a9a3-cf3a8abacae1 | -16.15855 | -42.31553 | 2026-10-09 15:58:00 | NPP-375 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9b91a0d9-cb85-36bd-b0e9-5a549e4685fb | -11.97329 | -43.49318 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| bf765136-9a19-339e-ae45-cd505a55ad3d | -12.229 | -40.20258 | 2026-10-09 15:58:00 | NPP-375 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| c9d8576d-a91b-31bd-a046-8d6eee38a882 | -15.34457 | -42.7088 | 2026-10-09 15:58:00 | NPP-375 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 85c50e30-8ad8-3638-9923-37f84d4b3446 | -12.14557 | -44.72461 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8db0bf54-299c-34d0-a002-b282d9cf22c3 | -11.98576 | -43.49225 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2f529592-f276-3ad7-a3c2-ae688479762f | -15.26137 | -42.36366 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| 4ac9dde7-4da5-3906-a6c3-9cbf51b6a9d6 | -14.05438 | -43.83743 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 41516ec5-748c-3462-b0f7-514945cf09ec | -12.25907 | -44.75497 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 19f929fd-ba61-3c14-af8c-4b9428400d8b | -11.99823 | -43.46015 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ea689d55-1fb0-378d-9bdd-6c961a6cc924 | -11.58683 | -43.70065 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| a00b7e51-db2f-3d41-b0b4-9661bcbc670a | -12.90971 | -45.1121 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 40e00017-3d53-3bf4-b9c8-e122a80bb74d | -12.82265 | -44.63977 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 82943ae1-99af-3deb-957d-4c0669324b0e | -12.04716 | -43.42324 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 2a908b44-96cd-373d-889e-3428155abddd | -13.7564 | -43.62489 | 2026-10-09 15:58:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5fb7fc62-fc30-3f8b-9a7e-10c7e32e2a5b | -11.46864 | -43.39436 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0f9e554b-648a-3f3c-b3f3-19d7a15041b1 | -11.89912 | -47.39358 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| fa374b71-4d56-3b91-9146-6a6337cc9602 | -12.24833 | -44.75903 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8eb56f4e-3dd2-33f9-83eb-a8ad01e6cb97 | -11.77339 | -44.95074 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 41efe105-5edc-3887-b5c0-10c7676bce69 | -15.26176 | -42.36728 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 6cfb9afb-b016-335c-ac05-e159a09f90cd | -11.77101 | -44.95909 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 91df059e-7bed-3d9c-99e0-f5b5e6957e01 | -12.15439 | -45.35429 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f9141b3c-5cbb-3d24-9658-a5cc19e1b1cd | -11.9951 | -43.47271 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1d6d996c-e7f9-3012-8bff-095cb8037db2 | -11.45788 | -43.38021 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0411dbdb-015d-3845-a11d-bcfd6de7d385 | -10.9693 | -39.29879 | 2026-10-09 15:58:00 | NPP-375 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9a0e3d44-11cd-3bc6-ae23-64f57a9568f8 | -14.7637 | -40.90199 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e3621516-deda-3488-a1de-03a0ad4a8e60 | -14.57468 | -43.83853 | 2026-10-09 15:58:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| d18bd0c2-9172-3001-9c05-8b4b839b2f57 | -12.82687 | -45.55606 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 78dcc3fc-92c1-313e-b147-d327a5c0e74a | -13.47505 | -42.48067 | 2026-10-09 15:58:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 1925dfab-4b54-36ac-a0c4-0db76972ea47 | -14.24826 | -43.73619 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6ba03cdc-b1ff-3b54-9830-27e62c18cdf9 | -12.33556 | -47.07538 | 2026-10-09 15:58:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1cc1d0ec-16c4-3327-a9ae-e5ffb640e97a | -15.5308 | -44.40206 | 2026-10-09 15:58:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 991cc68c-0cbf-3499-8f01-278e7c3b1fe4 | -11.98521 | -43.4957 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0d6eaedc-ea3c-36f8-8255-ded57bd8ebd4 | -11.59747 | -43.64505 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| f54655af-4df7-33f1-a901-f400536ed6c5 | -13.85045 | -42.64501 | 2026-10-09 15:58:00 | NPP-375 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| dbaeda71-21b9-3ca6-8dd8-e0596802767b | -11.9648 | -43.47104 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 367c56a0-760a-3048-a8f9-49bf035e4ff2 | -16.70477 | -42.53128 | 2026-10-09 15:58:00 | NPP-375 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 801b5eef-0c93-33a8-bf33-46ad4ee326ca | -18.08914 | -42.26686 | 2026-10-09 15:58:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b22a5306-8447-37ee-a925-907024b7d5b9 | -14.5211 | -41.25095 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 36.8 |
| f466a32c-5c3d-3147-8fa7-98ef66a7734a | -15.25113 | -42.37289 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 45a3e344-b876-39a7-b696-3efa401ba024 | -15.1218 | -43.62476 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 1e14a2c1-b19e-33ea-aba7-d5f533556eb4 | -12.15498 | -45.35952 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 66cda728-f5f2-3abf-8a3c-7f2636e2bba7 | -15.91195 | -38.95163 | 2026-10-09 15:58:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9d317843-608e-35b9-98c8-ad4a4afca625 | -18.26175 | -42.22988 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 61948405-d3a5-3c73-a179-9929f54b058b | -14.83774 | -41.27448 | 2026-10-09 15:58:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 81a9c65b-8b60-3487-a2a1-61a457d79517 | -11.97417 | -43.50045 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| cb182c88-d291-3978-88c5-0feff3317aaf | -18.08307 | -42.26396 | 2026-10-09 15:58:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 39c37af5-7ba3-3091-9839-52349c06e78d | -15.25208 | -42.36945 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| cf8efa9c-22aa-3733-ad7d-559d907c7dc4 | -15.25384 | -42.38472 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| 8ed227ba-b1f7-37d1-bc5d-bb4a7a8b0245 | -11.98981 | -43.47717 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 78da90b1-f44a-3871-bb74-ee415a979be4 | -12.25457 | -44.7585 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 6a200595-6b57-318f-b7f1-0ea6a7699c75 | -15.92006 | -38.96099 | 2026-10-09 15:58:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b0669372-d530-3f51-84b4-47439cf1ca0a | -11.82692 | -43.59473 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 86a5b781-df2f-3931-bfa5-041609a36031 | -18.26088 | -42.22136 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 919d360c-a4c4-33e1-b75f-e537741231c4 | -18.32924 | -42.36764 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 53b4d764-5543-3348-b11c-85cc2fd1289d | -17.10205 | -41.56584 | 2026-10-09 15:58:00 | NPP-375 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| 85d30f0c-b87f-3268-af16-f128cdf01e41 | -11.99716 | -43.45148 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 711a4664-955f-3193-8419-f2523883e875 | -11.97521 | -43.46136 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 920e8096-3c51-376c-ad6e-e01ffefe0e53 | -12.36425 | -46.56761 | 2026-10-09 15:58:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| c826eab0-37c0-378b-8640-b116c9453450 | -12.0141 | -43.43704 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1e9488b6-caa8-3c52-95db-5b58757cd998 | -14.42941 | -43.93314 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0e7783c3-0f73-3d44-89e1-83359dfeca43 | -14.05591 | -44.80151 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2c31b8e5-a63e-389d-bd37-4679dc59e3fc | -12.22175 | -44.74735 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 81261534-cb6c-3206-984e-80a66e547f92 | -14.32492 | -41.30301 | 2026-10-09 15:58:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 94.8 |
| d3925b71-f92a-327a-8c78-0f7a87783580 | -11.96532 | -43.4753 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 6da0a3cf-cc75-3708-bdf0-0582dbdf38e2 | -16.97311 | -41.15428 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 97b00516-0ac1-3ca1-9713-b181d1e562d4 | -15.07061 | -41.13803 | 2026-10-09 15:58:00 | NPP-375 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 132ebcb5-4665-3ff5-a741-8738c1ac92ad | -14.04934 | -43.84714 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9a34e5fb-e0b2-3f0c-b234-fdb5eb75ba1d | -18.08522 | -42.26587 | 2026-10-09 15:58:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 6ec282e0-06b9-349e-be24-21f9f3bf023d | -11.96713 | -43.49025 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| b4bcbaa0-32b8-3ace-93f6-bc125e547222 | -11.99011 | -43.48833 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a6f312ff-0580-3bba-8de7-3a2d30ce021a | -11.59651 | -43.63294 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| b134a93a-0c54-3e6a-9627-2e39d2e727b3 | -14.42992 | -43.93775 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9c93a443-36ea-3998-8d62-948e7933662e | -15.84781 | -42.02339 | 2026-10-09 15:58:00 | NPP-375 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| 60ad14ef-4c16-3b06-958d-7da05d7c769e | -11.89991 | -47.40077 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 19706edd-eebc-3fd2-8cbf-95058a3e772e | -14.06054 | -44.7852 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 753e96e5-8050-31d4-8947-2731d6dced81 | -14.35446 | -40.86598 | 2026-10-09 15:58:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| ae28278a-078e-39ea-a164-1548a87a3878 | -11.60706 | -43.62355 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| e8f86d5a-d24c-39d0-b766-a94be7892229 | -12.31475 | -47.04978 | 2026-10-09 15:58:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 29644f2b-0829-3a9c-9cf0-403a2c203a9d | -15.38286 | -41.90538 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| 2b4e78b9-190c-322e-87d2-970343fe8601 | -14.27103 | -42.18866 | 2026-10-09 15:58:00 | NPP-375 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 3b5c8c9e-ded4-3bc0-9ade-755805297866 | -11.97775 | -43.48216 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| c6ae886d-d694-3ce7-8d05-304075c763c1 | -16.24497 | -44.06948 | 2026-10-09 15:58:00 | NPP-375 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 736f5d46-d30e-3859-865d-78840200dba7 | -15.263 | -42.37865 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| a2b327c3-77e2-3a21-bad2-bd3443a50027 | -12.21898 | -44.83254 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 761c50b8-7cb1-39b7-bb33-f90e8860a686 | -12.04668 | -43.41927 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 9a932058-a00c-3d82-9a25-79000c95beb1 | -17.28429 | -43.8988 | 2026-10-09 15:58:00 | NPP-375 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a41bf26-4e72-37b4-8f5e-0d673818c789 | -15.47906 | -41.21993 | 2026-10-09 15:58:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8ca488d8-d7e4-313c-bcaf-63d966e7c581 | -14.76363 | -40.89979 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 8646bd54-7b55-3dbc-a211-a86c8253e654 | -12.00934 | -43.44585 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1f3e00fc-7a46-3feb-93e1-bb3fa43db545 | -18.33563 | -42.38322 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7dc98b70-71cc-3cd3-a562-4a44a8bc3b11 | -17.45188 | -45.05614 | 2026-10-09 15:58:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README259.md)
