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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a88acf9-02e6-355b-875b-1f3baccf6083 | -8.1244 | -44.7871 | 2024-10-04 00:55:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 00f849a6-4287-38fe-92a5-701c754199ef | -8.3128 | -49.5679 | 2024-10-04 00:55:53 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 49651d04-82a3-3f96-9db6-14b7d478fce2 | -8.6448 | -50.0518 | 2024-10-04 00:55:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| f64032c5-da38-3272-8b3b-5425a2be98fd | -9.1041 | -50.902 | 2024-10-04 00:55:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 375e5d49-f66f-320f-9b06-187688b9522e | -9.1158 | -51.5315 | 2024-10-04 00:55:58 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 479e3bc7-e053-3556-b2ac-11ad8b72381f | -9.0898 | -67.4997 | 2024-10-04 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 5a5af50d-2625-309b-ac2d-b9290901a2d7 | -9.3115 | -50.8203 | 2024-10-04 00:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 236.7 |
| f0fff3ce-c0d5-3809-be0b-33c465ac618f | -9.3118 | -50.7991 | 2024-10-04 00:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 306.1 |
| fb9bcb4f-c413-3567-8d73-17a556604031 | -9.312 | -50.7779 | 2024-10-04 00:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c3c9a554-c94a-3746-85f7-add0be3974ca | -9.3303 | -50.8186 | 2024-10-04 00:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 56eceaf3-01c1-3b9d-a082-6abe5825b73a | -9.3306 | -50.7974 | 2024-10-04 00:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| a3500b7a-9244-3622-b82c-55ed277bde56 | -9.55 | -64.2179 | 2024-10-04 00:56:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 73be3779-fc84-3b1a-9493-79701123d677 | -9.5686 | -64.2171 | 2024-10-04 00:56:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 96139c95-b6dc-39bd-b09f-e30273565ec7 | -9.5687 | -64.1983 | 2024-10-04 00:56:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 9c7164e6-ed0e-3fba-a4ba-47b631d26081 | -9.8349 | -46.7726 | 2024-10-04 00:56:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 02407a83-083a-3e4d-8539-09578045b30c | -9.8353 | -46.7502 | 2024-10-04 00:56:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 0978e3cd-a5b5-31ef-addb-a02439777c92 | -9.8539 | -46.7704 | 2024-10-04 00:56:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 2c5f57b2-6b66-3e77-953f-6deed523b7b2 | -9.9375 | -64.7675 | 2024-10-04 00:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e45c08cc-dd66-3d64-bc2c-6afe9846b682 | -9.9561 | -64.7668 | 2024-10-04 00:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 5c678cbe-2c40-3738-9642-0043a8bd9aea | -9.9747 | -64.7661 | 2024-10-04 00:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8a1c261c-37b3-352a-b14d-616c8cf7ec5d | -10.4424 | -50.7336 | 2024-10-04 00:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 52a353e9-12c8-39ad-b020-30d677892a97 | -10.4613 | -50.7317 | 2024-10-04 00:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| fd82ec65-c937-36ad-9c81-879a76f09091 | -10.8992 | -46.6442 | 2024-10-04 00:56:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 80624e7a-f54c-36ad-b2d3-34bef1392b8e | -10.8996 | -46.6216 | 2024-10-04 00:56:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d75d2d51-1996-3685-8cb2-50366c98fbb0 | -11.0532 | -46.5344 | 2024-10-04 00:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b21583d7-b24e-397a-b9bf-172c6b3e3c5f | -11.0536 | -46.5118 | 2024-10-04 00:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 2425eb17-52ab-35e0-a0ec-bd0a8402fd57 | -11.5238 | -65.0615 | 2024-10-04 00:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 5c02355e-28ec-35a4-970e-95ad8152e401 | -11.5425 | -65.0607 | 2024-10-04 00:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| bb96b58e-1a0e-3187-a85a-82ead11fd744 | -11.5991 | -65.0204 | 2024-10-04 00:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 467e1d22-9f49-3dff-81d2-3ff922fd6a5b | -11.5992 | -65.0015 | 2024-10-04 00:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 7f30b8c0-3bc0-39e5-b7da-145b496a8827 | -11.618 | -65.0007 | 2024-10-04 00:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1ee92166-4ce8-3231-923b-9e510d6260a5 | -11.6181 | -64.9818 | 2024-10-04 00:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 6ed6148c-da78-3d4a-a497-67c41914ecbb | -11.6369 | -64.981 | 2024-10-04 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 906462b2-b64c-3c7f-91bb-c2f4c7ec7075 | -11.6744 | -64.9793 | 2024-10-04 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a32e849e-b0fd-3b54-9a78-bc0265e3bd2f | -11.6932 | -64.9785 | 2024-10-04 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 55dd55e3-f11f-300d-bb10-765a48e2ecc8 | -11.712 | -64.9777 | 2024-10-04 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 589ee921-ff33-3015-a821-6d5310c18f71 | -11.8052 | -56.6024 | 2024-10-04 00:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| dd55905e-91e3-34da-a963-c1bd89117bb3 | -11.8242 | -56.6009 | 2024-10-04 00:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| f948ed98-39f9-39c0-8452-43fa6f6168fd | -11.8244 | -56.5808 | 2024-10-04 00:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8770fc3f-b503-3509-81ac-cd4975c23a8b | -12.5898 | -53.1359 | 2024-10-04 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 57898873-622c-32da-b142-8888e0ea8fe0 | -12.5901 | -53.115 | 2024-10-04 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 186.6 |
| 78f01c3b-2fed-3cf9-ad00-e3380976c68e | -12.6295 | -63.1225 | 2024-10-04 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 5996cf1e-4b41-3aab-aac5-5bf89e95d740 | -12.6296 | -63.1033 | 2024-10-04 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| aac59d28-a70c-39a7-a965-bcaeeb118cae | -12.6484 | -63.1214 | 2024-10-04 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 67892ceb-0195-3f15-8132-20339df122ee | -12.6486 | -63.1022 | 2024-10-04 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| be3c2209-5f82-3aa3-8b81-0733e8b5b82a | -12.9831 | -51.129 | 2024-10-04 00:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 1c33da0b-54c0-3c1d-b80c-718ef5837ad5 | -12.881 | -62.4538 | 2024-10-04 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 540dcde0-a8d5-38a7-a562-121c136ee7d4 | -12.8999 | -62.4527 | 2024-10-04 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 9ac3166f-78dc-333e-96e6-67fa8f24564e | -12.9186 | -62.4901 | 2024-10-04 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 283b6fe4-6450-3ee4-8b44-2b669b10e5bc | -12.9187 | -62.4708 | 2024-10-04 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6ceda524-1c81-350e-baa1-c2f430f5d06b | -14.004 | -44.0201 | 2024-10-04 00:56:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 6b1512b5-8661-3eed-8ae8-a58759ad371b | -14.7939 | -48.0275 | 2024-10-04 00:56:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| e3f11299-8096-336d-9cb7-16068cd2bef8 | -14.7944 | -48.005 | 2024-10-04 00:56:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 51b27846-9cfa-389b-8eb2-68ad562e1e96 | -16.0929 | -50.2983 | 2024-10-04 00:56:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 00781824-0ff2-3909-8a1a-ed21b39a7811 | -16.3552 | -49.9256 | 2024-10-04 00:56:37 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 83557825-a941-311c-9a74-249055639eed | -16.3749 | -49.9223 | 2024-10-04 00:56:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 31168096-ec41-3930-9fa3-888aa3ebb46b | -16.4148 | -57.4028 | 2024-10-04 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| a56a8e8b-ccf1-3303-94ba-9ae86ce2cd9e | -16.4151 | -57.3823 | 2024-10-04 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 87f90ec3-93f7-3111-9422-c78a458fd433 | -16.4554 | -57.2962 | 2024-10-04 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| e504656d-4f25-3789-8d13-9159236974db | -16.475 | -57.294 | 2024-10-04 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 667b57c5-b8aa-3e24-bf9d-690b3e1c41b9 | -16.5783 | -58.198 | 2024-10-04 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.1 |
| a7332323-0ef3-3622-9fdc-8235d8be5f9d | -16.5935 | -57.1988 | 2024-10-04 00:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 7d8cdac9-452c-3f4f-b64d-c4314229f3e9 | -16.5938 | -57.1783 | 2024-10-04 00:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| c2c77fa0-fce3-3ff8-b073-8e76d5117ede | -16.9302 | -47.1224 | 2024-10-04 00:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 123.4 |
| ec746dbf-65bf-32f2-b22c-9046ffcc2d1c | -16.613 | -57.1965 | 2024-10-04 00:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 7a244ff7-d3f4-3460-ad64-70f54b2cf637 | -16.6133 | -57.176 | 2024-10-04 00:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.5 |
| 5b5e4173-a149-3db0-a6bc-d2e865f7fb6e | -16.679 | -55.5402 | 2024-10-04 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| a7a3135a-7e90-39fd-b4a6-595ab4e7a0fc | -16.7606 | -57.7512 | 2024-10-04 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 48a4510e-2d31-3147-8794-bdc891d6011a | -16.779 | -57.8306 | 2024-10-04 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 8ef59305-0022-3fd9-af9b-06721ce8a430 | -16.7856 | -57.4015 | 2024-10-04 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| d3bb74af-e7f1-3875-8aa5-58cd88ad8854 | -16.7859 | -57.3811 | 2024-10-04 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 197.3 |
| de2e0991-e8c1-3ad4-99dc-d5162b92e517 | -16.7985 | -57.8284 | 2024-10-04 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| bfbbb258-c4e6-30a2-bc6e-d2664ca63562 | -16.8051 | -57.3993 | 2024-10-04 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 1bd61dd0-23e2-3dda-8470-29610a485e0b | -16.8055 | -57.3788 | 2024-10-04 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.2 |
| 07fb257d-4e12-36e8-bc11-7cec5fa8cdf8 | -16.843 | -57.4767 | 2024-10-04 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| cc90a47c-5f7a-33e2-90e6-ee18febd9f4b | -16.8433 | -57.4562 | 2024-10-04 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 11d136d2-e95e-3924-82c0-7264e67ee327 | -16.9087 | -55.843 | 2024-10-04 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| c01bea4a-6738-3a6c-9ff5-1bdf6e152f0c | -16.9283 | -55.8405 | 2024-10-04 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 0073715a-8f59-3f92-92b6-9ba39fbea40d | -16.9287 | -55.8197 | 2024-10-04 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 371c7f36-a9de-3fc3-a44f-c877286730fd | -17.3844 | -42.6235 | 2024-10-04 00:56:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 2137e9c8-25dc-3ed8-9cfb-a706b4f12c3f | -17.0616 | -56.0723 | 2024-10-04 00:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| def8ae8e-40f7-3269-a096-4e723d6f969b | -18.8413 | -42.8985 | 2024-10-04 00:56:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| e359d63d-36cd-309e-b1bf-6046b8edaf86 | -18.8609 | -42.9182 | 2024-10-04 00:56:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| fb6f0024-2c31-3004-ae3a-7f8f80d514c8 | -18.8617 | -42.8932 | 2024-10-04 00:56:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 129.9 |
| 97c091bc-b992-36cf-afc4-e319759692ed | -18.8613 | -43.5837 | 2024-10-04 00:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 193.7 |
| fc3befa3-caf0-3edd-9ce6-2ae3c116d217 | -18.862 | -43.559 | 2024-10-04 00:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.9 |
| 80207061-3b34-3621-815a-f4af801828eb | -19.4899 | -42.8746 | 2024-10-04 00:56:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.8 |
| 33c1d474-b3be-31ef-9b60-55ca10edbe94 | -19.5104 | -42.8691 | 2024-10-04 00:56:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| f02b79f8-c564-395c-8960-a647803d5ff5 | -19.8054 | -41.9067 | 2024-10-04 00:56:55 | GOES-16 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.9 |
| f8b7a489-803b-3e7e-a2a2-0e6077589469 | -19.8063 | -41.8811 | 2024-10-04 00:56:55 | GOES-16 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| 8f9fb974-c195-385b-bbf1-738fdb1ac3cd | -20.121 | -43.5219 | 2024-10-04 00:56:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.8 |
| 58015b5d-006d-3867-b72c-fbc5219d8c2f | -20.1886 | -41.4374 | 2024-10-04 00:56:56 | GOES-16 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| 1c458e30-9a59-39cb-8436-e72d23231059 | -19.9907 | -48.6913 | 2024-10-04 00:56:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 17db4494-943e-37b0-b85f-1ca8d71d71b7 | -20.1416 | -43.5162 | 2024-10-04 00:56:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 130.1 |
| 743c5968-f5fe-3de5-9fed-ced1362ea039 | -20.1424 | -43.4913 | 2024-10-04 00:56:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.5 |
| 0681915a-8852-3f4b-92a1-e09e57886eaa | -20.0111 | -48.6869 | 2024-10-04 00:56:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| aff241a8-3f37-331f-beef-d40b3c2a6a86 | -20.42 | -43.7613 | 2024-10-04 00:56:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| b7c5b60f-fb96-3ca7-9181-0c2c19b330d5 | -20.4591 | -43.1795 | 2024-10-04 00:56:58 | GOES-16 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| f1081593-06c4-301b-a49b-253a3582ba01 | -21.3334 | -48.8044 | 2024-10-04 00:57:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.4 |
| 8788cc09-02d8-3552-9a8a-26041bb3b740 | -21.3541 | -48.7996 | 2024-10-04 00:57:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.7 |


[Clique aqui para ver as próximas entradas](README21.md)
