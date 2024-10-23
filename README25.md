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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 333dcf82-79b6-3e48-ba64-00cc5db7f68c | -6.67673 | -43.03862 | 2024-10-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec4a5213-6853-3312-bb20-5cfbe135439b | -6.67538 | -43.04682 | 2024-10-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ce5fe75-4b6e-353a-899e-c3e06ef57f22 | -6.67471 | -43.05094 | 2024-10-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55e0c9cf-5bb9-3424-8edd-d99e1c9fd029 | -6.67247 | -43.04214 | 2024-10-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 751f7d03-7940-30fd-848b-8c4e79477817 | -6.6718 | -43.04625 | 2024-10-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ba86501-84db-34b5-9d5b-c9653824f7d2 | -6.67113 | -43.05035 | 2024-10-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca5fd74d-9b6a-3a04-a513-812857d4c876 | -6.63544 | -43.45059 | 2024-10-23 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 903db2aa-9f2d-368c-8f5e-d3d3b009dd06 | -9.18165 | -43.01833 | 2024-10-23 04:00:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 81faab14-6f6d-37bc-9a99-83b3c2e7f67d | -9.17424 | -44.12863 | 2024-10-23 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f584aa6a-6888-3e18-ae8f-b84185baf97c | -9.17376 | -44.12709 | 2024-10-23 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6896061e-11fb-3626-9be1-a8e49f25704c | -8.71392 | -44.00852 | 2024-10-23 04:00:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db36e117-cd50-3ab9-8307-3632cdc12e71 | -8.71319 | -44.01295 | 2024-10-23 04:00:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d91f06b3-c49b-36b7-be4f-0056268f0ef2 | -9.64606 | -43.9089 | 2024-10-23 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1f4d3d5f-39de-3e42-8064-b1f518ce06b2 | -9.64471 | -43.90977 | 2024-10-23 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92296cc8-d872-37e6-9608-7360678448b7 | -9.51499 | -43.21585 | 2024-10-23 04:00:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c71cb622-1b28-3c30-bfeb-a4ce02f7057b | -10.70296 | -44.3819 | 2024-10-23 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bad36015-771c-39b7-b319-433ea1a05f06 | -10.70222 | -44.38625 | 2024-10-23 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0194809-cda2-3c3f-b03c-a4912c30a668 | -10.6993 | -44.3813 | 2024-10-23 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ad9aa0b-5774-39dd-9c92-a24570e12836 | -10.60713 | -44.282 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 635200f7-bc5b-3526-acf8-21063ef13804 | -10.60422 | -44.27709 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2ee0c22-8c1c-3f5f-80b1-f874ce83191f | -10.6035 | -44.28135 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c220e64-1679-329b-9b51-6c22de803680 | -10.60278 | -44.28564 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 063813b9-3e09-340d-aa8f-f2fb0a3d8c1a | -10.59986 | -44.28071 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2aee4f65-8cce-3c96-9697-7d776bebf247 | -10.59914 | -44.28499 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b9ed762a-a84d-3204-858e-4a3c190562d9 | -10.58315 | -44.29101 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 649b6cdf-a869-3eff-9b66-fc54414e8136 | -10.57952 | -44.29038 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60de87fa-456e-3582-9125-111f2ee12c96 | -10.57878 | -44.29469 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29182275-f38a-34f6-8c70-e0db9fc427b4 | -10.57588 | -44.28975 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f313807f-2390-3e59-9d18-4440ffd91b3c | -10.57515 | -44.29406 | 2024-10-23 04:00:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad8b8431-9497-309f-bbe4-e59d72c92261 | -11.61377 | -43.74847 | 2024-10-23 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caf206bd-39c7-3828-b02f-586e817a2362 | -6.26561 | -44.96651 | 2024-10-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dba14240-7113-3e6c-8997-27bda77111e7 | -6.26159 | -44.96576 | 2024-10-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d435f1ab-a398-319c-bbe7-ad97668ba906 | -6.07177 | -44.63018 | 2024-10-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 489de26d-3a0b-3379-ac37-d365f9bde6c2 | -6.06782 | -44.62949 | 2024-10-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c29a4f9-e5b1-3348-a181-f88e74610e92 | -6.06387 | -44.6288 | 2024-10-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4c231eb6-df9f-37f0-97b2-d2a52f955f44 | -5.6996 | -43.53133 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18c8fa17-0ea5-32f9-829b-4cba374e78a3 | -5.6059 | -43.93736 | 2024-10-23 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cce834b-e0d0-32ef-b1e3-a1ee4168bb83 | -5.51006 | -43.68984 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41b3b22d-bdb5-3710-a1f5-20754464a7c7 | -5.50931 | -43.69445 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 122f7f02-40d0-398d-9a67-e267cedb1a56 | -5.50856 | -43.69904 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0d44831e-a846-3364-bc7d-dda8d821f308 | -5.50782 | -43.70362 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 469b5e27-01bf-3853-b970-1ef963f1ac9d | -5.5063 | -43.68919 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab12a6c9-fafb-3871-85db-8a5a16f0225c | -5.50555 | -43.69378 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f43adcac-08a5-3340-b61b-9c2d968e4f3a | -6.25413 | -44.14144 | 2024-10-23 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 78f6d4ff-a5fe-3fc0-bc08-f4a843b41557 | -6.25335 | -44.14613 | 2024-10-23 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 846bcc08-3887-32cd-a80b-309aa49db142 | -6.25256 | -44.15085 | 2024-10-23 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0e37d2a2-dba1-34c5-8094-3c704b727d22 | -5.92758 | -44.71976 | 2024-10-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f54ac47-2a7c-338f-8895-0674a6e56ecc | -5.88165 | -44.91446 | 2024-10-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6a248b6-92b5-300e-822f-2988b246cdd9 | -5.6198 | -44.83411 | 2024-10-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5fe448cb-109b-32f4-80bf-151ad1d767c7 | -5.61577 | -44.83343 | 2024-10-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8597c7ee-ff7e-3d63-93d7-295cd32e64c7 | -5.6079 | -44.49569 | 2024-10-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eec31bc2-7cb1-36da-ba64-18d26787307e | -5.58262 | -44.88253 | 2024-10-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| eb639834-03dc-3835-8926-f3c9ee161f18 | -5.58201 | -44.88616 | 2024-10-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 38d3068c-5ded-38a5-8fea-4751e37a35c2 | -5.5798 | -44.87462 | 2024-10-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41096aa9-1d7c-375e-8302-2585cab125eb | -5.57858 | -44.88182 | 2024-10-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5bd39d6a-a925-3fc0-9fd9-3d41b4873ffd | -5.57797 | -44.88544 | 2024-10-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1789bc86-dfbf-3b00-81a5-558dd4735ce3 | -5.46266 | -44.42379 | 2024-10-23 04:00:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05806a69-1b80-37d3-8bd5-b4f5d592ccfe | -5.44261 | -44.69311 | 2024-10-23 04:00:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76c5b04e-cdc8-3721-ba43-41df78b93306 | -5.4386 | -44.69246 | 2024-10-23 04:00:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b8026b6-8bf4-3344-837d-d8509b486a4f | -5.42113 | -44.79829 | 2024-10-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f3fc697-82bc-3d48-a4d3-1f5b8bed2be4 | -5.39993 | -44.62847 | 2024-10-23 04:00:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dbcecc0-54e1-3566-8ee0-bbdb3d5bf990 | -7.31896 | -45.28359 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 456e7626-f651-3c46-8585-c81a6e87bc8e | -7.31837 | -45.28715 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 627e009d-3509-3cc3-a9ef-ffbd6c8e4038 | -7.31491 | -45.2829 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19998109-88e9-30f6-8f82-bc98bc038c17 | -7.31432 | -45.28646 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09f5cde2-7a61-36bf-8aae-f4d1037ce8ef | -7.19044 | -45.1547 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16490b7d-bec9-38d7-8f46-4fecfe69f137 | -7.17892 | -45.05273 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b783705-2ae0-3358-b8d9-303ce81f0c79 | -7.17219 | -45.14053 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52a19977-0faa-3a9b-bf92-4ceefbebe654 | -7.17159 | -45.14405 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7284461-e7f8-39e7-8797-d18c30bc4d25 | -10.96916 | -44.60343 | 2024-10-23 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd95ed5f-9d98-3162-a960-d781b20c0896 | -7.16877 | -45.13636 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 08cbb911-33c2-3092-8ae3-fd47e75df05b | -7.16816 | -45.13988 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ff40dd1-8ea0-30f7-8961-f1650497434f | -7.16755 | -45.14347 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 18119486-2731-3c8a-aa93-de6d4bd25626 | -7.16474 | -45.13572 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d2a8733-4446-3421-a72a-14fbf6fc017d | -7.16413 | -45.1393 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7d2fa8a-526c-3c92-a2b2-0ec173483f77 | -7.15444 | -45.04147 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95b34cc3-c260-3c89-96d2-9fa90ddd8c6d | -6.98156 | -44.57858 | 2024-10-23 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3ab19f6-e88a-35e0-944e-32f2af45ee4b | -6.94289 | -45.21119 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6eb23b7b-23f4-3ef0-afc9-db739854c5fe | -6.93823 | -45.21406 | 2024-10-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 927e9af6-63d6-364a-b4cd-ce027a9afbaf | -6.83921 | -44.38954 | 2024-10-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 143a5546-05f4-38d7-bd48-3e47d8e5063b | -6.83666 | -44.39116 | 2024-10-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d81cdfb4-a252-3676-85ce-23626e38ca5e | -6.7187 | -44.6832 | 2024-10-23 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70f6fab1-49b5-3c53-8d15-a7acab09ed54 | -6.56701 | -44.03571 | 2024-10-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d7a48ae-f268-31e4-b695-a6105f6cc3d8 | -8.6261 | -44.83167 | 2024-10-23 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 297d8ec0-c0fa-398a-a771-241065dd4759 | -10.03184 | -44.51407 | 2024-10-23 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0a52478-54c7-369d-8bd8-0672e60848bd | -10.87887 | -44.53952 | 2024-10-23 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d8f3397-9c3a-36c4-9cf9-bdb99f9a66e4 | -10.78744 | -44.52566 | 2024-10-23 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c52bbc69-0b08-3291-833e-39517a7a3e92 | -10.75805 | -45.02043 | 2024-10-23 04:00:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2da43ca0-03eb-3c02-9bb2-13134bd093b5 | -10.75761 | -45.02231 | 2024-10-23 04:00:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7e78a086-8ec0-36af-8b4b-5a71d9f03573 | -10.72476 | -45.21103 | 2024-10-23 04:00:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72edf485-a701-30b5-a2ff-67fa962675a8 | -10.72258 | -45.2089 | 2024-10-23 04:00:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74632e60-523c-3b53-963a-e1c25ee4547d | -10.62523 | -44.59468 | 2024-10-23 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42c78074-d0a7-34b5-849a-453964a72810 | -10.44882 | -44.8968 | 2024-10-23 04:00:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43af13ec-96d9-3554-bcfd-90bc8278c655 | -10.44505 | -44.89614 | 2024-10-23 04:00:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d9c3b30-2f82-32f8-9cbf-0defce4b80d0 | -10.44427 | -44.90082 | 2024-10-23 04:00:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2f09bb6-b363-3e59-9cad-406f670b66bd | -10.44127 | -44.89554 | 2024-10-23 04:00:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83a25179-69a5-371a-9f72-b2221e741eb0 | -10.44049 | -44.9002 | 2024-10-23 04:00:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f502805-f93c-3c9c-bd34-e625ee64fe8e | -11.134 | -44.95722 | 2024-10-23 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c2e6df1-af80-3e9e-b0c8-260aba3c66cd | -11.13025 | -44.95657 | 2024-10-23 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dedae1a-9987-34ff-850c-449d8f19c29c | -11.02994 | -44.88502 | 2024-10-23 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)
