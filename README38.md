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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f2444b6-be51-39a3-8769-12228da0487a | -17.56455 | -57.57747 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 77e4acbb-3fa9-34f3-8be7-e19400872b73 | -17.58282 | -57.5654 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cebcc3f1-7a08-371f-95ca-30d6c34a1e71 | -17.58562 | -57.49853 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9cc2cd5a-d74f-3e74-ad97-f1c2515dc5ef | -17.57102 | -57.46648 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 111d4c6d-a4c7-3e21-927b-5ac411788f29 | -17.65143 | -57.45052 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fa0d0c83-7bf0-355f-801a-33fb5b7b057e | -17.56571 | -57.54535 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1188d847-f5dd-32f8-8867-f8408e6e7741 | -17.57912 | -57.58397 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 428f3413-6807-33aa-b905-eaf8fc5e9b18 | -17.06461 | -57.48781 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a1cfb6fc-7849-399e-9575-863a5c66b16f | -17.6502 | -57.45658 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e66ae528-dbb5-35b4-9e32-926753c02cac | -16.0093 | -59.37033 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a66b1b9b-7c4f-30dd-baa6-0b4663a70c95 | -17.62717 | -57.5697 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.7 |
| df19c7f5-3442-3926-b04f-0dc3503ec53c | -17.566 | -57.46535 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e6e9a29f-11b0-3e0f-ab06-cd555cabd1a3 | -17.81577 | -57.37624 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 5edf37e1-6dd4-33fb-9c6a-32482ffd6940 | -17.61392 | -57.55702 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5fc091a6-5155-3ea7-858d-7f37c5db9b43 | -17.55747 | -57.53382 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1f6b7e62-d12c-392f-a898-d92563a1cb78 | -16.0428 | -60.11683 | 2024-11-16 04:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f35b334e-30b8-3e52-85f8-1199710fb7ec | -17.57164 | -57.46342 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cf707762-36b5-300e-ab43-6bef3b03dbf7 | -17.56385 | -57.55462 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bb801f85-7cf5-316f-b04d-ee76fbda61f8 | -17.70215 | -57.57725 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 28a13b0d-7560-3614-99e3-d6d98e6e483c | -17.57089 | -57.44104 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5efe5dd1-f71d-3954-b58e-ccb37d4ba598 | -16.10252 | -60.10204 | 2024-11-16 04:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0506639f-4e16-3e36-abd3-e5dbd4d032a6 | -17.23445 | -57.18894 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 253dd1dc-b4b7-3c61-afff-cc6a015ba584 | -17.58938 | -57.49697 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a13d6fa4-b016-33bb-af53-e5d93b00659f | -17.55809 | -57.53074 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 043bd89b-a0fb-3983-b723-696cdcf1573c | -17.59945 | -57.47374 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a3c133f6-fddf-32b7-b6e8-09547f0fd9fe | -17.54614 | -57.53771 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 091990c4-b367-3828-b1f1-b02c7401f05e | -17.5721 | -57.56618 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cc59b61f-efd2-3222-b851-cc5a5eb2d270 | -17.06847 | -57.41749 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a94a0359-254f-3da6-bcdc-f81d9465beda | -17.59613 | -57.47218 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d2c8f0a2-030c-39df-a31b-10e2c91ce8d5 | -17.69241 | -57.50744 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c57ed16f-761d-35d8-b46c-fe25c2102bc8 | -16.04074 | -60.12646 | 2024-11-16 04:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0511f00a-5f0d-34e6-9188-4260f09ae32b | -17.65298 | -57.54653 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 8c694a64-9cee-3f7d-b50b-356cebe18596 | -17.09253 | -57.48103 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 293f00b7-3a6b-3529-9fe6-20b21eecc223 | -17.58372 | -57.4989 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b73b6441-7861-35f1-9db0-5c6b93d27c4e | -17.55623 | -57.53999 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 14cd9ba4-26c0-3885-8689-0088a4ee42ad | -17.57408 | -57.45126 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6ef4c5b1-9e39-340d-b831-1fabecee7433 | -17.56633 | -57.54227 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f623da9-7a37-3fc7-80f0-11fb5d537889 | -17.06342 | -57.41635 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 6c9c241f-fb81-321c-9aeb-e062b9558806 | -17.23911 | -57.45005 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9e5032d1-8e85-3280-a748-b22c31516073 | -17.59002 | -57.49392 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f0f65b7c-fd4e-38b1-8b0b-8ca268a063f7 | -17.62527 | -57.55313 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3afcd180-626d-3a4e-a0b4-bd2ef7a6ac81 | -17.23158 | -57.46124 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8547d946-50f0-3c91-bbe4-1384d2f71222 | -17.23787 | -57.45621 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| e09c5e62-e9b0-3718-ba3d-d66d1328f4e6 | -17.56252 | -57.53497 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ffa64ec7-f3fc-32d8-9446-709a9ce2cc4a | -16.01322 | -59.37074 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3cb7467-4707-362d-af9e-4b8482e97336 | -17.68642 | -57.55124 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5c75335e-dccb-3e72-871a-ccfee863d15a | -17.81557 | -57.55416 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e9450822-9ff6-363c-b425-4e2f5df51f68 | -17.57604 | -57.46762 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 9e512335-802b-3eda-a1b6-2e6e5f04a57e | -17.68579 | -57.55431 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7b8a321f-a1ba-31bd-9586-9619c48a5492 | -17.24354 | -57.45425 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| d37e89f3-bf67-3bd4-b849-30ba5578bc7c | -17.58168 | -57.46569 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ea61a0bc-b41c-3bfe-9140-ef57899ad1d9 | -17.68388 | -57.56351 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2061c3ff-0cbe-3c10-b754-151f4a0eb969 | -17.57126 | -57.51768 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b78b4817-4c30-3d10-a245-00cd7b39e56d | -17.57034 | -57.56332 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7a6241fe-100f-34a0-9466-c043cbfa2cec | -17.63348 | -57.56466 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 3d2ae686-e5da-35e1-80b8-08c2c6a70e7f | -17.57727 | -57.46149 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9c494c31-4539-369e-a846-9ef7b542d7fb | -19.00281 | -52.3947 | 2024-11-16 04:27:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4587f819-23d6-3ed2-8fca-1d394bd4bb64 | -17.58229 | -57.46264 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 65db7ee3-4448-33ff-a152-d437c2009666 | -15.92128 | -59.2734 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d3125d3-6a75-3d89-8e29-9360603ff8bd | -17.57354 | -57.54794 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 558fc4aa-7539-341b-9a2e-f441299c539d | -17.58365 | -57.48211 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d4889cfc-d8ac-35fa-9f94-29d94e5ce547 | -17.5823 | -57.58218 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 58350ee5-16fa-3afc-bcee-df0f6f5df76d | -15.91972 | -59.27556 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b253a04f-4ce4-3ccb-857a-f62bbae0ac60 | -17.63285 | -57.56775 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 46417194-b724-3ee8-b0b5-cfb7d30c1a39 | -16.04383 | -60.11202 | 2024-11-16 04:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a5c8394a-38d8-3d92-a3b4-b8db6aa67fd9 | -15.9049 | -59.26458 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c250ac77-0dc7-3471-a883-cb8bb01fd018 | -17.62212 | -57.56855 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.7 |
| 0ec1b6aa-84f4-3310-ad4f-e77cfaaf7e91 | -17.57065 | -57.52074 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| eb7e6dc6-3537-31b6-b807-2a4c6898c051 | -17.58623 | -57.49547 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0dda769a-ec61-3ff4-a79b-4d58874e062d | -17.65423 | -57.54039 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fa58f0f5-97f5-38cd-8e69-bf1023196f2b | -15.95465 | -56.38022 | 2024-11-16 04:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 621105e7-f7f2-33a8-9393-7cbe45fdf17e | -17.68839 | -57.58031 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6c179194-4b36-3a9e-946c-2cb992717c4a | -17.56208 | -57.43274 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 11b44819-a9ab-3f30-bfb3-34ba6acd97a2 | -17.36058 | -57.43565 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 77ec028a-947e-3795-b008-f49c3e0311d7 | -17.58032 | -57.44632 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3c239972-2b98-31d2-b4e5-92fcf472fe73 | -17.2322 | -57.45815 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e8e93364-12e0-344b-98a6-2423eeda1057 | -15.90827 | -59.27226 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 95fba28a-49b1-3b86-8366-fc4df6899f5b | -16.02109 | -59.37229 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6fb6aa54-4059-3dd4-bd9d-b5d41ac575f8 | -17.5894 | -57.4715 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3e24e0f6-c673-37c5-ae71-667851d0c68f | -15.89144 | -59.27087 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ef0c0fb8-673b-3862-882e-4693c67efeb6 | -17.63536 | -57.55541 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| b267d895-c7e0-345a-8724-482c0aaf4eea | -15.91633 | -59.26797 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f99caa43-fb51-3faf-a62d-abea3c6d9d80 | -17.57666 | -57.46455 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b4d54c13-e359-3a0a-b8fb-d2fa209ac57f | -17.57075 | -57.54652 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 48cc0677-9764-3167-b817-d481bf0f2414 | -17.56539 | -57.46839 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fea8e210-84dd-35b3-8ff1-16ca5094790a | -17.06397 | -57.49092 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6663f8f0-eeca-35e5-8d4c-deaba9425c50 | -17.21778 | -57.19651 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e342afc6-71b1-3d06-91bd-8193359fe38b | -17.66183 | -57.55497 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 29a97888-b9e7-3198-8a52-05046e072824 | -17.58875 | -57.50002 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c27728b4-a183-388c-a6b2-2bc79444c129 | -17.57652 | -57.43913 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 03599e5d-393d-317c-a02c-efa9dd28ef4f | -17.63599 | -57.55234 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 6d6c88d9-ca35-3250-a7bc-0b343c7106d2 | -17.65361 | -57.54346 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 110f5c7b-a505-3f8b-b3e1-f5e6f2c8855e | -17.82377 | -54.54441 | 2024-11-16 04:27:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13812f10-6ed4-3678-ab2e-566c62004606 | -17.57862 | -57.48096 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7fb7df17-e404-3cbd-a664-9b4d21153155 | -17.35935 | -57.44175 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 323e0a58-7779-3fa7-8adb-ee83345172ee | -17.68322 | -57.55339 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6c475389-7718-302f-a8ef-6085c2a866cd | -17.24478 | -57.44809 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cec2016d-fda1-3db5-9366-b41d3760650a | -17.63832 | -57.46341 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fd7d5919-004b-3c59-85ba-96346b4a17d5 | -17.57347 | -57.45429 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e6ee3326-f308-32c4-a74e-d5a53895738d | -17.57971 | -57.44934 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README39.md)
