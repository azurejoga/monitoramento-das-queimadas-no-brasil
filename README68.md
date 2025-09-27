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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6efd8e9-d961-3dc6-a033-9eef5c90b399 | -9.8781 | -47.7441 | 2025-09-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3a50c014-205f-380a-88d3-65fa22c709ad | -11.3846 | -44.9618 | 2025-09-27 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 389c7a58-ee5f-37a7-9de6-b0c9e429e77d | -9.8784 | -47.7221 | 2025-09-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 775b8362-2a7c-3ea7-9bda-86b66d815308 | -5.407 | -42.2812 | 2025-09-27 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| a48abaf0-6a42-32df-a712-e30f5fd9435f | -4.1947 | -44.2706 | 2025-09-27 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 628e3c28-c314-3b10-8342-999ae7f6d7ea | -8.6442 | -43.9931 | 2025-09-27 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 7f63ba17-9df9-35a5-8874-9821c4a185aa | -11.4225 | -44.9794 | 2025-09-27 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| a49642cb-5507-39b1-b77e-7573c29c4e19 | -12.2829 | -44.0568 | 2025-09-27 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f34ec18e-0a9e-392f-9227-f2d74b58b2dc | -6.2501 | -42.4736 | 2025-09-27 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| b63068ae-8d56-3bef-805b-240ab4c478d3 | -14.0191 | -56.0927 | 2025-09-27 14:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 36e42937-ed68-3187-b819-024fbf10aa15 | -9.3514 | -47.6022 | 2025-09-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 1814f266-064d-3d70-b3d9-fc4fb44a4151 | -9.3702 | -47.6002 | 2025-09-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| b9457e13-2a26-3cb3-af9e-b1a9f1f9154a | -5.7413 | -42.6576 | 2025-09-27 14:10:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| 7bf8e2be-51c7-3aed-93bf-55b5e85cd18d | -8.8415 | -46.2095 | 2025-09-27 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 920ee190-8ea9-30d9-9c38-71f484423c0c | -8.6631 | -43.991 | 2025-09-27 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 72fa3d5d-ef5a-39a0-8d1c-22d9ad8eddf9 | -4.1946 | -44.2935 | 2025-09-27 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 8f6a667c-a834-3e59-b4a5-d9eda6f253a4 | -14.85 | -45.3911 | 2025-09-27 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 185.9 |
| f9fb88c7-0dea-32db-ba63-dc4f6dd8fa8e | -15.2136 | -56.0047 | 2025-09-27 14:10:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 5cb33345-e247-33da-a510-985918ace53e | -6.6009 | -44.9053 | 2025-09-27 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d2dcb946-1552-3d4d-9436-dec390624b16 | -8.8226 | -46.2115 | 2025-09-27 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| a2537f2b-9cef-3014-b096-617e26120380 | -8.1619 | -46.3451 | 2025-09-27 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1a48c289-a5db-385e-b77a-edd8825d8b4c | -7.3659 | -47.0394 | 2025-09-27 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 168.6 |
| d0ffbe63-1030-313d-b6a1-82a0f7cd6a78 | -4.1759 | -44.2945 | 2025-09-27 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 349a88d7-ea01-3a07-a508-d0870714a970 | -9.6159 | -47.5741 | 2025-09-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 152.7 |
| b32564b1-76a2-3122-a93e-12a7a0817e49 | -18.3049 | -57.0938 | 2025-09-27 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 178.2 |
| 03dd69e5-f7d2-3823-a6ed-f036cf765056 | -11.4221 | -45.0025 | 2025-09-27 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| fee3af8d-9928-3fb8-84d8-c46ef3df9959 | -7.7558 | -47.3809 | 2025-09-27 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| bb3c1813-2fcb-3746-9b3b-103ddcc8eb88 | -9.8971 | -47.7421 | 2025-09-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 7adb102d-24eb-3f37-97a7-ec67a624b8b4 | -9.3517 | -47.5801 | 2025-09-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| d16dde82-af6f-3e63-b1fb-4436600a6f45 | -7.7609 | -46.9166 | 2025-09-27 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 730b9925-6a00-3bdb-bcc7-516830bf62ea | -9.1099 | -45.8879 | 2025-09-27 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| d524bbb9-c738-3d26-9dea-6ae246d380f5 | -17.1739 | -56.3892 | 2025-09-27 14:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 92a4923d-ab9b-328f-a91f-25ddb039d5e2 | -5.6813 | -43.0619 | 2025-09-27 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 215.9 |
| 30aed329-f81f-37cf-9a0a-4225cc0758ca | -7.2605 | -42.9939 | 2025-09-27 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| bf0ef0aa-5f07-307f-8bca-3a80666650ec | -11.0125 | -45.5189 | 2025-09-27 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 0824658f-67d7-33ac-9782-960d18dbd3fe | -11.3646 | -45.0108 | 2025-09-27 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 0357590c-cd8f-30e5-ad62-de20e15e08ae | -20.7342 | -57.7873 | 2025-09-27 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 6bce685d-ffcc-3992-85c7-d11c42be67b4 | -9.0422 | -46.7255 | 2025-09-27 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 8c0b401a-0cc4-3495-8bfa-f20f91eb4f4b | -6.698 | -44.5774 | 2025-09-27 14:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| ac8e3634-b994-3d43-9d1d-aabd31d41250 | -7.798 | -46.9576 | 2025-09-27 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 01754f3c-402b-3f89-9906-04801cd5b680 | -5.6223 | -43.3701 | 2025-09-27 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| e5a14e69-b277-39b1-8fa1-e9efe9db4865 | -8.6628 | -44.0142 | 2025-09-27 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 7eaf82c8-663e-379d-b69f-19bd4b843c82 | -14.8309 | -45.3714 | 2025-09-27 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| cff51e08-91a2-32fc-8a2a-477c1ec51798 | -6.6986 | -42.741 | 2025-09-27 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| e9f938be-a36c-3e14-9df0-75f221f31f1a | -7.8735 | -45.2911 | 2025-09-27 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 7f9ccf66-e577-3bd9-9cca-2996b26a6531 | -12.6498 | -48.1509 | 2025-09-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 38a00058-1d72-3151-b087-d38bdc72f6ff | -14.8304 | -45.3947 | 2025-09-27 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 480.8 |
| 73ee5b1b-40b9-39e5-94c4-9b6a5a60146b | -6.5163 | -54.8784 | 2025-09-27 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 0adca988-b42a-3862-9264-3a10c2f18da8 | -11.385 | -44.9386 | 2025-09-27 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| a77ed68b-416c-3a24-9863-db59c6407a48 | -6.0593 | -44.7432 | 2025-09-27 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 9368c9c0-a3ec-364f-aee5-a26309568f38 | -5.7227 | -42.6354 | 2025-09-27 14:10:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| a76441c5-fc06-30d1-bd04-f6169ed4fb16 | -7.1383 | -45.5174 | 2025-09-27 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 88458587-cd11-3ae8-a00f-6f2d1e722b9a | -7.8637 | -44.5382 | 2025-09-27 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b2c99302-0488-3841-b2ed-bec2c52c8f54 | -8.4825 | -47.8421 | 2025-09-27 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 6cf5e2fc-eee1-38f4-8eea-eb3c4f537446 | -8.822 | -46.2564 | 2025-09-27 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 2a4c058b-809a-3ad5-8b83-5a825daadd1c | -9.3343 | -48.9364 | 2025-09-27 14:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d08fcfdd-de03-38c5-8e17-0ce41d6f354d | -10.4215 | -48.1234 | 2025-09-27 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c22ca0f5-8ab6-3439-928c-39bed8248cba | -5.7959 | -42.8417 | 2025-09-27 14:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| d3b20ebe-24cb-3251-be0b-4614db5a2ee8 | -11.7006 | -44.4049 | 2025-09-27 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 0b128430-380c-3416-b77e-c685b2576ce4 | -9.9772 | -43.5962 | 2025-09-27 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 202.8 |
| 624fdc74-3562-311f-9f53-612510d78af7 | -12.0369 | -47.0543 | 2025-09-27 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 17bc9aa6-67f1-3552-96ad-aa5d18e01a17 | -3.8277 | -40.3373 | 2025-09-27 14:10:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 125.5 |
| b6071db0-fa91-350c-972b-965b06b31fe1 | -14.8299 | -45.4181 | 2025-09-27 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 97a17649-b132-30e9-8cb6-fa26ecbfcba2 | -10.4025 | -48.1256 | 2025-09-27 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 6a1f0043-b496-30b8-8ee6-d1a2a776b423 | -5.7961 | -42.8182 | 2025-09-27 14:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 45f36ec7-7df4-398c-9563-1aef9409fd33 | -8.6328 | -44.848 | 2025-09-27 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 0fdc5072-2ca0-3f48-bac5-0d836e59fb87 | -8.6517 | -44.846 | 2025-09-27 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7defbd89-7de1-399e-9243-f143bc467081 | -5.7588 | -42.7976 | 2025-09-27 14:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 75808360-3ea5-32e9-a428-93dfb96ded96 | -7.7797 | -46.9149 | 2025-09-27 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 17198b3d-3557-3b45-8b58-545fb02ce4c5 | -11.4417 | -44.9767 | 2025-09-27 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 254.8 |
| b8af20b3-8ae1-3d3c-a461-0b4c32073602 | -5.5056 | -43.866 | 2025-09-27 14:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 28b2410a-b8c9-3528-8cf0-e234ca24250c | -9.3511 | -47.6243 | 2025-09-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e58e3c85-3d6e-30d9-b8b9-039c97ede9f5 | -7.8732 | -45.3139 | 2025-09-27 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 35f91541-d0d3-3542-ac74-4c725ed1b637 | -11.4413 | -44.9998 | 2025-09-27 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 211.9 |
| c3c0dd86-79bf-3f06-81d5-7af9725c9969 | -5.3693 | -42.3077 | 2025-09-27 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| 8407c018-a86f-329f-b729-f5009d35316b | -9.4269 | -47.5943 | 2025-09-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8b28b352-4ef9-3963-90ac-121c4b938495 | -11.3642 | -45.0339 | 2025-09-27 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| d3c0a458-bfc4-36d7-8806-f5b01492e64c | -7.3659 | -47.0394 | 2025-09-27 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| bbacaad9-2f05-3214-ab28-45df0552599d | -8.8226 | -46.2115 | 2025-09-27 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| c0c467ab-f3d5-3a84-a6d4-245d6c30d0eb | -11.4425 | -44.9303 | 2025-09-27 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| d88bdc78-3112-380b-a9de-a60bf829381c | -11.3654 | -44.9645 | 2025-09-27 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| b5f4a571-1cca-3411-9870-366a435f59ec | -5.8149 | -42.8167 | 2025-09-27 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 1b2dbc4c-0121-34ce-9d71-663ac6105d31 | -4.6946 | -37.661 | 2025-09-27 14:20:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 136.9 |
| fbc2ad1a-7919-395d-8893-6eaf441e4e70 | -5.7775 | -42.7961 | 2025-09-27 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| da6df905-262e-3a56-856e-a02a2ac5c3e9 | -7.7794 | -46.9371 | 2025-09-27 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 375.9 |
| 2f125722-c240-315a-9e0e-cbe0117206ee | -9.8971 | -47.7421 | 2025-09-27 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 9b7fb440-25af-3d34-93c5-4ffa6dbbc28b | -7.1571 | -45.5158 | 2025-09-27 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 994b3978-6195-3bcb-b027-a83a951c5c4b | -5.5056 | -43.866 | 2025-09-27 14:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 25210eeb-8630-3e8e-a0b0-b6542d3bc5c0 | -20.564 | -57.1616 | 2025-09-27 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a2cbe331-370a-3b64-9afb-b131a615ec3e | -9.3343 | -48.9364 | 2025-09-27 14:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 4c6f0458-3503-3d0e-b273-bee94cbe59e4 | -6.5163 | -54.8784 | 2025-09-27 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 97ae3b97-caaf-3b1e-bf51-4de577f4097c | -9.8784 | -47.7221 | 2025-09-27 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 24414175-0783-3f07-945d-3817b83c4ae2 | -7.3849 | -47.0157 | 2025-09-27 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 257.0 |
| 23c5554c-14ce-36b7-9443-31d782ef3af1 | -7.6064 | -47.3278 | 2025-09-27 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 0f230a79-5989-36b6-8511-1248bbfa9f5f | -15.54 | -44.3169 | 2025-09-27 14:20:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 322ecc4a-0c58-3ada-bf14-2b0e1d810614 | -12.2829 | -44.0568 | 2025-09-27 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| aebf5fea-d79d-36c7-abad-f1ba7042dd1c | -9.0391 | -45.5334 | 2025-09-27 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 2d82cd2d-93c3-3bc6-a2e1-97c4ec667f6b | -11.3646 | -45.0108 | 2025-09-27 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| d68bd41a-80b0-3393-9967-688e1ff54687 | -7.6062 | -47.3498 | 2025-09-27 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 1e90f1c6-2b05-3c44-981a-113490938d8a | -11.6058 | -45.4364 | 2025-09-27 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |


[Clique aqui para ver as próximas entradas](README69.md)
