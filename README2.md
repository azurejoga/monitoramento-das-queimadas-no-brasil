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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4584087-6ff5-3f38-bc26-a40b24aba7e2 | -9.86788 | -37.16798 | 2026-02-17 03:04:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c6edaec4-5e6b-32b1-a00a-c7ac09a81437 | 1.0663 | -60.5606 | 2026-02-17 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 4724a7f2-2f1b-34d2-a9d0-f945a423231f | 1.0663 | -60.5606 | 2026-02-17 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4429cbc4-e74b-3fdb-ba2f-9937a8275535 | -4.89148 | -37.24806 | 2026-02-17 03:23:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 15369800-8bae-38a4-b356-ab3fbb2203ca | -6.56547 | -34.99633 | 2026-02-17 03:23:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 68db059b-458b-3ba5-941c-de294bcf9a0e | -4.71597 | -38.4454 | 2026-02-17 03:23:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a3db22d6-09ac-367f-aea5-680732f74650 | -4.89066 | -37.25284 | 2026-02-17 03:23:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9cd01f0c-4806-3890-93ad-bed3b2b6211a | -2.94597 | -39.95184 | 2026-02-17 03:23:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| eb15244c-b88a-3bfd-b24f-3b74d523f620 | -5.55258 | -35.622 | 2026-02-17 03:23:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6f723daf-03d6-343a-8523-0d3a21a09f9c | -5.09064 | -37.60249 | 2026-02-17 03:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| eb091af9-f125-3ac9-a4c0-f59b856567f5 | -4.71647 | -38.44247 | 2026-02-17 03:23:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ba5b5138-f09f-37fc-a178-be62af56863c | -9.8697 | -37.17131 | 2026-02-17 03:25:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 09070b64-9d56-3677-a691-43a85a32630c | -10.99754 | -44.81562 | 2026-02-17 03:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3b4c0ffb-d89e-34dd-8f06-f31c068297a3 | -8.8247 | -35.67429 | 2026-02-17 03:25:00 | NOAA-20 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 231b21c4-29e4-3656-98d1-f6b6e70557d4 | -9.94196 | -37.38216 | 2026-02-17 03:25:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 08521dee-61d9-33bb-b68b-f6e2f2fbf806 | -8.82082 | -35.67352 | 2026-02-17 03:25:00 | NOAA-20 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8f6e9ffa-de0f-37bc-bcb3-70a54f07908d | -9.87038 | -37.16735 | 2026-02-17 03:25:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de4ef4af-7ec9-3e09-a6e5-5bc6cb97f9fb | -8.58125 | -35.73469 | 2026-02-17 03:25:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 107d1e30-c12f-33bc-8c0c-1db61322cca9 | -15.89213 | -43.48225 | 2026-02-17 03:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 32e0e229-90bd-3eb9-8182-203ef56facaf | -16.38778 | -41.04984 | 2026-02-17 03:27:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3dc84897-2a7e-39a6-86d7-852faa1d5d2e | -16.02406 | -41.18646 | 2026-02-17 03:27:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ae0b3b1f-f8f0-3885-ad88-5a6ba8aaf25e | -15.89301 | -43.47808 | 2026-02-17 03:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 998af6fe-983d-3b05-abab-496063a6e95b | -16.60351 | -43.36243 | 2026-02-17 03:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40e5c9fe-02d1-38f8-8c93-52f9543255e9 | -15.16848 | -45.65059 | 2026-02-17 03:27:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da21dc2e-ab2a-3189-beee-5b7b1b10d4ad | -16.6043 | -43.3586 | 2026-02-17 03:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9f7745a-a5f7-394d-8646-48e812254ac8 | -20.1115 | -40.7101 | 2026-02-17 03:27:00 | NOAA-20 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 236029f9-b846-39ef-9cb9-b698be6eae59 | -16.60774 | -43.35801 | 2026-02-17 03:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d4d2d1b-2eb6-3dd3-82af-d5c630aef173 | -15.44362 | -43.64006 | 2026-02-17 03:27:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4efc0592-eaae-30a1-b956-e35aec25e9c9 | -14.84118 | -40.91204 | 2026-02-17 03:27:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 64bad696-7b8b-3444-90e8-00bf2b0c90fb | -15.17099 | -45.64875 | 2026-02-17 03:27:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf110b7f-f366-3103-a250-8c9db4267c62 | -14.84049 | -40.91161 | 2026-02-17 03:27:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 59aad714-a7ed-3939-89ab-2054927be88e | -15.16981 | -45.64457 | 2026-02-17 03:27:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efef73b2-d7ab-3672-bc37-6e45f45883cb | -15.44273 | -43.64436 | 2026-02-17 03:27:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b65438b1-0f56-3b5b-82e1-66cadea307cf | -16.60914 | -43.36344 | 2026-02-17 03:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db225458-08bd-3ad4-bb0f-a856ddfb17eb | -16.0228 | -41.19279 | 2026-02-17 03:27:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ba761bfb-42c0-35ac-a94f-67c6beafe20a | -16.60691 | -43.36185 | 2026-02-17 03:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f29510f-d993-3ad6-bd72-040f77dffda2 | -21.70749 | -48.43646 | 2026-02-17 03:29:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c43d5abd-ec8f-310a-977a-f43637123808 | -22.78593 | -49.3639 | 2026-02-17 03:29:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb07000a-c22e-329b-b1a7-29fa529676cf | -22.78406 | -49.37114 | 2026-02-17 03:29:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3232cda-b9ec-3ef1-94ff-dd5d92524a27 | -2.88483 | -40.17058 | 2026-02-17 04:14:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf1b47c7-ff12-36fd-bc5b-a64045aa96ea | -4.77049 | -39.64193 | 2026-02-17 04:14:00 | NOAA-21 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91f33df3-9e0c-3576-a96d-6cdaa9112f21 | -2.9467 | -39.95287 | 2026-02-17 04:14:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cb36dc62-5253-3c84-865b-a51500fa2597 | -4.89136 | -37.24928 | 2026-02-17 04:14:00 | NOAA-21 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 953f3def-d9ec-3ba9-9bb5-fa9484951450 | -3.09649 | -41.85929 | 2026-02-17 04:14:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd886400-77af-371c-a40a-faeba37c9a95 | -5.0891 | -37.60132 | 2026-02-17 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| afe29edf-7117-314c-bfb5-3b84862d4340 | -5.98627 | -42.37844 | 2026-02-17 04:14:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 286ab546-3d04-3566-a4c1-65ae5ec3f7ca | -4.71701 | -38.4411 | 2026-02-17 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7465962e-1aff-3cf2-a171-3f4117c98324 | -2.9473 | -39.94899 | 2026-02-17 04:14:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 98ee05a0-1ed0-3f33-b628-af7fe3cd400c | -2.5204 | -47.81555 | 2026-02-17 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2fdf5bf-8cda-362f-b9e2-35947aac62ac | -3.09318 | -41.85877 | 2026-02-17 04:14:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ed0a4ff1-094c-38b7-b95b-f3a94205f977 | -4.72087 | -38.44173 | 2026-02-17 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9b7236e6-c053-3ff1-9cf9-a8c134e21184 | -12.2432 | -44.23341 | 2026-02-17 04:16:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 025a6c77-c30e-369f-a230-e90d587a2085 | -11.88259 | -45.29118 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74216294-7f8e-317f-9d3b-767882a039ce | -11.88704 | -45.28461 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cca5d2d-4a48-3d66-a470-f7a6b6ca5229 | -12.2399 | -44.23288 | 2026-02-17 04:16:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22c2ca69-ef8e-3047-ba62-db93ebd09a37 | -9.86977 | -37.17123 | 2026-02-17 04:16:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0fca07e1-7bad-3d57-8930-9142242fec7f | -11.70919 | -44.73188 | 2026-02-17 04:16:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1da7bde4-6041-3fca-93d4-f74d5bc49790 | -9.8704 | -37.1666 | 2026-02-17 04:16:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8fe7e764-b7b7-39ae-8c54-6bf137ec20ca | -12.82485 | -44.82454 | 2026-02-17 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78978080-312b-3ed1-b866-763ff2e978f7 | -11.89036 | -45.28516 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66dda124-7f34-3585-b2a0-b4df10627021 | -9.40904 | -44.53311 | 2026-02-17 04:16:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34be56a6-c0aa-34f4-bc5d-56d52fe7c0b2 | -9.94387 | -37.38435 | 2026-02-17 04:16:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e0d32e4-e131-3222-ad81-48f8d78e2ac1 | -10.93011 | -44.66527 | 2026-02-17 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bd7d5c4-ecf6-32e0-983f-a9835a1b0ce2 | -10.99868 | -44.81337 | 2026-02-17 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e97bbefe-d8ca-380f-84f8-afe533eec977 | -10.62051 | -40.52521 | 2026-02-17 04:16:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5346d1e9-e6df-3a11-b211-4080fbf2870d | -13.54851 | -43.70583 | 2026-02-17 04:16:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e93ed6f-694f-3a40-ad7a-88fa88475e30 | -14.84128 | -40.90567 | 2026-02-17 04:16:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 44652b39-1dee-3c22-9039-48c3268c6f19 | -11.71853 | -44.73699 | 2026-02-17 04:16:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aeb2527-86a2-373a-a025-4651f175f3d5 | -11.85803 | -38.20475 | 2026-02-17 04:16:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e1ed9bd4-7de8-3db6-a06f-2be26442073c | -11.88979 | -45.2887 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a1e9aa3-f971-30e5-a834-033680d06c5c | -11.89149 | -45.27808 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db795f8b-9eaa-3285-b64a-f0c1b21453c8 | -11.17978 | -43.30391 | 2026-02-17 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 07ebf198-e4be-3691-b859-8543f42cf423 | -11.88818 | -45.27753 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cad48d2c-30ec-3511-859e-ddb82df6662b | -12.23936 | -44.23639 | 2026-02-17 04:16:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81c9b05a-d237-32c8-bc5f-fa1aea79e370 | -10.62115 | -40.52083 | 2026-02-17 04:16:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b9d8fe08-f236-305a-92c0-343f99d7082f | -11.88647 | -45.28816 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75a21732-921a-3f85-be93-042d6b42fac4 | -12.8243 | -44.82806 | 2026-02-17 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7616f8c3-4e72-3c07-ad14-2685205ef13a | -11.8859 | -45.29171 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16c5952e-f4ec-396d-ad02-e0c2706465fc | -13.54517 | -43.7053 | 2026-02-17 04:16:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c29c1e45-088b-3f43-aaca-425a46e16b79 | -11.88316 | -45.28762 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5b1dc4b-ca4b-3b4d-ad3b-376725c42e90 | -11.88761 | -45.28107 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6b45b31-335c-360c-930c-1bb28043045b | -11.88922 | -45.29224 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36388fc3-3811-3c0a-a385-e3bf4127c90b | -12.24266 | -44.23692 | 2026-02-17 04:16:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ed00c0f-1278-3ec8-812e-27d83c6139cf | -13.43602 | -48.22312 | 2026-02-17 04:16:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e6246c9-43f9-3da5-92f4-52a6d2c54ab3 | -11.71304 | -44.72892 | 2026-02-17 04:16:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db4d6294-da7e-3dab-baf9-034975226339 | -11.88373 | -45.28408 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47db9e0c-c675-365f-a206-a3fb8b7c5d79 | -11.71249 | -44.73242 | 2026-02-17 04:16:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d93cbaf2-ef36-3675-bbab-0c0de480c88f | -13.43963 | -48.2238 | 2026-02-17 04:16:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38510973-c203-342a-b385-d4df9f5b259c | -12.07441 | -45.34789 | 2026-02-17 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6df15105-20b9-3afe-a04c-3654c96813e5 | -11.70974 | -44.72838 | 2026-02-17 04:16:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f4f39f7-8b68-3fca-bc59-6f3a3cd8220f | -14.84063 | -40.9104 | 2026-02-17 04:16:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8216a8bd-c760-3946-88f5-d21f5026b1a4 | -18.97893 | -52.93034 | 2026-02-17 04:18:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cf02c55e-38e9-3052-ab5c-5580d718e74c | -17.31155 | -44.92931 | 2026-02-17 04:18:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c407cad-0a5d-39a7-baac-7b86379e9d0e | -15.17227 | -45.64643 | 2026-02-17 04:18:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d305bf15-8576-3cba-9998-9b40314fa9d0 | -16.02671 | -41.19043 | 2026-02-17 04:18:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 90b62a0e-f783-3f6d-b775-28ff2dccb1ea | -15.4439 | -43.64051 | 2026-02-17 04:18:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ab3f39d3-2676-34a3-b624-dd441ecb56d8 | -16.60705 | -43.35672 | 2026-02-17 04:18:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c59aa70a-ac0c-3c50-8b67-bf12219c4b30 | -15.44051 | -43.63997 | 2026-02-17 04:18:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 59f7c829-3c48-3eb9-8de0-ab03da017748 | -15.20786 | -43.1775 | 2026-02-17 04:18:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7bd2c92e-bcc6-3a98-8baf-35198845a3de | -16.60647 | -43.36065 | 2026-02-17 04:18:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
