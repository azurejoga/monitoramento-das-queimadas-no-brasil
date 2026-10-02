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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2234c5c0-36f6-385b-874a-5ef56f39fd16 | -12.76145 | -43.71213 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37c44dcb-2c7b-3173-a9a0-e96f796c3975 | -11.36382 | -40.05973 | 2026-10-02 15:54:00 | NOAA-21 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| c245a00d-afbe-3fed-af82-09dbafd39bcb | -9.79773 | -44.8037 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 21ff767d-c914-3f5a-a2b7-58c837d6d15a | -11.70674 | -43.51738 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 739ef7b1-d0da-3be0-b5e2-1aed2a904800 | -9.80303 | -44.80299 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6e76fd66-34e0-39b9-85e8-5027821c2b16 | -11.11945 | -44.60725 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 86f1bbaa-fba6-371d-8805-805a96011d21 | -11.99008 | -40.58386 | 2026-10-02 15:54:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 8a2c2874-a7bd-3815-869a-2abe1664a7eb | -11.70445 | -43.61952 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| eb473467-1d4e-3d6b-ac7e-2de3fd4b516f | -8.86756 | -40.87069 | 2026-10-02 15:54:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| add73c3b-752e-37f5-9f20-48d5e6ba80c2 | -7.03386 | -34.83785 | 2026-10-02 15:54:00 | NOAA-21 | CABEDELO | PARAÍBA | Brasil | 2503209 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| c8be0300-c8d0-37f7-8afb-9b3f511a7529 | -12.4983 | -44.13521 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 23b56de7-fe44-3f60-af51-be1e9d1edbc2 | -11.2683 | -43.51382 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b3d436b4-047d-3804-b7c1-dae79b918590 | -12.13675 | -38.70126 | 2026-10-02 15:54:00 | NOAA-21 | IRARÁ | BAHIA | Brasil | 2914505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 3ca20567-ffdb-30bd-91a6-aa3db91f38e7 | -11.64816 | -43.57587 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3e4d6b0e-428b-3f2d-8509-edd0a4c8d95e | -10.14275 | -45.11772 | 2026-10-02 15:54:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b767beb7-bc0b-3fb1-be73-2a8046aacf19 | -9.84324 | -44.82889 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4a26350d-6cff-34df-ada0-86dd9aefc281 | -8.81031 | -45.81646 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| bd4b2d15-d809-36fc-a0a3-e26808f56392 | -11.16172 | -44.59879 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d78c7768-7059-3143-b809-74bb3487afaa | -13.10046 | -43.49471 | 2026-10-02 15:54:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c869ce9e-f83f-342b-bd45-9cc63fc2fb70 | -11.31733 | -44.26528 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 561e1668-bd01-35a9-8b79-a7cb59ff3b68 | -8.24298 | -45.43176 | 2026-10-02 15:54:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4603ee31-616e-397d-bf33-5101f2c0f5e8 | -12.53525 | -43.08157 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 43bbe95b-097c-35ea-be1b-1c2d20693c1f | -11.28032 | -43.57003 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d7a0ff73-e29b-3d09-aba4-5303fb8beb6d | -11.1478 | -44.61736 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e3ee5f47-edaf-34d9-87ce-fad8e194cafd | -13.34355 | -43.84107 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| f0e57d07-4561-3f3a-9a69-c74c663cfec7 | -11.46666 | -43.50865 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| cc2293c7-4930-318f-add8-648e4db4b51a | -7.70041 | -35.12362 | 2026-10-02 15:54:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 4e9b0d3d-a4af-3fc5-b9c8-43c770dd434e | -11.36365 | -43.43271 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 85bd982e-0a3f-35a1-bb15-9b8844cd2b24 | -11.80888 | -43.55573 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3f9d8b15-0e3b-3163-92ee-61ec56a7d148 | -8.97347 | -41.14415 | 2026-10-02 15:54:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d9bf28a8-908b-3499-891b-fafe92f20164 | -11.8096 | -43.56282 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| a8ec9296-a157-36f7-a8d6-8d09bf69b5af | -11.70169 | -43.59689 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a114f9b3-0dde-3a10-8910-570d28a8ae1d | -11.67366 | -43.61608 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| ad56eb7b-eb62-3263-9c75-1acdb7ea8a7e | -12.85945 | -43.81079 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ed7a209a-f322-3455-a094-452f59edf83d | -11.76154 | -43.54552 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cd903614-c2f5-396b-b5c3-d67f6ab0c754 | -11.47465 | -43.40981 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 052b4fda-1d5e-37ca-828a-3dc09b741c1e | -11.31814 | -44.27173 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 980f25b0-0119-365b-9e40-a8d0eec73be7 | -13.35554 | -43.84452 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 8e9bf62f-8c79-3915-ba78-145dc2be08b5 | -13.35145 | -43.8549 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 26897802-e9df-3c34-a1e6-57e2dd11d9c0 | -12.5052 | -44.14774 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| b77e937f-76be-32ff-9ad4-8aa70bc04d99 | -11.85088 | -44.7496 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 56ce17d3-520b-3fa2-870c-2cc3f3dc7e31 | -13.34738 | -43.86552 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| a4cd8dfb-3951-3116-a9fa-5cdde6d9404e | -11.76655 | -43.54489 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| e466a122-7614-3751-b7de-4ae1cb32642c | -11.45199 | -43.40234 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f71e0028-257b-31c4-9fa8-b452b08f941a | -12.76854 | -43.27754 | 2026-10-02 15:54:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eabdaa0b-e922-38dc-87d1-9c9a9afb135b | -12.25959 | -42.15319 | 2026-10-02 15:54:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 1e00cdb6-3aa2-39a7-8fe2-45ed2302659d | -9.80346 | -44.8063 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d498bf4-7f18-3e51-8125-356a129af693 | -12.74796 | -40.23077 | 2026-10-02 15:54:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 23cd08a2-16ac-3071-87e9-3ac8c356cbe6 | -8.7763 | -45.81753 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ef8ce5b9-8a2a-3a6c-aaf2-71a288d3c4c9 | -12.41256 | -39.47666 | 2026-10-02 15:54:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b480dbdf-414c-33c3-93f7-af0b88188c74 | -11.47604 | -43.4211 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ac0ef571-1450-3793-a69c-dadac1156aa8 | -13.35707 | -43.85756 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 9c7c539d-6704-3d7d-baaf-94237754dc72 | -8.8112 | -45.82344 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 27a91476-36d1-32f9-9a1a-e00e318e4c2e | -12.52831 | -43.10611 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 7e15b8ae-e832-3d0b-8bb9-4fd3a6e56750 | -11.28357 | -44.24981 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 206c9094-0e5b-34b5-857b-51c0e6b24e24 | -11.24794 | -44.31034 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6cefba2c-3ebe-3d60-877e-2830220e310f | -11.8547 | -44.74982 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 693596a7-a667-37c8-931f-67d8283d8a36 | -11.27351 | -43.56237 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e725c462-5e6a-3b8c-b52f-8bf0e43543c0 | -11.41759 | -44.89033 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 938fd865-ac49-39ed-b4ba-588f09bf1f82 | -11.30043 | -44.25751 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6eac34ef-db44-3606-b037-00c849ddfe19 | -11.14486 | -44.59393 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| dc8831c5-62e9-3e88-9e93-d71bcb21a052 | -11.70782 | -43.60379 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 53eb9474-6e7c-3315-9f1e-b6675f1bc24f | -8.7834 | -45.81696 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 47ae3f76-ac88-3447-9740-ef2e2b5d81cd | -11.77694 | -43.54655 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 841c6dc0-0de9-3291-9047-7f4fc444cf70 | -11.61127 | -43.56565 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2874402-2be4-3b53-b6e0-a8b8de5129bb | -11.76685 | -43.5875 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b826282f-956a-33f7-b15e-246b6ca113de | -7.89082 | -43.85485 | 2026-10-02 15:54:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 8ed14468-3310-32b5-a378-0f4372a25548 | -8.57039 | -44.13067 | 2026-10-02 15:54:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| baf4824f-17c1-32f1-8ff9-1ba161771d9c | -12.21434 | -38.99348 | 2026-10-02 15:54:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 34a05fac-03c9-3eeb-923c-27b4ad21b509 | -10.91065 | -43.83568 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5e76654e-f6cd-33a7-b413-40be0c53c34d | -12.64994 | -39.83743 | 2026-10-02 15:54:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| d252c993-05a5-32d3-9afa-56b5eab6466a | -10.30264 | -44.654 | 2026-10-02 15:54:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3d2ff3f2-c39b-3806-943d-0819bc10a232 | -11.85591 | -44.74549 | 2026-10-02 15:54:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 18ca8fee-a66f-3802-8d9b-a8a4278da309 | -11.81034 | -43.56851 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 1cf2220a-329a-3bf5-bf8d-af61327ca7f8 | -11.8139 | -43.55511 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| edb9b4e9-8516-37b0-931c-1475fcebe89b | -11.26678 | -43.5112 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d4ad32f6-6a3c-3673-a593-4a8a8c46b0ca | -11.64988 | -43.54919 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a82a03e6-5712-3975-87c5-5bf88b16088e | -13.34116 | -43.86462 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 659fad8e-2a28-3377-84e8-a8a276ecdee0 | -11.28998 | -44.25876 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b32c8047-a3ac-3d07-b5d4-002688995251 | -9.78623 | -44.79822 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b59ba7f3-e75d-33ec-9e74-79bd11b71b46 | -11.66723 | -41.5801 | 2026-10-02 15:54:00 | NOAA-21 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 7d481869-c817-3df4-8e28-ab3a1806bbfe | -11.46475 | -43.41098 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a8c42ae4-d894-36ec-93bc-b11887f2cb9c | -11.70998 | -43.58128 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ab540311-dafd-3fdb-86fc-69ea624e7edf | -9.18244 | -45.70001 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 170f1494-9414-38d7-bb7e-c5909e494f05 | -11.45841 | -43.40029 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 729e0ab8-6a5f-3013-b66f-44099fb94c4d | -11.80851 | -43.55435 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 0b6d8fc0-e43e-3d0e-8ae5-592e36624dc0 | -13.33654 | -43.86353 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1d32fc19-864e-3a81-9a0e-fd1294899d3c | -11.32678 | -40.34451 | 2026-10-02 15:54:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ba0a55e0-7f3a-3540-96b5-aaf86e7ce05c | -11.12435 | -44.60308 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e41a954c-036e-35e5-962d-69c2d7a6fea3 | -12.77285 | -45.1553 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9b2103cf-cffc-3a66-a938-ac98cf3017c3 | -11.43586 | -40.41233 | 2026-10-02 15:54:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| adde8d43-634d-34be-9f57-eab9f528042c | -11.71481 | -43.62067 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| decc8287-6a4f-3542-bd8c-4d8a9f26a102 | -8.56046 | -44.13222 | 2026-10-02 15:54:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7ffd6e3a-425f-3eb0-802b-704f2523450e | -11.26711 | -44.24527 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 077e50ca-bd18-38a5-8b93-c309c57732e2 | -9.94656 | -43.4566 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 8997280a-ee9b-36c6-b28f-1ea849ab4ac0 | -11.72624 | -43.50716 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b9297a88-b281-34c8-b616-f21e8531cfe8 | -11.72116 | -43.42611 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 92197198-02ed-3cc5-9de0-c2f625950072 | -13.34023 | -43.84961 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 71d4dcf0-e203-3ffb-93ce-fd67133d8878 | -11.69961 | -43.61927 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5bf0f960-4a89-3c47-aa63-c9e76aa38345 | -11.66223 | -43.60649 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README99.md)
