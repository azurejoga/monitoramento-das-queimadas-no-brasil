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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2e4854c-ea9d-3af6-bbd8-c36b513d42e7 | -18.21709 | -56.54929 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b1c5c5e0-93f6-3369-9406-939111dd3ad9 | -18.21653 | -56.5769 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2d7bb184-f13d-3236-9429-7a41fe708f69 | -18.21646 | -56.48172 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e851d31f-eed9-3a29-aebe-d69fbe75708d | -18.21641 | -56.43391 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fbc6b6f8-552b-35a1-9f68-5695d0c13d35 | -18.21595 | -56.55702 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| cc4a8e29-abf5-32b9-b63e-7921d00f7717 | -18.21538 | -56.56089 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b9f3149b-26e1-32eb-84d4-a05e270f533c | -18.21537 | -56.53712 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5acda018-b62f-3bf3-b740-23a0f38490cb | -18.21527 | -56.4417 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 59e53d7a-ae4b-3226-be3d-6da5e6e59512 | -18.21471 | -56.4456 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 79271de3-49d1-3010-b8b5-3f8f51f5609a | -18.21414 | -56.4495 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 533a4479-49ce-30ae-b451-53de04bac482 | -18.19666 | -56.85202 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ef9c0ef0-67de-3bb0-baef-6fb074aa82dc | -18.19609 | -56.85581 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| af1da74b-6ec6-3e84-b31a-64592d18ff5b | -18.19382 | -56.84766 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 7959c19a-cc62-3873-846b-1a80b3e12811 | -18.19326 | -56.85147 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| d0895f85-dcf6-377a-a488-350df80cb30e | -18.19269 | -56.85526 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 4330d9e5-0750-37c9-a840-bf67b2261655 | -18.19156 | -56.83951 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 262b1794-74a9-3fea-bd5b-9f8a307e4672 | -18.19099 | -56.84331 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 884301de-64b6-3671-b021-715b9208c638 | -18.18986 | -56.85091 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| bfe57c9a-1127-393a-bbeb-09be8b16bef4 | -18.18646 | -56.85035 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8eb1ab02-d1f2-3b52-a05f-628153506758 | -18.14824 | -56.40426 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 604682c2-41d8-3132-95fc-b310dcb291f7 | -18.1448 | -56.40371 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cbf70601-213e-3213-a183-be280357984d | -18.14193 | -56.39926 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7df60925-6efa-37eb-a329-972cae5aa4d2 | -18.13849 | -56.3987 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e208b161-daf2-3d47-bb38-7826098f140b | -18.13555 | -56.29806 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| eddecb6e-6fac-3258-94a8-51e2f4d9a3d5 | -18.1321 | -56.29751 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2da57772-7144-31c1-8da0-ddcb332fb2a0 | -18.13095 | -56.30537 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7e5e091d-4980-3c72-8af3-b1be0171d7fb | -18.13038 | -56.3093 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c09320ee-e51d-3629-9ad3-81a766c5f12f | -18.12804 | -56.27674 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 81092f4d-788d-35d6-a7c1-208931b60f91 | -18.1275 | -56.30481 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3e464ebe-6ac9-3597-b22f-48f5e12a85a8 | -18.12693 | -56.30874 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 227b1863-ea78-3c34-8dad-432242c77a97 | -18.12458 | -56.27618 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d503f838-f8fc-30d7-a382-db61370b0654 | -18.12113 | -56.27563 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2fb309d9-10a7-36e7-a2ce-9b11c05047d1 | -18.11711 | -56.27901 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b06a1f8f-6595-3839-a74a-9e5df7d33237 | -18.11654 | -56.28295 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 33f9d1ce-ca29-356e-8d8e-4d44a1da00e3 | -18.11365 | -56.27847 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| dc646fc4-dc0e-3a65-89ec-e8fc03d8ea5a | -18.11308 | -56.2824 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8ab41f0a-e321-32b8-8197-e8a7621f743a | -18.0927 | -56.44712 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7fa561f0-ec0d-333d-9192-c56b491cfbe1 | -18.09097 | -56.4349 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8a5d4df0-857d-3012-bde5-8ae5abc1a187 | -18.0904 | -56.43879 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4168a285-562e-3196-b603-13073e2c5b7b | -18.08876 | -56.43164 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 573ec3fe-af37-3224-b417-02a623f6c6c6 | -18.08819 | -56.43552 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b823194e-69f4-3518-a436-744a670d1ea7 | -18.08753 | -56.43435 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9ee9a429-99fb-35cf-8a8a-fbb223b7a849 | -18.08718 | -56.32357 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c001ffaf-e3e3-3dcc-a707-c16cac3f9037 | -18.08536 | -56.40721 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d6de0a41-cb2b-3c07-9cf4-44b5c4de6827 | -18.08533 | -56.43109 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 01c8d46c-08a3-393e-bfbe-2a3da86fe93d | -18.08478 | -56.41109 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1270ebab-fd09-3426-b1fc-600902bd4764 | -18.08475 | -56.43497 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 321ee2e3-7c5b-3a35-b625-1ba83c2b4078 | -18.08431 | -56.31911 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5d975787-916b-3dca-bc5e-3fa8d643492a | -18.08421 | -56.41499 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 16203386-7340-36fd-b95f-7b5315b4e684 | -18.08373 | -56.32302 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ec43c141-ab25-3d42-8323-526939b6720d | -18.08192 | -56.40665 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ead9a480-8eda-380b-883a-959c41d8bf49 | -18.08189 | -56.43053 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d920fb25-d6d6-3ce0-8a67-9b8034c8b2ac | -18.08131 | -56.43442 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0a659ab6-bedc-3d1c-b01e-280abf362b0a | -18.07966 | -56.37438 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 23ef6833-b155-3e29-b255-998a4f07501d | -18.07913 | -56.3303 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 62ec0487-4a0b-3720-a6e7-bbcfe6951933 | -18.07845 | -56.42998 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 314aac46-be6c-39bb-ab7a-8d709072e630 | -14.35524 | -57.61381 | 2024-10-13 05:06:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4c3c262-8a3d-3d79-b842-8f689d18cfea | -14.35136 | -57.61681 | 2024-10-13 05:06:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acf050af-9a40-38a9-b36e-ed1dc96ee420 | -14.35192 | -57.61325 | 2024-10-13 05:06:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3dec904-0ed8-338a-97b6-048fc78cc31e | -17.99035 | -57.3674 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8a753289-b45d-3dd0-8700-61ec43967050 | -17.98978 | -57.3711 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 3c9fb709-1f03-3125-a652-13c7fc3d5d6f | -17.98922 | -57.37479 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b88a4fc0-d22d-33af-9f03-72881b422ac8 | -17.98755 | -57.36314 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a16a8530-709e-308f-a09d-529cb6adce89 | -17.98699 | -57.36684 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f6c72b8c-d222-3971-afe7-ab75e15aa0d8 | -17.9853 | -57.37793 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 77500230-25eb-3ad5-a521-81c9af4df360 | -17.98476 | -57.35889 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 3c147fa5-dd98-36dd-8840-4d41b6e97083 | -17.9842 | -57.36259 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 94876864-09da-39a1-a473-4b405bce195f | -17.98195 | -57.37737 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8f3b62bd-0620-35fa-bc03-66ebd3c32062 | -17.9814 | -57.35834 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 4f100544-1a84-35c7-a428-a4bbd952a831 | -17.98139 | -57.38106 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cd4e8b5c-db88-3827-9c66-673367e99a9f | -17.98084 | -57.36203 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 142b3fb8-2d31-3632-8c90-c2d5f1ed957e | -17.98083 | -57.38476 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a277006e-e628-345d-944e-4f3ac8047c66 | -17.97804 | -57.35778 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| e43c8171-b0cd-38d7-b4ed-931868d1e1bf | -17.97803 | -57.3805 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b590e4c2-e9d9-3d18-b151-3e37cde1fc17 | -17.97748 | -57.36147 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 07e92506-170c-36a8-89a8-ef93e600ca9a | -17.97747 | -57.3842 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 56304a81-d032-39f9-9574-e54d38d7de5d | -17.97692 | -57.36517 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 5101030d-7440-3a81-acb5-4fd05f737810 | -17.97469 | -57.35722 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e1615310-7a67-3661-acf9-be86c01f0b69 | -17.97413 | -57.36091 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1180a8d7-a499-390f-a5ea-c2113c88aa59 | -17.97357 | -57.36461 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| b5f6a181-27b2-3060-8601-2ba92c9cc5c6 | -17.973 | -57.3683 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 6772a4f7-0054-3b64-a738-a8d7942419dc | -17.97021 | -57.36405 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 753cec30-a95a-30e4-812f-3491a66e8023 | -17.96965 | -57.36774 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 5cccbef9-78dc-31da-bc25-1e49df92e0cf | -17.96685 | -57.36349 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 822241cb-4187-3d09-9788-ec6f4df381c0 | -17.96629 | -57.36719 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d22fa98b-efa0-3f9d-b46c-ee34aee5e9e7 | -17.9635 | -57.36293 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1e5bdc56-fbf5-3106-8205-f4d632ccbcef | -17.96349 | -57.38566 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| d8902e8a-0570-3c54-91e0-c563c9d5cba6 | -17.96294 | -57.36663 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 352ddb41-8b31-3f21-b0c6-573b0dd51fda | -17.96293 | -57.38935 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 5977745c-df28-3edf-8ad5-434a647e4f5a | -17.96237 | -57.39304 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 336c591c-7d2e-3d2f-9a08-1c6a89d9de3b | -17.96014 | -57.3851 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| bdfa890e-0778-35c6-8541-ca2cf3f4e19b | -17.96014 | -57.36237 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5782d012-8248-3bfc-8bd2-4e79843c7d64 | -17.95958 | -57.38879 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| ab5aa455-6c02-37b1-ad8d-e45efc10629e | -17.95958 | -57.36607 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a83fe941-c5bd-3202-a464-5dc8e1c935a2 | -17.95902 | -57.39249 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c32bc9c1-a017-3977-a668-951dd457f317 | -17.95902 | -57.36976 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 23d1a337-b4cf-39be-9a5e-1e8ab5f9d4a2 | -17.95846 | -57.37346 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 073aad47-cc58-3227-889c-d89aed51d6bc | -17.95734 | -57.38085 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 48832485-eee5-36d3-bc08-dd49b559ac23 | -17.95678 | -57.38454 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.9 |
| f258e341-b7e6-3249-84c6-98c967de8bf1 | -17.95623 | -57.36551 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |


[Clique aqui para ver as próximas entradas](README91.md)
