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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 857637d8-51fd-3f9f-ba11-d5c93976b007 | -21.3869 | -45.49721 | 2025-08-26 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b93ccc08-d9b6-31fe-ae7c-66e8c7db3079 | -20.366 | -50.69764 | 2025-08-26 04:00:00 | NOAA-21 | SÃO FRANCISCO | SÃO PAULO | Brasil | 3549003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b20c4487-da09-36b8-af24-30a97baa2a0b | -21.47747 | -43.583 | 2025-08-26 04:00:00 | NOAA-21 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 40430641-a4d5-36f5-a831-645b03662804 | -20.73072 | -49.38197 | 2025-08-26 04:00:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 228172be-3c66-325b-a8b5-f7ced55806ed | -21.3877 | -45.49275 | 2025-08-26 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| b1c1d5ef-725b-3946-90a6-b4295acce7a7 | -21.28944 | -43.33706 | 2025-08-26 04:00:00 | NOAA-21 | ARACITABA | MINAS GERAIS | Brasil | 3103306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| eeecec3d-b3cd-35c4-bab3-7057b7022793 | -22.89594 | -49.05944 | 2025-08-26 04:00:00 | NOAA-21 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ccc890b-fb81-37fc-8322-222df047f522 | -21.03954 | -48.62506 | 2025-08-26 04:00:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 62698465-e63f-3f75-8363-9be7f4c4fb72 | -21.29007 | -43.33323 | 2025-08-26 04:00:00 | NOAA-21 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b918e30c-945d-377f-a3b8-a923301866cb | -20.36502 | -50.69856 | 2025-08-26 04:00:00 | NOAA-21 | SÃO FRANCISCO | SÃO PAULO | Brasil | 3549003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 62ba9859-a907-35ab-addb-3f60875d201a | -21.54333 | -41.22808 | 2025-08-26 04:00:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3422d160-fd99-30c9-b2e1-8fa12df66c73 | -21.46928 | -42.75074 | 2025-08-26 04:00:00 | NOAA-21 | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 63e79820-dfaf-32f3-8695-81f7fae61238 | -20.38943 | -46.71889 | 2025-08-26 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eca32c10-cbd6-35b4-bbf4-741cd07a9ab4 | -21.72479 | -46.80895 | 2025-08-26 04:00:00 | NOAA-21 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8d8be344-ec52-3bfc-af76-b6a91e930036 | -22.47491 | -48.9971 | 2025-08-26 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6179241-8860-3047-a38f-9413c5d11eff | -22.90115 | -49.05592 | 2025-08-26 04:00:00 | NOAA-21 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9f852f55-2671-305b-a5c2-2e21ce77b9e1 | -22.27061 | -46.45239 | 2025-08-26 04:00:00 | NOAA-21 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 211e0a62-15c7-33a1-9dfe-1182aa7ae629 | -21.12583 | -45.88053 | 2025-08-26 04:00:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0729eee8-28b2-317d-8819-0f4a547af70a | -21.60731 | -49.70298 | 2025-08-26 04:00:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| eb404deb-0c08-3757-b230-557cfd2d745d | -22.25259 | -42.51192 | 2025-08-26 04:00:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c3646207-c4de-35b3-9691-e61dc9e58575 | -22.89162 | -49.05858 | 2025-08-26 04:00:00 | NOAA-21 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e6e4f8c-302d-3dc2-9949-a987c2555f58 | -21.72092 | -46.80831 | 2025-08-26 04:00:00 | NOAA-21 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| b0431b34-6f9f-349e-802f-a03d013cad27 | -20.88144 | -49.03326 | 2025-08-26 04:00:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 9bab1105-8ad8-3915-a8ff-c77b21fc9186 | -21.03865 | -48.62955 | 2025-08-26 04:00:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5229f485-f6f5-3df5-af24-82a0452239ec | -6.8044 | -58.9568 | 2025-08-26 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| db3c9339-ef68-30fc-b6a3-a40d67304505 | -8.9873 | -65.4379 | 2025-08-26 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 8cfe27b5-5446-31c2-b61f-6bead93c491d | -8.855 | -62.4313 | 2025-08-26 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 110.5 |
| a84c1862-da53-3b90-b25d-1f473392b0be | -11.521 | -52.1209 | 2025-08-26 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 022c1a96-183d-3739-9ae3-c33d593ca1e6 | -11.1587 | -44.7627 | 2025-08-26 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 4498a7c3-1ac4-3fc6-b414-803f3b3fade0 | -8.8363 | -62.451 | 2025-08-26 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 5b191c3e-fd59-3071-871d-65ba93ef06d6 | -4.9605 | -55.8226 | 2025-08-26 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 26231755-9d65-381a-8834-6a03c4182661 | -6.2459 | -60.0174 | 2025-08-26 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| f9f58cf5-f181-3445-b782-4597d0eba256 | -6.2275 | -60.018 | 2025-08-26 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2b0f79d2-c8ae-33d9-88c7-7279346f83c1 | -11.1591 | -44.7395 | 2025-08-26 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f688bec3-1237-3bb7-bf18-e85a55e7c8d0 | -9.023 | -65.7355 | 2025-08-26 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 68280a64-2ce9-3523-9048-52ebb32e84a5 | -11.5207 | -52.142 | 2025-08-26 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9cc17e66-35a1-3b41-867b-07b407a42c69 | -6.8043 | -58.9761 | 2025-08-26 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| aa52fa60-ec16-394a-9236-994deb280eb2 | -11.559 | -52.117 | 2025-08-26 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 3c41bd7d-b907-302d-9825-3fc267528ae0 | -9.0415 | -65.7349 | 2025-08-26 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 413dfdc5-ddc6-372c-91a9-930c2bbffcb0 | -8.9874 | -65.4192 | 2025-08-26 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 390ea89d-1aef-323b-bbb8-cf00a4f3ec57 | -11.2937 | -55.1129 | 2025-08-26 04:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c4d97e6e-a9ac-3803-9c3c-4d99e0110786 | -8.8548 | -62.4503 | 2025-08-26 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 170.7 |
| 687c2074-a8a2-3076-a68d-0a28f83122da | -7.3854 | -64.3662 | 2025-08-26 04:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ef2c71d5-5e86-3aa2-8448-8ab3b6f693d6 | -6.8228 | -58.9753 | 2025-08-26 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.6 |
| a14cb0e7-3535-3ba3-9bab-d39fc4d3adba | -8.8734 | -62.4495 | 2025-08-26 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7b62d62f-9b22-3e13-9784-b74c2053c123 | -6.8229 | -58.956 | 2025-08-26 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| f3110cc2-168d-3a43-8a9d-9baa05f6bf41 | -11.54 | -52.119 | 2025-08-26 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 26378967-f316-3d4d-9e0a-0b43808ada1f | -11.5017 | -52.1439 | 2025-08-26 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c2106143-442e-3734-96b7-fcda99132b09 | -9.1724 | -59.4436 | 2025-08-26 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ec406527-93d9-3f75-8914-7cda6e7c4e70 | -11.502 | -52.1229 | 2025-08-26 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| ec99ff6f-e37e-3cde-84ba-6f9697f0530e | -9.006 | -65.4 | 2025-08-26 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| d60fb2ac-d04e-3513-9a14-30292de8bbc2 | -8.8364 | -62.4321 | 2025-08-26 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 32471467-0063-3573-9288-890c486e0436 | -7.3854 | -64.3475 | 2025-08-26 04:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 0b3d71db-d48e-3470-b9d0-1de25507eb5d | -9.1722 | -59.4629 | 2025-08-26 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 221b3510-f0ea-364c-a63d-024846d2fde8 | -3.49826 | -43.31269 | 2025-08-26 04:19:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d5046e0-e464-3a93-b166-e24d97c8f64b | -2.25405 | -47.85706 | 2025-08-26 04:19:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06f9a5eb-9bba-3673-ab35-3b2c7ed12d53 | -2.28882 | -47.88697 | 2025-08-26 04:19:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a05956e-9319-3038-b493-c68fe0486f66 | -3.06493 | -40.04904 | 2025-08-26 04:19:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a1f07d37-0a28-3e40-b73d-1eb28872221a | -3.79869 | -41.77214 | 2025-08-26 04:19:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 97280911-f0e2-3bea-b754-dc8f8a4215d8 | -2.48672 | -47.75404 | 2025-08-26 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54d31734-ab08-36ee-9478-f559581d7b0d | -2.26562 | -47.85885 | 2025-08-26 04:19:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d638ac9-98be-3f80-a3d1-065ed305bac9 | -3.06562 | -40.04457 | 2025-08-26 04:19:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 11d86347-c7a0-3ae9-8fdd-d1e7a7c9c24b | -2.51629 | -47.71572 | 2025-08-26 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 156591cf-74e3-3442-b40c-95bfd4890c16 | -2.29268 | -47.8876 | 2025-08-26 04:19:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9231b095-9099-396c-93b1-dab0fcb1d6a9 | -2.4715 | -47.77554 | 2025-08-26 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ee4daa2-686a-37e7-be83-8dfb58f7ce44 | -2.26252 | -47.85351 | 2025-08-26 04:19:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0b0e06c-aa01-33b4-b944-f810974cde6b | -2.26637 | -47.85415 | 2025-08-26 04:19:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78f0f4a4-3e6c-3ba4-9c47-9df5ac518295 | -2.29372 | -47.89008 | 2025-08-26 04:19:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9f0ed03-b976-3368-ba30-30ed611e97db | -3.35153 | -43.361 | 2025-08-26 04:19:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faf1d694-1ece-30c6-9f3c-fad3ea412282 | -3.35486 | -43.36152 | 2025-08-26 04:19:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dee58ca2-7c8d-33b5-ab45-eeef9c58e4cb | -3.34766 | -43.36395 | 2025-08-26 04:19:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97eaa92c-3376-3451-bd7a-1937123d457e | -2.64626 | -48.05669 | 2025-08-26 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 636f4744-463d-3f96-80ac-a77fefe94fcc | -2.44667 | -47.33109 | 2025-08-26 04:19:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac0eee0a-6f2d-316a-9170-af52a78c8cd7 | -2.65014 | -48.0573 | 2025-08-26 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62770830-2b7c-3f3c-9830-9610010e9d49 | -3.36313 | -44.19125 | 2025-08-26 04:19:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c084434f-f6eb-3640-9e14-a1573db7795c | -3.34682 | -43.26799 | 2025-08-26 04:19:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd3625af-b3e3-3f62-9e46-e80fd567c6cf | -2.88516 | -48.28967 | 2025-08-26 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64efd894-52b2-317c-9b14-7de8538d7260 | -3.36368 | -44.18779 | 2025-08-26 04:19:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af30ab41-dbfa-3d67-8a71-e4d577d0ec2e | -3.34737 | -43.26451 | 2025-08-26 04:19:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a0448d6-0a88-3523-977c-c13b771e76ca | -2.88452 | -48.29152 | 2025-08-26 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44d686a0-ef8b-3a40-897d-eb46059d87f2 | -11.5017 | -52.1439 | 2025-08-26 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d5b63519-aeed-39fe-92b4-ce6b1079a18e | -11.559 | -52.117 | 2025-08-26 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 00023d44-08f4-3954-85a0-d13b6f461f90 | -6.7635 | -59.6718 | 2025-08-26 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| ac623771-8bda-319f-92b2-2dd13e5ba144 | -9.1718 | -59.5211 | 2025-08-26 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9ea7b15d-edf3-3260-bb12-f662e65e7970 | -9.1722 | -59.4629 | 2025-08-26 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| bfa8f584-11a2-330f-8db6-9d6e155042a4 | -11.5207 | -52.142 | 2025-08-26 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 34f1b0be-8cf8-3084-8d7d-4252a8c24a50 | -11.1587 | -44.7627 | 2025-08-26 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 22c134fc-2b8b-398e-8813-c7acdfac8e78 | -11.1396 | -44.7654 | 2025-08-26 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 179ed2da-2f0d-3640-ac68-d34728ab87a4 | -11.3126 | -55.1112 | 2025-08-26 04:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6003c972-0ba1-3d1f-a6bc-b3b253757515 | -6.8413 | -58.9552 | 2025-08-26 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 3747cec2-94e1-341a-82ff-1bc533847bd0 | -6.246 | -59.9982 | 2025-08-26 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| faf0ba87-2eae-39ce-98f8-e522e78f27b1 | -8.8363 | -62.451 | 2025-08-26 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.5 |
| fbd4b675-e8a2-3ee3-b62f-62365618dec0 | -9.1724 | -59.4436 | 2025-08-26 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 15601fed-e958-30b3-a818-f5779d854dc4 | -11.54 | -52.119 | 2025-08-26 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8efdacfc-68f9-31a2-b1f8-b595c3c4a40a | -7.3854 | -64.3475 | 2025-08-26 04:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 3dc7e0c5-62ef-3b12-a34a-9dd0247a7f1b | -4.9605 | -55.8226 | 2025-08-26 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| d3299b61-ed43-3fbd-b4b0-1e3b1cd7ddf7 | -9.1529 | -59.5609 | 2025-08-26 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| df7b22b1-9aa7-3d8c-9ea3-c4e33a6d2fc5 | -8.8364 | -62.4321 | 2025-08-26 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 102.4 |
| da740e37-9903-3d49-b058-fb749f91bfe0 | -9.153 | -59.5415 | 2025-08-26 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 20aa3468-6302-35b5-a1f9-ddab4b9b2ab3 | -6.8044 | -58.9568 | 2025-08-26 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |


[Clique aqui para ver as próximas entradas](README35.md)
