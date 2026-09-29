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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b857470-3c7f-35c6-a549-b4ff79f9e389 | -9.73055 | -39.68113 | 2026-09-29 15:46:00 | NPP-375 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f01aa2ca-5e1e-371e-9fc1-2d456e6f249e | -15.30478 | -41.77845 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| 0c728ab2-359c-3b65-baf0-3895c16bb20f | -10.92479 | -42.30571 | 2026-09-29 15:46:00 | NPP-375 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| a252ce71-dbb8-3bd4-9d8a-4ef26739aef7 | -15.08859 | -41.41208 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 3a887333-f0ee-32e3-9b07-cd2728ca11d1 | -10.29924 | -40.02048 | 2026-09-29 15:46:00 | NPP-375 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| a818cff0-bbbf-3518-87ff-d07bc08a5c44 | -11.6525 | -43.52266 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 30d09921-0be3-3bed-9d35-fb4d38bf7c92 | -14.97685 | -41.53313 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 41.3 |
| b7551643-b914-3f29-88e8-716c38a8a629 | -10.11586 | -43.92958 | 2026-09-29 15:46:00 | NPP-375 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 5b6e0921-c44b-30bf-b943-383881394305 | -13.33666 | -43.94567 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| c6c1cd7c-51a2-3560-abe1-c5982b22bad7 | -11.64426 | -43.51197 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 245dd05b-ccce-3902-a1a5-b52fcce5ec41 | -11.39279 | -43.38976 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71bfd73d-4d0e-394e-ae20-5a16f5f1dd86 | -11.45909 | -43.47601 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| aa797543-376d-39b3-a469-9777fb472b36 | -11.34711 | -41.27299 | 2026-09-29 15:46:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 2d039289-b7e4-355c-a30a-5fbdc2645b79 | -14.97049 | -41.53402 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b0669f08-646a-3f5a-8683-ad0d5f9b8db1 | -15.23542 | -41.7416 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 9651195a-c7e9-3efb-8ac5-24e77d82b300 | -14.06231 | -40.57331 | 2026-09-29 15:46:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 807fa6bd-3137-387c-a3fe-60237817c521 | -8.31151 | -39.3824 | 2026-09-29 15:46:00 | NPP-375 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f10f768b-bcf8-36fb-9bf9-bcdad6db26ef | -15.24632 | -43.27654 | 2026-09-29 15:46:00 | NPP-375 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 1acb4065-38a9-370a-9c4c-fc40c89e2f61 | -13.32792 | -43.95528 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 374.3 |
| 0600a5ad-f127-3655-a76e-4863702385ef | -11.39504 | -43.46366 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 3900f674-1f40-3e46-84b9-3a3aa5921026 | -11.415 | -43.45512 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 99d94ddf-8365-3174-8727-25565add944c | -9.41019 | -36.68711 | 2026-09-29 15:46:00 | NPP-375 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 73d32751-77e0-30d3-8d22-da561b2db40f | -14.38288 | -41.67012 | 2026-09-29 15:46:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 248b508b-df3a-3bd4-9e9d-e2f270343b9d | -12.91473 | -40.04122 | 2026-09-29 15:46:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b7a756e5-9fc0-344f-8f0f-0ed676a2bfa6 | -11.25803 | -43.54971 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 25abdddf-145a-32ed-957a-50cfae66fb7a | -10.4877 | -39.52938 | 2026-09-29 15:46:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c772257d-7ae2-3009-9277-5256bfbe0e19 | -11.41008 | -43.41936 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| cd1d0eca-d4cc-3ecb-97e6-fa57d26935f4 | -9.87656 | -43.62282 | 2026-09-29 15:46:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d428dc0a-b860-3779-9acb-26ef1f12c45a | -11.81624 | -43.30698 | 2026-09-29 15:46:00 | NPP-375 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1a6ab4e0-cf3d-3a33-8cdc-3a017a4b4497 | -11.40607 | -43.44483 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 8977ce31-70d9-34c1-b29b-73f66fdfb412 | -14.58245 | -41.44672 | 2026-09-29 15:46:00 | NPP-375 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f11d72d7-807a-33b8-bca4-761351c94d79 | -13.97192 | -42.66407 | 2026-09-29 15:46:00 | NPP-375 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1a330553-37de-3a82-88f3-1da91623b46d | -11.28771 | -43.56495 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e1bf4b25-d137-3ca6-a2ea-9dda00d9f1bf | -10.94766 | -43.87936 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2801bd9a-4cc8-3226-a588-c479e26e53d4 | -10.29073 | -44.62949 | 2026-09-29 15:46:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5c1ad521-95e8-30bc-9e3b-56bc33cd30ad | -11.39707 | -43.42701 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 42afad1c-1087-3e6d-93b1-5f54d651a013 | -11.4267 | -43.43491 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| daab8412-ab8d-38b9-9b2c-0ab233cef89a | -11.28081 | -43.56581 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6999eab9-47f6-370a-8a72-8be2a8b8eb44 | -9.43745 | -41.81592 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 52bd7508-dc2d-36ad-925c-5c691a409aa0 | -12.43372 | -44.14239 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 13781395-d0ec-300d-bec3-2937bc4873c0 | -15.07224 | -41.94149 | 2026-09-29 15:46:00 | NPP-375 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 18a4c8c4-ea05-3361-b0b2-1e9ebfe6fb84 | -12.3365 | -40.30725 | 2026-09-29 15:46:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| db169ea6-edbd-3b69-88d1-c51d6c6e72d2 | -9.65485 | -40.35793 | 2026-09-29 15:46:00 | NPP-375 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7cb54bb1-68b4-3787-af0a-defe366e5f17 | -11.40752 | -43.45737 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 47f2a379-13ba-365b-981d-084bdbb9b217 | -11.68161 | -43.5325 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ba8b0594-a7da-3a09-986a-54486b5cceb8 | -11.44601 | -43.48382 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 99ecf01c-3acc-3559-9791-57303ca686a3 | -14.38688 | -40.94433 | 2026-09-29 15:46:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e2b1d15e-ec7f-3a92-9635-87d7b80f6d7a | -11.64353 | -43.50564 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| d15293ec-d066-3b4c-8872-87cfcb208322 | -13.3793 | -44.00721 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| b1b4144e-57ab-3fc8-b606-3a3c70c81c1b | -12.10337 | -40.22199 | 2026-09-29 15:46:00 | NPP-375 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f4497210-905f-3a37-8268-00f1311a19bc | -14.65463 | -41.82915 | 2026-09-29 15:46:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4bc6af59-9bd3-33cf-96d3-9751505148e3 | -12.32203 | -39.06553 | 2026-09-29 15:46:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2ad05e7e-a45f-352f-a630-4dbeaec836b2 | -13.32155 | -43.94029 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 1f187086-0c29-331e-ba14-7cbe67f4384d | -11.41912 | -43.43738 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f492a848-c8ff-38c8-85bf-0e01286b22c5 | -14.98665 | -41.48196 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 96af9985-5865-3338-97f9-607f6a377fcd | -11.40742 | -43.44945 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 8d7b42ef-eef6-38c9-a7ef-0b7bb4e37b9e | -14.9983 | -40.48017 | 2026-09-29 15:46:00 | NPP-375 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d91c2c89-4cb4-3cf7-b7e8-8e1f2969e6ed | -10.92541 | -42.31094 | 2026-09-29 15:46:00 | NPP-375 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| be060dcd-44ad-3f62-8dbc-da2043389e2d | -12.17352 | -38.59467 | 2026-09-29 15:46:00 | NPP-375 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7bd6617a-df25-355d-aae2-fa319b4fe341 | -11.39436 | -43.45732 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| f4fe1ee5-41bc-3aa7-b9db-b8496d58e722 | -11.45081 | -43.46417 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 783230a4-a4f8-30a4-876c-0c7c280b4301 | -14.97223 | -41.53111 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 45.6 |
| c3830b32-2a5d-3a40-8ead-4ffa336f4b2d | -11.29177 | -43.53923 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| dcffb0bf-fbf9-346e-8f14-c94cc44d0f40 | -12.43976 | -44.14302 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 233.1 |
| b7581447-39eb-302a-8821-2a047c213f0f | -10.86917 | -38.51251 | 2026-09-29 15:46:00 | NPP-375 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 213ef2b0-024b-3db3-89f1-3ba6aecc9934 | -11.71448 | -43.45116 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| a421cc3d-635c-345c-9fbe-42c7c1c15eea | -14.73916 | -40.93495 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 192.1 |
| 1c90c502-e8e1-3e5b-90b7-c9104a0b57bc | -11.28011 | -43.55963 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0cfe3775-ade2-30b0-af0a-3ebb46fc20b4 | -8.84199 | -41.12957 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 84f7b60d-2ff6-3a08-b603-fc30beb3ad5f | -11.41441 | -43.45675 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 4aec4aa3-d903-3e6d-b801-d8b58e3e24b0 | -12.67216 | -42.68204 | 2026-09-29 15:46:00 | NPP-375 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f0216d81-9b8c-351c-a904-86fdcb148250 | -14.60925 | -41.10457 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e8375b59-cebf-3c50-8290-99c433ec115e | -11.34763 | -41.27736 | 2026-09-29 15:46:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 7e6a023b-341e-3bcd-b745-41df4f2fd978 | -11.42739 | -43.44118 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ccb0653b-5b9e-3e25-8db1-ffa2f40b98fc | -11.4867 | -39.90882 | 2026-09-29 15:46:00 | NPP-375 | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6032c89b-be5f-35bd-a683-dc54809c7b2a | -14.67853 | -41.86954 | 2026-09-29 15:46:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 73d86ce5-9549-3002-bf7a-c395e033afc9 | -11.39919 | -43.44551 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 3d56f13d-0a63-3ee2-a08e-e13fb2d2237c | -13.32937 | -42.70152 | 2026-09-29 15:46:00 | NPP-375 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 0ac816cd-8887-30f3-a1aa-d9697a2a33e8 | -14.60751 | -40.80612 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 28b7121d-699b-35d1-bc57-7abce3192eee | -11.4108 | -43.42558 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 639b1c85-52d2-3c94-b9c0-54e38367b6ac | -11.39377 | -43.4589 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 3405acd2-1444-3569-b837-ef2e2c124a07 | -10.91019 | -43.86199 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ea95bdac-bd6a-3f35-9c8d-d889b4fc40b0 | -9.06808 | -45.01453 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 788fd9c9-0905-351d-8eaa-af84aa746e7b | -12.92038 | -40.04047 | 2026-09-29 15:46:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 9362dbda-46f9-33ef-9fdd-aba77dce4f2e | -13.33357 | -43.9395 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 11f6f5b7-99ef-3d51-9053-6ad87b7eaa43 | -11.6297 | -43.50707 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 91e6dca3-9bf7-3923-a827-9fe0f5a71bf2 | -12.44368 | -40.47246 | 2026-09-29 15:46:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 978fb425-d0cb-3fc5-a628-17aca323ef16 | -15.83709 | -42.56481 | 2026-09-29 15:46:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 9f488bd2-6034-3633-a4ab-c8e5f8518cf7 | -11.40811 | -43.45575 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| c9166a80-29cc-3f12-a9fa-44b2d8cdca8a | -13.97378 | -42.66427 | 2026-09-29 15:46:00 | NPP-375 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| e4909185-2c26-3555-b486-283721d76266 | -14.12712 | -43.91283 | 2026-09-29 15:46:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c9de4586-8193-332c-9f03-7a0f2408fee0 | -14.99099 | -41.48476 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| d0342059-e6e0-331d-b27f-97eb4093184b | -14.12639 | -43.90542 | 2026-09-29 15:46:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 226.2 |
| d01d822c-64ea-3291-8ff5-4f186e7b8139 | -14.74598 | -41.05329 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 27929972-23f4-364e-8a43-874a0329abf3 | -11.67468 | -43.5332 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f11da203-aedc-3602-b01e-16df43863d54 | -11.42347 | -43.47491 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 88b1f80c-1613-3a8e-9891-1544bb7c6deb | -10.94532 | -43.85931 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b0250d6a-e804-3dfb-8e35-4255d489c8f1 | -14.05883 | -40.57313 | 2026-09-29 15:46:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6a86e750-5bb9-3212-a8af-25f3b52f16fa | -10.21266 | -40.35628 | 2026-09-29 15:46:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2226500b-4825-3e0c-8023-67a3ba0cce67 | -10.29335 | -40.01771 | 2026-09-29 15:46:00 | NPP-375 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 40.3 |


[Clique aqui para ver as próximas entradas](README90.md)
