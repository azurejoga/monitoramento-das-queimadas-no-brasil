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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43194764-4096-34f7-b3d9-eaf1d6d6a085 | -19.6268 | -56.6869 | 2024-10-25 11:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| e9115e96-4e5c-3419-9f5b-7d00e018c049 | -17.2386 | -57.2256 | 2024-10-25 11:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 199.0 |
| e388e63e-c781-36fe-9d24-5cb86c89e797 | -17.219 | -57.228 | 2024-10-25 11:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.1 |
| 2965117e-46f5-3629-a47c-1d8adc42903f | -17.2383 | -57.2462 | 2024-10-25 11:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.1 |
| 1d9b240d-30f4-3669-80b4-b8203b2911f0 | -17.2186 | -57.2485 | 2024-10-25 11:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.5 |
| b4386dd9-26d2-3e86-85e5-462e3a1763dd | -17.7644 | -57.532 | 2024-10-25 11:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.7 |
| caff3395-c934-31eb-9ab3-9c51e6f194c0 | -17.8628 | -57.5407 | 2024-10-25 11:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.9 |
| 1b2771e8-9e90-301a-ac60-4ab2bddd5a19 | -19.6071 | -56.6688 | 2024-10-25 11:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 9ceb63b0-e2e0-33a2-9c96-1b40a8161d53 | -17.2186 | -57.2485 | 2024-10-25 11:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 167.7 |
| dd004a50-7135-3569-a4cb-cb193dd50001 | -17.2383 | -57.2462 | 2024-10-25 11:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 3d85463b-d73c-304f-a3ad-d06f341eb8c3 | -17.219 | -57.228 | 2024-10-25 11:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 270.6 |
| 9b298808-1aa5-31a2-8a4d-900bc3c0bb55 | -17.2386 | -57.2256 | 2024-10-25 11:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.5 |
| 4f6a77ab-aa9d-3d83-96f4-a3215bce9b58 | -17.7446 | -57.5344 | 2024-10-25 11:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 343b4ea7-a27a-3971-a3cd-33fddc7ef958 | -17.7644 | -57.532 | 2024-10-25 11:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 7912cf22-7f13-337c-aae7-f040d59c3c29 | -18.0431 | -57.3745 | 2024-10-25 11:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 1adff7ba-204c-3260-9be2-d9cfa04961fa | -19.6272 | -56.6659 | 2024-10-25 11:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.8 |
| 371a17e7-af42-35b2-bee0-612514ce7648 | -19.6268 | -56.6869 | 2024-10-25 11:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| e5320212-61c1-35e6-823a-8c0f47fe4b83 | -19.667 | -56.6813 | 2024-10-25 11:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 2915afad-8489-3813-b579-c799fb937fc9 | -17.0014 | -57.3561 | 2024-10-25 12:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 4a168675-3f69-36e7-98e7-6c143452704e | -17.239 | -57.2051 | 2024-10-25 12:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 990ca8f1-95ea-3422-ada9-26f8d43202c1 | -17.2383 | -57.2462 | 2024-10-25 12:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.9 |
| 9f746212-9034-38ae-93d3-5bec9840dc52 | -17.2386 | -57.2256 | 2024-10-25 12:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 303.3 |
| eea7a3c9-06fd-3100-bb71-cdc43988634c | -17.2186 | -57.2485 | 2024-10-25 12:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.9 |
| 8dfdeae4-ce25-3997-930c-1182939e845d | -17.219 | -57.228 | 2024-10-25 12:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 350.4 |
| 921d1d26-fe0e-3144-8e14-f6fcb340a8b9 | -17.7644 | -57.532 | 2024-10-25 12:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 7d80ed6c-ea33-37cd-80c5-9b3c91aaeef4 | -17.7453 | -57.4933 | 2024-10-25 12:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 3b87029f-1094-3108-922a-bc639e8aa4d6 | -17.8825 | -57.5383 | 2024-10-25 12:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 714a85a3-65d5-38bc-9613-f19513f02c6d | -18.0452 | -57.2506 | 2024-10-25 12:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 8ad029dd-e9d3-33fa-a0a7-e1bc8481ae0f | -18.0431 | -57.3745 | 2024-10-25 12:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| e343c83b-82d3-3620-bd7f-1641b5001466 | -18.2645 | -56.0184 | 2024-10-25 12:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.6 |
| 75a3b6c2-0d3e-3c7c-a209-9091fd2e26f8 | -18.321 | -56.1777 | 2024-10-25 12:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 0da2b8c8-13f2-37ac-9007-9c6d5e2732c9 | -19.6666 | -56.7023 | 2024-10-25 12:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 9baf28f7-ad96-320d-924d-f6d50e2e42f3 | -19.6071 | -56.6688 | 2024-10-25 12:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 7ca1f16e-8c88-3006-8005-936654a90162 | -19.6268 | -56.6869 | 2024-10-25 12:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| a9015f0b-f3bb-3423-a414-ae2aad97cb3f | -19.667 | -56.6813 | 2024-10-25 12:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.5 |
| f71903a2-9efd-3a56-b6ce-9ce7819493af | -19.6465 | -56.7051 | 2024-10-25 12:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 3e42b272-b4b7-3544-a5ad-8b0405ace526 | -17.0014 | -57.3561 | 2024-10-25 12:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 295b5f2e-4448-3000-a30d-2dce4a2f8170 | -16.9596 | -57.5245 | 2024-10-25 12:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 029e330e-7366-38f6-aaf7-babb71ce7c42 | -17.219 | -57.228 | 2024-10-25 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 228.1 |
| 9dbeae3a-c899-3985-b7a0-29f9d920e53a | -17.2186 | -57.2485 | 2024-10-25 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.1 |
| 0fd6a6d5-866f-3cd0-97dd-bb413c4a5019 | -17.2383 | -57.2462 | 2024-10-25 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| a02640bd-1ac4-39ac-afb3-12be14e96e17 | -17.2386 | -57.2256 | 2024-10-25 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 208.4 |
| ece241fb-e450-3864-a4be-d7950fb463dc | -17.7453 | -57.4933 | 2024-10-25 12:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| dc68c7ea-541b-3871-9d26-1f2947e1f28c | -17.765 | -57.4909 | 2024-10-25 12:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 2c64e0ba-50a8-3e5a-80b7-3a69568ee7bb | -17.7644 | -57.532 | 2024-10-25 12:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.7 |
| 92442aa0-f47f-30c9-8cfa-296736f9806f | -17.7446 | -57.5344 | 2024-10-25 12:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 3705d752-105a-30d2-a356-52d2155044df | -17.7647 | -57.5115 | 2024-10-25 12:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| 48e9728b-ac7f-3d69-8daa-cc1ed6cb614d | -17.8628 | -57.5407 | 2024-10-25 12:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.6 |
| a67f3d0a-0afc-3c8d-b7f9-254b2db6210b | -17.8825 | -57.5383 | 2024-10-25 12:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 0c384f30-7d2d-3e5d-8610-3683ea251178 | -17.9272 | -57.224 | 2024-10-25 12:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| f5df1009-31fe-3208-9db8-63ebe1bbe84e | -18.0452 | -57.2506 | 2024-10-25 12:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 37da0731-3fd0-3a4d-b7bd-2ff2df0cb66e | -18.0431 | -57.3745 | 2024-10-25 12:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.8 |
| 11e2dae2-03f3-370f-a41e-30ec306616cf | -18.321 | -56.1777 | 2024-10-25 12:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 89b9ce01-2334-3750-b5e4-6b154a81fa54 | -13.0553 | -43.0478 | 2024-10-25 12:26:18 | GOES-16 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 130.0 |
| e4c68d35-dbd2-321f-a474-4ebd903533b3 | -17.2386 | -57.2256 | 2024-10-25 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 186.0 |
| a9295f11-fde8-305e-acb5-4db44d87d5eb | -17.219 | -57.228 | 2024-10-25 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 205.6 |
| 771fd597-498a-3dce-b7c6-54468de5980c | -17.0789 | -57.4085 | 2024-10-25 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| ff12326c-6055-328c-b05d-2e9caaac866b | -17.2383 | -57.2462 | 2024-10-25 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| d0bba22f-5fb8-36f8-b461-9639c1d49bac | -17.2186 | -57.2485 | 2024-10-25 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| cea5cef1-1222-302d-a9cd-de60d00a2d76 | -17.7647 | -57.5115 | 2024-10-25 12:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 8955b05a-bd6c-3c4a-9d2e-e29b10a778fd | -17.7644 | -57.532 | 2024-10-25 12:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.1 |
| c7b218d7-7068-378f-970a-7d01c21e2850 | -17.765 | -57.4909 | 2024-10-25 12:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| 3127e52d-dc13-3d8d-833b-fcd0d51030ea | -17.7453 | -57.4933 | 2024-10-25 12:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.7 |
| 674ab5d0-b172-3b59-8e78-2f9320019403 | -17.9272 | -57.224 | 2024-10-25 12:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| df99a96c-ffb2-3bb7-b49f-826202f280b7 | -17.8628 | -57.5407 | 2024-10-25 12:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.5 |
| ab0a1e0b-123d-325f-bcd0-5f6c08383b33 | -17.9268 | -57.2447 | 2024-10-25 12:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 16e9f714-73c7-38c0-83cb-4546b086edaa | -18.0452 | -57.2506 | 2024-10-25 12:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.4 |
| 88fd4aa5-476a-30ce-9763-f9d6bfc83d52 | -18.0431 | -57.3745 | 2024-10-25 12:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 80544614-c291-38a9-9e00-a3d26cc5928d | -18.3012 | -56.1804 | 2024-10-25 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 4d851b8c-a141-39d3-ac08-cca168681512 | -18.321 | -56.1777 | 2024-10-25 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.7 |
| 4b7c6ab7-f505-3b2f-ae1a-7fe154456959 | -18.2641 | -56.0394 | 2024-10-25 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 06829c4c-06c0-3227-915f-d95e1e830abb | -18.2645 | -56.0184 | 2024-10-25 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.2 |
| f30cca69-df12-3d7a-981e-68c8ec5c60f9 | -19.6438 | -56.8521 | 2024-10-25 12:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 884486e1-164b-3290-85ee-910d79477694 | -16.9596 | -57.5245 | 2024-10-25 12:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 193c51f2-5fd4-33f6-87c5-b8050ca25a7f | -17.2186 | -57.2485 | 2024-10-25 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 260.3 |
| ea0eb412-2909-3ae3-94cb-38ad95e1e26c | -17.2383 | -57.2462 | 2024-10-25 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 195.1 |
| e064881b-cefa-33a9-803a-b78966d28171 | -17.0789 | -57.4085 | 2024-10-25 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 147.4 |
| 1816d552-aa6d-3e3c-b6cb-b698bf3a1b22 | -17.219 | -57.228 | 2024-10-25 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 641.5 |
| 3ce8994c-3592-3b56-965d-50c108be8b35 | -17.2386 | -57.2256 | 2024-10-25 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 693.1 |
| 5b9fb71e-49e5-3645-98d6-40f834add239 | -17.0786 | -57.429 | 2024-10-25 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| eceefbcd-fb5a-3db2-9bd8-fed463a220fc | -17.2583 | -57.2233 | 2024-10-25 12:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| f60b64fc-642b-3600-8894-8335bf05688d | -17.2966 | -57.2803 | 2024-10-25 12:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| cfbdb753-5b54-37dc-b067-3133c28ab3e3 | -17.7453 | -57.4933 | 2024-10-25 12:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.0 |
| b91a7a21-606f-3726-b8f3-20661e52221e | -17.765 | -57.4909 | 2024-10-25 12:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 6aa3136c-72ef-3763-9bfa-2fc74a15b254 | -17.7644 | -57.532 | 2024-10-25 12:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.2 |
| 6e3e927e-eba3-3feb-8c1b-95f5e0f064f7 | -17.7647 | -57.5115 | 2024-10-25 12:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 04ce8314-186f-3740-b74d-aab68611b3f7 | -17.7446 | -57.5344 | 2024-10-25 12:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| a24cd454-b9bf-3ae7-8103-f020e7195ebd | -17.8222 | -57.6072 | 2024-10-25 12:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 51878c47-30cb-39c0-b07e-69665ed35c8b | -17.9268 | -57.2447 | 2024-10-25 12:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| be9eefb2-5280-301d-baa3-5e4ae838b2e4 | -17.9071 | -57.2472 | 2024-10-25 12:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 8bec6643-5405-377a-869f-f7108884e7e8 | -17.9272 | -57.224 | 2024-10-25 12:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 697d92a7-b45e-394b-ab0c-cf3af6c50da7 | -17.8825 | -57.5383 | 2024-10-25 12:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 3ef88780-e0b8-335f-a63c-2743b3c003f6 | -17.8628 | -57.5407 | 2024-10-25 12:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| e4317ed9-b8d8-3b05-97c9-22dd7906c5d8 | -18.0441 | -57.3126 | 2024-10-25 12:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| d8149f49-ebda-3817-972d-8b260f6f500a | -18.0431 | -57.3745 | 2024-10-25 12:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.4 |
| 3c2d50c5-af8f-3e47-8da5-0719169e9923 | -18.0452 | -57.2506 | 2024-10-25 12:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.8 |
| dbaf3c2b-4c0f-385e-aa8e-dc07a383b3c1 | -18.0434 | -57.3539 | 2024-10-25 12:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 228fa201-5383-31f8-91f4-0bb110d7c7b4 | -18.2645 | -56.0184 | 2024-10-25 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.8 |
| 59a60a17-04a2-36e7-9e9d-d1aa2c22c6f8 | -18.3004 | -56.2222 | 2024-10-25 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 94bbad99-f975-3c2d-b979-c2733042fe8e | -18.2641 | -56.0394 | 2024-10-25 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.7 |


[Clique aqui para ver as próximas entradas](README113.md)
