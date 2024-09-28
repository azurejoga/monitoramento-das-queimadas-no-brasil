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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39f0a049-beff-3d59-bdcc-6e954c702eb5 | -20.26032 | -41.30193 | 2024-09-28 04:23:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b5dc24a4-d148-3046-a4dd-50019accc725 | -20.08466 | -41.68135 | 2024-09-28 04:23:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ccfe4f14-90cb-3bb0-ab13-1427aeb8d722 | -20.08415 | -41.68554 | 2024-09-28 04:23:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 4cc6cfbf-41d0-3b77-8d76-729297c6979d | -19.95139 | -41.42425 | 2024-09-28 04:23:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dc3706d3-1c69-3554-9523-2c7f9f623921 | -19.93431 | -41.78589 | 2024-09-28 04:23:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b21686e7-afe6-3ff2-8c9a-78b8464e8737 | -19.93382 | -41.78995 | 2024-09-28 04:23:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a43939e8-818c-31b0-8665-d8b170d6020a | -19.52381 | -41.55315 | 2024-09-28 04:23:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0131d82e-dacb-38c2-a71d-2276f7ef20db | -20.70914 | -41.7781 | 2024-09-28 04:23:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 98e7f091-0fea-337e-aebd-628e2d15178d | -20.7086 | -41.78256 | 2024-09-28 04:23:00 | NOAA-21 | DORES DO RIO PRETO | ESPÍRITO SANTO | Brasil | 3202009 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| e7cb734b-4d38-32df-a380-37a60330d361 | -20.61983 | -41.7365 | 2024-09-28 04:23:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c99a8a8c-9225-3c79-8384-ddc0661e7468 | -20.61931 | -41.74078 | 2024-09-28 04:23:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2ffe188d-64de-3837-af46-3a30e8ec0c46 | -20.5188 | -41.96294 | 2024-09-28 04:23:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 89a47c1b-1599-393b-a4a5-b06d03084b8f | -20.51678 | -41.97902 | 2024-09-28 04:23:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a29b5e75-5c65-3857-879c-b171d703165b | -20.51532 | -41.96154 | 2024-09-28 04:23:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d0d065e7-c7bc-3844-875e-48f6d52bb779 | -20.51484 | -41.96557 | 2024-09-28 04:23:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9a0840b7-e774-3b0d-bb24-78cae5ded00b | -20.51457 | -41.96255 | 2024-09-28 04:23:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b137c9a4-ea52-3123-b4f0-7afad7fc0023 | -20.51343 | -41.97748 | 2024-09-28 04:23:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 91ce3470-1a09-38c5-a597-1634e0da3057 | -20.5092 | -41.97712 | 2024-09-28 04:23:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f403fe8b-56b4-3f1e-8613-537923b5f44e | -20.50886 | -41.97403 | 2024-09-28 04:23:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8ddc163f-816e-3aad-9e38-bdd53af8f44b | -20.50835 | -41.97812 | 2024-09-28 04:23:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9cad956a-6b73-38c9-af8d-d5ee160a2049 | -20.50514 | -41.96951 | 2024-09-28 04:23:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1b0c0581-0d2a-359f-a85e-959e7302e243 | -20.50463 | -41.97365 | 2024-09-28 04:23:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 19bd0d3f-1dbd-3ba8-95c4-54bec5873e7c | -20.47861 | -41.16076 | 2024-09-28 04:23:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 96611fef-eb10-3973-a788-79cc3de958bb | -20.4781 | -41.16506 | 2024-09-28 04:23:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| e7aa5fa9-c88a-3a1e-a952-6c4b8063b65d | -20.47759 | -41.16937 | 2024-09-28 04:23:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 6cbec277-d6f2-3bdb-a5f4-b2e6d809b6d4 | -20.47369 | -41.16431 | 2024-09-28 04:23:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5660e574-9e79-3a2f-9a7d-864509f3da60 | -20.47317 | -41.16873 | 2024-09-28 04:23:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5577a318-5bf0-33d7-b097-62bccc2e9478 | -20.4369 | -42.00397 | 2024-09-28 04:23:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 86d01cdb-2b3d-3599-989d-84b57f368bfe | -20.4364 | -42.00813 | 2024-09-28 04:23:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 15c3134e-b8d0-3adc-9386-44c29246905b | -20.43592 | -42.01208 | 2024-09-28 04:23:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6b273395-5ba7-37bb-acd9-558780747e55 | -20.43275 | -42.00301 | 2024-09-28 04:23:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 05e10496-7fb1-310f-a2a5-6e13d6b835d6 | -20.82682 | -41.6201 | 2024-09-28 04:23:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 406cd40d-c39c-3188-9d51-7820d4603da6 | -20.82635 | -41.62401 | 2024-09-28 04:23:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e00e828f-5551-34e7-9ce4-dc62900d40a8 | -20.82303 | -41.61497 | 2024-09-28 04:23:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 222a40e9-74f1-31a0-8ba4-9e3ad3d41e15 | -20.82253 | -41.61923 | 2024-09-28 04:23:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4e201324-dcfd-3a12-9276-485387f4a1ac | -20.82205 | -41.62327 | 2024-09-28 04:23:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 90b53fa9-5c31-3474-992b-b37b3c33164c | -20.82158 | -41.62717 | 2024-09-28 04:23:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 121e021b-92df-3ae4-9a09-433ccdf55dc9 | -21.60395 | -41.88334 | 2024-09-28 04:23:00 | NOAA-21 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1417b0e5-1944-35f8-a756-3c1870194fc6 | -21.60262 | -41.88048 | 2024-09-28 04:23:00 | NOAA-21 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1313abb8-610b-3b18-a55a-3638972c9c5f | -21.60212 | -41.88483 | 2024-09-28 04:23:00 | NOAA-21 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3aa1c758-1452-3062-962b-3f807a3fb6cb | -21.59966 | -41.88276 | 2024-09-28 04:23:00 | NOAA-21 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6d19caa2-5c97-3cd3-8b92-22c4f04a643a | -21.50597 | -42.04952 | 2024-09-28 04:23:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0bf3448e-fc27-3fd8-b37f-d8fe66abf208 | -21.29719 | -41.92467 | 2024-09-28 04:23:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bc099ad2-ff38-3718-9af7-f61bdcd53c0e | -21.29677 | -41.92822 | 2024-09-28 04:23:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3adc19d9-678a-3671-a651-62376b85bc95 | -17.78021 | -42.81021 | 2024-09-28 04:23:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df089d3a-bc8f-3cc1-89ff-e7f7a18bbd82 | -17.71186 | -42.33083 | 2024-09-28 04:23:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b87179b-1d19-364e-95a2-9a77511b9f7e | -17.44592 | -42.62141 | 2024-09-28 04:23:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 36.6 |
| f46894d3-d9b7-31f3-9969-6402a427946c | -17.43885 | -42.61515 | 2024-09-28 04:23:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| e0f4548d-7cce-3249-ac4b-956f3dc1c40d | -17.43818 | -42.62027 | 2024-09-28 04:23:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 442d63e7-895f-39a6-b637-8cc4ead5a957 | -17.90752 | -42.13728 | 2024-09-28 04:23:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 01fdcb48-1da4-3bbe-9c68-da48541c8e17 | -17.88896 | -42.14275 | 2024-09-28 04:23:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2ad20a26-7cb6-3521-b481-3843e9869ba9 | -17.88542 | -42.13852 | 2024-09-28 04:23:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f7f997bd-465a-3887-9a30-3dc7eb3ea0ba | -17.98088 | -42.29484 | 2024-09-28 04:23:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 55669ab5-10dc-34ac-b077-9a376d786fb0 | -17.91154 | -42.13786 | 2024-09-28 04:23:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3f84d9d5-1bc4-3950-a279-233ad51e1fc7 | -17.88945 | -42.13905 | 2024-09-28 04:23:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 80774de0-01d0-3e47-ba32-1a1a33fe2f98 | -17.88494 | -42.14222 | 2024-09-28 04:23:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 59e694ef-bda6-356f-b9d5-919636e607d2 | -17.44661 | -42.61626 | 2024-09-28 04:23:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fb5571cd-5c3d-3891-9059-ac84dec40210 | -17.56193 | -42.34938 | 2024-09-28 04:23:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b60dc178-0420-302e-90e0-b060cc6f64ad | -17.44273 | -42.6157 | 2024-09-28 04:23:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| f3da40f0-1604-3ff3-a4a2-3b0d390598d0 | -17.44205 | -42.62085 | 2024-09-28 04:23:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 3a2a1508-b583-3146-b68a-f9ab69d428bf | -17.91605 | -42.13447 | 2024-09-28 04:23:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a81fb2e-8d98-387d-964b-0a725a545103 | -17.91202 | -42.13396 | 2024-09-28 04:23:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b5ca4a22-925f-3543-afdb-17929fff48ee | -17.9769 | -42.29424 | 2024-09-28 04:23:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 055e3f29-cb96-3581-a8a9-e17b9bade350 | -17.91557 | -42.13831 | 2024-09-28 04:23:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 66c72b3f-1dca-3514-b6ad-32898e7fe3fa | -17.91008 | -42.13774 | 2024-09-28 04:23:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fb1bde2e-7bb0-372c-b889-d587cc4a1c75 | -19.3957 | -42.9912 | 2024-09-28 04:23:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 397c9cce-0244-3001-8e41-cae4ecdc26cd | -19.39222 | -42.58441 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c99e1200-2582-3a11-88f8-b77767974623 | -19.38605 | -42.60123 | 2024-09-28 04:23:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 54b670ac-1a58-30f9-a9a4-d3e5ee75871e | -19.37803 | -42.60055 | 2024-09-28 04:23:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 330989f0-42f7-32a9-8d24-b313b01c92a8 | -19.37614 | -42.58329 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| a87fc2b1-274e-34e1-bf2b-482bd90fb8d0 | -19.36956 | -42.57088 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| af6984ae-9a89-3552-a513-44c7a0e3f94a | -19.36433 | -42.5803 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0249d972-5b52-3e12-8b4a-78de3238561c | -19.36294 | -42.57328 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| c8413582-6a4e-36e4-83c6-107794cbfe63 | -19.27847 | -42.72575 | 2024-09-28 04:23:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4b884c47-d1e5-3d83-ac65-f6c6a699485e | -19.27454 | -42.72503 | 2024-09-28 04:23:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 21f35647-b9f2-3de8-a68e-36300ea64e38 | -19.40813 | -42.32669 | 2024-09-28 04:23:00 | NOAA-21 | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 16ca018d-a917-355d-bc42-59b4908b1c16 | -19.40159 | -42.57452 | 2024-09-28 04:23:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c6b1afd9-4278-3128-a87b-57484323bb05 | -19.39148 | -42.59035 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6e894140-9e45-306d-8514-8a524dcd4c75 | -19.36765 | -42.56836 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1a48d4b8-0df4-3ded-bcc0-64c0556bdbb2 | -19.36684 | -42.59271 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6c57d6ee-1289-302b-80ca-c19ac78fcd3d | -19.36463 | -42.59127 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| adcd5e32-216d-3c31-8498-530203d7ef95 | -19.3639 | -42.59682 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3b0a522a-7d16-3245-9b1b-255412007153 | -19.36107 | -42.5738 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 56311e4c-f8c4-33d0-8f30-997a40b1ea7e | -19.40431 | -42.58509 | 2024-09-28 04:23:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7553e8ec-9078-36a2-bcf4-2464dc98a557 | -19.39541 | -43.27663 | 2024-09-28 04:23:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 991df81f-777e-34b6-8488-b79fde0559f3 | -19.39476 | -43.2817 | 2024-09-28 04:23:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 22b5de46-118c-32ee-9ae5-a4dfada6546a | -19.3787 | -42.59527 | 2024-09-28 04:23:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 171d75f9-ace2-3cb4-9b3b-a4afb89a2f8a | -19.36687 | -42.57432 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 03616b74-e129-314b-9a29-88ed20a2edf2 | -19.36613 | -42.56573 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 7409419e-c31a-3b20-8da8-b5e2fb72e2c1 | -19.36371 | -42.56747 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 6e9c7565-94b9-3cec-a52a-aa1eff18b02f | -19.36221 | -42.59735 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d7a63349-30e9-3ed3-890a-c901e6d2845f | -19.36166 | -42.56901 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 057d5ead-ae43-375d-83ba-538365a867a7 | -19.35896 | -42.57266 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 99ddee97-bfc9-3522-94be-50d00bd21102 | -19.4266 | -42.50598 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0b5dd0d3-17fc-31f4-bff6-e79a113efe1b | -19.38674 | -42.59579 | 2024-09-28 04:23:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 86466333-e13a-31c8-8ec4-961d3b217953 | -19.37474 | -42.59449 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 907133dc-aea5-30e9-bf51-1102db4f9248 | -19.36616 | -42.59818 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 551a18fc-44d0-3712-a5ac-de40c1c57871 | -19.36562 | -42.56987 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 653896b8-6439-3994-b8a6-b727d91b9dee | -19.36221 | -42.57885 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e54d904b-1d9b-33b6-b3d3-c17b818860a6 | -19.36216 | -42.565 | 2024-09-28 04:23:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |


[Clique aqui para ver as próximas entradas](README60.md)
