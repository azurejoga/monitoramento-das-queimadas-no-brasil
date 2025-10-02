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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb9b46ee-f8b0-32ef-b760-f5b340c19b23 | -11.81602 | -47.58689 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4c711938-64a3-3dde-a44b-56f73e558d51 | -8.89939 | -46.61248 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fccf8868-e0b0-3e28-baef-68676160f4e6 | -11.47628 | -44.98633 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 689e90b1-3a08-3fe8-aa6f-112cb926c08e | -12.79556 | -46.85331 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e18021c-bcab-3d82-b905-5d6267950b78 | -11.42244 | -43.49731 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddff8ddc-f66f-35bf-bcc2-3b65079af1f8 | -9.7731 | -46.21889 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0f9752f-35e9-3580-bbf2-b9bb7fae69c0 | -9.71219 | -48.94874 | 2025-10-02 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fd7e597-1540-3553-97ff-1d7987b6ac81 | -11.48536 | -43.50396 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f11649bf-0bbd-3a23-a8de-f5d5016adfb8 | -11.47245 | -45.00921 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74507f7e-3286-3931-899d-2954158b41c9 | -10.2871 | -44.32417 | 2025-10-02 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bb47df0-840d-3313-b6e5-377747da565d | -11.80334 | -47.57554 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39c798db-119a-386e-8dca-d2fab78bb3dd | -9.84361 | -49.95919 | 2025-10-02 04:02:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c2ae701-15b4-3fb2-ad97-c398b82a4aaf | -10.25931 | -50.31672 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f851790b-e1eb-367e-b2f8-360425652957 | -11.48716 | -43.21297 | 2025-10-02 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d7f0379e-75b3-3faf-aa6b-b912f3f18f3a | -8.5774 | -49.60318 | 2025-10-02 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5c073a8-0b69-3ff8-81ff-4d064eefffe5 | -6.10143 | -43.4457 | 2025-10-02 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 36a912c1-63fe-3249-a071-e28d5815fd21 | -6.5494 | -45.22168 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98e40f3c-7d21-3862-8d45-8a5ba3c5b5ea | -11.49228 | -43.50513 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bf5ae79-6947-3a0c-86b8-9d7fe5546796 | -7.05214 | -43.27805 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 64d54058-d862-37fe-97f5-61b0208fed63 | -10.69382 | -48.57908 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e43aff9b-d3c9-3880-98d9-e7d2142e6546 | -10.24665 | -50.32505 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 28646532-f7b4-3dca-b2fc-1e6488f038eb | -6.29173 | -42.48109 | 2025-10-02 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ff63d3a9-6766-3db2-9a31-368f28cb2c3f | -6.69384 | -42.82288 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1f7ea782-9878-3472-ac29-6e4506dd2c00 | -11.37836 | -45.04377 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee5eb5a8-e69c-36b3-9b77-83c704a2f4d0 | -11.00129 | -46.54571 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c783a732-12f2-35e7-8969-3caf191c7dd7 | -9.93567 | -43.71863 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a1718376-656d-3a66-bbfc-e8de07d2ec29 | -5.93477 | -43.29404 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f9b85ba8-19ad-391b-8831-b5410bd354be | -5.63741 | -45.96339 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 590dfeb6-f4c9-3f32-aa88-fa4d2775812b | -11.442 | -43.87788 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87fa7212-260c-3c6c-ba73-549e59c40ba0 | -11.58333 | -47.64339 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4587c23-e370-39ea-bc97-939ac876a0e7 | -12.0657 | -47.98244 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24f0d2a3-11a6-3eaf-a06f-2bc19f543f85 | -11.13912 | -43.38317 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 84714ccd-0abe-3375-a111-d0c443364cfa | -10.22859 | -50.33241 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2f8874b7-8db0-3bb0-8ccf-003e564220e5 | -12.26428 | -47.81535 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c8313641-9cb6-3481-b014-a01b0b95c1d0 | -11.46437 | -44.96616 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 341946e4-ae6b-3bdf-ab4b-fddd851d286b | -10.10637 | -45.67362 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 575a5836-2790-3785-9b25-ec95e01b878f | -11.47479 | -44.99523 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 535ca6b5-23fc-3086-ab2f-ff935ab4f1ea | -10.23788 | -50.31271 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 656b2003-542f-3041-851c-a8d27b92d086 | -12.86468 | -47.00879 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c7d5aad1-ea9a-3bc1-bbde-a61a3e4ac27b | -10.32652 | -45.2557 | 2025-10-02 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f5c1752-d891-3c42-b123-1386e287cf27 | -11.67627 | -45.32468 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83f47a02-5374-307f-af09-653af18ade55 | -9.9511 | -43.57991 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6022fda4-8e9d-3415-a1f3-17b1ed0e1b54 | -7.00638 | -44.50304 | 2025-10-02 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 128c7f95-b51d-36e1-bb8d-64b63d0d0cfb | -10.22371 | -48.22825 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5bc3e0ba-efb3-376f-91e7-3c4e1572a1c0 | -9.92521 | -43.73795 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 057a4913-ace2-318e-85bb-909230656340 | -11.47401 | -44.97702 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8bd775e6-8385-37bb-b195-c7a90f384795 | -9.92924 | -43.71335 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 01cbe3cb-a011-33a1-b340-397fce9d21ee | -10.95775 | -44.31543 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c302f956-469c-3a05-9afe-047a2467e4b6 | -9.93298 | -43.73504 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 159.4 |
| cfd0dbbc-d059-3659-ba27-3da7dd0a0eda | -7.78937 | -50.21876 | 2025-10-02 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed488d07-cff2-37df-8ed4-c5f15a29021e | -6.23824 | -45.33226 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e0fb311e-977d-30fe-9a51-756fdf4ff8a9 | -9.84501 | -49.95565 | 2025-10-02 04:02:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed1a30e3-906b-38fb-a2ee-188405bed76b | -12.8869 | -46.90596 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b00ec1b5-07d0-3d49-ab50-45b7fc2e8649 | -6.2243 | -42.96587 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a109562f-e11c-3085-8700-903d090a3eaf | -11.15879 | -47.40245 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4e82b05-9a10-3e9d-8459-9c8fac1e8348 | -6.96558 | -45.33392 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3eb50591-ea05-34e8-93fe-892d98dc736a | -6.04416 | -42.44341 | 2025-10-02 04:02:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7425203b-b158-37e2-89a3-1718d1817d86 | -11.82992 | -44.99908 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e52d5c7-9826-34c9-a617-5f7c199160b8 | -11.00893 | -46.57434 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fe5adec-3d53-307a-bef6-0bf87c822998 | -12.87394 | -47.01992 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41f95079-55b3-3ca8-9ed5-2e92c082bafe | -9.93613 | -43.69355 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20a8896f-e999-35c6-a9b4-dfb11421cf88 | -9.94653 | -43.67447 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9ca6c60-ca02-3dd5-bfff-a0047e963aed | -9.9091 | -43.68076 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dc31ee7-f822-34eb-b7b5-325e16bae8b1 | -10.13333 | -45.68242 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c5ac3aee-2c2c-32a6-8611-7a8d1a21aa6c | -10.42269 | -48.30346 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b65c8f95-dd99-35c6-bafe-64443efd22b3 | -11.41833 | -43.50061 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e4e70f4-cfa8-38af-b248-c4a6f92fbb04 | -6.32602 | -43.89282 | 2025-10-02 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f79133ae-2c95-3ac0-8294-64f4bd45d4b2 | -12.08469 | -44.91777 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dea0adc-4bdd-3d70-8e1b-f3e5a0277d60 | -11.17241 | -47.2741 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bcd7ee84-dc51-340e-8efa-7a5fe57f16b4 | -10.85979 | -45.41518 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c245cdf7-0ede-3674-91d1-5a3f5b75bf3a | -10.26616 | -50.33945 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bd40732d-03bd-3e84-98a0-8ebd82545675 | -10.99305 | -46.52819 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 003054bd-ea05-3231-a14a-5be2a2d7e032 | -11.57715 | -47.02747 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5822fdcb-0971-3be6-a4e8-bf6023806fc7 | -11.13287 | -43.37808 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93311104-78d0-35f3-96f9-1f04cac150b9 | -12.11958 | -43.43023 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3e4a3ca-772f-37f8-ad65-3c5b2574431f | -6.78039 | -45.59359 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 779cfed8-5f05-3225-87f6-c0ecff1318d6 | -11.46066 | -44.96551 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 377ae3a3-3c9b-343f-996c-a0d59e7e4066 | -11.66606 | -44.27878 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50682221-306b-374a-95ef-569e13bb5758 | -11.94762 | -43.9189 | 2025-10-02 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c43976f6-e179-3785-aaa1-03f62c8e6c31 | -6.26832 | -44.05778 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4b736ca-19dd-3bda-aaa1-dc12a99e99f2 | -12.88948 | -46.93461 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b39d2eda-d2f4-348f-ae5e-ef0aca66a693 | -6.78513 | -45.59069 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f988bfa-0df2-35e9-97c5-9e218cd7c464 | -9.91398 | -43.67324 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 586899e2-ba43-36df-abe0-0ccb30e619c7 | -11.67366 | -47.4912 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9dfc26c-cbf7-34d6-98fe-61c67c3020de | -11.81704 | -45.02953 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc900a12-ed28-3e36-9c7e-91658d2bef89 | -9.93679 | -43.68949 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eea2785-8c74-3c04-8f15-39d0156e386e | -9.94342 | -43.71576 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e40b9bfe-b977-38d5-b3eb-a955f54ce905 | -6.04129 | -42.43904 | 2025-10-02 04:02:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0313cfca-011b-3d58-ba6a-d68f314fba2d | -11.46757 | -45.1304 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2c14795-d8f3-3c71-bb8a-2c1c76489e8d | -7.60679 | -45.40584 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62803f4a-ca30-3676-81db-b57131e9c0b5 | -7.05529 | -43.23592 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8408f67b-b2c7-3e78-86d9-0338d388cf78 | -11.80855 | -44.99048 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df69bf9e-5b2e-33a6-8338-948c9f3a756c | -12.82212 | -47.05717 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 03070a6a-5dcf-32b7-bdb3-c383dc282a09 | -12.31245 | -46.88325 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10ff97eb-4aba-3d0c-bdab-164e438a7e91 | -12.84051 | -46.95365 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8304ecf4-96e9-31ef-8942-f1c0eb94bd06 | -10.84839 | -45.38905 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 716634f7-3058-315d-bfaa-549314619eac | -9.94676 | -43.69535 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cd4800c-beda-3ee7-a43f-b7e584726204 | -6.88085 | -39.27309 | 2025-10-02 04:02:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7806ba51-0dd2-3884-b6da-8e7be5f6eb0c | -11.91332 | -46.74806 | 2025-10-02 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9650388e-45b6-337d-ae76-4e17d87d0ff0 | -11.87442 | -49.91478 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
