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
| 853919a2-ed39-3153-b110-e17709cdd5a4 | -5.47928 | -39.42437 | 2024-12-25 03:53:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 85bc6910-8c87-3f12-97b1-d113b3e6b53b | -4.20314 | -44.54443 | 2024-12-25 03:53:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9303d01f-eb10-3c4b-8394-52fe8e692584 | -5.07067 | -37.71618 | 2024-12-25 03:53:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1cd4adc4-0d29-3999-a1de-15bdcbc1cca7 | -3.76508 | -47.13953 | 2024-12-25 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc4d28c5-4745-3803-a659-5aa7b9f69555 | -5.48593 | -39.66399 | 2024-12-25 03:53:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28d5993f-9943-31c7-85a7-36ccc1cc5060 | -2.07293 | -45.17371 | 2024-12-25 03:53:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef142c34-7af3-301e-8d04-2d8575fe7ebe | -3.78974 | -41.61106 | 2024-12-25 03:53:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05b360f7-4a40-3da6-8c7f-369447e27f4d | -3.92582 | -47.19445 | 2024-12-25 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd4b2af-a11d-3d55-b93f-26b8d10cad93 | -5.48199 | -39.66697 | 2024-12-25 03:53:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c7eef87c-ffce-3180-9d9d-c26911f90668 | -3.79348 | -41.61168 | 2024-12-25 03:53:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce610b46-b5a8-37e8-8d94-fd1c300e4a40 | -2.07779 | -45.17452 | 2024-12-25 03:53:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30c552fb-d7fb-342d-a5cf-e4ac3915cb7e | -4.20037 | -44.54138 | 2024-12-25 03:53:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11fe0a86-f282-3ab5-b385-c090aff4f66a | -3.786 | -41.61044 | 2024-12-25 03:53:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe8f3493-6fc0-359d-b56a-8627949696f3 | -5.48255 | -39.66346 | 2024-12-25 03:53:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 265b1fa5-eb5e-3e45-988e-8d0c9f2edd36 | -5.00761 | -41.86734 | 2024-12-25 03:53:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d1f091b3-d625-3b4a-8e26-c85de4046759 | -2.94472 | -51.49155 | 2024-12-25 03:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ec10627-30fe-3ea6-b7e0-ba0d2c0852ed | -5.47916 | -39.66292 | 2024-12-25 03:53:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5435da86-e868-3f08-b6f3-324e4d7e4098 | -4.76646 | -40.46398 | 2024-12-25 03:53:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c56a9ea5-a463-3aff-a421-a2f42799ef1a | -5.4786 | -39.66642 | 2024-12-25 03:53:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e26e761-ba2b-3adc-b0b6-a9c674e2c826 | -4.20386 | -44.54 | 2024-12-25 03:53:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| defd173e-6062-379f-9001-df276f60865b | -3.39534 | -42.10125 | 2024-12-25 03:53:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd002ffc-b454-3ea7-95ac-f04228190676 | -4.86831 | -38.33398 | 2024-12-25 03:53:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a9310fa-e4ba-375a-a0c0-923e910d97ad | -3.76591 | -47.14231 | 2024-12-25 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b32d7113-d4cd-3ba3-9b71-e334c23e2ef5 | -2.77065 | -45.09444 | 2024-12-25 03:53:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18cedd50-8f6e-3e93-b0a9-6979979cedc4 | -3.92041 | -47.19351 | 2024-12-25 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 311cc7b1-2ff3-3773-897a-b8f3c8aa54b6 | -4.24837 | -47.58605 | 2024-12-25 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ed1614f-a739-3e9f-ae40-4b3e6319bdea | -2.83769 | -40.29628 | 2024-12-25 03:53:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2cfaebe6-da4a-356f-bd4c-cc61a0914f53 | -5.20017 | -37.29575 | 2024-12-25 03:53:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ace4ee2-f510-3429-835f-7f79e5c53800 | -4.25448 | -47.58361 | 2024-12-25 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b72fc7c-fddb-338c-bd66-806369c543fc | -4.86499 | -38.33346 | 2024-12-25 03:53:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4d358976-1202-3665-bb28-e11ab9ed9d99 | -2.55739 | -44.275 | 2024-12-25 03:53:00 | NPP-375D | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc96cbd5-6c42-38c6-8b0f-52b40cd9958b | -4.77059 | -40.46064 | 2024-12-25 03:53:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eeb2faec-bd5a-3b15-a007-add9b473bba7 | -3.77047 | -47.14055 | 2024-12-25 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c6a588e-5da1-3a89-9be7-f076c58ce00a | -4.05631 | -38.29095 | 2024-12-25 03:53:00 | NPP-375D | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 01cbd220-0695-38bb-9949-a99ece4c90a9 | -4.07841 | -40.31945 | 2024-12-25 03:53:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b100ef1d-0f2c-3eb7-8daf-3decbe725985 | -4.24897 | -47.58258 | 2024-12-25 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a248aa9-011c-3ea7-9608-286d5d7e9c34 | -3.76452 | -47.14294 | 2024-12-25 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cf4260b-3b20-3cd2-a606-b54524c516df | -6.21023 | -42.63852 | 2024-12-25 03:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b3b8d6a-84ea-304f-8ff4-0ef774196bf1 | -5.01608 | -38.04146 | 2024-12-25 03:53:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 97475c22-9901-3e43-b13e-b968729f21d5 | -4.12622 | -46.70323 | 2024-12-25 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4883b3b6-77d8-3972-8dc7-236cf3150a7b | -3.22609 | -39.66909 | 2024-12-25 03:53:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7b1b8dad-e69e-3be8-911b-eaa24bdb184e | -6.90618 | -38.73048 | 2024-12-25 03:53:00 | NPP-375D | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 26266335-416c-310a-b8c1-0c38ab6b78d0 | -2.94375 | -51.48112 | 2024-12-25 03:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50a9e8bc-9836-3da6-a789-d5d7ee90beeb | -4.05686 | -38.28749 | 2024-12-25 03:53:00 | NPP-375D | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b462aa6c-b4ae-3c51-87c7-016be57a750f | -4.20486 | -44.54214 | 2024-12-25 03:53:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 90a95cb4-d419-382a-bb39-04ecbd658608 | -3.22953 | -39.66964 | 2024-12-25 03:53:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2ded0e53-95ff-3d08-93c8-894029853f96 | -3.92639 | -47.19107 | 2024-12-25 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd036bfa-0326-3688-984c-f8a674591189 | -12.5367 | -38.00608 | 2024-12-25 03:55:00 | NPP-375D | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fb670bf2-693e-3b33-87e8-826878f19475 | -8.09879 | -35.11321 | 2024-12-25 03:55:00 | NPP-375D | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c7b77c5c-97ed-3e8d-b89b-1db7a95179ce | -11.95463 | -37.63948 | 2024-12-25 03:55:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6d312996-9d98-3fbb-b2f2-ebc303b2ff64 | -7.62091 | -38.72611 | 2024-12-25 03:55:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c73fd0db-5cfe-385a-a17f-1f50a51f866a | -12.36721 | -37.88434 | 2024-12-25 03:55:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 750f1b0a-9fef-3bea-977a-4629ea32ad04 | -12.36664 | -37.88815 | 2024-12-25 03:55:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b38222e6-17d4-3db6-ad47-60305384757d | -6.92045 | -40.15018 | 2024-12-25 03:55:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 58697cbd-8f55-37d3-b1e6-cfeb50b89ea5 | -7.42125 | -38.09769 | 2024-12-25 03:55:00 | NPP-375D | PEDRA BRANCA | PARAÍBA | Brasil | 2511004 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0bc92b8d-11de-3887-805f-eb88524d70ce | -10.62549 | -38.01404 | 2024-12-25 03:55:00 | NPP-375D | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ec45ba3d-cd2b-3ca5-9fbe-cc22df4f5d4d | -12.53727 | -38.0023 | 2024-12-25 03:55:00 | NPP-375D | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb8ce1be-0860-3fcc-9140-153f43d72c21 | -15.01105 | -39.01931 | 2024-12-25 03:57:00 | NPP-375D | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cbe59d20-ad24-332d-9460-5deec4e904c4 | -20.76562 | -46.76844 | 2024-12-25 03:57:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7fb16604-e95c-340e-b12f-643d8d0d8d4a | -23.59499 | -47.44062 | 2024-12-25 03:59:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09bfec4b-a023-3c19-9dc3-b626e6cea515 | -23.59475 | -47.43634 | 2024-12-25 03:59:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5333ed08-56ef-3a8e-b4b4-ffe9925d057b | -22.53951 | -48.81301 | 2024-12-25 03:59:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 993b792a-274d-37ad-abd5-8e0ade80eb5f | -3.7879 | -41.61002 | 2024-12-25 04:16:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dc86bc1e-bab0-388b-a1b0-1937ac2c4ab5 | -4.76938 | -40.46509 | 2024-12-25 04:16:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06b6132c-7fd8-3414-a9d4-e6145da8d3e6 | -4.86541 | -38.33409 | 2024-12-25 04:16:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d72f75c-b6e3-3119-9a6f-f02790e4128f | -4.62635 | -39.60995 | 2024-12-25 04:16:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 565d084f-f9d8-3e0f-8943-8d07ebf7681b | -4.05525 | -38.29071 | 2024-12-25 04:16:00 | NOAA-20 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 732d9329-1dc6-34e6-a96b-88121fbc6a5e | -3.63762 | -40.4836 | 2024-12-25 04:16:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 39419d43-c21a-3957-8e4a-590314ea8549 | -4.05641 | -38.28782 | 2024-12-25 04:16:00 | NOAA-20 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1ee26c5e-0c21-3f62-aca6-e391070b58d9 | -1.51246 | -54.95659 | 2024-12-25 04:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a00040e-f016-3e5d-bdb4-b8a32f286026 | -4.77006 | -40.46065 | 2024-12-25 04:16:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 050aa51b-c966-37e2-8ab2-ccab5acfecae | -2.33891 | -53.88741 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57e159a4-74c3-31ea-aa20-f623dfe57b91 | -5.2012 | -37.29385 | 2024-12-25 04:16:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc230250-a18e-395f-86b3-c146a478b69b | -2.83633 | -40.29915 | 2024-12-25 04:16:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 5196cc1b-b9af-301b-9450-5dc7ea9f7527 | -2.33956 | -53.88338 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edacfed4-e6fc-349d-aa30-cc83aa38bd10 | -3.78034 | -41.6128 | 2024-12-25 04:16:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e80f04c-2bfe-3e98-90c9-91897270dce7 | -2.97403 | -45.83973 | 2024-12-25 04:16:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47051618-5351-36bb-8eff-2d2adf3a6194 | -2.98132 | -46.95708 | 2024-12-25 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de2a1b67-810f-37b1-bb2b-2f38524a0317 | -2.81931 | -45.93077 | 2024-12-25 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f1d5979-60ee-30e9-8a43-810ae878257a | -4.38591 | -42.14054 | 2024-12-25 04:16:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 31c5e5e5-d567-30bd-bcd7-7a1695e47db8 | -2.33827 | -53.89138 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71284730-c6b7-3a5e-9dbe-d9f37fd6f674 | -3.78441 | -41.6095 | 2024-12-25 04:16:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7c7303f-223a-3119-8d7c-8ec6e3aa65d1 | -2.34464 | -53.8883 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a60be967-6f07-39c3-88f6-8f8fa1541cbd | -1.69442 | -52.61209 | 2024-12-25 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 435e02ee-d09b-3cc8-ab87-a647f897b127 | -2.76945 | -45.09275 | 2024-12-25 04:16:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bf24988-4d8c-3a84-a138-94fc8f31c380 | -2.31766 | -45.06999 | 2024-12-25 04:16:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c717c8ab-f396-36fa-916f-dea31f2434b1 | -3.2263 | -39.67196 | 2024-12-25 04:16:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 044bf2eb-69b5-3092-861a-c1298e27e847 | -1.83744 | -46.25179 | 2024-12-25 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52fb49b5-af15-3600-b1e1-276da926a671 | -4.62665 | -39.60841 | 2024-12-25 04:16:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 738bdc60-612c-30db-a1f0-08aa62c3b0a4 | -1.84118 | -45.64285 | 2024-12-25 04:16:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04055339-1ff5-36b7-bcc3-e32411cf8e02 | -2.55189 | -45.51757 | 2024-12-25 04:16:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a1c86f4-a3af-340b-aa0e-42998782c529 | -1.51865 | -54.95768 | 2024-12-25 04:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f13dc503-a0a5-3d02-a3a8-c06eda5d0278 | -3.7341 | -43.99327 | 2024-12-25 04:16:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbbbea66-2956-3cc5-a093-b9bac1e82fd6 | -2.31149 | -45.06535 | 2024-12-25 04:16:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0eb3dae-1fb7-3c91-8560-2f68713f2f9b | -2.29391 | -53.6641 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0eff34fb-3f54-316c-8b25-84af8c29de20 | -2.34009 | -53.88941 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f648020c-eda0-35be-b126-c0e7a496c9df | -2.41343 | -54.2308 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf9cef85-c11e-35c8-a90b-2bf8b27a6b1b | -2.76833 | -45.09988 | 2024-12-25 04:16:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d637212e-0891-359d-b1b0-f92864fc8dfc | -3.50288 | -44.91806 | 2024-12-25 04:16:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ffee52a-8cb2-3dc8-82dc-03bab9ff3547 | -4.0558 | -38.29179 | 2024-12-25 04:16:00 | NOAA-20 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |


[Clique aqui para ver as próximas entradas](README3.md)
