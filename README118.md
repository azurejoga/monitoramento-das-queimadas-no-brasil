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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93ebeddc-9979-3030-9ee1-6cec79220203 | -11.24068 | -47.78369 | 2025-10-05 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d9a45d9-2517-3d79-ab14-61920d9ee1a9 | -9.30993 | -45.66645 | 2025-10-05 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5ba4566a-257b-3021-95f9-b3f960e5cd41 | -7.16431 | -46.21273 | 2025-10-05 05:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05834587-444d-3d6f-8f7c-368387fcfae2 | -9.06855 | -47.01655 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9ef203b-072d-3e60-9be3-d5f653555b29 | -7.58373 | -63.35677 | 2025-10-05 05:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50d078a4-5312-3b14-ac2c-f9b0dbb4663d | -9.30037 | -46.00003 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b64a67e-a671-3207-a809-b7816163cab2 | -11.46282 | -51.51563 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd444a95-7dd4-342b-b3ad-25d2e12e4240 | -8.60741 | -54.96539 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8a5c321-3b4f-3629-b2e5-757c1472dcc6 | -7.31517 | -45.56406 | 2025-10-05 05:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4f8143a-baa1-3287-b1e7-3a639c076a3d | -10.84719 | -47.97472 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe65b1f9-6537-3b22-91ad-8ad11f7530aa | -7.06887 | -55.45307 | 2025-10-05 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49b88f1a-6184-3f49-a18f-35b933f39226 | -8.59879 | -46.30014 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8909e9e4-abda-3455-a389-50e601a45816 | -9.04066 | -61.64404 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83769b23-385d-3437-9591-0cfc0fcc13f5 | -6.25004 | -45.34362 | 2025-10-05 05:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5052860-5b37-3f5c-b9d7-abd27e895848 | -5.60982 | -51.80981 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7a62cef-f488-3ae9-9622-e779bf9897c6 | -9.20147 | -59.40416 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 285a3ead-0c68-3b5b-825c-5cdab23d4adc | -9.21938 | -62.46822 | 2025-10-05 05:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9130a190-d3b1-3b3f-a67c-3be191a66f62 | -10.46154 | -57.50745 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6199dbb6-f4e2-3416-a19e-057be12c90e9 | -7.435 | -46.51965 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1083b497-a619-3382-a8b4-e612321af708 | -10.46656 | -57.4973 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d51e07c-971a-3532-a839-7ea23596e504 | -6.18373 | -44.5836 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d9b85f7-607d-30b7-a841-b0c3f8691dca | -9.84047 | -59.47072 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af3e7ea5-6940-3d91-b78d-e5b10a2671be | -9.19906 | -58.9622 | 2025-10-05 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b529a31-11e3-3ffd-bdb2-940a64951e4d | -7.44071 | -46.52141 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6271c5ce-8ddf-3c4b-9daa-862dc46322d1 | -8.59559 | -46.30371 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0e711eb9-d576-3811-9721-c7bec33b966b | -9.80524 | -56.17085 | 2025-10-05 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf24abbd-5b52-3915-869a-50f5bd84efe0 | -6.80547 | -63.05399 | 2025-10-05 05:14:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0864f714-9a0e-3ddb-8bcf-30da1e5a6361 | -11.77865 | -47.55547 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11ad6eca-8cbb-341d-94d2-45ce482a5aa9 | -8.54852 | -46.27161 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6d1eb7f1-3d6b-366b-a55a-f7dde67ba39b | -6.45794 | -44.58507 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ca7fd272-4cea-3314-903b-de6d96a45043 | -8.61582 | -54.95824 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cea16c20-dced-3419-b1c0-cbb6aa3a7fc1 | -9.16284 | -62.2282 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6ca48ed-8cb0-3d44-9021-38977ebc3bdf | -10.6953 | -56.1614 | 2025-10-05 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 297376d6-5437-3e62-a2d6-27a50d6442b6 | -9.56781 | -46.11958 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f22079b4-515d-32d8-8c56-053d01a07641 | -9.9039 | -45.96103 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 511108d1-09b2-3414-ba41-3e07ff737d67 | -10.27474 | -48.08292 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0de9b49f-2bb7-389f-8e64-afc9d987a999 | -9.64757 | -45.84983 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 660beab5-2ee9-3137-880d-3866c536f694 | -7.13141 | -63.12064 | 2025-10-05 05:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8832dd6-c2a6-3bb3-946e-ceb14d104e14 | -8.61459 | -54.96648 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abc5e67a-17ac-36d3-9724-46f61dd83f0d | -9.32797 | -54.51668 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c86d135-0ce8-3fe4-b937-cdcfc0f804cb | -6.14825 | -44.59094 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45832201-aba0-3375-a2de-331f3c72b60a | -11.67484 | -47.48573 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9dbbc524-2da4-35d7-96be-f4d2d6623713 | -11.80395 | -46.85103 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22aa8502-5fd3-3d84-9b37-ee24f5a8e990 | -8.588 | -46.31279 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d0be1138-94a3-31ab-a358-602b66a7370e | -5.52041 | -44.20759 | 2025-10-05 05:14:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19302f96-d961-32bf-9221-253783f47d33 | -11.81032 | -46.85149 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63473936-8402-35e0-b518-1d67261d360b | -10.39942 | -45.41486 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 109e4eeb-e5e8-3bfa-8b1f-e3a79030ff5b | -4.69052 | -46.82485 | 2025-10-05 05:14:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2aa7cef-ed1d-3e6c-baa3-b0c661708245 | -10.50048 | -48.11219 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c988df73-a357-31cf-adf2-bb3708520487 | -11.80029 | -46.82656 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef78e105-03f5-30e6-b2cc-9e4d14b3dcc6 | -6.42311 | -44.47222 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f0f4140-e32f-3bf9-aaef-aea183094fb0 | -7.4346 | -46.52061 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aad37961-a98c-341a-8dba-177c0631df2b | -5.34643 | -45.29908 | 2025-10-05 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 547640fc-99d7-3b36-91b6-fed4a5a0e9b6 | -11.46618 | -51.52592 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc3bf436-4c7b-3ed9-99a3-259b6f763a04 | -11.78592 | -47.92086 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d4d8241-1543-3b05-b67a-42774db54c87 | -8.53396 | -46.33564 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b3d32a0-5dd1-3490-b4c3-4809aba38d69 | -11.59615 | -46.7146 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c4dccfb-8484-3732-abe9-06492b40bc07 | -6.14994 | -44.57851 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 241283bd-dea7-343d-be3c-aef40f87f73f | -11.75747 | -44.74054 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 10c46825-6686-330a-8c1e-bec06182afb6 | -5.92371 | -43.32219 | 2025-10-05 05:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d51fa60b-9755-397e-9056-05d1b591bd57 | -7.42523 | -46.4991 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d0893e2-13a6-38c1-9495-e168378649d5 | -5.37597 | -50.90278 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adf1a41d-c291-350f-9b11-58473c8442c7 | -11.01936 | -46.69145 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 018019bc-3f08-3060-be54-23fbd2fc41c4 | -8.42109 | -70.12581 | 2025-10-05 05:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1910659-d37d-3c2d-ada1-3162cdeccda4 | -10.35898 | -55.38591 | 2025-10-05 05:14:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7aa7fb2-70d6-33d2-a77a-6b6b3598559d | -9.56017 | -63.2122 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fdfecdd-b4cc-33f4-9eb3-5d8f62b4387c | -6.16849 | -44.59414 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fdb37667-8cfa-359e-a220-e9059bc017a2 | -7.5844 | -63.35289 | 2025-10-05 05:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e3ca3b0-1f90-32e0-b90c-699861705327 | -8.59005 | -46.31907 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cbfffc23-a08d-3fac-a575-c99fe76f6661 | -6.59756 | -44.3217 | 2025-10-05 05:14:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5628f52f-122c-3152-9f4e-ee39568749ae | -11.09262 | -47.88738 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f28f10a-650c-3261-93ff-33910e148d19 | -9.14448 | -60.29455 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ef76a02-9b9b-3a9c-bb49-fa61213b0721 | -11.77801 | -47.93722 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a46ac8a2-2cd9-3ec3-8c47-ee673bf66a63 | -11.45354 | -51.51452 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53c1a023-ff57-37b9-9fe7-92b820d3ee32 | -9.56805 | -46.12582 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55996d96-9e81-3410-8575-0d82c62e2518 | -10.3511 | -48.1707 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9e7543a-296a-3fab-95f5-54c2d33339d3 | -11.8161 | -46.85711 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5fcaa4fa-90b0-3e7d-85cf-6032dafffa17 | -9.41695 | -49.21645 | 2025-10-05 05:14:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16610971-30de-3d7b-b87b-9d6d1f08b064 | -11.83167 | -45.08564 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57a9b6e8-446d-3801-9b2f-86b240e882ac | -10.8475 | -47.96902 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d8b9bf8-9554-31ee-8f84-8ede8b68dde9 | -11.12918 | -47.92942 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c48a4ba-89ef-3de6-be8b-65943ed81380 | -5.12623 | -46.23487 | 2025-10-05 05:14:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b6a6e5a-8182-33c0-bc86-d9a63f38df71 | -8.86086 | -46.84128 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99fe5743-478c-36cd-9e4d-148a0eccf8d0 | -9.33843 | -54.52279 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38532195-a289-3386-bf4a-e61b81e60f71 | -8.56226 | -46.26443 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e25f85e3-e866-35e3-9d25-79f2e8338a0b | -10.35644 | -48.1744 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 49c29196-c8d4-3db0-bf18-9be1547fda39 | -6.17274 | -44.61345 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cca2ec53-60ff-3067-bc0b-e87a723631e0 | -11.07003 | -47.77681 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62cb4e4b-5220-3222-9119-5b1903a4253d | -8.56844 | -46.26625 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f2cc3812-dbc6-3d2b-9253-5089c752ef45 | -11.86701 | -44.95972 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9626532d-3ff2-30a9-91fd-dbaf184c0c48 | -10.78239 | -51.63459 | 2025-10-05 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ef2daf5-61a4-3961-a026-8f0689634ca4 | -9.84118 | -60.27629 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fa39e55-bf6e-3e22-9f38-86bf1386c1a6 | -11.12589 | -47.90799 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07407dca-ed0e-3669-834c-1b2172c03ca7 | -4.36518 | -50.86549 | 2025-10-05 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 112a64c4-feca-3b9e-a378-6bd2eea801b6 | -11.11656 | -47.17554 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ca591c6-cbe5-3d10-9429-f9e05f4c3125 | -11.78525 | -47.55172 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f154f94-5cb5-3492-ae69-4826760e3ae1 | -9.33473 | -54.52223 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27cc493c-f0fa-3b30-9190-b5f699265491 | -7.80129 | -46.01988 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 245ee5fd-30be-3397-88bb-e7f1c44a2ff6 | -11.09682 | -47.75415 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 327d0e30-11d5-3c17-bf5c-582cf4e3d54e | -11.52322 | -47.67072 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README119.md)
