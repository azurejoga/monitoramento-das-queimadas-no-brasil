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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c81d57d-934d-3b2c-8497-080ef6882648 | -19.91212 | -47.96025 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 79b64199-fee2-3c35-b138-17396d793c57 | -19.37211 | -43.43715 | 2026-08-31 16:45:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f1e98f7-2264-3eff-9acb-0ebe42a0ea01 | -20.16043 | -42.1763 | 2026-08-31 16:45:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 0af5312b-b791-30a2-b4fb-563615dc7960 | -20.95441 | -42.60928 | 2026-08-31 16:45:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0e2f3f26-8c97-373c-aa50-f7727decd3a8 | -20.28852 | -47.8335 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 37279142-acb2-3cd7-b8f5-f2f194350b86 | -19.85354 | -47.91723 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b955add6-6646-35a6-bbbe-c5b130442105 | -19.8204 | -47.92972 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 152b5bb8-161f-3109-a165-1dfaf707cc8b | -20.83104 | -43.0725 | 2026-08-31 16:45:00 | NOAA-20 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 7d64a015-0eaa-3cab-b7e1-a43012a68ab8 | -19.58323 | -40.51513 | 2026-08-31 16:45:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e5cf7776-4502-3d25-8413-474538742e65 | -21.20846 | -44.20552 | 2026-08-31 16:45:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5b036c91-5fb0-3ae0-96c3-c7a1e36ec0c5 | -19.31922 | -40.35709 | 2026-08-31 16:45:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9e68eff5-2a22-3615-ab3a-7e891eb128a0 | -20.70436 | -41.82272 | 2026-08-31 16:45:00 | NOAA-20 | DORES DO RIO PRETO | ESPÍRITO SANTO | Brasil | 3202009 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| fb013f96-99b7-37f6-b19d-8fab036b11c7 | -19.26267 | -40.16942 | 2026-08-31 16:45:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 3a44d750-6db2-3b5b-9e5a-094b1faad56a | -20.65191 | -47.24841 | 2026-08-31 16:45:00 | NOAA-20 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ec36dab9-14fc-31ca-857f-568793aa0b01 | -20.88853 | -44.63136 | 2026-08-31 16:45:00 | NOAA-20 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| b92707be-8438-32cb-a605-2a2429088512 | -20.29194 | -47.83295 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c4454d6d-3545-33d5-ac4d-c4faea6d48ed | -19.85067 | -47.92166 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c797470f-9a0a-313b-ba78-4caacc616b3a | -19.83808 | -47.93159 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0b3bfe6a-ab0b-3783-b608-ba657a49fc89 | -19.82781 | -47.93258 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 545837b0-f27f-3f0e-9930-232efdef8906 | -19.84327 | -47.91879 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| cb090f49-276b-3b3c-a6f9-6da7ac593a3d | -20.00282 | -44.08059 | 2026-08-31 16:45:00 | NOAA-20 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c1c942f8-ca57-3f27-8517-709933277d8c | -20.00273 | -44.07995 | 2026-08-31 16:45:00 | NOAA-20 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a58ce1f1-9bd6-3395-b936-8ffe7957dd16 | -20.81984 | -44.84013 | 2026-08-31 16:45:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| da443d9a-1a86-3c4a-a908-e58967f13a02 | -21.32509 | -45.93375 | 2026-08-31 16:45:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 0140b0a3-fb60-3fd9-877c-ff74e2a6146f | -19.82724 | -47.92863 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9fd38d8a-e570-3756-beaa-dc5239624aac | -22.08309 | -55.71617 | 2026-08-31 16:45:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b51c9e5a-1c17-3a7d-bfb2-099ee81bf5db | -20.75201 | -49.72059 | 2026-08-31 16:45:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 82f2c3f2-aee9-3393-a987-164c56555e80 | -19.88996 | -47.43776 | 2026-08-31 16:45:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6cded12e-528e-3d41-8e2b-dc7454e48cf6 | -21.22431 | -44.12392 | 2026-08-31 16:45:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 36d9c90c-07b0-3547-8007-2f6554f44751 | -20.31247 | -47.82964 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 133.5 |
| dbd237c9-8d66-3966-b950-40092c5431b8 | -19.83179 | -47.93662 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7ada2b31-9113-32e1-bbee-09096c45a542 | -19.82759 | -46.30078 | 2026-08-31 16:45:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e242f12f-9c9a-3698-b096-bfe8818409df | -19.85011 | -47.91775 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 4a605ea4-477c-38b2-aadc-96d398f400f8 | -20.29536 | -47.8324 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5d6ef898-0db9-3e33-9494-27d74ab4caf5 | -19.80231 | -48.07332 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30fcaddf-8142-3321-b3c8-5929eb858649 | -19.82607 | -47.94488 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7da143bc-dfda-3545-809e-1ae98ac6b26a | -19.84382 | -47.9227 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 66450e90-13bf-3e49-9d32-c0e6a719d5bc | -20.29878 | -47.83184 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ccb3aca8-caf0-3167-9902-4743147b83ac | -19.82461 | -43.40992 | 2026-08-31 16:45:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e3c14936-9fc2-3082-84ed-28ed2de10172 | -19.84095 | -47.92713 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 36.0 |
| b3f25dc9-90fe-3950-accb-6b3005365d86 | -20.34316 | -47.10027 | 2026-08-31 16:45:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa1ee41b-cc69-33b4-9276-c926116353fc | -20.64799 | -47.24516 | 2026-08-31 16:45:00 | NOAA-20 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 1aa8e232-f0f8-3a14-b5cb-21894dac1f7a | -19.61932 | -40.78124 | 2026-08-31 16:45:00 | NOAA-20 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 444f18ab-dfef-3e6e-bfde-df0b84e0eab3 | -20.82044 | -44.84387 | 2026-08-31 16:45:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 8c2ebd2a-9fee-3fa3-949d-545496db890b | -20.30562 | -47.83073 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 393c9838-7442-359f-b45e-09cd6349eee5 | -20.24745 | -40.7534 | 2026-08-31 16:45:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8c80e902-77b6-34e5-87ba-992376391bd8 | -18.73789 | -41.50875 | 2026-08-31 16:45:00 | NOAA-20 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 7f5e7f91-bd5a-32b7-bbb7-b7a30e269b4f | -20.42582 | -41.52095 | 2026-08-31 16:45:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| be90e67e-50b5-363e-87e2-f11e8a1ee3b6 | -20.7407 | -41.7817 | 2026-08-31 16:45:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| edf43371-4685-3c19-b905-e05fdcab12e1 | -21.32453 | -45.93005 | 2026-08-31 16:45:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 4678c6af-83cb-37cf-9c9c-6cb57aacda31 | -20.30276 | -47.83521 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b020ab6c-af89-3e2a-8ca2-4d95253cbdc1 | -20.31191 | -47.8257 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 4b59ffaa-d05f-3d3b-9241-b2318fd3f600 | -20.41574 | -42.1955 | 2026-08-31 16:45:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| dc46e140-74fd-3fe6-bb96-6974b864bae9 | -19.84779 | -47.92609 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9433adab-4765-3f7c-9e59-826ad70a08c0 | -21.20553 | -44.11531 | 2026-08-31 16:45:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ca4fd5d-b495-3192-a124-83e74b3d3c4c | -20.83385 | -43.06777 | 2026-08-31 16:45:00 | NOAA-20 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ddb722a8-e329-328f-9df9-427870745a88 | -24.24921 | -52.23692 | 2026-08-31 16:45:00 | NOAA-20 | LUIZIANA | PARANÁ | Brasil | 4113734 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d439f217-f7be-3371-a2cc-7324ea6775f8 | -22.12396 | -44.81937 | 2026-08-31 16:45:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 75b8bc4b-6726-3066-85ac-22bc1619aeaa | -21.96568 | -51.45762 | 2026-08-31 16:45:00 | NOAA-20 | ALFREDO MARCONDES | SÃO PAULO | Brasil | 3500808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 35a9169d-2f7a-382c-8841-32b019602d40 | -20.02378 | -44.20757 | 2026-08-31 16:45:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 56555f80-ee01-3c5e-8474-4c99d3b5eb17 | -18.52688 | -40.26732 | 2026-08-31 16:45:00 | NOAA-20 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a530f057-34fc-32d7-9f8e-1030e4059310 | -21.00133 | -40.87915 | 2026-08-31 16:45:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9428480f-772c-3d6d-8f5b-331655e5b6be | -19.75332 | -44.77362 | 2026-08-31 16:45:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 00cf54b1-f50e-3c8b-8695-83f0e61b1875 | -21.17839 | -46.58805 | 2026-08-31 16:45:00 | NOAA-20 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e7cff27a-6df3-342d-8dc6-8c3c2940ef42 | -19.735 | -46.47488 | 2026-08-31 16:45:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14d45a3d-a96b-37bf-8b92-f291d2efe49a | -20.82377 | -44.84328 | 2026-08-31 16:45:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 9aa4c637-9bc3-3456-b94f-586f6f0fa66d | -19.59196 | -46.53682 | 2026-08-31 16:45:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| befc3094-b055-3057-9f0c-70906ee28607 | -20.02348 | -44.20832 | 2026-08-31 16:45:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c93f95de-7461-37fc-bc72-2532ddca07e6 | -19.83234 | -47.94055 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5f595d2a-b844-3b08-9f14-cef59e445e2f | -19.9087 | -47.96078 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53c0e83d-ee5b-3246-b0a4-746dfa288283 | -20.2996 | -40.85968 | 2026-08-31 16:45:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6ef0b7fe-7c7b-3b98-b168-3192dea25f3a | -19.83753 | -47.92765 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 4a33ff02-5197-33f9-8f1f-fd0d2236b9f6 | -19.85409 | -47.92113 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 14c47e75-2adf-3614-ac27-8b2be4d58b62 | -20.30905 | -47.83018 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d43c3960-c7ce-3344-a008-cc99c9440e04 | -20.30674 | -47.83859 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 0cdc6154-f312-32ec-a3e2-9aa86b7abc7c | -19.82439 | -47.93312 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 29edf4c4-1265-3456-9af5-df6bdd91dff8 | -23.01652 | -51.82431 | 2026-08-31 16:45:00 | NOAA-20 | SANTA FÉ | PARANÁ | Brasil | 4123402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2ca9a00f-3870-32a0-928d-8f1212f81708 | -20.34461 | -46.5607 | 2026-08-31 16:45:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a78a5ccd-d2f4-3c61-a523-0ca302906102 | -20.82437 | -42.75674 | 2026-08-31 16:45:00 | NOAA-20 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3fe390eb-a46f-327c-bda9-c4098c49424d | -19.98387 | -43.96402 | 2026-08-31 16:45:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 03a4a818-0018-38b1-a4f0-3c2e9f76be35 | -20.92944 | -42.14701 | 2026-08-31 16:45:00 | NOAA-20 | TOMBOS | MINAS GERAIS | Brasil | 3169208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fe9f1e04-5294-3346-b550-295eced522a4 | -19.97982 | -43.9607 | 2026-08-31 16:45:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| cc370fe1-51de-3dfb-84d7-d50bba7d423e | -19.83068 | -47.92871 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 0f3c6c75-6ecc-3785-85fb-ea2543e5e2da | -21.21857 | -48.14581 | 2026-08-31 16:45:00 | NOAA-20 | BARRINHA | SÃO PAULO | Brasil | 3505609 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f1a049a-6f86-3a7e-933e-ec36f6d0a030 | -18.99319 | -40.72729 | 2026-08-31 16:45:00 | NOAA-20 | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 081a6252-b5a8-3f58-9cc8-cc75782d6986 | -19.81867 | -47.94204 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b8516fc7-b966-3642-bfcd-e958cbd8f0ef | -21.4096 | -43.14663 | 2026-08-31 16:45:00 | NOAA-20 | RIO NOVO | MINAS GERAIS | Brasil | 3155405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e185c101-69e1-32a3-b582-e073fd3176b6 | -19.82382 | -47.92918 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a09066f4-f169-39cc-acb8-4d3cb221ac21 | -19.83124 | -47.93267 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a208b520-6427-37b6-abc2-9f99e0ebfbcf | -21.94097 | -45.01698 | 2026-08-31 16:45:00 | NOAA-20 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| eeded939-0f34-31bb-9a8b-2dc8f720cbd2 | -20.29249 | -47.83684 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 66e9fe49-0750-3084-a724-ecb7b1e491d2 | -19.85518 | -47.92891 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 8b690d3f-714b-3182-b53b-9922348becae | -19.36932 | -43.44198 | 2026-08-31 16:45:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e339cbd4-832c-3f3a-994a-c170f6c9f62b | -20.70587 | -41.82317 | 2026-08-31 16:45:00 | NOAA-20 | DORES DO RIO PRETO | ESPÍRITO SANTO | Brasil | 3202009 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7d71c09a-b511-3ec2-992a-31fce1d850a3 | -18.77152 | -40.20079 | 2026-08-31 16:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 41e5acd4-ed59-37ec-baa3-5078716f9720 | -18.74623 | -40.55113 | 2026-08-31 16:45:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 279435eb-c0eb-3be4-b4a8-dd5607c6779a | -19.85464 | -47.92502 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 98d3e56a-1cba-30d8-b70f-fbebf637a136 | -14.23266 | -42.40557 | 2026-08-31 16:48:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| f16ba950-e2b3-33ce-ad90-8cf29d6c8a09 | -15.89256 | -56.47499 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 637e5f27-b0e7-3976-bad9-1bb37e351fc8 | -14.50418 | -40.33466 | 2026-08-31 16:48:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |


[Clique aqui para ver as próximas entradas](README137.md)
