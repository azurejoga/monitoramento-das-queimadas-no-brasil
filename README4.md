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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11ff0d2e-2ea5-34c4-a504-5dbf48958cda | -3.6806 | -50.114498 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab9f4db1-09dd-3c65-930c-c37fadf5233a | -2.604 | -46.1866 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6ca20b4-6356-3ecc-851d-54d2f16ed91d | -2.6179 | -46.833099 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 869ab904-c6e3-3735-964e-07a253bc841c | 0.6266 | -51.777901 | 2024-11-17 00:28:00 | METOP-C | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6a624711-7920-351d-ba7f-9ee0aea94d5f | -3.2035 | -46.688301 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4890a4-2a6b-3bda-875d-1928de4a22fa | -4.2911 | -42.191502 | 2024-11-17 00:28:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 48ae130a-a9e8-39ce-a6e9-012cfdf26c81 | -2.5057 | -46.387798 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6cbfbf0e-35fd-3105-ba18-75c786fe8800 | -3.2857 | -45.605099 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 54725546-5e86-33a8-86bb-70b8cac2a9e5 | -2.6516 | -46.1688 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16ab48e2-875d-30be-8497-85147758ea38 | -4.4431 | -42.9314 | 2024-11-17 00:28:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed32ff95-a804-3611-8bf2-e65809cf6820 | -2.6277 | -46.830898 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98a7a075-5bad-3da6-885c-b76098918827 | -5.5723 | -44.8699 | 2024-11-17 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbc639a0-8c6d-38cd-a3b1-1d8a55206a34 | -3.7855 | -46.030602 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7593b75d-b590-340c-9dc5-51502c055c37 | -0.8933 | -51.729198 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 51f36d70-f693-3299-8306-19b4a1126966 | -4.2052 | -48.698502 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9dfe114-afbb-305e-acac-1f737e221eec | -5.6918 | -46.571098 | 2024-11-17 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 172b6f7b-e338-3320-b7f7-0b59d876ab78 | -5.1964 | -44.222599 | 2024-11-17 00:28:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4d008f3-4fd1-3a7a-83a7-e9dbf2f75d8d | -3.0701 | -45.474499 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 606637e5-49e9-3e36-a570-1c3083e5f3eb | -2.4659 | -45.674 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28b91040-5cde-33c3-b983-2de24b61e17d | -2.9491 | -45.801899 | 2024-11-17 00:28:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 967675e0-600f-3c83-aa09-68e9f1abb871 | -1.8329 | -46.602402 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90211106-2d67-3078-8595-ee1ffca66183 | -4.1009 | -46.8717 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f66932d2-e369-3641-a921-a5e6c543b40a | -2.9637 | -45.820099 | 2024-11-17 00:28:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 39ba48c3-cad6-3947-99dc-6641ca6a9633 | -4.9331 | -40.8433 | 2024-11-17 00:28:00 | METOP-C | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b9b945df-6dfb-3214-ae5c-ffa8801d5d07 | -3.2504 | -46.532398 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d62e73e5-a09d-3a21-8a35-d9544a1e74de | -2.2127 | -48.4007 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31452432-11df-38a4-990a-52a5bfef967f | -2.6155 | -46.1912 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| caee2d0e-5254-3ad1-ae8f-c464fb7459bc | -1.491 | -47.406799 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b9ef00c-68e9-3d2a-8cbe-afff896c3be4 | -3.1633 | -46.602501 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44ace20c-72b8-3801-8bc6-ce136174d898 | -0.3192 | -51.510101 | 2024-11-17 00:28:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bccaba4c-1da0-3855-abd0-54c01a4a97cd | -2.6619 | -46.8452 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fcecab9-fd28-38ec-8d76-f86ee1b14465 | -8.9114 | -44.135601 | 2024-11-17 00:28:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 066b8dbc-5574-35ad-8201-89c554a5dfe3 | -4.9861 | -44.071301 | 2024-11-17 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f435e40-2d77-3cf5-99d5-7e27d30f46e7 | -3.252 | -46.539299 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fabb1bc0-a75a-32bf-a6fa-bd5ed3f00afd | -1.2846 | -51.958401 | 2024-11-17 00:28:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df068c0d-46e3-36e7-847c-56833ea795e3 | -4.1025 | -46.878799 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20f63038-c763-33e7-8c5a-b44666e656a4 | -10.6644 | -44.5 | 2024-11-17 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c14a5662-476d-3a09-95ae-9775d1a935e0 | -2.6083 | -46.250099 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 751444ea-8c01-3340-979d-3c2fb3eb9c20 | -6.3004 | -39.4856 | 2024-11-17 00:28:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 66db49b3-d0d5-3952-b8ec-abfd3e5c5bdc | -2.6739 | -46.2211 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff2e9342-f9ee-3548-b6c7-906b7a7f75b7 | -2.6635 | -46.8521 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9f065f0-742b-38e1-ba1e-d3caed708980 | -4.2975 | -48.103401 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15515971-ecd1-3267-8d0a-b7cae5ccfd2c | -4.098 | -44.470699 | 2024-11-17 00:28:00 | METOP-C | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94552318-98c2-3ba3-bc17-51faa611fbfe | -4.4663 | -44.233299 | 2024-11-17 00:28:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3491e38a-dd0e-3de4-adc1-372c1651e281 | -8.4526 | -44.203899 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d5e99b2-45c0-31ca-b14e-117de25d9137 | -3.2826 | -45.591499 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2364f47b-c196-3e35-b8f6-22eb53348431 | -1.0147 | -47.758598 | 2024-11-17 00:28:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4dc0ae8-d2b3-36e3-b63f-2da123bbc29f | -2.6922 | -49.287399 | 2024-11-17 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f36307ca-6b55-34cf-904c-fedf9c7d31fe | -2.1612 | -46.414299 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb86b122-4083-39f7-b030-e267b4da659b | -2.4778 | -45.635601 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 370adb8f-37fd-3851-9819-7f23f3892336 | -3.7953 | -46.0284 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 27e30f98-3024-335e-92bc-921c9b22d6dc | -5.4036 | -46.345699 | 2024-11-17 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c93cff1-0994-36f0-b350-0d5400c23b0c | -5.6256 | -46.370098 | 2024-11-17 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe4757d5-c0be-3493-8e6e-fbba0701f834 | -2.9164 | -45.164501 | 2024-11-17 00:28:00 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 329ef24c-4c46-3c95-a5c0-8eb366d26115 | -3.7772 | -46.0397 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed5a1451-1122-35ce-bcf1-ce56e618b825 | -2.9207 | -45.4077 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1128519c-4eaa-3ba0-85c6-f4b1ba4da49f | -2.6511 | -46.211899 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40c538fe-1602-3030-b758-dfe1316de78f | -10.6628 | -44.493099 | 2024-11-17 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 048c165d-34fa-3582-be7e-04fa00929937 | -1.9946 | -46.588001 | 2024-11-17 00:28:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b1702d1-e3cf-334c-8664-3f950dcd3a2e | -2.6188 | -46.025799 | 2024-11-17 00:28:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b2692a1-1532-34ab-9357-56939822369b | -2.5105 | -45.4636 | 2024-11-17 00:28:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 109b14e8-673e-3836-a8c8-378a20e0ed74 | -8.4494 | -44.190102 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4b6f87a3-4f39-3912-8e6d-8a2891960a84 | -2.8283 | -45.5 | 2024-11-17 00:28:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62082b1c-1163-34d8-a1b5-6415fdbd2306 | -2.226 | -46.832901 | 2024-11-17 00:28:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea041714-1bfd-350a-9144-437947788502 | -5.265 | -47.1898 | 2024-11-17 00:28:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb4095f-fb8d-3f22-8a3a-f613090582cd | -2.239 | -46.844601 | 2024-11-17 00:28:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 090c8380-f100-3ba9-8cf6-fa98ed7de160 | -2.2374 | -46.837601 | 2024-11-17 00:28:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 085a7941-6b85-30de-b8f2-d1eeae9f29bc | -3.9529 | -46.719601 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45034939-3a47-3a68-86aa-4b3fb705a74f | -2.5961 | -47.550701 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0cc54da-e4a2-38b8-9505-a3855fe1f84f | -2.0586 | -46.552101 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b940a3b-f012-328a-b2e4-816ed92d122c | -0.8908 | -51.717999 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce813dc-ebdb-3e42-a6c1-77e70ad13a09 | -3.0147 | -47.442799 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c550529c-03bd-3dd1-9b3a-e100e1ee0d61 | -4.2117 | -47.223301 | 2024-11-17 00:28:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f9a735f-4d19-3ea0-91f7-ec26e2c96a49 | -4.0506 | -44.757999 | 2024-11-17 00:28:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97299b1d-be57-338d-89f0-2177c0d55f17 | -2.1226 | -46.5163 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11ad727b-90df-35f5-b566-195a25289909 | -3.3226 | -50.486198 | 2024-11-17 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d601042-d3f8-36c4-a86c-66d913e65e2b | -3.0105 | -45.394699 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6e42ce1-15a2-325a-9cc5-e6bcebd86aab | -3.6222 | -50.220299 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 829f299e-73ef-3996-99de-0550bba237b8 | -4.0522 | -44.7649 | 2024-11-17 00:28:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2bf1886-73b0-3ab1-9b53-8799a8f0ae0a | -4.5343 | -45.246799 | 2024-11-17 00:28:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fc274a2-ee29-3011-a824-d3702d8ea2c9 | -1.5599 | -47.347099 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 288d3668-650c-3e8b-83e6-82097c34b232 | -3.8882 | -46.616402 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dda1bf01-49c2-3f9c-8379-5e7c581475d5 | -0.7703 | -49.482399 | 2024-11-17 00:28:00 | METOP-C | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adbd3bc4-abcd-38b4-90eb-2a67e58cd67c | -3.1403 | -45.4659 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a18b84d-2570-319c-aaac-6c253123b919 | -2.5986 | -51.7826 | 2024-11-17 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc7462e-d7da-38a8-8a5c-26d9e86e3983 | -0.8959 | -51.740501 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 99945246-5b53-379b-a300-e8d2926ce461 | -3.0925 | -45.977299 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1eccc9c-70b8-35fd-a897-e776bc34b203 | -4.722 | -46.838501 | 2024-11-17 00:28:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 829f0389-1bef-33e8-bd0c-eed6ee13d5e8 | -1.8313 | -46.5956 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4f6e841-2e13-332a-aaf5-d9d9421bb3c4 | -3.9415 | -46.714699 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c991b0db-4947-38e8-86d4-0b4f2ab2fe31 | -2.8236 | -45.479599 | 2024-11-17 00:28:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e8180a5-5e8b-3ae9-8bb8-838cd159aa43 | -4.2891 | -42.183201 | 2024-11-17 00:28:00 | METOP-C | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 31e28984-9cfe-3d30-9a35-f09807b78c6f | -2.3205 | -45.175301 | 2024-11-17 00:28:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 48c1c11c-7334-3258-a958-fc20f0109c5d | -1.4894 | -47.3997 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8a4609-7555-319d-b499-a1136a0e2976 | -2.6805 | -46.205299 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 096602c2-869e-3b00-bf1b-021174f520ef | -2.9653 | -45.8269 | 2024-11-17 00:28:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34ef0022-73ba-39ed-bebd-f6ec8337c207 | -2.6317 | -46.5326 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5470c212-4078-35b0-b1cb-fdfe3dfa3f43 | -3.5167 | -50.253799 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eca3486b-c86d-397d-a093-23046d48905e | -0.9057 | -51.7383 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c41e1992-e8c9-3ebc-a4c6-4ae120740543 | -2.6197 | -46.2547 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
