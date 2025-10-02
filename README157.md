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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 250e0e5f-53d2-34e6-a8d1-c7fc0498bf84 | -11.8349 | -47.7067 | 2025-10-02 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| dda0fadb-805b-315a-9f15-88d52b8f393c | -8.8929 | -46.6072 | 2025-10-02 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 44a07afe-1fa0-3432-924f-169b1d5cd4e9 | -7.5746 | -46.8 | 2025-10-02 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3aaed782-3814-3b1a-bbb4-a89bc6f1648e | -5.7937 | -43.0766 | 2025-10-02 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 4b9d137b-fb17-3856-8f01-265c482f0825 | -8.1513 | -44.1397 | 2025-10-02 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 7c5b6b95-743a-3fb6-b7fe-11af9a5c0eef | -9.3389 | -45.7266 | 2025-10-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 22e30a04-931a-33f1-a748-daf6b4b5a0b5 | -10.8234 | -46.6313 | 2025-10-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 3dab5b61-51b0-3286-afcf-970cb033498f | -8.5599 | -44.6494 | 2025-10-02 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 201.2 |
| e4ab83c6-21ed-3ada-9af6-03b2073b9d7b | -14.4947 | -48.4329 | 2025-10-02 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4ae8f9fd-33e6-39cc-a85c-1061de998a1c | -11.2803 | -47.8223 | 2025-10-02 13:50:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| bb0831e3-3961-336a-be93-793a7ccc3f2d | -6.0997 | -42.4865 | 2025-10-02 13:50:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 2464c2f5-b76b-3e28-839c-9e36dee2451e | -15.3072 | -45.0477 | 2025-10-02 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 151.6 |
| c8c421f3-a827-360a-8155-d2938fc296d6 | -10.8622 | -46.5814 | 2025-10-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.3 |
| b5b0a4c6-73ae-358f-bfa0-2009c8addc82 | -7.1914 | -47.6257 | 2025-10-02 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| d3bbde5f-9f37-3876-9da9-bbc597173ec8 | -9.3357 | -45.9532 | 2025-10-02 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 0c9e6e8c-1bf1-3a2e-b799-f712de2e88e4 | -9.9186 | -43.6978 | 2025-10-02 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 65e37c5a-5893-394c-9d7a-f7d20b6c7daf | -8.6722 | -47.6924 | 2025-10-02 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 25779e67-153e-318e-b0f4-b6bf18003879 | -6.2411 | -45.3198 | 2025-10-02 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 71cb6d4c-ed22-3208-8ec1-37be3fab8220 | -8.5201 | -47.8386 | 2025-10-02 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a6132466-2dab-37d0-bebf-0a2daab52201 | -8.2094 | -45.5301 | 2025-10-02 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| baeed6f7-2c14-3b05-86b1-e52ae8071aff | -11.868 | -48.0126 | 2025-10-02 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| af26a9af-5c51-303b-a5d2-f913a04b33d9 | -15.2738 | -49.3073 | 2025-10-02 13:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3f88484e-6ae0-3cb5-b46b-114817a880ca | -8.0004 | -47.3151 | 2025-10-02 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 879e2453-f65a-3948-b011-fc5c1dd4f57b | -14.406 | -46.1184 | 2025-10-02 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 104.1 |
| c4173c10-eec1-3a61-a7b7-28ae359b5f3c | -7.7755 | -42.5152 | 2025-10-02 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 200.4 |
| 97954431-8744-33be-bb73-b728b3a4e497 | -6.2138 | -44.2502 | 2025-10-02 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 82bdc2be-d61c-3467-b73f-350cc56b60c0 | -13.3131 | -47.5876 | 2025-10-02 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 04a2f3a6-20a1-3c08-933f-e885488197ce | -11.0518 | -46.6246 | 2025-10-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 239cece4-2e20-3357-85ee-0c2a515b7046 | -11.9276 | -47.8719 | 2025-10-02 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 6820afbf-30e3-33c9-8e88-1a11d6028cd3 | -9.9031 | -45.978 | 2025-10-02 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 15a18c6c-665a-3f52-a09f-babe7504f212 | -6.7816 | -45.5703 | 2025-10-02 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ae05dd79-c7a0-30b0-8117-d8999b752b5e | -8.5204 | -47.8167 | 2025-10-02 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 8349d1ea-2228-3a42-ae0e-bd5fd424860b | -13.1542 | -47.8568 | 2025-10-02 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 80e0ed06-2bc8-314c-83f8-315809b9ea73 | -15.3067 | -45.0713 | 2025-10-02 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 2cbe2e97-fa21-3c78-acd9-e735b42cf47e | -13.3282 | -47.8089 | 2025-10-02 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| e32c10da-7dc8-3586-875b-25991c89bb75 | -12.5001 | -50.2453 | 2025-10-02 13:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 3b21d20b-59f7-3e3d-8794-46556c4778c1 | -8.8926 | -46.6296 | 2025-10-02 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 73b486b4-3a7b-38d3-8971-a811cf6885db | -9.4272 | -47.5722 | 2025-10-02 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 206e37c7-c1bd-3ed6-a218-c23702baf0aa | -10.8424 | -46.6289 | 2025-10-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 5c3170f6-b972-3684-a8a9-d65b09dee983 | -12.7002 | -48.5637 | 2025-10-02 13:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f67c41fd-d08e-3e71-9b76-a1eb94616004 | -9.8896 | -46.9226 | 2025-10-02 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| e289b283-4b76-3b5a-811d-e2a18fe26f2f | -8.2094 | -45.5301 | 2025-10-02 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 260796cd-aa6a-360e-bc6f-c72aa8fb3ec7 | -11.8238 | -45.0132 | 2025-10-02 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| dca2b2d7-15ca-349b-b424-ec0fbc9555f8 | -15.2031 | -48.0045 | 2025-10-02 14:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 7f1fa14b-e2a3-3b68-8798-c1e1b3f94fb5 | -6.6756 | -41.406 | 2025-10-02 14:00:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 140.5 |
| f07dbb8b-b041-3800-9a35-6e49ef451fa4 | -9.9031 | -45.978 | 2025-10-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 06b67dad-672c-3eb0-bcac-eb7dcd3ec3e9 | -6.1981 | -43.9286 | 2025-10-02 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f205d176-756d-3876-9380-9dad44f20035 | -6.6976 | -42.8354 | 2025-10-02 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 115.5 |
| 0d4b0071-fd30-31d4-920e-3aa87c85504a | -11.8349 | -47.7067 | 2025-10-02 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b6e31267-5c12-3f30-95b9-deb50ed94f87 | -13.7873 | -51.2189 | 2025-10-02 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 5ee06909-6c98-307b-8c27-309a28353c14 | -15.2738 | -49.3073 | 2025-10-02 14:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8b25d2d7-06d2-3496-9c01-3021d79db2db | -6.6567 | -41.4079 | 2025-10-02 14:00:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 571acb45-2f6d-3fca-87ff-ef4bd4fa2e15 | -8.8929 | -46.6072 | 2025-10-02 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 167a279c-740d-3cf3-b36e-b24218408d45 | -8.1513 | -44.1397 | 2025-10-02 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 303.6 |
| cb70b8d2-7971-3802-81ae-3b4aa51627e4 | -5.323 | -43.3221 | 2025-10-02 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 381c1889-08f9-3b00-9dc4-9978747d45fe | -6.0997 | -42.4865 | 2025-10-02 14:00:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 13992370-5a95-3d9c-a0ed-7be4f1185c46 | -15.5379 | -45.2375 | 2025-10-02 14:00:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 20528d52-de24-37cd-b922-c050bd735550 | -13.7876 | -51.1974 | 2025-10-02 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 4f4e8327-632b-329c-8be3-87c8ce1e919f | -10.2025 | -50.3109 | 2025-10-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 643aafe1-4fd1-3d20-a19c-4a5f8ef54ff1 | -6.1984 | -43.9055 | 2025-10-02 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ac6beb9e-f6ca-319a-95a1-c3e246263f9f | -14.3114 | -45.9967 | 2025-10-02 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 21b39d64-d238-3b79-bb12-5e3f675911de | -14.406 | -46.1184 | 2025-10-02 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 113.9 |
| ca36bbe5-6529-3a2f-83e8-4a48baadc144 | -14.4065 | -46.0953 | 2025-10-02 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 19277c20-a92b-383b-8cdf-e82c246c0aad | -10.222 | -50.2662 | 2025-10-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f448c748-799f-3a22-a359-300ab3bbcafe | -7.8092 | -47.6399 | 2025-10-02 14:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7a03b875-8653-3ce5-936a-44807209f159 | -6.657 | -41.3837 | 2025-10-02 14:00:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 612d8246-b0dd-3a83-bbdf-3040ffcf0720 | -6.6758 | -41.3819 | 2025-10-02 14:00:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 133.2 |
| 6752785b-fcf0-3336-bbf7-a99855bc910c | -13.3001 | -47.2529 | 2025-10-02 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| aa99f2c2-9557-32eb-9d30-a172566338e6 | -11.8101 | -51.7957 | 2025-10-02 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e8fac042-bd4d-36b0-b310-0a0e7126c5f7 | -11.843 | -45.0104 | 2025-10-02 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 339a3581-20e3-36fe-abca-c65e98e58a01 | -7.7311 | -46.2289 | 2025-10-02 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f68027f8-7a9c-354e-a38e-6bcdb4a8b743 | -14.3139 | -45.8811 | 2025-10-02 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 77b2cb5e-159a-3f09-8d32-b4ab339f72f6 | -5.338 | -43.7623 | 2025-10-02 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 90d1835f-98cc-3bf8-94da-932824f3b27f | -7.8879 | -47.3031 | 2025-10-02 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 181.5 |
| fc008790-fc27-3112-abbf-a0ab3c0af347 | -6.6978 | -42.8118 | 2025-10-02 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 136.8 |
| 455d38c0-f3ea-3a6a-8442-52b4539ccfed | -14.2924 | -45.977 | 2025-10-02 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 104.4 |
| d5d15ff3-6e7f-3a19-9ca0-7c0bde60b7dd | -9.062 | -46.6565 | 2025-10-02 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d05bfb72-5f46-3b32-b678-14503c74b1f8 | -5.6236 | -43.23 | 2025-10-02 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 5421aaa9-1042-3c57-b91e-3f37990a2857 | -10.9748 | -46.6794 | 2025-10-02 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| cf2c2662-bc45-3065-b2ba-1996cb6807e4 | -7.8882 | -47.281 | 2025-10-02 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 8a0553f5-0f89-325f-8f9b-6004b30ad7bf | -6.679 | -42.8136 | 2025-10-02 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| a484420b-d4b4-3027-87b4-e744a969eaae | -10.2028 | -50.2895 | 2025-10-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e7dcb436-abba-3167-9bed-5034fc3f108a | -8.1702 | -44.1377 | 2025-10-02 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 422.2 |
| a2eecd95-8f1e-328e-9470-9968b6629c08 | -6.6604 | -42.7917 | 2025-10-02 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 7274f803-d71e-34a6-b805-59c70d23b760 | -11.8438 | -44.964 | 2025-10-02 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| f2186dc3-1384-31d2-a7e6-268aae302b6a | -6.7818 | -45.5477 | 2025-10-02 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b0ae5b66-92da-3e97-8209-2e83523b5017 | -10.2214 | -50.3089 | 2025-10-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 801cb549-9109-395c-acda-a4bd84853cc9 | -9.336 | -45.9305 | 2025-10-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 0cb4e953-c739-371a-b32a-daab2a0aa2ea | -9.3199 | -45.7288 | 2025-10-02 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 7130cd84-97ca-3ddc-8cd0-44b2657d1268 | -8.5201 | -47.8386 | 2025-10-02 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 96f94e8b-c873-3f9f-afc3-e81cba6c42d7 | -9.9186 | -43.6978 | 2025-10-02 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 248.4 |
| af86d734-ae80-3e4f-a5c7-5c8d9001ea51 | -9.9372 | -43.7187 | 2025-10-02 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 172.6 |
| 327f3c12-75e2-3447-a290-e8e190d9663e | -9.7851 | -46.2851 | 2025-10-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 9bf88083-1fda-3682-849e-dcbacff84106 | -8.0004 | -47.3151 | 2025-10-02 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2a6aa407-16da-3df6-b810-e6e41a00bb6f | -5.3379 | -43.7855 | 2025-10-02 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| eb83cc89-cd30-315e-965e-fe43e4c23e14 | -11.212 | -40.7359 | 2025-10-02 14:00:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 102.1 |
| b2236815-092e-35e8-a3b8-ed83483bb169 | -8.6722 | -47.6924 | 2025-10-02 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f3de4e27-a72b-3d70-afb1-2e97b4c24f6f | -16.0561 | -45.7438 | 2025-10-02 14:00:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 106.1 |
| d6794796-3171-3b61-977f-8f3b93245c12 | -7.7944 | -42.5132 | 2025-10-02 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 226.0 |
| fd6ae9d2-8ec3-3aaa-a3ac-c47d009401cc | -9.3389 | -45.7266 | 2025-10-02 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 198.9 |


[Clique aqui para ver as próximas entradas](README158.md)
