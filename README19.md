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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f58a3b77-a378-34be-8fd4-712a7ef8d3f0 | -13.50887 | -47.00549 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e61ff978-4962-331a-8a36-1b29e4be37af | -11.67385 | -52.23276 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 6b3aa394-9d50-38ef-8ffb-815471b3fa6f | -11.10453 | -44.63153 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 3ae23c1b-e7f3-3968-a964-c73575d6fa24 | -13.89237 | -48.11074 | 2025-09-02 03:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bf269e8-f376-3242-91d0-f43b7e81e4e0 | -13.6885 | -46.93716 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7926fc84-dabe-3ad0-8bd2-5c6a7a8aeae1 | -13.2898 | -46.92798 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c92508f-4697-37d2-9962-78704646242a | -7.61093 | -46.03891 | 2025-09-02 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d646a0a-1aa1-363a-bae1-9db3117cb2a1 | -11.09459 | -44.63466 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| d663460c-6e6e-3d2d-9ebb-12c482b0803d | -12.756 | -44.41262 | 2025-09-02 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6456e3a3-1721-3eb1-9281-db6c92244043 | -11.66431 | -52.20734 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 2ee52d5e-b5a4-3c54-a377-c4b3cd3ccbff | -13.49806 | -46.92621 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb44a353-509e-31bb-8b2a-848189d1d7bd | -13.33859 | -46.85092 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46be40d0-ef3b-32b3-ab9f-7f6e04ef763f | -12.87453 | -48.05855 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa7bef8f-5a65-33e8-ae7e-05baed8f26c8 | -13.36978 | -46.93505 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 185ebaed-0220-37c5-82b9-d3fd230b52dc | -14.61303 | -48.03269 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c2a2aaf-e34f-377a-881e-81d620973118 | -11.75701 | -47.8315 | 2025-09-02 03:51:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43c27fbd-043c-3cfd-8ef8-4adc73694e08 | -7.99297 | -44.04422 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b82b52bb-8483-332c-b7da-5d180ddfffad | -13.89596 | -48.09252 | 2025-09-02 03:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0befc20-a511-30eb-a431-c84fd69dffbe | -12.61529 | -48.19071 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cdc541ed-ac00-3356-8838-1b0bd74f3c78 | -13.5271 | -46.99331 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0077fccf-d6f8-3193-88e5-765240e83afd | -10.04585 | -48.1167 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ddfe3134-869f-3d69-b00b-d6a2bd9d40ef | -14.26883 | -45.2575 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4dd06db2-877b-3ce3-89fd-03d742b254d0 | -11.65678 | -52.19831 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 51e5904f-4840-3028-9306-786dd8b38ede | -11.09629 | -44.62516 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 2c146fac-7b39-3347-8a52-cf099fb23b21 | -13.72032 | -46.93517 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d91fca86-e5bd-3c47-a73f-86019ca0dccc | -10.83845 | -47.44935 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 27d4abd4-2225-3def-8376-f6a094c7e485 | -11.97162 | -45.87545 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6756b746-83a1-39fe-afc5-30da9b5671dc | -14.73958 | -46.74796 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c91dfae-b98c-3f12-9a01-d62a64d8fcdb | -11.90368 | -46.67192 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e560526-0540-37b7-a6d7-eea0168fa3f8 | -8.88136 | -45.74163 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0399e8e1-b0e9-37bc-b8dd-2c68efa742e0 | -14.04121 | -44.61049 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae20c84b-f04f-31f7-9db9-62d279c29119 | -13.28922 | -46.93102 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c5d13af-ecd2-35ea-9c61-072d5df5c79e | -13.30482 | -46.83572 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29b73ae4-e1fc-3fed-9444-afea4d388799 | -11.92373 | -46.45317 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ae270e1-49c3-33f4-a51a-fd0ced96d4bf | -11.89549 | -44.88388 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bf5302b-5387-35f3-9775-a7a062f1ea5d | -11.53944 | -44.84859 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eed729e9-fbe0-3bcd-b797-9f21b42214d4 | -7.57315 | -45.22897 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93e361f2-700f-3420-8540-c52afc5b5c93 | -12.56665 | -44.78703 | 2025-09-02 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b613f2f4-4a5c-3109-b978-c5d331aab93a | -11.86238 | -46.72136 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffde028c-c4ba-3278-855c-9a6a263d31db | -11.10285 | -44.64101 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 911a3bbb-fba4-3ac7-a446-04108a0d2d80 | -7.97734 | -46.45891 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dbca1e21-5d35-3946-8a55-c1a8cfae27ac | -11.01203 | -46.82837 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e97096a7-001d-352c-9bdc-bdf5a52fbb51 | -8.88062 | -47.97187 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dd30b05-aab6-3473-b6fb-bafb806e0c34 | -8.12788 | -45.03233 | 2025-09-02 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9316db3e-37d5-3ab4-ac19-82a84cd3763b | -8.71043 | -50.43811 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1010e46b-1e8c-33a2-89da-7ef58bb18ec2 | -11.9737 | -45.86455 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94b43fcc-bf87-3932-8308-f24d9ec8be71 | -14.21375 | -48.06352 | 2025-09-02 03:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 044131a5-3e06-30ed-9ef7-f4d953af40d2 | -7.49601 | -45.35151 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e4c8fd6-5a06-3e13-89a3-e187c20c6ba8 | -12.98817 | -48.11711 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40b5694b-5ddb-339a-a19c-9d3d41fe2e3b | -11.97266 | -45.87 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7877eff6-eba6-39dd-80f1-c28118aa63da | -12.93495 | -48.10122 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86ae1610-f4ff-3796-86c7-eb8f0cf85440 | -11.66827 | -52.22376 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 809a56d0-44ea-3124-9224-01ed9db27416 | -12.33898 | -45.67744 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e04e63d2-b1b6-3a4f-83ea-8df968413305 | -11.92637 | -50.61332 | 2025-09-02 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34e57b87-1a19-3e4d-9f1d-c52cf5e12701 | -10.26244 | -47.52634 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a930c096-d388-355d-9184-ab0852253bbe | -11.08835 | -44.64329 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96767221-2da2-3149-a40e-52944bc2bee5 | -11.87702 | -46.72863 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a967f07-0bc8-3329-aa09-1e72a5b2a86b | -9.29134 | -47.0989 | 2025-09-02 03:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bd9d304-4b34-3053-b301-2f1635c12e12 | -11.97077 | -45.86867 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89af0d7a-0a6d-36eb-b657-7e401c0bb05f | -14.59958 | -48.07185 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93a5938e-512e-3fee-87b0-0a998991ab50 | -11.96227 | -45.84546 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 738f07f3-3226-328a-8fbe-49b7c8567952 | -15.78813 | -42.13197 | 2025-09-02 03:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a6638085-5498-3af8-aed5-eefa77c5ee50 | -14.72225 | -46.74971 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb64e80b-e7bb-3a3e-bbd8-046fa0d958c1 | -11.09375 | -44.6394 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 3b9dc832-db33-37b1-9ddb-6c51ffa5672c | -13.52649 | -46.99644 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4233ae18-d788-38bd-8992-2a686969df8f | -13.6981 | -46.88686 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 92e6afbd-f112-3d94-b749-a8d3ecc48678 | -7.87018 | -47.96948 | 2025-09-02 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb5d9d18-f95d-344c-bd53-ba969762ed17 | -12.98894 | -48.11324 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67d75713-6fde-3364-8568-32462201c9ba | -7.48319 | -47.87928 | 2025-09-02 03:51:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d8b58d7-53fd-32aa-9724-db544ea71d47 | -14.05529 | -44.55692 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94a1e471-415d-38ba-bea2-f746381f4b5a | -8.70229 | -50.44328 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c6661ee-0078-3397-aaec-7a976e1af0b8 | -12.76784 | -48.08374 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 616b36bd-6c48-3507-9fb9-b040d75d26d0 | -11.38192 | -43.62268 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14dae7c1-0d01-3650-9be2-04a08bd84752 | -7.70749 | -50.2625 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 066bb9f9-c5f0-357f-8501-c6a5f778fa4b | -14.27505 | -45.24913 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a9b030e-a9ac-3057-ab0e-901438efb744 | -13.50827 | -47.00854 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a9f44fa-c3ef-3662-a2d7-590ac68f8b0d | -9.73271 | -48.97935 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60613a80-9e58-3b31-9a78-a7841d9c23fe | -11.10619 | -44.62223 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 253e6fcb-3d0f-30fd-8529-3dab98909700 | -11.65636 | -52.17482 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0a594cb4-23ba-32e6-bf58-6e24f99dbe8c | -7.69895 | -50.27448 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 677a7cfe-4ac6-33bf-bcf8-f060703398ca | -12.85844 | -48.053 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9a04346a-dc36-3023-9df0-99b8798051d5 | -12.12859 | -47.19495 | 2025-09-02 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e942935-8407-36c9-bcc6-8ce1270fd204 | -12.61437 | -48.17989 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e2b31e65-bdb5-34d0-bc8d-3735527daf81 | -13.69296 | -46.94125 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| d968272b-0817-3055-890e-4ec9e8d92b6b | -9.4843 | -46.50778 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cfeb98b-ba79-3520-8bd1-fa423290f1c2 | -8.70478 | -50.43139 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9fe083d-5001-3d43-8773-ae73bd40c78c | -12.99059 | -48.1049 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36fb65a1-4960-3ff4-9b68-617e57606f2f | -13.52589 | -46.99953 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 552f4658-e8fa-3da0-98f2-58889e33b88d | -11.65555 | -44.85809 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d7fec82-5fa7-325c-b997-1d05e444e096 | -7.99054 | -44.05033 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fa4a96d-9b81-3e45-8941-844298f1ca8e | -11.48181 | -46.79422 | 2025-09-02 03:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5b8864c-f5ab-35b9-9c7b-3f3d0b0deaf6 | -12.64926 | -48.25386 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ed6199e-beac-322a-a536-9169c653cf51 | -14.61073 | -48.04411 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 221a4da0-fb8b-336b-9f79-b30f32b4ce7b | -10.04997 | -48.10249 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 370e7b00-465d-34d4-8d55-dff0c9b3409f | -7.48938 | -45.3594 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bbf88a4-e251-3585-a7af-f900e40f15cf | -10.66784 | -47.33487 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8faf397a-d815-3bd9-95ca-c91045221490 | -11.64911 | -52.17366 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 087c512a-9f07-3c96-84b1-4a79860e3a62 | -11.79863 | -46.40693 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37d6d4cc-36a5-39a4-be6e-bcb68e77c22d | -11.05252 | -46.89641 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdffe83a-17fc-3e21-8c6d-c06e4b131c00 | -13.51842 | -47.01074 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
