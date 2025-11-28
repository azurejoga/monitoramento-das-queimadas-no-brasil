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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d74b790b-e2e0-3171-8d9a-2e1b4f74c4fb | -3.17109 | -48.60871 | 2025-11-28 05:22:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe4cc0f0-7020-3715-893d-1c5d3ad35c23 | -3.2254 | -50.3235 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4eef5793-47f5-3481-a983-652b5440d43a | -3.92704 | -50.99671 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b487b97-8258-3ad4-bddb-bfda8a1354b3 | -3.41967 | -50.15406 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 969ed672-1141-3226-a81c-9db80c6a5763 | -3.40553 | -54.5827 | 2025-11-28 05:22:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 873453c1-8e64-3bdd-a62b-37a260f26356 | -1.34242 | -55.4431 | 2025-11-28 05:22:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0e31051-4c2d-3d21-bdf2-783960dfdb50 | -3.35824 | -50.49302 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d32b06f2-7266-315b-bf56-eb2703218f86 | -2.70846 | -53.18307 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89e38419-c17e-3c98-af25-b056affa0b70 | -3.17653 | -48.61427 | 2025-11-28 05:22:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b5d7205-b505-38ea-9b2d-9eb9d9be510d | -3.59916 | -50.42587 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f244643-4bb8-3d78-a1d8-ee7c89ed43a6 | -3.5846 | -47.27676 | 2025-11-28 05:22:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74a81f66-463c-3f3e-a6d6-857159ab92c3 | -3.24814 | -50.02253 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c956691-7140-3335-ac3a-491e56542631 | -4.29949 | -55.6105 | 2025-11-28 05:22:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e981f90e-5046-3964-9345-c693e3b4ac05 | -2.73304 | -51.83916 | 2025-11-28 05:22:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fd59182-a055-39c5-bc82-c63ad3089c33 | 2.05275 | -60.87275 | 2025-11-28 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79ce2851-5948-3a3c-baa5-c1757496f3c1 | -3.4191 | -50.15787 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b628c4a-1374-3167-9a2f-ae8742d46ffd | -9.93461 | -60.71639 | 2025-11-28 05:22:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a38b2bc-8272-3b93-8e30-c6c7d8a94671 | -3.4057 | -53.30903 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2e3f445-d150-35f5-ab64-83609cdd99d9 | -3.92225 | -50.99235 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7adff2e0-43b1-319f-ba43-78e739eda209 | -11.08466 | -54.77687 | 2025-11-28 05:22:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb54ba22-64a4-31f2-ad3c-306f086fd6fa | -3.03944 | -50.97872 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68423cd9-e5da-3d3b-a48e-fdeb328453c9 | -3.39828 | -54.54708 | 2025-11-28 05:22:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1867db20-2857-31ba-bf81-39e41da0cd62 | -10.27848 | -60.5349 | 2025-11-28 05:22:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cc431c6-3605-372d-810c-231bb1331ea8 | -3.17666 | -48.61276 | 2025-11-28 05:22:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acc3c823-bb36-3a69-844e-460f0af7d7e9 | -3.17725 | -48.60959 | 2025-11-28 05:22:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 512e1bf0-73e6-36aa-9c43-0367e505df1a | -3.38407 | -54.1265 | 2025-11-28 05:22:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b3e4595-e83e-344f-b54d-2bf8d54a29a2 | -1.8366 | -55.3487 | 2025-11-28 05:22:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaeda28f-ef9c-3e66-b91f-ac09b7a0e0cc | -3.03457 | -50.97594 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 496c755f-1049-3a7c-881b-b126b520ba07 | -1.34548 | -55.4483 | 2025-11-28 05:22:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e81e51dd-b89e-3208-9df6-528174ea0566 | -3.05926 | -50.37877 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a606b74d-e62f-3636-9e29-01e809df1642 | -9.94071 | -60.72097 | 2025-11-28 05:22:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d7b3f66-99ba-3145-b5f3-5acb6d635eb8 | -3.23017 | -50.14207 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2551ec9-99a1-320a-98fa-dd870e4693dd | -1.34589 | -53.09455 | 2025-11-28 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f794be1-1afd-3adc-a46f-6a4162c5922a | -3.0603 | -50.37176 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32341f09-fad2-30bc-9669-b4906fab8d51 | -3.03369 | -50.98121 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9412f636-5771-315f-b602-873824623396 | -9.94125 | -60.71745 | 2025-11-28 05:22:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3b0a426-c955-3149-971f-27ed76a2a9b7 | -2.4236 | -50.29304 | 2025-11-28 05:22:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74958c32-0309-3806-8161-025caae9046a | -2.42197 | -47.23111 | 2025-11-28 05:22:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d884ed09-d089-3a37-99d3-c6b6f521f5b9 | -3.92649 | -51.00046 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88f0fc7b-4e66-3d09-b4f2-55a8c3f149bf | -3.92876 | -50.17232 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 868310a1-fc1d-39b5-8ef0-6cf461e3ebe3 | -2.42404 | -47.23332 | 2025-11-28 05:22:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72f68719-ee1d-3582-b6ad-747e53c15428 | -1.24758 | -54.05965 | 2025-11-28 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0efb658a-f711-38bc-9582-98ab37f89bcb | -16.06307 | -59.29412 | 2025-11-28 05:25:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c18d33f-348a-3058-bb56-a60b66f22b05 | -16.05573 | -59.29309 | 2025-11-28 05:25:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b46b02df-6180-3e6e-a43f-1085aba668d8 | -12.30091 | -63.72938 | 2025-11-28 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 600f7b42-2e74-3c85-9bb3-b70f4972fa55 | -7.58386 | -55.49704 | 2025-11-28 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e741db7b-5cc2-35e5-86a3-6e3370f0ff01 | -11.94886 | -63.95015 | 2025-11-28 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0879ca36-9231-3b6c-9dfa-d4893d479587 | -16.13959 | -59.95952 | 2025-11-28 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 475cac92-1271-3c11-99c1-232de4025770 | -19.98514 | -49.99666 | 2025-11-28 05:25:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ae07f1c8-54fd-354f-ac29-35b1671e8830 | -16.14314 | -59.96006 | 2025-11-28 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d800de1-bbc8-34fb-8275-c0c572932e56 | -14.50948 | -59.75391 | 2025-11-28 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8643ea4d-53a0-3475-a044-900f7573f8db | -15.60093 | -59.94257 | 2025-11-28 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0a1ffbe-0608-3fa6-af93-5a484892111c | -11.94948 | -63.94633 | 2025-11-28 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 785be211-4147-35d0-946c-6c96bae7c7e8 | -16.09599 | -59.76546 | 2025-11-28 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5c8e204-d195-3675-be0f-d4e7f21b288d | -16.14254 | -59.96424 | 2025-11-28 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e34825e5-6c49-30ac-b23a-c8e1e488a0c3 | -16.06002 | -59.28928 | 2025-11-28 05:25:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb1772b8-3cbc-3dec-8528-962aa6f6071d | -16.09958 | -59.76601 | 2025-11-28 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25ecb62c-93fc-34de-86aa-e9dc3efabfba | -16.13899 | -59.96368 | 2025-11-28 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59399bd0-133e-38dc-a674-f789a2dafe8b | -15.60153 | -59.93844 | 2025-11-28 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 851f09a3-8c5a-37bb-86b6-24b4f1a802e1 | -16.05939 | -59.29364 | 2025-11-28 05:25:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd60dcbc-1e12-396a-a72d-4f59a12698a1 | -20.42954 | -57.94372 | 2025-11-28 05:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 80682fa9-2bb4-37e8-bb61-2a09cc631135 | -20.42533 | -57.94314 | 2025-11-28 05:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a7821a33-c2d6-304b-8e74-9d6d068bd4f4 | -20.43375 | -57.94431 | 2025-11-28 05:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| ae432f9d-31ca-3b77-bc5a-701468509789 | -20.43797 | -57.94489 | 2025-11-28 05:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 01c6f17e-ed75-3834-9531-8c5445e2d4c0 | -29.77316 | -51.17992 | 2025-11-28 05:29:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 31b4eec8-415e-3ea7-b824-5a918f0deeda | -3.7508 | -46.9608 | 2025-11-28 05:40:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 12f13fda-7807-3782-bbfe-74923ae82397 | -9.1727 | -67.01104 | 2025-11-28 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97bbedfd-0a89-33fe-9352-7dd5158a89dc | -1.35304 | -53.09874 | 2025-11-28 06:26:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6ea7ce44-843b-30f3-a800-1ad4eba26200 | -2.38461 | -49.3819 | 2025-11-28 06:26:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 11696a09-efee-3b49-af26-1b472e0eaefd | -2.74383 | -47.12699 | 2025-11-28 06:26:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e550aa38-320b-3c2c-921c-f5d5ee375da8 | -2.68974 | -49.55516 | 2025-11-28 06:26:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5a5e4b2e-5ce9-32f3-a697-bb590f04b7c6 | -2.4241 | -50.28892 | 2025-11-28 06:26:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8abceb0f-cf49-376d-850c-13c7f77a8ae7 | -1.47486 | -54.19819 | 2025-11-28 06:26:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f9d0603c-33e9-3280-bdb4-9843780aada1 | -2.61702 | -47.35446 | 2025-11-28 06:26:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c8edfb08-b1ca-31ce-a960-b888969bf9c5 | -3.80551 | -44.30516 | 2025-11-28 06:26:00 | AQUA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 6a6d8b4b-3eff-3748-b2ce-3a9e60bad944 | -2.41802 | -47.22632 | 2025-11-28 06:26:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 388f7e69-16c1-3176-aa87-f8a7842d823e | -3.79408 | -44.30878 | 2025-11-28 06:26:00 | AQUA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| a52bcac7-7eb6-3f1d-9428-fb344b645344 | -2.61913 | -47.34046 | 2025-11-28 06:26:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 776f939f-65b1-3252-9edc-fd2d66802c14 | -2.76966 | -49.63556 | 2025-11-28 06:26:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4f9cd65f-0675-312c-a733-bbbaaf541b8a | -2.74275 | -47.13393 | 2025-11-28 06:26:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3223220a-979c-310d-8dd3-3e93933cf186 | -1.35443 | -53.08952 | 2025-11-28 06:26:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38808e3b-9235-31dc-85c2-705272313d19 | -1.34543 | -53.08818 | 2025-11-28 06:26:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b59e561-8d93-3679-bd7d-155be40582ad | -2.69124 | -49.54501 | 2025-11-28 06:26:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ad545fc4-8079-36d9-92bd-ac1afa783989 | -2.62096 | -47.34602 | 2025-11-28 06:26:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 6efb1ea3-acd6-3514-9877-1afacc3e8597 | -3.34885 | -54.089 | 2025-11-28 06:29:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e37919f9-86c3-3a1b-9729-5fc23f5e785c | -3.40399 | -53.30063 | 2025-11-28 06:29:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e6940864-3a71-3331-8de4-e0a2cba1c242 | -3.03418 | -50.96985 | 2025-11-28 06:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 704b8670-cf0c-36a0-af32-48632113acc1 | -3.03284 | -50.97885 | 2025-11-28 06:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8ee3ceea-2a48-3d3e-a665-1a583bef38ca | -2.56139 | -54.75413 | 2025-11-28 06:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bbc3b14a-f28c-3591-829d-e7ee21853a4c | -2.71054 | -53.17636 | 2025-11-28 06:29:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 55f97afa-9e6d-3ca1-9668-886241d11cb9 | -3.24871 | -50.01569 | 2025-11-28 06:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9717c300-d2d1-338b-b83e-f3c7781f84f2 | -3.40259 | -53.30975 | 2025-11-28 06:29:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a78bb06-0f18-3f4a-9de8-c093984c27c7 | -3.38228 | -50.24829 | 2025-11-28 06:29:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6f83fd22-552b-3c56-b02a-d205a7007dd0 | -3.22309 | -50.31684 | 2025-11-28 06:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 054f2bbd-57c4-38a4-a797-3df640392f3e | -3.41347 | -50.1513 | 2025-11-28 06:29:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 75a17ea0-391e-3f33-a34b-c14f51474c5c | -3.40131 | -54.57968 | 2025-11-28 06:29:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 92865f8a-b0e8-3a93-8dae-6484543aa36f | -19.97823 | -49.9921 | 2025-11-28 06:31:00 | AQUA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.9 |
| ca4c8a8c-25ac-3292-9d42-71b6bd5e1c04 | -19.98037 | -49.97445 | 2025-11-28 06:31:00 | AQUA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| 09ae33a2-f9a7-322c-b186-b27ea9863c20 | -19.98561 | -49.98239 | 2025-11-28 06:31:00 | AQUA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.6 |
| e85d968a-ebe6-378b-9d31-7fe0bfce6ca8 | -3.5269 | -43.6828 | 2025-11-28 07:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |


[Clique aqui para ver as próximas entradas](README23.md)
