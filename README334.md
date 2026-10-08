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

## Dados Diários - Página 334

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c8ed560-10a2-377a-9cd2-ed3fc1bfb6bd | -9.13281 | -45.83965 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 13768260-4ff5-3c7c-ab19-3400c795491a | -6.31909 | -35.13984 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| dc5e4260-3c9d-3d2a-a38f-2b8e6f0b25ef | -6.8467 | -39.55269 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fe393585-722f-3fbb-86dd-52ac1db41839 | -11.12054 | -47.68887 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 726786f4-7976-3869-a240-aa3c190c22bb | -9.44628 | -44.60559 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 12047b52-4169-3d94-9a87-c658743e8b5d | -5.98804 | -41.36697 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| b72a38db-0c32-36a6-a3ff-de68b743e587 | -6.36306 | -42.56831 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 9b22aee8-df19-3745-b581-b64de56cde59 | -11.0936 | -44.02109 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e93ee09a-a131-3585-8ba5-ff31ccf12898 | -9.85168 | -47.84952 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| ab8884a4-e443-3ecd-8cf3-6e3836779452 | -8.06591 | -45.606 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9bb1392a-0b93-3c90-bba0-b8587ccfab44 | -7.7601 | -54.9461 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5730157a-d230-37b1-b0a2-3b94e1d15c5c | -12.96769 | -50.9978 | 2026-10-08 16:37:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 884f7f84-833f-3041-8886-f2fc177750f3 | -11.24074 | -46.24028 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| de871033-0632-3aac-9e89-109166589ae8 | -7.53306 | -42.09007 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| a4e6e54c-e5b6-384e-8600-fc1df984e459 | -7.04283 | -45.43959 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 297e1d16-d124-3911-841e-d1e949979d58 | -8.78292 | -47.26282 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 701d0689-33fa-32a2-b550-9f330f4e3d63 | -12.15636 | -44.75029 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 310790b5-23e2-34bb-aaca-37207ad84d05 | -5.84048 | -42.41553 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a4b95eb5-0836-3312-80d2-96f6d8d4ca72 | -9.88055 | -44.86839 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 23832e87-1ad1-3a9f-8c8e-487c95fa8e06 | -7.25051 | -39.40507 | 2026-10-08 16:37:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| beb66cdb-760d-3c17-9bf9-a0f1c98aefdb | -8.93256 | -45.19367 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 1a63132f-5528-3bc3-af70-791faaa8ab1c | -6.95531 | -44.89567 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 66818043-edf9-3ec6-9671-78e841bce821 | -11.20615 | -44.86099 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 634e3f12-5890-374c-82f7-8631e1fa0d0c | -10.86088 | -45.56028 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 345aecf1-2418-3807-8b28-1eadd124162f | -7.86461 | -37.82077 | 2026-10-08 16:37:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 49feb402-86a3-3f80-8add-1b8b0c4aa03b | -6.07211 | -44.38515 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 12654ef9-264b-3d54-baba-6736c0baf549 | -7.46354 | -42.82572 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| bdfadfa7-1b5b-326a-b6c7-661bd5dfbfb2 | -10.86314 | -45.5527 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| de64945b-c154-3541-85e2-948a2281b00d | -7.22398 | -44.28711 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e543819c-65fe-35cb-aaa9-307f2c11439d | -9.1909 | -49.76798 | 2026-10-08 16:37:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d079658b-4f08-3669-980a-95e4e0bc116e | -9.76292 | -44.78725 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ae74eb6e-a974-3adc-997c-35e81763ffcc | -6.31315 | -35.14079 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| a4d75385-38bb-3886-9e18-af2959e512fa | -6.81714 | -38.53569 | 2026-10-08 16:37:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5b3f671b-ff97-3af5-866c-bfd313f0941f | -10.52162 | -47.31789 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| cc2a9319-e72c-33fb-84ef-4962160ef16f | -9.87947 | -44.86141 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| fe1b9155-6109-32e3-949b-0a5eb3e646ab | -13.12383 | -46.37052 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 00034feb-dd31-37b3-8d71-3db3dc8cdcf5 | -9.02474 | -44.38103 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8067a116-2ad4-3c12-8ce0-2d4c569767c1 | -5.98838 | -40.94051 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 755e19f2-653f-338c-abec-cf7f4d5a91d8 | -9.0445 | -46.60267 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| afb99e3c-da4f-341f-8728-051e865f5fbd | -7.76519 | -44.16336 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc11e0bf-61cf-3589-98ef-af0622729dc1 | -8.93864 | -45.18917 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 165b9e85-60b9-3cc9-94b7-1250e9d7d69d | -7.08834 | -43.08552 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 890ebd62-acc3-316c-82af-a0968af8aa58 | -8.96057 | -45.15335 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fc7cc726-a441-3c62-9e20-740bae4a0ce0 | -11.65001 | -43.68842 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 00309b8d-88d9-3360-bb0c-00ac1dc393e8 | -8.08321 | -55.29317 | 2026-10-08 16:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1086d220-c70d-3743-a906-96ff054f3583 | -13.29097 | -48.77246 | 2026-10-08 16:37:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 94c987bb-3afc-328a-9f92-842ff4bcae04 | -9.77482 | -47.81597 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 97aafffc-1e5a-3d32-a3cd-7d1ae6b4dc47 | -11.84769 | -47.30217 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2fb7ec54-da1f-3c06-bc4e-b90789284e45 | -10.16531 | -44.66824 | 2026-10-08 16:37:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d83e8011-08a5-367d-9895-d16cd5ef8aab | -6.3372 | -43.34859 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e50983e9-59f3-34ae-95ec-5d6ea56877f8 | -6.34049 | -35.12297 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 9c5bb984-28c9-3a1b-bee8-af515b339efc | -8.35355 | -47.6494 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7384fe08-d7f8-3e24-a411-c55f4ff1d6c5 | -11.61112 | -38.98305 | 2026-10-08 16:37:00 | NOAA-20 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 48c11822-1702-3df0-ab5b-1ccd368b60d3 | -5.40166 | -40.31102 | 2026-10-08 16:37:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ea5b865-132c-366e-9e79-71913f15c129 | -8.9562 | -45.14691 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 7ecb2c9f-ecdb-3447-856b-b98b880d5d8d | -17.42931 | -40.41926 | 2026-10-08 16:37:00 | NOAA-20 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 95e86ee6-8071-340d-8fc6-ff86ac606f54 | -7.69816 | -45.44136 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 01f524b3-3e5a-3d91-b94f-3cc8fb7c05e5 | -9.26165 | -40.26461 | 2026-10-08 16:37:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 67f18df2-db17-39fe-b242-47f25bd4401a | -12.22145 | -43.93762 | 2026-10-08 16:37:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 407.1 |
| 7cbab28e-865d-38d6-b95a-8b9d69278a04 | -11.79204 | -46.77675 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 52695dcb-3711-31f8-9df0-d10834d5aa69 | -8.1904 | -46.36093 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 9b11fbdd-b9eb-39b6-9881-4d5356903b96 | -11.63545 | -43.59481 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 7c6f54ce-5c91-335e-bfd6-f4e071d87dfb | -11.85992 | -47.36164 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f46abaaa-980f-39f0-bdb2-4131578fc990 | -6.69375 | -45.28931 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 63ed9d87-f97b-3ec4-90b0-0e40b439dd5d | -13.67979 | -48.64377 | 2026-10-08 16:37:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2bbbf21c-2e93-3927-948a-2e6d9438994c | -10.42059 | -47.27034 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 033599da-0605-3ac6-815e-ed5ef80fca97 | -8.96612 | -45.14536 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0db3a8fa-a2f5-3589-98ef-c0e392f39b74 | -11.13758 | -46.15973 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3b8be62e-e49d-3977-aac3-823d94d2eb32 | -8.92765 | -45.18375 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 221.0 |
| 8d23e396-4d1e-3733-b27b-a612e04637e3 | -11.76857 | -43.53944 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 37bd664b-f392-3c93-9f31-f9552379ea49 | -11.11081 | -44.00014 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 23379fe6-51d3-38a5-8fe7-a70cec98145c | -8.93225 | -50.69506 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f4c563dd-b095-3818-83ad-677d8dca696c | -8.3028 | -45.73553 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3d752270-a6d8-3472-b21d-aa33336d8411 | -18.88471 | -43.2473 | 2026-10-08 16:37:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ab539acd-1149-3e21-9691-7c8f0de140ec | -11.21993 | -44.86242 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b66e1106-b755-38c7-94bb-21aee7515192 | -8.30294 | -45.71419 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 303f7c3c-2444-3fe4-8f28-b8d6b3352e28 | -6.90884 | -43.93147 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 23a0e6dd-4e8f-319a-8294-084c5b86dcea | -6.83238 | -43.77906 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 500648ae-f2ff-33de-94d4-a3885c6d79d0 | -11.27772 | -45.19796 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 44be392d-ef12-386e-a6c0-5615489c2a82 | -10.82062 | -47.33445 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bca5341b-6e06-3109-9cc1-ccc278707502 | -11.85815 | -47.37421 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ef10a1ad-165b-3760-9c52-81f07292be90 | -18.96335 | -41.68699 | 2026-10-08 16:37:00 | NOAA-20 | TUMIRITINGA | MINAS GERAIS | Brasil | 3169505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 3ef10fac-be84-3f0d-a54e-f813e8eda1b0 | -10.43728 | -47.28753 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8733cf19-ac5e-3d3f-8fbc-e38900ef9621 | -8.25217 | -54.64817 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5e075ea4-5b39-3130-85f2-e90c5c294e73 | -8.7858 | -47.37701 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fbcd7da7-5624-3703-881e-e72a65017259 | -11.59148 | -43.66462 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 9ad05bb6-0edd-30fb-ac6d-8016e873c7a2 | -8.75601 | -47.57477 | 2026-10-08 16:37:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7cbfa030-774f-3816-b637-df5ad5d0e6bf | -9.9029 | -44.79336 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e2807711-e593-3638-ae12-093ab99c9275 | -8.69109 | -45.27835 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1067bc45-e47e-3cba-98eb-38d0f2be89da | -5.70855 | -41.67366 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 03f32d6f-0e9d-39ad-a13c-c76cedb5c335 | -11.78475 | -43.53313 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| e6979f4e-d63c-3f10-ba9b-ea784e89d2f3 | -6.66711 | -45.35823 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 0dfa072a-ff28-3fde-a306-2c1c98d7b496 | -9.18406 | -46.70645 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 203b5d60-3a73-3981-a92d-84a271b8d882 | -8.40232 | -38.85189 | 2026-10-08 16:37:00 | NOAA-20 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7f7cdc41-787f-34fb-8fcd-04df2a9d296c | -11.30015 | -44.8316 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| de7add15-6d2c-3234-9f1b-496f0e97982e | -11.84119 | -47.33168 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 8b314521-62ec-3068-9201-6436a4241864 | -10.28531 | -53.96931 | 2026-10-08 16:37:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cc0ddaba-86ed-3fe9-9d56-0f63dcac36a6 | -7.68894 | -44.74532 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 18d12ead-8da1-3485-83e7-ed3f57625968 | -9.03142 | -44.37997 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 390aaf02-2652-3419-a667-eb31382cca7a | -9.92053 | -44.79776 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |


[Clique aqui para ver as próximas entradas](README335.md)
