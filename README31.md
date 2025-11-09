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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51955f0c-0f82-370f-a888-a89cb4ea64c0 | -5.65403 | -45.98905 | 2025-11-09 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7a7294c2-837e-3afb-b9cb-e26c15131ece | -3.80413 | -46.00052 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44dc9b74-741d-39de-a6dd-38d73a2499a2 | -3.30618 | -50.2248 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c78850a0-bc28-30fb-85b5-88b54e989330 | -3.84831 | -47.40281 | 2025-11-09 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2b289f01-27ca-32c6-80d6-9c6742c3e86f | -3.07434 | -49.37944 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 06967d8e-bf28-3550-b4ba-edf811f2dfa0 | -2.60175 | -49.23053 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6370409-9b2f-31ce-b572-14c409997dc3 | -3.03246 | -50.30851 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6722ea19-7c5c-3259-a2d7-7b9dda16ab89 | -3.8347 | -51.12437 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f73d89be-f8d2-3802-9a2d-e5881d0f4723 | -4.26821 | -45.53802 | 2025-11-09 04:38:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b63c8833-90e9-3014-8ec6-574a41c5e861 | -6.17469 | -44.38755 | 2025-11-09 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6de2151b-fda2-38e4-a6be-0a63508ff3ce | -3.31325 | -50.1269 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c96a0315-4cd9-36a9-86cc-10a3cc5b83cf | -3.43594 | -50.24536 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 016290d0-c910-34c0-8578-5bdc592870af | -5.29155 | -49.50015 | 2025-11-09 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f605c030-73c4-3e02-a811-c84df782b8e3 | -6.04348 | -57.96239 | 2025-11-09 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5462109-cb90-37ff-a751-7a56f92552f3 | -4.23318 | -48.6058 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb0fc881-be38-37e9-8d54-450dbff53e0f | -3.29182 | -50.19699 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d8bdbd1-e7e0-3225-88c6-613d97d367a9 | -3.4114 | -51.56724 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5df1ca5a-8641-3833-ab4c-6b8c4bd80564 | -7.14078 | -46.41362 | 2025-11-09 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a375fca9-ce54-3add-bc3d-891dcd767c90 | -3.91007 | -49.76795 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 202f5933-9827-3414-878c-459b10b3a838 | -10.33117 | -49.64176 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c405c7b9-76fa-31fe-b4f5-5b4c2e51b12f | -9.62587 | -48.88805 | 2025-11-09 04:40:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c126ece-8872-34c2-914e-07493b8a63d1 | -11.73099 | -44.6636 | 2025-11-09 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0305488c-064b-3cba-8bab-3ab328b05b86 | -12.10644 | -43.64724 | 2025-11-09 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01fd7f14-05f6-33ec-a051-bd5bbef8d506 | -11.01813 | -49.34994 | 2025-11-09 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee4834b7-fa63-3cad-a982-6b61a95a5247 | -9.05425 | -48.83609 | 2025-11-09 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1d7dd2c-ae5f-36f1-b881-88dae6fb944b | -10.32895 | -49.63419 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16ee24c9-b17e-3ddb-88a4-16b8d3742051 | -8.90014 | -47.90449 | 2025-11-09 04:40:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b17029d0-4980-30e8-9793-4dde411d7d47 | -11.95062 | -46.25216 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2f89ea99-b518-36f0-bce9-fcb2c6b89a7a | -9.32734 | -47.84024 | 2025-11-09 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c10ff919-e8c3-37c6-b053-c5c04185761c | -11.94329 | -46.23888 | 2025-11-09 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99c8a4f0-2b93-3da7-8d8b-0e204a71026c | -10.33504 | -49.63877 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56575cad-24e2-3ad1-a49c-c9ce606a8469 | -10.33172 | -49.63824 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b87492b-b82c-3421-a5d4-98d4d10f7965 | -10.34388 | -49.62573 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36d77686-3285-3753-a80e-d6840114bc12 | -8.35792 | -49.94239 | 2025-11-09 04:40:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d2be6c4-17c2-3763-9fff-5c1ef13afce5 | -10.33614 | -49.63172 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19986514-8c97-31ab-b17c-076b1ae4b7b4 | -11.94675 | -46.2516 | 2025-11-09 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a23cad4-cb0c-3f16-9af9-bbd39f0e987f | -10.7169 | -47.74155 | 2025-11-09 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40567d4c-558e-3a29-8da2-4d21970728bb | -11.61947 | -48.50542 | 2025-11-09 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65868bef-b40e-3b09-8db1-35602a4baf7b | -8.44969 | -48.10471 | 2025-11-09 04:40:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8666ffcf-c975-3872-9d1b-c689eab9b43d | -9.14132 | -51.29237 | 2025-11-09 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4560b84-609e-37a1-8c0a-410ddf44bd7b | -11.73371 | -43.84645 | 2025-11-09 04:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74bc45ac-9650-3f9a-a936-728db5c108d5 | -11.55077 | -48.54614 | 2025-11-09 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| add65245-55f5-3504-99b3-6735f07722ff | -10.33227 | -49.63472 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e3bb45d-7e3a-387c-9873-93d56744166a | -8.71212 | -46.72694 | 2025-11-09 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6c9610f-15fd-3848-b1b6-301a5a9d4cd4 | -10.33946 | -49.63225 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a21dda65-336b-39a7-8900-6945c4939f67 | -11.01758 | -49.35353 | 2025-11-09 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f48d584e-a5bd-32bc-8b05-202854bc899e | -8.91727 | -47.81416 | 2025-11-09 04:40:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d112541f-36ae-3cc8-8349-c249aeb5bdf0 | -9.34541 | -48.99432 | 2025-11-09 04:40:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f180195c-e716-3524-b4a2-e35a21fc957f | -10.76725 | -48.84043 | 2025-11-09 04:40:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d75491ae-2f4d-39ac-accf-70dfe92db211 | -10.33449 | -49.64229 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87925c04-4aa7-306d-9e3f-de0e330333b9 | -9.47233 | -48.74249 | 2025-11-09 04:40:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c9823de-ce22-3ea5-99e7-c1a68c68f3b4 | -11.55019 | -48.54994 | 2025-11-09 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9afb917-1775-32ce-addc-7cced5dd7618 | -9.3297 | -47.83918 | 2025-11-09 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3af68ba3-f642-3232-a8df-21df4f1f74c2 | -11.94494 | -46.23615 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 875beecf-a178-3b0a-99f7-7dc3dc2085ef | -10.17191 | -49.31297 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23736cde-5fca-367f-a5ea-adf576bdf2fd | -9.47514 | -48.7466 | 2025-11-09 04:40:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74b23c4c-8793-3576-a894-9298e042065b | -10.41592 | -48.80511 | 2025-11-09 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 99e97e78-62c3-30cd-95cb-2335fe88b335 | -9.37803 | -47.07716 | 2025-11-09 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbfd4c50-5170-3c1b-9d26-2dc2433e3402 | -10.34001 | -49.62873 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64b44ae6-4e9e-32a5-94eb-fdac3bda7f70 | -11.39693 | -47.64032 | 2025-11-09 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b369788c-0773-3d41-8705-cd37c0a76af6 | -3.3369 | -44.3806 | 2025-11-09 04:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| b577afbe-7a80-3ada-9b74-89989d5e3db9 | -11.9513 | -46.2472 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e129b886-7443-3387-993f-4690722804d5 | -11.94643 | -46.24449 | 2025-11-09 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 22127ce9-35c7-3bc7-af71-225adc6c5fa6 | -11.94958 | -46.24997 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| adc411c0-462e-385e-9356-c6b66d3d29ef | -9.51546 | -47.27163 | 2025-11-09 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6bc6298-c5e6-370f-934d-6ef84aa83429 | -9.47569 | -48.743 | 2025-11-09 04:40:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ec99802-c550-31fa-9dae-ee987c2e8cae | -10.3284 | -49.63771 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 012e8d7a-9020-360b-bca6-3d2d28af9c41 | -10.33559 | -49.63525 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a4df7a1-c5f1-3b15-a920-f7b499d5944b | -9.09377 | -44.32272 | 2025-11-09 04:40:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8752cd35-83d6-327b-8478-10f09d1266e9 | -10.71336 | -47.74109 | 2025-11-09 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 127adeda-ec22-3cb3-9f3d-36ba5eeb04fd | -11.95199 | -46.24225 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c9ca163-9d9e-3453-bb94-33278e305942 | -8.81962 | -50.05175 | 2025-11-09 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34f8061d-a7b9-36c8-b119-e147310ce95e | -11.94812 | -46.24171 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c77f27fe-d67e-3798-aa5c-7965d55abf9a | -8.44629 | -48.10418 | 2025-11-09 04:40:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80e06104-c547-335b-9c14-fdbc7bb54482 | -10.65333 | -47.92693 | 2025-11-09 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a43d0d6-0d22-3604-acc9-31c87535e4bd | -8.84187 | -48.19765 | 2025-11-09 04:40:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e1ee2a0-b1c8-328b-8daa-fcc06d8b379e | -10.34056 | -49.6252 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a316993-abd9-3027-bb58-ad31db37e506 | -11.73045 | -44.66772 | 2025-11-09 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48d2d731-7322-3d52-a511-e6ed0440cd7b | -11.95449 | -46.2527 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6fd8380c-9d15-3894-82a5-a1e80a9dd41d | -9.04 | -48.5947 | 2025-11-09 04:40:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea1d75b0-ec23-3754-b1eb-1a95401a2a58 | -9.95463 | -48.58866 | 2025-11-09 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e814ebc-d61e-3118-8c2a-2c3421423583 | -14.41362 | -43.1879 | 2025-11-09 04:40:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2d28ac2-ff15-32d2-9a51-6956d165c5b8 | -10.33891 | -49.63578 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 421c178d-019c-3192-82f0-31f2ad4e9353 | -10.77615 | -48.7141 | 2025-11-09 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46dc9f37-85ff-3da1-a0b2-e0ecd387e765 | -10.06397 | -44.31788 | 2025-11-09 04:40:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9764edd-2dd5-3ae3-a362-9de98d5a1498 | -10.35929 | -47.33146 | 2025-11-09 04:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8627dff-1921-3f6e-ac73-c42c89b0400c | -10.33669 | -49.6282 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b28e8b0-a51d-3ffa-997e-32805dd6d4a1 | -10.33282 | -49.6312 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6869e4aa-cb2f-3be8-8c4d-bb381e01dad3 | -11.6166 | -48.50108 | 2025-11-09 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac8aceed-5b7c-3655-9436-4787c38241c8 | -11.94715 | -46.23953 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75395876-cb5a-3ea1-a574-eb36c37f90a4 | -9.37741 | -47.0813 | 2025-11-09 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5edc405-5189-3aa8-92d6-bc94914e08b5 | -10.89779 | -49.13556 | 2025-11-09 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b42ebe37-ebd2-3671-8797-55e95517556a | -9.94861 | -49.19767 | 2025-11-09 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b59d5142-03bf-34b4-a458-a5ea36aa40a0 | -11.94426 | -46.24108 | 2025-11-09 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1f40277-3b6e-33f6-9187-71cb58a0ee30 | -10.72043 | -47.74202 | 2025-11-09 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e6f26d8-798d-38b9-a6ea-824c975ddb77 | -12.11105 | -43.64789 | 2025-11-09 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cde34075-ba25-393d-a038-31e4f293b7ba | -10.33836 | -49.6393 | 2025-11-09 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05b67da4-99a2-3f0f-a44f-24cad4dfb536 | -11.46 | -48.65993 | 2025-11-09 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ce8228b-e6ee-3615-98f3-4f77ee0f7611 | -11.94743 | -46.24667 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfa332ab-ccd0-3223-bd70-d30ab6f23afe | -11.94886 | -46.25491 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |


[Clique aqui para ver as próximas entradas](README32.md)
