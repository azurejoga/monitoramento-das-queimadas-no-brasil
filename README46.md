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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2431f1b4-5ac3-333b-a2e2-901e5db26e5b | -8.35235 | -44.09214 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5ed1d260-ac99-3d43-b4ef-eb555cb22563 | -8.35203 | -44.09261 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 924c8943-b693-31ad-8706-ee447283e8d2 | -8.35174 | -44.0958 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c41dad3f-2329-3e42-944c-229845c93ad7 | -8.35113 | -44.09945 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 552e905b-fa52-3932-82dc-bf650f16993b | -8.35076 | -44.09991 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb26b14e-d13d-3142-928f-2a7b12d5320c | -8.34827 | -44.09146 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 651c69ea-1236-3c01-9763-ebe35a01785e | -8.34765 | -44.09512 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d96c38df-0cf7-3154-8bd3-4fa37e4c11cc | -8.33887 | -44.09743 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51a36bbb-b681-3994-8d3d-3af0c7cbd1df | -8.33417 | -44.10043 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa07738d-4379-3883-ab95-ea325321248b | -8.32485 | -44.15579 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bd08463f-7a7b-345c-86b0-e32d149a203a | -8.29771 | -44.16661 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec8b78df-82a1-3fe0-863c-1899cf5d077f | -9.97152 | -45.47121 | 2024-10-10 03:55:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94214bf7-e46c-395a-8f9b-4400ab1b1920 | -9.97029 | -45.47224 | 2024-10-10 03:55:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b866bca7-04c7-37f6-894e-9f9be258068c | -9.71169 | -45.47684 | 2024-10-10 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a5ff7ae-be29-3091-80df-82547b636adf | -9.55954 | -44.44608 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89ad13f6-0d68-3486-b90b-d949cfb62815 | -9.55801 | -44.43048 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 56e35862-6ad4-3eee-a3e7-232fa0976e04 | -9.55546 | -44.44534 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d3cebf8-baf7-3922-890c-39a908afd2ed | -9.54164 | -44.4277 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 455f93c6-99cb-3292-95c4-7ad748ca2c4e | -9.53691 | -44.43068 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6800563b-f4cf-364c-89f8-9a672e12c592 | -9.53282 | -44.42997 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3b6d95a-6845-3e6e-af41-d8e02f2d53b6 | -9.53217 | -44.43371 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f203f43-dcb0-3f1d-9182-eb89f230ad37 | -9.53152 | -44.43746 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fae23630-61c5-353d-98cc-851d60ff9933 | -9.52742 | -44.43677 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 402ef440-c637-3637-8de2-3780a3d036d4 | -9.52332 | -44.43609 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65b67fd1-6c90-3e66-9056-08b74a77931f | -9.52267 | -44.43984 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efdc25f6-1f53-304f-82ad-e959e4448ffb | -10.51333 | -44.85397 | 2024-10-10 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd52825a-4e3e-36c2-82a9-2acc94626f39 | -10.51141 | -44.85286 | 2024-10-10 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| add43814-a131-36a4-a4e3-c69c92ede39f | -10.5092 | -44.85323 | 2024-10-10 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6d3518c-ddbd-34f6-8aee-513873b72b01 | -10.50727 | -44.85211 | 2024-10-10 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97596d4b-2c49-3a09-9735-f7a8d1b5b4f7 | -10.44732 | -45.12548 | 2024-10-10 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d1fde40-7869-334d-8f3e-a2dd79e9f70a | -10.44243 | -45.12861 | 2024-10-10 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6813e1e3-105f-33a3-8013-5334d65d5fef | -10.44082 | -45.26439 | 2024-10-10 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb1bea9b-1b6b-324d-a0fe-b6f44fa7c055 | -10.12402 | -45.20985 | 2024-10-10 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cc1d8f0b-5b8c-3ab0-9733-804c93f87316 | -10.12303 | -45.20959 | 2024-10-10 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| e94921bf-d486-3c5c-8291-8197fbb31d22 | -10.11979 | -45.20886 | 2024-10-10 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7280ab8b-9f26-3d75-ad95-d977d092da41 | -10.11881 | -45.20862 | 2024-10-10 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7dfab0fc-f8ec-3465-9357-a50b39b992e9 | -10.7612 | -44.99844 | 2024-10-10 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc94ff7d-db6e-373a-80c4-02f1f14bf0a4 | -10.70077 | -45.00023 | 2024-10-10 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dcc3b1d-c47b-399f-8381-e93d085adf6a | -10.69933 | -45.00048 | 2024-10-10 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cd873f9-815f-3d81-87e1-eb79e8b8c150 | -10.6002 | -44.77105 | 2024-10-10 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8e34b3fb-ce73-3369-951f-02eac215eb50 | -10.59955 | -44.77481 | 2024-10-10 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d534365d-1691-317b-80fe-5a8e8f610502 | -10.5989 | -44.77858 | 2024-10-10 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daf9a11c-9bd3-38ac-80c9-1cf1025f2f66 | -11.78376 | -45.20446 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6539a806-2596-3e33-8393-b589dc86120b | -11.78308 | -45.20829 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f040aca-319d-3b7e-a584-6643fe9a57a5 | -11.66897 | -44.88483 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dabb860-e6f6-3747-b253-23ea352c3de1 | -11.55602 | -45.02996 | 2024-10-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c490874-eacd-354b-bc6c-d86470678485 | -11.13047 | -44.94927 | 2024-10-10 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cabdee0-e70e-3541-8e36-e79291f683fc | -11.14271 | -45.37902 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfeae505-4f90-35f2-b441-eee1856fb9b2 | -11.13848 | -45.37826 | 2024-10-10 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5d492e8-81c5-3c68-bbc1-c13e1e4828ab | -4.08007 | -51.03363 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e3606b32-c920-3c80-8df7-3b913bdcdf01 | -3.84909 | -51.25753 | 2024-10-10 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6eb0768a-680f-311e-8f43-e5560612f61e | -3.84796 | -51.25737 | 2024-10-10 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82997e05-53b4-3f98-9fe6-b499edc09401 | -3.84213 | -51.25625 | 2024-10-10 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2d09636-e492-3310-b47a-5d52c97a0a90 | -3.84102 | -51.26263 | 2024-10-10 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1004b3c-f417-39eb-beaa-4d56099c7c76 | -3.841 | -51.25608 | 2024-10-10 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6b052e74-fe98-3e1c-af00-9cc3fc49dfab | -3.68993 | -51.07062 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2826c416-1a64-3c8e-a607-77ccc58dc1ca | -3.68977 | -51.07066 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 65982896-d353-329b-a90d-ac093f19c72b | -3.68785 | -51.1243 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| a7a65f4d-0e9d-3b71-abb2-5e697d5116be | -3.68736 | -51.1242 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 830a68d4-cf5d-3769-9557-f6b370125c20 | -3.68299 | -51.06954 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c8f7b582-4184-3e84-917d-3f71cb1d7183 | -3.68283 | -51.06962 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 617d918e-80fd-3901-adb5-012afeacf8be | -3.68202 | -51.11665 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f4276b32-3597-3bb7-ba5f-5bcbabe5f7cf | -3.68189 | -51.07596 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b89c709a-75c6-35bf-b3c9-886cbd0ae64d | -3.68157 | -51.11658 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ada44080-5042-30e5-99aa-3d5f69bbf387 | -3.68087 | -51.12333 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 16cf4770-cfcc-342b-85be-888efc3329b6 | -3.68038 | -51.12325 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ac5e8f91-566b-3ea1-93af-1f17cf2585f6 | -8.86425 | -52.99263 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 741ebda2-8ce7-33d8-a02a-2fef8c77c2ba | -5.08769 | -45.17086 | 2024-10-10 03:55:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30d1e23a-b4b9-359c-b2f3-f1690b515551 | -4.96508 | -45.03037 | 2024-10-10 03:55:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc83f5c4-3dea-3346-8a08-fbce258682e8 | -4.92923 | -45.67286 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1369cb90-39fe-393b-82e4-f0b03ca5f708 | -4.9059 | -45.93732 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d18a13a-879f-313d-b3b0-ce1b902cc213 | -4.88394 | -45.33665 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57b54e90-cc6a-3230-b1df-448b3d6d7d13 | -4.9472 | -45.50795 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57187145-44a8-3cd6-baf7-48454c4bf3c1 | -4.93056 | -45.43274 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbc1ce23-25ff-37b6-ba5f-78006692d987 | -4.90314 | -45.93862 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35f0c7e9-6f29-3ce3-87cd-d19048f345a2 | -4.89103 | -45.69682 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e7069d4-4d4d-3fb0-b5c0-42165df1fe6e | -4.89017 | -45.70191 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eea489b-1a29-36f8-b070-7456acbb773b | -4.88535 | -45.70114 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b8d22ef-8df5-3449-9f75-409b383665b4 | -4.8822 | -45.33433 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4dcab37c-7808-332e-bb7e-5c12b4de539f | -4.86758 | -45.80648 | 2024-10-10 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 53b1bf43-7f8f-3dfb-aff3-89db282d786c | -4.83883 | -45.4206 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9a7bc255-8a26-39d9-8bf4-07815455168d | -4.72654 | -45.67729 | 2024-10-10 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d526b034-b8a2-369e-aa60-678cd764664d | -4.72234 | -45.67834 | 2024-10-10 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22edef4a-5cf8-34a6-ad66-026e899fb18e | -4.68695 | -45.81974 | 2024-10-10 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9dd5d92-677e-3744-a2ca-80026dcaf669 | -4.49586 | -45.70989 | 2024-10-10 03:55:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dda1c683-0df0-3f1f-884f-e60897d41ee0 | -4.49496 | -45.71535 | 2024-10-10 03:55:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 269184c3-9067-3149-8006-117fc1e96617 | -4.46528 | -45.89567 | 2024-10-10 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab8bc2c4-6d17-39a6-8912-87ab6c7d8691 | -4.46436 | -45.90123 | 2024-10-10 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 862c3444-1521-3e18-8b51-9be66f12fb95 | -4.46193 | -45.89716 | 2024-10-10 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eb5c60dc-1fc6-334d-b16f-8a57e7f6a012 | -4.72174 | -45.67641 | 2024-10-10 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 148a4761-9a02-3101-9d91-35ca4b57d24a | -4.494 | -45.71162 | 2024-10-10 03:55:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d56c713b-a911-34dc-a73c-71991de8d3fa | -5.70726 | -46.44337 | 2024-10-10 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21ef7b5d-b88e-3590-8459-0c47410f3de3 | -5.70176 | -46.44537 | 2024-10-10 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51467bdb-53c8-3617-8513-4fb38fdf52d9 | -5.62998 | -44.94804 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ed70459-790a-36d0-a31b-135fc1cea833 | -5.58132 | -46.31023 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dc6887fd-eb97-34a6-9e79-74fe5907653c | -5.58057 | -46.31448 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87268f0b-b1c5-3f0d-96e0-5b3513d0a170 | -5.57959 | -46.31429 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95e80d04-3f71-3794-a1e5-723f371e3df8 | -5.55037 | -46.30581 | 2024-10-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ee47f52-e9e2-3a78-8859-79ba1b52e0a4 | -5.50072 | -45.37746 | 2024-10-10 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e1161b3-c61b-3b3d-bc39-ee66ca118ff1 | -5.42956 | -45.09966 | 2024-10-10 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README47.md)
