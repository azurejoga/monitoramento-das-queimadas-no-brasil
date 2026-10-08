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

## Dados Diários - Página 210

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe4b2445-f70d-358a-937b-76fd3ff5c71e | -9.3736 | -45.9489 | 2026-10-08 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9d17ac97-cfcf-3392-aa55-bf69299eb042 | -11.6186 | -43.6433 | 2026-10-08 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 340.4 |
| d079901d-8c6b-3488-9639-d5ab324aed51 | -8.6106 | -67.0486 | 2026-10-08 12:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 424fd3ca-8410-3ba3-a421-524ff0fdae80 | -14.6701 | -51.4643 | 2026-10-08 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 65b4d764-862f-3c0a-b1ea-4b4b27c1794f | -8.6106 | -67.0486 | 2026-10-08 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| babd61d7-3a75-3db3-85f2-f91b4efadb67 | -8.6292 | -67.0111 | 2026-10-08 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 7ce6f10c-012d-3d7a-9985-d4486e84bc65 | -11.394 | -46.6697 | 2026-10-08 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 11cea3e3-4eab-336f-899d-4c6be893597b | -11.8676 | -48.0348 | 2026-10-08 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 873652df-f9c5-39bd-a841-4ac080ae782f | -8.6107 | -67.0301 | 2026-10-08 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 74957165-449c-31bb-8082-0c683bc798f7 | -13.1641 | -54.3178 | 2026-10-08 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f6b5d561-50f8-3efd-adc1-5cf2e3c5ccab | -9.9018 | -44.7917 | 2026-10-08 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 9ce087e6-1cdc-3f96-bccd-06596e0d110b | -8.9501 | -45.1334 | 2026-10-08 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d2d3abde-006c-3298-9c17-ea4ea773ae56 | -9.8253 | -47.4629 | 2026-10-08 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 972fb805-a177-3a06-8e21-89e4590981f7 | -11.3103 | -44.8337 | 2026-10-08 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 524.1 |
| 8529f5d9-13a1-3840-8518-8044b628ea53 | -8.6107 | -67.0116 | 2026-10-08 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 568ab5c4-e661-3493-93c4-9cf344ce98ca | -11.3937 | -46.6922 | 2026-10-08 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 859ce759-ff51-33fd-8fa2-10971b284c72 | -9.1543 | -49.8142 | 2026-10-08 13:00:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 54d65f5c-1a8b-3390-a6b1-ef5ed3fed801 | -8.6291 | -67.0482 | 2026-10-08 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 22eca578-a2b2-370c-b6b3-54c7b2411b60 | -11.6369 | -43.6876 | 2026-10-08 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| fda65a50-92ba-360b-b4e9-d1b81320a20b | -7.2185 | -55.1016 | 2026-10-08 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| fe2ef0bc-79ae-3246-b1f6-7c19fbe24cc2 | -14.6701 | -51.4643 | 2026-10-08 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 25be131b-8a43-350b-a9b2-3ab38b5683dd | -10.4527 | -47.2801 | 2026-10-08 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| e632789e-6409-3f23-b9b7-f94dd055b9f0 | -11.8485 | -48.0373 | 2026-10-08 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| bf6748c7-9753-3d70-98ad-3b38d5837679 | -11.6186 | -43.6433 | 2026-10-08 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 13acb476-5ec2-3d0b-83b9-57377f6c6cfc | -9.3736 | -45.9489 | 2026-10-08 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 2bd895f0-bbc1-39af-a67c-e1c47d13d1e2 | -9.9014 | -44.8147 | 2026-10-08 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 127.5 |
| fb4a808f-7481-33b2-9ace-db944c57686a | -8.6291 | -67.0296 | 2026-10-08 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 00816afd-9163-3f7c-97de-a448afc1d0a4 | -11.6181 | -43.6669 | 2026-10-08 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 3d56a987-412e-37cb-8531-8628d067de2b | -10.4337 | -47.2824 | 2026-10-08 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 6c5ec46d-6e65-398a-88b1-0d9b1a7e8fba | -11.8676 | -48.0348 | 2026-10-08 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 63be7f57-e884-31fc-978c-ba3d1aa7b98e | -8.6107 | -67.0116 | 2026-10-08 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 83a6b3f7-994f-30fc-8032-07ba7016bb99 | -13.1641 | -54.3178 | 2026-10-08 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c59497a7-3c02-3b1c-b59f-c3f3a8fdf463 | -7.8876 | -55.0023 | 2026-10-08 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 6081bf48-5006-3169-bfd1-3f9045005908 | -11.3539 | -51.8654 | 2026-10-08 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 841ea7e7-a7d4-305d-bf1a-c02500e4cd0d | -9.9014 | -44.8147 | 2026-10-08 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| c086b2cc-df6a-32b9-b1e2-0fdbdbd3e421 | -11.6186 | -43.6433 | 2026-10-08 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 426.6 |
| 928ace4d-be9e-37cc-a9a0-5c4130c6cc06 | -8.5313 | -46.911 | 2026-10-08 13:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 387e4743-59ed-3bfb-bb2c-c556f0ecb21a | -11.6181 | -43.6669 | 2026-10-08 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 244.2 |
| dc0656b5-4216-3a63-bf61-d2d450f389d2 | -10.6722 | -47.83 | 2026-10-08 13:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 47187c4f-bafd-388a-a493-b6ddd812c9ca | -13.1833 | -54.3158 | 2026-10-08 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a75da9a5-a260-3844-b0ec-87a49d199b9a | -11.619 | -43.6196 | 2026-10-08 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 412f8b11-85f8-373c-9d2e-4e2c24f64ea7 | -8.6292 | -67.0111 | 2026-10-08 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 13bd40e1-6127-3929-a91b-95eff8c9b538 | -11.3103 | -44.8337 | 2026-10-08 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 279.2 |
| c0d730a4-8678-36b6-93e0-da9133128101 | -9.1543 | -49.8142 | 2026-10-08 13:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9f703a7a-7954-3d58-8b35-08e8059e98b8 | -8.0578 | -45.6131 | 2026-10-08 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 65832313-66ce-3358-ab27-3745c490dd5b | -8.6107 | -67.0301 | 2026-10-08 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 260.3 |
| cf72600f-24e7-3e82-be66-4d865f7ec08b | -8.6106 | -67.0486 | 2026-10-08 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 91f2da31-ada3-3695-8711-fb3f5a6ef520 | -11.8485 | -48.0373 | 2026-10-08 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 077a4021-70df-3b97-9646-5750ba20e4dc | -9.9018 | -44.7917 | 2026-10-08 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 51d70bd9-50fa-3fa2-9b2c-523d46e77e53 | -9.8442 | -47.4608 | 2026-10-08 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| bde4170d-bcb6-3ffd-8b99-051f21367bcc | -11.2482 | -46.2604 | 2026-10-08 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.6 |
| 2a1778cf-702e-3749-b07c-cf1ed071bfe6 | -11.2486 | -46.2377 | 2026-10-08 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 31fe7e35-3f43-38a1-9bf6-5a5915734599 | -8.1996 | -46.3415 | 2026-10-08 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 92392dc3-8c02-341a-b79c-34bbd796eecf | -11.6177 | -43.6906 | 2026-10-08 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0f678b97-5752-39d7-ba66-8703ae1063e2 | -10.4337 | -47.2824 | 2026-10-08 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 224.2 |
| a1e12f82-19b7-3f84-b5f8-78ed96fa353a | -11.335 | -51.8673 | 2026-10-08 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| b368c6dd-a549-3066-81ef-c718bcce35bf | -9.1483 | -45.8385 | 2026-10-08 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 622f8bd7-f769-3ee1-aac4-f377f9f4dd30 | -9.8253 | -47.4629 | 2026-10-08 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ef3d6375-f97d-3157-b561-0fe8e0ae90d3 | -11.6369 | -43.6876 | 2026-10-08 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| a621546d-7d6f-31d8-8ac2-dc7f4bc119f0 | -9.9398 | -43.5542 | 2026-10-08 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 03b4392f-1d75-343d-ae5b-0b6f39ea0c4f | -10.4527 | -47.2801 | 2026-10-08 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 8e143002-134d-3d0d-8f88-663c90afd7c3 | -7.2185 | -55.1016 | 2026-10-08 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| de460e9e-4d82-3f03-afc9-0bbd6e487b77 | -14.6701 | -51.4643 | 2026-10-08 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 07e86985-836c-3d80-858d-e99091772adb | -8.0769 | -45.5886 | 2026-10-08 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 36f7f117-d569-3fcd-8615-8e429bbd8700 | -11.3367 | -46.6773 | 2026-10-08 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| cb03eabf-fe55-32c5-921f-55efd9df5a5f | -11.3554 | -46.6973 | 2026-10-08 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 1b03fe7b-c43d-342e-9724-f579cbe1ed57 | -8.9501 | -45.1334 | 2026-10-08 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 4aa320d9-6ed6-32bd-b769-bf5b9d3c02d0 | -10.4147 | -47.2846 | 2026-10-08 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 911e814a-e7a4-3e76-8402-11995e6386fa | -13.1641 | -54.3178 | 2026-10-08 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| c88549ef-684e-3545-a913-7c06315a1fbc | -8.6106 | -67.0486 | 2026-10-08 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 1b3871bb-6260-3cbb-985e-e54f4e03cb91 | -11.3986 | -47.5635 | 2026-10-08 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| c0e10038-315d-302f-8d01-ac975aa9f6e8 | -14.6701 | -51.4643 | 2026-10-08 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| bab3fd7a-be10-3013-91f6-4dd7d252b591 | -10.4337 | -47.2824 | 2026-10-08 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 289.1 |
| 7a3d5314-2331-39b2-8b42-a22363c2d9dd | -9.1543 | -49.8142 | 2026-10-08 13:20:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 865c967c-26ad-3bdf-8c35-05f479df23d2 | -13.1833 | -54.3158 | 2026-10-08 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 8bc06835-a20b-3912-9c0a-1fb58a0391b3 | -8.6291 | -67.0482 | 2026-10-08 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| e9592876-cec7-37f2-a534-6bc5b3e9934e | -10.4527 | -47.2801 | 2026-10-08 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 203.8 |
| da2a50f9-9c92-34f0-9f4c-eabd32f8595d | -9.0592 | -65.9209 | 2026-10-08 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 988d8669-dec7-32a7-b256-901dc96275e3 | -7.2185 | -55.1016 | 2026-10-08 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c6b770ea-9f4b-3b4f-801d-901ce87a756b | -8.5313 | -46.911 | 2026-10-08 13:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 7c4b3aa1-abee-373e-80f5-da470e7203e9 | -7.8876 | -55.0023 | 2026-10-08 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 396eb295-b4f8-36df-85c3-4d17e1ad76a9 | -13.1639 | -54.3385 | 2026-10-08 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 535176d9-ea21-394f-8a6f-23a8e156e3ca | -9.9398 | -43.5542 | 2026-10-08 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| e1a65331-077d-38a9-b7dc-ab5420095b10 | -11.619 | -43.6196 | 2026-10-08 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 59ab6057-fb4d-3aae-a818-0ae0cb21f05f | -12.834 | -44.4362 | 2026-10-08 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 542a6514-c4fd-305f-a243-2a6a4498a572 | -10.351 | -47.7571 | 2026-10-08 13:20:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| a290efed-4ca0-36bc-ad75-5d5d3951ff84 | -11.3103 | -44.8337 | 2026-10-08 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 096c560c-55fa-3289-9cad-89f0fbdb3c39 | -8.6107 | -67.0116 | 2026-10-08 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 136.4 |
| cd880566-0d3a-3a73-8dc9-1dd9f9695c1e | -8.6292 | -67.0111 | 2026-10-08 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 99b88b39-447a-318c-ab29-6905c83dadae | -8.6107 | -67.0301 | 2026-10-08 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 400.3 |
| 01cc9103-41b5-303d-a84f-ecffc40f577a | -8.9501 | -45.1334 | 2026-10-08 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 34df3874-0e9b-3d25-a7ae-03aff6ca3b8b | -8.969 | -45.1313 | 2026-10-08 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 821873e4-6f89-3caa-8474-fbdb40643825 | -8.0711 | -55.2921 | 2026-10-08 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d100e30a-056f-3d46-a1d6-e8d8ca9a5a17 | -11.3539 | -51.8654 | 2026-10-08 13:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ea89f9ab-9bd9-3da9-9f78-4d76fb3b4e0a | -8.1876 | -54.7219 | 2026-10-08 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 7a603d97-6dba-3c48-8dce-b8be8f76b543 | -11.8676 | -48.0348 | 2026-10-08 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8029e0e7-23e9-3568-8750-4678e522da18 | -8.0769 | -45.5886 | 2026-10-08 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| a5b36f62-6903-36ea-9c1d-1e12abd61d99 | -7.5286 | -45.8659 | 2026-10-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ad6266c4-3eee-3a30-8f54-cf9519a2d140 | -8.969 | -45.1313 | 2026-10-08 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 0d08f9a8-346d-3e57-8c7a-5a67d5d9b695 | -13.1639 | -54.3385 | 2026-10-08 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |


[Clique aqui para ver as próximas entradas](README211.md)
