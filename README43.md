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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e62aa70-0953-379f-a9ad-6687b1ec926d | -17.89436 | -57.50594 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| b0a4a41c-9399-3316-a164-1c77341038e7 | -15.09025 | -46.62181 | 2025-10-10 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 183fab4f-e011-3302-99a0-e03ed700a301 | -13.83806 | -45.88284 | 2025-10-10 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9087486e-635d-3515-9ef6-15ce9e06b985 | -15.24135 | -46.37613 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e90f2cd7-4f43-33ea-9c79-cbb39d69557c | -15.46416 | -48.53764 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed900dd4-f506-3f26-a6e4-a3ea2b1f180b | -14.26785 | -45.91232 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 269b4c9c-4086-3ac6-8bdf-e0bf3119c70e | -17.89973 | -57.49503 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a8f5cca8-cb2a-3f28-82b2-2d79fa398b75 | -17.20829 | -47.65473 | 2025-10-10 04:53:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 226062b2-bfe0-363f-90c5-e3bff1506721 | -17.66013 | -44.44958 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8167796-d2ea-39b7-aae7-68b2142e990a | -16.54378 | -48.89161 | 2025-10-10 04:53:00 | NOAA-21 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0befe31-8622-3a97-aa80-1c4fddcc718e | -15.43028 | -47.98734 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a244975e-fa22-399b-b79e-e6887a3c548e | -13.2973 | -47.13268 | 2025-10-10 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 806397c4-2bcc-359c-a4c3-20c0a27f0417 | -18.4196 | -45.23766 | 2025-10-10 04:53:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b1c98ab-fc5c-39fb-a9e8-5d60c3f6fc72 | -17.93346 | -45.01058 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c5797a7f-1023-38ed-9052-887d6b18fcfa | -14.85603 | -48.44854 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68fea720-efe3-32d7-824c-a4a513175b5f | -15.09495 | -46.58226 | 2025-10-10 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d641e7a-c006-3784-88fe-3cea673dc378 | -15.28304 | -46.15284 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87a3d908-4c50-3e45-b513-e769fa86fffa | -17.83396 | -57.65346 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1a741b65-cd76-3236-b004-9fe104e6b5f4 | -14.72851 | -48.36278 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 613f1981-95de-3cf7-95da-69105aef27f8 | -11.75986 | -61.06537 | 2025-10-10 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27027fd7-d67d-3d65-9966-547956fcfaef | -18.77915 | -44.6173 | 2025-10-10 04:53:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 54424f43-9779-3893-b087-baf54f52b9ab | -13.30239 | -47.12941 | 2025-10-10 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 498b3b04-c235-3577-a0fb-0cc019d3c88c | -13.31744 | -48.47665 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be80cd5f-31d2-3900-a3ab-9660fb39ea4b | -15.97111 | -59.53589 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| af3236c2-200f-3a50-84cb-7867d3c24afe | -14.93047 | -46.77528 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 041ec4c3-ef17-3e9b-aaab-de8ee920a080 | -13.26778 | -48.03465 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9125d63f-7115-3a20-9eda-5373903aff22 | -16.05407 | -48.06977 | 2025-10-10 04:53:00 | NOAA-21 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97768744-2b0f-35bd-9b20-6bd6c9ff30a8 | -17.84464 | -57.59046 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7fb7261b-0292-3905-8665-b09926060751 | -18.10518 | -53.34513 | 2025-10-10 04:53:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3d7929d-6bf3-3cb1-b474-f944fb09c9a4 | -17.82348 | -57.63129 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f2525d68-686d-39c4-abc1-f5979193f911 | -14.3896 | -45.99811 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8703e2cb-a814-3fbe-9ed9-30f56013d49a | -15.75614 | -48.98921 | 2025-10-10 04:53:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 536896a7-c1f7-38cd-9ae4-5dd59982f73b | -14.37925 | -46.00271 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38a4970c-b7f2-33af-8aab-f1f94b4dd1c5 | -17.90906 | -57.52383 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 89ea91e8-062f-3777-9cdc-38698bd10c5c | -15.30412 | -46.14778 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fd5bf10-b83c-3a75-87ab-ed25d7420102 | -14.93304 | -46.7587 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d45b370-cdf8-390f-9c17-be68372decac | -17.22689 | -52.81352 | 2025-10-10 04:53:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a8ec8502-6ce8-3577-9153-37f3d6484d0a | -13.29851 | -48.4903 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1026e3c-c50b-3c94-8eb1-76d0ae84deba | -17.8484 | -57.65224 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2141db6a-4f45-37b1-b413-49342fe1541b | -14.94588 | -46.7691 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bfc6fa92-4718-3377-977c-799f97af93de | -14.93237 | -46.7591 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c16eb9fb-1aef-3d17-8df6-1cbe0771f8b0 | -13.26648 | -48.02773 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ccef5ab-3721-3896-b7ee-0dc37a69834c | -14.38927 | -46.00102 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6440ae49-029f-308a-bc9d-4551587e27dd | -17.8154 | -57.65789 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 85e1c05d-e352-3dc0-a4ce-f4adfdf52174 | -11.16467 | -61.31019 | 2025-10-10 04:53:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fde935c0-cce3-320a-8b21-53902c961eff | -15.06681 | -46.61073 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d37b268-cb4a-3840-9283-b5d9ef628380 | -16.26788 | -47.16124 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db9b3665-5ab4-3825-b800-d5227a6f3b4e | -13.30263 | -48.00316 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 01f5ca64-50cd-3216-be93-994b2a2fbb2e | -14.84496 | -48.46687 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01c17953-fe9c-3566-bd1c-00fe399b6c9e | -18.07192 | -57.53724 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 67bf1ad7-2096-31d3-8799-df4ce38c7695 | -17.88848 | -57.66796 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9939ded1-9b3a-3c60-800a-e73e57bef003 | -17.94219 | -57.61638 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9cf894a3-2674-3cf9-9497-bd46d3162aad | -18.0306 | -57.55468 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| de2c1147-fc6f-39d6-84e4-957fdd6d49ff | -17.8954 | -57.6692 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| af4ff338-b8a0-3477-8149-16c07025726e | -17.93462 | -57.61909 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4bc8dd82-f688-3092-9257-7c8c0bbc12d9 | -17.92128 | -57.62067 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 17d26b4c-5c93-3159-a247-795b70d36b69 | -17.9043 | -57.65854 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 31e128a7-d531-379a-802b-851f4b68c943 | -21.72748 | -52.41751 | 2025-10-10 04:55:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9719febd-2a5a-35e3-aace-8d77935efe58 | -18.03403 | -57.5554 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| dfb615ea-bb51-3778-8aa2-0ecaf41776e9 | -18.04673 | -57.52156 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f5165ccb-0111-3239-a943-1a70c34df5b9 | -17.89606 | -57.66523 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 50e3ce69-d031-307b-aa56-49679dc128a5 | -18.04251 | -57.5645 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 85fc4313-1660-3d4e-8583-8db22509dadc | -17.89327 | -57.66062 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 89c1aabd-3e10-3f4c-94e0-72efd446226d | -18.04091 | -57.55657 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a4fc0d09-20ba-34c0-9d51-ce845c82caf0 | -17.89261 | -57.6646 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f334ae98-5664-36d9-9d0b-7358bca3af1b | -17.89194 | -57.66859 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 81d8c088-de4c-3838-8aac-821b83193fae | -17.96008 | -57.61562 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4823d2ea-98ec-342c-8a25-857f5f74ed4b | -17.8974 | -57.65726 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 70f5f5ab-f23a-36d0-aa86-b1a227f16fa0 | -18.07333 | -57.54985 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b3cb95f2-d09c-3c2d-8910-b59addfacf5d | -18.06105 | -57.55962 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2d42ec63-8a5f-3df0-9f7e-8a63bd225700 | -18.07049 | -57.52481 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bd67cf05-fcfe-3485-85ef-b8523af4eeb4 | -18.06652 | -57.54826 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ab731359-e381-3c77-8d5f-60840e1f778c | -18.03978 | -57.55974 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ffd51257-9f36-366a-ab95-0ef512dd8a05 | -18.03954 | -57.56489 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 69f9f11a-4c9f-3552-8b95-68efda502194 | -21.72379 | -52.41691 | 2025-10-10 04:55:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e75acfc3-1da5-3155-a78b-99e56cdfe419 | -18.07265 | -57.55382 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f4a994ad-dd84-33f4-a29d-efb7a79d78cf | -17.92363 | -57.62105 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3e24f4b1-961f-35ff-803a-88f84422ec4e | -18.01227 | -57.49502 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0d22f774-0806-3fe5-9976-6aa9b312c855 | -18.06854 | -57.53638 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 16705c26-9414-3606-849c-9b94ef5dfe91 | -18.06857 | -57.55707 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3cc6247e-9007-3407-abf1-61c8f082c1d9 | -17.89885 | -57.66986 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a8c7a562-0e32-34b2-8324-12368155b41d | -18.03745 | -57.55607 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 942f3db5-7820-3615-9cc3-ca33a897b139 | -17.89951 | -57.66589 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 130414b5-f329-32f1-8178-2cc829e7daca | -18.04051 | -57.55551 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| abf0d247-9c07-3453-b412-034cd52b302a | -18.04021 | -57.5608 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a119797b-7950-3f80-b7c7-aee8f9785d4b | -18.05764 | -57.55886 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 16c4ac72-97a2-340d-ac9d-66e4f8ad09f4 | -17.95664 | -57.61497 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 66e1795a-b58b-3996-8641-af6ef7a15442 | -17.90775 | -57.65921 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 932305ad-c474-3848-a87c-fb781d74a43d | -21.58225 | -53.81237 | 2025-10-10 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf11d057-5a6e-3807-99d9-5ccc3247e1e7 | -18.07326 | -57.52935 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 540a14cf-8a18-3df9-807f-b6c2b3ffcc88 | -17.90363 | -57.66254 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5de1f924-05cf-3f9c-80d3-240916767594 | -18.0638 | -57.54343 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 69e7700f-8667-31ad-9a37-e48957eeae79 | -18.03335 | -57.5595 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a9086a2b-d135-3250-9dfe-3d5c3c9d83de | -18.06992 | -57.5491 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 932109b9-a26c-3f2c-b554-c8e5522af96a | -18.06925 | -57.55305 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 460817ec-ef2f-36f6-a6cb-2630de9211e9 | -18.02992 | -57.55882 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3ad065d4-6e1e-3dda-ba77-dea8fd2c3ab1 | -17.88982 | -57.66001 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 99c6a5fd-1907-3e2a-9456-e2133d8b0043 | -17.93655 | -57.54533 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 071268c0-72a6-3f1d-bd67-63df062db892 | -18.99705 | -52.59381 | 2025-10-10 04:55:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ab0699a-f917-3d44-8b89-290526dd3aa0 | -17.88915 | -57.66398 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README44.md)
