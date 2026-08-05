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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eeac534e-57a2-38f8-a4d9-816730e4f6c7 | -13.2604 | -54.2662 | 2026-08-05 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 9104a6fd-bb8d-3e43-96f6-6e819d7c5f43 | -11.183 | -54.8991 | 2026-08-05 12:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| c8c48d4f-9c01-30f9-b82b-c0a139fdbb0d | -12.5942 | -46.9527 | 2026-08-05 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c548b04d-c510-3bae-8633-acfdd7cd6be6 | -14.2682 | -45.287 | 2026-08-05 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 33438dd5-5b7f-34ec-ba44-20f674f98d91 | -11.183 | -54.8991 | 2026-08-05 12:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 70d1a707-9463-3f05-bfcc-742e24203afc | -12.5942 | -46.9527 | 2026-08-05 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| dd2fbc0c-9bde-39c2-ad6a-7a0564e972bc | -13.2413 | -54.2683 | 2026-08-05 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 253.6 |
| 1431084a-3499-3151-9e82-c3000e388aac | -11.1833 | -54.8787 | 2026-08-05 12:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 89d23bc6-c2e9-3b2c-a972-153a856f3ac6 | -14.2682 | -45.287 | 2026-08-05 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 54aa5160-8c69-359d-90e2-4cf58b159f88 | -11.1642 | -54.9007 | 2026-08-05 12:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| ffb9bb8a-6c1d-3308-9a08-9cb9fc58ca69 | -13.2604 | -54.2662 | 2026-08-05 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 242.7 |
| 42592642-55b6-3f94-8ca4-bf616ef0228a | -12.5947 | -46.9301 | 2026-08-05 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e06c9f52-9234-39be-9fae-56d6945097a3 | -11.2019 | -54.8974 | 2026-08-05 12:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| aae8d6d4-7e1d-3352-9c4f-2e39e17d2fd3 | -14.2682 | -45.287 | 2026-08-05 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 180.7 |
| b2ba1674-ed09-30e8-92a0-8d37830303df | -12.5942 | -46.9527 | 2026-08-05 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d29f5098-0b62-3ba7-b912-5c5421268c00 | -11.2019 | -54.8974 | 2026-08-05 12:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c0e6ed2a-b6a1-3b92-91e5-bce67e228346 | -11.1642 | -54.9007 | 2026-08-05 12:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| cc10d345-3e23-3c6c-b024-7f45ec06fa69 | -13.2413 | -54.2683 | 2026-08-05 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 46caea45-4808-325f-87f0-fc8bbf801158 | -11.1833 | -54.8787 | 2026-08-05 12:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a48097cc-804b-3f7e-be23-c66d3022f734 | -12.5947 | -46.9301 | 2026-08-05 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| fbfb563a-7771-3d61-b1de-7db162d48519 | -13.2604 | -54.2662 | 2026-08-05 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 327.3 |
| 1b56456c-2e37-34d2-b7e4-dff924e6deec | -11.183 | -54.8991 | 2026-08-05 12:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 0ad8b5c9-ef09-3a87-b6f1-80078b5d333e | -12.5942 | -46.9527 | 2026-08-05 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| ff4a2c7c-0b47-3c4a-9f06-463174f058e7 | -13.2604 | -54.2662 | 2026-08-05 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 289.3 |
| 4adafb48-464a-3412-85fc-fd6a909aca3c | -11.1833 | -54.8787 | 2026-08-05 12:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b5c624df-65f3-378f-84f9-172356455922 | -13.2413 | -54.2683 | 2026-08-05 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.9 |
| b90718f8-0136-3dcc-999f-0caeda7f4302 | -11.183 | -54.8991 | 2026-08-05 12:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| c38877f3-1dcb-3971-80a1-6771d7238212 | -11.1642 | -54.9007 | 2026-08-05 12:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| ce3fedfd-eb39-3316-939f-e3de2e5d9da7 | -14.2682 | -45.287 | 2026-08-05 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| e23a786c-c675-3448-be97-a6eb38e95ec5 | -11.2019 | -54.8974 | 2026-08-05 12:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8f9fe35e-b162-3f5d-bbf3-0443cb1ff56c | -12.5947 | -46.9301 | 2026-08-05 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 2c0a996b-66b7-3d78-9c79-97d039004b6d | -11.1833 | -54.8787 | 2026-08-05 12:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 9e75683e-959e-349d-acea-6ac56b4185b8 | -11.1639 | -54.9211 | 2026-08-05 12:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 3ecdd72d-a567-3107-bd4a-09a7671770f4 | -10.6181 | -46.3872 | 2026-08-05 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 24e02212-138e-3274-9730-fdfd0b16ea1e | -11.1642 | -54.9007 | 2026-08-05 12:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| d2eadb29-22ca-3903-a129-57a3d3602a64 | -11.2019 | -54.8974 | 2026-08-05 12:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| b55b07f4-2836-34ca-9ef6-71b349140051 | -12.5947 | -46.9301 | 2026-08-05 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| ca481700-4589-3f5a-a8b0-61a565fd357e | -14.2682 | -45.287 | 2026-08-05 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| b84c2d30-f89f-30df-b2fa-29ba62956f9b | -11.183 | -54.8991 | 2026-08-05 12:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| c5ebd225-cfdb-3e3d-ac66-4391671f3063 | -12.5942 | -46.9527 | 2026-08-05 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 79ce5767-4e4f-3028-851d-e6fcff984bcb | -10.6184 | -46.3646 | 2026-08-05 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| e2e08e4b-243b-3e48-a5b8-9e7a247ab59c | -8.3494 | -46.394 | 2026-08-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8a770d1c-90c1-3fca-9247-9b43b33b0e10 | -13.2604 | -54.2662 | 2026-08-05 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 629a3b5c-102e-3296-a6e8-722aa9f2e8be | -13.2413 | -54.2683 | 2026-08-05 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| ade1be45-5c7b-3335-a775-f87d49b53b19 | -12.4383 | -50.5324 | 2026-08-05 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8ff68b74-2f64-3196-a357-fcea21474c1d | -13.2413 | -54.2683 | 2026-08-05 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| ec13e98e-2a0c-3303-afc4-1bdf69771714 | -12.5754 | -46.9329 | 2026-08-05 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e30ec2c6-a8dd-381e-8698-74a380724b16 | -12.4383 | -50.5324 | 2026-08-05 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| b8d4a175-0fe5-393f-8c1b-38bb3748e048 | -13.2604 | -54.2662 | 2026-08-05 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 177.6 |
| c70fe95e-662a-3af8-b23a-de2ebc97919f | -10.6184 | -46.3646 | 2026-08-05 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 80932255-ecc9-3a07-bf6c-684b558d50ab | -12.5947 | -46.9301 | 2026-08-05 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| e73c9172-305e-348b-97d9-8c598cebf914 | -14.1969 | -54.4309 | 2026-08-05 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e41c6777-d66e-3999-a5d0-a5e0f22d02c8 | -14.2682 | -45.287 | 2026-08-05 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 195.2 |
| fa98e637-f5f0-35ce-8c42-b7579d1c3adb | -12.4386 | -50.5109 | 2026-08-05 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 11f525e2-7085-3c65-a45e-3337b6a6ac3c | -12.575 | -46.9555 | 2026-08-05 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| ab8cd6b0-2036-3d83-a2d3-bdd16075d649 | -12.5942 | -46.9527 | 2026-08-05 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| c49464cc-4531-3acc-83dc-13b821242785 | -14.2487 | -45.2904 | 2026-08-05 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9337ad44-6051-3c83-a8e4-970197b5d873 | -10.6181 | -46.3872 | 2026-08-05 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| be59c1a3-9d2d-36f7-a8c9-61bee10e4d24 | -20.896 | -44.9072 | 2026-08-05 13:00:00 | GOES-19 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.8 |
| 23123995-e1d2-3ae3-9dc4-5e92fcba0350 | -7.2293 | -45.7801 | 2026-08-05 13:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c12569ae-8343-3cc0-89a4-25cd68e22a04 | -10.6184 | -46.3646 | 2026-08-05 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 249.1 |
| d3ab2310-6a4d-379f-bc63-5aa2cff8f818 | -13.2413 | -54.2683 | 2026-08-05 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ee94b4f4-4e46-3104-9264-5347106b513b | -12.5942 | -46.9527 | 2026-08-05 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 2410367a-b53b-33de-ada5-5bd23852aa72 | -12.5951 | -46.9075 | 2026-08-05 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| d791bcd5-9c0c-3573-a237-dc51931b2dc5 | -10.9192 | -50.4283 | 2026-08-05 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 0de9ac72-c153-3ebf-a0e0-04c9aba88ca4 | -14.2487 | -45.2904 | 2026-08-05 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 3cae6196-e9f6-3611-a0e2-b05994e814c0 | -13.2604 | -54.2662 | 2026-08-05 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 145.1 |
| ce7e0ac2-83f3-38a7-8f87-d4d2b854c135 | -14.2682 | -45.287 | 2026-08-05 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 239.4 |
| 91be2fde-df8e-3827-a7ef-82a3991c1919 | -12.5947 | -46.9301 | 2026-08-05 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 871d3cfe-99ef-3954-adb5-6d3cfe1deb79 | -12.5754 | -46.9329 | 2026-08-05 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 24d2f3ad-9232-3c43-adef-592369c7eb51 | -10.6181 | -46.3872 | 2026-08-05 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 414.2 |
| feca7979-57ca-34b4-afdd-101164a13f72 | -10.599 | -46.3896 | 2026-08-05 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6ac6fc23-0800-3912-878e-fb01ddc2fcea | -12.5951 | -46.9075 | 2026-08-05 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d75165f6-8851-308e-b69c-2f424565256f | -13.2413 | -54.2683 | 2026-08-05 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| d3928d9b-730b-3f9e-942f-41679f051245 | -6.9879 | -42.1201 | 2026-08-05 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 7ae649ea-2d32-37f2-b307-a1c7b43c5fb2 | -13.2604 | -54.2662 | 2026-08-05 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 208bef0f-c374-3c66-91a1-7f03892fa8f8 | -12.5942 | -46.9527 | 2026-08-05 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| f779d51f-849c-36ac-9450-2704c670a6b4 | -14.2487 | -45.2904 | 2026-08-05 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 87928122-d09e-357b-a14e-cfbe603f3934 | -14.2677 | -45.3103 | 2026-08-05 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| fff435d7-0831-320b-aa40-c6c6cee76ec5 | -14.2682 | -45.287 | 2026-08-05 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 201.4 |
| beb588fe-2fa3-3b5f-b0ce-0e4127220a3a | -20.896 | -44.9072 | 2026-08-05 13:10:00 | GOES-19 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.6 |
| 8b1c9c29-7e44-3c76-89d9-abebecdb568d | -12.5947 | -46.9301 | 2026-08-05 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 22abe5d1-8bf2-37f6-a4d8-216f8d58c252 | -12.5938 | -46.9753 | 2026-08-05 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 0da03320-2d0d-3b18-83ef-6cf4893ee60b | -3.43056 | -60.43929 | 2026-08-05 13:14:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 28512b6c-84e0-34da-bdb6-8c1b32918381 | -3.43009 | -60.43266 | 2026-08-05 13:14:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 171c8f83-e0b7-3390-96cd-9079d0cb22dd | 0.40333 | -62.34211 | 2026-08-05 13:14:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1931c1a1-8594-3e2c-8c3f-c9d1d47a59ec | -6.66698 | -69.28137 | 2026-08-05 13:16:00 | TERRA_M-T | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b5e6daea-963f-380f-ad2b-0b73d5548718 | -9.86165 | -61.41378 | 2026-08-05 13:16:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 5ebab7bb-a3e6-3449-8b94-73cee04d1714 | -14.2682 | -45.287 | 2026-08-05 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 221.2 |
| bd35c46b-0cdc-35b9-9de8-81d1ede61b96 | -13.2604 | -54.2662 | 2026-08-05 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| f8065211-98e2-3785-9406-bae13cb93b04 | -7.2293 | -45.7801 | 2026-08-05 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1f3f6baa-0e48-3c75-84de-f58d60a11feb | -7.2187 | -43.3499 | 2026-08-05 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| f7d9618f-363b-3ba5-ba3c-65a75f91e874 | -20.896 | -44.9072 | 2026-08-05 13:20:00 | GOES-19 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.7 |
| 1841d1a2-4f2e-3e94-b18c-928effe731a3 | -13.2413 | -54.2683 | 2026-08-05 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 8b2bf5ec-6de0-35d5-bd94-db66791e5b30 | -6.9879 | -42.1201 | 2026-08-05 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 6bbca101-9200-360f-bbf3-692835bd9654 | -14.2487 | -45.2904 | 2026-08-05 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 9651a22e-a218-35ab-8642-de8c7a020199 | -11.3111 | -44.7873 | 2026-08-05 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 782bd21f-2317-3279-92e3-8512b1ae8488 | -14.2687 | -45.2636 | 2026-08-05 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 11be9901-c434-3c0c-b7d7-259fef920046 | -10.9192 | -50.4283 | 2026-08-05 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| f6572740-2e11-32fe-9346-d3b1d15298b9 | -14.2487 | -45.2904 | 2026-08-05 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |


[Clique aqui para ver as próximas entradas](README31.md)
