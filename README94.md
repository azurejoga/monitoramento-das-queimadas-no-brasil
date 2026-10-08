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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29e0cc41-54d7-3b44-8612-caf8b135bfb2 | -11.62949 | -43.70142 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f5510fa-4344-3f9e-b356-ae9db6e9a775 | -3.10554 | -54.18097 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dac74cab-fb77-317b-ac8a-516d789595d4 | -7.46466 | -42.85384 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c028e827-0c3a-3a70-87b3-1ff2a0e56ea1 | -5.69685 | -53.47279 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f43a48a7-53db-3bc0-803b-2157f09f6378 | -3.08647 | -54.30081 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ce31ee4-f5d7-39bb-82af-4c8367522d06 | -3.02958 | -54.0942 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05b9a862-cfa6-30a8-bffc-7908fb9865de | -7.3943 | -55.19973 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 928f715e-60ff-377b-8213-35ed7dc7add8 | -3.10483 | -54.18544 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2d35d566-7097-364a-b012-53c72ec1be31 | -3.20452 | -53.86811 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a30a29d-a610-3d3c-ace1-be6468b90344 | -5.83761 | -50.14046 | 2026-10-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8815b1aa-7740-3e27-b9d7-2b3bfbf90c4e | -11.22486 | -45.2476 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 186ae4f0-e2a0-306a-8043-2566c8e19c94 | -5.733 | -45.15824 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c5b8a324-68a6-3412-bbd6-9414c6166673 | -3.39865 | -60.83819 | 2026-10-08 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a890ca2-c094-3b52-87b9-8d4d29b7b050 | -4.07543 | -59.83933 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3980a5cd-301e-3d2a-8248-784d6f4bfbf3 | -7.88797 | -55.00578 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e099870-5854-34f3-a743-e2d2166f64a9 | -3.29151 | -54.00243 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aff71ff3-56aa-3868-ba23-f226ca2354b3 | -2.9342 | -54.08111 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af248fc4-8941-303c-a64c-eae9a63cf959 | -2.83117 | -54.13262 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8a50977-5e23-3e56-95d1-f7427f7d384c | -8.08779 | -55.31676 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e9c5ea7-53da-302d-9374-a6ef9455e315 | -3.97259 | -56.12062 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 131dee91-c267-3061-92e7-e82dcdefe538 | -3.28086 | -54.04482 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a293f2b9-31fc-34f2-8d3d-b1618cd6d268 | -7.44379 | -63.5453 | 2026-10-08 04:46:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9a8c1ff3-0d50-33ca-ae50-109444df9231 | -3.36214 | -58.18689 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20f305f7-51d4-3bce-8fd5-3b2ea9697538 | -4.30577 | -60.94435 | 2026-10-08 04:46:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db0bd4e8-9334-3a7a-a5f3-d1af0987f0fe | -3.96555 | -56.11192 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9471e34d-0648-3bb3-b201-7b1ce9af4f07 | -3.54685 | -50.10389 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e7a8d97-234e-3ecc-a1f9-771a35fbb8c0 | -4.30511 | -60.94828 | 2026-10-08 04:46:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0fa0d8f-bcc8-3161-b5f8-bebbc9ca4525 | -3.28122 | -54.06853 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f5aa437-7782-376a-aae9-e5cbff610a46 | -2.96216 | -54.16032 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d4e81fa-f665-3593-9e00-2792c39c916d | -3.26097 | -54.02991 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e9337c16-d94d-370e-b724-b03ca973a99f | -6.14711 | -47.93059 | 2026-10-08 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2b47ab23-adb3-309e-a590-c88df3649a09 | -3.20817 | -53.86864 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7410db8e-6a72-38f6-b6dd-c5ab80f46c34 | -11.22297 | -44.87156 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f904e1bf-0a10-3c7c-8787-0807b1d59edb | -6.6359 | -43.73135 | 2026-10-08 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 535bd971-0b9d-3449-93b0-b37b87a80d5a | -2.84486 | -54.07169 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0eedff2f-2ff3-303f-9849-5f3065e385fe | -2.47351 | -56.10053 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d813a31a-afbf-38b9-be4f-691d8a27b620 | -3.09027 | -53.94706 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ce6cbeb-ac80-33b9-940f-3cd41a328bda | -3.32431 | -50.17803 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a17aee52-3792-363c-9a64-51524e51df98 | -2.46943 | -56.072 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04a125f1-6814-3d2e-8135-b23e118ea7d1 | -3.13487 | -54.36707 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 564ace5b-b576-3cf9-bed8-2469139e6be2 | -6.2264 | -55.65987 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8a89b701-8a01-3f6f-9e3c-92ce7aa795cf | -5.99206 | -55.36179 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81631a17-1d88-3e39-80e0-ccedef690837 | -11.39299 | -46.69569 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f316536-c6ae-363f-ad03-01b41be6192f | -6.85055 | -41.76732 | 2026-10-08 04:46:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e7a0831e-d024-3040-bf70-1fb6ea268d08 | -2.99317 | -54.06169 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fb520caa-dd91-3843-979a-95b21242f168 | -5.25094 | -50.91685 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb8fb3b4-c18e-350f-a6df-f826497d35c0 | -5.71772 | -41.72777 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e79840a8-cee9-3fa7-9ded-a8656fedcdf8 | -3.16127 | -54.73547 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 40950684-fa2c-366a-b1c6-1730ddfee118 | -10.43279 | -47.27692 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81d55d9e-9496-3616-9f10-5e8d55871fd7 | -2.84518 | -57.48217 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d35af07-d6ef-3f45-b801-e97c838c8247 | -3.01759 | -54.07441 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 458cb63f-e002-3c54-b9cf-8af965253f47 | -3.04052 | -54.20699 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9e3a1d3-39a5-3c60-8a85-146dc7884bf8 | -6.23555 | -52.85267 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 23b5eb9b-664e-3069-8d3c-fa629dcdc436 | -3.69403 | -55.48824 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a3145ce-f092-3a45-ab5f-28a34d83fba5 | -3.30633 | -54.02681 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 46248a1e-aeef-3cc3-8fd2-5e02853b68c1 | -3.05251 | -54.22698 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d548b25f-b4fb-3685-a17c-6418e3b784ba | -3.59328 | -54.58099 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4d1e69fa-c851-3026-951e-eb0e2a35c870 | -6.4842 | -55.29777 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d04cc8c1-9cbe-3cfb-9180-ddbe6acc9ad3 | -3.31823 | -54.04624 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a13ca704-d3d3-32a8-85f4-83b80a6e130a | -2.88484 | -54.17728 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bb38388-4d6b-3404-913f-d0fcdd80b36c | -6.88477 | -43.70121 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 751d3d47-bf34-3b76-ae88-47bea1f57d59 | -6.46143 | -55.53001 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30a3a310-28b0-3718-8e25-9b546c2c94ad | -10.48075 | -47.22428 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d35f2e4-983a-3744-9374-08d90ed3c6eb | -3.70822 | -58.93925 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c360bc37-5c29-3842-9985-70fb1d470389 | -3.28296 | -54.03191 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85dd7e58-6706-313c-8277-8c506d262651 | -5.76137 | -42.06912 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ca0bfd80-2ef9-37bb-8cf7-62c15ac27d56 | -3.84371 | -55.98637 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2b53d11-fe93-3d81-baac-382f0891c8be | -5.68867 | -53.47933 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9df68d6a-e698-38b1-9297-6cced24a1218 | -3.13861 | -54.36767 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 949849ef-18ea-30b8-ab33-a1fba9fac2be | -7.1824 | -52.61644 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 07b73bd6-c0f7-3e0b-93e1-34988b5f3720 | -3.54445 | -54.64398 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20e4477a-3f1b-3e78-9f30-5e417194a93c | -8.71059 | -45.21178 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11792afb-02a7-39f3-8b7b-283f2c8ac697 | -6.52194 | -55.28029 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9226622c-4ff5-3880-af40-1ca0abe8995a | -3.08345 | -54.29577 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2b94ad6-498a-3168-b82d-124fcecdf8b7 | -7.86458 | -44.14903 | 2026-10-08 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79904a39-8c02-3eba-a684-d4c593359da8 | -3.9573 | -56.11057 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d239f174-aec6-30b6-a67c-37510b340b09 | -3.05837 | -54.21429 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 936ef3a8-9c3b-30af-bd83-f4fbf27b558c | -2.84671 | -54.13051 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e78ad4f4-88ab-38c0-8b11-69ee436ec4cc | -3.48556 | -54.62284 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d163bd6-deb3-321a-b746-d600ec07162d | -6.11251 | -51.7383 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78dcfc7a-083a-33da-99e1-e8d5c9342f60 | -7.18856 | -44.33167 | 2026-10-08 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73b40b93-03b8-37ac-9abb-8e77465f3ea4 | -3.40904 | -58.91265 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7c2d6804-0aee-3718-a908-27e9695eb6d4 | -3.22916 | -54.30393 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 021c4912-ace3-3cf2-8882-ea2ec787edf2 | -4.31327 | -48.62568 | 2026-10-08 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea2b9a5f-0b28-3c8d-8f08-70e9c26a0004 | -9.59697 | -47.78195 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec0c2ac1-a179-3c3a-92e2-bb0250bfc5cd | -3.26735 | -54.01325 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fe432a03-d672-3f7b-915a-96b5e721e95d | -3.25808 | -54.66177 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ba09c2b-17f4-307b-b42d-488a3e644603 | -2.72353 | -57.47277 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e0e5fe9c-d8fa-3796-9b69-2085f2e7758e | -2.72475 | -57.47042 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a3b734bd-56bb-3fc9-a161-3944e655deb1 | -5.08911 | -49.69989 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6129bd7-ce2f-349e-8f71-bb53e2798645 | -5.33664 | -45.27039 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b32e99fb-3b18-395c-892a-db62d11fb315 | -7.02638 | -45.29905 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e921bd99-ae0f-3f11-8482-67c115114c2f | -7.38768 | -55.21684 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3d9341c-c2c7-3a24-aa65-6f16098b48a0 | -5.99129 | -55.36653 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c523b108-d602-35ed-af3c-e0f650e5b393 | -10.42557 | -47.27052 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4bcf8a60-40a5-36e6-bad7-cdc33d27fe38 | -2.7721 | -54.08362 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17b6c22b-ebc5-308d-8bdf-7a4ecc787c99 | -3.05078 | -53.95981 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 280.2 |
| 52e20a3e-5e37-3ed8-9b91-b006bd650133 | -5.23965 | -48.39718 | 2026-10-08 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80428f5f-aa5e-393d-9b50-fddc9d27b72c | -9.14121 | -45.83371 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6af7b7d4-bf89-3b5e-b6f8-1fc763e6a368 | -3.3054 | -53.8663 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README95.md)
