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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99d8964d-2dc6-355d-bada-6e608d3d3a95 | -4.43205 | -55.74937 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ce73175-ee15-32d6-b2d7-37d5e96fb697 | -3.85099 | -55.80302 | 2026-10-03 05:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be1bac04-90c8-3529-812b-3fd90eb174ba | -4.26183 | -50.75029 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f065513-f69e-3b91-9dec-611217bae306 | -4.29348 | -50.78749 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c85778a0-e3e3-3e09-b54f-c75ced3f08eb | -4.6852 | -55.7968 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6671fd39-2b37-311f-a64b-16a83a8b156a | -6.85444 | -59.26511 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52c3655a-922c-3dc8-a8b7-0e58688c1e6a | -6.85997 | -59.25303 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4625daef-c614-38c1-bfd1-d810a5908c05 | -4.42925 | -54.85138 | 2026-10-03 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5050c7ff-548c-3dc9-8d17-c3517f2452fd | -6.0181 | -53.54749 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e869f1c-f1bd-3601-8e11-4652b5e1378e | -6.02062 | -53.53916 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bd84c50-3597-3cbe-bd80-606985993ed1 | -6.20399 | -60.01659 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe5b44b4-34d2-309b-8905-1c6e97eb3ad2 | -3.7622 | -55.53529 | 2026-10-03 05:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8afad814-e934-3c79-932e-d854f3de7344 | -6.00964 | -53.53305 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 699dd097-3755-3650-a11e-1260c7a1d601 | -6.84705 | -59.28944 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f06dfc8a-d690-3aff-ad95-7da7a9d33afd | -4.42769 | -55.74883 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 123b5c7e-0645-3445-bbdc-507ca7af4260 | -4.28742 | -50.78662 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97df3472-61c7-351a-9363-e70f35fabdfc | -3.0829 | -59.18828 | 2026-10-03 05:36:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b696618c-79ab-35fd-906d-d25c7086be17 | -6.20224 | -60.02794 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccef807b-083d-3818-8678-74588e3bce50 | -6.06988 | -59.88297 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f890fa46-d1ef-32f5-a678-8eaae02ad34f | -6.23638 | -53.14783 | 2026-10-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64b78326-b2b0-35ac-a38f-c9758a3538f5 | -6.04837 | -59.93081 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b2eddf1-576d-3eb8-bfec-2242738522eb | -3.91665 | -54.4283 | 2026-10-03 05:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44a010f5-dbdb-3376-9d66-f62729c68f46 | -5.09582 | -56.25323 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b17b0b0-ab73-3724-8a2e-84136d1a5c5a | -3.24728 | -54.51633 | 2026-10-03 05:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f122a7be-796d-33d7-96f6-4e74303cbc9d | -5.89436 | -55.49128 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d630277-46b8-33b2-b606-b92d2fcad642 | -6.15468 | -57.73326 | 2026-10-03 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 317a3b81-e5a2-303f-a3fa-1a99b86d9a70 | -5.85346 | -53.46775 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f73b3d0-d923-3d03-9388-936f4a6db964 | -4.26918 | -50.74854 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05733c19-3659-3724-a903-07d7531dba4e | -6.85805 | -59.26566 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2cc48fb-59a8-357d-b99e-daa97c153227 | -6.92019 | -59.27784 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ad5e447-9726-34bc-b35f-43bb280f3aca | -6.00404 | -53.5352 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 204f734a-3c9b-3576-8629-f016da22cf53 | -4.79353 | -55.76554 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8be9442-7229-37b3-bc28-5026961373dd | -5.25213 | -55.92019 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 315a8c95-9071-32bf-83bf-017f1e4daf88 | -6.01429 | -53.53745 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3db5270-ebd4-3665-b1db-fab6d697880a | -5.37531 | -56.05796 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58311ad9-a6a0-32de-a3a4-a4734d34c8cf | -4.40827 | -49.97526 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3718bee-677e-3cd7-b252-84250fde1e6d | -5.09101 | -56.25653 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8074d24e-e839-3604-a109-fa4be391843c | -4.41047 | -49.9718 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9346cea6-df9f-3463-983f-b1d98ae67952 | -4.11833 | -55.01791 | 2026-10-03 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89dbd03b-92b3-3b29-a1ad-70575f54bf10 | -6.21034 | -60.02142 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e0389fb-3931-391b-9aae-982e8a160167 | -4.26438 | -50.73857 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b6f43f9-b22d-3bc6-b1c1-64ee8e014ea6 | -3.85036 | -55.80706 | 2026-10-03 05:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caa66244-bec0-3d09-802b-721fd94b45cc | -4.28889 | -50.78439 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a7b097b-e4b7-349d-b6c2-24b121118ce5 | -5.25592 | -55.92465 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc41b663-048c-3eb2-8933-4e25ffd4d32d | -4.78851 | -55.70963 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 469a9e42-b6d2-3002-bf9c-542cab7bedd6 | -4.26321 | -50.74096 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0784a05c-34b6-3475-acae-c8c2f1132520 | -4.79538 | -55.72345 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 407a4d5b-d96f-3ade-95f7-0c6b62d94168 | -4.68583 | -55.79266 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 295b5851-e203-3f31-a329-949963e64849 | -6.19878 | -60.0274 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0798cc91-2cc7-37de-b90a-d5ec460593d7 | -4.26792 | -50.75103 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 787fec1d-0413-31f0-8ff6-e8f0c83d749f | -4.42833 | -54.85283 | 2026-10-03 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec2ba6b0-602c-3c83-b11a-5d4e58b619e3 | -3.58759 | -54.52891 | 2026-10-03 05:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0947aff9-2a8a-32c1-b1a0-a13825612a82 | -6.20687 | -60.02091 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 445990f8-085d-3cc7-ae00-231bc40ba7d6 | -6.2144 | -60.01814 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74794dae-acd5-3b65-97b4-45c2cdf210c1 | -6.01459 | -53.54452 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4991d59-0276-3fca-acc7-bdad1115b5fb | -5.09949 | -56.25776 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 257286e7-38c7-3607-b417-37e0dd8f8dea | -6.84642 | -59.29361 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bdc5f69e-d046-3cc1-92e9-07e2efc0aaf9 | -5.85176 | -53.47967 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 736e1ecb-0772-38ed-b03d-b489c0b81d7b | -4.29495 | -50.78529 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f06094c6-0716-33ca-93c7-2e634d19a6e2 | -5.99936 | -53.53099 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d4e8dfd-73f7-3c1d-b09b-21155d23c3cf | -6.85002 | -59.29416 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1d8ffe0f-7093-3433-9a12-66a601c95ffa | -4.78788 | -55.71383 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 209d7ec7-24e0-33a3-a38d-746f6c70a4ff | -3.84963 | -55.80219 | 2026-10-03 05:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ceab3ab-0292-3fc1-884d-e23350c33b3d | -6.21668 | -60.02626 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 890cd577-2ea9-3333-aeec-9447792c4c9c | -6.0664 | -59.8824 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6841cfb0-59e0-3699-8cc4-c4c5c4b1ad88 | -6.20629 | -60.02469 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f166b36-d873-3e36-ac75-6212359cf456 | -5.88983 | -55.49068 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e5dd3f3a-60ce-3e21-b0a2-4b0c5154c58c | -4.42273 | -55.75237 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5be394d4-b3eb-32e0-b01e-f53568032339 | -3.67799 | -60.53916 | 2026-10-03 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc038f0d-bc0e-3e1b-ba1d-825e426bfd01 | -6.85701 | -59.24821 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 268665a0-d593-3bd2-94a6-26f05254bd27 | -6.20858 | -60.03282 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2020ed28-8500-3a89-b904-484e480a6257 | -5.99982 | -53.52787 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2123307b-e771-3187-b4fc-49f6d9e93ab8 | -6.01338 | -53.54364 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7758918f-c849-3d28-a5c7-9742d5a9dae9 | -5.3747 | -56.06207 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cabcd2b9-8de9-3e8f-ad80-7bc60b180e63 | -3.64122 | -60.62746 | 2026-10-03 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45f56796-9290-3027-a8cd-e79fbe98d58d | -6.91297 | -59.27672 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b30c7191-ec19-33d4-b5e0-b9be0240441c | -4.70934 | -56.15173 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4ff0f29-ea93-3523-8038-89a891dbe98b | -6.91658 | -59.27728 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 633ffeab-1cdd-3eab-b3ea-1061e07c802f | -6.20746 | -60.01711 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6b912c2-df40-3e98-85c1-71962e7638f7 | -4.26242 | -50.75252 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 873fb2fb-04ca-3fd4-b8d8-021ab40d055d | -6.21093 | -60.01762 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 704f5158-c00c-3e7c-9250-3204a39a0c22 | -6.00496 | -53.5289 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c3820c5-696f-3ea5-8b86-0875a119817d | -4.26723 | -50.75571 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52825cb4-4b20-3f08-bbb9-64ba4787a791 | -5.85217 | -53.47684 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3f160d7-5c94-333c-a30f-d9e11f708188 | -6.91235 | -59.28087 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33f21676-7643-34d7-957d-2d806aa11f6c | -4.4048 | -49.96578 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b82e4b1a-5f14-31e6-9681-c862b7707315 | -6.19819 | -60.0312 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 937b3997-b102-308d-b96e-d2668bdc137f | -4.26374 | -50.7431 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ede40a78-924a-3b18-a475-8187033e644e | -3.67366 | -60.61078 | 2026-10-03 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 195159a3-6715-33a2-add1-33ba21ce2b28 | -5.96214 | -55.3481 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0756980-c337-3dc9-a9df-7e4bd22356a7 | -3.85038 | -55.97378 | 2026-10-03 05:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 825c7f23-3b68-39b0-9ab9-d6c0e65117da | -6.85219 | -59.96626 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e955111-2eac-358f-864f-96cbce1d16da | -3.84904 | -55.80623 | 2026-10-03 05:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7e5f946-6e47-3edd-9aeb-dc7a90728ef4 | -5.88916 | -55.49524 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf0f65e0-a170-3342-8241-b02f8c7f3a27 | -6.01502 | -53.54145 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f255feb-60a6-3d49-b048-56d36ce3edd1 | -3.67032 | -60.61026 | 2026-10-03 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e0ce0cb-6e47-3c58-bc4a-58119156e70c | -5.2565 | -55.92067 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d550236-dc5e-3c31-a0ac-3e49caa635eb | -6.019 | -53.5414 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc27d51f-7ae1-3faa-8ca7-61a97c30c866 | -6.04489 | -59.93027 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf10bc9c-aa24-3cbe-83cf-aea2115f530d | -6.01854 | -53.54448 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README45.md)
