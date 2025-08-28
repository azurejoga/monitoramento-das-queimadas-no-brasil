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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3533c7a6-0d7a-3612-af72-4d9e4346a2b6 | -8.2705 | -45.1605 | 2025-08-28 05:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a33ea80c-a287-35ed-a6aa-4356aa552f20 | -14.2568 | -53.0679 | 2025-08-28 05:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 4be5d1ec-5099-31e7-b87f-90a226e49387 | -10.786 | -60.7848 | 2025-08-28 05:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1d556360-8bb0-3fb6-ac62-bd4acff55a74 | -9.134 | -65.7694 | 2025-08-28 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 164.9 |
| aedd1090-dd78-3c94-84d1-fc3b8380d575 | -6.8774 | -43.5919 | 2025-08-28 05:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| ecdbda62-9dad-343c-bf0a-a83f7830a08a | -6.896 | -43.6135 | 2025-08-28 05:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 14211015-1f8b-39e4-b1ef-997987f92bfd | -10.8049 | -60.7644 | 2025-08-28 05:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 490.9 |
| fa8dcfc7-a085-3fd0-9171-e5d9fe20ffa0 | -14.2761 | -53.0655 | 2025-08-28 05:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 237.0 |
| b3451a38-78c7-314f-b28f-d3ba07e2063c | -10.4736 | -57.9563 | 2025-08-28 05:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a5fe3e6f-5f7d-36fe-857f-652bbb652a5f | -9.1155 | -65.7699 | 2025-08-28 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 215.4 |
| 834a3fc3-b2fd-393f-a075-97e617f0bd52 | -14.2765 | -53.0444 | 2025-08-28 05:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| e072c55b-43a1-3a1b-ab17-261a456da5d5 | -10.8236 | -60.7633 | 2025-08-28 05:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 9108e925-5f13-391c-a6bc-a888431ea35c | -17.75652 | -44.48735 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bcebd581-2873-3003-89b8-209f314c1724 | -14.76522 | -59.74222 | 2025-08-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 822f3a33-b64e-30a2-9f44-920087a2333f | -16.9576 | -53.5188 | 2025-08-28 05:01:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6747fa8f-abf8-38db-98a0-ec64f0007538 | -19.91475 | -43.72274 | 2025-08-28 05:01:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 71a7312b-755e-3fac-a441-e07736521428 | -17.54789 | -46.6286 | 2025-08-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9679df88-f5d5-3a6e-8041-9913cba896d7 | -19.11593 | -44.02411 | 2025-08-28 05:01:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08fa1be1-e90b-3ab6-90e1-38691095d4f9 | -14.77924 | -59.72623 | 2025-08-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e58a243c-8a9a-3513-9f36-75752ade677d | -21.90696 | -48.51588 | 2025-08-28 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dc873fd-af2d-352c-93d9-ad48061ade7b | -17.77686 | -48.50548 | 2025-08-28 05:01:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0def8aad-de0a-3ec8-82ee-49f39537ef36 | -17.75742 | -44.47726 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0c3baea-570b-3e59-acf7-2700500fd040 | -17.77515 | -44.4975 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4f22c5b-a5a3-3020-a056-90821ebf3775 | -17.54988 | -46.6087 | 2025-08-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e962ebf-815e-322d-8ca3-86b54f311b26 | -22.53481 | -50.43488 | 2025-08-28 05:01:00 | NOAA-21 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6c2b6822-dcad-3668-bb42-dec578d1348c | -17.54829 | -46.62462 | 2025-08-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3f81628-9a22-3c42-98a1-c2b7a9f980fb | -21.03931 | -48.62641 | 2025-08-28 05:01:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ea986fd6-aa80-30e0-9895-7a768ca58701 | -17.76744 | -44.49768 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ed1fd18-dd9a-3d90-b9f6-2a36aa2cfd7a | -17.75695 | -44.48252 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f65599cd-62e1-3b89-9b7f-5e67afd7a6db | -20.13684 | -47.37582 | 2025-08-28 05:01:00 | NOAA-21 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c458299e-9b46-3354-a6ba-b9bd7018a152 | -17.77751 | -48.49986 | 2025-08-28 05:01:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bf42f4d-ddae-37db-aa97-7e24f8692ef1 | -14.78444 | -59.71785 | 2025-08-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 871ec363-3839-378b-81e8-228ff5469441 | -20.14264 | -47.3739 | 2025-08-28 05:01:00 | NOAA-21 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5dd2dd6c-fd5c-32c3-8776-a038f6dc8991 | -17.75575 | -44.49586 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 46661801-fb7f-302f-9229-e4433f783e4f | -14.77048 | -59.73359 | 2025-08-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc4464ad-ec19-3e57-a811-dd53d9bdd468 | -17.76782 | -44.49363 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7929646-368d-3bcb-9705-6de70ecbfc20 | -17.03809 | -52.70218 | 2025-08-28 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d8721bf-5f0b-3ac7-86f1-43ccb2a33794 | -20.13649 | -47.37951 | 2025-08-28 05:01:00 | NOAA-21 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28e5dfbe-042e-3f63-8ff0-186fa44f533b | -19.67921 | -49.36554 | 2025-08-28 05:01:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4791ed64-9528-3506-8a70-4232ee5d2d78 | -18.98173 | -52.13172 | 2025-08-28 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b20c584b-979a-312b-807c-af4072806eb3 | -17.15206 | -53.51761 | 2025-08-28 05:01:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e05baa7-d4ca-386b-90b8-26844f69af6b | -18.08109 | -44.06765 | 2025-08-28 05:01:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63accd7e-c185-3bfa-9e2a-819b132e73f0 | -14.78159 | -59.7127 | 2025-08-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba5d0382-0a33-3f65-8257-12a06f4b32c5 | -17.75613 | -44.49163 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 475f1d41-42c7-3de0-b0f1-d92ff1cce68a | -15.50859 | -56.06522 | 2025-08-28 05:01:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3f7902d-a127-3924-95f1-8b2b461889bf | -21.2982 | -56.20581 | 2025-08-28 05:01:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94e1a365-b415-3bda-b7a4-d7ea5745e180 | -16.01148 | -59.92736 | 2025-08-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3e6a687-8675-3129-b163-131c05d33c3f | -16.47307 | -54.66244 | 2025-08-28 05:01:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d2da530-c111-37bb-a7cf-ccd864ff3e86 | -21.14426 | -46.97363 | 2025-08-28 05:01:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fd9c163-c12b-315d-a2d3-05a3d2bdf0d6 | -17.54459 | -46.62677 | 2025-08-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 367ec9b9-49ed-3adb-acaa-dda361405906 | -17.76903 | -44.49317 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94d7a2d1-da9d-3415-8703-d0d397205f58 | -21.03878 | -48.04482 | 2025-08-28 05:01:00 | NOAA-21 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1eead1d4-bc85-3f87-a661-f5435d53937f | -18.52234 | -54.10067 | 2025-08-28 05:01:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a816b09-32fc-3f5a-ae98-7b1752766651 | -14.76603 | -59.73761 | 2025-08-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5595b61f-16d0-301f-989d-ca01b2880634 | -17.54869 | -46.62064 | 2025-08-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ba05d7e-b8d7-372b-95ad-def805d71406 | -14.77871 | -59.70772 | 2025-08-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30accbc2-0b22-3353-aa91-c5913ccbab67 | -20.11699 | -44.34512 | 2025-08-28 05:01:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8baa92e1-f583-3053-bf35-eac750e5d537 | -18.07673 | -44.06803 | 2025-08-28 05:01:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86d9f1b8-d409-3442-bb1f-50c096c9f07b | -17.91789 | -45.90599 | 2025-08-28 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c933f1e1-eaf7-3da1-b910-6474465b30c8 | -17.77796 | -48.49821 | 2025-08-28 05:01:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39e414ad-a44f-30ba-b48e-c7390e2a953f | -14.78366 | -59.72236 | 2025-08-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c7158534-684d-3289-897d-c9b23f51f130 | -21.03897 | -48.62967 | 2025-08-28 05:01:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 23cb7449-0dd5-3d64-a6e1-e19f6bd95e84 | -17.77765 | -48.50104 | 2025-08-28 05:01:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52b2fb59-2c57-3aff-97ae-c85c07f7fe20 | -18.25054 | -47.66486 | 2025-08-28 05:01:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dffc423-5870-3ce9-bcea-a483691d0a53 | -19.04067 | -43.99459 | 2025-08-28 05:01:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc8eef2c-d663-33f1-9014-3a2cc1bab2b6 | -17.55023 | -46.62746 | 2025-08-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 353d293d-36c6-349b-b240-fe6764772670 | -20.14814 | -47.3752 | 2025-08-28 05:01:00 | NOAA-21 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a83cfca3-4ec1-3883-93ef-1764737c0ef0 | -19.00194 | -57.62486 | 2025-08-28 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d9beabca-c350-39e9-9a98-8cfa68487cce | -17.97536 | -48.04284 | 2025-08-28 05:01:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1ec40de-4852-385f-94fc-48e399b2fbfb | -19.63434 | -44.00417 | 2025-08-28 05:01:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36eb972d-ecc2-3d29-ba1f-5c6e3333b769 | -20.14227 | -47.37786 | 2025-08-28 05:01:00 | NOAA-21 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c20df539-f823-363b-a389-a03c25ad3826 | -17.72816 | -45.53003 | 2025-08-28 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a11ef054-f799-3d00-b35f-0a6dbc55a248 | -16.65038 | -50.19249 | 2025-08-28 05:01:00 | NOAA-21 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90a6b683-b30f-3db4-b5b1-00278a991e56 | -17.75535 | -44.48779 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8b24e175-c626-3483-a948-3c436f334758 | -20.14775 | -47.3792 | 2025-08-28 05:01:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 802b50ff-da44-3ca6-9f28-ee39bcac255f | -17.75494 | -44.49206 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4cd0ce87-07f7-3e3d-a2a3-31a4ea170fcb | -17.7743 | -44.49403 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e17ec64-89e2-3b6a-8887-19b8bb3d9310 | -18.08375 | -44.0646 | 2025-08-28 05:01:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fa6074f-f7d8-3046-bc32-25b190609d62 | -21.9017 | -48.51512 | 2025-08-28 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b8763bf-2a3a-3a20-8213-aaafc5af1286 | -21.90416 | -49.59188 | 2025-08-28 05:01:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 89e0860e-43b3-303e-b776-11d46c1cdef6 | -18.25091 | -47.66143 | 2025-08-28 05:01:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f74de65-cdd9-385b-b753-a6d352d363ac | -17.75453 | -44.49633 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc1786b9-3d8d-3f5a-b9fa-1f9d54898f9e | -17.76867 | -44.49709 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 226a0d8e-5da0-3031-9984-9553588f8f2c | -17.77392 | -44.49794 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fed6087e-fc64-34d1-ba67-b789ed0a44c2 | -19.1154 | -44.03043 | 2025-08-28 05:01:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12966d0f-c7be-3b63-af00-844aae39d4b8 | -14.76963 | -59.73843 | 2025-08-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d21bb1e9-76e8-3604-b8dd-e922c04d2330 | -21.03912 | -48.04124 | 2025-08-28 05:01:00 | NOAA-21 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96294c5b-1b2d-36a8-a1cc-cef98545e7fe | -17.77551 | -44.4936 | 2025-08-28 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ad2aa1c-48a9-3849-b2c5-fa3fcf08ef80 | -17.77718 | -48.50526 | 2025-08-28 05:01:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f0ac0be-026a-38cb-9d0c-4ece7e72cbf5 | -18.08144 | -44.06361 | 2025-08-28 05:01:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b55c499-d444-3119-a035-1a0330270fdc | -21.67841 | -49.05524 | 2025-08-28 05:01:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9dd02b8-47c0-3f18-ab41-e1e33e640edb | -21.00753 | -47.37168 | 2025-08-28 05:01:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fca37052-85d3-32c8-be17-8728a0cab26a | -17.54502 | -46.62278 | 2025-08-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a4f3b7a-ee62-36bf-b384-057f125f9791 | -29.42953 | -55.61916 | 2025-08-28 05:04:00 | NOAA-21 | MANOEL VIANA | RIO GRANDE DO SUL | Brasil | 4311759 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| dad319cb-278f-3a93-96e3-1b8d7e9ad986 | -22.5462 | -50.434 | 2025-08-28 05:10:00 | GOES-19 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 0d984065-ba16-30e2-ab66-272a89df3830 | -14.2761 | -53.0655 | 2025-08-28 05:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 2ddec484-c3c9-37b5-9ad0-1bf19d5dbbec | -6.8772 | -43.6152 | 2025-08-28 05:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 3b9139ed-ec64-3dfa-9e7d-f72c613f2a41 | -6.896 | -43.6135 | 2025-08-28 05:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 01c954da-e965-39c7-b7ba-094bbe7ca7ca | -8.289 | -45.1814 | 2025-08-28 05:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| f23b7c80-e276-3989-8b24-78c42c578eb8 | -11.3521 | -43.5423 | 2025-08-28 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |


[Clique aqui para ver as próximas entradas](README67.md)
