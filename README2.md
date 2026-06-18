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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3658a0b9-b386-3abf-97ab-26ee0e29749c | -9.4387 | -40.3419 | 2026-06-18 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 116.6 |
| eed7b233-7c86-3f93-b4b4-adbbc51fd3ac | -13.2066 | -50.3492 | 2026-06-18 00:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 29880a33-2ca8-317d-a949-cf4b7b2261c9 | -10.98642 | -47.76013 | 2026-06-18 00:43:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e5963ffb-5de4-3e99-a586-06a23f1110cf | -10.99331 | -47.75365 | 2026-06-18 00:43:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 79f9b411-446c-3732-bfa8-ddc45888db94 | -10.91341 | -56.84684 | 2026-06-18 00:43:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b6448fab-7360-3133-9307-2f0ef7ec378b | -10.15389 | -56.61275 | 2026-06-18 00:43:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6178740e-f3b2-37b0-82ef-c28681b6354f | -13.20033 | -50.35884 | 2026-06-18 00:43:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 27cf64b5-bb20-36e1-851c-d20587158627 | -10.15517 | -56.62185 | 2026-06-18 00:43:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6c9cb240-02a5-3bb4-9592-af1765d3457d | -9.20999 | -47.9371 | 2026-06-18 00:43:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 9ef26aba-1f49-3594-8842-051240c47ab4 | -14.09756 | -59.45433 | 2026-06-18 00:43:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f1cbd00c-0951-30f0-a2e6-fd8c985e696f | -12.46609 | -55.12286 | 2026-06-18 00:43:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a5012dfe-12ba-3c54-82c9-fccd54b34dfa | -15.0724 | -55.81735 | 2026-06-18 00:43:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2b148ed3-ee6c-3a73-912a-565b27cac265 | -14.0893 | -59.46661 | 2026-06-18 00:43:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 18f1bd78-d958-3207-938f-dabb795cd1cf | -13.19702 | -50.33889 | 2026-06-18 00:43:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 19d86318-c6e4-3c19-a73a-240b46c30592 | -11.8089 | -52.52322 | 2026-06-18 00:43:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 4bb6f9f1-c740-3cf6-97b2-749536f7cf19 | -15.64681 | -58.01318 | 2026-06-18 00:43:00 | TERRA_M-M | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 49296a46-c8d3-3edf-85a6-f81122d841bc | -15.64808 | -58.02291 | 2026-06-18 00:43:00 | TERRA_M-M | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 70f452b3-6d0f-3624-9271-90cee2250e40 | -12.20623 | -52.7802 | 2026-06-18 00:43:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| ce340ac9-8307-3da2-8499-a9825f34ad94 | -12.46754 | -55.13277 | 2026-06-18 00:43:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 908d6f1b-8ea2-3860-81d7-2ffc0d338754 | -14.09898 | -59.46534 | 2026-06-18 00:43:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 2b97e696-176c-3de5-afc4-0dde8fef6eba | -10.91467 | -56.85584 | 2026-06-18 00:43:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| e9627eb1-4f62-3e6e-977e-b093519467d8 | -14.08789 | -59.45559 | 2026-06-18 00:43:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 47c37951-c6de-3569-a183-6bba874445a6 | -6.57333 | -51.11616 | 2026-06-18 00:45:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 75234e9f-8f89-3190-9ffe-408999ca4e8a | -10.2798 | -60.54613 | 2026-06-18 00:45:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 63648b1a-7a81-3a58-996b-061fc6dbf997 | -7.83367 | -55.39535 | 2026-06-18 00:45:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0e1ad320-b7d2-3bad-8fb8-dc663d7fef9d | -7.83518 | -55.40591 | 2026-06-18 00:45:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| dafd6e5a-e81c-3e1d-9a10-787721f2f9da | -9.4387 | -40.3419 | 2026-06-18 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 334.5 |
| 4362a8e0-c408-3432-a8e5-da3409e777d7 | -9.42 | -40.3198 | 2026-06-18 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 184.8 |
| bf84b5af-27fb-3453-9aa5-66997475bccd | -9.4196 | -40.3447 | 2026-06-18 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 227.9 |
| 95bf7af3-a57f-38ed-a20c-d28d8995ac9f | -9.2152 | -47.9241 | 2026-06-18 00:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 0d2fc7d6-938d-36d1-a1a4-75ed95342358 | -10.9164 | -56.8536 | 2026-06-18 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 2d3e1dbb-b36f-3948-912b-1f95f1fc0cdc | -4.3588 | -47.7636 | 2026-06-18 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| cebcb359-b24e-3601-884b-fb89c6989da0 | -12.8354 | -44.3657 | 2026-06-18 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c13346b1-2ce3-393f-be16-cf1315e65ce0 | -9.4391 | -40.3171 | 2026-06-18 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 253.2 |
| 9c0cd5ca-6d62-32c9-a31f-af3def97a92a | 2.58785 | -60.69674 | 2026-06-18 00:50:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1f43ce28-0c32-3ff2-91f7-2984d352db3e | -9.4196 | -40.3447 | 2026-06-18 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 502.4 |
| d2a44d12-142f-3cfc-aaa6-fed0e2066332 | -12.7741 | -44.5396 | 2026-06-18 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 1fd80ea4-abb1-30c8-a0b5-b17430d60142 | -9.42 | -40.3198 | 2026-06-18 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 527.8 |
| 87d70f57-9eaf-35c2-b2be-b231f7cdb746 | -9.4391 | -40.3171 | 2026-06-18 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 712.3 |
| 75dc6282-a144-356d-a277-ea6c79e52aaa | -13.2066 | -50.3492 | 2026-06-18 01:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| a57a6a4b-9902-3f18-bdda-d37e2c347376 | -10.9164 | -56.8536 | 2026-06-18 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| d7662c90-5a4c-36f7-8135-72eacceb7bbd | -7.7176 | -44.1611 | 2026-06-18 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 138.7 |
| e03ef46f-9c97-3e25-a54f-e8b6e774090b | -12.8354 | -44.3657 | 2026-06-18 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 16d4dbfb-bcb3-3700-981d-c1f73d33e19c | -4.3588 | -47.7636 | 2026-06-18 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| c90733f5-aa48-3966-93d0-908c7a21fe12 | -9.2152 | -47.9241 | 2026-06-18 01:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 37fbf390-8e5a-3e82-bc3a-b5935e4874cc | -9.4395 | -40.2922 | 2026-06-18 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 589e9850-fea2-3c39-bbff-92f8100253b9 | -9.4383 | -40.3668 | 2026-06-18 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 1a395034-088e-36db-9125-43877b51edec | -9.4387 | -40.3419 | 2026-06-18 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 658.8 |
| 44b649e8-d072-3759-a8ca-9a884fd3a778 | -7.724 | -44.138699 | 2026-06-18 01:03:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e6af273f-c34c-30af-ada1-523b0c5a856c | -12.2125 | -52.7686 | 2026-06-18 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03fca9ed-18bf-3c1f-b4b3-e2f1ebfdf947 | -10.9907 | -47.738098 | 2026-06-18 01:03:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b11aa454-ef1a-3d60-a561-ae648df5348a | -7.7144 | -44.141201 | 2026-06-18 01:03:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0671989f-5c27-3718-ad5f-2024f57c4e09 | -8.088 | -48.307701 | 2026-06-18 01:03:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38c84d9d-d282-331e-8488-2d1c56afc92d | -10.1538 | -56.615101 | 2026-06-18 01:03:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f320492c-5fe6-33c2-a852-be8972b7bb46 | -8.9836 | -47.968399 | 2026-06-18 01:03:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95bb7938-71fc-3c7d-a54e-56f5b533709b | -15.071 | -55.8078 | 2026-06-18 01:03:00 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 381cae45-5ea0-311c-abdb-4a87469a2b21 | -10.1554 | -56.622601 | 2026-06-18 01:03:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68ef01b6-db06-3558-8b25-59ec40d2fe14 | -7.3731 | -49.8591 | 2026-06-18 01:03:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dca4765-42ee-3cae-9c55-43f12bb392a9 | -13.2017 | -50.342899 | 2026-06-18 01:03:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cd452d3f-19bd-3c5a-a604-813912abfb2b | -12.4664 | -55.121201 | 2026-06-18 01:03:00 | METOP-C | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 378f7851-80ed-3a3f-ad37-43425e50b1d3 | -7.7309 | -44.165298 | 2026-06-18 01:03:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ea85bcae-4ab0-3746-a3c8-f75724229824 | -12.7775 | -44.5326 | 2026-06-18 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57afef25-2f28-346d-8a91-76c230d650b5 | -10.9152 | -56.8549 | 2026-06-18 01:03:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6914de2b-ab1a-30af-8314-39ce9597a816 | -12.2158 | -52.7831 | 2026-06-18 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f2f8a29-04af-32c8-8152-17d881179e13 | -11.8152 | -52.523499 | 2026-06-18 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37a6a6b8-31be-3508-b8ce-9c541d3e81fe | -13.1995 | -50.334099 | 2026-06-18 01:03:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 74c6fd38-1e97-34c1-a63b-dc14389f6742 | -11.8134 | -52.516102 | 2026-06-18 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47543816-63ec-3865-9b69-a3f4754fc587 | -12.2044 | -52.778198 | 2026-06-18 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 372e42b2-8d24-3f29-958c-12f6aec168d0 | -12.772 | -44.512001 | 2026-06-18 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91243d18-572c-32e7-8644-51669ec9f73e | -10.1521 | -56.6077 | 2026-06-18 01:03:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ea5809a-a983-3dff-bfea-f0ed0d87efff | -7.7213 | -44.167801 | 2026-06-18 01:03:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 60b7629c-4721-33bf-9d9d-4d7ff43a7994 | -12.7679 | -44.535301 | 2026-06-18 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25210d04-0bae-3339-8a17-c05edabd07f9 | -13.2114 | -50.340401 | 2026-06-18 01:03:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1a3be388-e624-3ea0-a0a1-8deb192a3b46 | -7.834 | -55.4006 | 2026-06-18 01:03:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 128f256c-1939-3a00-acfa-26c6ef634e90 | -13.2038 | -50.3517 | 2026-06-18 01:03:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec52541b-c53a-3d11-b29c-ec8c08ff4442 | -9.2299 | -47.9216 | 2026-06-18 01:03:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 117f5a33-a5f8-34d3-add1-a1171e29cde6 | -9.2167 | -47.910099 | 2026-06-18 01:03:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4bc0a49-4ea9-3056-ae38-1c5f733d4750 | -7.6116 | -46.4753 | 2026-06-18 01:03:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad99cb2b-0871-3812-b1ed-2f172b33dab2 | -11.3566 | -55.823101 | 2026-06-18 01:03:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9b9cac1-57f8-3241-8ae1-8846a56e52d9 | -9.2202 | -47.924 | 2026-06-18 01:03:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ba16d9c-e960-3f2c-b77e-0f6f332540b0 | -13.2093 | -50.331699 | 2026-06-18 01:03:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 660ae139-f2ad-3029-b5c9-fdf8bbfeeb1c | -14.0925 | -59.471199 | 2026-06-18 01:03:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4650d4c-d0b4-3796-ae92-159c64725e56 | -12.8501 | -44.378502 | 2026-06-18 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b40964cb-af23-3dcc-9aad-9c96b1af298d | -7.6019 | -46.477699 | 2026-06-18 01:03:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59f5488c-99d3-3daa-97dc-779481870683 | -15.6589 | -56.1633 | 2026-06-18 01:03:00 | METOP-C | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64e46cad-c014-3519-b33d-dd57ed9b91b0 | -12.468 | -55.128399 | 2026-06-18 01:03:00 | METOP-C | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3285e1f3-2486-30db-8f12-8dd9f71ebaa7 | -10.9135 | -56.847099 | 2026-06-18 01:03:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85f9bd69-153b-3f4c-9d7a-038555ad2dd7 | -15.0727 | -55.815601 | 2026-06-18 01:03:00 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6978c96-5585-33d3-b0cb-2dc23680cd2c | -12.8348 | -44.360199 | 2026-06-18 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 157cc703-5e43-35a6-83c0-b2415dead273 | -14.0901 | -59.4594 | 2026-06-18 01:03:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dbf6c8f6-3d64-3e6c-baf9-559acfec12e8 | -12.2142 | -52.775902 | 2026-06-18 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e508c7b8-421b-351e-8cbc-7b4c802d1098 | -7.3634 | -49.861401 | 2026-06-18 01:03:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a0386d-05ec-3352-9d4d-2812cd72a66a | -12.8445 | -44.357498 | 2026-06-18 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a582ef5-427e-34b9-b99a-121ff97762a4 | -10.994 | -47.751598 | 2026-06-18 01:03:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1916ac45-0588-387e-a0e3-d62885ff1eea | -10.9168 | -56.862598 | 2026-06-18 01:03:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ccf6f8c-d768-36e6-aaed-e21c3db2613a | -12.0787 | -47.543999 | 2026-06-18 01:03:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b703fb08-e573-3c65-8e01-19a317d12865 | -9.2236 | -47.937901 | 2026-06-18 01:03:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9ab9f9f-a236-3e9e-a31d-54fd0b6b5739 | -12.2027 | -52.770901 | 2026-06-18 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f70aaff2-68c0-3d5f-ba35-c1054da3e9fc | -9.2152 | -47.9241 | 2026-06-18 01:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 53e8da57-2bb0-3ae5-b450-166c18c7beb8 | -9.4395 | -40.2922 | 2026-06-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.3 |


[Clique aqui para ver as próximas entradas](README3.md)
