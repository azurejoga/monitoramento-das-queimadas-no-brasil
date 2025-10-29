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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c45c5a49-6d8d-3dbe-8fb4-ce54ff1fc11b | -10.5218 | -47.7373 | 2025-10-29 04:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 154d0bc7-7511-3306-af85-32c9f3f7482c | -18.9197 | -45.0478 | 2025-10-29 04:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b502c409-cd2e-3904-a69c-ac4e1a19412d | -15.1006 | -43.8333 | 2025-10-29 04:00:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4b11db20-e205-399a-9068-f067dac17fd8 | -12.7021 | -46.303 | 2025-10-29 04:10:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 05fe42d9-617a-37b7-9f35-7fb42ac78a33 | -15.1006 | -43.8333 | 2025-10-29 04:10:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 40b6a431-cf43-3d67-8104-af0e197ebeba | -12.1958 | -46.717 | 2025-10-29 04:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 95c79124-40bc-3492-b5db-1b7e157a7eca | -4.2156 | -50.1022 | 2025-10-29 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 198b3502-f1cb-3fea-818a-01937e353689 | -4.1972 | -50.0819 | 2025-10-29 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 2ea9357d-0f3c-3cdc-99ff-31a431cdd015 | -6.1249 | -41.8414 | 2025-10-29 04:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| c2d9936d-4bea-3460-addc-9c2c38e77638 | -4.2157 | -50.0812 | 2025-10-29 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 27a09cc2-23a2-3a5b-ada0-bc4a7fc70c65 | -4.2159 | -50.0601 | 2025-10-29 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 22addd52-20ca-365b-99d9-cf239c3694b6 | -6.1249 | -41.8414 | 2025-10-29 04:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 05b823fc-9b4d-35fd-922b-f418a7b8e2b0 | -15.1006 | -43.8333 | 2025-10-29 04:20:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 6d4dd006-7d27-39f1-9960-654fc16ba321 | -7.8037 | -46.4458 | 2025-10-29 04:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 318c9ddb-4375-34e3-b448-23bf64308f63 | -4.2157 | -50.0812 | 2025-10-29 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 180.6 |
| cfd227fa-3b85-3170-ab74-a1bacce158b6 | -12.0036 | -46.7667 | 2025-10-29 04:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 293134c6-da7a-301f-b186-ec81281418d0 | -4.2156 | -50.1022 | 2025-10-29 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b1c705cc-9251-311d-aa28-f110fac7399e | -4.1972 | -50.0819 | 2025-10-29 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 2465aa90-94fe-3246-aa3b-ed4dbde2d022 | -18.9197 | -45.0478 | 2025-10-29 04:20:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b632bb7f-e7ed-34b6-9257-ef30194ed792 | -3.5934 | -47.51629 | 2025-10-29 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f41eca09-1af7-35a5-88ca-9a797ab6b101 | -4.20148 | -50.08917 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbcc5639-dcfc-31f8-8653-006a828e2242 | -4.67952 | -43.24366 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0990bb5c-a412-3f59-b87e-bdbcc8445aaf | -5.11508 | -43.29272 | 2025-10-29 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b807199b-f96b-3bfb-80b5-4d4fd372cbc4 | -1.14188 | -48.09978 | 2025-10-29 04:21:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebe3d633-f2e3-3ddc-badd-04ef84667601 | -2.80249 | -49.14906 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 051ccb47-dad1-348f-a07f-e1140a7c102d | -5.26402 | -42.49273 | 2025-10-29 04:21:00 | NPP-375D | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3f103e9c-8ce2-3ddb-a377-ad4bd439a9b6 | -3.59771 | -47.51876 | 2025-10-29 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96eebe7d-0652-3c5a-8116-3951c39d5a73 | -5.38384 | -42.24422 | 2025-10-29 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4840ff83-bb32-31f7-b79d-1da10484b213 | -4.51625 | -45.99726 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 632973da-0b08-33a0-9dfa-95de24652f79 | -3.11581 | -40.99147 | 2025-10-29 04:21:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2940b30d-482f-38c5-b0c7-3bd09fff5fea | -3.12581 | -49.10393 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66ecd6b7-e964-3490-b2ef-ca0862801516 | -4.77219 | -46.50997 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7fae504-62f6-3180-bc31-9de16c330039 | -4.96279 | -42.63749 | 2025-10-29 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 461c0495-1a29-3df9-ac88-0ad85c3ef64d | -4.08322 | -46.93313 | 2025-10-29 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 46c94322-b580-35dc-8b31-12292df110aa | -4.41189 | -47.96555 | 2025-10-29 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edae0694-25d4-3e2f-9a79-df177943e4ed | -5.08521 | -44.81209 | 2025-10-29 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5fd4f9f-5786-3922-9683-9125388dffc8 | -2.43068 | -49.3036 | 2025-10-29 04:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4416b53b-4f9e-377f-a664-fe301e4ab359 | -3.37385 | -50.14585 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77265fa4-c3a5-3899-8f4c-0ced4aed60a1 | -3.78428 | -45.5928 | 2025-10-29 04:21:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6090a16f-d2a8-3cfd-9ff9-c3a1b44bda7f | -4.23037 | -43.62357 | 2025-10-29 04:21:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebe9416a-e14d-3e84-96ef-30bb86ae1dc6 | -4.92901 | -44.55998 | 2025-10-29 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 856c0817-0800-35af-bbfb-6cb2ef1f3d51 | -5.63611 | -41.53519 | 2025-10-29 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 431c0c62-537c-399f-a917-20f6d65cbc1b | -4.21801 | -44.24263 | 2025-10-29 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 864d2e48-a479-3a49-bc83-56ebbdec0543 | -4.479 | -43.44011 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b07459e3-e322-3095-a3cb-0ed96396da9b | -4.66696 | -46.40486 | 2025-10-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67bfb3db-05c8-3ff7-a403-3506225c91c9 | -3.72274 | -41.56979 | 2025-10-29 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 00814362-cd11-38e4-bd0b-0f6953b835cd | -3.71922 | -41.56927 | 2025-10-29 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ea8d9ccd-8e67-3637-abfd-47225d8bd05c | 1.83143 | -50.50114 | 2025-10-29 04:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24ab72fc-c98f-3965-ae53-56a8cb706568 | -4.72249 | -46.81686 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d803409-1661-3add-b94e-c8c702438727 | -3.86676 | -43.35596 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e1fd831-782b-397c-a053-7ff7319efc9e | -4.99014 | -44.68725 | 2025-10-29 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bc9660f-155d-3a04-a79d-04d431d97d20 | -3.70635 | -47.64781 | 2025-10-29 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7695590-5095-3465-b898-37c2da8c7dae | -4.14374 | -50.68571 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32f25d88-78ed-3655-abfe-2a122cdf3a89 | -3.15578 | -49.2536 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9111a13d-4c1c-3226-ba50-69add75f255b | -5.02369 | -44.81308 | 2025-10-29 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cd1c69b-6f6a-3490-a43d-499d4a8b710a | -4.30639 | -48.06461 | 2025-10-29 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dddf49e1-5da3-38ce-8d9a-9ad6f699470f | -4.72975 | -44.45075 | 2025-10-29 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 131575c6-bb69-3bfd-8652-a5244cd69d8a | -3.30811 | -49.13388 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc825277-bc86-3652-bfc4-ab28fcbcd1a9 | -4.20215 | -50.08516 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17ad46c8-7242-3089-9987-9a60d8136c9f | -3.81377 | -48.65239 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e51f638-cf37-326c-b413-5a42b8c53509 | -2.85591 | -48.24286 | 2025-10-29 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c9475156-ecfb-3c9c-b6ea-b703bfcf9ce1 | -4.00474 | -43.20824 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85944c79-219a-322b-99f0-fedea84417b8 | -4.37386 | -48.67914 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc18585c-95af-3ead-a818-0bbcc7b384f0 | -2.90826 | -40.34819 | 2025-10-29 04:21:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7f36acb0-3dc2-3d90-974d-098077443ba5 | -1.50697 | -53.15766 | 2025-10-29 04:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c37d591a-6155-3fc6-bcd8-38928d96179b | -3.70266 | -47.64716 | 2025-10-29 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92fe6b92-c5da-3a39-85b0-271eea456488 | -4.21564 | -50.0832 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38b76e01-c2ca-39ef-9d04-5c9b39beef82 | -3.10703 | -42.61206 | 2025-10-29 04:21:00 | NPP-375D | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bd4886a-f382-3734-8562-09655fb1c38d | -4.26834 | -46.92472 | 2025-10-29 04:21:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e091634-3bee-3dc5-8ae6-f4e2bcaa3ad6 | -5.56483 | -42.17178 | 2025-10-29 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 998acad5-c3c9-3a02-9bf2-52b098996549 | -4.22919 | -48.36803 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30bc3c4a-7e23-3826-becf-fdd57f0d010c | -4.10825 | -48.73746 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b909724e-1b2a-34ae-8479-57a6914fd87b | -3.48012 | -52.86407 | 2025-10-29 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c39bee3-05be-3fcb-bd02-72ad1d8d6852 | -5.09681 | -42.47189 | 2025-10-29 04:21:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb6835de-a1ed-3c3f-900f-f58470aebc00 | -4.01372 | -43.23852 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f96acc0b-03a5-38f3-a185-45e9eca44422 | -4.58573 | -47.03865 | 2025-10-29 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a97f3126-9424-391c-8135-d14edc38c523 | -3.35582 | -52.80683 | 2025-10-29 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bd5556f-794c-3ab3-a41c-824eb0073d6d | -4.08839 | -46.94626 | 2025-10-29 04:21:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b261623e-f7c4-305f-9635-31c5cd498ec2 | -2.99587 | -51.25205 | 2025-10-29 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75579e15-d994-36f0-95ab-a0a5aee31a90 | -3.32299 | -54.08521 | 2025-10-29 04:21:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8ac2758-bcac-3d00-91cf-55c1d56d8b09 | -2.13849 | -47.99966 | 2025-10-29 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5721d45-4860-3b23-bca9-e0d5fa01aed5 | -2.43008 | -49.30738 | 2025-10-29 04:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bb13db18-2ec0-3eca-abfc-8adb2d104fed | -4.67674 | -43.26138 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e41e64e-6e25-380a-8b54-cf67c4c09dca | -2.76734 | -45.40071 | 2025-10-29 04:21:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15e4f57f-b59d-3141-b2b2-ef0757124957 | -4.4818 | -43.44414 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ecd2a865-9d9c-30d3-87d0-00f6f782cdb3 | -4.20082 | -50.09315 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5f53f23-15a7-36e3-91f6-4e600d5d96c4 | -3.31994 | -45.35429 | 2025-10-29 04:21:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5be9da75-9b65-3d26-936d-be88e2a799ca | -3.26044 | -49.11888 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2fe3303-7040-3fb1-a100-3ded22ba94c3 | 0.15008 | -51.10105 | 2025-10-29 04:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcea3346-c7a1-37e8-b892-642dedfd24ef | -2.08223 | -48.37056 | 2025-10-29 04:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7785e2da-ab10-30cb-8cc3-864886f9ee92 | -4.70483 | -46.10578 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ed4a4bd-9305-30ff-9672-f6fbc61737f6 | -4.20348 | -50.07711 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 312a7395-c418-34cf-a996-50d31628da09 | -3.03935 | -50.27293 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 710130c5-fc3e-3286-9ee8-3f8826493bab | -4.66006 | -46.4037 | 2025-10-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf75b42d-012d-3645-b418-7c6c0385510a | -2.80308 | -49.14545 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a311260f-2388-3d87-b56e-90a54f7670b9 | -3.99556 | -43.65789 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f143a79c-d271-3ee7-9980-7b6894bc088d | -3.87011 | -43.35648 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8227391d-7ba5-3cfa-aa2f-7ca6e7f2a52e | -4.33121 | -48.62251 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 194f5862-0788-3d37-9509-66e7819cc8e7 | -1.4951 | -47.81251 | 2025-10-29 04:21:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f71836b6-1ab9-3271-bf4d-c5f22512587d | -3.38141 | -49.96204 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README26.md)
