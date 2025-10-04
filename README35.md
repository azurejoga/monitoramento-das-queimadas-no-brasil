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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 212add1d-6fb7-3d01-b78c-692e92d6116d | -14.88739 | -48.35917 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c68d4f7f-e9f2-303b-9816-902e7c83b5e8 | -13.11943 | -47.93935 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a2e312e3-f477-3eea-80e6-442a80a9b89c | -16.04401 | -50.93642 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f77c202-cae2-34c7-8e0a-34b595657497 | -13.34045 | -47.19898 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1393dff-059b-3880-a287-e90f65664995 | -13.97465 | -48.12256 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 364ef3f4-bfda-38fe-893b-b2254776d860 | -13.22058 | -47.82175 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41d4488e-36d0-3190-a584-069e6ea65f2d | -15.72731 | -46.26679 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f5404fb-ebcc-38f8-9721-ed82816dc2d0 | -12.07074 | -45.19416 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d62039d-14dd-3577-94ed-f552d0b56740 | -13.32701 | -47.1861 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 909bf857-f8cb-366a-a0a5-d8aad083c286 | -15.37461 | -47.95248 | 2025-10-04 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81451b4a-8ec7-398f-8d9a-a11b61d1f9d5 | -12.42114 | -44.08118 | 2025-10-04 03:53:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e9a0cc5-79f5-3878-bed1-d91b05b739b4 | -15.59695 | -52.49475 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| efee5d98-b945-3ab6-9038-33d66dd8a076 | -12.64133 | -46.98923 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa6dbcde-73ef-3113-9add-a2ee02ce9c71 | -15.32561 | -46.37991 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 312b3436-69db-39f8-a195-7a2f1b27138c | -13.11034 | -47.87216 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 777cfeab-431b-3c9a-8238-3b0f7ffbb1f9 | -16.01504 | -50.95077 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 690dfb2a-fd81-3e98-858c-0eb7b9f5fc6e | -17.1511 | -47.02713 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58eb2333-365f-3839-ae9c-9b78da1753a3 | -14.19931 | -46.65796 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fd82c26-6e90-3fc2-84b5-d583b90adecf | -11.24853 | -47.79126 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b45274a7-561a-31aa-a2f9-f8c474f992e6 | -11.84077 | -44.93386 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9d09713-677a-3368-aecc-a5d9a2b24511 | -14.44835 | -46.10895 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5760a2e3-f4a7-375c-bf19-3fc3de5bfde2 | -13.17991 | -50.93362 | 2025-10-04 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdff279e-c3d4-320a-828a-2c123c133126 | -15.2617 | -44.12099 | 2025-10-04 03:53:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2f8cc4a9-ac45-37cc-9027-e7bde0f3dfb5 | -13.32525 | -47.79362 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ebec39e-c879-3daa-8777-9a35e4cfff88 | -16.01313 | -50.93013 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 509d417b-4afe-33bf-a7bc-6af1ad32bc40 | -15.35766 | -47.95608 | 2025-10-04 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4ea9379-f98f-333e-9d89-670c26f9d51e | -15.78242 | -42.04459 | 2025-10-04 03:53:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 968caea7-e2d6-35e4-80f9-cfa799085013 | -13.75398 | -48.06179 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b78390e8-87e0-3fc6-9b4a-e8a2b3d58647 | -15.59828 | -52.48888 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1a759f24-42cf-3ba0-8431-f613c9012755 | -13.12009 | -47.8512 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34ea8e34-80b9-38bf-b70d-9134e4cd4163 | -16.35456 | -47.07069 | 2025-10-04 03:53:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0242b43a-5ec5-3ce9-8ee8-cbc31d1608e2 | -17.0854 | -46.23705 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a3f92bc4-d20c-327b-8bd3-c573f7ca1174 | -13.69962 | -47.34928 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 365546a3-87db-3e29-9f24-5fc2ff73863a | -16.01178 | -50.94679 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb7847d2-220a-3044-8ba3-8e99e09c0634 | -14.72762 | -48.07867 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3385bfe8-e195-3a7f-a954-f058dedb2bcc | -14.94641 | -46.86518 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 355a9e08-eec9-322f-aaa5-a4b0c78a6e44 | -14.91898 | -46.87582 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ba83d7c-9582-3315-aa7e-238f03b5908b | -13.99403 | -48.19511 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e10ea1d5-c6ae-30c1-a08d-99a01df55d1e | -14.67867 | -48.26749 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30ca2aac-577c-3cc2-803e-e02fc66818ed | -13.14507 | -47.80952 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd782f2a-7909-3d49-bb7a-d192eed2f222 | -16.35752 | -51.47076 | 2025-10-04 03:53:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 07adca93-ca3a-36fe-952c-3fae379e191d | -15.53673 | -46.82186 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b5fb331-2e45-3c3c-af30-c77b9daab7ca | -13.30075 | -47.81923 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66062eff-d4f4-3bda-a91a-21a075886066 | -12.08656 | -45.15551 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9dd08e8-02f5-3199-9945-f094f51f7b37 | -15.62122 | -46.94326 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0765b95c-037e-341b-b6f0-9b7b6802024f | -11.79113 | -46.83556 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16cca8f2-596f-3c3c-8965-deecc4ec2d35 | -13.74684 | -48.09774 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41d6b1d9-1420-3b96-b047-5d0dbef31e1d | -11.91637 | -46.37247 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d95d874f-81d8-31bb-af7b-f728e0466f0b | -14.57456 | -52.48389 | 2025-10-04 03:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c1d40b0-c5e4-3af5-9360-ccbcc2842254 | -14.24335 | -46.09915 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 0e0b7ac8-3d97-38fe-a26b-e24321d270d9 | -11.91132 | -46.37186 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a006e7a-fad3-3ae8-b8e1-7609d28302b6 | -13.98599 | -48.12184 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12b0b6fe-ce10-3807-816b-1674902581f2 | -13.10056 | -47.88478 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10f33059-b4af-38cb-9c1b-eab37fc603bc | -13.11648 | -47.86938 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e3a3d5f-f90e-3e3a-8082-bce6fcf32040 | -13.33641 | -50.9533 | 2025-10-04 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5967500b-67e5-35e9-ae78-9e9850ef98b0 | -12.08036 | -45.18841 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72b186e7-7c87-3821-b255-b8fab95f435e | -13.2117 | -47.81979 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25ba3a08-caaa-3c5a-a294-77642b350754 | -13.21517 | -47.82097 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4035ecb0-42c5-34b3-b533-9220d6a9d386 | -16.34976 | -47.06964 | 2025-10-04 03:53:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 34e71173-bd8b-305a-92f3-4d2e1ff5fb3e | -14.92521 | -46.86996 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e46c2ada-fe18-3ed4-8c4d-ebc719784a9b | -14.72983 | -42.29624 | 2025-10-04 03:53:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2d8fb961-47c3-3d11-b173-243c7a9f1f01 | -13.13437 | -47.83547 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 604dca9e-9630-34be-a5de-9ab98b513c3f | -13.32942 | -47.19507 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f0d9d7c-653a-37b6-9fd5-229b935afa90 | -13.47925 | -47.23397 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dbda521-21e3-324c-ba36-6b90acf8be0d | -12.08795 | -45.17781 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 317469c8-cf1e-3a01-98d6-9c609e2d61e7 | -15.19085 | -46.39254 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84f5f009-d9c5-3911-ab29-5b74c0b24889 | -13.11373 | -47.85513 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 84e7999f-2f85-311e-b658-abe7a3b32287 | -17.08362 | -46.24648 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 882a18c2-060f-3d97-85a2-248eb6a9373d | -11.49693 | -46.76366 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f79360d7-ebf2-3c7a-8136-03a18b104a0a | -13.21786 | -47.84468 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 031b5c2a-d126-3ceb-82d9-b01e734f84b6 | -13.20613 | -47.81021 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1aaff934-737a-309d-b092-472a6e2e77f1 | -15.25697 | -44.1239 | 2025-10-04 03:53:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| feb3cebe-48e0-38b7-a42d-208df6d35928 | -12.88746 | -47.16607 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58682e00-75d9-3982-8cda-70d1667a1004 | -13.77963 | -47.82095 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| deca6fbc-2668-34f2-b318-fe11f45f8925 | -11.54748 | -47.67718 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36cd7463-9309-3ef5-aa1a-5712b2b9d2cf | -11.91263 | -46.73706 | 2025-10-04 03:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91b6d52f-685a-34f8-9c6f-582ae7a5752f | -13.29178 | -47.83684 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c0bb4bb-e4b0-3230-a002-206c8a4be2e8 | -16.02346 | -50.94184 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c88c9e09-3e56-3583-98d2-352817814ead | -13.27441 | -48.15979 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd7adc78-665b-3a25-9215-2e4bc056387c | -13.34521 | -47.22898 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 580a6e06-554a-36df-a2a1-b3dfac27ae86 | -12.10637 | -43.4492 | 2025-10-04 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc8ac1bc-3af9-3aec-908d-7256065c7f53 | -13.99416 | -48.19852 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf56c52c-db25-30a1-b07b-9ede21df1c1b | -15.83533 | -42.62264 | 2025-10-04 03:53:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a99f536c-438e-3e54-8259-613c0933b213 | -14.69828 | -48.19765 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff09fd88-c4ec-303b-a214-218fa33d9290 | -14.692 | -48.09129 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0844e4b-010e-33d5-a65b-3984d5ccf440 | -13.32013 | -47.24775 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb3cac47-d7fa-3176-88e8-08c0d23fb7ad | -14.23855 | -46.09879 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 6071a4b9-47d6-3322-bcce-9360ac660de4 | -13.58274 | -48.17955 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 737ae89a-2304-3429-998b-3cd976ee8cfa | -12.71741 | -48.57129 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d0d31b1-561a-3692-bbec-4788b837d6b1 | -13.31444 | -48.12979 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d70458da-35af-3467-9251-4e0d4b2a0bb1 | -13.5756 | -48.18695 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e138c7ab-c16e-3ef8-9170-0f64819b34b2 | -17.63723 | -44.45109 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b64b6008-a8e8-3d1c-a897-8d5e69526b6c | -13.74131 | -47.92965 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b49567f9-61a1-305f-b0af-59011fde6dcb | -14.75267 | -48.14718 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6358344-777d-3ea2-be23-f7ea8437d721 | -13.12994 | -47.8297 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3cbb84b5-8646-3158-8d94-d182e845945c | -13.08241 | -48.12626 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d05c45ad-13a3-3e49-b9e4-a46fa71f2188 | -13.74198 | -47.92626 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b07f3c3-8885-3d92-8cd7-20630de3ba8b | -13.11144 | -47.92298 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75d0620e-ec66-34ae-8367-6323614fec1e | -12.65523 | -46.97236 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14885fc5-26cf-3f57-9024-59326a8b5a0b | -13.99947 | -48.20009 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README36.md)
