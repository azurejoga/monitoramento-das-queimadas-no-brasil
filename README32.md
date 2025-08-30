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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79196d28-3f5c-353e-82f7-dc7a40f4e2c4 | -10.53568 | -56.38491 | 2025-08-30 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 86c0e4f4-ff80-3d53-8621-9af117e01d5f | -13.60451 | -46.87433 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1d9725d-b57f-38d0-b20b-e66dd33be7e9 | -9.1817 | -59.58527 | 2025-08-30 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6550c4ae-8724-3b89-aeb0-f997d46e26a4 | -9.50168 | -45.38602 | 2025-08-30 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfafce86-95c3-3903-afa7-782652737165 | -11.06312 | -52.04266 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf9970ef-05cb-3e85-8fd0-82579b4a6e59 | -14.3239 | -51.95704 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ec5d68f-7bb7-3402-b6af-9e69d10abad2 | -13.3676 | -47.01735 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d0f91b86-4254-3484-afef-6d4788107392 | -13.46737 | -46.96789 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a80b00f-2984-3e82-ade3-ddde390fc363 | -16.4091 | -45.64799 | 2025-08-30 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| faf2e9dd-abd9-3bce-8188-2d8da59a9593 | -11.35992 | -43.55725 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b4c0a55-f608-3d41-a02d-c5896344eb57 | -12.56452 | -44.80333 | 2025-08-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b86746a3-0680-3ef8-b830-d64646c924d5 | -10.37274 | -57.82396 | 2025-08-30 04:21:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d8fc7b7-357d-34d0-a27a-5a27792bb45a | -10.67772 | -47.06851 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45ff36cc-524d-3e5f-b4f2-a66ba515c2fa | -8.88842 | -47.16282 | 2025-08-30 04:21:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf5cc485-6b0f-3725-84b6-faa2170f2ec9 | -14.62309 | -48.07739 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a67e71fb-bc0b-37ed-83bd-49b69036d35f | -10.72825 | -47.0104 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcf54da9-373e-371d-a59e-38b2b8b38bbb | -12.63027 | -57.01154 | 2025-08-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e794c958-1ddb-3a6e-91e8-47da0c6829f2 | -11.07615 | -44.60675 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10f1b7a8-99f2-3146-a811-12b12c0b0e29 | -13.39341 | -46.96301 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b22e5abf-8c51-383b-b656-30d716474927 | -14.44881 | -53.38078 | 2025-08-30 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 039adf1f-a3bf-35be-8afe-06352216b54b | -11.30841 | -43.61715 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f215c5b-e8d2-389a-a49a-4307bf56c655 | -13.48418 | -46.83994 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50a0dfeb-dcb1-3c8d-9db2-05fe237cb67e | -11.30598 | -43.56097 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b1bd606-79f0-36fd-b343-a99578775e55 | -14.25434 | -45.24114 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93c59715-2d45-36ba-a54a-7961def8bc11 | -11.86903 | -46.38323 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f96cf59-9afe-33fa-8309-5d3e883c2cd5 | -9.94173 | -46.35026 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8eb1ed69-2a11-374e-8460-4ca4b42eaee6 | -13.37378 | -46.97826 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d2b37254-9c4c-312f-b876-9856c89c36e6 | -8.55956 | -51.30997 | 2025-08-30 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2f12ef7d-545b-3ff0-9a8a-77b759089e86 | -13.66987 | -46.87092 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c28828d-3425-362d-bf48-169eed7f14dc | -11.86951 | -46.44461 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd5138d1-201a-3838-a1aa-dd56f7ee11be | -13.51196 | -46.83724 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8a2f674-6257-3ebf-bfe7-33ebda168008 | -13.68689 | -46.91357 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b005dc9e-4653-3928-bfd3-72ffac4222df | -10.36399 | -59.21348 | 2025-08-30 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e93ed5b-6425-39e6-9cc8-8ed71e551411 | -14.00323 | -46.32701 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 324d0207-9763-3620-b7dc-6b45a89d09c9 | -13.69189 | -46.90339 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6f14bee-abb9-34c2-9c3b-a6ca3a2b2664 | -14.04408 | -44.49054 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5edf9b97-8be2-34b9-a7cb-15d45b94e53c | -14.4586 | -48.45747 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba28250a-31f0-3141-82b4-ffad8ca9ecdf | -9.69788 | -48.31268 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6912c716-540a-3b82-990a-d6fef7020ee0 | -13.36573 | -46.8787 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6e22fe5-a71b-3f3a-816d-5a26f925d298 | -13.39315 | -47.02868 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c43cc532-c824-3593-b19b-528b54b4d46f | -9.73122 | -45.24371 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94cdc3c3-abc0-3c9f-a3ec-4125cd0be8fe | -11.30774 | -43.5733 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1df6c7b8-0e3e-345e-9cbb-6225ea07a050 | -14.50393 | -52.05204 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4251c700-defa-3a02-adcb-a36208c1d791 | -12.70347 | -48.14055 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2af08aac-18e2-32d1-95fe-6a15465df42a | -11.32808 | -43.62818 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d792aa4c-4881-38da-8ffe-77871f388791 | -15.0975 | -48.15821 | 2025-08-30 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d0a1843-6480-3c6d-8ab2-2fc92ac222bc | -13.62758 | -48.25177 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03dc5ddf-8ee7-35b9-bcfa-517091488bf6 | -13.38539 | -47.03469 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a712a12-0da9-3463-83a9-ed380e029415 | -11.37733 | -54.34025 | 2025-08-30 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8dcfe88-e1a9-3d93-a291-bf94273ddb11 | -12.92392 | -46.35723 | 2025-08-30 04:21:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb52d770-ae6e-32ee-9b4f-b3f66f1d7f18 | -11.32113 | -43.62712 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aa58a415-c689-3677-b561-f9c97263841c | -11.89518 | -46.71291 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6076805c-cef7-3186-b178-6069c56494c4 | -13.42988 | -46.94724 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f765cb79-d977-3d31-a8d5-692cd69af595 | -14.00422 | -44.594 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf453b68-573c-3730-a03f-1dc1b134910d | -13.36816 | -47.0138 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4950700f-e317-3eed-a306-17d90e7c7282 | -10.27477 | -54.23737 | 2025-08-30 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5d1bf65-7b67-357e-ad0d-20044ee1e1d2 | -13.39116 | -46.84665 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ced5fd9d-187d-3295-9070-19392bded06e | -10.6469 | -48.65524 | 2025-08-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 198136b7-9140-328b-ae8c-ebde02d0d68d | -11.86676 | -46.44055 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8751af0-9c9c-35c1-9ef3-0b1e7e7f4b06 | -12.84789 | -48.18056 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da885d1f-cdb3-3a46-bd24-706cb87650c0 | -11.30078 | -43.57224 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f4aff50-c6d9-3501-bdf4-71101a9b4d87 | -13.97624 | -46.32625 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 286a9f13-3957-3837-8012-90ccab0b8b88 | -8.86866 | -45.73324 | 2025-08-30 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15fbfc19-1a99-3d0c-84c5-9fd94414a65c | -13.67815 | -46.88297 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4ebd570-2bc4-3fdd-9aeb-c3896c3c142a | -11.77961 | -47.55841 | 2025-08-30 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b5b29a1-f605-3798-aee5-128232c5d83e | -11.83394 | -46.86221 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b655213b-374d-31d4-8ffd-b30e9cf3452f | -12.81879 | -48.18736 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aecfea5-062d-369c-9de0-c160628f69de | -14.00989 | -44.57937 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 118f9142-d1fc-35fe-91a9-e07cea05e8c2 | -13.50512 | -46.94485 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f362734b-7265-3b31-a5ae-f7a8cd733cfd | -8.69081 | -50.3782 | 2025-08-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91dd08dd-29a7-3bac-b309-96c4dc93c617 | -13.63061 | -48.19098 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0679d88d-10c9-3f34-8bfc-ce516b3630aa | -13.60795 | -43.46301 | 2025-08-30 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5275d54a-7d70-3d27-b10e-1fc4ce6fc272 | -13.57908 | -46.90646 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f004055-c034-3264-a916-0c0cbb9a8d11 | -11.58592 | -46.3658 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3339e9c5-fcfb-3559-bb68-d7054a3e8dfe | -13.60987 | -48.16156 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bd46a0f-ccf7-32b8-8d6a-59a4b90d9e1d | -10.02408 | -48.09005 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5269dde-79d5-34ca-a365-cd2ef0f6c9be | -13.58406 | -46.89638 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b448bfd-b830-32a4-a576-bbdca33ece8b | -13.40585 | -46.84167 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41a64918-c1bc-35db-9035-9f982c8a23d7 | -12.92447 | -46.35371 | 2025-08-30 04:21:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19b658c7-e5e2-3626-baf8-94c058628d32 | -11.41746 | -46.91413 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b78c4e5f-1e9f-3b96-acdd-cce19d872a8e | -14.52106 | -47.29654 | 2025-08-30 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 51cfb3be-f3b1-3a47-ae86-88755dc48705 | -11.84699 | -46.39404 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 01c5fc8e-a019-3a30-89e5-1f0b1bf5f298 | -15.17542 | -48.03206 | 2025-08-30 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37627f1e-e8e4-30d1-a800-1a71f20bd242 | -12.40129 | -46.48127 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64974e15-91ff-354e-9056-38ecf7f4ac1f | -11.92618 | -46.68898 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3ac90f1-30fa-3881-be6d-1bea007e0dc0 | -11.8574 | -46.43541 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9856eca0-25e4-3578-9efc-4136e3ff6cb2 | -11.77564 | -47.56152 | 2025-08-30 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62b86521-6f3d-3386-bb34-63d7a1eb1ce4 | -13.50866 | -46.83669 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0745205f-8090-3b4d-8aaa-1ffba1a100e7 | -11.9245 | -46.69959 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89c5b7f7-fa44-3a9b-8f47-10f21f7a1137 | -13.60009 | -46.88086 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c4bc970-7960-3a20-b0b4-f03bcb235598 | -13.53487 | -46.94988 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 241f07ca-5903-3a9d-87d7-9788a6473025 | -12.89775 | -48.90189 | 2025-08-30 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d06c9dc-f4b1-3523-8d15-754a89b0f70c | -12.84595 | -48.14943 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 661c9368-d0dc-39dd-bd7a-3ffe9601e3d1 | -9.44362 | -47.63884 | 2025-08-30 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a0f12c6-998d-3426-a21f-d4a72bb000a6 | -13.36995 | -47.02485 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c5df2bd-3086-307c-a60f-8abdd9ee95fd | -10.02676 | -46.02655 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 016da491-82d3-3945-b6e4-d0061d9626b9 | -13.49079 | -46.84103 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95155040-fc56-395c-ace6-ad48cf36c1df | -12.84873 | -48.1538 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2ce4936-996f-3188-b1fa-79cf443c62dc | -10.73436 | -47.01512 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc8d94c6-771b-3a78-9342-93bf263915dc | -14.03032 | -44.48843 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README33.md)
