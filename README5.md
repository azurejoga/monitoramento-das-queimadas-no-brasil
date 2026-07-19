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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8038d47-cc26-3d44-8f58-83f782e4e241 | -22.23419 | -56.00491 | 2026-07-19 04:04:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a857607-cd7a-3bfd-8514-99e57f1637f8 | -22.63244 | -43.61783 | 2026-07-19 04:04:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7d1120f8-d334-3f17-b979-74d05a2ad3ff | -22.91811 | -43.43345 | 2026-07-19 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8c44fb8e-425e-3150-bef7-a1244413c7ce | -22.90906 | -43.44392 | 2026-07-19 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3e27d39d-bc46-3912-90bd-fa3843493f29 | -23.2907 | -46.15511 | 2026-07-19 04:04:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 735addba-c68d-322c-975c-33f8bc978548 | -19.7425 | -46.47389 | 2026-07-19 04:04:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfd60677-81d5-39ea-8a62-8c93ab1c1c56 | -22.46223 | -43.10003 | 2026-07-19 04:04:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2cbc8b2b-e1fe-3fa0-8780-040048fbf405 | -22.25245 | -52.88132 | 2026-07-19 04:04:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 93249012-e094-358b-8f18-e1c7e8f939a4 | -22.72235 | -43.47775 | 2026-07-19 04:04:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 96094151-2b0f-3f2f-8912-8da2ca0ce1d9 | -19.72371 | -46.17266 | 2026-07-19 04:04:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a07bab3-6181-3231-aed3-07c2e8a72b85 | -22.22736 | -56.0019 | 2026-07-19 04:04:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5263ddea-560b-354f-af44-6100a465d15d | -20.74135 | -42.04699 | 2026-07-19 04:04:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e1ad705e-9ac8-3d31-a511-397fed8c1b40 | -23.73618 | -46.62021 | 2026-07-19 04:04:00 | NPP-375D | DIADEMA | SÃO PAULO | Brasil | 3513801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ea203db9-bd13-36ba-b9a2-30e59fe0f785 | -19.98575 | -43.96944 | 2026-07-19 04:04:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4102d96b-ddee-34b2-96de-ef97e899a948 | -19.74162 | -46.46992 | 2026-07-19 04:04:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0c02b60-df08-331a-a9f4-5dbda502d2d6 | -22.23201 | -56.00729 | 2026-07-19 04:04:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2118f76f-4d48-3860-a31b-109a5a2a6d0f | -22.79615 | -43.77713 | 2026-07-19 04:04:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5a6eb01d-d7c5-38d0-9ffa-36c4ec840930 | -19.17797 | -47.35361 | 2026-07-19 04:04:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3ca342f-128b-3e96-b729-6ababf0638cc | -23.76404 | -53.28176 | 2026-07-19 04:04:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| a3be3198-bfa1-3293-ae7b-d94a4569c112 | -29.00598 | -50.37302 | 2026-07-19 04:06:00 | NPP-375D | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74b44b07-d22d-3627-b4c2-7a93142d53d3 | -29.55045 | -51.38855 | 2026-07-19 04:06:00 | NPP-375D | HARMONIA | RIO GRANDE DO SUL | Brasil | 4309555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 75db1865-ba29-359b-b747-a9f7d04f7879 | -29.90868 | -54.6742 | 2026-07-19 04:06:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| f99ca6bd-114d-3ce1-a406-32ba7b461b3a | -29.90753 | -54.67877 | 2026-07-19 04:06:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 70295b49-d0e5-32c1-9bea-6c388a34eca6 | -30.412 | -52.60944 | 2026-07-19 04:06:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 8c92ae6d-321a-3b28-a928-09dcd36fa96f | -29.54573 | -51.38711 | 2026-07-19 04:06:00 | NPP-375D | HARMONIA | RIO GRANDE DO SUL | Brasil | 4309555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5076341a-e77b-3d6f-8a84-6d544026c975 | -29.14071 | -50.8196 | 2026-07-19 04:06:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6ee178de-4b52-3862-b862-b0f21added17 | -29.5444 | -51.39295 | 2026-07-19 04:06:00 | NPP-375D | HARMONIA | RIO GRANDE DO SUL | Brasil | 4309555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d9661b1f-00ae-3cce-a75e-a5beceaa2f37 | -29.00716 | -50.36766 | 2026-07-19 04:06:00 | NPP-375D | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dac3abbd-c732-315e-81e7-61ba16b3d00d | -29.54911 | -51.39441 | 2026-07-19 04:06:00 | NPP-375D | HARMONIA | RIO GRANDE DO SUL | Brasil | 4309555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 885c51a2-942f-3270-9b01-c5b3bd1d16db | -28.61312 | -49.23411 | 2026-07-19 04:06:00 | NPP-375D | MORRO DA FUMAÇA | SANTA CATARINA | Brasil | 4211207 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cc3ad914-bba7-3798-b930-9b2f27cf9613 | -13.6764 | -48.7786 | 2026-07-19 04:10:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 94b80562-f8e0-3211-a7c4-13c5dffc9db2 | -5.93437 | -43.64765 | 2026-07-19 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30753a90-3bb8-3046-bb86-dc7b26de80b3 | -7.29902 | -46.25051 | 2026-07-19 04:17:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6be70c6c-1cf4-3d8e-a266-d35d61840e8a | -7.30455 | -46.23911 | 2026-07-19 04:17:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a7634dc-27a2-30ea-bf40-b5a7d1212f73 | -7.30256 | -46.25109 | 2026-07-19 04:17:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d4de37b-89fa-3ca7-a4de-dcdfddebd087 | -7.11532 | -44.04277 | 2026-07-19 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a79c764d-eaff-3859-9f17-d1042738fe5b | -5.93493 | -43.64418 | 2026-07-19 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e74fb267-1f5b-3bcb-8961-3aa0a565499a | -6.2958 | -43.64116 | 2026-07-19 04:17:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c610ad6-188a-33cf-b93d-1d165a97af4f | -4.14167 | -49.27703 | 2026-07-19 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6d4dfb8-796b-368d-b65a-8acd7af363af | -5.72959 | -49.09961 | 2026-07-19 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cb536e1-024b-3179-a57d-6e383ac30af1 | -4.03659 | -49.25741 | 2026-07-19 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 143d8a64-9f9b-3fae-a37c-fc5b2d5989bf | -7.64748 | -37.27099 | 2026-07-19 04:17:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3071f736-77ef-30f8-968c-f1501adc49cd | -6.63882 | -46.54086 | 2026-07-19 04:17:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cf2efcd-97ea-328a-843a-ba651b2b0f48 | -5.52699 | -45.27092 | 2026-07-19 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 307be42c-7b67-3a37-8471-42a05ee3c49a | -7.11588 | -44.03929 | 2026-07-19 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 457bb286-429b-388d-9949-db335c60eba7 | -5.52353 | -45.27039 | 2026-07-19 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3201e816-e795-394b-bdb5-c60a4626cde0 | -5.73389 | -49.10029 | 2026-07-19 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 037adba8-3f7d-3a7e-834a-c50fe937724b | -6.73354 | -44.36623 | 2026-07-19 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8484e18-db50-320f-83e9-5e049ca2913d | -4.58345 | -46.29779 | 2026-07-19 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a25aeb21-bc65-35ba-983e-c53ffd0873bb | -5.73029 | -49.09555 | 2026-07-19 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 926f4e47-563e-35d2-b11b-1d434804e756 | -4.6697 | -43.22288 | 2026-07-19 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff04b5cc-dc1a-3fbe-9303-749455d18e51 | -5.7094 | -45.66336 | 2026-07-19 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5e90b40-35c5-30da-80e5-4c5a34315ec0 | -7.29548 | -46.24993 | 2026-07-19 04:17:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 037e968e-40b5-3131-8917-78e888853d27 | -7.30101 | -46.23852 | 2026-07-19 04:17:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3af29b80-7dc2-3620-9801-968927f8fa19 | -5.79351 | -43.63556 | 2026-07-19 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52bfeb43-0e17-3fec-ab29-821b302d91c2 | -7.11808 | -44.04677 | 2026-07-19 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19be747f-47cc-3ce3-9ecf-469eed3fa9a9 | -6.90098 | -45.66971 | 2026-07-19 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12697cba-4775-3067-9f56-2353007a8b37 | -7.30323 | -46.24706 | 2026-07-19 04:17:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84838af8-f606-31ba-a45b-521ae34811cb | -5.71003 | -45.65945 | 2026-07-19 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d54bf1e-2c6e-340b-84e7-7f625a98a464 | -4.65869 | -43.22821 | 2026-07-19 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f882295-8271-323d-97af-c98e4a559edc | -5.7129 | -45.66391 | 2026-07-19 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9616c8c-1691-30a3-9f0b-7b75b0cfd5ff | -7.29969 | -46.24648 | 2026-07-19 04:17:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 65cc0412-e0c1-3c6f-b7b4-9220f619d84f | -4.6653 | -43.22926 | 2026-07-19 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4642f3b-59d7-3860-916c-ac33957c7f27 | -7.8132 | -42.80972 | 2026-07-19 04:17:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5bd08600-8e7c-34a3-b0fe-80d2976649f3 | -4.66199 | -43.22874 | 2026-07-19 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6b56f44-8532-3c40-822a-ec2302b6dc28 | -6.5989 | -41.62938 | 2026-07-19 04:17:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f8d7c808-e534-33af-a877-d674b0904419 | -4.66254 | -43.22528 | 2026-07-19 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1d080ba-24d8-3e51-9bb1-7b6e942eb9d7 | -7.30035 | -46.24249 | 2026-07-19 04:17:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46836110-53b3-37d1-b884-a71d8bf84210 | -5.92775 | -43.6466 | 2026-07-19 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63205da0-58a0-3780-9d34-311b79ecb2f2 | -5.8029 | -43.64059 | 2026-07-19 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7676da2e-b997-3607-b747-a137fefef882 | -4.6664 | -43.22235 | 2026-07-19 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 404bd378-781f-3f9c-803a-a91a40355584 | -6.7302 | -44.36568 | 2026-07-19 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbd4f23e-69a9-34cd-a7db-eb501f441ef5 | -7.29615 | -46.2459 | 2026-07-19 04:17:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5df33d58-d387-3a5b-a613-de4b4da418ea | -3.97183 | -47.20068 | 2026-07-19 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 154248e5-3772-33a2-a936-b3620d0cb2f7 | -7.30389 | -46.24307 | 2026-07-19 04:17:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b38af35-649c-3063-aff6-150e100129aa | -4.66585 | -43.2258 | 2026-07-19 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7627b9b-b2ab-3100-a308-dd36ace1d2d4 | -6.90418 | -48.0446 | 2026-07-19 04:17:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 039b1f5b-a26c-36cd-93ab-7cc56cd36ff3 | -7.11864 | -44.04329 | 2026-07-19 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2488284c-08d7-3246-a4e2-32ea3a6fdb57 | -5.80345 | -43.63713 | 2026-07-19 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1c2882b-5b07-3423-8a31-b7d986e7423c | -4.03429 | -49.24355 | 2026-07-19 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 484c2c31-faf0-3ab5-866b-f980f6353244 | -4.03357 | -49.24793 | 2026-07-19 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9c00230-ddf6-3d05-ad60-6c5477c23e05 | -3.84022 | -49.05243 | 2026-07-19 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0693e01-2f43-34b3-ab3b-2a957ede78cb | -4.03875 | -49.24429 | 2026-07-19 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8559a2e-4a04-3b33-b813-bfffd371d217 | -7.11477 | -44.04625 | 2026-07-19 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dc0aa53-8dd8-314f-adf3-43cb687f15e4 | -5.92284 | -46.24439 | 2026-07-19 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8ea0fa8-d623-3a62-8833-b626fd46ad17 | -4.03732 | -49.25297 | 2026-07-19 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fa10312-837b-3500-a47e-dd64c4175e45 | -5.9283 | -43.64313 | 2026-07-19 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61be0afb-fb54-37ce-a9d3-0be5aba033b8 | -10.66374 | -44.46603 | 2026-07-19 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46535984-415a-3585-b436-ec32cc63f842 | -12.10785 | -44.936 | 2026-07-19 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b08df2ea-c8ad-3ae6-bd28-3e744492e005 | -11.97224 | -47.11322 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8f11af83-b63d-3f65-b4aa-772e6e1a552c | -13.56331 | -47.7064 | 2026-07-19 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d92db86-c4b4-31a7-a006-f6dc465cabe5 | -10.4768 | -49.14345 | 2026-07-19 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fc73780-74ed-3e68-855e-63bfbcfda49a | -13.56469 | -47.69815 | 2026-07-19 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dae6b68-63a1-3ea4-9eb7-0e08f961b17f | -11.98407 | -47.1071 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d6ff41e-6466-3321-a42d-08034690c25d | -12.6625 | -48.22071 | 2026-07-19 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0f80f830-17f6-3e4d-bb73-0fe5851ea5f9 | -11.97424 | -47.10131 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db822abf-9125-3e81-a61f-6d60cd3e4658 | -10.4253 | -46.32347 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39cb2657-0ce0-3a09-97b9-6b935de56edc | -11.63061 | -47.95602 | 2026-07-19 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1fc2ce1d-978a-3835-bcd2-6f7cf6c6f426 | -10.90128 | -50.32895 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ecec746-b32d-3842-972d-84d5581cb88f | -13.564 | -47.70225 | 2026-07-19 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README6.md)
