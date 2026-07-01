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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d429163-1549-3e09-bca4-6fa8dd7bbf3e | -10.7654 | -53.5451 | 2026-07-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c64a3d98-f63f-38e5-bfd2-766fae4211f2 | -6.3142 | -47.5386 | 2026-07-01 15:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| af78558d-4a05-339a-b79c-88cf9f3fe1d2 | -11.4147 | -56.0726 | 2026-07-01 15:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 4edda31d-e166-3db8-a217-0b079052b21a | -10.6596 | -54.5372 | 2026-07-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| d3d9768c-6492-3458-bfb0-6642accfa6da | -10.8485 | -45.0595 | 2026-07-01 15:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 91d4c828-cbf0-3afd-b81c-b2bead5ea7ef | -10.4387 | -49.6005 | 2026-07-01 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 83b7ae56-43df-3333-b21d-920202c11f34 | -10.6787 | -54.5153 | 2026-07-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 1d659c63-0497-3dbc-9fed-1a2b3fb482fe | -10.6784 | -54.5356 | 2026-07-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 189.3 |
| b7547c61-0ff1-3bbb-bd39-b4ae0c8f92e3 | -10.1237 | -52.0905 | 2026-07-01 15:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 5e9c861c-7eeb-3f9f-a0ae-4f2c8052de8f | -11.4149 | -56.0525 | 2026-07-01 15:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 166.2 |
| 6890f19c-3afe-3caf-a9b9-f512dd5f66be | -11.4338 | -56.0509 | 2026-07-01 15:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 3b6eb458-86da-340d-9a6d-91d2dc4a247c | -9.1833 | -58.0584 | 2026-07-01 15:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 093c0304-b975-35da-837d-290f16d8a581 | -17.712 | -46.7798 | 2026-07-01 15:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| fcf1614b-4ce0-39d1-a72c-fd4957d7d2db | -10.6598 | -54.5169 | 2026-07-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 944c1283-99b5-37f0-9aa6-c83ea87df703 | -10.439 | -49.5789 | 2026-07-01 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 12491d38-f9aa-3a33-8793-b0df04b306dc | -10.7843 | -53.5434 | 2026-07-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| de2df112-2f59-3414-9fc8-079a993a03d3 | -9.202 | -58.0573 | 2026-07-01 15:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 820eab44-38bd-3865-a88b-70b1c232b35d | -10.6596 | -54.5372 | 2026-07-01 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 0f310945-7b99-3a1e-af23-736143addc1d | -10.6598 | -54.5169 | 2026-07-01 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| e1447b32-0eba-36eb-9e29-b40beaea7b89 | -10.6787 | -54.5153 | 2026-07-01 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 47738b85-7443-3ad4-9832-95adbf29a534 | -10.1237 | -52.0905 | 2026-07-01 16:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 16733df4-a330-3dba-a0d4-f4390f4ee585 | -11.4149 | -56.0525 | 2026-07-01 16:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 10a88207-838c-3168-9cfd-bdb4ee128ba8 | -10.6784 | -54.5356 | 2026-07-01 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 9900eb03-5ce3-3e0b-a48c-c03313a50408 | -9.202 | -58.0573 | 2026-07-01 16:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 21c08b5d-5e0d-31ac-a4ff-491f0036c28a | -6.3142 | -47.5386 | 2026-07-01 16:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a9c4d9cd-e30c-3c40-a405-70472497b9f5 | -10.439 | -49.5789 | 2026-07-01 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 9d5c6126-b07c-3387-aeb4-84bb2af61e39 | -10.7654 | -53.5451 | 2026-07-01 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 45914582-23cf-3d83-87b3-fdd57cf1f790 | -6.3144 | -47.5167 | 2026-07-01 16:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 38e7e028-b2b3-3ba9-b0a9-ce6d59ee29e6 | -10.4387 | -49.6005 | 2026-07-01 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 74f0c284-1df6-3abf-8220-713b8e5b1ee4 | -17.712 | -46.7798 | 2026-07-01 16:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2ab1fe15-950a-3fd8-8571-23856d0ed6a9 | -10.7843 | -53.5434 | 2026-07-01 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| c64bcf5f-2f1f-38cf-9be8-a15bea52693f | -10.8485 | -45.0595 | 2026-07-01 16:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| e25a982d-58ee-3691-a0e7-dcd20f9ed07c | -9.1833 | -58.0584 | 2026-07-01 16:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3b597794-f193-3000-b39f-6f6b7f09b8dd | -11.4338 | -56.0509 | 2026-07-01 16:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 1c051300-29b9-39bc-bed8-66e8f2c4f982 | -10.7654 | -53.5451 | 2026-07-01 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e6013d5d-2e29-3691-87ef-d586c48f68e1 | -10.4387 | -49.6005 | 2026-07-01 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 58287a79-292d-3459-9778-86a7b7a46271 | -10.003 | -54.4287 | 2026-07-01 16:10:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 512a0474-1b82-3e17-b21b-7a541629126b | -10.6598 | -54.5169 | 2026-07-01 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| afb24b6a-d94e-30dc-b967-24a65f01b17f | -11.4336 | -56.0711 | 2026-07-01 16:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 154.0 |
| fa985103-9115-3360-a3e2-b3ef0e99638f | -10.6787 | -54.5153 | 2026-07-01 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 8fcd8742-b90b-377d-b6e3-f074696f06da | -10.7843 | -53.5434 | 2026-07-01 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| deb411f6-4b15-3615-8546-98ff11003b08 | -11.4338 | -56.0509 | 2026-07-01 16:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 4a69c88e-4667-3222-8470-b878c70be8e3 | -10.439 | -49.5789 | 2026-07-01 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| e2602bf0-6f01-3f2e-9512-c284505df7fe | -10.6784 | -54.5356 | 2026-07-01 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 8ed35b53-391f-3da7-a792-8aca5c360c0a | -10.8485 | -45.0595 | 2026-07-01 16:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 13e3cc91-940c-3141-8706-53d7e0c5297e | -9.1833 | -58.0584 | 2026-07-01 16:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9a2f775b-b775-33ce-bac8-08daf769f087 | -17.712 | -46.7798 | 2026-07-01 16:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 2327e971-37cd-3e8b-a8f6-984d3ae3009c | -11.4149 | -56.0525 | 2026-07-01 16:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 142.1 |
| c11fd8bc-5434-360b-887f-292f96579ed7 | -10.6596 | -54.5372 | 2026-07-01 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8ed62902-4ce7-34b9-989d-32018a107584 | -11.4149 | -56.0525 | 2026-07-01 16:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 0dabe84d-866f-3f9a-9ee9-ac0181f70a9d | -10.6598 | -54.5169 | 2026-07-01 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 46c7e6bf-8575-3361-be95-e5bc03812887 | -10.6596 | -54.5372 | 2026-07-01 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 0e81ccb2-69eb-32a4-b154-fc3f89666399 | -5.4925 | -43.2165 | 2026-07-01 16:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5dc5520e-2026-33a4-bef7-5c4626490a4c | -11.9108 | -43.4081 | 2026-07-01 16:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 6da81ce4-cd33-3158-932d-6a3d61780fd7 | -10.6787 | -54.5153 | 2026-07-01 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| af94d656-b045-3b34-9afe-1bc45f9042eb | -10.7654 | -53.5451 | 2026-07-01 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8554a68a-0d14-336c-9286-5326200622d6 | -11.4147 | -56.0726 | 2026-07-01 16:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 2d66a25e-e3e9-3342-84aa-f2c1baf43c92 | -17.712 | -46.7798 | 2026-07-01 16:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 89.8 |
| b36c4659-b1e4-359a-98f8-1fdcace6f7c4 | -11.4338 | -56.0509 | 2026-07-01 16:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| f42db72f-bc52-3c1f-8c16-6f660235537f | -10.6784 | -54.5356 | 2026-07-01 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 82b8d068-0378-34b9-be07-2725a0ef1233 | -10.439 | -49.5789 | 2026-07-01 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 72d61703-7b85-3536-8b28-b2d7df6dacd9 | -10.8485 | -45.0595 | 2026-07-01 16:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| ad040043-5873-3f22-bc4c-064e4f18d347 | -10.4387 | -49.6005 | 2026-07-01 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4d684638-1dfe-32fe-b6e9-65b8b2bd1adf | -10.7843 | -53.5434 | 2026-07-01 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| b5706900-7cc9-39f3-b5da-e7d5063dedcb | -3.8671 | -42.9685 | 2026-07-01 16:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| b3aa5017-dd41-3b12-9290-1342e67908b1 | -6.3142 | -47.5386 | 2026-07-01 16:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6ba54842-d900-32f1-9415-2eaac288753f | -11.4149 | -56.0525 | 2026-07-01 16:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 121.9 |
| f495dd28-e906-384e-b636-75369f0ef032 | -10.8485 | -45.0595 | 2026-07-01 16:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| bace2c66-3cd1-35fa-aa27-b2732d36e399 | -17.712 | -46.7798 | 2026-07-01 16:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 6ac9c4b4-4e33-3d92-b780-284035cc8498 | -10.7654 | -53.5451 | 2026-07-01 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a02d99ba-51ac-3b1f-b728-39d51f92679a | -10.6596 | -54.5372 | 2026-07-01 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 062b6e40-0674-356f-bd5a-d313333cd8de | -11.4338 | -56.0509 | 2026-07-01 16:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 193.3 |
| 24d74f00-33de-3d03-87e9-c59d26af8598 | -10.439 | -49.5789 | 2026-07-01 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 6381892f-5059-3801-be7f-c23cd05f53a8 | -10.7843 | -53.5434 | 2026-07-01 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 0f48f3e6-a18e-348b-b633-f328c63bd810 | -10.4387 | -49.6005 | 2026-07-01 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| dbf815e4-8f92-39f1-b8ba-8979e4e2cca8 | -10.6787 | -54.5153 | 2026-07-01 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 58bd5377-be39-3f78-9ba1-217fdb56ac60 | -12.1574 | -57.2335 | 2026-07-01 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 37d06bf0-9976-3f17-81a0-105e9591e08a | -11.4147 | -56.0726 | 2026-07-01 16:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |


