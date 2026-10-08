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

## Dados Diários - Página 332

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14a0da97-5291-35c1-b493-46fd7f65c44e | -12.19459 | -44.82351 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 941e242f-01e2-322e-8e34-7b2825663bac | -13.16984 | -54.33125 | 2026-10-08 16:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 40f5b141-bfe2-3dea-a3bd-d64b4a176a7f | -8.96522 | -47.5472 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b1027967-91fd-30bd-8365-587a8ff9da85 | -7.75748 | -54.94851 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c4d4fe8f-4904-3c98-a32f-254884d298ad | -8.28534 | -45.70977 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4a96aae6-cc4d-32fb-a0ac-aed1c3cb5dcb | -12.17313 | -44.81608 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 380ce77f-b95c-3b02-8238-85522d340d01 | -9.07968 | -45.11212 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9cec66dc-b1fe-33d2-a48b-a9e950f427ef | -5.77395 | -42.0513 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 8afddee6-9eb9-38a9-bec5-bb574c70caee | -10.47406 | -47.23426 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 70efebef-c331-31a6-8197-3fa7d998f25e | -11.83587 | -48.09956 | 2026-10-08 16:37:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ca844fd9-7115-353c-98d2-d59d16b8aa09 | -11.10653 | -41.30697 | 2026-10-08 16:37:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9c8595ed-a18b-36f9-a819-eb8d169116fc | -7.82594 | -44.57555 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 174985d7-22e2-31b9-9fa8-8b8a6692ab93 | -6.92662 | -43.06979 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d7e31589-db08-305e-b7f1-33e4281c6d7f | -6.49484 | -41.83416 | 2026-10-08 16:37:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| a744e455-40a6-30cb-ac21-4ee9982fcc71 | -5.96407 | -40.91842 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| cc49c5de-5b55-36cf-9b1b-69d15fc097ba | -10.33082 | -43.60982 | 2026-10-08 16:37:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 4c8826d7-6a41-3db8-b1e8-df03f508c3ba | -11.45969 | -43.3863 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1dbfe926-848f-35ce-98c7-a8e1b8cc3007 | -8.19641 | -36.54673 | 2026-10-08 16:37:00 | NOAA-20 | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 043ed0f9-c3a9-3eeb-8fdb-3a27ef5fa597 | -9.83293 | -45.75995 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 26b5246d-f687-3d51-8c12-d88fef23f687 | -7.47298 | -45.12492 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f808f35-9a78-3015-b161-13d805fb56fe | -6.8503 | -39.54745 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6e0e6622-6ff0-379c-892f-5818c767383e | -11.2116 | -41.57719 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 75e102bc-5607-3ba4-b8e3-c4bb3a764712 | -5.92123 | -43.03417 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 94058448-e34f-352c-855f-9b33e7bf60e6 | -7.51042 | -44.42156 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6a71913-803b-3252-bdf7-2df704444d09 | -18.38518 | -40.31844 | 2026-10-08 16:37:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 34bd352d-aa51-36d7-9217-2a6001acaeff | -12.19152 | -44.64759 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c33f8810-7dbf-3831-a333-717e6f3c21cf | -14.50482 | -49.33505 | 2026-10-08 16:37:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 646d4d54-b881-3487-aa1f-2ea7f3325d2d | -11.64166 | -43.70077 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 63742872-7603-3ae5-9e43-d8c4f71f7643 | -11.77968 | -47.73136 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2895bd3-7036-3567-b1eb-75ba20779654 | -12.24067 | -44.74783 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a6219002-7a9e-3058-ac77-32529e3f02b7 | -11.58926 | -43.67234 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 62e89bef-2af3-3909-80ab-a3da6200bcd6 | -19.3633 | -40.35549 | 2026-10-08 16:37:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 32bb5564-4504-39c4-ab28-b229e7ee3eaf | -11.00203 | -45.41547 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a6dc7c69-b8a2-35a6-a67a-9d6c173bcd5a | -11.78866 | -43.53619 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 30fa2fcd-877d-30ea-9a36-25110f3859b0 | -5.70705 | -41.68882 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 16372873-7506-3921-84e0-e2876a3023c9 | -8.97704 | -45.93196 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 96101a4a-f5b2-3d77-9ef4-c19f0a96c4a8 | -18.96779 | -41.17396 | 2026-10-08 16:37:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2fc29137-4766-3422-ba92-a07ec859b386 | -8.19321 | -46.35695 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e3e310de-9f1b-3585-bf15-fdc0cd8cd1c5 | -9.13507 | -45.83214 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 8f988d80-98fc-34bc-b289-250740d32900 | -6.3146 | -35.13388 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 81e913d8-98c8-3c9e-9f6c-04cdf44dc1e7 | -7.18968 | -44.3108 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8fba33e3-6c6d-30a2-93b4-c2986c3ee2f9 | -12.308 | -47.06184 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 36e826c7-9fa9-3570-a4e0-59f59c4a5875 | -11.75867 | -45.48661 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 307e82ad-29d0-3bbe-8405-96cbc6333e3b | -9.94679 | -43.57077 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 097ba39b-9637-3fc7-b506-4ced0d55c970 | -10.25101 | -49.66038 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d09a65ba-0e04-3a99-a07f-99772c511177 | -8.68831 | -45.28234 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d22d542-c7da-341c-b769-a736046976ee | -7.14288 | -45.00978 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 333f832f-c03e-35f1-8919-461a9b044109 | -7.7069 | -45.4542 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 2b3128bb-3a30-3489-9917-b373e1d25be6 | -11.36659 | -46.71296 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5421f36a-6deb-361d-9dc5-87b1f45cc0bd | -8.93267 | -45.17229 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| c85243c9-9a1e-3b20-b6c7-3e93c090c153 | -11.45912 | -43.38265 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 94672525-3545-30f9-b890-2018cc2576c6 | -8.7891 | -47.28098 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d4909dd0-2174-39f3-9fc0-7a8baaeb3c40 | -7.22711 | -39.244 | 2026-10-08 16:37:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 24c50389-069b-336d-a45d-59013da2caa7 | -8.32752 | -51.30992 | 2026-10-08 16:37:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| bf716c71-d9f2-3c5c-89b4-1619033ed3fa | -12.77752 | -44.86559 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 650af34d-ddb7-3e21-ad53-2f9d6134166c | -8.18855 | -45.7644 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a7293ffa-a705-3e02-bd45-f45456fbf47a | -6.31563 | -44.03712 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 52caa0ec-2bad-3777-8d4d-b1e08a3d306c | -12.13491 | -43.31504 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 5d9d0d25-7ded-3603-ad15-4189bccfa457 | -9.04605 | -40.29859 | 2026-10-08 16:37:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0b45db52-8c77-3f42-a6ce-4f1117ae7095 | -12.03559 | -43.44024 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| b8d30679-4ebd-34bf-987f-d84c29d106d5 | -9.88717 | -44.86736 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 2d55c4c7-f064-3353-917c-21a4cfb8f3f1 | -11.40478 | -44.96233 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2b8a25cc-2a8f-326a-aedb-707ccbdc7022 | -9.92438 | -44.80074 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4c5bcfb3-6f9c-3739-8d1c-e23666c1a263 | -8.06856 | -45.62336 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 5119a1d1-9dcc-3884-b8fd-5cad39bfaba9 | -6.89327 | -43.83104 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| fbdd8d6e-9c5f-3dea-9f2a-eafecc25c79e | -8.0675 | -45.61642 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1a8e29d9-2c31-3e94-a7ae-662c81816be4 | -11.5212 | -48.22169 | 2026-10-08 16:37:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 25a0cc27-86a5-31a1-93fa-6a63a54e8ac2 | -6.92011 | -44.56009 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5337be19-3b18-32d7-b070-df8483c9749f | -11.82503 | -44.69209 | 2026-10-08 16:37:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 52d52c3b-e163-38ca-920a-8151d06d34b5 | -6.93496 | -43.67381 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| ada26804-391c-3320-8a47-8647186d32f8 | -7.72065 | -44.72967 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8f1afc57-1d54-3317-b776-a882fe5e3dcf | -11.5937 | -43.65688 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7a032b1f-a590-3920-a195-05f57127fae4 | -7.85626 | -45.14601 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| db9390af-15ca-3afa-8b5a-45136f79aa12 | -11.77811 | -45.5709 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 98b96d2c-1002-38d8-9762-7045db1f25c7 | -9.81466 | -45.68375 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 38384586-62e2-32ee-9cf2-104d2e1f43fb | -6.31238 | -35.13654 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 32e5bd19-7f71-363b-a89f-8986f5d27e2e | -6.94073 | -41.95131 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6fec2d14-dd51-3d2d-9f11-4f038d313d1a | -12.02946 | -43.44497 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 61ca7189-7341-3f28-9b62-cf91fed8049e | -11.85226 | -47.38331 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7054edf9-1fa6-3dc2-b048-b5ef7b69fdd5 | -8.95951 | -45.14639 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9ee2c7ff-e000-3c40-b318-824fb5fd919c | -11.08472 | -44.02979 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 5429472f-4175-3d4e-b316-3f7cb102dbe9 | -11.40831 | -46.68756 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3bee93f1-6128-384a-bc7b-c048ab1db1f5 | -5.99279 | -40.93892 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 672b3b1f-341b-3928-801c-b888df48e30e | -11.06178 | -39.50504 | 2026-10-08 16:37:00 | NOAA-20 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 305b2b36-39c9-3855-b62e-c312d8265fc5 | -7.94123 | -50.96044 | 2026-10-08 16:37:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8c8e426-1006-36a7-b101-e6b225a189d6 | -7.75561 | -43.81215 | 2026-10-08 16:37:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a4481d0f-d822-357d-acc7-8a57a713f5a1 | -6.72516 | -45.18458 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3165e6a8-653e-3b33-b4c8-33110c24fccd | -11.20056 | -45.22556 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| f920a271-bde5-387d-b90f-a705f77cb68c | -6.59878 | -37.89957 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 117.4 |
| ec23e920-2002-35c2-9b29-bddacc33979b | -9.20319 | -46.53428 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3799f624-3013-3b97-98a9-a9ba88c7fece | -6.38138 | -45.04567 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ef336913-3d54-3c70-8755-2e7b1172360a | -11.11597 | -45.70102 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 44e11138-b530-3460-9511-dceb6427ee39 | -12.71298 | -45.81414 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d0045152-c057-3033-843f-8a268c053862 | -8.59888 | -47.15067 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 56d7359c-f3b7-3e80-ac45-df48bad4e4da | -6.89761 | -38.52686 | 2026-10-08 16:37:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 13.6 |
| b950f732-d457-3376-9685-e6a4cf83545a | -6.97527 | -47.66763 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a3f7fc75-c5e5-3f9d-9b40-9943de98f017 | -9.89933 | -44.85831 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 884ae761-be38-3025-9012-b67ce0f8a637 | -10.24829 | -49.66809 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4006c25d-ed87-34de-92ad-0957dc29d90f | -7.70563 | -44.74281 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7743d973-7fe6-38a2-99f5-d6a3431eebf5 | -7.7697 | -44.1701 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README333.md)
