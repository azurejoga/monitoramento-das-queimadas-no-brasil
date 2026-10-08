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

## Dados Diários - Página 402

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d448cfc6-cc0e-3a38-ba2f-2d5cefd4c8e0 | -2.1019 | -46.5761 | 2026-10-08 19:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b62357c7-3a9a-306a-bc7d-92c753453272 | -6.895 | -43.7066 | 2026-10-08 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 5c15f3d1-f528-3cff-9013-a3900e1ac498 | -11.1992 | -49.408 | 2026-10-08 19:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c2da2e86-25d0-3bc7-8f79-4694e90f1329 | -2.853 | -54.1322 | 2026-10-08 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| afe1090f-7f05-39eb-a7b3-bd68606fb1f9 | -7.5126 | -47.3358 | 2026-10-08 19:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| b9939dd5-7c41-3092-b8fd-bcd04523bcb6 | -5.5146 | -42.8399 | 2026-10-08 19:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 03eaabab-6fb3-3af4-b3a2-3c5353e54064 | -8.282 | -45.749 | 2026-10-08 19:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5b60eadb-3f95-3727-8ffa-d9aea3acaf9e | -3.2031 | -53.8621 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2c1414f5-677c-347a-80c1-9db0afbeac04 | -6.1042 | -55.6964 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 5e4e36d4-1144-3874-839d-535fe14f70f4 | -13.885 | -44.1365 | 2026-10-08 19:10:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| c49e46d4-2b22-3533-8720-43b47937fa1d | -5.2352 | -56.109 | 2026-10-08 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 8e473ad4-ef14-37d6-92be-f8c2b6338cb5 | -6.0744 | -43.1478 | 2026-10-08 19:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 113.2 |
| ee0c9ff7-0725-349a-a349-2e36c051c533 | -8.2621 | -54.717 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| bca42081-f265-3389-be63-d0a1bde7ee76 | -4.1457 | -43.2103 | 2026-10-08 19:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 222dd68c-31a3-38d0-9b68-2331ed250a45 | -4.7404 | -55.6522 | 2026-10-08 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 8fba995e-7224-3154-b39e-07d32c9241b6 | -5.5144 | -42.8634 | 2026-10-08 19:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 69267756-85c6-3a96-9335-6e061fa57e7d | -3.195 | -42.9772 | 2026-10-08 19:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 2e1d49a7-8c79-3c39-88fd-e332706ed13e | -6.8952 | -43.6833 | 2026-10-08 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 4f46e87f-4a50-3625-83ea-b695bb0c8db5 | -7.4694 | -42.8551 | 2026-10-08 19:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 63a98e81-5875-3541-bb7d-ab2748812133 | -3.2533 | -50.3899 | 2026-10-08 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 29fdc311-97eb-336a-8fce-eaa23a7e58c5 | 1.6938 | -55.6066 | 2026-10-08 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6976535f-2751-3245-a9de-ce21780a5de3 | -2.9451 | -54.0698 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8856c956-4043-3de2-b413-49999c8b9223 | -2.9267 | -54.0501 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1d16f91d-99a6-3628-a818-231d366a2557 | 1.6937 | -55.6263 | 2026-10-08 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5ad43928-d4ae-3498-9ecb-31547d2efc16 | -6.8322 | -39.2961 | 2026-10-08 19:10:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 92.8 |
| c52f40ed-71fc-311d-bd81-930becaba966 | -5.8799 | -45.9761 | 2026-10-08 19:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 96842428-26e7-3f55-8f50-7f5e6e293020 | -3.1484 | -53.7225 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 405a13fa-f18b-310f-9250-fbbe9928a03c | -3.2955 | -53.7185 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 368457a1-605f-395f-996c-32eecb2c256b | -3.2717 | -50.4102 | 2026-10-08 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 46dbd2d1-a009-3bd4-96a0-796f7573dbb2 | -6.0024 | -40.935 | 2026-10-08 19:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 148.5 |
| 5210cc6e-780f-374e-9af5-23e240df758b | -8.2823 | -45.7264 | 2026-10-08 19:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 778dabf0-32f8-3e79-8165-23725fedb032 | -2.572 | -56.1646 | 2026-10-08 19:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 88069ec2-6d37-30c9-a8ca-32fa6e6bbe34 | -6.1041 | -55.7162 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 95c25696-e165-350f-9594-ffbc403b8de4 | -9.2778 | -47.4554 | 2026-10-08 19:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 339eed5f-fb72-3b23-bf0f-edf11af8b52c | -13.3671 | -43.8742 | 2026-10-08 19:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 220.4 |
| b0b03bf3-ec42-38c5-94b9-c68964514656 | -5.4806 | -44.6029 | 2026-10-08 19:10:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| bf8d5ae8-6d73-365b-a929-41a1aa80eb51 | -6.0609 | -42.608 | 2026-10-08 19:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 135.7 |
| ab07c4ca-5e10-3c35-9e93-8867c49cd312 | -6.1501 | -51.6992 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| b64be34a-376e-312a-a7f6-f1943c5f5c73 | -2.8895 | -54.1915 | 2026-10-08 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 2df0d4e9-f317-3203-aa00-d6b3f9b92dff | -6.1617 | -47.9201 | 2026-10-08 19:10:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 4ccc49d5-1971-30c6-84f6-b4360cb2bd46 | -6.8319 | -39.3213 | 2026-10-08 19:10:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 194.9 |
| 77bee305-928a-38f5-91b5-942f685bbc8a | -3.3636 | -50.4911 | 2026-10-08 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 20d4e1a5-5dd2-33ec-a3ad-9b2bb469042b | -2.7152 | -57.472 | 2026-10-08 19:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 60299a7d-0e12-37cb-a75d-a0147f43d4d0 | -4.7009 | -56.2268 | 2026-10-08 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 7e0bb9c1-098e-3a8a-96c7-9f1cd77c59de | -11.0754 | -44.0534 | 2026-10-08 19:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 83ef46fb-8a1a-3f42-a044-cfec8790d2b8 | -10.4914 | -47.231 | 2026-10-08 19:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 77e8f2c8-dbd8-3aa3-9a85-a442d2cb4bac | -7.9086 | -54.7194 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 2ed850a2-ed83-385f-aa5e-3894af5d39b7 | -14.4345 | -43.9157 | 2026-10-08 19:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 245.6 |
| cba1535c-24aa-3381-8d10-cb135ae5e1ef | 1.7672 | -55.5463 | 2026-10-08 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e975333f-a026-3ba6-933b-3756cb91c3a6 | 1.7671 | -55.5661 | 2026-10-08 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 1bf9615d-2196-3225-bf1b-d29fa6f5df45 | -3.1298 | -53.7834 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| bc94df40-ddb0-3a72-a6de-21246f83c03f | -6.498 | -43.9501 | 2026-10-08 19:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 237.7 |
| d6ebcbe3-9347-3870-8252-62d6f4293224 | -8.9772 | -45.9249 | 2026-10-08 19:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 1a6c8310-0160-334c-a839-2538999b94e1 | -7.0281 | -45.3008 | 2026-10-08 19:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 61b7e443-4ce7-3327-9429-363cff99dde3 | -2.5903 | -56.1839 | 2026-10-08 19:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 180.7 |
| 4e66837e-4949-36c8-9de8-17e01a5375ab | -5.9266 | -51.8358 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 18c8b93e-4d72-39ec-9c0a-52a0fd28db86 | -3.9483 | -56.0138 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| fe6192dd-d7a1-3164-813e-5ca2e991e228 | -6.8904 | -45.9212 | 2026-10-08 19:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1d116836-766e-35af-bf7a-f2f7451fb960 | -14.4535 | -43.9359 | 2026-10-08 19:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 962b5c49-1cd2-3e28-8d14-4d81c50dcb2d | -3.5726 | -58.5581 | 2026-10-08 19:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| beecf7f7-34d7-3ede-846b-bd07277232ae | -2.0649 | -46.577 | 2026-10-08 19:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 20747780-7495-3eeb-8545-95a0e67566ff | -3.2137 | -42.953 | 2026-10-08 19:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 553.0 |
| 74a9b853-6ad8-30f1-bd14-eb374bc5ff77 | -3.188 | -58.6241 | 2026-10-08 19:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 50e381da-a579-3537-a65b-3816684581bf | -5.9586 | -55.3648 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| e41c1f7f-6187-324b-b32b-dc1390d306a9 | -7.0892 | -52.6753 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 281.4 |
| e188c6a7-15b8-3e1a-b837-2e8ac5447e66 | -7.089 | -52.6958 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 254.6 |
| 29f01518-89cd-3145-93d2-121e9e696e9e | -5.8801 | -45.9537 | 2026-10-08 19:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| d0e5c8aa-9097-3543-9fc4-ee972c87b1f7 | -10.9384 | -45.3916 | 2026-10-08 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 25d396f2-0845-38fe-b448-2c643686f805 | 1.7488 | -55.5663 | 2026-10-08 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| eb307ea5-6454-38d3-9483-cf8d95cd67b0 | -8.9964 | -45.9002 | 2026-10-08 19:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| e2423596-a651-3b2e-9e94-09b05a18ca39 | -3.1115 | -53.7637 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 350f026c-4187-3bb9-bfb1-378f3a8def55 | -1.3264 | -56.398 | 2026-10-08 19:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 5fdca0c2-3495-3339-8846-1f28d9cd1a20 | -2.4942 | -58.0768 | 2026-10-08 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| d25afee6-efb6-3c75-9113-d0e0465fc9e7 | -5.6934 | -53.4667 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 267.6 |
| 3287ca2b-1bc0-3ad4-bf8d-d587bbf57e93 | -15.1248 | -43.6369 | 2026-10-08 19:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 136.6 |
| affbf0fd-9bdf-350c-a64f-275654b20056 | -2.7429 | -54.0945 | 2026-10-08 19:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| bbe08985-cbf3-39ba-a7ab-5d259e67512d | -11.2267 | -45.2604 | 2026-10-08 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| db0ba212-1b61-3bb9-bc01-088cde7c281f | -7.4886 | -42.8295 | 2026-10-08 19:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 33f65fe4-0488-3d87-ba93-d6a5fa86fb73 | -3.6603 | -54.512 | 2026-10-08 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| e6c91019-773a-3cf8-b56c-43767725a391 | -11.2482 | -46.2604 | 2026-10-08 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| ac0da186-9dbf-3f6b-9313-ba936a5891e3 | -3.1541 | -57.6772 | 2026-10-08 19:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 12f873b6-babc-3ca6-bf1a-aa725a734e4c | -6.9328 | -43.6799 | 2026-10-08 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 284e3907-ccf1-317b-9211-5fbe88570b07 | -2.5492 | -58.0373 | 2026-10-08 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 307.4 |
| c623728e-2686-3c0b-90e6-72d098c99159 | -4.7589 | -55.6516 | 2026-10-08 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 62d13d56-8929-3d55-b981-d90ec801908c | -2.8712 | -54.1719 | 2026-10-08 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| b4d45984-ea26-39c4-a68d-43bbcdbf834a | -6.4568 | -55.4609 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| e5947e5e-a074-3040-ab3b-51c3c99f1a8a | -3.3912 | -58.0017 | 2026-10-08 19:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 765401b1-0024-30e5-bdb5-339b41453868 | -3.9121 | -55.8964 | 2026-10-08 19:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 17b16fa5-449c-3ea9-9012-3150e3f0578f | -6.6814 | -55.0903 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 466fdbd7-e292-392a-a527-a8a0ad4a2ffc | -5.0631 | -45.4466 | 2026-10-08 19:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e4e47288-9027-377d-a991-7df3e0674f1e | -15.1051 | -43.6409 | 2026-10-08 19:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 210.2 |
| 753af3c4-2634-35c7-85d6-58c437d4d024 | -15.0346 | -42.4941 | 2026-10-08 19:10:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 101.1 |
| e26d9ac1-b4d5-3cba-9782-68043e7c1ea3 | -2.5309 | -58.0376 | 2026-10-08 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e2b8bb7b-5107-39f1-8cf8-13197046aa6c | -6.1615 | -47.9419 | 2026-10-08 19:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 4f595456-7913-3099-bcb9-fc10238e6543 | -2.8346 | -54.1326 | 2026-10-08 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 18f5b85c-4c40-3027-b59e-bd7552f67781 | -6.3283 | -55.3276 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 6e17b48b-b5dd-3f39-a176-97850515f664 | -2.7613 | -54.0941 | 2026-10-08 19:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 4c81a82a-f47a-312c-9b35-513f1e840686 | -7.0706 | -52.6764 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 9d9fc49f-87db-33ef-95d3-e78bab87afc4 | -2.1361 | -54.4671 | 2026-10-08 19:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| c51a4967-da04-365b-9b2b-a6d78037345b | -4.1025 | -44.1149 | 2026-10-08 19:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |


[Clique aqui para ver as próximas entradas](README403.md)
