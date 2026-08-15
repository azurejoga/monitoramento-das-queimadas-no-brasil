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
| e250d88b-e189-3596-833e-0964286d9015 | -11.50379 | -54.63041 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 387adfe9-517d-35ee-ad33-904473ce4a52 | -14.44469 | -51.90866 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 887aea95-1f3f-3d27-8ba7-c508f221b375 | -14.09319 | -53.62545 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 846656e0-17dc-3624-bd24-34be67c7a791 | -11.50821 | -54.62383 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3252f9de-727d-3e26-a351-f8c770f0c751 | -14.46101 | -45.67691 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c072145-4124-35a1-b4cb-4e711db94f74 | -13.45441 | -57.06936 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e305e3ca-39d8-3d66-a9a2-0a29b0787520 | -11.51214 | -54.64262 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62cc0c17-5c21-318a-8980-438c3562e217 | -14.53165 | -53.24706 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a9ae499-32b9-3d61-b294-28e990cb8334 | -14.43354 | -51.91024 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1f137c2b-c71d-3ab5-904a-16a0c49999f8 | -14.43466 | -51.92995 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ec98bc9-0220-377a-870a-dec253ef8048 | -14.08441 | -53.70878 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b03146c-6851-373e-a80e-55ecd1ae35d8 | -13.69222 | -46.26122 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7900f54b-05b5-3b1f-8cc9-f54aa0e52738 | -11.23235 | -54.82697 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47734198-fdff-3b47-8a74-62ef39a23103 | -14.4322 | -51.91982 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8e486ee0-df58-3c29-a9ee-33a72be0df1e | -15.17468 | -50.06258 | 2026-08-15 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6c13330-b967-3b82-9420-34bd146b3e7a | -15.10578 | -48.69551 | 2026-08-15 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e3b83b5-112d-3e72-a7f9-96a020b9d1a5 | -14.44497 | -51.91193 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 604fe3b4-6259-3bf3-af95-e7b957f6abca | -14.44663 | -51.89421 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 133cbb71-1e98-3641-98cb-e21debd84d60 | -14.57589 | -46.77337 | 2026-08-15 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f7f1518-c999-3fcb-9cea-58deffef25ac | -14.26206 | -52.03234 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9a4abc5-ee1e-351b-ac1f-9659e9b83939 | -11.50433 | -54.62686 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9adf8be2-1edc-34e8-a518-a53c5779a623 | -11.4849 | -54.62018 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ffd0154-8af8-399f-b773-fbf8fce2b345 | -14.46116 | -51.93068 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85350d63-8c14-3794-92de-b3d066e2d3c9 | -11.24399 | -54.83963 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5b074d6-8343-3cbe-bbc8-8701eaff3aa0 | -14.08384 | -53.71267 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcecffeb-b052-340e-8de5-61b398638005 | -13.54146 | -46.25887 | 2026-08-15 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c1b353b-bf77-3027-9ecb-609b3c7cba2e | -13.25249 | -54.1958 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18d306b2-71ef-3532-acf3-28ad254c1bf0 | -14.09611 | -53.69016 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8731c5b8-ce3f-3b52-8b60-a3ea960bb804 | -13.04129 | -57.09386 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57544377-04e8-3e70-9fd7-203fd9c45f98 | -14.41406 | -52.1646 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dc3f46b-1aba-3792-99db-4c9f5a0a8a3c | -13.24513 | -54.19154 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65275a88-7349-3b0b-84bc-1a1d8076b6c6 | -14.44909 | -51.93377 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 138c74cc-e8fc-33ba-a4e7-356f1f737033 | -14.4529 | -51.93435 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba895392-12f8-31c3-b87b-1fae93b9e7f0 | -11.98624 | -53.45133 | 2026-08-15 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1ea82bc-ea76-3f7a-941c-a0810cc21c2d | -11.48877 | -54.61715 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4db9a025-67cf-3919-b3e2-2c8e34f6fb6b | -14.43767 | -51.93207 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8745cd9-1fa9-369e-b0a1-663070c65c1c | -14.43891 | -51.95178 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7de9a274-02ed-3453-ad61-aab7693e40d2 | -11.48436 | -54.62373 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ef512d6-4dc2-334d-91fe-02e043f218fa | -14.42906 | -51.91447 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d353d8c0-7551-3dc6-a575-70d4880cca77 | -13.42049 | -57.04512 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4be31d46-1671-3ed6-97c3-dd3219a9a70c | -14.13374 | -53.67566 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d63679c-776a-35ce-90e2-b1595a302847 | -13.82066 | -53.78539 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77bc395d-e777-3a55-98ba-eadfccfd4023 | -11.20141 | -54.82928 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49b61f39-a8e9-3e5c-b1d2-da10168a55be | -13.68675 | -46.26043 | 2026-08-15 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32091ef8-fd72-330a-acd7-e6146da384ca | -14.46145 | -45.67283 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9174bfdf-2844-31ad-a9ff-cf9c54de47b2 | -13.23608 | -54.1825 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13465f54-ebae-3653-9978-a23fee97d325 | -12.74106 | -48.43599 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c82b2ed8-7e5b-3e4a-8c27-4bdf6f01e3f0 | -12.89842 | -52.82528 | 2026-08-15 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9b46943-e47f-3d7b-bbf6-831cea96232f | -14.73428 | -52.68686 | 2026-08-15 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 773916a9-ce47-37cc-b787-d176927ef216 | -14.03743 | -53.6172 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b9b0999-a802-380e-b20d-3cfd4c77bac9 | -11.48823 | -54.6207 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a863fda-e7d2-3053-8762-440b7491d702 | -12.03324 | -47.81554 | 2026-08-15 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b56f5a99-5ee6-3ef6-9162-205cd299464e | -14.72036 | -52.88969 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b7da6a7-a2d9-3c5e-8a2d-d4a2dec73c40 | -14.72399 | -52.89019 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24571adf-c0d8-3ee7-82fa-4cafaa907aa7 | -11.50046 | -54.62989 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f81a7c8b-8638-3e0a-863b-12c3fb288dd3 | -10.94061 | -57.11042 | 2026-08-15 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2bc149f8-16b9-3907-88eb-0a12116a13c1 | -14.43668 | -51.9156 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9263b29b-1639-37ac-af93-3e0707656f4d | -13.83217 | -53.77921 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb9dd7bd-afe8-3bc0-8c2e-1cd9fe2b6efe | -12.70402 | -48.4426 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9dada6f9-e06d-35e4-b0ff-a7326159882f | -14.71611 | -52.8935 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31018a28-72d8-38af-aa92-c53b1b667d0c | -11.49659 | -54.63292 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69fc4312-2bfa-38cf-9d3d-2ac980809cba | -13.27056 | -54.19099 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b9c0865-4552-3b92-8def-c7a349cc602b | -13.28018 | -54.19629 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d43a6642-8e35-3bb7-bbef-77e87627936d | -12.13763 | -57.2073 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bdd25fd-fa05-31bc-a98d-8bfee7cb09ff | -14.40335 | -48.95609 | 2026-08-15 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 96f41b5b-1f8b-3738-9cf9-be253ab3533d | -13.82872 | -53.77868 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 346d690e-bf26-324f-b470-acb71f0cf35b | -12.38381 | -46.41863 | 2026-08-15 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4945a02a-cfea-3ca5-a9fd-8e45fbe8f6a5 | -14.40262 | -48.95823 | 2026-08-15 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d8a65178-5a69-3612-bcda-e6755febe83d | -14.21848 | -45.41195 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bb59950-ba60-37ab-b54c-24f9e309635e | -12.7201 | -48.4283 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cfa5d76-023e-353b-a4b7-a11cd4c4e055 | -14.43153 | -51.9246 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12e3a964-490b-3a47-894b-b4781325870d | -11.50766 | -54.62738 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcb5065d-8068-321c-9d69-7ca2aa80f409 | -14.07804 | -53.67979 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26bebc7a-e5fe-338f-ba11-c4bb26a5a98f | -14.42458 | -51.91869 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 446366be-fce6-31fc-b884-6354d2455a3d | -14.71974 | -52.89401 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 969f48d6-206f-3c93-9119-1c44b2caa90f | -14.91555 | -46.64278 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d4901963-614e-3f55-aa19-9d1e6bf8f6dc | -13.42852 | -48.34901 | 2026-08-15 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96508df8-b3f9-3a40-aba3-1f54f22a94bb | -14.23013 | -45.41344 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9434c56d-000a-34e2-90f9-7cca44420ae6 | -14.45484 | -51.91995 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d94264b-97ec-3295-9a99-ca2d2e2c255d | -12.74569 | -48.43695 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c8247e0-4e3f-36b9-b2ba-834af8e8a6b1 | -14.75544 | -48.24964 | 2026-08-15 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7accc91a-6ca3-3958-9333-572f070cba39 | -14.45327 | -51.90825 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 663428b2-3d94-3134-aa4f-db09804cac44 | -14.465 | -45.68231 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 511417d5-4eb1-3fc9-b66e-c65d90513894 | -14.72275 | -52.89883 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6bba03a-a792-3ed7-a4c9-5e742ca9e204 | -14.43703 | -51.93686 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 780ac778-e6ef-34b3-b6fd-1f3211f735eb | -12.70217 | -48.45703 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a013d141-f6cf-3cde-944e-4201b495bcb5 | -14.38235 | -53.10787 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a6f5f6d-47bb-3cef-ad7c-8ac7b7584be5 | -14.44529 | -51.9332 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceca113a-0258-3e12-a4d3-2c20ada41676 | -14.72098 | -52.88533 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 034a184f-661f-3a5a-a230-2b3e213aa779 | -14.4396 | -51.9177 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2c3936c9-f282-3743-bc3e-9026ef9c2e76 | -14.94391 | -46.63535 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8039859d-3982-3b90-ae97-46d19ed0a94d | -13.27 | -54.19471 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd985dce-b1fd-39ac-8c25-6c172506e0c8 | -13.25927 | -54.19688 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d71b8d0-8eba-3394-985b-30a2d19dcb9a | -14.92134 | -46.64025 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7c9f3d6d-f53c-3358-a8c4-3bfde0f37c51 | -14.44946 | -51.90769 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9cced8d-4d45-3f68-8930-2b6fc4120b6a | -11.49767 | -54.62582 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fd5c763-16d5-3d10-aa48-d41f6d351da0 | -11.49876 | -54.61871 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec300245-3714-314b-b252-7bddcacf206b | -12.35678 | -51.21303 | 2026-08-15 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d132da21-bebb-3550-9768-8bede46acd5e | -14.96618 | -46.63328 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f90bbc24-72ab-3d31-97f2-e6bf52338fb0 | -11.49435 | -54.62529 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README31.md)
