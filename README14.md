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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdc82d1f-fbf6-35d0-99da-d23b2b6e64d2 | -6.0891 | -57.9254 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c94ee2f-28b7-3931-85dd-ec6294133fef | -6.0972 | -57.915798 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8d745e-e006-3e35-895d-9684505e5b55 | -6.144 | -57.850498 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a076b7f8-01f7-36f2-9d48-9e57d08040d4 | -9.4005 | -60.560001 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98547358-d3bf-31fa-b787-dd91c86c3420 | -9.0918 | -50.792099 | 2026-08-19 01:23:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 268e1d32-a1f9-3f9c-b6a6-8bf0d899cd06 | -5.4298 | -48.411301 | 2026-08-19 01:23:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82407cd9-d1c5-3905-b923-695ca82633f2 | -15.2749 | -56.491501 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf4ca7dc-f659-3172-ac2f-be5a55ebfb76 | -6.749 | -59.177898 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4231249-02d8-303a-854c-3a5362115dbc | -8.5739 | -54.715698 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91182dcf-9a31-3237-a726-7a27c6e1f0f8 | -6.3508 | -54.9132 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99b4914b-a55b-389f-8335-0bca58b59b7c | -6.7906 | -59.450401 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c39f33e-b894-3356-9636-724a08804673 | -19.753901 | -57.9659 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9376c592-933a-3484-b69d-d53bf8069211 | -8.581 | -54.745399 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b736a5f-398b-35ea-acd2-b3b8697594d9 | -6.7401 | -59.049301 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e861f8a6-a9fd-30e5-8dfd-f934920cca6a | -6.3582 | -54.9006 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc7307e1-6750-390b-8c3b-9866c69bf7fc | -9.117 | -61.602501 | 2026-08-19 01:23:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3387cf2-bed8-3ac2-8801-829fe6bb6f32 | -8.5857 | -54.765099 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f5c1652-c46e-3e63-93c9-3c52c0a9dbfd | -29.149401 | -50.3923 | 2026-08-19 01:23:00 | METOP-C | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 322b53f3-5854-3a55-8655-8ca7d54a9033 | -15.2005 | -48.240299 | 2026-08-19 01:23:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a62baea5-d3a1-3928-94b0-3543ca466c73 | -6.0177 | -57.840199 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b4a8e88-c19d-3d64-a57c-76c1676f2b62 | -6.4095 | -54.943001 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57313b44-507a-30e6-80da-dae2f8316462 | 0.3039 | -60.445099 | 2026-08-19 01:23:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c9132e59-189e-395e-a2b2-e0f09272d085 | -3.1065 | -61.200001 | 2026-08-19 01:23:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e2a7739-7329-33f8-8327-23660c32168e | -15.2799 | -56.513302 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f168adb1-1419-3c94-8242-fbd861ccaa95 | -19.765301 | -57.9711 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eacd203b-cffd-38f5-86cb-dbb637b421df | -6.6151 | -58.953701 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c70a96d3-679b-33e9-97d3-25702d3fa958 | -9.0867 | -50.812099 | 2026-08-19 01:23:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95bfc60e-db6b-3b1f-9bcf-c49864860faf | -9.0105 | -60.519001 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 947046c7-0309-304a-941e-d7332e01823b | -11.2392 | -55.059101 | 2026-08-19 01:23:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c1f0a91-33a4-3e70-9a91-36f63f9da17c | -9.4135 | -60.572201 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e326119-cec9-3c11-8968-bc89f1daa366 | -6.9556 | -59.044201 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0e4e7e2-950f-3ddb-9985-d6a712871b18 | -9.4322 | -60.425301 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83a0d49e-c6c5-306f-aaf6-87ab9ec1c46e | -8.5615 | -54.750099 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3024057b-667e-3ff1-8385-91a12a224749 | -8.5881 | -54.775002 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b0f7dcd-f377-3416-85d3-949d06955e7b | -6.9964 | -59.042198 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 74d6bb07-da27-367c-927c-9cb454120208 | -6.6167 | -58.960602 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee09e7bf-9769-324c-8a5f-373ec080fe93 | -15.8878 | -55.569801 | 2026-08-19 01:23:00 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 33a01065-222f-3499-a248-b6641be78333 | -6.998 | -59.049099 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89cc9e0b-b631-312d-b3d1-fb6127650448 | -6.0955 | -57.908401 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6c991f0-a809-3291-afca-51a2e184672a | -9.2846 | -56.886902 | 2026-08-19 01:23:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac36458f-c12a-3929-b24c-4d8ad316dc83 | -8.5639 | -54.759899 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 443da3f2-19d8-3de2-bdd9-1c835e45864a | -8.5759 | -54.767502 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9e6b4b-ac01-3f47-9684-0b8339f23c00 | -8.5789 | -54.693501 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6ecbfff-3808-3a99-a899-2aa90b406fdb | -8.1888 | -55.004601 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef3ad58-c8e9-32fb-b5a2-d6f980c149b8 | -8.5736 | -54.757599 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6b05cc6-8efe-324d-aa33-70a9b3c9596a | -19.7507 | -57.951 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 58934728-5f04-3c23-8256-f07ad7fab004 | -7.5402 | -55.575199 | 2026-08-19 01:23:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e6c6be-a136-388f-b710-92841389ffc9 | -6.042 | -57.811199 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08e464cc-fd37-36fd-ae55-95fb7dc4d08d | -8.5765 | -54.683498 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46e8d6cf-7357-34e7-a85b-b6c75a021082 | -15.2732 | -56.4842 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0736a07f-a30c-37ac-8a67-75c3693dc61f | -7.55 | -55.572899 | 2026-08-19 01:23:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f66e1895-046d-3c23-a2a0-abbc6174a97b | -8.5688 | -54.7379 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb0e1d5c-08ac-3ffc-a258-e767f6d5cbf7 | -11.2196 | -55.0639 | 2026-08-19 01:23:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1188ce8-1ff7-3749-b3e9-3683a002ce92 | -19.0769 | -57.354401 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fa3db550-8e42-304c-963d-e80bac892259 | -8.1911 | -55.014198 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca44aa5-7013-3214-9996-e36e1189516f | -15.2044 | -48.216801 | 2026-08-19 01:23:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be88040b-4904-3981-89e7-b965d11d2425 | -16.5854 | -51.622101 | 2026-08-19 01:23:00 | METOP-C | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eff405dd-c9b5-3464-913c-a49e578d314e | -12.0045 | -53.437599 | 2026-08-19 01:23:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa68087d-097d-3edd-af16-4a96a2ea0ce1 | -4.1257 | -60.7864 | 2026-08-19 01:23:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5344012d-2a92-3d6e-9578-8dad9162c9ef | -9.4158 | -60.443901 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ace2f18e-68ea-3ea5-8285-e03037a0189d | -8.5493 | -54.742599 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3774cd8c-fbe2-3185-9362-7367a7bbbf9c | -8.5955 | -54.762798 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d00b73c-6c7e-305a-b6dd-bf632e00c134 | -6.6009 | -59.117001 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e6c83cd-b541-3df2-ada7-5828def32040 | -16.575701 | -51.624699 | 2026-08-19 01:23:00 | METOP-C | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 27993f4a-ed54-356f-aa05-44698102136c | -9.3939 | -60.576599 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db090af9-58ca-3d77-858f-240e6adf11ed | -6.8869 | -59.0597 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29ce3dc5-76b2-310c-bbed-2a6575d9b6fd | -16.2638 | -57.672401 | 2026-08-19 01:23:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3d98645e-9866-3303-b6fa-a4f818c1ba92 | -11.2273 | -55.0527 | 2026-08-19 01:23:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 993eb9e4-60a9-31a4-921b-4c7e0979e674 | -6.1065 | -57.866901 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 060866f3-e51f-3410-8d65-bc7e1633b954 | -8.8976 | -60.566601 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79ac6e28-cae3-3e14-ac33-b3804ce9756c | -5.4394 | -48.408901 | 2026-08-19 01:23:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75490798-acb1-35b1-9cef-77b2046b14c6 | -7.9117 | -61.7304 | 2026-08-19 01:23:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd6c2c14-e887-3629-91d7-2c4b353788d3 | -19.055799 | -57.351799 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2ee22cc6-9804-3359-b0b3-2a68f89370f1 | -9.429 | -60.410999 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc075d5-b754-3683-a406-68e6091a270c | -6.7474 | -59.171001 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b1852fb-6728-3094-901a-cb59890b7497 | -9.2101 | -60.8144 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c7b53a1-a7ed-31bb-9709-40f9451b2423 | -21.5315 | -52.017399 | 2026-08-19 01:23:00 | METOP-C | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f997845-79eb-379d-8da8-6724be4c6911 | -7.1119 | -59.774502 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4c6f382-5b9d-3367-836a-4ae05c6fb96a | -29.1448 | -50.373001 | 2026-08-19 01:23:00 | METOP-C | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7677719-9bd8-3654-8517-d9c41b1df9d1 | -6.6967 | -58.949799 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44f594ab-cca2-3c9a-86ae-b4bf2b70ca93 | -8.5884 | -54.7332 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edcfcc57-8fd6-3d59-b981-a7d592a2da3d | -9.2231 | -60.826698 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0bef1e6-31a8-3eb3-948c-911408f0b4c7 | -6.1474 | -57.865299 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3d493b4-faa4-3eb4-978e-e0faafd64bcc | -9.4085 | -60.596001 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c7f08ec-5731-35f3-824b-bf57647e22cf | -6.1048 | -57.859501 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e267d05-fd62-3bf0-87b9-ad75f23ba539 | -7.4605 | -63.646702 | 2026-08-19 01:23:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45c72d92-c330-3398-8905-9548ff93c3e9 | -7.5424 | -55.584301 | 2026-08-19 01:23:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b14f1dc-b309-3aea-a25e-04da2607462e | -6.1491 | -57.8727 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44ec80ba-cb95-3ec8-882a-138e970a5172 | -8.8992 | -60.5737 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c694b75-aa24-38ad-ade3-2d37a99f1fe2 | -8.5298 | -54.7472 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7306529-dceb-3ec5-88fa-c7ad5353fbcf | -3.1014 | -61.222801 | 2026-08-19 01:23:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a8b0199-1091-3509-b8c5-ae2fd838ab48 | -9.3875 | -60.547901 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d4eb74c-922a-31b5-8b06-e36240586279 | -9.4069 | -60.588799 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4c6c5ac-e641-36cd-8dbd-83a03a590425 | -9.4021 | -60.5672 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b906368-c677-33fe-8650-6878b746d89b | -9.4208 | -60.4203 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02d1ff8b-b5db-39ed-b472-6f8bfd116d04 | -19.0574 | -57.3591 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7e093b04-977e-3715-b4f1-e9b3f5f68cea | -6.8499 | -58.987999 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7962a206-94bb-3d7d-a31c-98086a640aaa | -17.615499 | -54.867401 | 2026-08-19 01:23:00 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 200a50e3-cc7c-31fe-8da9-ff16648dcbd0 | -6.0219 | -50.195301 | 2026-08-19 01:23:00 | METOP-C | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1e6cb74-2a43-3f61-b6f0-b0b74f1dda51 | -6.446 | -52.744801 | 2026-08-19 01:23:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
