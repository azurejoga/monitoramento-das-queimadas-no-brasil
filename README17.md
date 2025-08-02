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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc1321b1-ebc8-3d58-bcd8-1fdff5433e25 | -7.36135 | -44.17092 | 2025-08-02 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17635add-1d19-313d-9713-05564636a2ff | -10.46664 | -46.9607 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 018ec12c-a76e-39af-ad6e-9871e936707f | -11.66871 | -43.77556 | 2025-08-02 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99551909-9d09-38b7-9f7e-332df06684f8 | -10.46411 | -46.9493 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1727b30e-6861-340f-ac5c-9d1c06849972 | -11.23784 | -48.8927 | 2025-08-02 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e215b26d-fa58-34f1-95f4-37971c220399 | -6.72323 | -47.20815 | 2025-08-02 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32fa9372-6107-32d3-8550-01679b0e9a7f | -11.96739 | -46.66608 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f702775-5ff1-3518-80f9-dd630a34a390 | -6.79316 | -42.98585 | 2025-08-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5d310533-4698-3f6f-9e56-5589cdf94238 | -11.75799 | -44.97625 | 2025-08-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c89db418-b00b-3d95-9be5-f4c337cba652 | -7.60592 | -44.8006 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c220dd69-6f86-3093-881b-642360cf097a | -9.11642 | -47.63985 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ba438746-5116-3247-94b8-317cd797dc1d | -8.02314 | -43.14287 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9e5768e4-54d4-3bd7-858e-b39ee7c844ee | -8.44697 | -47.48655 | 2025-08-02 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a14ccbac-b8fc-3aef-96d9-586752054588 | -10.45806 | -46.93345 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d38ca9f5-3cc0-3376-ba73-8520287d1288 | -7.75231 | -45.13379 | 2025-08-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32058d27-e81f-390a-8094-87c596eee074 | -9.39459 | -45.50181 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f04bf5c6-3b39-37cf-b264-a97d314da9dc | -8.91383 | -47.33844 | 2025-08-02 04:46:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 85b80dec-d346-35fd-a238-5faa3e991b52 | -8.04827 | -43.10991 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6e748a65-ad72-3a02-8485-7904cf4c8bb8 | -11.16948 | -45.75084 | 2025-08-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae05bd45-0c3c-3bdd-9720-aef5e2051990 | -9.19024 | -45.29308 | 2025-08-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc1f0e01-92e9-340c-8b7b-9adbc8992a28 | -7.24967 | -43.38488 | 2025-08-02 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2a35d970-3589-330c-8fcd-6b1c1a80e936 | -10.04054 | -44.71371 | 2025-08-02 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96dec4bb-6010-3ead-b6ab-34b7ac04f9da | -10.58769 | -45.27879 | 2025-08-02 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c80bb58b-b1eb-3c70-a0d2-1730bf9d8ea9 | -9.05893 | -45.06561 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d97c0e4-644d-36da-8624-a02a41ba4b19 | -11.94657 | -44.91434 | 2025-08-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 25e9fb1e-36dc-3b6d-ab7d-938687d965b9 | -9.06922 | -45.05766 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c7336b3-601b-3d57-86ba-e33e4a718818 | -10.4636 | -46.95293 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2845db00-d809-38f5-b80d-9911285388f6 | -9.3904 | -45.49899 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9b6b8bb3-2440-3977-810f-94bf63c1ede6 | -8.03609 | -43.12342 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 77e31c2a-2585-37b4-81ef-b99da18d495d | -11.97161 | -46.6667 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 427cc6f2-fb36-362c-998b-54f34627d0b1 | -9.43543 | -56.50558 | 2025-08-02 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e461c6f0-a470-396f-9dc4-2f13405c1f95 | -10.46714 | -46.95713 | 2025-08-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8403eea3-cca3-311a-b574-65c383987b34 | -12.45728 | -47.03278 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 491d253e-c666-342e-8f2f-9f8ea87d4771 | -12.66636 | -44.49157 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 75a06df2-6d87-3d1f-a599-aa7529667b3a | -12.71439 | -47.79645 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7b77d1c-e0f3-3540-8d37-73d416952850 | -13.89933 | -42.13696 | 2025-08-02 04:49:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b3eae59b-31ee-30a3-bf89-bfb5c3b412cb | -12.66574 | -44.53746 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8eef37e3-17cb-35b4-9fda-a84dca7b5f18 | -12.45211 | -47.03984 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 739e5f1d-ba88-364d-b42f-55e0dc3254f3 | -12.43976 | -47.06909 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83127d0e-3be0-3529-b0af-2ce8203eb725 | -14.21915 | -49.05526 | 2025-08-02 04:49:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69ba3018-3ea6-316a-9179-db46051b4854 | -13.04286 | -49.17175 | 2025-08-02 04:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 063bb3f4-4ebf-3097-a12c-2cf3f39f9b04 | -16.13151 | -46.87959 | 2025-08-02 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c904b80b-e8f2-321d-8677-a4108cd7a089 | -12.67248 | -48.09768 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 531aa4d1-9125-3af8-8c6c-0691c09c7352 | -13.21874 | -42.25367 | 2025-08-02 04:49:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 1d47e983-a1f7-3757-8f91-ab47b6f507d5 | -14.00163 | -53.94905 | 2025-08-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75d9edf3-c6a1-3b2b-a2d2-55535103c274 | -13.7013 | -51.9547 | 2025-08-02 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a324e11-77b8-3877-9a7d-116c579eb55b | -12.66211 | -44.48521 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a688ca32-9dd3-34e3-a71b-5ad82bc641ba | -12.65709 | -44.51176 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0f4a0a65-40fc-384e-a5b6-768b02201adc | -16.70764 | -47.57366 | 2025-08-02 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f727547c-9aa8-3060-b4ef-eadbbba170af | -12.4578 | -47.02893 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b8a8371-9624-35da-83a9-0d98eefa7ee7 | -15.11066 | -55.21487 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a80ba944-9ce0-35ff-9ae4-c4ba99ef4f5e | -11.91004 | -54.78754 | 2025-08-02 04:49:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88a3bc3d-6359-3b26-96d5-8b42eb3ec28c | -13.17385 | -42.23598 | 2025-08-02 04:49:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 11d8f9c0-a951-36e7-aeb4-e1d418816289 | -12.65782 | -44.50612 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 884f8f61-036a-3f7a-9f2e-915d4e681c3c | -13.23609 | -47.23254 | 2025-08-02 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5451e2b-5c71-31fb-b30f-cd8d56bb08ca | -11.90865 | -54.78668 | 2025-08-02 04:49:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fd26189-90bb-3bfe-8d3c-6b31165cf143 | -12.67276 | -44.52125 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e392f879-034e-3565-b98c-060038a3b748 | -17.00293 | -49.47383 | 2025-08-02 04:49:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d590d8f0-8fd1-3770-b767-0c32f1a57812 | -12.65439 | -44.50725 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 328358f6-abcb-3d96-8e5f-77537bd2b30f | -13.03058 | -47.42857 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5dab65f9-ea2b-3dfa-a748-4336ed8a0391 | -15.06145 | -43.87231 | 2025-08-02 04:49:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdf56c19-d2ed-3d7a-ae33-73bea42475b3 | -12.67556 | -44.49856 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ac7439f4-f14c-3989-b545-521944b9ac51 | -13.22123 | -47.24879 | 2025-08-02 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d7a7e98-70b2-3393-9424-13ae5064f326 | -12.66991 | -44.50356 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 45757b32-b42b-36ba-994d-aefbef16392a | -18.22417 | -44.70793 | 2025-08-02 04:49:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c169c59-c28e-320b-a650-dee09fb810c9 | -13.2305 | -47.24264 | 2025-08-02 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88190d7a-a4ea-376f-9415-c9792a30c087 | -13.06827 | -47.42663 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03ec772b-6051-3835-8928-55a63912e4c5 | -13.21964 | -42.25005 | 2025-08-02 04:49:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 02af9cdc-acdc-36d8-b035-33f6ab96c76a | -14.27849 | -48.84815 | 2025-08-02 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46a895e1-74dd-3088-aada-189a7609babd | -12.65361 | -44.49981 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 90eeb0fb-7394-3af3-893f-41005e6fd354 | -12.66151 | -44.53114 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| baa8bd80-1a45-3637-9c39-e83b4d32f110 | -13.70463 | -51.95522 | 2025-08-02 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12ac70ce-01ea-3786-96f6-1473af4f7790 | -13.69742 | -51.95777 | 2025-08-02 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6797a35-0f9a-39da-ac00-039d838b6851 | -13.89819 | -42.13604 | 2025-08-02 04:49:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e30c5e1-0cf3-3a76-9382-ac622a699bfa | -16.71135 | -47.57856 | 2025-08-02 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c536d07a-bdfb-3d42-8638-97413696a21a | -12.45995 | -47.07592 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43302b73-0ecd-32b8-b78e-317e65f6da7c | -12.65215 | -44.5111 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 830d19e6-e345-36c6-a769-a11fbcfd3ab6 | -18.2392 | -45.17076 | 2025-08-02 04:49:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 577ea73c-3368-3c8b-a55a-6a911f64ac53 | -18.21338 | -44.70933 | 2025-08-02 04:49:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdc6bbb0-7942-3ccf-9491-e0f41852e6d3 | -18.23953 | -45.16763 | 2025-08-02 04:49:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a270b9e-cc86-31b5-93a3-44d56f5221c8 | -16.71187 | -47.57437 | 2025-08-02 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36dde288-efb1-37ae-bf7a-f3e73aaa3691 | -13.0653 | -47.44859 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc956c22-8a83-38b1-a411-057f9530e7e5 | -18.21893 | -44.70713 | 2025-08-02 04:49:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23ff462c-a00b-31c2-a0a1-82b8b2d0cc71 | -13.22537 | -47.24931 | 2025-08-02 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e16eac9-3d81-305a-aaf3-927238506d4f | -18.24429 | -45.17147 | 2025-08-02 04:49:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 323de2cd-1afa-31ec-a7b7-83fc15981ed4 | -12.44745 | -47.04307 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4068ef85-8d5f-305e-ac98-3d2a7ec7addb | -12.50717 | -57.78535 | 2025-08-02 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eae5516d-58dd-3f9b-867a-e5e12b868ced | -12.67699 | -44.52759 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91a928c6-dce4-3cb7-b779-7bfa1c8b10a4 | -12.45314 | -47.03216 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d39fc6dd-36d3-30c5-a02c-07b7b08e3bea | -12.66706 | -44.4859 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2a5a91d0-102c-3bf6-9e02-65b8307b9786 | -14.21539 | -49.05469 | 2025-08-02 04:49:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3a229ed-f064-330c-a502-5e4bfdeb5c19 | -18.24462 | -45.16836 | 2025-08-02 04:49:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 090e5c70-3a51-3c1b-8d31-2eff9e337caa | -12.67696 | -44.48721 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e726afe0-ac9a-31a8-a926-50723452b322 | -15.12367 | -55.22129 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c6a5ec6-1382-3be6-8385-45c687f9ce58 | -15.11343 | -55.21939 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8316b65a-8b37-3ad6-8d85-db2d2b0150b4 | -14.21476 | -49.05935 | 2025-08-02 04:49:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acae1fa2-3cc7-3af3-ae6e-b41677eae7f0 | -13.70075 | -51.95829 | 2025-08-02 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ac06ff1-8584-326f-b232-00aef31d5110 | -13.06875 | -47.42308 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85b067b8-b0a6-380c-8877-df2ca9e2a584 | -12.65288 | -44.50547 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a74cce61-7bb7-3292-872f-399403b39643 | -12.65856 | -44.50045 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |


[Clique aqui para ver as próximas entradas](README18.md)
