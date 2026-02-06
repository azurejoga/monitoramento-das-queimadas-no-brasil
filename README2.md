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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9ae5726-792c-34c6-9cef-ddfbc1fa15c4 | -5.90511 | -43.84549 | 2026-02-06 04:21:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f04c6d8-c7a8-3ad1-9c6e-2f91c97710d0 | -5.34079 | -45.12482 | 2026-02-06 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78b4870f-31cf-36ae-ba72-dde388029365 | -5.90456 | -43.84899 | 2026-02-06 04:21:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4adfca86-cb3a-3182-877e-caa3e4ee32cc | -2.61069 | -48.29277 | 2026-02-06 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64f4a16c-e9e1-3a8e-8d39-c4ceeda086b6 | -5.10438 | -39.45893 | 2026-02-06 04:21:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 82e65af4-e777-31e7-8e8e-bec35e55eb2c | -2.11421 | -49.00018 | 2026-02-06 04:21:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c877e79-686c-3f33-b480-358b4d598d53 | -5.34464 | -45.12188 | 2026-02-06 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e11aa7b4-9bfd-370f-a449-0e0a00978d01 | -5.90124 | -43.84847 | 2026-02-06 04:21:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05e7381c-5cf3-32a9-82e3-093f564b1148 | -12.02521 | -40.83959 | 2026-02-06 04:23:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e49cc835-c3a2-32db-9b26-6c496c4c698e | -8.28389 | -44.89301 | 2026-02-06 04:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ddb2017-8186-3430-bf30-3309de2faa56 | -11.84372 | -47.60219 | 2026-02-06 04:23:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d8dc942-7c47-34b4-a067-995f7494e172 | -10.80204 | -44.48634 | 2026-02-06 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1390606-d956-3705-91f3-aaaee54504b3 | -11.677 | -43.89836 | 2026-02-06 04:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c015daf3-a372-3dbf-9526-7b9ccf55088c | -11.01693 | -44.83546 | 2026-02-06 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae192c2f-d117-3ba1-89ae-2b95ffe6f0d7 | -10.04216 | -36.21205 | 2026-02-06 04:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cade0827-6239-3ed7-80fd-b8e9de87ac72 | -12.04384 | -44.30101 | 2026-02-06 04:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfab70c0-d0cd-303a-a21b-d938fa31d7e6 | -11.68002 | -43.89871 | 2026-02-06 04:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5eb873c6-d756-38c0-94f3-62cc70be7c60 | -11.0136 | -44.83493 | 2026-02-06 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc1b9b07-6ff1-3d34-b1d5-9d60513cf265 | -11.67658 | -43.89817 | 2026-02-06 04:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f20c8419-735f-3ff6-8d54-9fa703c1d93f | -13.42484 | -46.58912 | 2026-02-06 04:23:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dbd3033-e209-3f17-8456-64631d954b78 | -10.03873 | -36.21349 | 2026-02-06 04:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d25a795b-559d-3de0-ba2c-457e51564a99 | -6.84216 | -48.8417 | 2026-02-06 04:23:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc6afd9d-5219-3f28-aa24-1ba5dfbc4dae | -6.2568 | -43.68475 | 2026-02-06 04:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| becb80f3-31a8-3bcf-95ae-ae11ea9d4e78 | -12.20973 | -39.33179 | 2026-02-06 04:23:00 | NOAA-21 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 022068b2-0387-3035-bbe5-b43ccc84dd1d | -11.13443 | -37.19812 | 2026-02-06 04:23:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 631d9098-f081-3726-9a1b-f4c56cf7a5f6 | -10.03628 | -36.21487 | 2026-02-06 04:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| def00d8c-74e0-3ab9-a501-f0afb9b6b142 | -10.03674 | -36.21136 | 2026-02-06 04:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a555f91e-04fe-3ad2-a939-80a269ec36bb | -7.46057 | -46.20507 | 2026-02-06 04:23:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5369f426-d4db-3540-b1a9-50eb503bafbe | -11.96621 | -44.51626 | 2026-02-06 04:23:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1170efe7-1b98-3a08-b67a-08b23e63143c | -13.15754 | -39.70239 | 2026-02-06 04:23:00 | NOAA-21 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c7236504-8513-317f-9354-ea0e27bfd9df | -11.67714 | -43.89436 | 2026-02-06 04:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6b60b1a6-ab47-3c1b-824f-97020b6245f6 | -10.13675 | -42.15643 | 2026-02-06 04:23:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 037bfb7f-199c-3563-b95e-6cb0d6b97ad6 | -11.13482 | -37.19503 | 2026-02-06 04:23:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 427820f5-147a-30d7-846e-0ab1d01a2c1b | -10.0417 | -36.21556 | 2026-02-06 04:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1ba62f86-eb0d-3ec2-b9c8-268443cc45a7 | -11.11692 | -41.07416 | 2026-02-06 04:23:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 46c5a271-0a57-3798-8562-b6fe0b6224f5 | -11.67758 | -43.89455 | 2026-02-06 04:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c5958634-a4f3-3db4-9279-8b1b5c23e799 | -23.47536 | -51.58766 | 2026-02-06 04:25:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7957bdea-d3df-308d-b574-fb4ed61c3820 | -24.32255 | -49.72798 | 2026-02-06 04:25:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3963f6b4-f0c1-3188-902f-964f9d2d7470 | -24.17152 | -46.78249 | 2026-02-06 04:25:00 | NOAA-21 | ITANHAÉM | SÃO PAULO | Brasil | 3522109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 5bf599ce-4d75-31fd-86fc-4721656e7e49 | -24.17554 | -46.77897 | 2026-02-06 04:25:00 | NOAA-21 | ITANHAÉM | SÃO PAULO | Brasil | 3522109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 5e5a5eb0-1036-34cb-bbb8-0c51198e3057 | -24.32586 | -49.7286 | 2026-02-06 04:25:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbcf8fba-ee88-306c-8f8b-17b3f1b54ccf | -19.22507 | -53.8631 | 2026-02-06 04:25:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91d923a0-b313-3b7c-bc0b-cae39ec9a555 | -22.02802 | -54.00961 | 2026-02-06 04:25:00 | NOAA-21 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 799b8ec8-c3e0-39ba-928c-26458a6e7a13 | -23.0818 | -46.9932 | 2026-02-06 04:25:00 | NOAA-21 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dee6da37-94ba-39d5-8d4c-93fc591104a5 | -31.78201 | -52.50545 | 2026-02-06 04:27:00 | NOAA-21 | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| a7020a95-2779-3c29-b32f-9b390a70be76 | -32.14172 | -53.12239 | 2026-02-06 04:27:00 | NOAA-21 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 5.9 |
| abaad851-1980-3aef-b5d0-23284d700661 | -29.51639 | -50.44502 | 2026-02-06 04:27:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fb0dc9ad-aa81-3790-96f0-53dd94ed5f0e | -32.14099 | -53.12664 | 2026-02-06 04:27:00 | NOAA-21 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 5.9 |
| 38ee0ae8-eb91-3af4-8741-cb611567593a | -28.98205 | -50.68131 | 2026-02-06 04:27:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 952c0076-f1bb-3fa2-a869-cf35e224372a | -30.53519 | -52.72004 | 2026-02-06 04:27:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 17af4925-7212-3342-9584-390b51ee4daf | -28.82804 | -50.29905 | 2026-02-06 04:27:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| acbb3626-94d7-34cb-930f-5fa37ebc2da4 | -30.29603 | -50.91925 | 2026-02-06 04:27:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 3f72ecd9-ef10-3bd6-a58b-798fec0ef193 | -31.78536 | -52.5062 | 2026-02-06 04:27:00 | NOAA-21 | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| e2e9d48b-8e97-35ec-bbe5-33dc4e53afae | -30.04743 | -51.13177 | 2026-02-06 04:27:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 678fe74e-630e-30dd-9370-4670c827b378 | -32.15184 | -53.12483 | 2026-02-06 04:27:00 | NOAA-21 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 3d6c998e-77eb-356a-848b-33aa3f651d7d | 4.0106 | -60.7981 | 2026-02-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c800235c-3807-3611-9cd3-add657a0de88 | 4.21985 | -60.41346 | 2026-02-06 04:48:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21ed5bfe-6146-3a21-bf64-2e43ed4456c7 | 4.01684 | -60.79719 | 2026-02-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7df12384-2b75-3549-b0f9-3a0549626050 | 4.34186 | -60.94227 | 2026-02-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7b88c3e-534d-30ed-9d20-17802f81d2b3 | 4.57259 | -60.66196 | 2026-02-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f4fb13b-7703-3fdc-81d2-45cf60e9b4e9 | 4.00991 | -60.7934 | 2026-02-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0175f76e-2ef1-376e-a45a-c27138dca437 | 4.33543 | -60.9441 | 2026-02-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56534228-ff58-38e8-8d33-d5e7c0a2d8c5 | 4.33965 | -60.92696 | 2026-02-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 571707f5-080f-321c-ae32-6b9534532f50 | 4.21265 | -60.40827 | 2026-02-06 04:48:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cf16670-e04a-306e-b9ce-f36b4ffa7f5c | 4.57167 | -60.65545 | 2026-02-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 718654f6-4ac1-3453-b8a9-2cd0dc450bed | 4.21311 | -59.97535 | 2026-02-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a82781b1-494c-3f1a-b2c0-d189c286a502 | 4.20898 | -59.98501 | 2026-02-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba871711-4684-37ba-a551-4c84fa6193a0 | 4.20832 | -59.98052 | 2026-02-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a87a15b0-8415-34d0-a66c-98ed52f18243 | 4.5781 | -60.65427 | 2026-02-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45b10a50-1798-3b73-8d3d-e75f930f8f6c | 4.21374 | -59.97989 | 2026-02-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 268823d5-ab82-38b5-aba2-aabf302f9c92 | 4.21377 | -59.97471 | 2026-02-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdc02ce6-be34-3bed-aaa1-6ad96c1a93ad | 4.01035 | -60.79801 | 2026-02-06 04:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7269a8d9-9b2a-33d8-a464-64194abc0613 | 4.21443 | -59.97923 | 2026-02-06 04:48:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2c6a2bf-3684-30f7-b7c5-9d61502800b3 | -3.18151 | -48.02702 | 2026-02-06 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 289961a7-bf1b-3098-b4d7-439946341e0f | -2.5758 | -54.72562 | 2026-02-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 557bb18a-08f7-3c43-9b92-587a154fb123 | -3.68366 | -52.53695 | 2026-02-06 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0477d10-64e9-3053-9a77-b793fe91ace1 | -3.14834 | -48.14756 | 2026-02-06 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c49b9f92-8373-379e-9eb9-128e9494e09e | -2.52294 | -51.82053 | 2026-02-06 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19837e03-df20-3c07-807f-39cc8e0d3f3e | -3.69416 | -49.56379 | 2026-02-06 04:50:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13141fd6-b789-3f44-8516-86ffc21504f0 | -2.22553 | -48.29031 | 2026-02-06 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55b4d927-f6f1-385d-9412-9602031114fd | -2.98842 | -52.35971 | 2026-02-06 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 993bcb76-91be-3982-9b66-31301e6918ee | -2.57608 | -54.7236 | 2026-02-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6e0f2b6-4e27-3a1e-abf6-8e5aaa3a9550 | -2.56516 | -54.74184 | 2026-02-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52023baa-348a-3598-8633-d2e7b3803fa1 | -1.94741 | -52.93095 | 2026-02-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53062fd0-5fd4-3f2d-867c-863b4e0a279d | -1.94384 | -52.9304 | 2026-02-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76f8ac70-2387-3df3-991b-f4d7cd9ac4a3 | -3.18684 | -48.01592 | 2026-02-06 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ce8c0e9-0f3e-3e40-939c-7fcf881940e7 | -2.98782 | -52.36344 | 2026-02-06 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18687dd8-7e34-3c1e-9712-f7bf8df340e8 | -3.18333 | -48.0154 | 2026-02-06 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 65f3b80d-6eb9-3824-ba60-fb047d9e7080 | -3.6821 | -48.92877 | 2026-02-06 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8c395c0-926a-3a84-a9d5-818b6a34d1ff | -4.00396 | -50.32316 | 2026-02-06 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8dd726a-456b-358c-9354-476bd6cf0832 | -3.15182 | -48.1481 | 2026-02-06 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6c89100-67c3-3bbe-af42-ddededbf7d8a | -2.57253 | -49.46535 | 2026-02-06 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d685cf9-4a9f-3592-9bc6-77dd233aa225 | -3.18501 | -48.02756 | 2026-02-06 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcfe4df3-0fa8-3151-86f2-51e6bb7b4308 | -2.52236 | -51.82416 | 2026-02-06 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 980579e4-0e6c-3936-8bd0-c9ac72979549 | -2.61002 | -48.29162 | 2026-02-06 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5640895-ff82-3b6b-b6ba-05332f59d02f | -2.56438 | -54.74676 | 2026-02-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 891e437d-51f5-362c-bfd8-29a71d2478c5 | -2.98722 | -52.36718 | 2026-02-06 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 136899a0-9530-37f5-a0ca-3d8c42648315 | -2.4588 | -48.22663 | 2026-02-06 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25ecd873-dafe-3673-9844-e5f05cef5909 | -2.51516 | -47.81805 | 2026-02-06 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d6eaf12-611f-3a06-b18b-f19f4b54f4b8 | -1.66992 | -45.80403 | 2026-02-06 04:50:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
