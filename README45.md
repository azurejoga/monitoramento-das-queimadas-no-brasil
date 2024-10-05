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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffc88d25-57b0-3a07-b104-6950a35846e6 | -12.25647 | -45.60057 | 2024-10-05 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f61937e5-53e9-3075-a3d5-ce873eff12b2 | -11.56403 | -42.18266 | 2024-10-05 03:49:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bbd85ce5-78db-3967-a3e8-0d42f97568bd | -11.241 | -41.64114 | 2024-10-05 03:49:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e13c804-4e2c-3a66-80ae-680e79152b4c | -11.32781 | -45.52433 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d67c252-13a9-3ec9-9b52-ea4c6fcb88e6 | -11.32218 | -45.52825 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 143233b2-3e6e-3957-9619-8df889c49fe4 | -11.31744 | -45.52732 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ff7c4f2-fecd-3af5-8f94-a7a2a7767694 | -11.31655 | -45.53208 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 996f9b30-7cda-3762-9892-8953274fee32 | -11.67396 | -45.26181 | 2024-10-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0eb3784-974a-336d-aaa0-0720546c750d | -11.67221 | -45.25265 | 2024-10-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b40d546a-8e97-3b9a-9a11-4d87d57254f0 | -11.67132 | -45.2576 | 2024-10-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 03286bd6-8979-397f-be7d-39cf3908e8da | -11.2198 | -43.32504 | 2024-10-05 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 717b6c25-e3da-3157-899e-f0514b5d59eb | -11.21568 | -43.32438 | 2024-10-05 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dc3a0e0e-71fc-30fd-a441-d22622aeeab4 | -11.1959 | -43.34052 | 2024-10-05 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 86abd223-043d-3dc9-a524-c46e222c0f61 | -11.11281 | -43.33837 | 2024-10-05 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c1cc45ff-733e-3ff7-90ab-4d416821c964 | -11.1087 | -43.33763 | 2024-10-05 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 025e3952-9369-36d6-a466-d86d609ef6f4 | -10.98795 | -44.43461 | 2024-10-05 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0a38f06-00b6-35b6-93dc-aa87be658d33 | -11.15192 | -45.04013 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bc00542-9392-3f93-9eae-24b5be5a1fb5 | -11.14864 | -45.03706 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2852333a-6bfe-31e4-93ea-e53d71de5581 | -10.84204 | -42.84835 | 2024-10-05 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0f23e13-ef24-3f40-b11e-264c83a430d8 | -10.83864 | -42.84411 | 2024-10-05 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acdbd3be-0da3-3211-9006-1f746623e241 | -10.83803 | -42.84766 | 2024-10-05 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1853a874-d424-3899-b742-f86b3d320901 | -10.83741 | -42.85121 | 2024-10-05 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 4506b762-bc08-316e-bfad-380922a84b62 | -10.47921 | -43.65164 | 2024-10-05 03:49:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d79a10e9-bd76-3cf2-839a-b532d4963b05 | -10.61806 | -45.19418 | 2024-10-05 03:49:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f1b5551-0b34-3d41-812a-8bb3802d9058 | -10.27086 | -36.33577 | 2024-10-05 03:49:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 8bfa2be4-a097-3b74-922e-67c3cbeca7d3 | -10.27031 | -36.33937 | 2024-10-05 03:49:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| b1df1b30-9369-36dc-a285-405abcd7f635 | -10.26751 | -36.33524 | 2024-10-05 03:49:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| eab57506-da24-3dd8-950e-ce3fdb860f1d | -10.26696 | -36.33884 | 2024-10-05 03:49:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 5b704c28-3e53-3b3a-bbf8-cfede203ac2a | -10.18282 | -36.20047 | 2024-10-05 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 71c9a962-09d1-31cc-8753-51c32efd9eda | -10.28057 | -45.4723 | 2024-10-05 03:49:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e8b605a4-641a-32ed-aa52-b5a050cdd4c4 | -10.27659 | -45.4668 | 2024-10-05 03:49:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d8577254-9c7f-3377-9b02-b9b0aad93280 | -10.2756 | -45.47224 | 2024-10-05 03:49:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 817706db-2c03-389d-9266-3c22632798df | -9.8393 | -46.7277 | 2024-10-05 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0fb06bd7-d407-374d-a61a-11a70411829d | -8.10484 | -35.17205 | 2024-10-05 03:49:00 | NOAA-21 | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d03a890-c4e6-37d7-8b40-ae9e9da69275 | -8.05186 | -35.1524 | 2024-10-05 03:49:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2835ef08-05a8-3ddb-a048-9db300b7ffc2 | -11.40887 | -47.1951 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d20c1d74-ef8a-3e7f-90dc-bfef78947766 | -8.7691 | -44.82034 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| b085e4c8-c847-35d5-87f0-d4ced1e60482 | -8.76818 | -44.82555 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 7cad53dc-4c3d-3f15-884a-16bf5b396c1f | -8.76725 | -44.83083 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1f5057b9-4e2f-3114-b08f-c3408982432f | -7.3503 | -41.94937 | 2024-10-05 03:49:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 609ed311-2192-3aa5-b062-29975d2aadf6 | -7.34861 | -41.94873 | 2024-10-05 03:49:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f5cb1db-35d4-346f-9382-add40fba5773 | -7.22707 | -43.33415 | 2024-10-05 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 347ad717-b14d-3459-9e4c-f13d93c100d7 | -7.29896 | -42.24953 | 2024-10-05 03:49:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3ec7deee-91f9-3deb-8f4c-4304931d3005 | -7.29853 | -42.24949 | 2024-10-05 03:49:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dcf08e72-a780-3bf5-bcca-547290624537 | -7.12952 | -42.61622 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9fa932a-0716-3af1-bb65-92382b849c21 | -7.12759 | -42.6082 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 09a253a8-fabc-3245-87b5-c224397879b2 | -7.12625 | -42.61593 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7b9afe49-a48a-3f54-b0c7-7dccd7183a72 | -7.47055 | -43.99 | 2024-10-05 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 968693d0-ea5f-3381-8b18-1eaec94c4198 | -7.44266 | -44.73737 | 2024-10-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ded0bec2-df08-362b-a924-376f0eaf79d4 | -6.28255 | -42.7693 | 2024-10-05 03:49:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c8cf966c-4f1f-3640-a632-829d7144f09a | -6.29138 | -43.85111 | 2024-10-05 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba40cf50-869a-3c35-b090-ce932ace3066 | -5.97882 | -43.94267 | 2024-10-05 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0c18533-a34b-3e79-b3f2-3a8a4afa1416 | -5.93982 | -43.90211 | 2024-10-05 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e495d661-79ce-3779-af16-e288ed0b70f5 | -5.93804 | -43.90045 | 2024-10-05 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7ef0943-e53a-3b0f-98c3-208c6a8717c7 | -12.26362 | -45.96742 | 2024-10-05 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 96c1f3bc-f95c-3fff-bc45-9dcd43cec12a | -10.83679 | -42.85476 | 2024-10-05 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e14cc4ba-4910-3b39-ae8d-0afeff4cdef3 | -10.76993 | -45.54933 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21b9b3b3-6ef0-329d-b28f-48d42afc4378 | -10.74019 | -45.60759 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 292854f6-7d02-35f9-bd97-cbc1cce61281 | -10.7393 | -45.61255 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 42689bd5-b499-37ce-a952-ba2b795f32fb | -10.73891 | -45.60913 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c58dbeaf-13fc-38fd-a5da-a54520cd8c91 | -10.73798 | -45.61412 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 033b639b-7fee-3aa1-b03a-1991b278b174 | -10.61896 | -45.18927 | 2024-10-05 03:49:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b54ca7d6-b1a9-32d7-9807-d23c43d8ec88 | -10.75961 | -46.1876 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46e873a0-a90e-3555-bc39-9d0a337e5c89 | -10.75404 | -46.18966 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da403adc-c294-315b-af5a-3df841d6ccfc | -8.09505 | -39.5797 | 2024-10-05 03:49:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ff01c75-c124-31c2-848f-82b4c2df2173 | -7.90416 | -41.14442 | 2024-10-05 03:49:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e9dc7e26-5f71-31d4-9c34-b3ab49411ec7 | -8.33295 | -41.16031 | 2024-10-05 03:49:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 083a4ab4-4f0c-3011-bf63-115742c7dfd6 | -8.15767 | -41.34904 | 2024-10-05 03:49:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 386e6e82-28be-31cd-8185-98a62382afec | -8.15386 | -41.3484 | 2024-10-05 03:49:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fd9f5df2-f974-37ec-b2bc-85bf43d93e06 | -7.79913 | -43.10705 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7237260c-7972-34aa-bd16-ffe5751be6a5 | -7.79844 | -43.11117 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 0f2b3d00-ebfc-3468-bb2d-f24468ac4411 | -7.79774 | -43.11528 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| bb4eadaa-80ae-3796-81dd-46a0a574d35e | -7.79415 | -43.11045 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 88d9f4cb-5f8f-3f63-9890-36a479f5bbb5 | -7.79345 | -43.11458 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c5602ae6-9efb-3089-8c78-372bbd859e9f | -7.74694 | -43.07709 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1621ce6d-c5b6-3c83-8616-98bbf5de5333 | -7.74627 | -43.05544 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1b09b93f-2fc2-3a7e-9256-aeae6c9a17db | -7.74557 | -43.05953 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e3cedabc-ef51-3285-b13f-18f7e490767f | -7.74486 | -43.06365 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f51b19bb-27ab-35b4-aba0-e1e76a828562 | -7.74413 | -43.06784 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fe547ae9-1a88-3cfa-a94d-863a0e150488 | -7.7434 | -43.07209 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| afa33710-c967-3381-8236-b67846d826e3 | -7.69851 | -42.98085 | 2024-10-05 03:49:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 9e92c70f-5427-3a56-925e-986dc2fabbb1 | -7.69783 | -42.98487 | 2024-10-05 03:49:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9ec10c6b-ade5-3699-84ce-e8f7b2b73bed | -7.62976 | -43.70092 | 2024-10-05 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4961cc67-dbe5-3fbe-b331-5b252e68a5c1 | -7.94446 | -42.46107 | 2024-10-05 03:49:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7af42189-5cb6-3cec-b7be-4d23aa72295b | -7.93626 | -42.4597 | 2024-10-05 03:49:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 64f62561-a667-3ed2-8dfc-9ce5e136b5f0 | -7.66152 | -42.45478 | 2024-10-05 03:49:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bbda5de9-ecf7-3490-93c8-9b3048226f9a | -7.65418 | -42.42325 | 2024-10-05 03:49:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1ad2dfb0-3024-3176-a362-b37eaf0b30d3 | -7.65009 | -42.4225 | 2024-10-05 03:49:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ea4a362-acba-3e0a-b27d-eee56c579bd8 | -7.64599 | -42.42176 | 2024-10-05 03:49:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| daf34515-7ef0-351c-8198-7fffa6dcf7f5 | -7.64189 | -42.42104 | 2024-10-05 03:49:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c21fe4f-720e-33b5-8b87-200f50cb23a9 | -7.63779 | -42.42032 | 2024-10-05 03:49:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 142adb80-c4df-307f-aac1-d54d030e0d54 | -7.63523 | -42.48495 | 2024-10-05 03:49:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 36cc5b5b-dd08-3a9c-afb3-565377ef1771 | -7.63305 | -42.42337 | 2024-10-05 03:49:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1d1c248-43af-35ae-83bf-bea7824676bb | -7.6311 | -42.48429 | 2024-10-05 03:49:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e7808a2a-4a41-3cf6-95a8-eec4fabd5650 | -7.6283 | -42.42644 | 2024-10-05 03:49:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43c94333-1e73-3183-965b-4f00cc06ca0c | -7.62766 | -42.43015 | 2024-10-05 03:49:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1a33dc2c-b9fd-3419-88d2-dffaa63250a5 | -8.36685 | -43.6548 | 2024-10-05 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c62884ff-c15c-3b81-ad82-2e654e920b39 | -8.36612 | -43.65908 | 2024-10-05 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe13d6ab-5bac-3b91-8480-26b1215676ec | -8.3661 | -43.6574 | 2024-10-05 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1d9bb8d4-b8bb-387a-810c-a6285cdc77d2 | -8.36404 | -43.6435 | 2024-10-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README46.md)
