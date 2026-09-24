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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46527566-d2cb-3bcb-a157-13d7fa1e1c47 | -11.9583 | -50.7607 | 2026-09-24 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 12b2e1b0-11bc-3564-9237-a8c049163eca | -6.1841 | -57.7786 | 2026-09-24 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 1828660b-db77-3252-9197-60a1e3be86c6 | -10.9115 | -53.9429 | 2026-09-24 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 97624208-c5ee-392d-9b69-c53db6ea9750 | -6.6146 | -59.9272 | 2026-09-24 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 124.7 |
| b20d92ee-ccd1-365b-bdc7-4b416b180c69 | -12.4024 | -46.9579 | 2026-09-24 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 96beae13-a74d-35dd-9f42-5de405c43a31 | -9.8488 | -48.5146 | 2026-09-24 00:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e6aa3c22-d537-39aa-b7a1-f2a334d6998e | -12.0414 | -50.3011 | 2026-09-24 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| b4ab1bba-ab3a-315c-af0e-d92dee42561e | -6.5962 | -59.9279 | 2026-09-24 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 49c1eff7-0a10-35cd-8cf6-8fc56578df2a | -12.0224 | -50.3034 | 2026-09-24 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a61e1984-1cce-3d1a-893f-dc35661d4e73 | -12.422 | -46.9326 | 2026-09-24 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c8b213b6-aa08-3d7f-b6e3-6f8dea2f278a | -3.4578 | -50.0679 | 2026-09-24 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5b91f0b3-5272-3ef4-986f-519b43ab21a6 | -12.0605 | -50.2989 | 2026-09-24 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 6241e082-74fd-3762-b7c8-f03ba8024742 | -6.3317 | -57.7725 | 2026-09-24 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 77643711-5c2b-314c-9eea-8c3ed4dd6b82 | -3.6764 | -60.5649 | 2026-09-24 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| cab0c52d-572f-39fe-aacf-7b8d8ecee5e8 | -9.8491 | -48.4927 | 2026-09-24 00:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f77324f9-ff29-3f08-9399-9f15ac7f4a2c | -10.0921 | -46.0232 | 2026-09-24 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 7bcbf60d-0585-3312-ac01-0faefb06b082 | -3.1637 | -54.6054 | 2026-09-24 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| f801ffd3-d902-399e-b636-8caa4667596f | 1.57288 | -55.93583 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9faccb38-cab7-3faf-85eb-14cf68133568 | -2.70679 | -57.50233 | 2026-09-24 00:41:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| af2fbaee-1aa0-33bb-b97f-eb09b3f16358 | -2.93129 | -57.92157 | 2026-09-24 00:41:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 19ec0fc5-8253-3757-8d38-b8992cfdf70e | -2.77202 | -57.02744 | 2026-09-24 00:41:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 93438195-f66b-398b-9137-94c1827fc0ea | -2.14845 | -59.23958 | 2026-09-24 00:41:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a89111e2-a041-35de-beca-4b4132dd0252 | 1.57409 | -55.94651 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 3101afa4-c38f-3342-a24e-a72420aba2aa | -2.46946 | -57.91454 | 2026-09-24 00:41:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6f0bf50f-303e-35dd-919a-cc2b32379cb6 | -3.44789 | -60.57747 | 2026-09-24 00:41:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d41890a1-e094-3533-b735-21f32484094d | 1.60028 | -55.90743 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e4cc514c-eba5-3318-9ceb-8a8ff8dff20e | 1.60242 | -55.89146 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 291f2f88-d50a-3116-b953-deca9032cafe | -1.92051 | -58.25999 | 2026-09-24 00:41:00 | TERRA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 12cb682c-8c7f-35bf-98a1-9c5fd06774cd | 1.57632 | -55.93061 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 1a7462c7-c87e-3ea7-a040-aed72d2ea5dc | -1.84111 | -55.06739 | 2026-09-24 00:41:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 62c517d7-d8be-346d-947b-82184cffdf71 | -3.28943 | -59.42601 | 2026-09-24 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 41c26dc2-66ae-3be5-bb98-6abc5e648820 | -1.27011 | -57.04336 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 426f358c-4ff9-3795-a0e3-a281eeb70c21 | -1.83165 | -55.73096 | 2026-09-24 00:41:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0f1133c2-058a-3426-85e6-f39ecdf934df | 1.50568 | -56.01668 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6c4cb751-2dcf-3737-ab6e-22913e226bab | -1.62272 | -54.90874 | 2026-09-24 00:41:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 2bb39dd1-a410-3afe-b4eb-985e7150c77c | -1.62511 | -54.92555 | 2026-09-24 00:41:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 955df1be-8a70-34e8-a46c-beff6f2bcb28 | -2.83741 | -60.22482 | 2026-09-24 00:41:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb3be4c3-5bf2-3d6d-ad4b-3c07398ba609 | -2.12357 | -59.59667 | 2026-09-24 00:41:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fb10fc7e-80c7-35c2-9c95-9bbfdeffc52f | -3.33256 | -59.86911 | 2026-09-24 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8fdbbaa7-84bb-36da-840a-3f591a238257 | -1.82962 | -55.71661 | 2026-09-24 00:41:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 9f92b770-53a6-3754-b06a-ef5916aeb5ad | -1.19851 | -54.14179 | 2026-09-24 00:41:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| dbd3d9d6-543a-3a9a-9aba-19336d807b09 | -1.63703 | -54.92383 | 2026-09-24 00:41:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 7885fce6-383e-37a1-b5fc-0058cadeaeba | -3.47933 | -59.53145 | 2026-09-24 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d4a70e79-fcc6-38ab-8ebf-ace5e799e155 | -3.5428 | -62.0826 | 2026-09-24 00:41:00 | TERRA_M-M | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e68933f2-362b-35c1-8e5d-96c225aeac08 | -3.44668 | -60.56865 | 2026-09-24 00:41:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 61041ee4-0573-3368-b413-a6b2199af21a | -3.54628 | -59.95203 | 2026-09-24 00:41:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3d0a00ca-b966-32dc-bbc0-092738e273e4 | -2.82981 | -60.2348 | 2026-09-24 00:41:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| fb7ffbee-d4c4-3a83-8211-1434f895084a | -1.92188 | -58.26984 | 2026-09-24 00:41:00 | TERRA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| d02e0d59-fdf2-3574-960b-af5cd1402863 | -1.28026 | -57.04193 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| bd8af26f-bcdf-3f1d-8f68-a9716a12807d | -1.63466 | -54.90708 | 2026-09-24 00:41:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| d1c5d498-490e-3edd-ac86-1cc11cbb67e9 | -2.83887 | -59.9747 | 2026-09-24 00:41:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8bdbd3f5-c147-399b-9f0b-3da02e42b230 | -2.7083 | -57.51295 | 2026-09-24 00:41:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 5f2324db-666c-3164-a813-2d88e4867a75 | 1.60336 | -55.97234 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 08826031-8036-3b37-922c-53d157e31bd3 | -3.39195 | -59.22687 | 2026-09-24 00:41:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d04cc2be-8b21-3145-8338-ca9be13510ea | -2.76208 | -57.02885 | 2026-09-24 00:41:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 24d01782-e098-3e90-91dd-83569e5125f1 | -2.41244 | -58.27991 | 2026-09-24 00:41:00 | TERRA_M-M | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3e81488b-da82-3f5d-9a20-dc54d32d13e4 | 1.57077 | -55.95184 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2b0c9290-519e-3828-aa3e-efeee3a1ec67 | 1.56632 | -55.83202 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4bcf4c7b-e7ca-3e55-a7f7-522ea07f5787 | -3.16017 | -57.69039 | 2026-09-24 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0087ce04-f5c8-32f9-a622-a225b9f04fcf | -2.68446 | -60.92797 | 2026-09-24 00:41:00 | TERRA_M-M | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf5a4356-ed7b-31d0-92c0-f2ca12ad54a1 | -2.60697 | -59.75973 | 2026-09-24 00:41:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 57cf0e1f-fccf-3538-aa95-74ab0e977019 | -2.57273 | -54.73882 | 2026-09-24 00:41:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5796ee8a-bffd-3ccf-aef4-5fdc48ebb4ef | -1.27859 | -57.03004 | 2026-09-24 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 7daf0d6d-1160-3ec2-9704-79e8633130f1 | -2.1472 | -59.23054 | 2026-09-24 00:41:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 90711527-3f76-3f7d-a55a-76dd85350dba | -2.83861 | -60.23357 | 2026-09-24 00:41:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cf046729-71bf-32e4-b53e-5197bb567cda | -2.82861 | -60.22604 | 2026-09-24 00:41:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 978ab903-1e6f-3ddc-bf11-687bddbd4c27 | -3.60548 | -60.57935 | 2026-09-24 00:41:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c9a0d5bd-3ef0-3592-97d9-66b68a5e4ebd | -3.44547 | -60.55983 | 2026-09-24 00:41:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1c7a3e5-501e-3d1d-a704-1c29679e0051 | -3.33135 | -59.86034 | 2026-09-24 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 999b1eb2-48ee-38f0-a477-1fe40b6ce2b9 | -5.7754 | -45.1053 | 2026-09-24 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 673a2b50-a71d-364e-84c1-439fce332f1e | -9.695 | -64.9081 | 2026-09-24 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 01e61a37-b9df-33de-ab88-ecf1ffd9cc50 | -3.4577 | -50.089 | 2026-09-24 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0cef943b-f2ef-36c2-9678-50112c2aa7fa | -10.0917 | -46.0458 | 2026-09-24 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 815303f0-53bb-3fbd-965d-cde5bdcef887 | -8.2616 | -54.7776 | 2026-09-24 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 883fcb83-9d4b-3aae-8f37-ae18808b341e | -14.4786 | -53.6485 | 2026-09-24 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 00d05b3a-011c-35ee-aff7-6c1b81660cd6 | -11.9586 | -50.7393 | 2026-09-24 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| eec3ecee-1bd6-3dc7-8e71-3100832fd68b | -10.0921 | -46.0232 | 2026-09-24 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3fa7ac96-2a49-38e8-ba21-2e6b4427b9dc | -6.4302 | -59.9724 | 2026-09-24 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f2d55b91-5648-375e-b1df-cd17439e0976 | -10.2637 | -49.9626 | 2026-09-24 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 0bbb2e3e-b9cd-3f81-8555-3e61da2fd773 | -6.4487 | -59.9526 | 2026-09-24 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| ae2115d3-2306-3c60-87a3-41722f0ab382 | -6.5962 | -59.9279 | 2026-09-24 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e7df39c9-a624-3fba-bd8a-629708cefb5f | -3.4392 | -50.0896 | 2026-09-24 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 716a53f8-fb86-3762-9a54-803a3b10b750 | -10.0924 | -46.0005 | 2026-09-24 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a8dcb488-657d-3651-b0bb-23d5d564f158 | -3.4387 | -60.5695 | 2026-09-24 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 978a5b3b-320e-35c8-9b74-7902cd55ddb5 | -4.118 | -51.0903 | 2026-09-24 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 91624e3f-c5d9-3808-bac5-39af664bfd48 | -8.8914 | -62.5436 | 2026-09-24 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8b7e4b15-4473-39bf-b2d3-60431f24e288 | -3.457 | -60.5881 | 2026-09-24 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| e60e327f-eeb2-3ddf-b417-3a40abd2df01 | -4.1181 | -51.0695 | 2026-09-24 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| eb7e9c19-e150-3644-bd9c-5e08a2efd617 | -6.6145 | -59.9464 | 2026-09-24 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9fc4423f-d266-30d1-a9a4-49ff52d17733 | -2.8366 | -60.2379 | 2026-09-24 00:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| a3ab3dea-515b-3cad-a71a-2065292bed92 | -6.0928 | -57.6262 | 2026-09-24 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 1e040634-ed1d-3e22-bceb-6cf70e6d600d | -10.2827 | -49.9606 | 2026-09-24 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| d3208915-9a87-39b3-87e5-4ddaacbfdaed | -9.4953 | -64.0316 | 2026-09-24 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| cd97ef26-45df-375d-9fba-02eb504a3703 | -14.4789 | -53.6276 | 2026-09-24 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| d0e60648-e91c-3334-86c6-c794d7d0fdc9 | -6.3501 | -57.7717 | 2026-09-24 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4b246c80-0c58-3949-bb1a-f8f804778e35 | -4.2951 | -49.1234 | 2026-09-24 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 34d55975-8722-3ad5-997b-f5bf777db681 | -9.5139 | -64.0309 | 2026-09-24 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| be4f126a-c32f-3dfd-a667-0b8c39856e47 | -11.9583 | -50.7607 | 2026-09-24 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 1eb4a128-73b8-3e93-9ede-d13007291a84 | -12.0605 | -50.2989 | 2026-09-24 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8b859740-b4c1-3e09-a9a8-8aa265525465 | -12.0224 | -50.3034 | 2026-09-24 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |


[Clique aqui para ver as próximas entradas](README21.md)
