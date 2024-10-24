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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f85026db-e5f0-3557-a9cf-8d921e15d58c | -19.6457 | -56.7471 | 2024-10-24 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.0 |
| 1c26be6a-ab3d-38e4-a7a5-b44899429c58 | -19.5866 | -56.6926 | 2024-10-24 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |
| ebb90a85-6e30-385a-9c4a-5ee1ca390c5f | -19.5469 | -56.6773 | 2024-10-24 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 1dbab241-0daf-3619-aaad-590e55977053 | -16.9792 | -57.5223 | 2024-10-24 10:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 153.6 |
| 6ee95835-af26-357a-a960-66367a9501f9 | -19.5866 | -56.6926 | 2024-10-24 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 140.4 |
| 353ed602-fe1a-3f4e-9512-869a40dc3400 | -19.6461 | -56.7261 | 2024-10-24 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| a6f177fa-b8a8-353c-a062-935b3be4a342 | -19.5669 | -56.6744 | 2024-10-24 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 0cb53d41-5559-3855-9d0d-88ef80db4a0f | -19.5666 | -56.6954 | 2024-10-24 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 4983b295-4c22-3ced-a7ab-430812ab715a | -19.5469 | -56.6773 | 2024-10-24 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 261ce712-a4d8-393f-90d6-5cc6c048c4ba | -19.587 | -56.6716 | 2024-10-24 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 96a53700-ddab-3405-b19e-b106f0ff3800 | -19.6457 | -56.7471 | 2024-10-24 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 138.3 |
| e4df6f58-5777-3f6e-9e6c-18c7892b1117 | -16.9792 | -57.5223 | 2024-10-24 10:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 181.7 |
| 0375b956-7d76-3bb2-95fc-78937dbe4ffa | -19.5071 | -56.6619 | 2024-10-24 10:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| e081dfa6-57b8-36c9-8bd6-ed6b13f2d75f | -19.6453 | -56.7681 | 2024-10-24 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| efb841d8-f82d-3654-8198-8d3d5d81c4e7 | -19.587 | -56.6716 | 2024-10-24 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 9eff193a-05f7-342b-ba9b-547885b9e706 | -19.6457 | -56.7471 | 2024-10-24 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 137.8 |
| b0220771-11dd-3969-84f4-39ce6adad198 | -19.6461 | -56.7261 | 2024-10-24 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 124.8 |
| 76d14826-92a7-3c34-8938-92b99891a2f7 | -19.5866 | -56.6926 | 2024-10-24 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 166.0 |
| f45fb839-4e7f-3f10-b786-2d43a25dd76d | -19.5669 | -56.6744 | 2024-10-24 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| c008f6ec-e60c-3d01-8fea-f9a30a073309 | -19.5666 | -56.6954 | 2024-10-24 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| a2da7696-6688-32ab-8ac6-73050b1017be | -19.5469 | -56.6773 | 2024-10-24 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| a6078e29-7eab-3516-af18-636fc8a735f3 | -16.9792 | -57.5223 | 2024-10-24 10:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 142.0 |
| 18745a35-9e2d-3df8-aa6f-876649f5c14a | -18.2641 | -56.0394 | 2024-10-24 10:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.4 |
| a4ed2773-457c-3562-afe6-dac056213286 | -19.5071 | -56.6619 | 2024-10-24 10:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 7485bd42-9901-3fc9-9876-9df583438950 | -19.5075 | -56.6409 | 2024-10-24 10:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.6 |
| c95cf278-8d3f-3f94-9abd-875072fe3efb | -19.6662 | -56.7233 | 2024-10-24 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 232e8706-fec7-39cd-b51f-9bcc9bfa676a | -19.5469 | -56.6773 | 2024-10-24 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| b49b3faa-a0d1-3ace-9bfd-2c316eb6344e | -19.5666 | -56.6954 | 2024-10-24 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.0 |
| c1645439-ab13-3d0f-b819-ca4bd57b28dd | -19.5669 | -56.6744 | 2024-10-24 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.7 |
| 3afce579-7aaa-3e74-a4f7-3c3d3aef1228 | -19.5866 | -56.6926 | 2024-10-24 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 164.2 |
| 4e6e6081-a0f9-332e-a367-551eb3a69fea | -19.587 | -56.6716 | 2024-10-24 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 2e65b4ce-aec4-3649-b09a-71a5cf0eacbd | -19.6453 | -56.7681 | 2024-10-24 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 0c5d5317-8330-3db6-8116-f9160fe0838d | -19.6457 | -56.7471 | 2024-10-24 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 153.6 |
| 07045ceb-dbda-35d9-ae65-9fe54db2ad19 | -19.6461 | -56.7261 | 2024-10-24 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 148.1 |
| d171d623-20c3-3e75-884c-d05c999288be | -16.9792 | -57.5223 | 2024-10-24 11:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.4 |
| d32ba3c3-9bd0-3651-846d-eadc99c02ce8 | -16.9596 | -57.5245 | 2024-10-24 11:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.3 |
| af69c6b0-8a20-37d5-8df6-c90c936305e7 | -17.2383 | -57.2462 | 2024-10-24 11:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 225da775-33ab-3efd-91b4-c9b8ddb7fc54 | -18.2641 | -56.0394 | 2024-10-24 11:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 43bdb7e5-da15-35ff-90bd-1fcafb3adc4b | -18.2637 | -56.0603 | 2024-10-24 11:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 988f1753-2819-391b-824e-c55c5f599cb4 | -19.5075 | -56.6409 | 2024-10-24 11:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.0 |
| abfc4560-c4e2-37e0-9ce8-aead040e4fc5 | -19.5071 | -56.6619 | 2024-10-24 11:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.1 |
| b85d3627-20e2-32c9-a2af-33a57bd25f18 | -19.6457 | -56.7471 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 183.8 |
| 7fa42461-00de-353d-b873-5debbf37cfac | -19.6256 | -56.7499 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| d5d27f8e-7b73-303a-a2cd-86fa548159a2 | -19.5669 | -56.6744 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 159.0 |
| b0733bfd-3e0b-3c21-85a3-4eb2ebe0276b | -19.6453 | -56.7681 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 17e10a08-9b7a-3150-bb48-c5977836dc51 | -19.6461 | -56.7261 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 160.3 |
| 0db58c63-03f8-3427-81a4-d77848f11bbb | -19.587 | -56.6716 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 123.4 |
| ba8e1145-f4f9-3333-aa00-0d7fd1c75edb | -19.5866 | -56.6926 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 186.8 |
| 66d633ae-1de8-36c0-80d1-dda0ef36f368 | -19.6658 | -56.7443 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| ace1c023-fbb8-3bd5-9d2b-93ea71986a3b | -19.5469 | -56.6773 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 9429d168-9164-3abd-904c-d9cb565d7273 | -19.5666 | -56.6954 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 162.3 |
| 51b89558-5f57-3be0-8ec9-9591435b6cfc | -19.6662 | -56.7233 | 2024-10-24 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.9 |
| 1af318a8-1389-3f74-9b84-8043286cd2b6 | -16.9792 | -57.5223 | 2024-10-24 11:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| f9c2a7a1-07da-3685-bc5f-f7c550b2495c | -16.9596 | -57.5245 | 2024-10-24 11:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.7 |
| ef41b757-3135-35ef-8213-89ecdf3b7d29 | -17.2383 | -57.2462 | 2024-10-24 11:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| ed70642c-441a-3710-9277-a4d32e74f777 | -18.2641 | -56.0394 | 2024-10-24 11:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 3f3a953a-8f5a-3f16-a60a-0beccae453e4 | -18.2637 | -56.0603 | 2024-10-24 11:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.8 |
| a3a27a13-4c2f-3187-b721-4d1e9883fd3d | -19.5075 | -56.6409 | 2024-10-24 11:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.8 |
| b325be74-72b0-39bc-9857-559034be4bf1 | -19.5071 | -56.6619 | 2024-10-24 11:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.1 |
| 3a404be9-2b45-3054-8bb7-394ca2cf9e76 | -16.9596 | -57.5245 | 2024-10-24 11:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| b519e258-191d-3d68-95ba-a90e1d70510e | -16.9792 | -57.5223 | 2024-10-24 11:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 29100b85-b31a-38a2-bbfe-b9d59635023b | -17.2383 | -57.2462 | 2024-10-24 11:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 178.7 |
| fe4e7828-791e-3d8e-9446-883ac9847f2d | -17.2386 | -57.2256 | 2024-10-24 11:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 9a1a159a-1edb-3d98-9d20-a4c6a2a8419d | -17.2579 | -57.2439 | 2024-10-24 11:26:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 480845be-0a82-3769-a8b3-fb4f55c7c31e | -19.5681 | -56.6114 | 2024-10-24 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.2 |
| e7d4d669-d625-3c71-b649-5bfe1d5632df | -16.9596 | -57.5245 | 2024-10-24 11:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 03233387-5175-35ae-90c5-549c8a9b0ce5 | -16.9792 | -57.5223 | 2024-10-24 11:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| c1fe6ff5-ecf5-33b4-8182-c80370e04b70 | -17.2383 | -57.2462 | 2024-10-24 11:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 174.1 |
| 7cb1c6e9-199f-3938-8743-38ec038e905c | -17.2386 | -57.2256 | 2024-10-24 11:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| 6d8e5068-9d04-34a8-8a35-4cd131b6a84d | -17.2579 | -57.2439 | 2024-10-24 11:36:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 697b1019-25ac-36eb-8346-8760aa49c016 | -18.0837 | -57.3076 | 2024-10-24 11:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| c8d1f613-cded-33eb-8c2e-debd95843a4a | -18.2641 | -56.0394 | 2024-10-24 11:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 189.2 |
| 833747cc-e398-3a23-81fb-feb8be7f3b80 | -18.284 | -56.0367 | 2024-10-24 11:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 420693a7-0d18-3b38-8881-68df8617f355 | -18.2637 | -56.0603 | 2024-10-24 11:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 152.9 |
| 2e8c86eb-aae6-37bc-a32f-d8f9fcd0e78a | -18.2836 | -56.0576 | 2024-10-24 11:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 3f7879eb-fe4a-3ae3-ae78-d25ea4607059 | -19.6438 | -56.8521 | 2024-10-24 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 34a24359-2457-365a-b8c2-522b397b53a0 | -19.5681 | -56.6114 | 2024-10-24 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 10af4ced-c482-3a1c-87a3-f4cbc78c2ddd | -17.0387 | -57.4745 | 2024-10-24 11:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| bf6838f8-2f6d-3487-9891-759b63b47228 | -16.9792 | -57.5223 | 2024-10-24 11:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| d071d47e-84e3-3d33-bacb-e1430d4ca26f | -16.9596 | -57.5245 | 2024-10-24 11:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 87cffda2-ddf4-3107-b77e-59956463b763 | -17.0188 | -57.4973 | 2024-10-24 11:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 3a818033-9eff-3c75-b65a-5e7bb9fffb50 | -17.2383 | -57.2462 | 2024-10-24 11:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 438.0 |
| 4ee681bd-585e-383d-a329-4e2328bac25d | -17.2386 | -57.2256 | 2024-10-24 11:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 296.7 |
| a417c8ca-97ec-3fbf-82ec-9d1a23992014 | -17.2583 | -57.2233 | 2024-10-24 11:46:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| 24ba8d49-108e-32f4-99e5-6a372e0cd7d6 | -17.2579 | -57.2439 | 2024-10-24 11:46:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.9 |
| 2d88285b-f398-310d-953f-41c28d285ab9 | -17.7082 | -57.3539 | 2024-10-24 11:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 170279ec-5496-374f-ab37-eb45b8abfbcd | -17.764 | -57.5526 | 2024-10-24 11:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 33b6ff1b-7ac4-3028-9063-d3e51fb21b9d | -17.6868 | -57.4593 | 2024-10-24 11:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| fc1c2485-863c-3435-a5c9-38fd85b3aba8 | -18.0837 | -57.3076 | 2024-10-24 11:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 451dd63a-bce5-3ae8-bfb4-bf7ffdfc11b7 | -18.2641 | -56.0394 | 2024-10-24 11:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 230.1 |
| a20be620-a4c5-380f-94eb-69bf87a3fc4e | -18.2637 | -56.0603 | 2024-10-24 11:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.7 |
| 53608c90-93ae-3071-815d-b6fec6e44955 | -18.284 | -56.0367 | 2024-10-24 11:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 185.4 |
| f6e2dbcc-824f-3e9b-9af0-b971f4bff394 | -18.2836 | -56.0576 | 2024-10-24 11:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 09f445dd-e096-33a3-a68f-8c22e16893e8 | -19.6438 | -56.8521 | 2024-10-24 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| afcb1c23-5293-39ab-b877-6a2e4c71689e | -19.5693 | -56.5484 | 2024-10-24 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 7b3d5976-3f4d-3082-a3fc-e967aa0a05eb | -19.5681 | -56.6114 | 2024-10-24 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 308fa665-e0ee-3638-bc69-f7f75c1fc1c1 | -16.9792 | -57.5223 | 2024-10-24 11:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.5 |
| 84d2212e-a567-3d47-906f-78d774d9ed47 | -17.0184 | -57.5178 | 2024-10-24 11:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| f32c555e-d664-3198-b2a7-a213257f3878 | -17.0188 | -57.4973 | 2024-10-24 11:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| a3ab9c64-ee84-3db6-8f50-36f789d32f31 | -17.2386 | -57.2256 | 2024-10-24 11:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 209.5 |


[Clique aqui para ver as próximas entradas](README114.md)
