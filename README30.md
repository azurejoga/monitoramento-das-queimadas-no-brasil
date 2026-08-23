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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdca622d-0c38-3442-93b9-634fbf561fa9 | -12.21444 | -43.15576 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b5406cab-0c1f-3388-ada6-6d62194d49cd | -8.55632 | -54.84892 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d88d2193-7ad7-3776-92c9-eaa1b798ce7e | -8.96124 | -50.76045 | 2026-08-23 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc383b85-09d9-3376-9fe7-e15662662d94 | -14.14908 | -48.07208 | 2026-08-23 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f822e7f-c849-3754-9e2a-312c8439602a | -14.37274 | -51.78265 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91a30965-0093-3232-a94e-ffd857245fb2 | -10.27387 | -50.38592 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f42be437-656c-371d-86ab-a212ac5ed39e | -12.40966 | -42.9016 | 2026-08-23 04:46:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3c21b1c6-761e-3737-801b-3cd010f75821 | -10.84955 | -44.74891 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebce151c-c8b9-3c62-8ec8-5b89193f963b | -14.96824 | -52.67443 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e889101-e4ae-38e1-a563-e4b54d4ff205 | -13.20102 | -51.42491 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a063011-f051-333c-b9ce-80fb85a5b54f | -14.56108 | -53.00243 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86e6c83e-4f6d-3478-a261-c1d9b8da1031 | -8.54157 | -54.83566 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5072b19c-6b8e-36c8-895b-45bcb0b98706 | -10.71945 | -47.74199 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 502ef2b6-8c2d-32fb-9952-92b06cea20ed | -14.30414 | -53.23428 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efeaba8a-2994-3089-8420-34da5c5c810b | -12.66634 | -42.29064 | 2026-08-23 04:46:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c177ca84-c3d9-3c47-8978-331d38f6566a | -11.0585 | -49.5066 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bf6c1db-e48b-3d40-acc3-e5319c0c231d | -14.43871 | -51.80528 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38952657-5865-306d-ac87-1908e5c67da7 | -11.43365 | -44.53794 | 2026-08-23 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f431b1a6-c9a3-32d4-a9a9-bf4cfb2f450b | -8.9245 | -60.72142 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3543f67-9e1c-3a03-97d6-87f5a72685ed | -10.71216 | -47.74456 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17ab8b3e-7e81-35be-9495-81b83528a14a | -14.40221 | -51.79098 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6be7691b-fdf6-387d-b438-914f100d2f42 | -10.84692 | -50.98437 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82b3e12f-785f-3f39-87cc-f8ea216101fe | -15.2095 | -52.80246 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54307314-d80d-3a20-88ae-730f38b2dad3 | -9.53027 | -51.64856 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3535aca-3eb8-33d2-8977-8eeb14b36204 | -13.22187 | -51.44801 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5bc5d22-395d-3790-8e14-c02ca524663f | -14.36994 | -51.77821 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c8fa812-50b2-3d43-82e0-eb3866fb4747 | -10.93952 | -49.59602 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 827113bf-7034-31f0-a0c1-848d80fd2a4b | -11.14785 | -46.19256 | 2026-08-23 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e984677-132d-32a9-ab49-d9c01b1da905 | -13.15801 | -51.42915 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19ac770a-ddd2-327a-bed7-31d3b0a21f7d | -8.62054 | -54.71594 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da8c817a-89e0-31f4-99fa-9ccc9965d4cf | -16.0564 | -50.44116 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9e0ca2a-e66e-3877-959e-6f8c30f14d38 | -14.38569 | -51.78414 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88a93fde-7eeb-3de6-a14d-657d3b4f7078 | -12.74091 | -46.45132 | 2026-08-23 04:46:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 393d906f-42ca-3912-80dd-6d6595f88022 | -12.73228 | -46.45146 | 2026-08-23 04:46:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1b1dc94-2935-3d39-8b80-30f1482414fa | -11.21012 | -55.07901 | 2026-08-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41678450-2cd1-3a7a-85e3-2b4359c8772f | -9.1155 | -61.59691 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a823e151-fa6a-3cc3-9c26-3c1b66b94f39 | -16.39974 | -51.85263 | 2026-08-23 04:46:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ddbd975-14eb-309e-bc8d-d21103301d80 | -13.25565 | -51.59791 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 343bfa42-09c7-38fc-99f0-cdc43bbbaed4 | -9.17896 | -59.459 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| da266b7f-ab61-37f3-ac2e-5fef3f5fff37 | -15.04438 | -48.69459 | 2026-08-23 04:46:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 115c4b3c-cc87-3c78-9556-2ec0d627f1bb | -9.43209 | -51.60767 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddcf4207-ece9-3774-a867-be13d680d79c | -11.62052 | -50.55468 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20228c75-573d-3a5e-93bb-a0df170a572d | -12.73897 | -48.39516 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9c45a11-8f95-34e7-a877-826ed8705e80 | -12.75031 | -47.12622 | 2026-08-23 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43685c6b-da80-3fbf-99d2-85b8388fbd55 | -7.78346 | -61.43515 | 2026-08-23 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb64654c-c64e-3a28-b0f7-e7aabb36540b | -10.5165 | -50.44456 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5d252406-00e2-3bb4-92db-5dbe29f37012 | -9.42734 | -51.66915 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c39f09b1-8cf7-3b1b-8095-f9c6d7dc95db | -8.53568 | -54.84348 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef9f8c93-bf0f-368d-944d-93c5d01d3842 | -13.68299 | -51.84834 | 2026-08-23 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ae3e9d6f-d59f-3ce9-9eb4-88eeeb341c5a | -13.89474 | -53.99762 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c438bc0-38d6-3d96-9d9d-f05c38e7d4d0 | -13.94342 | -47.81666 | 2026-08-23 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0157b421-58c2-3933-b9c8-c088e32e6597 | -15.04214 | -48.68669 | 2026-08-23 04:46:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b31c57a-1eb8-395d-92f8-71ad3ffe7177 | -12.74683 | -48.38887 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1763df16-4ec3-3b54-b365-8dfaa30adfad | -15.72793 | -56.0161 | 2026-08-23 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9a259179-67c6-3111-a2b8-8bbfd99d45e6 | -11.61039 | -50.55297 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c0154f8c-d95f-3f90-97a7-f66a1169631f | -12.40906 | -42.90608 | 2026-08-23 04:46:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 406cbdc8-f68f-3d84-82b9-33ce009036bc | -9.1857 | -59.4558 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5155d0f2-8f91-325a-8c50-265c0a3eced7 | -9.42992 | -51.61044 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f26a202e-6fdf-35aa-9661-7b5c56f31661 | -10.55688 | -61.45781 | 2026-08-23 04:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4cfa2194-d1e9-3c10-8c6f-68031f4c3ffb | -9.0125 | -50.72992 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 272c5ce0-178a-358b-92fb-824b6238821a | -11.57258 | -46.93113 | 2026-08-23 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f677d3e5-8d24-3e5c-adda-f5daa81a5b0c | -16.05697 | -50.43757 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2accf23-e494-3bd2-85a9-dfc772f94541 | -9.02507 | -50.7401 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d728f07-0be8-3f95-ae0b-10c5ec982357 | -11.27553 | -50.73919 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fa91a31-0893-3b0d-95d0-f2565c36d5e0 | -13.49632 | -51.75296 | 2026-08-23 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b21211c7-3880-3305-8b32-7d585847d4df | -14.49373 | -59.82922 | 2026-08-23 04:46:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a364360-00d9-3378-afb4-ac1f89633495 | -15.3995 | -47.57655 | 2026-08-23 04:46:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a327f8d-7bd9-30fe-94f0-4e67f23c112f | -10.83913 | -50.96749 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb8c128e-0980-3f4e-8690-fb2b7c5418f7 | -8.59363 | -54.71546 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50967cbb-8e3b-3b62-b926-51e6fda1bb0a | -11.36268 | -46.94615 | 2026-08-23 04:46:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7296a714-651b-3802-b018-69801395abab | -11.9896 | -45.51435 | 2026-08-23 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed989c50-c789-30ce-a876-ae321caaa607 | -14.49458 | -59.82502 | 2026-08-23 04:46:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4b2ed20-f936-3688-8980-a9befc9ac2ef | -10.79818 | -50.96445 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| de8a3949-515f-3e81-8adc-f8e380220abd | -13.25285 | -51.59348 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03e415f8-3089-33d5-a8dd-a839877ac1bb | -12.24212 | -43.12315 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5d51772d-6a72-30b1-8455-144e8f3d8033 | -13.15458 | -51.42855 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a306884a-155c-39a5-b069-bf3a0e57749b | -8.97633 | -50.7553 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ca8f1ed-7af3-3065-8ac0-91e218d0cdce | -13.19759 | -51.42431 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7a9d4ff6-8f66-31fa-9b16-2d013ad67918 | -9.79061 | -46.61298 | 2026-08-23 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3a91d04-a8f7-38d8-a6a0-91383e90bb92 | -7.78425 | -61.43004 | 2026-08-23 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6273883-27f3-3890-b00d-1d8c398b231c | -15.72373 | -56.01524 | 2026-08-23 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 23991dfa-9625-3ce2-8974-2710e6f8de2e | -12.07433 | -50.5999 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d24a0930-bb9b-3823-9b81-a483a8eff7b8 | -8.91809 | -60.72015 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1526db52-d6b4-3a53-a18c-43c8bd2c7836 | -9.52754 | -51.65075 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f869dcd-7c90-3af7-89ed-2914571157c0 | -12.22576 | -43.16983 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 47349079-6259-380a-a6e5-f42f2711af6c | -9.64013 | -48.31038 | 2026-08-23 04:46:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce8a5031-931d-3633-85a2-1822d2dc4891 | -9.18059 | -59.4504 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 27aceb82-b8c2-36d2-a66f-a71fc9880989 | -10.84193 | -50.97186 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2f571669-66e5-376b-97f3-7a02e12dbfae | -13.49286 | -51.75235 | 2026-08-23 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90a69edc-ef8b-3159-b2a3-c1f6d0acfe92 | -8.52611 | -54.84629 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57f0c44b-a1e1-3e9d-9314-1dc5bb121948 | -17.38538 | -42.6189 | 2026-08-23 04:46:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1684186-c494-3d8e-a10b-9ee9b52be469 | -10.83662 | -50.96707 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f672675a-6936-331d-8c2b-7a49d07ac3d0 | -12.82022 | -48.48145 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 006fe176-4035-3f0b-bc5b-d5aec72dd79c | -15.32756 | -46.08388 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 759648a4-d81e-3fc9-837d-3121b1e8265c | -14.34247 | -51.77338 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb5e153b-4d23-3633-94d2-cca15ea89259 | -14.39878 | -51.79038 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 421a883b-0da7-344b-9128-1d804eb2f37a | -12.7429 | -48.39202 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5585a95a-d610-3533-b896-afb923718ed9 | -10.30995 | -45.35809 | 2026-08-23 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b04e26d5-d81b-3bbb-a800-7eef13fc8fe0 | -8.97917 | -50.75966 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 393a1922-d544-3a07-9e3c-3285e8170c51 | -12.22564 | -43.1473 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README31.md)
