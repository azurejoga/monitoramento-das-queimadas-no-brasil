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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8420b69-e556-3d5b-81d5-ba26906f1108 | -10.05687 | -49.66457 | 2025-06-05 04:59:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4108637-c9cc-3bb9-ae2a-c362cb9cd879 | -12.06422 | -47.333 | 2025-06-05 04:59:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be6eaa20-27cf-3fe9-bcc3-7aace4eb5edb | -11.37904 | -55.1137 | 2025-06-05 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5fc4a8c-cf47-3835-91ad-cce8b3dfcd82 | -7.2123 | -43.12955 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93ebdfaf-73fb-3bad-846d-1f6ad6ebd3e2 | -11.14257 | -53.94126 | 2025-06-05 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e5813f6-daa5-3763-ad70-c9a6c28e110d | -10.50033 | -53.65117 | 2025-06-05 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2389c8ee-3f3c-316a-ba57-97641b4a9d67 | -7.69976 | -45.78255 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85d1532e-1a9c-39ef-b89a-c1dcd9ffed8f | -9.24273 | -63.2959 | 2025-06-05 04:59:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d7879a3-3cd1-3c91-b100-38126db778ab | -12.45858 | -48.9812 | 2025-06-05 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23275468-5bb9-390f-ba3e-700e90dab1e1 | -8.7225 | -48.01591 | 2025-06-05 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83711c31-10af-3ac3-90aa-e7f85e25a8a3 | -10.69471 | -57.6457 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df6e5f30-db0a-3acd-b54b-9fa2e56fe15d | -10.50316 | -53.65537 | 2025-06-05 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c76ab18-f7c2-3812-9a85-df035a6b5aeb | -8.95491 | -47.28217 | 2025-06-05 04:59:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed24d82a-3150-339f-a962-a60690e7c6ee | -10.71037 | -48.7827 | 2025-06-05 04:59:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de9b9a04-24a4-303a-b93d-420c184dc118 | -9.22259 | -48.85015 | 2025-06-05 04:59:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cf46a66-3351-3841-b1d6-9bac6c371a8c | -10.65587 | -49.43837 | 2025-06-05 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 248a0596-d2ce-3126-a242-0a09de92668d | -7.8188 | -55.37765 | 2025-06-05 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f975a8a2-728c-32b0-9be0-d594e7d4c6c1 | -7.19257 | -43.13612 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 46302bfc-1ae0-3e57-84ee-9ed9ce7fc423 | -9.70971 | -57.87886 | 2025-06-05 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58ecbf02-b506-3749-a334-4046717a9337 | -10.2929 | -57.14237 | 2025-06-05 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10504abf-cf28-31e3-be7a-4883fff01809 | -10.94472 | -55.33218 | 2025-06-05 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91835484-63c0-39f6-bc03-2dca919a9744 | -10.49976 | -53.65485 | 2025-06-05 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1713da48-275b-334a-bc3b-39936130f68c | -10.70593 | -48.78205 | 2025-06-05 04:59:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9eae58e4-1b3f-393a-9c73-a503528b6887 | -11.55504 | -47.61951 | 2025-06-05 04:59:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7d47efd-76e7-390a-aae8-ad67d4898123 | -7.61841 | -45.75393 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27a9785c-2646-3ab1-8c33-bdb4e68509b4 | -10.29696 | -57.13913 | 2025-06-05 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 704b7d1c-a885-33da-8ac5-abe7af3a76ee | -10.68507 | -57.59584 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a7a37aa-bd3b-3e2b-8b4f-97cbcbef50b8 | -7.21239 | -43.13532 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2f9fcf59-ee12-376e-bd9d-fe97f07dcee5 | -8.72697 | -47.98382 | 2025-06-05 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fa68628-a744-3202-949c-41954b6e7643 | -7.01197 | -44.60326 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 526c8d87-78b1-31ff-a7ce-0908b9992555 | -11.43328 | -54.09053 | 2025-06-05 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 22e84e4b-6d54-34e9-bfce-aa33bdeb2dc4 | -6.97923 | -47.08522 | 2025-06-05 04:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3a2cb49-a878-3b18-aa02-8a892ae116cd | -8.46002 | -46.47865 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13b379f5-01a3-3823-b12d-9c4ddc76f943 | -7.53911 | -45.82885 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0ce3a8e6-88fb-3cfb-8f6a-3002b74e4135 | -10.30041 | -57.13971 | 2025-06-05 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f7cdb89-1521-3c7c-a26c-45a2da07bf6e | -10.4924 | -53.65746 | 2025-06-05 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05b71538-12c0-3819-a945-62cfbe036fe7 | -13.5346 | -56.5469 | 2025-06-05 05:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 15d5db02-07ff-3cc7-a7d8-80811e76ab8b | -18.8479 | -53.6251 | 2025-06-05 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 73226204-e1d3-357a-8efb-9aadd26606f5 | -13.5155 | -56.5488 | 2025-06-05 05:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f0b42a44-24a4-3d41-afa2-63b822253593 | -13.5344 | -56.5672 | 2025-06-05 05:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 921ea7ab-5b62-3586-9e3b-d3e5d4202f70 | -13.515 | -56.5893 | 2025-06-05 05:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| f618149c-b6fe-3a9e-a4c0-7f1e80014927 | -13.5341 | -56.5874 | 2025-06-05 05:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 666af516-1419-3789-8d51-6641d7b083ec | -13.5152 | -56.569 | 2025-06-05 05:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 317.5 |
| 827e8436-2d08-3753-8019-e95ec6155c1e | -13.14492 | -56.81198 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 281eb80e-939d-335c-b408-b718e58a24f5 | -14.22195 | -45.48235 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d51a3ef8-3445-3dd0-974e-3577ea651ec9 | -13.81204 | -59.68305 | 2025-06-05 05:01:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50a714db-8350-3e64-bb7f-0264e7dfb615 | -12.64934 | -54.11838 | 2025-06-05 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1180bff-8e1c-3266-8b44-de16b4075b8d | -13.50889 | -56.56974 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1851b856-ec87-3607-bd90-53bdb489e5a8 | -13.52178 | -56.55352 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c35ff30-9407-3da6-94e3-c43e7661b51c | -13.50555 | -56.56918 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c87f1c9a-c22b-3683-b3ac-88bd6efe2899 | -14.72658 | -45.10273 | 2025-06-05 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b9f0d41-058e-3017-ac4c-53479dea8ef8 | -12.37021 | -54.16711 | 2025-06-05 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18c681db-2808-34d0-91a4-b033e279b76f | -11.54325 | -56.43671 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ca23368-f6ec-3f9a-b549-e5385d8576b2 | -12.05937 | -58.12409 | 2025-06-05 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c025e212-1425-32d4-a7f1-ecbbe559fc2f | -14.23282 | -45.48091 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 813fd63a-3f72-3134-a90e-5962a7ae0cef | -18.84612 | -53.62488 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a8ee6f9-f780-3c6a-a39b-e7802fd703c6 | -18.71476 | -54.18822 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 057e61f4-915b-31d6-bc5c-169088513511 | -11.78633 | -54.77187 | 2025-06-05 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0460c52-da9c-3114-86cd-0749cd016a2c | -14.72706 | -45.0984 | 2025-06-05 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 378770dc-190c-36c5-8014-a9a283d7bce0 | -13.52674 | -56.56536 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 805354f7-81af-38d5-ae32-ffa8c226d3e5 | -13.53065 | -56.56234 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0e03115-9c7f-3793-b925-f2a041539c0b | -13.52283 | -56.56838 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| b002b1e8-6689-3ca8-9bd6-379ae016dc87 | -13.51061 | -56.559 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da8b916f-bc39-3edc-bd24-4d44948fdcce | -13.52951 | -56.5695 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d7c0a4f-2404-3406-8627-1946f89fa03b | -13.51108 | -56.57746 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7006838f-705a-3a46-8c27-6391f678f0a1 | -13.81575 | -59.68378 | 2025-06-05 05:01:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfeab123-552f-3551-bba9-c386c3c88744 | -13.51499 | -56.57443 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10530f08-fb41-3d5f-9b68-3935b2d762f1 | -13.51672 | -56.56369 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 0323daf0-446e-3968-9b9a-b9851839bc83 | -12.66186 | -58.2143 | 2025-06-05 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5133cfc-4d95-3738-b750-e2035555ade2 | -13.5211 | -56.57914 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d5dbe68a-2d60-31dc-a5de-98ff36b1b779 | -13.51118 | -56.55542 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddd061dd-dd79-365d-b91b-bdc13f928f5b | -14.73356 | -45.09455 | 2025-06-05 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b98f1c17-0d12-3c71-9fd2-53991ba0ee01 | -14.22746 | -45.47599 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77636461-65bd-369c-b0ff-30fc6b7a6e5f | -13.71419 | -57.47855 | 2025-06-05 05:01:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e659637-450c-37dd-a62e-edb53da2f430 | -11.6229 | -55.38718 | 2025-06-05 05:01:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0379397-47f6-36a1-8fa2-c95b16cfdc69 | -13.52569 | -56.55049 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb06c120-dddc-3545-ace9-c54f9472d2d3 | -13.51948 | -56.56783 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 32ff8452-0477-34f3-bb51-0ab4e1de6490 | -13.52846 | -56.55463 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1955d33d-4ad3-306c-b62a-1c3cf46530f0 | -14.73308 | -45.09897 | 2025-06-05 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f26a7969-22aa-3506-9052-b4c94c12b5b4 | -14.73861 | -45.10394 | 2025-06-05 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5bf35dc-49e9-3ebd-8bc4-113483ae4702 | -12.64822 | -54.12578 | 2025-06-05 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d07f57ae-24b2-3483-b6f2-32843cc08133 | -19.39972 | -54.41871 | 2025-06-05 05:01:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9f5e187-6343-3970-9561-ddceed1542ff | -13.1455 | -56.80837 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c08be2de-61cc-3120-84ec-59c5869f0b2a | -13.51385 | -56.5816 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6de950fc-6245-3a00-a89f-23c99a904891 | -14.72151 | -45.09344 | 2025-06-05 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 908e125f-afa1-3a9e-ad19-e5f9925e5672 | -13.51614 | -56.56727 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 8c1a4bb4-a9ec-359b-8cd7-af92466b809f | -18.84487 | -53.63372 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b4f91d7-bdaf-32e3-9e76-01dfb57efc61 | -18.84058 | -53.63757 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 10bc85ba-e19f-35ce-94ed-56f021dae6d0 | -13.5151 | -56.5524 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c21ef8fc-09bd-38a4-ba7f-06358a5b3ce4 | -11.7107 | -56.45312 | 2025-06-05 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a87ba792-45ac-3725-a607-fea6d95b39f2 | -12.1238 | -54.66347 | 2025-06-05 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b94605a3-9d14-3102-bf3c-432421f9f9a0 | -19.01551 | -53.4923 | 2025-06-05 05:01:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 372f1838-e9bd-31b2-a426-376b2ece5e34 | -18.84549 | -53.62931 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e965008-4485-32d8-adcb-6d047a7de4a6 | -11.55054 | -56.43423 | 2025-06-05 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfc80391-0fe1-3fd4-abca-7de7e59b50f8 | -13.52225 | -56.57196 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 529b3e1a-f6c6-3d12-a61d-bb6c8b1db2f2 | -13.51051 | -56.58104 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38e2e101-6e29-3559-a129-76010e46281b | -12.66537 | -58.21492 | 2025-06-05 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ac397a61-99a4-34ae-af89-6d7706482f9b | -13.52731 | -56.56178 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb23806c-e8cc-3917-bf62-b72258dec78c | -18.83753 | -53.63256 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5c66ad40-2d7d-3b0e-938f-7262bceb3b46 | -11.54603 | -56.44085 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README16.md)
