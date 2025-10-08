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
| 7159da1e-e350-3425-a04b-babd74f05321 | -17.14292 | -45.78638 | 2025-10-08 03:51:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 71aa9de1-0bcb-3dcc-bc81-719f4a9571a3 | -16.00153 | -50.82079 | 2025-10-08 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4320efc-a2a8-32f7-ac88-db7f0334cdcd | -18.40575 | -45.21048 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d57d0342-b1ee-325b-b3b8-6177da292c8b | -20.49813 | -45.95177 | 2025-10-08 03:51:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4e7b7ea-b36e-3277-8b98-599bb0999fab | -19.40091 | -44.38724 | 2025-10-08 03:51:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77183e93-f2f2-3ca3-8d37-916dde5cbf50 | -21.06745 | -46.89411 | 2025-10-08 03:51:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db0d95e5-5af2-3e91-94ed-6c5a797a2600 | -15.79774 | -46.24969 | 2025-10-08 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7f45211-d0e2-37d5-acd2-f8f5d920386e | -19.38947 | -44.38465 | 2025-10-08 03:51:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94ee8ad1-9dc8-3d4b-b037-528096bee682 | -21.03922 | -45.6749 | 2025-10-08 03:51:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e78fcf4-c9a5-3140-b71c-3614ab65599e | -20.17183 | -42.20477 | 2025-10-08 03:51:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 11669e9c-ed76-39f9-82cb-768d401f4ef9 | -18.02399 | -44.30981 | 2025-10-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ca45265-90b9-3131-8ea5-05123db477b9 | -19.7206 | -43.90702 | 2025-10-08 03:51:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c70c10f2-fb5c-30ab-a02c-4a837e7c11bc | -16.74618 | -42.5118 | 2025-10-08 03:51:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 670a68b2-c60d-33ad-89e0-7a69f7230b09 | -18.42205 | -45.21399 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab9f8068-a9df-3046-8e61-263131b71c0d | -21.12114 | -47.03723 | 2025-10-08 03:51:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2388cc92-a6be-3feb-8d78-595ac13c964a | -21.41501 | -49.67944 | 2025-10-08 03:51:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8c1fbb98-fd13-33d7-97ea-f7a56448caa5 | -17.97978 | -44.97433 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 37baff38-7cff-386c-9554-bdbb3a66a43e | -20.5031 | -45.9482 | 2025-10-08 03:51:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eac7e5a5-fb79-30f0-822d-2a6b0d378931 | -21.912 | -44.99915 | 2025-10-08 03:51:00 | NOAA-21 | CAXAMBU | MINAS GERAIS | Brasil | 3115508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2b76fbd8-1daf-3100-bfee-5ae537548b7a | -20.12396 | -44.42079 | 2025-10-08 03:51:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0c8f5094-dae9-351e-b58d-84578eb2b169 | -19.4526 | -44.18678 | 2025-10-08 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bcc2135-2942-3fb6-b1d1-2525d6d67009 | -20.20215 | -43.94636 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a9c2d52d-d06d-3f20-b9b2-d4ca837928c6 | -20.20418 | -43.95636 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 206eb318-26a2-3411-b774-b3c052df9274 | -18.3052 | -42.22677 | 2025-10-08 03:51:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1414a196-1ea2-3790-b4d9-35a589df7803 | -16.13239 | -47.91368 | 2025-10-08 03:51:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| db6ce2f6-d9cc-3cdb-beb6-16bf433ace91 | -15.36639 | -47.2968 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 81bb484b-0b72-377e-affc-de7acb42c3d9 | -20.39099 | -43.06655 | 2025-10-08 03:51:00 | NOAA-21 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9324930b-7274-3fc1-91fb-6571a4b787e6 | -19.26577 | -44.11719 | 2025-10-08 03:51:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3c34e28-0a69-3ae5-999f-ed76634662eb | -16.00056 | -50.82526 | 2025-10-08 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7de51ff9-82ae-369d-bc21-3329e3c6abd5 | -19.90988 | -43.64267 | 2025-10-08 03:51:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 20e5a333-5827-372d-b709-aa59a78d4e4a | -16.13109 | -47.90984 | 2025-10-08 03:51:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b9018df-5642-3e6e-b510-3d657fbd1144 | -18.0085 | -44.30632 | 2025-10-08 03:51:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a6c20190-6b0a-3c01-a5dd-e8dbc7c3d704 | -15.86388 | -44.83159 | 2025-10-08 03:51:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a44125f3-364b-3fc6-b7a2-63db89bd24b4 | -18.06318 | -44.47202 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7340bd4f-2cb4-3835-96ca-92a540d0c0f8 | -18.405 | -45.21439 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f28a7a3e-3a87-36c3-890a-6495e53ec40b | -19.51437 | -44.08119 | 2025-10-08 03:51:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4d0435e8-2175-35c8-97fb-30fa0375fb76 | -19.29678 | -44.4559 | 2025-10-08 03:51:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbfc365b-1ae2-3740-aa92-8ae8e9cbd410 | -17.6377 | -44.09925 | 2025-10-08 03:51:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1099eee4-1907-3b41-bacd-05480813cbfd | -21.4156 | -45.12476 | 2025-10-08 03:51:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bb81b9ef-638d-3edd-842a-81a66990520d | -20.50396 | -45.94371 | 2025-10-08 03:51:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 282f8a3d-2626-3084-a8f6-ce81606fe794 | -15.19602 | -49.76105 | 2025-10-08 03:51:00 | NOAA-21 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79fabca3-e27f-340b-9ad4-d365106329c3 | -17.29112 | -42.645 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 69771041-eaf1-3367-83d0-04384297a653 | -15.79388 | -46.24507 | 2025-10-08 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f75a8cd-37c0-3a71-86e9-05672634dab6 | -20.86578 | -45.2064 | 2025-10-08 03:51:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 017be00d-f34b-3473-8488-6b45e715c3f9 | -20.06865 | -42.14856 | 2025-10-08 03:51:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2a416688-53d4-3e3a-beb7-8144a7ca3de2 | -22.34088 | -49.87758 | 2025-10-08 03:51:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 048e2abc-164b-3420-b678-ab9b1a561b06 | -22.3854 | -49.98005 | 2025-10-08 03:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bb253236-b093-3cb9-95c1-fe2df7c06e2f | -18.87636 | -44.1577 | 2025-10-08 03:51:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff1b0368-3805-3a4b-b5d7-9564a612f809 | -15.7938 | -46.24715 | 2025-10-08 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd1d6ac9-2c78-3d46-bf9e-bd2a510bb1d7 | -21.09672 | -44.20706 | 2025-10-08 03:51:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| be9ad229-a126-3c61-8d4b-65ed025b465c | -19.51988 | -44.07225 | 2025-10-08 03:51:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8e39d37-48a1-3b6e-8e52-b4b0cfe18558 | -15.38996 | -46.27478 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 130dae13-f6b6-3518-a154-bb9c611d57f8 | -21.3918 | -45.54929 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a040411a-5337-3a88-bda0-242f75b13d5e | -15.06541 | -49.49095 | 2025-10-08 03:51:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc53fa46-916f-37d7-a3ff-c233df9e56b8 | -22.30427 | -49.92307 | 2025-10-08 03:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 346e8eee-ecd7-3f9e-999d-ff3da2ca7c03 | -18.49732 | -42.90051 | 2025-10-08 03:51:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 6c7aff05-9b31-3d9a-aab2-a6941455f6e7 | -15.38678 | -48.03199 | 2025-10-08 03:51:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a897c015-1950-3c6f-a51b-06b492d078d8 | -19.87543 | -44.30514 | 2025-10-08 03:51:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e5b3c71-cad2-3299-8238-1921af4db97e | -19.3051 | -43.76527 | 2025-10-08 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b4261d1-fd41-388e-a447-44566d5c8064 | -19.46945 | -43.89632 | 2025-10-08 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 82476061-e11b-3c88-bc63-0446f584000f | -15.37207 | -47.29879 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 083d255d-3455-3974-8ad7-2deced327400 | -21.3021 | -45.45343 | 2025-10-08 03:51:00 | NOAA-21 | SANTANA DA VARGEM | MINAS GERAIS | Brasil | 3158300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a5534f15-3b9c-33cf-8f2b-4eb95d8edf72 | -20.38094 | -44.44684 | 2025-10-08 03:51:00 | NOAA-21 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1708cba6-503c-363d-aa98-45d615dbe6b2 | -17.81962 | -45.3207 | 2025-10-08 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05f4cecc-952b-39db-9d03-271b1fced87b | -19.5115 | -44.07554 | 2025-10-08 03:51:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5e5a4b7a-7fe9-3a00-b034-1fb0610ab157 | -16.93745 | -40.29462 | 2025-10-08 03:51:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7abf9f12-69a7-3090-8eb5-8b410eae1301 | -19.40005 | -44.39203 | 2025-10-08 03:51:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdf0f04e-2a8d-3a3e-89f8-8f22576cb557 | -19.517 | -44.06668 | 2025-10-08 03:51:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97cbdb77-8a40-3160-bfd1-0d1c04326c07 | -16.13872 | -48.24208 | 2025-10-08 03:51:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbc98374-f131-3de3-8230-614a34cc39e3 | -20.31214 | -43.47643 | 2025-10-08 03:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eab93c94-18cb-38a8-ae5e-3852b1ab2591 | -17.13248 | -43.46431 | 2025-10-08 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19ec8974-f755-3a28-9741-1851a0d7289f | -18.44929 | -42.91105 | 2025-10-08 03:51:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| b1301574-53f0-30ff-9232-39cf55991681 | -17.1492 | -43.45773 | 2025-10-08 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 777fc3d8-0152-331a-80ff-46d9378936eb | -18.13229 | -40.25439 | 2025-10-08 03:51:00 | NOAA-21 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e4d275c7-48fe-3484-8bf9-bbbd7bc4d2fd | -21.41431 | -49.68272 | 2025-10-08 03:51:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| edb9940e-ba91-37d6-84ec-17846f2095a5 | -15.38099 | -47.30561 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c424f7d9-fa91-3d93-baf6-e57bf9a9bd80 | -17.96626 | -44.97915 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 424bbbb4-951d-3ce3-9703-3c11e8e4359e | -20.58353 | -46.34839 | 2025-10-08 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f848bfe-a420-3836-9b23-bc6076498113 | -17.14209 | -45.79078 | 2025-10-08 03:51:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5a738f0b-337d-3dd0-972b-5ab58e1282f7 | -17.14082 | -43.46115 | 2025-10-08 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f251d333-0372-3e97-ab19-8e66df338acf | -20.16985 | -42.21648 | 2025-10-08 03:51:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| da4f1948-3105-314f-a232-d2632796b207 | -20.08618 | -44.3273 | 2025-10-08 03:51:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b7bf290b-0f1e-313f-a03f-02fdc205a2c3 | -17.35867 | -45.05885 | 2025-10-08 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afc53773-39d5-3f00-96bd-2c8c66708b12 | -15.36704 | -47.29819 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2779889c-0a27-34c2-9088-10807c71af9e | -18.00931 | -44.9729 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69558c53-b713-3ae7-ac3f-13d7cc87664d | -15.39025 | -47.30624 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfa38ac8-fd66-3156-96be-3e1f125489e0 | -17.13862 | -45.78531 | 2025-10-08 03:51:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 298fd81f-31b6-3abc-8efc-a8ab607879fc | -17.58151 | -42.24568 | 2025-10-08 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c1c1823d-9fd1-3f81-8405-782db29ece67 | -21.41942 | -49.68394 | 2025-10-08 03:51:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| dde9ff87-64e9-381e-9ade-ed985a6c1d63 | -22.11016 | -45.24843 | 2025-10-08 03:51:00 | NOAA-21 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c57ce513-a8d1-3ab3-976d-6eb36f9dd029 | -18.05931 | -44.47091 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| d53d1a1b-f5d9-3098-9287-e4d2e6135c50 | -21.84633 | -45.3778 | 2025-10-08 03:51:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a78dbf73-e056-312f-a53f-550f392d031e | -19.26955 | -44.11794 | 2025-10-08 03:51:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7391d3f-9910-353d-8709-9f5efac796ac | -21.3005 | -45.45483 | 2025-10-08 03:51:00 | NOAA-21 | SANTANA DA VARGEM | MINAS GERAIS | Brasil | 3158300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e0341d63-1dc3-3182-87f6-801b247f14a8 | -19.4488 | -44.18613 | 2025-10-08 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b75f669b-6918-372c-8641-2baa457b20a6 | -16.88758 | -46.95966 | 2025-10-08 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 90551de6-4596-38d2-93be-ab7d9e08ead9 | -18.06919 | -44.46129 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d90b80d-4c5d-37d2-b5bf-1791ca507f54 | -17.56241 | -46.06768 | 2025-10-08 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbdc94ad-bba0-3f7b-8298-e40b7e5ec711 | -15.70255 | -47.51433 | 2025-10-08 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 36056da5-9841-3d02-b8d2-553d3eeea8b2 | -21.9578 | -44.66212 | 2025-10-08 03:51:00 | NOAA-21 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README28.md)
