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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab82968d-8835-3764-8f56-4cc1bfe2a557 | -3.93844 | -46.41539 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3141f768-d01f-3233-8bf8-3a459f590551 | -3.93565 | -46.4114 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3e607a8-3ff6-3e82-b58c-7e17b646aeb8 | -3.92841 | -46.41382 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| e13d752e-48a7-3b02-a18c-071be9ad5cae | -3.90558 | -46.42819 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fb62449-ab80-3853-9255-cca7315ded0f | -3.90224 | -46.42768 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3837f4a2-5e12-3cc7-bd2f-fae9e22b0ca5 | -3.89725 | -46.45912 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08168d68-2ab3-34b1-8c9e-49d2fdea2970 | -3.89557 | -46.44811 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d37f1383-59c7-3d43-b5b5-8007e3090d6e | -3.8939 | -46.45859 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adb99597-f53d-38f8-a390-22f7c2932313 | 1.0199 | -52.2162 | 2024-10-15 04:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 74205f9f-2881-3730-94e2-89d17e39c14b | -9.20592 | -48.6656 | 2024-10-15 04:25:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64bb91b4-7505-3726-92aa-07811d00ff66 | -9.20371 | -48.65751 | 2024-10-15 04:25:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04f8d21c-bf8a-3f69-9295-8657ba7a9661 | -9.20311 | -48.66122 | 2024-10-15 04:25:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 026104b7-8360-3011-bb44-e8a763b50c8b | -9.20249 | -48.66501 | 2024-10-15 04:25:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d9e0245-79f4-3a6a-b1bf-f770ccf5f04e | -8.74887 | -47.55367 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 573276ac-10c8-3d11-9d11-dc9fdfe79846 | -8.74552 | -47.55313 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 868735bd-46b4-307d-b824-fc468048ad5c | -8.70651 | -47.53957 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93540dbe-3cdd-3904-a975-30a0d96179f9 | -8.69313 | -47.53738 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e8467d0-3008-3d07-b2fd-dd9af1263783 | -8.68979 | -47.53685 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7341d4f1-9390-3f0d-94f8-b9f3f306a70a | -8.5572 | -47.81519 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44c6edb7-7c00-3674-a540-cf44adc2232a | -8.5521 | -47.82538 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ce5ec17-b6d6-3e23-8187-00de5fb14975 | -8.46919 | -47.81907 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61cdc3d4-cbeb-3952-91b6-8276264a8d0b | -8.46697 | -47.81137 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| feb51955-70ec-33a3-935c-b8bb20fb3dc7 | -8.4664 | -47.81496 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f14edefb-725f-323e-9881-aac06b743534 | -8.46582 | -47.81855 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 525de93f-1f82-35a0-b65b-a1da78641b5b | -8.46418 | -47.80726 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11ef3ccd-c6ce-3bd4-8e56-714e12c84e59 | -8.4636 | -47.81084 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69cf4df8-c3dd-32ac-b6f9-fa632f4d1142 | -8.46303 | -47.81443 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6571b27c-2df8-354d-b28d-ab1943fed69d | -8.46081 | -47.80672 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3366785c-5d08-335d-a1f0-3e9a80f67975 | -8.45802 | -47.8026 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 94ae1fc3-e191-3d9a-8e47-c1928d94342f | -8.45745 | -47.80618 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ced0c57b-04fc-3632-b25b-699d1587c8ad | -8.45465 | -47.80206 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 773729e4-a801-367c-9da7-fb20ba801e10 | -8.45408 | -47.80563 | 2024-10-15 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f67743d-2ad3-32b4-938c-1e1c431b21af | -8.44571 | -48.02999 | 2024-10-15 04:25:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b500425c-55f5-3325-85b5-aaf571799adc | -8.44513 | -48.03361 | 2024-10-15 04:25:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 363bc462-88bc-395d-ba73-e66b1b34484f | -8.28485 | -48.13891 | 2024-10-15 04:25:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 592aa846-71ce-34e5-8581-27aab9b9861e | -8.28145 | -48.13836 | 2024-10-15 04:25:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2880a34-02e1-35bf-9a48-e90f2814641a | -8.13168 | -47.57478 | 2024-10-15 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f06da489-8c24-36f6-922b-80a992bd2703 | -9.32914 | -47.37188 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d477255b-cb70-3a28-b0da-9407d542d830 | -9.32636 | -47.36783 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3340fd8-2808-3379-a0c1-18894352b597 | -9.32581 | -47.37135 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04b21b24-23ce-30dc-8c9f-f531b4580c39 | -9.28856 | -47.73508 | 2024-10-15 04:25:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74594b4f-3828-32fb-b6a2-7804ea5b0b68 | -9.28535 | -47.89537 | 2024-10-15 04:25:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46baec02-659f-355c-b282-1fb120e6d99b | -9.28199 | -47.89483 | 2024-10-15 04:25:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94ee7b7b-dbab-327f-9e03-f53498a57261 | -9.20071 | -47.56482 | 2024-10-15 04:25:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f65522e0-7b3e-321b-beb6-a037a367af7d | -9.16443 | -47.59887 | 2024-10-15 04:25:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 466f347a-74f6-3027-b673-9fd3ccc3b8bc | -9.10356 | -47.93632 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14bf390f-1acc-33e3-9d50-7f29e2277ca2 | -9.1002 | -47.93578 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11dcc948-6a91-3a88-bb9f-9a6d70df9ddb | -9.03408 | -47.97317 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd80720a-58e7-3c6e-ac0a-bdd2b65f880a | -9.99884 | -48.85846 | 2024-10-15 04:25:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 088bb547-b95e-3af2-af08-e54b3f96c69b | -9.99823 | -48.86219 | 2024-10-15 04:25:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e264e6e-fab6-3317-9ae8-79537a5fa10f | -9.89917 | -48.76159 | 2024-10-15 04:25:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cd8b0f1-15cf-3909-a76a-05a3f5524c8b | -9.89636 | -48.75732 | 2024-10-15 04:25:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49ce8727-bfaf-3566-998d-64ac0b95ed0c | -9.63842 | -48.54092 | 2024-10-15 04:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85012b79-a321-386f-8e80-747cbd978130 | -9.61929 | -48.70159 | 2024-10-15 04:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 726eb431-edd1-3124-92f2-f0c939c38537 | -9.64608 | -47.40141 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48fff5b4-2295-3d73-bade-9dd995d80820 | -9.60672 | -47.71369 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9296b139-9dd6-3e2e-befc-3465c02936b9 | -9.59998 | -47.73442 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ca56fff-07a2-376a-a0ff-830db48b9819 | -9.59946 | -47.71614 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a67d767c-7034-3d8c-a7fe-a0e8c3f12130 | -9.59612 | -47.7156 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f04b425-dbc1-3877-97ee-d4386030a15c | -9.53726 | -47.63337 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb15e722-1f03-3a86-bf37-391dbe3e310f | -9.53392 | -47.63282 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91bad385-9f44-38fc-bcc9-a5e78c24826c | -9.52674 | -47.78445 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49d4caa4-9682-31fa-97ea-ee6be5a4d9fb | -9.52617 | -47.78801 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| de20102c-92a1-367e-80b3-2acbb2bff387 | -9.52502 | -47.79515 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eff6f813-35c7-3b17-bfed-217f32054b61 | -9.52168 | -47.79461 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e07cd1e2-7327-393b-85ad-891f74813d60 | -9.5211 | -47.79817 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b42e0842-98b1-36ce-ac5c-0173d490e791 | -9.51718 | -47.8012 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96f63195-9afe-3c15-b671-9c93eda8b772 | -9.51383 | -47.80066 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d511417d-1c75-3be2-b57b-8689fbdc25dd | -9.49757 | -47.81625 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6f9fa0f-d349-3360-8331-13cd700e195d | -9.497 | -47.81981 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 267f7851-574e-3015-94ce-8b42197dc388 | -9.49519 | -47.81909 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67f42156-13e1-34f6-8dac-dc4d949a994e | -10.14091 | -48.82343 | 2024-10-15 04:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b3078ab-f225-3ece-aaf0-e5fb48577b9f | -11.62885 | -48.50489 | 2024-10-15 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c44c9783-0b89-3b73-ba0a-7159d67db2b0 | -11.04958 | -47.93643 | 2024-10-15 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4f65669-b07e-3014-8d55-a4ace552eb1b | -10.94493 | -47.93385 | 2024-10-15 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8aafd51e-a01e-3ecc-bc06-104f146875cf | -10.94217 | -47.9297 | 2024-10-15 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90f22988-0fae-3f6c-9a86-5c6b6e1aa491 | -10.94159 | -47.93328 | 2024-10-15 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 426ccd58-20c8-398c-bf5d-febd0fa43bf6 | -10.92383 | -47.91581 | 2024-10-15 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd9d0bdc-8935-356d-b722-19450bd97779 | -10.92106 | -47.91174 | 2024-10-15 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d68f37f-5eeb-3c6d-a794-71b61ee4e2ee | -5.43462 | -48.96992 | 2024-10-15 04:25:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38510e07-a67b-3422-b7ca-6c0b76606b19 | -5.25992 | -48.06849 | 2024-10-15 04:25:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a1eb674-09b9-34f3-a04d-0713a42e7afc | -5.25645 | -48.06794 | 2024-10-15 04:25:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64042886-4eae-3b8d-a81c-afcae1c3cc71 | -5.25583 | -48.07174 | 2024-10-15 04:25:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4a03058-d58a-34ae-b48d-15ed4381cf3a | -6.57852 | -48.2352 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 92493557-9339-314b-a47a-48b32862da59 | -6.57791 | -48.23898 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 9caa2a57-aa07-321e-84db-8982bb923267 | -6.57731 | -48.24275 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 4e61ac61-4fd1-3a46-ad62-1135409cfb30 | -6.57568 | -48.23086 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 19.3 |
| bc558992-c7c8-37e7-a9b8-d155372cb313 | -6.57507 | -48.23463 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 19.3 |
| b51ed981-30f3-341c-af91-9f0d4299e8aa | -6.57446 | -48.23841 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 33.9 |
| b46cf017-bf36-3e42-be3c-10d6b312a7eb | -6.57385 | -48.24218 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 0042aa1a-3c54-30d2-83b0-8ed1d79698ca | -6.57325 | -48.24597 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c1193e8-c0a2-3644-80dc-b7213d84ac65 | -6.57264 | -48.24975 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f635e0fd-2be2-3a80-b305-69b40e1036e3 | -6.57223 | -48.23029 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26ef36e3-6176-341f-a93b-43b4113f9022 | -6.57162 | -48.23407 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b14172b-eac0-3549-a57a-2f06a7a8aec3 | -6.57101 | -48.23784 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c584c6d5-72b2-3904-9afb-1c652a51f2f5 | -6.5704 | -48.24162 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c86ce51a-c198-35a8-835e-e60c825e01d5 | -6.56979 | -48.2454 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c5055799-db03-37d9-bf07-b3879e385fc7 | -6.56918 | -48.24919 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 714f609b-a29b-3c89-9d1b-cc100d18290a | -6.56878 | -48.22972 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7053c151-b886-3062-ab61-c1ce2077224b | -6.56817 | -48.2335 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README43.md)
