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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 798493ea-9c3c-39d0-bdf1-0ad4d939ee35 | -6.6574 | -43.1348 | 2024-09-28 12:49:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| bf91b65e-b14f-3ea9-9e77-37ebabb8b506 | -7.88107 | -42.68877 | 2024-09-28 12:49:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 891c511b-aad6-39eb-b6ee-c6a60d7aaf33 | -6.94463 | -42.76271 | 2024-09-28 12:49:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 20101210-091e-35b6-97e2-78e7d8da7a3d | -6.85421 | -43.12276 | 2024-09-28 12:49:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 810c1969-f624-31e8-a4d9-1e731b13019a | -9.28101 | -43.46934 | 2024-09-28 12:49:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| b979b40e-c8b1-3f35-a4a8-686b8b996cb8 | -3.41452 | -44.45496 | 2024-09-28 12:49:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1bda236e-f287-35a7-be89-ad76b7f8796e | -4.93869 | -43.63407 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 93cee306-2e8b-3481-a686-29bced194fed | -4.79249 | -43.78912 | 2024-09-28 12:49:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 3c0d1003-a90b-342c-be83-344c6f8a9df0 | -4.73864 | -43.25365 | 2024-09-28 12:49:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0419f6b7-d66a-3574-8594-cdc8ee43603a | -4.61871 | -43.29152 | 2024-09-28 12:49:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 2868da3c-d626-3afa-bcc3-e361168c0821 | -4.51098 | -43.48878 | 2024-09-28 12:49:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| df6d1ab7-9a5a-3bd2-bd17-d07e651bc5d4 | -5.94632 | -43.99732 | 2024-09-28 12:49:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 08c608ec-578e-3269-aca6-bf9be1c7180f | -5.31012 | -43.3585 | 2024-09-28 12:49:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1c8e950b-0ec5-322f-ad9e-cc8cab4cf846 | -5.28328 | -43.47379 | 2024-09-28 12:49:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| bc9e2c7b-b335-38a1-a4b5-ad72df4932bf | -7.87764 | -44.61412 | 2024-09-28 12:49:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 22192df6-4069-37b9-b84d-bf91461f866b | -7.58981 | -43.87305 | 2024-09-28 12:49:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 0664b33d-9ca8-3aa0-bf61-4484ce22fe67 | -7.58286 | -45.03727 | 2024-09-28 12:49:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 791841c4-8b56-3c8d-80e5-3e834fb0d340 | -7.89428 | -44.60931 | 2024-09-28 12:49:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6b6ad0c7-1695-37d6-aae7-ff04a5c46624 | -7.88362 | -44.60794 | 2024-09-28 12:49:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 14402a1a-f90c-3258-940d-731e50d759b7 | -7.87948 | -44.60078 | 2024-09-28 12:49:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 74687dcb-f73a-3a4e-8ec1-5063fa6312cc | -7.58786 | -43.88746 | 2024-09-28 12:49:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| ba81f007-870a-30d2-a1aa-ff20ac8f7ba0 | -7.57469 | -43.90047 | 2024-09-28 12:49:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| db31d57a-f604-3179-a41d-eeb7f290b417 | -7.38824 | -44.10476 | 2024-09-28 12:49:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 31.5 |
| e6fd4e19-6c1d-309e-903a-7cc7bc2b7f79 | -6.61231 | -43.81575 | 2024-09-28 12:49:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9eb66173-927b-3d53-81e4-166abf34bf28 | -6.69798 | -44.55394 | 2024-09-28 12:49:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8b65a961-51b0-3bb4-93e8-fcec5b629398 | -7.5786 | -43.87147 | 2024-09-28 12:49:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| cedcaf1b-ddb0-312e-bff5-f8583c7f0133 | -7.57665 | -43.88592 | 2024-09-28 12:49:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 2e8d5ccc-086f-35eb-a66f-8f239f1bc18c | -7.38689 | -44.09807 | 2024-09-28 12:49:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 2256945b-4f88-3078-bdd6-901e679e8cec | -6.58605 | -44.18072 | 2024-09-28 12:49:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 7f194ea6-f47d-3f73-982d-12e6b843d230 | -7.87154 | -45.09467 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 24e206c2-970f-3d3d-9381-70de81218949 | -7.76694 | -44.67282 | 2024-09-28 12:49:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| f168713d-4623-338f-873e-eac5dd19c4dd | -7.81486 | -45.28232 | 2024-09-28 12:49:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a10ed129-1d50-3bfb-b42b-a02f18430e20 | -7.81326 | -45.2941 | 2024-09-28 12:49:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 31ae8235-59d1-3f81-8835-00a94fa8c355 | -7.78221 | -44.68082 | 2024-09-28 12:49:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 9a0c57e7-3e62-379a-a21b-7b5ec36fc19f | -7.77571 | -44.68727 | 2024-09-28 12:49:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 6c44f0be-65ed-36db-85cb-5461485b5466 | -7.43162 | -45.16975 | 2024-09-28 12:49:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 97a41f59-51d7-34da-b051-00676857721d | -7.34147 | -44.78533 | 2024-09-28 12:49:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b214f5ac-d1ed-34d5-9733-ec36fd1bbc63 | -7.28013 | -44.94695 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 30193ef3-8229-35bf-a6a7-d47dae8fda98 | -7.27845 | -44.94068 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| a68602d7-1eed-3f02-aa45-9de1ce72a4e4 | -6.6926 | -44.54696 | 2024-09-28 12:49:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9b93fb35-6cdf-3478-b0c8-54703a537caa | -8.82359 | -45.08235 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4a4b4347-3382-3e2b-bf12-2d5f6a08efb7 | -8.81316 | -45.08096 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| b85143c9-cf74-34a8-90fc-660a63b5edb3 | -8.4678 | -44.76163 | 2024-09-28 12:49:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| a97db9ed-d8b4-335c-9f4f-c243916ba6ea | -8.31423 | -44.98256 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| eda99c4f-4d82-390a-9153-84ae1fc39758 | -9.03271 | -45.10188 | 2024-09-28 12:49:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1b9c3e78-9a7d-3a82-8f8d-4fe2885c7010 | -8.71831 | -44.7861 | 2024-09-28 12:49:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| eb558826-a68f-3a9f-bd06-02441400e9df | -8.65988 | -45.37741 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 362364ff-ac2e-3cb9-8b19-1b43df8feec9 | -8.50991 | -44.89152 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| b845f1c2-93f8-3c43-b63a-62b4695808d6 | -8.4035 | -44.63895 | 2024-09-28 12:49:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d69d730d-1d4f-366d-888c-12f9996f2622 | -8.40171 | -44.65215 | 2024-09-28 12:49:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 07db2cc3-817a-3257-ba9f-296e052d59f5 | -8.82187 | -45.09481 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| d294d584-4c10-33e7-acbd-18003cb13d54 | -8.82074 | -45.07502 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 2e5c2786-19de-3577-8cb4-0c0f8bc2cd0c | -8.51099 | -44.52283 | 2024-09-28 12:49:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b553b325-3823-3fa2-a8e6-ea385c585606 | -8.81911 | -45.08756 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 22081aff-0f47-3511-9a1f-40b9bc44c0f9 | -8.72 | -44.77338 | 2024-09-28 12:49:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 8105280d-47f3-305e-9800-4a8e1c93e608 | -8.6615 | -45.36549 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8c8c7535-d822-3349-9b8f-e68e33479bb1 | -8.50813 | -44.90493 | 2024-09-28 12:49:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 19b23aa0-79a6-3cbd-a1cd-bb48d263c5b2 | -8.46607 | -44.77439 | 2024-09-28 12:49:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 10f0f639-37ae-3c57-8e5f-9d89560c96a2 | -3.60183 | -44.50466 | 2024-09-28 12:49:00 | TERRA_M-T | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 30915052-08a7-3050-a835-bc5f317bb240 | -7.82814 | -45.48484 | 2024-09-28 12:49:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 74aba1b5-e676-39f2-b087-c82ac6f0e242 | -7.82973 | -45.4734 | 2024-09-28 12:49:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ff1bd74d-2a85-3679-b59c-af4b1ef42c42 | -7.83344 | -45.52 | 2024-09-28 12:49:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 6fd01b8b-36d2-34c9-ae00-8435bd9cbf36 | -7.82345 | -45.51873 | 2024-09-28 12:49:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 18958a38-7fe5-3a62-8559-1d2030e0d05d | -7.82185 | -45.53024 | 2024-09-28 12:49:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 51a82ddd-0891-3ed1-90b5-b933faee76ed | -7.71408 | -46.54989 | 2024-09-28 12:49:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c97b047c-9c80-3009-a51d-920bbccc05a7 | -7.0287 | -45.35611 | 2024-09-28 12:49:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4ac48446-f65a-3004-b33f-e00cfd52bde2 | -7.02029 | -45.34352 | 2024-09-28 12:49:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 10fa2627-6be9-3786-95c3-7acf531438dd | -7.83183 | -45.53153 | 2024-09-28 12:49:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| e2e4bf61-80a9-39ac-9b90-aadb11d763b9 | -7.36296 | -46.76789 | 2024-09-28 12:49:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f613cab2-9c95-3633-92a5-b1c2ec682b8d | -7.36159 | -46.7776 | 2024-09-28 12:49:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d4019564-39ca-39f4-bbbc-0969ae9c7410 | -7.31828 | -46.68239 | 2024-09-28 12:49:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d358c735-0286-39c4-b17d-256d3fcb4b91 | -7.16421 | -45.86506 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 345.7 |
| bb12236b-e206-3898-9c45-acc3a87ea081 | -7.15453 | -45.86382 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 322ab527-bc40-38a2-b409-03c6cb6ea2e7 | -7.03028 | -45.3448 | 2024-09-28 12:49:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| b85d69c5-e0e4-34ab-b206-fca4b5cfbac1 | -7.01872 | -45.35483 | 2024-09-28 12:49:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4d74c3a6-93ef-38ac-a7ef-d7e3a0c4b8c7 | -8.9278 | -45.88565 | 2024-09-28 12:49:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 301217bc-898e-3561-b00c-0fb90881bebd | -8.92627 | -45.89695 | 2024-09-28 12:49:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 412171d1-0aff-3691-ba57-8e4d6bd638db | -8.87741 | -45.65323 | 2024-09-28 12:49:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| be33b731-4ff8-3325-ba8e-cbdc7e27be9e | -8.40538 | -46.34548 | 2024-09-28 12:49:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| af52d312-7087-3385-b390-4c68b21ef586 | -8.40248 | -46.36658 | 2024-09-28 12:49:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| c4c72e67-3ee5-3066-970e-ee845e37c9f2 | -8.88902 | -45.64295 | 2024-09-28 12:49:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c3b30827-246b-3179-bf76-3f6c5eb31fe2 | -8.40392 | -46.35604 | 2024-09-28 12:49:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 60325dc8-6348-3f58-90d0-8b73b7e1a530 | -8.12444 | -46.79277 | 2024-09-28 12:49:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f5b1ea46-89db-32c2-ab3f-226d075e4c74 | -5.88446 | -47.70888 | 2024-09-28 12:49:00 | TERRA_M-T | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| dec46aa9-0ea8-3933-bea7-abe3e85a1ee1 | -5.33237 | -47.70309 | 2024-09-28 12:49:00 | TERRA_M-T | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2aac2115-515e-30f3-b6c4-88883931e347 | -6.12149 | -47.27033 | 2024-09-28 12:49:00 | TERRA_M-T | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c2ee3947-33fb-3cee-8888-2064967bc9a1 | -6.08511 | -47.65815 | 2024-09-28 12:49:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b534c6e9-72c9-35fe-a678-12563bf35504 | -8.3408 | -47.5377 | 2024-09-28 12:49:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9873940e-0006-30d4-8ba0-3f0c00ccdff9 | -8.1973 | -48.21688 | 2024-09-28 12:49:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 65d79614-0f5f-3b31-ba44-c5dd26465538 | -8.12844 | -47.3468 | 2024-09-28 12:49:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b1c67acf-1952-3236-ac69-574b3dcb26b8 | -1.04648 | -47.74741 | 2024-09-28 12:49:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d97bc263-8e10-3196-ab7e-98abe248af03 | -2.95167 | -48.59882 | 2024-09-28 12:49:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b88f4d40-721a-3f1d-8762-0fa46b2e28c6 | -4.95523 | -47.88759 | 2024-09-28 12:49:00 | TERRA_M-T | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d038ff7-2276-3037-b05a-b313d97e984a | -4.91349 | -48.61311 | 2024-09-28 12:49:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c066c733-bc52-351b-9e75-d9f9f55a7e87 | -4.58833 | -48.75841 | 2024-09-28 12:49:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| ae96b4a3-f0e0-329b-a21e-939594314aea | -4.40183 | -48.71039 | 2024-09-28 12:49:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 0411af01-219e-31d4-bddd-979c867b7d88 | -4.19433 | -48.23528 | 2024-09-28 12:49:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 20a1749c-444b-32f7-a4b5-00842c2820ec | -3.55367 | -49.02523 | 2024-09-28 12:49:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 06935b69-3253-39fc-a28a-2650070f99fc | -5.93593 | -49.19081 | 2024-09-28 12:49:00 | TERRA_M-T | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 6dfe04f0-b198-3f82-8c64-a1dc1931d68f | -5.93461 | -49.19988 | 2024-09-28 12:49:00 | TERRA_M-T | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |


[Clique aqui para ver as próximas entradas](README102.md)
