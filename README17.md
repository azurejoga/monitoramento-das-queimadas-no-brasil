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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d10e0ef-1e20-3a78-a114-6569c2f3be83 | -3.2427 | -53.0722 | 2024-11-11 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 2a2e880e-588e-3015-941f-3077b535a81a | -4.11 | -49.1102 | 2024-11-11 01:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0621d747-cb75-3aa6-a0d9-5300b0280787 | 1.4733 | -56.0233 | 2024-11-11 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 72c962f7-db83-3ae4-9ee6-82eb7ba77598 | -2.2504 | -46.5282 | 2024-11-11 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 18fafbac-c306-373a-9e6a-b972a51b4df1 | -17.2933 | -57.4857 | 2024-11-11 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.9 |
| 24cf15fb-ebdd-320b-b8cd-031795256643 | -4.0293 | -46.9703 | 2024-11-11 01:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 309723c4-8f72-3d69-ad06-b61437e0dbcb | -3.1983 | -50.2867 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 45de0ea1-ad3c-3d3e-a0de-bac27d1fddc4 | -3.0324 | -45.8154 | 2024-11-11 01:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 067fa2a3-6ff7-326c-9a87-35ff7e061eac | -3.2428 | -53.0519 | 2024-11-11 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 22159ac9-4221-3086-80e3-78321a3c2d5c | -2.1891 | -48.36 | 2024-11-11 01:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| cf3e47eb-79d6-3542-aec3-4e2c97fd7a40 | -1.4057 | -52.3553 | 2024-11-11 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6282c174-8c7b-3e9a-9e11-9ba9214291dc | -17.6086 | -57.4276 | 2024-11-11 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 038e0964-baac-3015-b2b6-b48d91925421 | -3.1091 | -45.2968 | 2024-11-11 01:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 53a0d64f-4036-34ec-80b4-80a65e0934a3 | -2.8323 | -49.4325 | 2024-11-11 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| af5cda10-e206-3ad6-ad1e-42c0f4524f97 | -3.2536 | -50.3059 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 362aa755-9d4b-3285-87af-61a54df2f848 | -3.7149 | -54.6504 | 2024-11-11 01:10:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ee1c9c45-db09-3b85-aea9-cb19ca30d868 | -3.0295 | -50.9815 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 503b256c-2974-3c37-bd70-9f3779e3145c | -5.9788 | -45.3621 | 2024-11-11 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 166c6fc0-071d-310c-88e9-2be7ec508dfc | -2.8508 | -49.432 | 2024-11-11 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| f831caa0-1fab-3ca6-a436-b393af195975 | -3.2244 | -53.0524 | 2024-11-11 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| f279d164-5eec-3a39-9d60-f98eb9a4df8b | -3.2168 | -50.2861 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8ce92b4d-c81a-3c8f-98e8-4b4bdafeed04 | -3.0845 | -51.0631 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 3229e318-23c4-308e-b5aa-ae470d4b14a2 | -3.0213 | -53.2607 | 2024-11-11 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 03ca0eee-4245-30af-a813-e5ec870bf379 | -2.2504 | -46.5061 | 2024-11-11 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 593454da-2744-3d4c-a481-538dee52b5b1 | -2.2075 | -48.3811 | 2024-11-11 01:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 098fa46d-b1ff-3e3d-bb75-3173ddd3cdba | -4.6835 | -46.4074 | 2024-11-11 01:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| ad2916c5-60fb-3270-ba82-1f4e7ac77fbf | -3.1423 | -50.4352 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| aabe07bb-d1d8-3920-9a81-a5293fddf718 | -3.0214 | -53.2404 | 2024-11-11 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| e5e693a8-4160-3971-866c-7017b442b8d4 | -3.6218 | -50.5661 | 2024-11-11 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d44a33eb-1be6-37f0-ba74-30d019d5fc1d | -3.1458 | -54.4659 | 2024-11-11 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ab88cf92-fc4f-3362-b2cb-1675bd3e4804 | -3.2352 | -50.3065 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 20de1c86-1056-3440-826e-4e517c02a2a2 | -3.5322 | -49.9599 | 2024-11-11 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 1ee4a8eb-ddc6-34a1-829f-20e0c0bf6d9e | -3.1092 | -45.2743 | 2024-11-11 01:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 63e8ba34-8b6d-3650-9e96-c74b7c8935cf | -3.0323 | -45.8377 | 2024-11-11 01:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9925fc32-4536-35bc-80e3-cfb1e0db75ac | -3.6954 | -50.6262 | 2024-11-11 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 2121a328-eb88-3990-be34-78540ab16a2b | -3.6604 | -50.2081 | 2024-11-11 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a73df363-2460-3d70-afed-8969a110950a | -2.4367 | -51.948 | 2024-11-11 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 5c4acce6-8dac-36d3-bcf4-75bf34f97ca5 | -4.1101 | -49.0888 | 2024-11-11 01:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6a177cf2-f423-3be0-b085-19c16e86cdec | -3.1458 | -54.4859 | 2024-11-11 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 6482c270-0158-34e9-aaaf-28d0b3ed5a77 | -3.1641 | -54.4854 | 2024-11-11 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 1be05451-52b2-325e-a3dc-26fa083dffd3 | -2.8508 | -49.4108 | 2024-11-11 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| ebda80a4-981c-39fe-a571-2dc912d708bd | -2.189 | -48.3815 | 2024-11-11 01:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 01ccae93-757d-3d01-a499-1bc6f21f01fb | -3.2352 | -50.2855 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e451e11b-55e2-39a9-b271-6af81337e340 | -1.4057 | -52.3758 | 2024-11-11 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 1d9394bb-5e3e-373b-9786-9fc4731780d7 | -3.2588 | -53.6994 | 2024-11-11 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 56a747f8-9361-3f38-8d81-1ac3665de971 | -3.1097 | -54.2865 | 2024-11-11 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| bd86b52c-faa5-36ba-828e-0624ee183310 | -17.2936 | -57.4652 | 2024-11-11 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 77939f5f-69cc-37d2-b978-09db281ce10b | -2.2076 | -48.3596 | 2024-11-11 01:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 884005a3-6345-3db9-87ed-46758b516786 | -4.0294 | -46.9484 | 2024-11-11 01:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6d2b1adf-2876-351d-b068-84acf6249301 | -17.313 | -57.4834 | 2024-11-11 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 9f4ee3fe-2d38-34ae-b144-9985a619f562 | -3.6217 | -50.587 | 2024-11-11 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 6d204f78-9e8c-3f1f-9525-a8f5d29775be | -3.0296 | -50.9607 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 993d39b1-095e-30ab-aee1-a5653ec4abbe | -3.0111 | -50.982 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 896c9215-81c6-31ed-af09-ea735dae3a5f | -3.1984 | -50.2657 | 2024-11-11 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 407011e0-6c85-313f-b535-f70c50bc5c0a | -3.6789 | -50.2074 | 2024-11-11 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f310b9af-7b54-3ea8-9457-46b9bd5e35fa | -3.5137 | -49.9606 | 2024-11-11 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0a90a0ca-8402-3b7e-9933-18af6f1f544d | -3.6032 | -50.5876 | 2024-11-11 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b03708eb-8aa4-3b96-bb34-eb4fdd42be3a | -3.6033 | -50.5667 | 2024-11-11 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| d5e74154-d51d-3279-b9b6-9232440b4e46 | -3.4021 | -50.1329 | 2024-11-11 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 55e42821-3eae-3d58-bdb6-0e4d2f6eccad | -3.0138 | -45.8161 | 2024-11-11 01:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f0465e6c-3059-3a97-8ce2-d88f48c4f165 | -3.5772 | -52.3072 | 2024-11-11 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e70293bf-ac1c-34a0-8393-52abe4e4ad0a | -3.1423 | -50.4352 | 2024-11-11 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b45c601b-37ce-34a4-85af-9ad73cf92aef | -4.1101 | -49.0888 | 2024-11-11 01:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| df1d3861-4edf-3653-8282-34a66e79aee6 | -2.2075 | -48.3811 | 2024-11-11 01:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 57654c0d-8fdc-3864-b83a-04f3d4cf8a94 | -3.1458 | -54.4859 | 2024-11-11 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 1c6592d3-17d9-3191-a789-ea8e4ed3cc03 | -3.7149 | -54.6504 | 2024-11-11 01:20:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 78820ef0-b81e-320a-8064-089166cec6f8 | -4.6835 | -46.4074 | 2024-11-11 01:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 0612ac3a-b4ec-3447-b8c4-ccb865f92a15 | -4.0293 | -46.9703 | 2024-11-11 01:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bd319562-9f75-331d-b778-51b9096e6a6f | -3.2168 | -50.2861 | 2024-11-11 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8a176b6d-e56d-3da4-9767-f95c3a57ef2f | -3.2352 | -50.3065 | 2024-11-11 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 488ea285-d05c-3254-88dc-5388696cdf4a | -3.1983 | -50.2867 | 2024-11-11 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d823af7a-73ac-38b3-ae75-691f6b45dd4f | -3.0213 | -53.2607 | 2024-11-11 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 319a452c-543b-30bf-b5fd-4db94f3e4582 | -3.0111 | -50.982 | 2024-11-11 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5fd51cf4-60d8-36e1-901e-cf4207e1961b | -3.3836 | -50.1336 | 2024-11-11 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 51e6c28d-14c8-3432-9d9c-8f388209f32c | -2.4367 | -51.948 | 2024-11-11 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 957c95c1-5a02-38c0-88bd-bdf768344a16 | -3.5772 | -52.3072 | 2024-11-11 01:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 7e686dda-ab90-3f19-8660-16fe89c97469 | -2.8323 | -49.4325 | 2024-11-11 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 00012419-b668-3858-a9e8-74943f09f6e8 | -3.2428 | -53.0519 | 2024-11-11 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e05b2691-3927-3c0b-a1f7-0a5681d92025 | -3.0138 | -45.8161 | 2024-11-11 01:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 46b2f965-36cf-3b34-8333-41de717c43af | -3.6218 | -50.5661 | 2024-11-11 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 49161e1b-7c88-3cb1-a534-eaf01316b518 | -3.0214 | -53.2404 | 2024-11-11 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 3cc459b4-def1-30d9-acdb-ae5f25c2a2f3 | -2.8508 | -49.432 | 2024-11-11 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 2555f5a8-ef6b-3e3e-9265-7a654075ea5c | -3.2427 | -53.0722 | 2024-11-11 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| bcfe62a9-9390-3fd0-bbd5-9adc57f310f0 | -3.0324 | -45.8154 | 2024-11-11 01:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 3ce44343-9c79-3248-894e-a64db8ecd89f | -3.5346 | -45.7061 | 2024-11-11 01:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 237870f7-e331-32e0-b4c1-7842112ba168 | -3.1458 | -54.4659 | 2024-11-11 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7eba9de6-c563-3352-8ba6-5e0b06d45ec9 | -3.2588 | -53.6994 | 2024-11-11 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| bfe32462-74eb-379d-bd4d-b37b0a9f2329 | -3.2244 | -53.0524 | 2024-11-11 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 9549a47e-47e3-361d-b8eb-90fe889a4d02 | -3.2772 | -53.6989 | 2024-11-11 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| b5e01d3e-4f12-354c-8471-025cedbe9c75 | -3.6954 | -50.6262 | 2024-11-11 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| fad64258-fa6c-3f56-a018-3e4634ff716f | -1.4057 | -52.3758 | 2024-11-11 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 550c2713-2e73-37c0-8646-3645a4abc19b | -3.6604 | -50.2081 | 2024-11-11 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 459c72a0-59b8-357f-9cc9-2cea784c9410 | -1.4057 | -52.3553 | 2024-11-11 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c30c5973-db2c-345e-8e62-8ce0a75a6230 | -2.8508 | -49.4108 | 2024-11-11 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 22a19016-6615-3e32-8d17-a8ed335bac76 | -2.1891 | -48.36 | 2024-11-11 01:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 797987b3-c343-30be-8b5c-2e25913ae62d | -17.2737 | -57.488 | 2024-11-11 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 4fe3218f-9976-36ea-b973-61868a9d53bd | -3.6789 | -50.2074 | 2024-11-11 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 0e7838ed-991a-32f6-8c4b-d6986e107b5c | -15.9793 | -59.3267 | 2024-11-11 01:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 43bcf412-8d41-30cd-8343-fe95b1b25b77 | -2.9355 | -51.482 | 2024-11-11 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 73769528-48fc-35a9-84fe-ccd3de17788f | -3.0323 | -45.8377 | 2024-11-11 01:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |


[Clique aqui para ver as próximas entradas](README18.md)
