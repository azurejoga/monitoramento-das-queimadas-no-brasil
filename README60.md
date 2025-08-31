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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96e5e91a-3c53-3fae-bf56-c9dbf2b18e23 | -9.44672 | -60.55698 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e305b8d7-58e7-3699-8ab8-87a86c5ea869 | -14.22645 | -48.072 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5160750a-3055-3353-91af-f22fa7d65292 | -11.34079 | -43.63579 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f22461a7-c39b-35dd-87f9-60251f32579a | -14.55239 | -51.98967 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ddc996f-2c3f-37c9-9e38-e95c3afa0bd0 | -11.29156 | -43.63893 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a8d0c52-c6f5-33da-9c06-89c76dd5935d | -8.29347 | -44.92319 | 2025-08-31 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f016a79e-1700-3202-b883-4d5612a19957 | -9.44978 | -62.3312 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb881ec5-097f-3436-a476-aec26fb4415c | -8.64683 | -62.83409 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ea73d69-aaa3-3d24-bd9d-07d1ad039d02 | -8.64891 | -61.95196 | 2025-08-31 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97e5ea5a-4b1c-344e-b8dc-8472a0853a84 | -13.35986 | -54.3856 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2785f13-6b02-3bdf-b393-e416a0b44030 | -8.55952 | -63.02922 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a7b790b-ba0c-3c18-93c8-ea210bca5aa2 | -8.55741 | -63.00967 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b156973-18cb-3166-889f-7cd250a48428 | -15.94252 | -41.40062 | 2025-08-31 04:51:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c364d4d9-c71e-3c4a-babe-76ebd86e7d66 | -9.45382 | -62.33855 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c86f832b-991b-3f08-bcb8-1b246aca4793 | -8.2905 | -46.31155 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4085bcc7-36d1-33f7-a336-45adeb39e7c8 | -13.49138 | -46.96658 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25414490-20ef-3e49-8e05-e8f85dd71104 | -11.81993 | -46.42975 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f91af414-dafe-37e9-ba63-d7c6e30cb36f | -11.31635 | -43.69505 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de75911f-c375-36d7-8007-2972c5944b8a | -11.81618 | -46.43153 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 70eb9074-f104-34a0-acce-e60293cf9780 | -8.5664 | -51.30669 | 2025-08-31 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bed259b-d1ce-343e-a135-c8e0a9529e41 | -13.54035 | -46.95584 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66a14a64-b936-307d-bfc1-234cd4aaaa17 | -11.20896 | -45.03896 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 309d8813-bed0-3380-b6f9-cff439010de9 | -14.3537 | -51.89198 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bf794f2-5a60-3a08-8828-08f1d3fb2fd5 | -11.8335 | -51.49661 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d404840-71be-3e4a-9e68-373b44017ed4 | -9.45261 | -62.34515 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a1a350f3-3526-3616-a003-288dc2352220 | -13.35966 | -46.95202 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 28f405c0-f801-3bf1-b26c-799980af9456 | -8.92484 | -62.42674 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b62b556-e340-30c3-acef-a123aecb59d2 | -11.84454 | -51.49432 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| be8567ff-a946-3c9a-affb-61b0f6a26305 | -11.21607 | -45.02462 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6780876a-ea84-379b-af62-4830619f9f79 | -14.54175 | -52.99912 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0299a435-8dac-3afd-9b8b-e58ce7e389f8 | -13.57396 | -46.91764 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75bb8b48-749b-3d8c-9abf-e5362e173e61 | -9.5657 | -55.38865 | 2025-08-31 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80229af7-9f29-31e5-9980-237e4fc8c0f7 | -11.27945 | -63.23634 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a5b85e6-b08f-38d3-beb1-6d5985a7fa1c | -12.81217 | -48.09961 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e963bd20-664d-32ae-a619-392fb690797a | -13.9877 | -46.31971 | 2025-08-31 04:51:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eec628a4-db3b-3471-81e2-e9eb962f84b4 | -9.45322 | -62.34184 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 527dbbd3-6875-36a5-b993-bb3dde52e6e4 | -13.0139 | -56.89941 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03952e84-9fba-3dcf-a567-14647ecd7889 | -8.68836 | -62.41882 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a5cbbbe-35db-3d23-bfbf-1a8e73f870a0 | -6.88221 | -56.47604 | 2025-08-31 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f66ff4b3-17c8-31f7-af0b-228849708a2a | -13.47164 | -46.97234 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abf8b11c-d205-3141-8a91-3acdb03dd1ce | -12.92069 | -56.98031 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f5e33c9-5dca-3a90-a71c-19171a0813e5 | -10.41283 | -64.53342 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd61322a-7e65-3737-a01f-5bfc7ed2db7a | -9.06029 | -65.42998 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5552ce86-3b67-3383-ba95-4b1e332ac9fb | -9.47477 | -60.32039 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83fa2bb8-a90f-316f-a002-1a86a71b8261 | -8.68649 | -62.42908 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bda83d3a-ce22-3158-916c-873818e6f60e | -10.67158 | -46.27517 | 2025-08-31 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 958a56d8-1f5f-3853-8989-6f8d88b7dc1d | -11.42261 | -46.91772 | 2025-08-31 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33da2142-4001-348d-a829-367db6ff5137 | -9.06974 | -65.41544 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39747f5c-7f1d-31d6-ab76-7dc12eceefa8 | -11.02491 | -46.88792 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8ffe39e-7132-3aab-81d1-310db60bb8dd | -11.07612 | -44.6214 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 854d5662-21bf-3208-ac62-5074c5dcdd06 | -12.2252 | -64.22427 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 999c47b3-83b2-3616-8d0f-f1dab82fbf93 | -8.78059 | -46.59341 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 785be65f-5da1-35f5-bcba-34b89e8685ca | -9.44203 | -62.37325 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb0f6360-9fc8-34b3-8c5c-79eff3a13294 | -8.72731 | -50.38279 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7b20297-d473-3d90-a040-7ffe75dd057f | -8.68119 | -62.42799 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8b837cd-19d5-3319-9e8f-68bbe2f71b6c | -14.54305 | -51.98003 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2df0016a-489c-37d0-ad48-f8e86f099493 | -12.85846 | -48.08056 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 540f781d-3075-3dac-ade3-d0065aa6dc01 | -12.49282 | -53.83205 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff36362f-783c-3dc9-923c-e267b39a5db7 | -13.67494 | -46.92791 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e9e2293-6876-35dd-8d3e-32da0b5d6588 | -8.49262 | -44.73922 | 2025-08-31 04:51:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f9561a6-7237-35a0-9c9d-9e3c270b2d7c | -14.33439 | -51.87665 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1e082c6-3ef5-3400-ab7b-fbbdfa4e9778 | -11.31161 | -43.68671 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1865e25-d0c6-3361-b848-2da991655292 | -11.88493 | -46.34834 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ce1e7c46-9e60-3bf6-a99c-c9861995b237 | -11.34695 | -43.63251 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78b80d89-91cc-354d-a1a9-4b0527b9d777 | -11.07156 | -52.02479 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3776942-7546-3cb5-bfff-12cf0f5649af | -11.32775 | -43.67153 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20584a5b-e4b8-3288-8e7d-4c18b29cb56f | -11.78144 | -47.39968 | 2025-08-31 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d942d629-4525-3acf-abd1-4b2809c9401b | -14.49385 | -52.99522 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 946a84ba-b33e-3b55-a408-ef0460b704f2 | -11.88956 | -46.73243 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 959088fd-6498-335a-9786-36a7578ba964 | -7.71095 | -50.26914 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78c1ee87-7c2a-3283-9e30-d04cf999ab5f | -11.06929 | -52.01683 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da7cb8b4-192f-3b38-877e-3c580ab361a5 | -12.92995 | -56.99033 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ae34742-7254-36f7-ad97-eff54187d46b | -8.73168 | -62.38236 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25945c7d-cce3-3e3f-98db-d8d812b5493d | -8.68242 | -62.42121 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ac8a0e2-583d-3ccf-b300-59f1b10a1db6 | -13.02648 | -56.88926 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce76b71d-b449-3a2c-afe8-727781a82d02 | -8.64819 | -62.82687 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceace55a-415e-3d94-893b-2d5f6e0a1058 | -12.17584 | -50.09628 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02648e29-0090-3a0b-a509-51e8d54668eb | -12.92709 | -56.98565 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e170162d-0710-3e70-8373-c9ddaa7563eb | -10.60271 | -44.32478 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f52dbefc-9863-38ec-9673-bb5373bac188 | -11.82807 | -46.44084 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7a90ca97-f873-3c54-b2b1-9e18dbc226bc | -13.34834 | -46.98681 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 990dfec9-211b-331c-8d01-b02c3b9665df | -14.61588 | -48.0701 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76e5e5b9-fa6b-38d2-9139-c4c956063644 | -12.92777 | -56.98155 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a52edbb7-ea16-3ef7-8a9a-df006fa962a2 | -13.6879 | -46.87874 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 324bb42a-1f60-3606-b465-eb9825e12d01 | -9.46652 | -60.31391 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 944aa914-e9e7-3284-b542-a8a1d6c1375b | -8.38295 | -47.38898 | 2025-08-31 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1bebe41-a608-3b07-abab-2d59f1c2dc57 | -9.31046 | -59.21615 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eac26274-2416-371c-bc47-0daeb082000e | -9.61842 | -47.80202 | 2025-08-31 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0302113c-a893-3b98-8494-1675c2f2ba19 | -11.2082 | -45.04483 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52e1e335-a91c-3f69-9d4c-a5c58a80e334 | -11.32524 | -43.66899 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87ea1abe-83c1-3539-83f8-7dc59ed8d362 | -9.68083 | -48.30353 | 2025-08-31 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| acc7d9be-2311-3cb7-a436-72b94361414f | -11.82941 | -46.5158 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8547194a-6ef4-3382-ac17-6abb03b5566d | -11.06196 | -52.04225 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 941c709a-c6f0-3e4d-a04f-7fe9c1454ab7 | -11.81144 | -46.43092 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 0594d8cf-46a2-33b4-89f1-6a6331dc7d3a | -7.96171 | -46.42455 | 2025-08-31 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa7465eb-727a-3b3c-88fd-8d09ac6b9dcb | -11.89018 | -46.72765 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d147cd41-6626-3875-9336-17f5b5a7229c | -11.35163 | -43.6415 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 46b6660c-8256-325e-bb6e-ddc87751174d | -11.31115 | -43.69052 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1776943c-b17e-36cd-954d-62eb4ca6d80c | -8.33062 | -47.42245 | 2025-08-31 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9baab3b-6628-313e-ad20-4f6f01a6517a | -9.7005 | -47.04567 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README61.md)
