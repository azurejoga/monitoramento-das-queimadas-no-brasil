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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3064223-214c-3ccf-9049-f2f69cf7d566 | -1.718 | -52.4532 | 2024-11-29 07:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 88d67267-e55b-3e50-8d6b-113f2c86b9df | -2.9844 | -53.2819 | 2024-11-29 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ce4d846d-86c7-3ea9-8a37-bae84144e862 | -2.6499 | -48.7772 | 2024-11-29 07:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c9866bba-5a8d-3109-bcb9-7412a1f30d2a | -2.9844 | -53.3022 | 2024-11-29 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 0c0d9acb-0b0e-349e-b345-a79035f75246 | -2.6498 | -48.7986 | 2024-11-29 07:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| bb23ed25-bb5b-388d-a0ca-759ffaec6b77 | -2.7191 | -45.2208 | 2024-11-29 07:20:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f6751293-83a4-3313-9c7b-1733906b99b6 | -2.9844 | -53.3022 | 2024-11-29 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 95fd7a5b-8cc1-37b4-8b4b-5b5a66c382bc | -2.9844 | -53.2819 | 2024-11-29 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 2ebcfee0-212c-3557-b79b-6b120b797a56 | -1.6997 | -52.4535 | 2024-11-29 07:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| ed936c85-8e3b-3c08-a678-b230cf29388f | -2.2299 | -53.6219 | 2024-11-29 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3d4b47a5-bf26-325b-ba12-f10eff985e45 | -2.966 | -53.2824 | 2024-11-29 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 5ac68b9a-8f22-3500-87d7-538bce34b8dd | -2.6498 | -48.7986 | 2024-11-29 07:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| d8f90e12-e650-3c30-847a-26617eaf511c | -2.6499 | -48.7772 | 2024-11-29 07:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| d7fb3615-7973-3b21-9ee3-a47b22001e0f | -1.6997 | -52.433 | 2024-11-29 07:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 987022e7-44f5-36c1-b2b2-a70243a867b4 | -2.6684 | -48.7767 | 2024-11-29 07:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| af814c45-fd2d-3efa-a187-e3f4cdc7159a | -2.6683 | -48.7981 | 2024-11-29 07:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f8117260-33ec-3057-9bdd-ab356665b8e4 | -2.6499 | -48.7772 | 2024-11-29 07:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 66673b7d-ebcc-31c8-8a39-1f8e7486553f | -2.6684 | -48.7767 | 2024-11-29 07:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| d1e23296-ca8a-39fb-bf84-bf87ce39e3b4 | -1.6997 | -52.433 | 2024-11-29 07:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 3defdf3f-f658-3a19-a1c9-121611b690a6 | -2.9844 | -53.2819 | 2024-11-29 07:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 3387726f-a4a8-3f0f-a95e-b424037078c9 | -2.2299 | -53.6219 | 2024-11-29 07:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 48f0f181-f463-3e9d-ac3d-246ae2233ddf | -2.6683 | -48.7981 | 2024-11-29 07:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| edfa7022-903e-3902-99ef-90ac2a5b2419 | -1.6997 | -52.4535 | 2024-11-29 07:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| a91bfd9e-d81a-384c-9999-9a2b18a7bcba | -2.6498 | -48.7986 | 2024-11-29 07:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| f50e4b89-e043-3614-9fc8-b1aba4b98abc | -2.9844 | -53.3022 | 2024-11-29 07:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8480cf71-e7fb-3c33-913e-1eac668369bb | -2.6498 | -48.7986 | 2024-11-29 07:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 43d93a97-c839-3275-bdbc-9d5ec30f68c8 | -2.6499 | -48.7772 | 2024-11-29 07:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 84777a84-45af-30e9-af32-626ae68e5931 | -2.966 | -53.2824 | 2024-11-29 07:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| fd0cb349-28d5-30f1-8985-db5d040a7612 | -2.9844 | -53.2819 | 2024-11-29 07:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8576fab9-cd06-3505-81f1-e5c5e8a2b753 | -2.2299 | -53.6219 | 2024-11-29 07:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 88376b94-8460-31cc-aa36-0038653910cb | -1.6997 | -52.4535 | 2024-11-29 07:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1677a529-02c0-3596-a38c-b4f3651b0e9a | -2.6684 | -48.7767 | 2024-11-29 07:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c8189fd3-ba35-3a75-baad-5690ccbbad63 | -2.6683 | -48.7981 | 2024-11-29 07:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 1e5f25ff-67b2-3c51-b103-555433c61496 | -2.9844 | -53.3022 | 2024-11-29 08:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 086c872c-912d-3a75-ab7f-3bc3685d9316 | -2.6499 | -48.7772 | 2024-11-29 08:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 220.6 |
| ef76cea3-f065-3b10-b33c-d9d075817864 | -2.6683 | -48.7981 | 2024-11-29 08:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 310.2 |
| 5a2b69bd-da48-3d85-960f-b0aff4494792 | -2.2299 | -53.6219 | 2024-11-29 08:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 4e740f0a-6f24-336a-9d84-221b19d7487f | -2.9844 | -53.2819 | 2024-11-29 08:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 045e7e9a-3bb9-3ac5-81f4-1a90132efaac | -2.6684 | -48.7767 | 2024-11-29 08:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 248.9 |
| 0d7015b7-35bb-3a57-8704-8a8fafe01e18 | -1.6997 | -52.4535 | 2024-11-29 08:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| a81e437c-fa4a-3f6d-9609-e2a257a8637b | -2.6498 | -48.7986 | 2024-11-29 08:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 277.8 |
| a3537940-9427-3356-a16b-aa895b538298 | -6.52 | -35.19 | 2024-11-29 08:00:00 | MSG-03 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d0cfe00-d892-3b8e-a93a-866738973676 | -2.64 | -48.79 | 2024-11-29 08:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 672f997d-bacb-391f-93e3-08f5a9720900 | -6.95 | -43.52 | 2024-11-29 08:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5c92210c-ade9-324d-bde2-b6856c1f1daa | -6.95 | -43.48 | 2024-11-29 08:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9c2b95c3-bf36-3c54-b30b-96cdcd5e6901 | -2.67 | -48.79 | 2024-11-29 08:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8d9b60-df2c-3383-8669-1076e7e9e953 | -6.98 | -43.53 | 2024-11-29 08:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ff4c4b15-5e02-357a-a958-25be5649ab1d | -1.718 | -52.4532 | 2024-11-29 08:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3e490f8e-433b-3f67-a161-46204b8869a2 | -1.6997 | -52.4535 | 2024-11-29 08:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 2113e82b-43fc-3226-b337-18ba07d0f93f | -2.6683 | -48.7981 | 2024-11-29 08:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 463.7 |
| c939076a-d0a4-3c7a-b39e-441600f4b32e | -2.9844 | -53.2819 | 2024-11-29 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| e5cd89b5-d30a-39d4-b504-075a7013a3be | -2.6498 | -48.7986 | 2024-11-29 08:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 235.3 |
| d3f93a00-e7ed-370d-9259-d20a20a185bb | -2.2299 | -53.6219 | 2024-11-29 08:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 50887b17-48bb-3989-9103-0c3875c224e9 | -2.6684 | -48.7767 | 2024-11-29 08:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 275.4 |
| 085194f2-badc-3306-9fbc-7bfd56976d2a | -2.6499 | -48.7772 | 2024-11-29 08:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| d967764f-c3f0-35ad-9378-61186f1a743f | -2.2299 | -53.6219 | 2024-11-29 08:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| db0f99a0-5212-3d79-a287-c4e3d49a46ce | -1.6997 | -52.4535 | 2024-11-29 08:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| f1200112-d828-3c61-8c26-3bf694f8c1fd | -2.9844 | -53.2819 | 2024-11-29 08:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b34337c6-5840-3c45-9e6b-08c4cd103caa | -2.9844 | -53.2819 | 2024-11-29 08:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 5ab042cc-f2e3-346b-ae5a-a09cde0a582f | -2.2299 | -53.6219 | 2024-11-29 08:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 404f85c8-7f07-3e6e-95b3-93856fa98ae4 | -2.64 | -48.79 | 2024-11-29 09:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5a734b0-beec-3e28-a29e-a3ef9587df98 | -6.95 | -43.52 | 2024-11-29 09:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 68ec485d-3e0b-3a3f-ab0a-3e48785db6bc | -2.67 | -48.79 | 2024-11-29 09:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58ea67de-2592-3cba-92d1-15493857e607 | -2.6684 | -48.7767 | 2024-11-29 09:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 288.7 |
| fd7fe5f1-ad12-32e7-b26b-fe74c8f5700a | -2.6498 | -48.7986 | 2024-11-29 09:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 245.4 |
| f06d4b7c-7270-3772-897a-dbf9cbfa6e48 | -2.6499 | -48.7772 | 2024-11-29 09:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 015fd1f9-ea0c-3421-bb2d-c3d33695aa59 | -2.6683 | -48.7981 | 2024-11-29 09:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 447.0 |
| a8790827-09d8-39fc-ab3f-cb91d1b090d7 | -2.6683 | -48.7981 | 2024-11-29 09:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 454.5 |
| 49fa4d16-57d6-3aa0-96ad-29d6203fd2aa | -2.6498 | -48.7986 | 2024-11-29 09:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 183.4 |
| 693a1373-0313-35c4-af16-17e50a2b3828 | -2.6499 | -48.7772 | 2024-11-29 09:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 7090058c-ef97-3019-8b56-de162d011a93 | -2.6684 | -48.7767 | 2024-11-29 09:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 229.4 |
| 19031eb7-52e1-39b9-aa5c-37f714757cd2 | -2.2299 | -53.6219 | 2024-11-29 09:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| ff7cab41-4846-3a16-b8f5-648f03316459 | -2.6683 | -48.7981 | 2024-11-29 09:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 287.4 |
| 36a47e6f-68c1-351e-8378-f7cfa9bc1936 | -2.6684 | -48.7767 | 2024-11-29 09:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 161.6 |
| bc7bac16-0e0e-3904-8ef8-a846e322a2c4 | -2.6498 | -48.7986 | 2024-11-29 09:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| e09883ce-b4c1-337c-a9ab-ee339659676d | -2.6499 | -48.7772 | 2024-11-29 09:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| f4097e29-eb75-38e5-9973-11a8810d28f1 | -2.6498 | -48.7986 | 2024-11-29 09:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 167.6 |
| f26ce482-2650-3933-a466-d9ef36bdbf41 | -2.6684 | -48.7767 | 2024-11-29 09:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 79f04ae1-e67f-329e-8e70-dcaac688707d | -2.6499 | -48.7772 | 2024-11-29 09:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 323e7de4-f7e3-3096-93f6-aab042997ba1 | -2.6683 | -48.7981 | 2024-11-29 09:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 284.5 |
| 831ae7a9-c19c-3001-99cf-d93d11d5ff73 | -2.2299 | -53.6219 | 2024-11-29 09:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 0ca3e2d3-6b90-3a05-a74d-66ce054d40ca | -2.6684 | -48.7767 | 2024-11-29 09:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 8e5fcd8c-4cd0-3b53-8c95-24d55653a03d | -2.6498 | -48.7986 | 2024-11-29 09:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 185.1 |
| 09bd7c41-a6f7-3935-95aa-60e3343abc63 | -2.6683 | -48.7981 | 2024-11-29 09:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 637b5314-8c60-3c5f-beab-10816ff31aa6 | -2.2299 | -53.6219 | 2024-11-29 09:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 7396c98d-e96e-3bfc-85e5-58342a6bd5d4 | -2.6499 | -48.7772 | 2024-11-29 09:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| cc265f23-ce6e-33d2-929a-112a0299db27 | -2.6683 | -48.7981 | 2024-11-29 09:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 246.6 |
| 302b172b-1184-3daa-8130-6a6c16dbd644 | -2.2299 | -53.6219 | 2024-11-29 09:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 85377033-8345-311a-88fc-d3ea971e4600 | -2.6498 | -48.7986 | 2024-11-29 09:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 7c32510c-1f19-30e1-a8a6-c41abc5488ec | -2.6684 | -48.7767 | 2024-11-29 09:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 9d757871-85e6-379d-8802-fd2374f026e5 | -2.6683 | -48.7981 | 2024-11-29 10:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 237.7 |
| c602a73e-92d4-36be-a9eb-cd0f0f7fbe7e | -2.6684 | -48.7767 | 2024-11-29 10:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 152.4 |
| 37b092f1-337e-3fa4-910e-25119c7d60bf | -2.6498 | -48.7986 | 2024-11-29 10:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| bb1838bb-6f20-3147-aacd-64aff37c34c9 | -2.6499 | -48.7772 | 2024-11-29 10:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 2933b19b-946c-3e94-bed4-b863ff703861 | -2.6498 | -48.7986 | 2024-11-29 10:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 202.5 |
| 49519ec1-3c49-35e5-9607-d0477ee82357 | -2.6683 | -48.7981 | 2024-11-29 10:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 230.1 |
| 3bd183cb-d5bb-3dec-8b07-e3b5cd8b7b25 | -2.6684 | -48.7767 | 2024-11-29 10:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 5528d114-1831-30ff-a1eb-2910aef855bb | -2.6684 | -48.7767 | 2024-11-29 10:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 96e29e0c-39a2-33f9-822e-e13682181f06 | -2.6498 | -48.7986 | 2024-11-29 10:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 169.8 |
| 2d77f7ea-01f6-36e7-bb1d-87df12cb84f8 | -2.6683 | -48.7981 | 2024-11-29 10:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 365.0 |


[Clique aqui para ver as próximas entradas](README109.md)
