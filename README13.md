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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbcc2351-baad-3357-9af5-aceccd78b5d8 | -10.45714 | -47.02853 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d1cfa395-692a-32a7-8108-7d59abef896d | -10.29965 | -57.13544 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36bab02e-b00f-31e8-89d8-c99b190277f5 | -11.13963 | -53.91241 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae60c2fb-2e84-3698-bda3-d84337482bf1 | -12.97662 | -54.68585 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd28f74f-fef2-3bc0-b54b-96ce4a4d835c | -11.88129 | -54.67152 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 35246db8-8116-36ab-9adc-79809ae10770 | -12.76649 | -44.41479 | 2025-06-21 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60199f9b-e13e-3563-bac4-d7f1b84ecb6c | -11.87849 | -54.66327 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d2c0014f-e4a1-302f-ad60-914fb30cfec9 | -11.8759 | -54.67826 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c94f4c1e-9731-3e58-9628-a056bce4f719 | -9.47641 | -57.83831 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 238c6715-0fe5-3d93-8ecc-4253b3cae46b | -8.7364 | -47.99081 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ce893a5-f245-3410-a013-7edee9681fc5 | -12.45195 | -57.19089 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b856dfa0-520b-3056-ad98-1d992c58c8dc | -10.45317 | -47.03173 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c88733e8-448d-3116-8564-7ba8ce90d3e6 | -11.14388 | -53.93444 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca63d0ba-4d2d-362c-95e8-1a0732a7ae3d | -11.91842 | -54.81532 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 852f219c-c9a9-36d3-a74e-9eea68cf9e00 | -11.78506 | -57.2421 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a044c317-5c39-3ad8-822b-6e66c3aea3ab | -11.07083 | -49.61963 | 2025-06-21 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c860c63-92aa-3f66-bb41-def63e697ad2 | -10.89149 | -56.45919 | 2025-06-21 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1698b065-7b8b-340c-854b-530f2d416ced | -8.19483 | -47.77687 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e93707a2-8294-3ee8-b734-653adaeeb8e0 | -13.23802 | -49.83744 | 2025-06-21 04:34:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 3247945e-8417-3c98-8764-8e05b2b7ad4a | -9.13172 | -47.58911 | 2025-06-21 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbedd86f-2e19-34cf-9ce4-26429f4e4afe | -11.25859 | -47.82069 | 2025-06-21 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c956310-3887-37a4-8d23-9d9ad0f28f47 | -11.13608 | -53.91497 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0af437d2-6510-33d4-acd8-d887acce0b27 | -11.62412 | -58.29391 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c566f569-b5da-38fb-aa1c-4b4054364b4f | -14.81534 | -48.47003 | 2025-06-21 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ea030c4-f0d9-3398-9a38-d14d40820c1a | -12.58368 | -56.99023 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 371cdafa-4d44-327b-8c4b-99a5a4a8b201 | -10.54419 | -46.77588 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78fbef95-6cb4-37d8-8055-ba8fef8344f0 | -11.84253 | -57.76361 | 2025-06-21 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23fdbc07-efc4-3bdc-9c0f-2c0b254eda0f | -7.28017 | -49.99454 | 2025-06-21 04:34:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a02b994-ef8b-331c-80e2-9b161cfeabf9 | -12.50885 | -58.35402 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b7781fb2-ba50-3e45-9f43-b61aae69e552 | -11.32858 | -45.22478 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b7b8ed8-fb19-3c8c-8b0b-1bd484f903f6 | -9.74091 | -48.33548 | 2025-06-21 04:34:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f79a2e7d-1c4f-3cf9-9ead-3ca970ade63a | -13.03683 | -53.71672 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3e1fff6a-bfe1-3636-b210-a9613be0d746 | -11.76288 | -43.37039 | 2025-06-21 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3360738d-9864-34ef-9eb7-66e0d82845fc | -10.0284 | -54.32043 | 2025-06-21 04:34:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3ca0ed7b-2a38-313c-8028-4ac18389b37c | -10.58436 | -46.92847 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b87c4d1-2cb5-3f2d-b735-763fc398e3f6 | -13.66212 | -50.19109 | 2025-06-21 04:34:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3cc707c-7c9b-3f5f-b248-3194b4c5ee5d | -10.45261 | -47.03547 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69d1a688-345a-3f91-adad-5a5a94322937 | -9.48442 | -56.08197 | 2025-06-21 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93f41a98-812f-3f92-8be5-e92ef9c3e724 | -10.52411 | -53.62516 | 2025-06-21 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7f849f84-4e05-30fa-a495-bbdc5af38d8a | -9.47827 | -57.82838 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56d416f9-9152-3758-b656-940258ac6ede | -14.54475 | -47.91207 | 2025-06-21 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eddb7bf9-e040-306c-bc3f-670d63e6fdbc | -9.91824 | -52.44271 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 650d9e83-77f3-3719-a586-054347c82587 | -11.94498 | -58.74249 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e50403d-81c3-3607-83b2-3e4f3ec70995 | -11.88507 | -54.66904 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5f5affe2-86ca-386c-976b-4681eeac0117 | -11.70526 | -54.5028 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22cb1a3a-34d7-30cf-818c-12c21257e6a3 | -12.15989 | -48.68079 | 2025-06-21 04:34:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caf51364-d52b-3d3a-96d6-d3db9e4824f2 | -13.41764 | -48.72467 | 2025-06-21 04:34:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf6dd2a6-49da-3edb-b839-b353c66083ef | -10.95542 | -49.25215 | 2025-06-21 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbedc6b1-a37e-374d-b025-5d6642e09634 | -10.88416 | -54.75103 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 796b631d-4b1e-3c4c-886b-ab0b5b38bc36 | -11.88603 | -54.66852 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9aa05e2-cf12-33b3-abe3-85f07722d7b4 | -9.73538 | -48.32747 | 2025-06-21 04:34:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eb361be-7d88-3f74-a989-b0ed0367beca | -13.36817 | -54.2579 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e9486972-72b9-30bd-aa11-df2c03f39119 | -10.44128 | -47.04132 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86bfc042-5bd1-3875-b512-b98e7f9daebe | -13.26279 | -46.82906 | 2025-06-21 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b6d5017-2a2e-326f-b3b5-4cc921cddfd1 | -10.89059 | -56.46419 | 2025-06-21 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bf4a45fd-2f6b-32b7-a01e-c7ed9f1089b6 | -13.29215 | -57.08274 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0bf4e15-039f-34dd-8a00-0f890b9fbb97 | -12.97226 | -54.68148 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88bfc2ba-40dd-3b9a-af53-fa50130d317c | -9.25795 | -57.52518 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 06debb24-e754-3af8-a1b7-96c1540a0f86 | -9.47031 | -57.84637 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| acc272b2-1026-3d5a-8b69-32edb04c9156 | -11.20788 | -47.83855 | 2025-06-21 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 400b2f54-1b92-3b91-894c-1110d4250d18 | -9.46098 | -57.83765 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3cd2826-9ac8-3326-ba5d-f82bfbd5e240 | -11.94366 | -58.74933 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a7044a5-1e77-32d0-bc3b-c31bc36769ac | -10.95157 | -49.25512 | 2025-06-21 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c928cce-a22b-35df-bef6-d15c60cd187d | -8.73748 | -47.98385 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 713a2dc2-4964-3d29-9e9c-7bcb79d12c4f | -7.28135 | -49.98718 | 2025-06-21 04:34:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45ddc64f-b0c9-3c7b-bce8-dcddef64bcc7 | -11.57685 | -54.56377 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 61be4a5d-a4d4-30ec-a081-1a9314b827a1 | -11.17498 | -46.65646 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 07e72885-05c5-3a24-9051-e764c6557290 | -14.81427 | -48.47718 | 2025-06-21 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89519e70-2860-39b5-9b1f-692898595216 | -8.1344 | -46.82397 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7586d60-8136-3ab1-b5db-65c266f87f7c | -12.51075 | -58.34431 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5d87265-5a59-3624-9a48-c04ee190b1f9 | -11.07028 | -49.62315 | 2025-06-21 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb6cf0ee-768a-3d7d-ae04-1f8bc68429a9 | -9.46626 | -57.83861 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bd5a1bc-b89e-3594-bebe-b9104c06ace2 | -12.54825 | -48.49898 | 2025-06-21 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5536b196-d57e-38ae-80e8-a729d980e0d6 | -12.28661 | -50.10845 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b9c4a03-9baf-38b6-ab62-86d88f44650a | -10.53846 | -46.76717 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eef3d780-8367-3d86-ba2d-3d2986ef5ad0 | -9.45936 | -57.8419 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2376136f-7053-38cf-9767-8c491e26707c | -10.8604 | -53.7558 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5d32ed3-b2e0-3b04-8df3-c60c48ae9fbb | -13.24172 | -49.83789 | 2025-06-21 04:34:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fe9b113c-1c6f-38ca-b5b7-7f780f2f6666 | -13.0964 | -52.29637 | 2025-06-21 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb367adc-dc3a-37ce-a0c6-5da71bdcd0e0 | -10.87128 | -53.76307 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b17ef98-269c-3bb7-8000-efc3db0bddb4 | -9.47178 | -57.83387 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4653af17-550b-3c0b-bcf5-db25007ddf31 | -10.50961 | -47.58315 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8f8683e-197a-3716-a555-dcb9b84b01b8 | -13.25871 | -46.83242 | 2025-06-21 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 272650b9-034f-373f-99ca-ef18e38f1418 | -12.97164 | -54.68508 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67a85ace-75ad-360d-87b2-c2a6cd77625b | -8.18544 | -47.77184 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75c3429e-7bc2-3656-9af6-5b67c63c1944 | -9.26288 | -46.90505 | 2025-06-21 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3113acf-a1dc-3dc5-9810-e078ea8012ca | -8.73694 | -47.98733 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5219286-0fe5-35e4-9987-5dfbbb8db0ef | -8.98631 | -49.8658 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d12ca835-163e-307d-b739-f8a743f06e33 | -9.47953 | -57.82165 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d33cad70-4e59-3148-b288-243042f5b2ee | -12.47837 | -54.42369 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3537255a-961f-3d66-862b-e93976b9e504 | -12.57362 | -58.37963 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dc24901-6429-30ce-9c3c-b7f150c98960 | -9.41703 | -48.42646 | 2025-06-21 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1465734-db68-3990-b20f-c32d44af12e7 | -11.78888 | -57.24865 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| b86853a0-9f58-309d-8e46-84527ed228da | -12.76697 | -44.41125 | 2025-06-21 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8379f0b5-ea0b-3bb5-b136-e91f041a9d68 | -14.07416 | -53.37695 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5bf3614f-d219-36a9-b031-d9a107d764fd | -8.70515 | -50.04679 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 630cef81-48fc-3e61-ae17-906352c34dfd | -12.57423 | -58.37645 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fdefd4e-f056-3864-b348-5c8f10eb2ee3 | -13.14746 | -56.80972 | 2025-06-21 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d13edbcf-6e70-33f9-991b-1605c9f4b7ac | -10.52412 | -47.57806 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 947ee524-1700-3862-b508-129f17813963 | -11.79373 | -57.24963 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README14.md)
