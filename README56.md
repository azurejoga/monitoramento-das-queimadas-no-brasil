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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d73d9341-dd04-372e-ad6a-807ad31ac75d | -7.88308 | -61.79922 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f74aa06f-3b6d-320d-934b-23b2d689bb48 | -8.5824 | -54.72116 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 50e64f77-eb8d-3955-bd01-7378aa6dd4b3 | -8.20605 | -55.02389 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d997de89-bd50-30d1-82c0-37c7e9678688 | -9.4252 | -60.44531 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 643f8a69-8230-3c8a-8131-c8d98c73648d | -7.52894 | -60.68854 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9fab7b2-6314-37f1-aae3-eda6827c0801 | -10.14821 | -54.27791 | 2026-08-18 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7449fe60-806a-36a2-bba4-5a818eabaaf9 | -9.59922 | -60.50053 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecc65d88-a4d0-3e66-9ce3-6745acb43382 | -7.91186 | -61.73319 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 60691d75-656b-345c-9c1e-14784f1f1a76 | -8.57458 | -54.73405 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 38aa99ee-4a03-3e6e-8abe-a1881eae8e7c | -8.62739 | -54.70831 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c661f7d8-f24c-39d3-a679-b10165b45d46 | -7.55446 | -61.18059 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79fbd8af-209f-39ca-a6d0-00b89e3015bb | -7.55091 | -55.56296 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fcb1925-d449-3037-b2e7-956031f188ed | -8.21791 | -55.02558 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c01c3e3c-6e02-359e-a424-616804e7d1b0 | -12.944 | -56.64455 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ea4731b9-76f9-37dc-8f07-4f4e3e9e834b | -8.56965 | -54.72417 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 2b742a77-ec48-3f6c-914c-e0c9d2fec3d8 | -8.58422 | -54.707 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fca86af6-5b5b-39e6-af06-7faf1bd36b54 | -9.42938 | -60.44593 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fe843cc2-f6a7-3f19-9c5d-2b16bbcaa544 | -9.35066 | -63.56316 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17c993a2-2904-321f-9f84-a9d514b95e84 | -8.21848 | -55.02118 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cbddbedf-55a9-30f7-b0cf-4b0440289d7d | -8.55896 | -55.31276 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83d9fe65-5df8-3ea1-94c4-b60487415136 | -13.01969 | -56.58931 | 2026-08-18 05:44:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5f776a0-0d7f-3723-b9e0-aa43775ca92b | -9.01422 | -60.50713 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 023b9b9f-ef22-384e-bc56-a427490c2005 | -9.16861 | -59.70765 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36c1f466-0a35-3abe-a8b5-a3f229bacb65 | -12.23574 | -61.94958 | 2026-08-18 05:44:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f91ff122-9a54-3948-b4c8-4c046a99b628 | -13.42389 | -57.06514 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9809a40b-a347-3796-b012-487c5bd46686 | -8.58734 | -54.73091 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 517ba728-a9a7-3a08-8be5-6618c4ac1c45 | -8.58603 | -54.69278 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dfc3cbb5-d3e5-3077-80ac-71b1717669c3 | -8.72769 | -62.90584 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4970a7af-a127-3eab-b9b5-3dc9135008d4 | -8.583 | -54.71648 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| c1c3a30b-5905-3039-8f7e-fe05d7e3611d | -7.55557 | -55.57167 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d34346d-5b01-3912-aacf-ad198ddc1e3f | -9.45075 | -60.2934 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0a49dd7-76ab-3312-9e00-26d165e50da8 | -9.37691 | -62.35198 | 2026-08-18 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88432ac6-ff1a-3a20-b469-aaa256cfa424 | -6.91502 | -62.9065 | 2026-08-18 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a14bf71a-9a84-369e-a3f3-1776d4eda6d3 | -9.19145 | -60.80753 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 656fedf4-fe76-3f6f-9283-f4279c0844c5 | -8.90155 | -60.59818 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d728ec9-9965-3959-a2e3-163c5bba43fa | -8.58909 | -54.71724 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 8331fc6b-9027-311c-b2ab-8a4b1e6a09e4 | -7.55057 | -61.18003 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f57898-517d-3c55-9097-292929d6831f | -11.20349 | -54.81599 | 2026-08-18 05:44:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2765c273-e36d-3403-b19f-e3c36d4d41e5 | -8.89564 | -60.55158 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 092898c8-bde4-3cf7-aeee-b135d45c4092 | -7.56518 | -55.56564 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8dea12fd-f677-393a-b98f-c6f0437385f5 | -13.42899 | -57.06978 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fff5b8d-1bca-32dd-aa7a-ced0a6735831 | -11.22143 | -64.97666 | 2026-08-18 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d9b7144-bbf1-35ce-8a2a-82449c797bf5 | -9.18532 | -66.99755 | 2026-08-18 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd4b3847-94b2-3cdd-a0b9-2c3d1537b13e | -10.15025 | -54.27802 | 2026-08-18 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ae8b575-ebdc-3af9-b43e-342abe6aa87d | -12.94135 | -56.64483 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24f1a1ae-c0f9-3b42-af2f-cabcfa457be4 | -9.42587 | -60.40995 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e17cae7-6b50-3ef8-927f-86e750c8322b | -13.415 | -57.04457 | 2026-08-18 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc8eea43-016a-3e12-b2cb-426136942eac | -10.938 | -57.10839 | 2026-08-18 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 99e21acb-cf73-36b5-b0b1-8dd2c0e1b2a2 | -8.9592 | -60.56782 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c6fb8a2-304c-37dc-b833-8e929696df5d | -8.57574 | -54.7249 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 0fe0bc0e-002a-3675-9469-4ab2ff37b3d0 | -7.56229 | -55.5644 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c179f10c-335f-332f-820f-30e4e4fc9f30 | -9.08193 | -65.37655 | 2026-08-18 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0afba8fb-e337-3383-b526-3c8a8cb8fb68 | -8.95514 | -60.53658 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9a0d545-040f-3ac2-9681-f827574f59c1 | -8.5595 | -55.30849 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 067a3a34-b906-3286-8799-13861ebb7035 | -8.90101 | -60.60192 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3eda79a-31b6-3042-b792-66cfc770e6d6 | -6.9121 | -62.90203 | 2026-08-18 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b2ea243e-8248-3619-9912-80d438a3c84b | -9.83737 | -65.05984 | 2026-08-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd008c96-ad1b-3cab-89ab-e72219b36261 | -8.90263 | -60.5907 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66a0a233-0a1b-3ed4-80a1-7a7a48df8112 | -8.94944 | -60.54718 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fae3955e-021b-3236-82f2-b896f55cad79 | -7.88245 | -63.76044 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb983f28-3b49-39fc-9cab-d7e19bad7753 | -7.46239 | -59.99827 | 2026-08-18 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 242788b0-27fa-3ae1-81a3-24310b0decca | -7.90808 | -61.73264 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b99481d-8521-3e0f-905c-70a242d77865 | -8.63445 | -54.70784 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bb08025-c260-37fe-a3fa-7f2b92347208 | -8.18598 | -63.88561 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95c880ca-9cc9-3a4e-ab2c-5cd1e420e8a1 | -8.89923 | -60.5559 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89ecb1cb-9350-3abc-8791-618ea2aca854 | -8.55367 | -55.30747 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5b0f882-a687-3a0a-8e54-29c6723af39a | -7.61419 | -60.96033 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11199a40-d776-3f35-9466-9c44713e255b | -14.03147 | -53.68343 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9c53883c-c77f-318e-b5b9-f2f56b1d1e70 | -9.42574 | -60.44146 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6b6aa573-0710-3fc2-9b80-8634152a90f9 | -8.89511 | -60.55527 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21b9efa1-c84c-3d22-bcdf-f500f6012fda | -10.58207 | -63.54811 | 2026-08-18 05:44:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76939b02-a07e-3ec4-9638-6b880795e3e5 | -8.63502 | -54.70321 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1cedf87a-aa93-3dfd-a204-82286520ef1e | -11.36919 | -55.42066 | 2026-08-18 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8fb6aa3-4bb9-356c-bd96-92d5de2e9dac | -8.56595 | -54.70464 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9effaba0-a430-3688-b9ac-b5de53593b8e | -7.6253 | -60.96705 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 239203c3-1bf1-3dc7-aaac-3215d11488c0 | -12.46407 | -54.18057 | 2026-08-18 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0db3a66d-2dcd-37f6-9894-364651f97d13 | -8.8969 | -60.60132 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 781c469a-9fe8-361b-98db-d62266b16405 | -8.9541 | -60.54404 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9aae0d4-0473-3a2c-9497-860dcd05de7e | -7.85524 | -56.59639 | 2026-08-18 05:44:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 735578fb-833c-3a9e-858e-3fee8f57cf8a | -9.12526 | -61.60283 | 2026-08-18 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 87121446-ea7f-3756-864f-6e59f33b0841 | -9.59764 | -60.51207 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fd6f65d-defb-30f7-8c3e-c2e1bea76e4b | -6.9115 | -62.90597 | 2026-08-18 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1680a0e2-357d-3890-9392-22c15f886992 | -7.38538 | -59.99833 | 2026-08-18 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5676c4ca-f465-3c74-8a7f-01d14d49e813 | -8.22809 | -55.04011 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| b66590ed-f0b8-356a-9350-8bc145a5c8a4 | -8.55842 | -55.31702 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68b2277b-3e45-30fa-a181-c193d88ee957 | -8.72472 | -62.90118 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01a71733-8535-3b28-9e59-81de3eaaaadf | -6.91561 | -62.90256 | 2026-08-18 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9441a8a9-f29c-32c0-b718-36bc32c9c834 | -9.18392 | -56.98846 | 2026-08-18 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 105de074-e2f8-377f-8902-2f06fca969bb | -8.56712 | -54.69535 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b580c0cb-d293-360a-bf63-d853edcec8ec | -9.18706 | -59.67085 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3164946f-5337-31f6-9d95-db1794351b35 | -7.62135 | -60.9665 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fabaa634-f9ef-3535-b197-1da211afa8ce | -7.55376 | -61.18548 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54cda5a4-a3bb-385e-a23d-7797d9bf765d | -9.42628 | -60.43762 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ab654ec3-38ce-3d01-bc26-4e057b642ddd | -8.58609 | -54.74065 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 253c4d3c-4e15-3107-8621-676bb0c7f2a6 | -14.03769 | -53.69071 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5e4c254b-100e-30ae-855b-2f528a144ab2 | -13.41647 | -54.37608 | 2026-08-18 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4dbe1813-ced3-393a-b789-caf10ae261e7 | -8.20067 | -55.01876 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41b57d28-af6c-3193-97e0-f81b40e7439b | -7.6041 | -60.83327 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b7c8be07-863f-3860-88d2-767fb166db65 | -8.57942 | -54.74449 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| a0e3233b-d736-370d-8a5b-c021fb27cd2b | -8.63344 | -54.70938 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README57.md)
