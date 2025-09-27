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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b03d53e5-b960-3dfe-a578-db5da6165119 | -11.34989 | -45.00917 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcb9e1a0-c20f-33c6-9432-29e530e8fa51 | -11.37719 | -44.94378 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5386902-f993-337b-b79f-34423c6976ac | -12.65327 | -51.67601 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 942c0837-22e4-39a5-945c-b2fc22ce9355 | -10.5947 | -48.50536 | 2025-09-27 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64a786a0-282c-3d8f-a611-5e8700023733 | -10.17021 | -49.3779 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b5e8ac9-f0c1-3bdd-aa04-67a4abc29c79 | -12.18899 | -46.57364 | 2025-09-27 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97d601f1-d330-362f-9bfd-7c08b8d55d96 | -10.12177 | -45.34268 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2fc12da5-f64c-33ef-86fc-0e0e27d98bcd | -11.3811 | -44.94071 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1377df8-9743-36a9-9aef-833a9c60a998 | -11.68348 | -44.42629 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 202c5dfc-42b5-3539-8dd3-8e1c30033069 | -12.03102 | -46.50783 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d29dbff-d854-31a6-b004-016a81e7331b | -10.00331 | -44.17293 | 2025-09-27 04:23:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 504f5dbf-4f2c-3a38-bc78-f42de8abdbf3 | -11.35828 | -45.02148 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8bf72191-da90-3319-93de-8542ee181299 | -11.43776 | -44.98622 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dee650d6-2897-3bb6-92ed-2d73dccfefdd | -12.06177 | -46.62955 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 716ade94-a0d9-352b-b12d-3cf5540949d4 | -7.65656 | -48.21223 | 2025-09-27 04:23:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9977a01-877c-3c22-b84c-96b28814e138 | -11.97265 | -47.90425 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a49e9cff-b45d-3dac-9c39-062b5c3cfcc0 | -11.89475 | -49.90259 | 2025-09-27 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78bbbe8f-6028-3935-a9f9-ac92879be38d | -8.83773 | -46.21103 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25579d17-8441-32d9-9c47-d1a1c1d34f13 | -13.0682 | -48.72199 | 2025-09-27 04:23:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af9e6448-9b09-312d-91e3-0dc66c76bef5 | -9.42381 | -40.71814 | 2025-09-27 04:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| df369db0-490c-3906-841b-7edce76f7d9c | -12.84047 | -44.70298 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a68eec4a-3404-366d-a223-c3023ba1fe26 | -9.97171 | -43.6083 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80cf76ad-2fcf-3451-a74f-62561eb848ac | -8.4755 | -47.835 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ad98f5b-54f9-3dfa-bd46-bb8f61506870 | -9.89628 | -49.12636 | 2025-09-27 04:23:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7a5f0f37-5654-38d1-a0e6-64e34c203f1c | -12.9504 | -48.90917 | 2025-09-27 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dede04cd-de14-3e8b-957d-ff761b2d9d4b | -7.55214 | -46.41306 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5903447-967b-3783-9c3f-f9d45a087e77 | -11.60722 | -49.48151 | 2025-09-27 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 403a580b-e81b-3125-bcaa-d1c6fbc49eda | -9.98206 | -43.58671 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 573da186-bdcd-315a-b90b-a133594e7944 | -11.05288 | -47.65639 | 2025-09-27 04:23:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11cf1cb8-f5b7-3111-8a57-82c9b270f47f | -11.79044 | -44.91293 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3763edc-3623-3d99-b99d-bf55bc1e7eee | -10.17096 | -49.37335 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3a05568-b545-3391-9955-fdc0f4c7e0ff | -12.65049 | -51.66757 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8373887-6169-30f5-b6ee-da500a9b164f | -11.35269 | -45.01327 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eaf464b6-ffc9-3cdc-bf50-e220d85db659 | -11.67389 | -44.46622 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c5a8418-4239-3db3-9aa8-74a08d840b26 | -10.03265 | -45.41477 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da2910b3-9749-3bf2-91da-eb94a65fe8e6 | -8.5212 | -44.62175 | 2025-09-27 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb350642-f9bf-39d2-8c62-fc30721541e5 | -12.27939 | -44.06153 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfd280ec-f02e-3a4b-9f23-c248855f857d | -9.11449 | -45.8749 | 2025-09-27 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e532872-a6d7-3842-9053-8b907ff0a4d6 | -9.96598 | -43.59968 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0a8ec14-c5ec-3658-942f-2704bf6184db | -9.18492 | -46.63809 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56a16c41-b5fd-3dd8-b6e6-d41c6536fb05 | -8.32539 | -46.21227 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68d4fd22-5204-3175-a839-be8eaf10d629 | -11.29771 | -47.82032 | 2025-09-27 04:23:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f805b220-2644-3ca5-b96a-d67e00710881 | -12.95343 | -48.90832 | 2025-09-27 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b628af0c-bc80-3fe2-a1c3-593d0d403dfa | -12.64981 | -51.67135 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b690d5d0-03cf-3739-983b-662e2168a5f0 | -7.64388 | -46.77432 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc7aea66-7bef-33ee-a8ef-a8accd41d976 | -8.47758 | -47.83831 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd313a5a-4b05-3754-81fd-c5e7b3cd9934 | -9.70986 | -48.242 | 2025-09-27 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 636f1fe2-3753-39ea-a33c-88e7222abac1 | -12.30176 | -47.21748 | 2025-09-27 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93632f10-5407-3e0d-a4fa-1293248b1010 | -7.71383 | -47.30426 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d551e43-9b0b-335e-8d29-b34d3bc535a9 | -11.43368 | -43.51401 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3081b49-40c1-3118-9a8d-5cfe974284a4 | -12.64556 | -48.15234 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c10c2bb2-ca3c-37c4-9937-d04aaf2e7495 | -11.35772 | -45.02504 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8492a4b6-9c77-38be-b4b4-0f063bee968d | -13.04991 | -47.06739 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26028f50-e1be-3445-8f15-a665ced3da6f | -12.28457 | -44.05061 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca74397f-181d-3d21-b3be-cb179531f411 | -10.28309 | -45.22054 | 2025-09-27 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83c826cb-a449-3062-9a71-84dee1b06350 | -7.71668 | -47.30871 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b80f0f04-0758-30a1-8d55-81291c1f7dd2 | -11.97282 | -46.61493 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cf38a75-f6aa-38bc-b7b8-f003124f4f4b | -10.19676 | -44.84169 | 2025-09-27 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82816b51-0df5-3fd6-bdd1-c2dd14e00766 | -9.1883 | -46.63865 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd0b152b-5a7e-3992-a277-ad1cefe23902 | -12.36291 | -44.15196 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 911ebc00-bc0b-3956-a2a9-04af98f06216 | -11.69312 | -44.45419 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| befc3a25-e4d4-3953-ac35-952fbaa2841c | -8.72733 | -46.68353 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc663eed-9b1e-3aee-b7c0-546ab4dc450c | -12.97024 | -46.91052 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e297b381-bf53-3660-99cc-45ce7ea93a67 | -11.38339 | -45.03645 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5708105-8f9e-3de3-83b3-748d1588a884 | -11.42841 | -48.68118 | 2025-09-27 04:23:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 926ea199-9f27-3e7e-9a20-b7679d409b8a | -9.8761 | -45.90738 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2440b735-4495-3a90-856d-27e0b1d4ed22 | -11.79323 | -44.91713 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f114551-1e64-30ba-b8c4-4a1a7d5f3d66 | -7.80909 | -46.96075 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36e64c7f-315b-3d26-a04a-aad4c3b89cb9 | -12.2978 | -47.22053 | 2025-09-27 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68bf79f2-3db4-341f-b8b7-2aa0beb68481 | -8.26041 | -44.94626 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46e4b443-7fb9-3cd3-9c77-94971ed6ccf7 | -11.54074 | -46.95157 | 2025-09-27 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 749e20d1-9e0d-3009-ac22-6876cef733b6 | -11.62122 | -44.42404 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a5434b5-5fce-3b1b-9485-ace9d476027f | -11.61386 | -45.42187 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73461855-020f-3264-9e7e-44b79f17e8b1 | -11.98078 | -47.8978 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f3dbfaab-ec37-3a13-b891-03f3eb34ad62 | -11.97953 | -47.9054 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a37f08b-189a-32f0-afaf-f629083fea97 | -11.40847 | -44.91934 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90538ac6-0a8d-3efb-8740-1cab3479887f | -8.47892 | -47.83033 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bda76dc2-fe8d-37a5-a3b1-f393ce94ee43 | -10.56511 | -46.26081 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38be5870-15b4-3372-89b7-31cddf6a9b6b | -13.72564 | -43.72141 | 2025-09-27 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d1d7f49-5849-3061-bedf-754781685c95 | -11.78821 | -44.90503 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e3b465e-637c-375c-b6db-9defa1b4c413 | -10.24053 | -50.25211 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea1ddef4-d1bb-3778-b4de-063efd10dc42 | -8.67225 | -43.99019 | 2025-09-27 04:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d403c197-7e2a-34d3-b1f4-bfd073eeabca | -11.38506 | -45.02574 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f48cd44-4810-397a-9c42-d09e20aae62e | -12.17288 | -46.56733 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17eaae80-fd77-3963-9aeb-32c5d976cdf5 | -11.83025 | -46.61657 | 2025-09-27 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f458f6d8-dc77-3814-8c0a-b2330ac948dd | -9.7513 | -46.1404 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90a8c637-8d6b-378b-85a4-95b8538bb4e7 | -8.25855 | -44.80641 | 2025-09-27 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a14ae4c0-2229-359e-9d72-8f2493e06d94 | -12.28054 | -44.0539 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f201a934-c541-346c-a3d8-d40dd44da754 | -12.02884 | -47.06907 | 2025-09-27 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c695afa9-f482-3bb3-9219-a6add29082dd | -11.43106 | -44.98513 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 011f34ac-592d-3a80-b2d7-1219ab301d1e | -9.98035 | -43.57484 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96bc6d3f-ebe0-368a-bb49-296d8a64ebc8 | -11.9427 | -47.87192 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d0a6dbe-7731-38fc-9b62-abe3c5613f3b | -8.6582 | -43.9917 | 2025-09-27 04:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4527fb87-70e4-37da-90fe-e3e86bf672ea | -10.80458 | -47.27172 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a75da4f9-1e8b-3819-afba-e240fb76c862 | -13.43018 | -46.51477 | 2025-09-27 04:23:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b8a7543-9683-3976-a341-26201ca45959 | -8.83268 | -46.22109 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01d460ec-f526-3660-aa75-498d6c7b74fb | -10.56845 | -46.26135 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 177e447d-9282-3c20-abfb-4f3923f857d7 | -10.28752 | -45.21407 | 2025-09-27 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f0e3877-da65-320a-9fbd-e26ad112a331 | -12.03278 | -47.06602 | 2025-09-27 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1d2570cb-8870-3a6a-bb2b-32aa9be378b5 | -11.3577 | -45.0031 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README36.md)
