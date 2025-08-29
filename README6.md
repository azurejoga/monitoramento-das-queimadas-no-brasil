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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39246894-c060-3c37-b4e8-118b9c203d64 | -8.4512 | -43.715302 | 2025-08-29 00:31:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95a38f75-65e6-37c5-a8d0-a5f7acc4b589 | -13.4531 | -46.9529 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b759c406-cbfc-36a0-9940-b31e16f478c9 | -13.596 | -46.854301 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 91899135-db04-347a-a3be-9745cfc2c02c | -8.7116 | -47.861599 | 2025-08-29 00:31:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd640151-a5b1-3548-9aea-992f763d02f0 | -17.361099 | -42.6446 | 2025-08-29 00:31:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 07b21e4d-d351-35f4-8ac6-15619e4eb983 | -5.7605 | -49.982899 | 2025-08-29 00:31:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92b28394-b1ae-37a6-a6e9-4b4bc9fa5f4a | -7.0317 | -44.6716 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47e6dfcd-62fb-3484-aeb6-75086522a8e7 | -15.7967 | -43.343899 | 2025-08-29 00:31:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 828ac76c-b742-3d10-ba23-ead088df4acd | -5.7244 | -45.5364 | 2025-08-29 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dfe84ed-489a-3fac-bc30-426cac3464bb | -10.0273 | -51.114201 | 2025-08-29 00:31:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7772c324-1f71-3858-a6a1-0085e8d28116 | -11.5589 | -46.368599 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c595ee06-16dc-3cc8-b745-f04ee43249c4 | -9.4331 | -47.637901 | 2025-08-29 00:31:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c85a798-637e-3283-af4f-ccb166a792ec | -8.9107 | -47.321701 | 2025-08-29 00:31:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7df12cc9-4fd4-37d9-ae3e-f2cdaf87a95a | -7.4143 | -43.385899 | 2025-08-29 00:31:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d66612e3-6aec-37ae-95ca-3e313cef7d47 | -13.0807 | -43.064701 | 2025-08-29 00:31:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ebe9fa6d-f4d9-3347-99f5-7d491a533726 | -11.0953 | -45.122101 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23c6bdf0-3742-36bd-80c1-c0d379ca7065 | -11.3496 | -43.570702 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 001db939-e59d-3ec0-84d2-ce735f9b7438 | -14.3434 | -48.655201 | 2025-08-29 00:31:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d543d981-16e9-32d3-b560-b0bee77879ab | -13.2004 | -45.278 | 2025-08-29 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e512ef7c-0280-3f23-8250-edc519a4c09c | -6.542 | -43.0998 | 2025-08-29 00:31:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40d4d1ea-e125-31e2-9889-a6d88c4e8355 | -7.3321 | -46.118401 | 2025-08-29 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85d7ee18-a354-35e8-a805-f5e9b2596912 | -11.3022 | -43.544201 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 373777c1-155b-3e96-bf47-cda37aaa5365 | -5.7894 | -42.576199 | 2025-08-29 00:31:00 | METOP-C | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 987218ca-311d-306f-bc53-2387c93c7dee | -6.702 | -49.459099 | 2025-08-29 00:31:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4b7cf1-2dda-320b-aabe-e890c62a99a2 | -15.0512 | -48.124599 | 2025-08-29 00:31:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45b0d4a8-e01f-3d00-bc68-fd37f807c8f6 | -9.4072 | -48.2211 | 2025-08-29 00:31:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5aab6cd7-db2b-3a14-958e-399e453f8cd3 | -13.543 | -46.941502 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b6d3331-0cd1-38c9-bc62-ca31de463e63 | -7.2206 | -45.313499 | 2025-08-29 00:31:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3941b1cb-e37a-33ff-9fef-32facd823e30 | -6.4421 | -44.576599 | 2025-08-29 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98e3069b-1af9-3a70-a365-34868b04030a | -8.4593 | -43.705799 | 2025-08-29 00:31:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 32ab0617-31a1-37f4-a9d1-a59abd1f9342 | -3.7601 | -54.813801 | 2025-08-29 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51c49788-dcb2-3bc1-b752-8f914c87887d | -5.1877 | -46.074299 | 2025-08-29 00:31:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d869342b-843a-3445-b9eb-cf55e6bf6a2c | -8.4752 | -43.640598 | 2025-08-29 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 60648e85-cdb0-311b-b0c0-653114bafea6 | -13.5609 | -46.929199 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ead5d5bd-eded-374e-a626-2cd51f1b54ee | -8.2097 | -49.549801 | 2025-08-29 00:31:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad69cce9-bf86-36e9-9bdb-4c810ea8ea02 | -17.357901 | -42.630199 | 2025-08-29 00:31:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a2cce864-bf23-3d4d-9dcf-94ff6922856a | -15.7869 | -43.346199 | 2025-08-29 00:31:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d4cf149-5958-36ab-b7e6-da3b2cfb01f8 | -17.9235 | -39.959301 | 2025-08-29 00:31:00 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b12b1eb4-539b-3ce2-83a7-892b5ec696ef | -14.3413 | -48.6451 | 2025-08-29 00:31:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a5471506-23a1-3d81-8a0b-e4b9ea63b4a2 | -10.6457 | -48.633701 | 2025-08-29 00:31:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cfb811da-83d9-3a7b-97b0-cd7c487655e1 | -6.8865 | -44.445301 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d156eea-001b-36a9-a685-f177b9557d49 | -11.5769 | -44.653999 | 2025-08-29 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72f30441-7b14-364b-b00a-1d4d35c941e5 | -11.3512 | -43.532799 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4a5907e-07f2-3c46-8d90-ab24416522a2 | -13.6747 | -44.2206 | 2025-08-29 00:31:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf0efecf-bfca-34d3-ad9b-ae9dd1fa02fc | -6.8006 | -43.764198 | 2025-08-29 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bd1c5e53-c2b5-372a-87e6-2be9b4e8ccec | -6.4856 | -50.198898 | 2025-08-29 00:31:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0e4d38a-9e41-3e61-8d92-2e73aa1662b4 | -5.5025 | -44.574001 | 2025-08-29 00:31:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a88bbb34-b852-3fdb-99bb-e92d3d7d2e13 | -4.4908 | -47.674702 | 2025-08-29 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4854aa4-700f-3b13-b8bd-3857545048ef | -6.5452 | -43.908501 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0224abe4-79d2-31ba-b519-7018420bcbdb | -3.4286 | -49.0317 | 2025-08-29 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59a35777-b750-3991-8b05-12c3f9666e30 | -6.2394 | -44.771 | 2025-08-29 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfce00fb-ee24-3bb2-bdf4-90384114060d | -8.7138 | -50.364399 | 2025-08-29 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4cd4f26-6281-3f09-aa5b-bda85872a8e7 | -8.6989 | -50.389801 | 2025-08-29 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07fcd313-11a4-3ee0-8789-3ad02dbc0581 | -3.9766 | -43.249298 | 2025-08-29 00:31:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c45aacdf-e856-35d4-9c94-53ea4def6a60 | -11.5787 | -46.2719 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25e9f286-2686-3b91-aa65-8e959501bb4d | -6.7137 | -49.465698 | 2025-08-29 00:31:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4e5025f-ec9a-31cd-aebc-b518966722d0 | -5.6313 | -44.997501 | 2025-08-29 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23242e4c-091f-32b6-abae-27e852001804 | -13.6357 | -48.249001 | 2025-08-29 00:31:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 988bd7cd-1445-3ecf-8264-9548e23aafd2 | -6.8789 | -43.612701 | 2025-08-29 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa4dcec9-94ef-3b85-a8d1-7679aa0765d1 | -5.1893 | -46.0812 | 2025-08-29 00:31:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78179176-5ddb-34db-8ce8-4c89a4afc990 | -11.3038 | -43.5513 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfe04e64-9e20-3bff-aee7-a6880798a2c0 | -6.903 | -47.9142 | 2025-08-29 00:31:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce8b233-2b9f-3ded-9971-31f83f56ab51 | -9.4365 | -47.6535 | 2025-08-29 00:31:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25081344-0b29-39ad-b25f-cec5263960b7 | -22.146099 | -46.6786 | 2025-08-29 00:31:00 | METOP-C | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b86ba199-14fa-3b35-be0c-bbffe18d469b | -3.6225 | -43.544399 | 2025-08-29 00:31:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d077195a-74d5-334d-95b2-21e549c9362d | -6.4893 | -43.535801 | 2025-08-29 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46f61d5f-7316-3d3b-b003-ca91cf4ec910 | -6.7118 | -49.456902 | 2025-08-29 00:31:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63b09fe7-55fd-3526-a040-910e96ee5782 | -12.575 | -43.783298 | 2025-08-29 00:31:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2e4dafb-f214-32af-8103-42d53e08a156 | -15.0644 | -48.387402 | 2025-08-29 00:31:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6cbef868-3317-352c-baa6-0b0a93962a28 | -5.6961 | -45.9529 | 2025-08-29 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 550822f5-eb84-3ed8-afa8-e4c6e86888ae | -13.588 | -46.864399 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a353d9b2-9df4-3e33-8a31-09b2df5961af | -13.5603 | -46.878899 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7b16ed5f-1f63-3a9d-91f7-28288194b2bc | -11.9584 | -44.837002 | 2025-08-29 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e55f1395-4b4e-389a-8954-4dc7b634c93b | -11.2271 | -55.045101 | 2025-08-29 00:31:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a9c778b-ebf1-39f2-b7a7-69f4a51a8650 | -7.726 | -50.293701 | 2025-08-29 00:31:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cdc5d48-811c-3147-9c71-64fb2a382d44 | -11.3006 | -43.537102 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71d5805f-9cb5-3bf6-9e3c-57f5753588ec | -16.2708 | -39.4669 | 2025-08-29 00:31:00 | METOP-C | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3ce6ec0-9672-3300-a017-5602f7f176f8 | -7.648 | -42.665901 | 2025-08-29 00:31:00 | METOP-C | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82c31837-9211-30b4-8d77-920da948a528 | -12.9042 | -48.128399 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55f91a33-e7d4-3cf2-ba4b-c2920058730b | -13.9052 | -43.871601 | 2025-08-29 00:31:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b214ff24-d2fc-33dd-881c-8827845ef507 | -6.5403 | -44.109699 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c760e8e-b690-3f4f-a4ba-d885cbb2908a | -6.7241 | -43.569302 | 2025-08-29 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 576c9e4c-0480-357f-a164-02bdaa3887e2 | -11.3104 | -43.5798 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47d9d3dd-8614-3539-b0cf-386c6a103d91 | -13.4548 | -46.960899 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fc252c35-d831-3db1-b32e-7743da9a6b17 | -17.5511 | -46.6119 | 2025-08-29 00:31:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 13d76aca-d287-39b1-923b-893e2cbfacb2 | -17.5431 | -46.6227 | 2025-08-29 00:31:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dab27854-3be5-308b-be72-eaa8a2a3565f | -22.677999 | -46.8559 | 2025-08-29 00:31:00 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4269ad53-410a-323d-be48-ee29a5810211 | -13.4815 | -46.8461 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 97019987-ee3d-3e9f-9897-6c97d064d4df | -4.5902 | -43.314602 | 2025-08-29 00:31:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a794429-18ee-31c8-a980-35aceeb895a7 | -17.933201 | -39.956699 | 2025-08-29 00:31:00 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4976813d-fdfa-3460-a54f-79c17dd1e1f3 | -24.176701 | -49.5522 | 2025-08-29 00:31:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 620be5c0-7eec-38f6-85c6-01285570cc4a | -6.7277 | -43.584301 | 2025-08-29 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55d4aa1e-71de-3257-a737-2bbf375f72c1 | -6.8904 | -43.618 | 2025-08-29 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c849d1f4-1330-38c5-ae0b-823bf1c48836 | -11.5402 | -47.314899 | 2025-08-29 00:31:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3dab517-b9ef-3bfd-a4c5-c1880df630ad | -7.6368 | -46.553101 | 2025-08-29 00:31:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fabd6831-c1b8-3bf0-a0d7-d0a1fa7bd1bc | -7.5702 | -47.493301 | 2025-08-29 00:31:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4964dc87-259b-3c34-84b6-b856ea8cb86c | -6.4991 | -43.5336 | 2025-08-29 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 467885fb-fabb-3a9c-aece-41e390ad0483 | -9.4966 | -45.3908 | 2025-08-29 00:31:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a30d6b81-2e3c-3e8f-a6b6-482e77f8d9ac | -12.0517 | -50.6553 | 2025-08-29 00:31:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8654a477-428b-38ae-9e66-6efd6fc0e309 | -15.1335 | -48.127102 | 2025-08-29 00:31:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
