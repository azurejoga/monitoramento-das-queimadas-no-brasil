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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f91491cc-ca2c-3fd2-859f-404c55f2a08d | -8.46333 | -47.23455 | 2025-10-06 12:00:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 3581bec8-8e20-3909-98ec-293dcc7c81fd | -14.68784 | -48.39991 | 2025-10-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ac12eeb0-b3d6-3a79-b2dd-0983b94ae37b | -13.36437 | -47.2348 | 2025-10-06 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 230767f3-e982-362d-bcf2-634d90cdcd7d | -17.18423 | -42.36796 | 2025-10-06 12:00:00 | TERRA_M-T | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 56c5f924-3a20-36f4-830d-dc999a77f7ec | -9.66972 | -45.65777 | 2025-10-06 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0e691fbc-0265-370b-ae51-fe22f5585bc5 | -12.37976 | -47.17346 | 2025-10-06 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 8b35668a-6a45-3da7-ab19-27d0f975720b | -15.13776 | -43.99238 | 2025-10-06 12:00:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9d786fb-29f5-3e72-9092-f7a0b7dbed76 | -15.66625 | -43.64476 | 2025-10-06 12:00:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4eb078f5-8571-3a58-9e8f-8e3363a34d9c | -15.23305 | -49.29753 | 2025-10-06 12:00:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |
| ee23f93f-8699-39f0-b5a2-22f88126e062 | -13.36241 | -47.24719 | 2025-10-06 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0b188c0c-1d66-3709-8477-aee5b403c056 | -10.55896 | -43.07027 | 2025-10-06 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| e5902d5f-b07c-3cdd-9074-d6379458b887 | -12.70428 | -45.85256 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 959cea6d-0552-3bf2-8427-96c67a5f43e1 | -13.38132 | -47.57555 | 2025-10-06 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a89cdca9-fd16-380a-afd4-5c65d64ec2c6 | -9.42154 | -40.27312 | 2025-10-06 12:00:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 921da33a-9fab-3d12-9c77-85ac9cfef7ba | -13.10057 | -48.00821 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ab5c77e8-c9ce-3e6d-a899-9ec848154abc | -10.56025 | -43.06135 | 2025-10-06 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 49e6d41b-d081-3ed8-9d18-164365a3d091 | -13.78229 | -45.73163 | 2025-10-06 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f04e8737-6846-38e6-83c2-e9a180e66cf8 | -10.71994 | -46.63919 | 2025-10-06 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 86013e50-bafd-38d1-99fb-36e3b8088f4c | -7.25645 | -44.13478 | 2025-10-06 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c680a589-501d-32c0-94a1-d17502f3fc51 | -13.10555 | -48.00039 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 4f68c8d4-1128-3178-9e74-5f09cf18cd91 | -10.16558 | -45.42654 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 02a67cff-4650-3251-9d42-9e1e81ca46c8 | -13.26654 | -47.84842 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4232f1d3-d498-3f59-a9d4-a772ff567281 | -11.94093 | -46.43182 | 2025-10-06 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 5f8d0dc6-0fa6-3245-af2f-cba462e42826 | -14.54222 | -46.98427 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 356c061d-4d7c-3d61-b06e-546c0717c7da | -9.37696 | -45.90702 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b30e7a71-a9b8-33f8-aeeb-640c232f978b | -8.19674 | -44.20651 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 5c1d98c0-bbd8-3e80-af31-7f935b031694 | -14.70319 | -48.37335 | 2025-10-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 368aa46c-e0b7-3afc-ad08-3a0a09dc8b91 | -7.53777 | -43.85857 | 2025-10-06 12:00:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f5d6fa2a-b6ad-3517-86f1-17e0b296d8d3 | -7.66278 | -45.44353 | 2025-10-06 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4c2b5d2a-9b62-342c-9e74-7c5a670d7e98 | -8.62839 | -46.30896 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 2d008670-032f-3810-a68a-ea5ca6bd00f6 | -13.08626 | -47.82128 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c90f0510-b05b-3a24-a65d-d5934a7d292f | -9.6681 | -45.66856 | 2025-10-06 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c8bf4cef-b606-37ce-99dc-d5c74323a68b | -7.7996 | -44.14352 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d1a0c686-d6de-37d5-bbff-69993c77f0f0 | -13.24106 | -47.8037 | 2025-10-06 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 2eb0474f-04db-3b92-a490-8cb50b5c1a11 | -8.17134 | -44.25159 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b1e6b59c-51d5-3030-b7ca-1658553422ae | -8.6219 | -46.2827 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f89fed5f-4ba3-351a-9d23-d0dfe9a1e43b | -9.37499 | -45.91191 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| ec1d114c-95cf-3339-810f-a170d8acf779 | -14.62779 | -48.13103 | 2025-10-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c52ce978-a61b-3003-9406-9ca6a2addb81 | -14.92739 | -46.81715 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 05038593-6be5-3cac-8845-7727c0dcc553 | -12.98121 | -46.8012 | 2025-10-06 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 4df4c548-e914-360d-9f00-96bccbc16e7f | -8.20096 | -44.17796 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 99018629-2de4-3553-8c28-dcd77f62513b | -17.29711 | -43.90404 | 2025-10-06 12:00:00 | TERRA_M-T | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7a0b9e39-d6f1-395b-be9e-18b4006f9712 | -14.26413 | -45.84827 | 2025-10-06 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3a038a69-0752-3f97-b78e-a6666df90af5 | -8.87697 | -46.70229 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 593292cc-7637-3b80-a2c9-0263f313d3fb | -11.5776 | -47.44348 | 2025-10-06 12:00:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9d1bb4d3-c09b-3d66-9b6b-710bbcda832b | -10.16403 | -45.43693 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 094db886-bee0-38ea-a52c-52d41bc03a7f | -10.42935 | -50.35411 | 2025-10-06 12:00:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| cc185791-e089-31b8-9c62-a752b9289196 | -11.52783 | -47.68667 | 2025-10-06 12:00:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c8a7d222-0c72-327a-9fdb-3e65746e4834 | -13.02854 | -42.15354 | 2025-10-06 12:00:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 82bc24a2-8e37-3c9e-abe1-b777f7111772 | -14.56363 | -46.97608 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| b1725abe-f648-34a5-90e0-34ddf15cd163 | -11.91353 | -46.22073 | 2025-10-06 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| deaf6e45-1308-38d6-a887-7008cd67ff71 | -16.28725 | -48.27992 | 2025-10-06 12:00:00 | TERRA_M-T | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 16e8f0e3-2262-353e-b942-c544990dbe23 | -14.53417 | -46.97123 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| dd813a15-9e30-3ab2-8331-edafc6b9288e | -15.20816 | -46.38154 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 947bdb02-22c6-31b6-b39a-a2dab1b2e6dc | -12.71037 | -45.84911 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 99080ea8-08d0-3e36-93c3-d3a08ff564a2 | -8.6116 | -46.28136 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ef629b91-1edb-37eb-9392-3d1f7df8d24e | -11.6634 | -47.03365 | 2025-10-06 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2596d3b5-30cf-3e4e-ab44-e3681b0099ec | -15.76198 | -46.25531 | 2025-10-06 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9e546c52-890c-35a4-b2f8-2a9737441b56 | -11.01071 | -50.68611 | 2025-10-06 12:00:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 0c9717a5-b51d-3ba6-bd2d-71084150f4e2 | -14.32383 | -52.96545 | 2025-10-06 12:00:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4bc97c4a-2428-3c2d-a62c-80f5a5088591 | -9.49522 | -46.00114 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 394c3601-c785-359d-b13e-d960e3f510a4 | -15.35391 | -47.30842 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 42355d89-a9cc-35d5-b914-c1eb47e6a037 | -9.40189 | -46.27908 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9dbdb05d-b3ef-3f60-83d4-04af504e4a1a | -11.91021 | -46.22502 | 2025-10-06 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5665772a-a9be-3802-9048-ac10dd464d24 | -8.63865 | -46.31067 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| afbc6b70-9a1c-3c74-9b3e-ef33fa739997 | -17.27286 | -46.92382 | 2025-10-06 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cf6d5bc0-db47-3f61-9444-119d9bf232c1 | -15.41987 | -41.69661 | 2025-10-06 12:00:00 | TERRA_M-T | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 8275ef27-862a-38fe-b540-d7056a673de5 | -15.35203 | -47.32011 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 176.0 |
| f747200c-5e8e-3020-8463-b2d16a34860c | -8.51538 | -46.37457 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 47d72010-c3bd-3e26-a055-ab7e881ec721 | -15.87992 | -46.25583 | 2025-10-06 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d109a7fe-bb37-3668-862c-6a4926875f1c | -15.77441 | -43.27081 | 2025-10-06 12:00:00 | TERRA_M-T | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3e513c63-be4f-3f99-9fc2-fb6351e86c20 | -14.27039 | -45.86977 | 2025-10-06 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 17730781-5e23-3760-93e8-a139970bd874 | -8.10734 | -44.8071 | 2025-10-06 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d1da52b7-e4d2-3abe-b509-f1439b258fed | -16.04326 | -50.94961 | 2025-10-06 12:00:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 43a5b0f4-2498-38f7-9f04-f25269f9c30a | -7.71414 | -42.39368 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 87aae6cc-bef2-34a9-aa07-014a3282f30c | -10.7218 | -46.62705 | 2025-10-06 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 928bb449-9eb2-3aeb-953a-ebd38df81ac1 | -10.61908 | -46.36109 | 2025-10-06 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fe6a621c-2945-3e5d-b2f9-c60e0cc3f7b7 | -12.3817 | -47.16099 | 2025-10-06 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 8ed63b5f-2cf3-326a-9960-c50c0c3773a3 | -12.4895 | -45.5461 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 4642f05c-357d-3cec-89b6-4d02ddebd775 | -14.55733 | -46.9517 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4b873402-0c5a-30fc-8a58-d0df72e1f401 | -11.80454 | -45.08132 | 2025-10-06 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5c53d503-e0f8-305b-862b-5f8e641eef55 | -8.63027 | -46.29671 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 08878b2b-455f-31dd-bdd4-9af1314ae6ae | -8.15788 | -44.279 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c06a6287-029a-3345-bdb3-12709e39ac26 | -11.84658 | -44.91665 | 2025-10-06 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d00386f9-d503-3f31-93a6-64a2ab7fe678 | -14.54399 | -46.97285 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 2c2f9b03-ce84-3211-9795-2cf1223f1b59 | -8.49935 | -44.65375 | 2025-10-06 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 057a10e3-3baf-3815-887c-1c2a10a40870 | -17.27457 | -46.91294 | 2025-10-06 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ed69454a-bc51-3e81-939b-83d3f4283a31 | -10.35851 | -48.14748 | 2025-10-06 12:00:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a421c068-7c2a-30c0-b9f9-2b495d44a87c | -17.24875 | -48.10614 | 2025-10-06 12:00:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fe4cc313-9a5c-3837-bc50-c942a4fa026f | -8.16992 | -44.26115 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| df438c1f-bbb4-36db-bd18-6d39e3fca53f | -10.36971 | -48.1511 | 2025-10-06 12:00:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3eb06ceb-2cd5-384f-a1be-c8e8e4c5f9ea | -9.74563 | -47.7254 | 2025-10-06 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 81502afd-25c8-3d19-9617-c9e98e74554c | -11.00624 | -50.66675 | 2025-10-06 12:00:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| ff951de1-0388-3573-b524-eb0854409616 | -13.12991 | -42.08665 | 2025-10-06 12:00:00 | TERRA_M-T | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 16ca3d65-c183-3992-acb8-45f53eb31719 | -8.87808 | -46.80168 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| b186da84-da48-3c38-a03d-205ac36de1d9 | -13.32648 | -48.05032 | 2025-10-06 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 29.7 |
| e821a6ce-916e-3a90-bebf-cd887cf8b317 | -9.37526 | -45.91795 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e5293c8d-c3c7-3027-b4d2-1ab84153b0fb | -10.3432 | -47.01033 | 2025-10-06 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c1b88686-153b-3d3d-bbfc-4a5f41a0627b | -11.06442 | -47.76898 | 2025-10-06 12:00:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| af150ede-34ae-3a59-8770-f27f7564237f | -13.77771 | -45.76173 | 2025-10-06 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README82.md)
