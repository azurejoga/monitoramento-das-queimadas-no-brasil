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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1a8fc4c-f339-393a-90d4-c64464dbe823 | -13.3397 | -45.2145 | 2025-08-15 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 657.5 |
| 30c13ab0-31e5-3d8f-b0af-1e561781f3e1 | -9.1708 | -59.6568 | 2025-08-15 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 150.0 |
| f3869586-b7a9-3eea-a86d-7ea1aa538e0b | -13.3198 | -45.2409 | 2025-08-15 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 323.2 |
| b39385a1-1a5f-3dd2-8d70-4c21c4010962 | -13.3203 | -45.2177 | 2025-08-15 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 316.0 |
| 44735121-539e-3f8e-b9f9-2d349c528266 | -16.3746 | -50.887 | 2025-08-15 13:20:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 14e4aa78-6957-39b6-a50d-7ebcfa248ad5 | -12.5942 | -46.9527 | 2025-08-15 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 89d66b40-a5cd-3ec9-a3c8-c894c7aae1b6 | -13.8937 | -45.561 | 2025-08-15 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2e0243a8-3d65-3328-bfb8-b6eeb58d7a0d | -9.1706 | -59.6762 | 2025-08-15 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 068ce445-0e9b-311d-90cd-efac559468f6 | -6.435 | -44.6222 | 2025-08-15 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 78ce50f8-a563-3623-bb11-a5dcd6f20527 | -9.1522 | -59.6578 | 2025-08-15 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9dd7112e-0489-396f-9799-6ce745a55af2 | -16.3741 | -50.9089 | 2025-08-15 13:20:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 50ee3429-c798-33d5-9512-e9c00f70d8ed | -6.4353 | -44.5993 | 2025-08-15 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 63b495aa-cab9-381e-a0e6-910a6d063daf | -13.4566 | -56.6757 | 2025-08-15 13:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 590d9830-5d48-376d-b4ab-7e9565bcd0fd | -12.575 | -46.9555 | 2025-08-15 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| e238caf7-7eaa-3b22-8a1a-f1fe0ee93031 | -13.3392 | -45.2377 | 2025-08-15 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 703.5 |
| 9bcd0355-22be-30dc-9b15-5744c9e4f313 | -12.5938 | -46.9753 | 2025-08-15 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| cbc05e2f-66e9-3360-a968-c86d976189b3 | -7.8591 | -48.2255 | 2025-08-15 13:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 92b89026-ba4a-3719-ae22-29378cfd3e00 | -12.5947 | -46.9301 | 2025-08-15 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f24eea4d-c14a-3bc5-8db4-63d20bc4d1fa | -6.8673 | -42.7961 | 2025-08-15 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 381.7 |
| 8486ed33-0ede-36ab-8a02-3f5f4af89869 | -6.4165 | -44.6008 | 2025-08-15 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 261.3 |
| a367b5a1-88b7-39b1-b66d-f4e83219297e | -16.3741 | -50.9089 | 2025-08-15 13:30:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 101cf62e-d44e-33e7-81ec-847d2e2ace8e | -9.8915 | -60.4297 | 2025-08-15 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 903b082a-399a-3140-80f2-290ea5cac00b | -7.3896 | -44.8589 | 2025-08-15 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 00bb50bf-2dad-374a-bdc4-af7a766cf6af | -6.8673 | -42.7961 | 2025-08-15 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 307.7 |
| ff8b4b90-0bea-3db1-b87d-6786acbe95fd | -13.3397 | -45.2145 | 2025-08-15 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 536.3 |
| 39da0123-d407-308b-b620-fbdcec897a26 | -13.3203 | -45.2177 | 2025-08-15 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 396.0 |
| 0d439226-210a-392b-a541-8797051e50bf | -7.8591 | -48.2255 | 2025-08-15 13:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| cd197b20-a096-300b-81c5-c25fa8e181d0 | -7.3894 | -44.8817 | 2025-08-15 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 265.3 |
| a1f5cfd5-a61e-3b62-b456-56b5458fb213 | -6.435 | -44.6222 | 2025-08-15 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| acee1afe-84e5-3de4-8be2-f5325d587083 | -12.5947 | -46.9301 | 2025-08-15 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 2fac3cb1-3a78-32f3-b6d7-19b978ba5ca9 | -12.5942 | -46.9527 | 2025-08-15 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 432.4 |
| f2a55b7d-4e4d-3892-97a0-c7e9aedfd273 | -12.5938 | -46.9753 | 2025-08-15 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 216.3 |
| 56b70b4c-8ca5-3294-8e63-f4d37f371fd4 | -13.4566 | -56.6757 | 2025-08-15 13:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a4738805-50a7-395c-b07e-e542186c8fdf | -6.4353 | -44.5993 | 2025-08-15 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 8ba16e49-cf83-3c08-a047-a3aab5ba2c21 | -13.3198 | -45.2409 | 2025-08-15 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 345.0 |
| e506ee3b-283f-3f12-bc2b-2255ce8a907d | -7.4085 | -44.8571 | 2025-08-15 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 499.6 |
| 6adbfd35-8c54-3e8a-8fde-cdf2a97c113b | -5.2647 | -43.582 | 2025-08-15 13:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e4613e54-9445-3de2-95dd-2be3f617fc89 | -13.8743 | -45.5643 | 2025-08-15 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 102fca00-3d96-3b10-ab76-70acb38703fd | -13.3392 | -45.2377 | 2025-08-15 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 497.9 |
| 6fce9ac1-b035-353b-ac7f-b7779f790230 | -8.6694 | -62.4579 | 2025-08-15 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e09c8f95-8305-3a13-8174-ddc9780066b5 | -12.575 | -46.9555 | 2025-08-15 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 078c508f-876a-37b4-8afd-1d05fad02944 | -14.5631 | -52.0557 | 2025-08-15 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| fe1f2934-1b57-3ee4-86a5-c1ba726fca2d | -7.0201 | -44.2966 | 2025-08-15 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c56cd6d9-9242-31d1-bd83-db922b6cdee9 | -7.4085 | -44.8571 | 2025-08-15 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 585.5 |
| 1084bc9d-7db0-3e55-b9ee-05305e6bb92a | -9.1522 | -59.6578 | 2025-08-15 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 865325e1-b88a-3a6e-856d-b1005445fdff | -12.5947 | -46.9301 | 2025-08-15 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| c54f5ab6-0553-3097-a649-27e200cee1ae | -7.3894 | -44.8817 | 2025-08-15 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 413.2 |
| 8eb2d489-1147-307c-9180-d8072afe048a | -16.3741 | -50.9089 | 2025-08-15 13:40:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 205faee6-0eaf-369a-8116-6cceef2fad71 | -13.3392 | -45.2377 | 2025-08-15 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 572.6 |
| d57c3093-cbc9-3a3a-a837-9266f173d2fc | -9.91 | -60.448 | 2025-08-15 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 235485e4-f730-30d6-a846-1f8bd204ab42 | -13.8743 | -45.5643 | 2025-08-15 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 7e31aaa9-8a04-3df9-94dc-5ecb11566636 | -12.575 | -46.9555 | 2025-08-15 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 6e318351-94ec-38a5-b4ca-6ec25f78cbd0 | -9.1894 | -59.6558 | 2025-08-15 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b4a36830-582d-3138-8967-58eaf7966401 | -9.8915 | -60.4297 | 2025-08-15 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9847a3d1-ea41-31a6-922d-8f5c06f1b331 | -14.5631 | -52.0557 | 2025-08-15 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| d6e63d53-6ea1-33e5-9f6b-e622ee0e31d5 | -7.8591 | -48.2255 | 2025-08-15 13:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 03460d66-0715-3c33-99a5-3f1d2101b3f6 | -6.435 | -44.6222 | 2025-08-15 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 0cf212bc-378f-3cc3-81d6-cc3e96d4a1f1 | -7.0201 | -44.2966 | 2025-08-15 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 5e6aa301-cc3e-30e1-adc7-1477520be022 | -9.152 | -59.6772 | 2025-08-15 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 760e24b3-0753-3717-917a-a8663bf8bef5 | -6.4165 | -44.6008 | 2025-08-15 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 16088d88-6341-35d2-bd99-df4514f2c80d | -13.3397 | -45.2145 | 2025-08-15 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 879.0 |
| aeb0413f-3647-36ac-8b76-c443586fc213 | -13.4566 | -56.6757 | 2025-08-15 13:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 4d39d51d-8660-3d34-85c4-f4e16e51fcd3 | -9.208 | -59.6548 | 2025-08-15 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f9caf2a4-253a-35bf-a779-262fdfa83fc3 | -9.1706 | -59.6762 | 2025-08-15 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 80d1f10b-d4dd-3ea2-a68b-5c1db71ac10d | -12.5938 | -46.9753 | 2025-08-15 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 4b01a6be-4047-322b-9dec-92e10bcfb236 | -9.1708 | -59.6568 | 2025-08-15 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 1331714a-1ad3-374f-82a5-32c27fa4614d | -12.5942 | -46.9527 | 2025-08-15 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 254.8 |
| 7e7bf25e-e006-3933-bec5-257998e383b3 | -9.9102 | -60.4287 | 2025-08-15 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d00f9818-2f21-38e5-943b-44032bd1ecd2 | -8.6694 | -62.4579 | 2025-08-15 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 5396e7aa-d14c-397f-b26c-61270dc489b0 | -13.3198 | -45.2409 | 2025-08-15 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 289.8 |
| a2e2e5a6-d50c-3f79-9b6d-cc53ba0123dd | -6.4353 | -44.5993 | 2025-08-15 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 1829b0a2-7bd9-3c0b-a05b-5cbbf6ba1c10 | -13.3203 | -45.2177 | 2025-08-15 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 409.8 |
| 86af5fb2-7321-3086-b66b-3838d732161a | -8.6695 | -62.4389 | 2025-08-15 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 259ae553-625c-391e-a822-cd3453e01397 | -6.8673 | -42.7961 | 2025-08-15 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 404.2 |
| fcd5e6f8-7921-3eed-9a4f-c3025d69abff | -7.3896 | -44.8589 | 2025-08-15 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 211.6 |
| af957cd9-e502-3b09-8ab5-2bdbe14cf03f | -9.91 | -60.448 | 2025-08-15 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a4dfa982-c62b-3ab4-964a-a22cb375045b | -13.3203 | -45.2177 | 2025-08-15 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 415.5 |
| 0fd5ce69-1cb1-3f48-8f83-8b4f45d4ff3e | -8.6694 | -62.4579 | 2025-08-15 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 6992288f-8a0f-3d89-b3a7-a1599da2707a | -7.3894 | -44.8817 | 2025-08-15 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 526.0 |
| dc67ce0e-c948-3004-bbdf-d7df575c12a6 | -13.8748 | -45.5411 | 2025-08-15 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| b5b6aa2c-3c8c-392e-bf63-7cfaf289416c | -12.5942 | -46.9527 | 2025-08-15 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 270.7 |
| 05c32d8c-eb95-3774-bcbf-011f82fd0c3b | -7.5292 | -61.3254 | 2025-08-15 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e7886e73-4f24-3330-b6a9-4e64f692d0e6 | -8.6695 | -62.4389 | 2025-08-15 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 1e29f8ed-1844-3b07-899d-f48cf85a3e7d | -13.4566 | -56.6757 | 2025-08-15 13:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 65960593-ca16-34fd-94cc-0a5352440024 | -13.3397 | -45.2145 | 2025-08-15 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1083.6 |
| d8310a12-9bba-3e05-a07a-c531611c74d8 | -12.575 | -46.9555 | 2025-08-15 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 3d12d5fc-87f3-3d89-807a-c2f4e9760888 | -12.5938 | -46.9753 | 2025-08-15 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 9c5bd207-d45e-346c-9d93-b8fe4805dae4 | -12.5947 | -46.9301 | 2025-08-15 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 90917ed6-cbd5-3564-8001-851a25d4f03b | -6.8671 | -42.8197 | 2025-08-15 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 226.9 |
| 0ee8c550-a6e7-3457-99e2-0a20eb9521ce | -12.6461 | -45.1879 | 2025-08-15 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.9 |
| f1ad294f-8047-3d89-9a78-b4dca46b0de1 | -13.8743 | -45.5643 | 2025-08-15 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| aebeda76-b74c-31f0-a8ba-740d0ea3b6ba | -6.4163 | -44.6237 | 2025-08-15 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 2bf42d58-eb98-3cf5-a215-644a6066f52b | -11.9296 | -43.4288 | 2025-08-15 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| de4667e9-66a2-32a2-a600-5e7130257d7b | -9.8915 | -60.4297 | 2025-08-15 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 01cf3e79-6687-376c-bbe0-552aff25d23e | -16.3741 | -50.9089 | 2025-08-15 13:50:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 17db5331-86a0-3ff5-ad9f-613ce30f021a | -6.4165 | -44.6008 | 2025-08-15 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 2fb56679-a488-3db5-a916-19e20b3a0659 | -7.4085 | -44.8571 | 2025-08-15 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 603.1 |
| 4df98cdc-b20e-358f-81c6-b4e62c0e3e81 | -13.3198 | -45.2409 | 2025-08-15 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 258.8 |
| e1f4f195-7b8c-3762-a5c0-7ada528b8e76 | -14.5631 | -52.0557 | 2025-08-15 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 96ace4ce-b692-313f-ac5a-c3443cc630c8 | -7.3896 | -44.8589 | 2025-08-15 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 254.7 |


[Clique aqui para ver as próximas entradas](README77.md)
