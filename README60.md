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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b72d6ee-2abe-32f2-a0e7-5bde625410f6 | -8.31443 | -43.3938 | 2024-09-26 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 25831825-f9d9-3a7f-a223-a02db72d50ee | -9.18051 | -43.05239 | 2024-09-26 04:06:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5fc35b17-cd35-39f9-8b31-33a8df405dda | -8.31104 | -43.39324 | 2024-09-26 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c109151b-6f17-3707-ad67-d06fccddbeb4 | -8.06964 | -42.88496 | 2024-09-26 04:06:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fef72f55-f037-343b-b6c2-b680d5e6d959 | -10.85005 | -43.63921 | 2024-09-26 04:06:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90dd28fb-813c-3d64-a0a9-c8eb430cb435 | -10.47809 | -43.37567 | 2024-09-26 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8407615-d91f-3920-8041-de0699165a30 | -10.47141 | -43.37458 | 2024-09-26 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 39b907e0-f3a3-3a63-9c15-8d76aef158a1 | -10.29752 | -43.52352 | 2024-09-26 04:06:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e26ef8f-f272-3a7d-97c0-15a20a9bd4fd | -10.29693 | -43.52711 | 2024-09-26 04:06:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| baa05d91-70b7-3ecf-9652-d6eaaaad9e39 | -10.29416 | -43.52296 | 2024-09-26 04:06:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 500d7667-0da9-3349-b36a-f43da65412e6 | -10.19809 | -43.85072 | 2024-09-26 04:06:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ef1f78f-2bc7-389b-be12-542ce2e5a923 | -11.20116 | -43.33631 | 2024-09-26 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1e7770c-3737-3cee-a46c-6e1c2080d03d | -11.20059 | -43.33989 | 2024-09-26 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7154b48c-6fc7-3af9-8b93-56315af93cf7 | -12.2487 | -43.88291 | 2024-09-26 04:06:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f3ba367-aa81-37dc-b5bb-d40ecb3db186 | -11.84771 | -43.82138 | 2024-09-26 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 269cef6d-4f33-309d-be79-12e4dbe038b6 | -11.84713 | -43.82499 | 2024-09-26 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36059ecb-7fcd-3a4a-b4f4-c1d7b3683a18 | -11.84655 | -43.82861 | 2024-09-26 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd160da6-46c5-38bd-81bc-45166c1dfd7a | -11.84436 | -43.82082 | 2024-09-26 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f56b22cc-c639-3c00-84fe-17e33102d7c6 | -11.84378 | -43.82443 | 2024-09-26 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70054a7f-98cd-3d66-bbd3-cc9f1dc78abd | -11.8432 | -43.82805 | 2024-09-26 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69d74fb8-0603-37fe-ac49-1aaf682de7c0 | -11.68548 | -44.52148 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a70755f-e1a9-3369-aece-4d728cfe1416 | -11.68486 | -44.52526 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e7bc02f-f52c-39d7-9faf-2399a2dc0c62 | -11.68144 | -44.52468 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df9fe0b3-4302-346b-a708-8c82ce94bef0 | -11.68112 | -44.50523 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 92993354-6c63-3bb0-9014-15c8c01a0609 | -11.6777 | -44.50465 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2b09a0bb-3809-383b-aec9-b143f13de58b | -11.67708 | -44.50842 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 224fdda5-830c-34d0-923a-542994c49b2f | -11.67646 | -44.5122 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09f25b18-d198-3566-b200-0fc84f021767 | -11.67366 | -44.50785 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcf33bba-d3dc-3b34-84db-1194c02076da | -11.67304 | -44.51162 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48b52f57-88ce-3d54-8583-f02512796517 | -11.669 | -44.51482 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dd3c7d7-e420-366f-8869-7f280cca1919 | -11.66838 | -44.51859 | 2024-09-26 04:06:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02cf173c-4f33-3ad5-9c3a-a5a67573ccd4 | -10.99221 | -44.42746 | 2024-09-26 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db3912ad-db75-360c-9df6-5ce9094d9f36 | -10.9916 | -44.43125 | 2024-09-26 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9193d8d7-9e0e-33d6-9d32-1f27e6a43500 | -10.98878 | -44.42687 | 2024-09-26 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb0c5b48-7cc7-318b-a7f8-b9c862c9b353 | -10.98817 | -44.43066 | 2024-09-26 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67324ba1-9654-3637-a98d-539aec8d0b37 | -10.98536 | -44.42628 | 2024-09-26 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce6b988e-9e4f-37a6-b3ae-b913e8b7a977 | -10.98474 | -44.43007 | 2024-09-26 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 28f2f25c-6790-306b-b546-ab12bb985c30 | -6.56048 | -43.96127 | 2024-09-26 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3df62808-7110-333a-90de-feba84ca3444 | -6.5569 | -43.66296 | 2024-09-26 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bcacad8-c2c8-3ac2-ae7f-a240331eb127 | -6.42998 | -44.29749 | 2024-09-26 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b38f0639-c3f5-3188-98d9-2013a9bc8194 | -6.42332 | -44.02476 | 2024-09-26 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c83feb9d-0b67-3a06-a18f-265366004cf0 | -8.03387 | -43.977 | 2024-09-26 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a32b0b0-1c69-3147-83e0-169d5a9ce689 | -7.56549 | -44.06166 | 2024-09-26 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60a4e290-9692-36bb-8d0c-9e383bcda2b8 | -7.41444 | -44.4156 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 458b15f7-db15-312e-aaf8-e01db33d9605 | -7.41399 | -44.41436 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43292601-8c81-339a-9904-c06bca95a82f | -7.37385 | -44.39638 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7156bb05-d41b-3c2d-9327-eee9a67d11f7 | -7.37319 | -44.40041 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 75b91393-ceb8-32aa-afd7-f7164b7185f9 | -7.36781 | -44.10196 | 2024-09-26 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 598be4db-984b-339a-850d-0375c031f111 | -7.36211 | -44.09296 | 2024-09-26 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 640a94e1-ca9a-34b8-ac43-aee03dffdc38 | -7.36099 | -44.09332 | 2024-09-26 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7de829ab-d848-3823-a8ee-ed1f3e780c22 | -7.20572 | -44.09307 | 2024-09-26 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f6bc471a-6d5e-31dc-a560-6fd25d5bb689 | -7.20221 | -44.09251 | 2024-09-26 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2311de34-6da4-34b4-829a-68c358952dd9 | -7.1952 | -44.0914 | 2024-09-26 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfa080df-8dea-3917-9ab8-ec55f26552f6 | -7.07493 | -44.1619 | 2024-09-26 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81669f22-e446-3f7f-a6ae-88dae9fc4fb1 | -7.07076 | -44.16532 | 2024-09-26 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 976fe8fb-beaf-3c15-81ad-29b557fd964a | -7.06723 | -44.16478 | 2024-09-26 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2d715aa-365e-3d3e-8359-e8a7d21cb441 | -6.70216 | -43.97932 | 2024-09-26 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9edd708-3661-3782-9e7b-f4bd65cc5636 | -6.88591 | -44.30094 | 2024-09-26 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f627b239-8d17-34ba-acfa-4f50f747e44a | -6.55376 | -44.1591 | 2024-09-26 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e9b3320-a65f-36b8-a846-b203a948faac | -7.31694 | -44.74524 | 2024-09-26 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33731dcb-73e2-3e20-8982-b736a61fbfb8 | -7.31265 | -44.74883 | 2024-09-26 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e95ba5e0-2e2c-3a43-a425-3ae2425b4dbb | -7.30835 | -44.75245 | 2024-09-26 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3637d8e2-5b2d-3784-9159-a6f4a89a03cb | -7.22297 | -44.79123 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8a3a059-fa95-3b48-a1d9-8d323d58f9e7 | -7.22229 | -44.79546 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14cc5412-de33-386d-aaec-23924a72a4e1 | -7.21935 | -44.79064 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de3d5aa2-af79-3032-8c28-6cc6e3f9a864 | -7.21573 | -44.79006 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5d3121c-aabc-3067-a3b3-0aac5eb4ea4c | -7.12686 | -44.83187 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7ced1e33-3465-35a8-bb87-26321b09eb38 | -7.12623 | -44.83342 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ca90c658-9a73-352a-9ead-e9e42918b2f5 | -6.78657 | -44.73364 | 2024-09-26 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13c2f5b3-5882-344a-a39c-dca83e5f9c64 | -6.78435 | -44.72439 | 2024-09-26 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a3e849f-e1fe-3ab6-a171-92938e02eb16 | -6.78365 | -44.7287 | 2024-09-26 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7f7c90b-c380-3316-926d-30e80b2b32ed | -6.78294 | -44.73302 | 2024-09-26 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92708cd7-788e-303f-be07-5a4af97d9ae2 | -6.78002 | -44.7281 | 2024-09-26 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cb2faa0-491a-37e5-975d-3dbd35714c68 | -6.77932 | -44.73241 | 2024-09-26 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97b9745e-afa2-3020-861d-c63c8451702f | -6.67566 | -44.65659 | 2024-09-26 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a85348a2-b87b-3b32-9908-3db420a3439d | -6.67498 | -44.6608 | 2024-09-26 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3273e1be-2ab9-307c-8923-2e2a8dc63041 | -6.57828 | -44.92914 | 2024-09-26 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34c83b72-6cf9-33e7-b049-f9b938a673ea | -6.5751 | -44.93008 | 2024-09-26 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58630fba-d492-3164-a3be-1ed4f4ad3538 | -6.57386 | -44.93294 | 2024-09-26 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf539104-add5-35da-945f-997d5d5cc4f9 | -7.8435 | -44.91561 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d75d8229-f8a6-3d8d-bb79-cd9e3baa05b3 | -7.8226 | -45.3583 | 2024-09-26 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe37a5c7-d296-31ea-8f73-d726f585eecd | -7.80542 | -45.35694 | 2024-09-26 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b011717b-2ce7-3224-9c8d-b102d06328c1 | -7.80409 | -45.35515 | 2024-09-26 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e2f70c3-19fc-37d8-8c23-202638776447 | -7.78418 | -44.91469 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c7d9511-308c-3c7b-9121-e0fa23b7c141 | -7.75876 | -44.70196 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c4e36bf-5f08-35a5-b902-995f987eec3d | -7.75584 | -44.6973 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a52e22ec-f8c0-3dbf-bc50-6eb7a607b906 | -7.68218 | -44.63976 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 000f8ec7-1f5b-3e1c-9d38-a8f0c308159a | -7.68153 | -44.64378 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51dd8a6f-86d3-3027-945c-bfd93f6005dd | -7.4299 | -45.17405 | 2024-09-26 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e66db7cc-2cb6-3499-8bdd-8140a0719917 | -7.42028 | -45.16359 | 2024-09-26 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75947a83-2be4-3eb8-9e98-244be58982dc | -7.41956 | -45.16792 | 2024-09-26 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 243cd94d-6229-3023-b29f-a7cf96d531ba | -8.62106 | -44.05849 | 2024-09-26 04:06:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b820b3d1-a289-31b7-a002-cd3d998c3b0d | -8.55702 | -44.06782 | 2024-09-26 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33761dad-3abc-34da-a2a9-c19ff8d1f9f7 | -8.55358 | -44.06715 | 2024-09-26 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 31403932-2f02-38a1-a788-a180be7938c7 | -9.20323 | -45.69004 | 2024-09-26 04:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43a98bfb-0f0d-39c9-b03b-e1ef18866378 | -8.37869 | -45.39689 | 2024-09-26 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0e38d45-5725-39c0-8d8a-d7491914bcf2 | -8.37498 | -45.39639 | 2024-09-26 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07762de2-c4b8-3218-afcd-5aa3c8a64f24 | -8.26358 | -44.8477 | 2024-09-26 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe554b5b-9ed2-383c-87e6-24aa9c052520 | -8.23641 | -44.85588 | 2024-09-26 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aae18e54-3813-3ef1-83ed-29aaa46f26c0 | -8.70246 | -44.80155 | 2024-09-26 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README61.md)
