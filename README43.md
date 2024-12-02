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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69853a18-3ee1-3e8b-bf86-53a61cabad75 | -3.48861 | -52.10313 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 376f7ba6-27c2-3415-8ab9-42f844e89b79 | -6.07799 | -48.04749 | 2024-12-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40226527-742e-33a1-9394-2364d3963d79 | -4.07124 | -49.06472 | 2024-12-02 04:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7eec97db-ba87-3a20-b8ef-733adea81223 | -3.82574 | -46.6002 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aa85ff6-c9ea-3b2c-beea-828e41070a6a | -2.97885 | -53.87986 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3274c982-62cd-381c-8bb6-444dc0c1229f | -3.89687 | -46.68402 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60c8703b-596f-3b51-9e03-570782b777f0 | -3.43676 | -54.60957 | 2024-12-02 04:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4652228b-2f20-3463-bbb4-0ab565137f96 | -8.20705 | -40.9111 | 2024-12-02 04:25:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 095a766f-a29a-3dc8-9b4e-f63f361ab925 | -11.06411 | -45.37446 | 2024-12-02 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeec7a3b-fc56-36cb-9e5c-4b54b700245b | -3.98067 | -46.74061 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57b81fbb-8a1f-3e67-ac26-9922fc47fc95 | -5.11899 | -43.20859 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a538f18c-9fd6-301e-be34-0c507a7fae6a | -3.89521 | -46.67289 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 496ed7c1-6b2a-3a92-ba7e-3aca7f469417 | -3.27163 | -50.20695 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1d9541d-12f6-3392-acd7-2d0c7a7f8d5c | -3.18223 | -54.33498 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81301bff-1fef-3199-b609-29c50c7c1d82 | -3.25043 | -53.92968 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 359a17cf-a410-3277-9538-ef5a2d41a19f | -3.96725 | -46.73851 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04189524-7044-361f-8139-4ac094e25cbe | -6.74651 | -48.77296 | 2024-12-02 04:25:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7647cc0-f210-3045-8c81-41714b0514f3 | -3.75315 | -54.51167 | 2024-12-02 04:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1892c2e4-cafe-31ac-af0e-67d00cd5c3d6 | -4.27212 | -50.85081 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c9e31bb-d983-348a-b49f-47aa59cc86ed | -3.77782 | -46.69754 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a8deb1e-5fd0-3fd5-b8c3-c6ff311e63ac | -2.7986 | -51.90482 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fad2cc27-81ba-309e-9464-55fac2b2962e | -7.87791 | -35.13833 | 2024-12-02 04:25:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f4154f8a-05a6-35e7-8c4c-a434b2f0c60b | -3.02917 | -51.5358 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be7b55df-0396-3193-bc42-50c355471935 | -3.18171 | -54.33818 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19d85fcc-eab6-37d6-b3d2-32d2678d88ec | -3.82964 | -46.59724 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d458b788-ea5a-39d0-b11c-67d307d5877d | -3.7778 | -52.03346 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ed754e38-e79b-3cc5-8494-42d091798f42 | -3.18115 | -54.3362 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4061f3b-9912-3e69-bfc8-13ae598539b3 | -3.80332 | -46.53576 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55740f76-e1fc-3b6b-ac23-3d91d2d8b68f | -3.33667 | -51.52839 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f282d31-0e08-3dfd-b1bd-04d5251db44a | -3.93808 | -46.92302 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24abea2a-98f3-3ed9-a90b-732653489489 | -4.63206 | -45.45815 | 2024-12-02 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a9b5796c-f2a5-3a2a-828a-ac0f385ec097 | -3.86078 | -50.89847 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6454d226-2083-31e1-b7a1-e99f116ce572 | -3.75262 | -54.51488 | 2024-12-02 04:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18b5c3a4-abea-35b9-b48b-77b796221730 | -4.17134 | -46.55772 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7f5c8fe-3252-35cf-b834-1ca32465d8b3 | -4.11327 | -48.47921 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bc67331-c1b8-3bab-877c-f2ddbf2e8e48 | -3.26354 | -53.6451 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6cc56b4a-9b61-3376-8c9a-78c5055218cd | -3.69785 | -47.11693 | 2024-12-02 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b444c528-f9de-351b-be27-45fd804bd377 | -4.44934 | -46.12695 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98c886fb-a1ff-309e-a771-3e1e16ce81ec | -3.4972 | -53.83483 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d151e0f-1f64-3a68-adeb-e9df46c48376 | -4.75186 | -43.71883 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22cd6e1c-f22f-3413-930a-0c6a340b05f8 | -3.69106 | -47.11588 | 2024-12-02 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d127e428-1866-3a6f-b909-d66eae3eda45 | -2.81554 | -53.06759 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6adb313c-7892-3c57-be48-89eb1f774376 | -4.0403 | -46.82943 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e600712b-5b7f-3968-ac25-9cacc15f18f5 | -4.27777 | -50.68856 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0115ca69-f6c8-3bdc-8783-2f4098b69876 | -5.0213 | -44.79066 | 2024-12-02 04:25:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc34b111-38dd-3458-a3ff-d8474bec9815 | -3.89352 | -46.68348 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 156a6a7b-7efb-3f72-8b67-cec053de07f2 | -4.10741 | -48.8887 | 2024-12-02 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d59b815e-805b-3fd9-9fc7-aa6fc6c5d893 | -4.20339 | -50.68655 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42b57075-c51f-35d3-aa1f-3f9c0280f353 | -2.38832 | -53.71277 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d95d86c3-16a4-3fd6-b8d3-ab20b17839be | -3.06728 | -53.69018 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9739862e-8e23-3f87-9424-dbed59017bae | -4.74742 | -41.10728 | 2024-12-02 04:25:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 927b7cca-22ff-3af2-a74c-e85ea8e3f9a7 | -3.40523 | -50.22604 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb81cb5b-10fb-3aeb-8e68-1b1d88aa2b9f | -3.05865 | -51.71263 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaaad5ee-1d60-354c-b7e6-a5565f0efe4a | -3.54212 | -51.49768 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eff3e024-f4e5-344b-825e-77b27a50e3c5 | -3.94428 | -46.8838 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60348495-74e3-3135-80b7-15e5be6e025f | -3.95724 | -48.82408 | 2024-12-02 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e2b9a3d-13a9-38b6-9495-32ece6fd4d13 | -4.24938 | -49.19315 | 2024-12-02 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4cf1a5e-b74a-34b7-99d9-eea0fef8f777 | -3.89913 | -46.64831 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8561d861-1745-3842-bf55-b76c36bed3f6 | -6.07738 | -48.05122 | 2024-12-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fec637e5-7b10-392b-9b0d-c8647053a7bf | -3.46242 | -50.263 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2d38248-f193-3d8f-8789-93d30fa18835 | -3.24902 | -53.92426 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dc4ccc1-05cc-3ddb-b27d-42720e30d701 | -3.97005 | -46.74258 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e35dc8cd-1355-3737-906c-92cb0ecacbf5 | -4.14727 | -48.221 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bf3aa24-9fa0-3d62-91c9-5bbc3ff873d6 | -2.56111 | -53.40388 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| facaa5da-3734-3507-aa36-dba0e2e56796 | -3.53096 | -53.51058 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8ad2698-3580-3b6e-ad74-3f7c1cfbe542 | -4.06994 | -47.08629 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 971f5fbd-9432-3b54-a3a3-b373ae7da969 | -4.02785 | -49.94225 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b195e1b6-4616-39e8-929f-65893cd019dd | -2.90075 | -51.58059 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 09e760dd-a27c-3b2b-9f97-107411793f86 | -4.59548 | -50.83014 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ebde51e-f90c-31fc-9e61-484f1518a9b7 | -5.61076 | -43.47721 | 2024-12-02 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d9ce30a-c197-3860-8ada-267b04d847d5 | -3.26228 | -53.62156 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2b070f31-6bfb-35a2-83b7-6588953da64a | -3.87649 | -46.58294 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2fd2a44-2203-3965-b228-5125508b88d1 | -4.32055 | -48.0886 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b5ee331-e298-3e28-98d0-ae13c9456d93 | -3.42621 | -49.995 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 378e60e2-504b-3151-bb8f-6081606971b8 | -9.99203 | -44.74358 | 2024-12-02 04:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03360e1e-ae17-3860-a9e3-8bc2e3b37d44 | -4.50353 | -45.86983 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f95874c8-eb7e-3f16-9e09-1e0de1c7d404 | -3.32844 | -52.22227 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 481f6660-d464-3212-bdbc-81532ecd2fbd | -3.0967 | -54.13501 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 207ea0bf-369c-3de8-989e-f8210526affe | -3.03284 | -51.54063 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 09bc5b72-5837-38d6-9cd4-8bc9fa2488f8 | -3.94943 | -47.05286 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df347830-3124-3ba0-b327-2e6c874015a2 | -3.25589 | -49.90972 | 2024-12-02 04:25:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbe5a029-15e7-3b0c-899b-9e1e8566108e | -3.92925 | -46.718 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 666d91fd-ddfe-32c3-a6bc-67a2659ff6fd | -4.58141 | -43.35314 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 315dea02-6f9c-30ac-b4d6-672d3a18a6e2 | -4.6693 | -46.87364 | 2024-12-02 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a430fd1-439d-3720-9b13-dca54736df2a | -3.78602 | -46.6986 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a49321cc-a521-3747-89e5-570d3a3f3d25 | -3.07231 | -53.80553 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28df0d62-eae6-3d9e-9f95-73c4e124e66b | -2.74601 | -51.75246 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb794a30-82ec-38ae-8728-2dfb1398348d | -3.5012 | -53.84187 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eb32699-5e20-395f-ae2c-8f3ccf0814a3 | -4.05542 | -46.82093 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a0e257e-7f8f-33a9-8a57-67180891030d | -4.44386 | -45.3645 | 2024-12-02 04:25:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02dd69a2-e08e-3b44-b9cf-a8b5e0ec26c2 | -3.15365 | -50.6255 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fde4561e-3278-3c9c-8e1e-9b035b706e34 | -3.62019 | -52.49609 | 2024-12-02 04:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 948232e8-1acb-3d69-9946-b607d958fd60 | -4.15016 | -48.22547 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2732f20e-47f8-3d00-8fc9-8bb40bcbe440 | -3.85585 | -46.54012 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa48bbca-54cb-30d6-876a-887144754df4 | -2.30973 | -53.90208 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c32895c-bad7-30ff-9cb6-6fd46337f529 | -6.46762 | -44.19264 | 2024-12-02 04:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2befd9f9-a9fa-35c4-8ffc-40cc24cb22bc | -3.86245 | -52.39243 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9beac76b-8698-39d1-9406-5b40feb7ebbb | -3.84582 | -46.51698 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bb8c35a-87c8-3789-90a7-d54b532ae785 | -4.00297 | -46.65362 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fa97ab0-056f-3ec3-8590-bfd25a7a0097 | -3.21325 | -54.17706 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README44.md)
