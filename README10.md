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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 170d1b4b-164f-3517-83b9-52c610a58832 | -10.49994 | -53.65657 | 2025-06-06 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3617faee-8ee8-3a6e-b409-5fed6ff7faa1 | -15.52839 | -48.50544 | 2025-06-06 04:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3643759b-964b-3758-bcd0-813f8ad3d939 | -9.39582 | -48.42874 | 2025-06-06 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d9fa9ab-e20a-3ceb-a8c6-a8392aad1c67 | -13.51662 | -56.56676 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df16c84a-a101-3fb5-ba94-370df571a343 | -13.57161 | -44.26553 | 2025-06-06 04:42:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1424f93-a23b-3429-9352-c24ca7d5a00d | -13.36036 | -52.40092 | 2025-06-06 04:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e4e87b61-e556-3559-a0f2-c45e17047b59 | -12.83491 | -47.38964 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 869faafc-8a7e-3aae-b37d-d4abc71bdfaf | -11.53636 | -56.45603 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 994d1cd0-9222-3273-b469-0c44e0709e8c | -15.07693 | -48.94407 | 2025-06-06 04:42:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd228688-389d-396c-9d83-383b364982d6 | -11.29616 | -53.98475 | 2025-06-06 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cd9e336e-791c-3a89-b468-394ecb1afe95 | -10.81626 | -56.95742 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05bc13d6-57d7-36bc-bf48-d7ac72e15541 | -12.74247 | -48.92104 | 2025-06-06 04:42:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e4f4c306-f70d-358f-b229-780cfd029e71 | -14.22053 | -45.49226 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29afd2a4-e6ce-3190-9514-33db370ba7db | -9.38054 | -48.55135 | 2025-06-06 04:42:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 376938f1-6881-39ce-bd31-563fa40919d5 | -9.22524 | -48.8595 | 2025-06-06 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d14c2d92-3c60-3efa-a4e5-64efba5da521 | -13.5125 | -56.56602 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5052232e-ac93-33a5-b959-daf0fa11f7f8 | -14.73306 | -45.08745 | 2025-06-06 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eae95cb3-26d1-3054-8bd3-8d4764a86738 | -13.88715 | -54.67801 | 2025-06-06 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e46e79f6-c39b-3007-adc1-6459a714dc6c | -15.15095 | -45.51106 | 2025-06-06 04:42:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 211ba7dc-8d04-3c30-8d9e-bfd740571954 | -11.38129 | -56.54831 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab55ce93-8bcf-3375-bb88-8ff008b0c58c | -11.38409 | -56.55718 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abb62a7b-597b-39be-9789-a749475da5e4 | -13.51941 | -56.57502 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf7114f1-4015-3cec-afd2-9b861355e56a | -14.73248 | -45.0918 | 2025-06-06 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35c5caf9-36f2-3169-bc42-9e6fb3b433d2 | -11.13483 | -53.94617 | 2025-06-06 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15945cdf-1932-367d-a695-ea7d8ef35388 | -13.88424 | -54.67299 | 2025-06-06 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcad30dd-24a2-3de6-ba91-75fc4119deb0 | -9.52425 | -54.77524 | 2025-06-06 04:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81988ba9-8f90-3da5-acf3-74b099e714bf | -13.074 | -49.24686 | 2025-06-06 04:42:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfec619c-e68e-3d86-b0ed-10b7dfb97240 | -11.29982 | -53.98538 | 2025-06-06 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d443c968-eb9b-38e7-9ea1-88caaf7b6787 | -12.2669 | -55.07604 | 2025-06-06 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50919f77-701d-3e09-8d60-8b2a75351b46 | -12.96395 | -46.77269 | 2025-06-06 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25e60d8b-0c0d-309b-b8f0-564883afff46 | -13.51596 | -56.57051 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccc856ed-7371-3983-8914-6a646fd1949c | -10.07304 | -52.75313 | 2025-06-06 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98cf8042-d904-3d85-8c5e-f834546561ba | -12.66254 | -58.22445 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 480a8e5e-121a-36f3-8208-1309e4595aa6 | -12.26843 | -55.07851 | 2025-06-06 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24109297-4829-30de-87c5-66ce4034cee8 | -10.49488 | -53.66442 | 2025-06-06 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0d847ee-5486-3d62-a093-617cb84a37ac | -12.66441 | -58.2146 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e2a882e-ac9b-3cee-bb0f-5ef0e7d2356e | -14.66426 | -53.12368 | 2025-06-06 04:42:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6642344-72ab-3bda-8942-b08b53442ff2 | -9.20131 | -49.68549 | 2025-06-06 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1263ddad-0b16-3b4c-90ec-233f22ae75fd | -10.46274 | -47.94621 | 2025-06-06 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 37b67139-5395-316c-ac73-94821398452b | -10.65938 | -55.30827 | 2025-06-06 04:42:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8b55287-eae3-35c0-9c82-0382cf96dabd | -14.22423 | -45.49686 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e401de13-b472-3695-ba58-c58ccd3eeca4 | -11.13921 | -53.94246 | 2025-06-06 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61465236-dfe1-38d7-bc7d-cf58e69c49cc | -11.13645 | -54.21973 | 2025-06-06 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10efaf51-62c6-3d26-99b7-2791beeb3aa1 | -9.80516 | -54.72755 | 2025-06-06 04:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffa61296-82dd-331d-b5c3-5833d1cf30ff | -12.53295 | -58.35782 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c95b340c-0645-3ecd-bbbb-4577c047b750 | -14.22846 | -45.49748 | 2025-06-06 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2866930-8247-32fe-9ac3-83e08bb47db5 | -12.66188 | -58.21778 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e76ec45d-aa4b-3a26-8b54-fad6cd48692d | -13.51963 | -56.56285 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| efea57f8-8c9e-316d-9c4e-3416e4deb035 | -10.47101 | -51.88735 | 2025-06-06 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49f31890-60b1-3dd6-ad46-73a17a5dd081 | -10.2957 | -57.13992 | 2025-06-06 04:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa0652a1-1df5-37e2-95ff-e2e9c716573a | -10.99247 | -49.02142 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93009263-0371-3d57-9523-4a9b06cb0358 | -11.91919 | -54.82057 | 2025-06-06 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04dd118d-ba69-30be-984f-147883f612ac | -10.46214 | -47.95016 | 2025-06-06 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7e8e4848-e813-3697-937f-39a5f0150f0c | -9.20076 | -49.689 | 2025-06-06 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0441cc3-8766-3456-9aa7-5786a2a9e728 | -14.74452 | -45.10196 | 2025-06-06 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5348529d-1ce3-361e-ba35-a6c0ad6c5ae3 | -14.04331 | -55.13908 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95a5507f-d2a9-34ed-a572-d572bdbe28fa | -12.66561 | -58.22369 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70e5fd02-c94a-3b37-a501-534ff2e92651 | -12.83617 | -47.38073 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e94a83cd-2269-30f6-9923-04474086b4dd | -10.69224 | -57.65212 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50542bff-2712-32ce-b33a-92448c0509df | -14.30232 | -47.98879 | 2025-06-06 04:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5711087d-084a-38d0-b00b-cd1513571f94 | -9.39639 | -48.42503 | 2025-06-06 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16f22af3-3eee-3a33-a162-18f6766a8fbe | -13.07457 | -49.2431 | 2025-06-06 04:42:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41caff99-1ef0-3a86-830e-59bab785941a | -10.68884 | -57.59133 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dea3882-711f-3535-b1bb-72da19050a7a | -10.64737 | -44.49585 | 2025-06-06 04:42:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13b2dbd1-c5e3-3a33-bead-a071dd34ee28 | -11.11863 | -54.66412 | 2025-06-06 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf681af8-6e6c-3af3-be0f-e1dfa03ca380 | -11.57278 | -44.87752 | 2025-06-06 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7bf73fd-eac7-390b-b284-59c010738fb0 | -9.66994 | -48.71144 | 2025-06-06 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98727cc2-09a2-395f-a41c-194e5d002444 | -11.94689 | -46.63387 | 2025-06-06 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e74b212-e3e2-3259-87d9-6e24ce2a3d2e | -10.86675 | -57.67046 | 2025-06-06 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f533bff6-cd74-359c-8d72-3d90fc25a334 | -11.13773 | -53.92881 | 2025-06-06 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43e5854e-ae82-3aa7-bb6d-fbf4ba28926a | -9.24067 | -49.79943 | 2025-06-06 04:42:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56c90d11-d1f9-30fc-aeea-38fa592d077c | -10.49852 | -53.66502 | 2025-06-06 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 862a1f5a-e1cf-3ed9-beae-82a75dc96e2a | -13.08142 | -49.24419 | 2025-06-06 04:42:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2573e261-b38d-38f4-94df-15830ea6b17a | -11.9238 | -54.81654 | 2025-06-06 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 1f598fb4-5a15-3cef-a0c7-04c65e2e2b5f | -9.2213 | -48.86259 | 2025-06-06 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7842660f-e283-33b7-9235-aefde33038bf | -12.38266 | -47.31375 | 2025-06-06 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34e5e83a-482c-3950-8484-988831481061 | -10.30021 | -57.14077 | 2025-06-06 04:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c98dd507-a99e-3d36-b0a7-5e6512c3e0c7 | -13.51551 | -56.56213 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 12df5fcc-3b56-3059-91be-99608aacd59e | -10.07654 | -52.75372 | 2025-06-06 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5046d73-1863-3f2a-a6d4-70589c1d6550 | -11.31927 | -49.21068 | 2025-06-06 04:42:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff997f45-32eb-3efa-80d3-f823543a16e7 | -13.52074 | -56.56749 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b7056f8d-6645-36a4-aca7-f82edafd336e | -11.57837 | -54.88878 | 2025-06-06 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dc0ce16-4e3c-3eea-86a3-a9ab5a27ead4 | -10.65844 | -49.35783 | 2025-06-06 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7611979d-8219-36e2-8560-2137f76a934a | -12.83862 | -47.39019 | 2025-06-06 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe0a484a-16fd-382b-8a16-b8b0b5c09e19 | -11.53285 | -56.45131 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbafcfdf-9136-3aad-b657-233a06c68e17 | -12.52991 | -58.3539 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95e609d5-9b76-3f01-a972-c58ec0c4e8df | -13.51728 | -56.56301 | 2025-06-06 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b362b8d-3359-338d-8e08-af3268934120 | -10.30471 | -57.14164 | 2025-06-06 04:42:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6409f855-2b34-3a20-aa6a-6ea27726d53a | -11.53073 | -56.43875 | 2025-06-06 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af219c95-ae2b-35ba-b831-d38548fd9acd | -10.46565 | -47.95071 | 2025-06-06 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e9c9bd1a-e183-3823-bdd1-384af0614617 | -12.66652 | -58.21874 | 2025-06-06 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26a9a4c4-0471-3718-96c3-e77958f87d10 | -10.45804 | -47.95354 | 2025-06-06 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 980e3e6e-10a4-341c-9341-c40f29983d70 | -12.42622 | -47.1972 | 2025-06-06 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 54d3d394-d6e4-39f2-9b19-0dd195f1c771 | -9.52511 | -54.77031 | 2025-06-06 04:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 631ed201-8f1b-3f7b-b819-e3ac773fc9f6 | -14.02539 | -55.13098 | 2025-06-06 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30eabff0-81f8-3afb-a43a-7b938cc2d3ec | -13.88275 | -54.68164 | 2025-06-06 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4aa77479-54be-3323-a416-c10f6ccda90c | -19.39626 | -54.46738 | 2025-06-06 04:44:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ab1d0ee-4756-372d-9518-5c191a5b57b8 | -19.43072 | -54.77895 | 2025-06-06 04:44:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e9c1a2d6-3088-3771-b931-039d563da846 | -17.25534 | -43.64101 | 2025-06-06 04:44:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6458c70a-ae7a-3df0-9a58-ff46df4f2f4f | -19.43139 | -54.77499 | 2025-06-06 04:44:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README11.md)
