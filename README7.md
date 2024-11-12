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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 310b97fa-dfe3-335a-8ba0-f8aae36efcd3 | 1.048 | -60.5986 | 2024-11-12 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 87c0d45b-0609-367b-a14b-a80bfc65ea6b | -2.7587 | -49.3497 | 2024-11-12 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 724d726d-403b-3459-ae1a-3af7dc23042e | -17.2737 | -57.488 | 2024-11-12 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 3128aa40-fd5e-3bca-bbdf-f384525cc304 | -3.0913 | -54.307 | 2024-11-12 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c9ebfff4-03e0-366b-91f2-93b04311444b | -2.7871 | -51.7544 | 2024-11-12 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| acd29acf-ddd7-33a3-8324-1291932e7ea8 | -3.0504 | -50.3332 | 2024-11-12 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| af19e3e1-141c-3b48-b696-6158cfa2812c | -2.7772 | -49.3492 | 2024-11-12 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a63ee64c-d7d9-3da5-8786-239b5a42efec | -2.7773 | -49.3279 | 2024-11-12 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| f6fadb29-38b6-3db7-b6b8-a90bb9ea6b4a | -3.1096 | -54.3066 | 2024-11-12 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 79a941db-16d1-3af9-b2e5-418e56257bee | -17.274 | -57.4675 | 2024-11-12 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 52dd9d73-7b94-34f7-ba71-b92265b0973f | -17.2933 | -57.4857 | 2024-11-12 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 0cf1c07f-fa05-37e1-b8fe-86c35725e845 | -2.7871 | -51.7544 | 2024-11-12 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a6fe39af-6015-3c5a-bf30-85ff43adce53 | -3.0913 | -54.307 | 2024-11-12 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 5ab8d667-5467-37b5-a14c-0bb1ac99115e | 1.0663 | -60.5985 | 2024-11-12 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 605aaa50-bba9-3921-a336-899c94cb593f | -3.1096 | -54.3066 | 2024-11-12 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 7f44eb9e-eb76-3301-846d-f94a54fa342f | -17.2933 | -57.4857 | 2024-11-12 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 4b6a48d0-cd29-39ca-b0ad-0b01d3bbc104 | -3.1097 | -54.2865 | 2024-11-12 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 54479c48-29b4-3884-b7ec-0d86a6f875e7 | -17.2737 | -57.488 | 2024-11-12 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| de8af68f-416c-31ce-b9cf-5cf1e5e83c34 | -3.0504 | -50.3332 | 2024-11-12 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a2e0c4f5-576d-328e-8ce2-0a61c8c7aa2b | -3.0689 | -50.3326 | 2024-11-12 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3ec72288-eeb5-3e58-a59f-c5aafa787893 | -2.7587 | -49.3497 | 2024-11-12 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a7013534-228f-36bc-a870-1c1f118210a6 | 1.048 | -60.5986 | 2024-11-12 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| cb50b0d3-0d9a-3c2d-977c-a1b98960688a | -17.2936 | -57.4652 | 2024-11-12 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| c522b35d-86c6-3598-ba99-469a9723b029 | -17.254 | -57.4903 | 2024-11-12 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 5c1dc0a1-358d-3091-a010-7be55a19275f | -17.274 | -57.4675 | 2024-11-12 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| fae9fd7e-9799-3058-a4ad-e3ac4af273dc | -3.0913 | -54.287 | 2024-11-12 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 0bdcdf6c-e330-33c4-9552-2dd9a845690b | -2.7588 | -49.3285 | 2024-11-12 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1599246f-7252-34d9-9a4b-5860cb3b9b47 | -3.0913 | -54.307 | 2024-11-12 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 5ced0332-e85d-3223-a02e-edd44b26e127 | -17.2737 | -57.488 | 2024-11-12 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| c1d3f2cd-a757-388c-97e5-5d09af7479f5 | -17.2936 | -57.4652 | 2024-11-12 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 1681d152-6496-3532-a264-fd12ab3e528f | -17.2933 | -57.4857 | 2024-11-12 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.2 |
| ff3106ce-3664-347c-9516-97ac3866c257 | 1.048 | -60.5986 | 2024-11-12 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d42b24bb-7acd-3772-b654-e0bee45ef21b | -17.254 | -57.4903 | 2024-11-12 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 9084c9f2-decc-391a-9c9b-95f4c9a982bf | -3.1096 | -54.3066 | 2024-11-12 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 29bb3ed1-1973-3263-bccd-62a2225959c2 | -17.274 | -57.4675 | 2024-11-12 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 4356d6bc-61fc-3495-8b63-c5185a9b0ceb | -3.1097 | -54.2865 | 2024-11-12 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| fa68ce32-c686-35da-a616-e1f278fd77f6 | -2.7871 | -51.7544 | 2024-11-12 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 0be26f85-933f-37d9-adc6-af3e0b0b702d | -17.2737 | -57.488 | 2024-11-12 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 740597d5-f192-31fa-b8fc-59c4e363da35 | -17.274 | -57.4675 | 2024-11-12 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 7f98aa46-ad91-35c8-8f82-3f5be5c41fe8 | -3.1097 | -54.2865 | 2024-11-12 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 2bc079d0-638b-3018-a0a4-7e024448dd30 | -3.1096 | -54.3066 | 2024-11-12 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 421a721c-3895-3505-bd2d-c856d5f74a0c | -2.9913 | -51.3356 | 2024-11-12 02:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 85ca0aa9-e1eb-32fa-8506-1c39f674ef5f | -17.2936 | -57.4652 | 2024-11-12 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| fd4dcff7-df5f-3d3a-9ea6-843335a92580 | -17.2933 | -57.4857 | 2024-11-12 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 984c6b92-0e00-3876-9527-cf1f79420b89 | -17.6069 | -57.5304 | 2024-11-12 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 19d96cff-1f94-3527-9d12-a5b34927946e | -2.7871 | -51.7544 | 2024-11-12 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 71034924-68eb-3acc-9f01-3295da426dc4 | -17.2933 | -57.4857 | 2024-11-12 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 91e1991c-38d1-386c-b935-494adf757816 | -3.0689 | -50.3326 | 2024-11-12 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 3144b9ec-e2c1-39e2-a1d1-373ca03d97b4 | -3.0913 | -54.307 | 2024-11-12 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| cf760ea2-eff1-3669-bde4-84010a9be3a2 | -3.0504 | -50.3332 | 2024-11-12 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 8c3b08ac-6a43-3e10-80c0-28fcb017f94d | -17.2737 | -57.488 | 2024-11-12 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 0bd21e6e-789a-3f88-96a6-9364118f3e28 | -3.1096 | -54.3066 | 2024-11-12 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 796beda1-1a88-3121-96b1-0eaa98668e5e | -17.6069 | -57.5304 | 2024-11-12 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 4fc3beed-73e2-3a83-a0f3-f1632579886f | -3.1097 | -54.2865 | 2024-11-12 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 14d06777-bbf0-31a3-91cd-251283a0cdd1 | -7.17508 | -35.02 | 2024-11-12 02:45:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 522f9c9c-621f-37e0-a2f4-4beb807bebe8 | -3.0913 | -54.307 | 2024-11-12 02:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 751339c4-4311-3d05-88cf-d49ee470f5d1 | -17.2933 | -57.4857 | 2024-11-12 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 3d1841df-f3ea-3336-9efc-b91c9190079f | -3.1096 | -54.3066 | 2024-11-12 02:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 7a6163bb-1039-3fc1-88c8-a29ad36675f6 | -3.1097 | -54.2865 | 2024-11-12 02:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 2f8a16d9-2749-3003-9273-35d6fd76ee39 | -3.0504 | -50.3332 | 2024-11-12 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| df6ed661-4f5d-38ea-97f7-a70170526a3d | 1.048 | -60.5986 | 2024-11-12 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ade47457-2b67-3352-b6b2-8eea8aa0793b | -3.0913 | -54.287 | 2024-11-12 02:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0e5cb1a0-2978-3464-82f2-7c0756cb61ea | -4.8032 | -45.282 | 2024-11-12 02:50:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| cd967b93-edf3-3c5c-8224-f133f62fccc9 | -3.0689 | -50.3326 | 2024-11-12 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| c0d21519-43a2-338e-b04b-b762317df26f | -3.1096 | -54.3066 | 2024-11-12 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| a37420f4-5b62-34e7-9ddf-06defce4f1a9 | -20.0989 | -49.1939 | 2024-11-12 03:00:00 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 144.0 |
| e3c67d48-2066-3ced-af4e-2b547eeb9578 | -3.0913 | -54.307 | 2024-11-12 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 20cc972c-0926-3993-81d6-9472f436e6fb | -3.9483 | -48.1724 | 2024-11-12 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| e936fd94-ee9a-36d1-bf95-a0909260d30c | -3.0913 | -54.287 | 2024-11-12 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b9842e93-1129-33d7-876c-e0a65317bea5 | -20.0995 | -49.1709 | 2024-11-12 03:00:00 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 6a179326-1643-3987-8ebe-ce39f2c09193 | -2.1271 | -50.6912 | 2024-11-12 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 8e34ac4b-ebe6-32c9-9b74-b284658f604e | -3.1097 | -54.2865 | 2024-11-12 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c918ca50-7afd-308b-a057-249178fc34bd | -3.0504 | -50.3332 | 2024-11-12 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 5d9ab212-fa05-3688-be77-d74221cd9717 | -3.0689 | -50.3326 | 2024-11-12 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b4cc0955-90fc-3bd2-b950-5af82ae3b7a9 | -20.1193 | -49.1895 | 2024-11-12 03:00:00 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 2a024e67-1bfa-3422-80cd-0cf63ba7d2cc | -3.0504 | -50.3542 | 2024-11-12 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| dc35f095-2b91-380d-8ae6-3a98f401c4a2 | -3.9482 | -48.194 | 2024-11-12 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 1023ad1d-9da0-397a-87c6-fc5b6fe6a87d | -3.9483 | -48.1724 | 2024-11-12 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 150b4255-2fbb-38a7-b82d-d25e24fa0b5a | -3.8534 | -52.3801 | 2024-11-12 03:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| aaeb50f6-3978-37cf-a65e-c9f66d48230f | -3.9482 | -48.194 | 2024-11-12 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9724fa67-f192-35af-b2cb-b05d583210af | -3.1096 | -54.3066 | 2024-11-12 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 8e8476e2-947e-3d3d-930f-5785837d7859 | -2.1087 | -50.6916 | 2024-11-12 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 62469266-2590-3c1c-bd9d-798063373a3b | -3.0913 | -54.307 | 2024-11-12 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 8bab09a9-7d8c-32a3-ad22-0d9c1ae67d70 | -3.0504 | -50.3332 | 2024-11-12 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| b643bb50-b3bc-3307-b2ba-09b9747762da | -3.0913 | -54.287 | 2024-11-12 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 292ac3c5-cf15-3415-9650-e12c00448904 | -3.1097 | -54.2865 | 2024-11-12 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ca425f70-32a7-30a2-adb9-4be741b87619 | -2.1271 | -50.6912 | 2024-11-12 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 8928126a-e71f-3c33-ada6-eab8de495b0c | -2.1087 | -50.6916 | 2024-11-12 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| facff790-b965-3c74-9baa-34b5749add24 | -4.8032 | -45.282 | 2024-11-12 03:20:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c543b30d-fc1d-3d42-93e4-97dfaf6be77b | -3.1096 | -54.3066 | 2024-11-12 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| cde7fa1c-dda8-31d8-8cf1-67862e04c9ab | -3.1097 | -54.2865 | 2024-11-12 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9c31d445-6044-3e7e-9019-78cdfd29531e | -3.9483 | -48.1724 | 2024-11-12 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 5506e6e2-2fc0-30ab-8779-048639eca5f2 | -2.1271 | -50.6912 | 2024-11-12 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 6ef667df-e082-3fbe-b315-53154ec09d87 | -3.0913 | -54.287 | 2024-11-12 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9fd7e78f-a3df-30d7-a4a3-5ec117d1db8a | -3.0504 | -50.3332 | 2024-11-12 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| a29447a0-4fb1-3be3-bd7a-2ac82e2af70a | -2.1455 | -50.6908 | 2024-11-12 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| eb7ec887-e1ec-3bc1-9837-de717d15e007 | -3.9482 | -48.194 | 2024-11-12 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 248da7b2-79d4-3144-a729-06f144d3da4e | -2.1271 | -50.7121 | 2024-11-12 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| a5a7abfb-28db-3cc1-9bdc-a867dd20bfb4 | -3.0504 | -50.3542 | 2024-11-12 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 05e1e171-cc07-3439-b58a-c7bcafe78cf6 | -3.0913 | -54.307 | 2024-11-12 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |


[Clique aqui para ver as próximas entradas](README8.md)
