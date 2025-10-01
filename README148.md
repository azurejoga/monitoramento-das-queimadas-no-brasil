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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7cf6d0f-86cd-34ab-acce-02500d18a8f3 | -11.829 | -48.0619 | 2025-10-01 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 957bf2f0-c841-3ff2-83c8-8f48c1fb4e4d | -11.8438 | -44.964 | 2025-10-01 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 958640f0-5f1f-3242-8702-f15318c75248 | -14.3514 | -45.9437 | 2025-10-01 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| e8faed77-3a71-3dab-92bb-b0fd6f9e98b2 | -14.8016 | -45.8178 | 2025-10-01 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 52034e10-38a1-3189-ba74-30d644ce2e77 | -10.9769 | -46.5443 | 2025-10-01 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ede48a47-2abe-377b-b4dc-3394bef08f00 | -14.4943 | -48.4553 | 2025-10-01 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c969ec36-90a2-3637-ae82-839a2fcc4d2e | -7.8882 | -47.281 | 2025-10-01 12:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 7ccfc2d9-d658-3a7a-9066-78186b10ab4e | -14.3524 | -45.8974 | 2025-10-01 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d6ccf2a1-d017-34ff-a0b5-8d954b23fdb7 | -10.0906 | -50.2154 | 2025-10-01 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 063e151e-4da9-343f-9419-2f093ec2b8cd | -14.8021 | -45.7946 | 2025-10-01 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 94d70bee-10fd-33be-a35e-5ec0cc1c06c7 | -11.9254 | -48.0051 | 2025-10-01 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 18c7f6d8-0749-34d8-a5e9-2d3e6e1e4c60 | -9.8201 | -47.8386 | 2025-10-01 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7c300f20-aea6-3e85-98b7-d07dfa40d390 | -14.3519 | -45.9206 | 2025-10-01 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 5978f92a-4197-3950-bca6-0cdeaeb78dbc | -13.3278 | -47.8313 | 2025-10-01 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 548ca863-31eb-37e6-8386-162515356678 | -11.4596 | -45.0433 | 2025-10-01 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| c44cf2e1-a039-3709-9cb4-b6fe29094928 | -9.9186 | -43.6978 | 2025-10-01 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 0557d735-a15f-36fb-ae04-6ed335ce8459 | -14.1732 | -46.1124 | 2025-10-01 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 754d1d5a-08e0-3066-929b-f06b7cb888d8 | -13.1747 | -47.7869 | 2025-10-01 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a4c1f0f2-193a-3247-af4c-5ac0db7aba4a | -9.0236 | -46.7052 | 2025-10-01 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 6a170259-9fe4-33d5-84a8-0f2cfc4afd4f | -8.672 | -47.7144 | 2025-10-01 12:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| bbc5b0cc-0de7-3831-8cd4-9689865ee308 | -14.4947 | -48.4329 | 2025-10-01 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 1b1e29f0-f97d-3384-9c02-9f974d72759d | -14.1926 | -46.1091 | 2025-10-01 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 2f8d9b8f-a414-3131-b1be-90555e966eb3 | -12.7022 | -45.2715 | 2025-10-01 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 4badb582-ee44-32de-b006-6088ec5cd638 | -11.46 | -45.0202 | 2025-10-01 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 231.4 |
| 7d4195a6-ed77-370c-bd7b-f0cad27bba5f | -14.8026 | -45.7713 | 2025-10-01 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| c63c621b-d0db-31f0-b012-d90ae2f6b46a | -14.3714 | -45.9172 | 2025-10-01 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 202.8 |
| 72db9586-cc87-39a8-bf3a-c45628362a4f | -9.4458 | -47.5923 | 2025-10-01 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 4d9fc7ce-c443-3565-8716-144626865740 | -7.8002 | -46.7578 | 2025-10-01 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f6ac5a03-a347-3f4b-9248-c1f1613fd549 | -14.9738 | -46.8668 | 2025-10-01 12:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ce279fce-6ab0-3cb0-a29e-4b5ab6d09f05 | -15.9388 | -43.2979 | 2025-10-01 12:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 7cef5c8f-a536-38aa-84c3-f25eb520a38b | -11.4409 | -45.0229 | 2025-10-01 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 84b8e794-aff0-33af-810b-d353940ef9af | -14.9733 | -46.8896 | 2025-10-01 12:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0726fce6-eb6e-3205-90fb-e5f2a96696f8 | -15.9381 | -43.3223 | 2025-10-01 12:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 07876923-38d6-3472-9202-5696d7c4e115 | -8.7084 | -44.8398 | 2025-10-01 12:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 82a360b6-d919-3eba-9851-412037d57e64 | -11.8618 | -45.0307 | 2025-10-01 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 72be46eb-5cd9-3cd9-8c31-17af3eaaf24c | -8.9182 | -47.5803 | 2025-10-01 12:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 5f3a0c25-e16c-3ee7-9fd2-65119711cb91 | -12.7815 | -50.5758 | 2025-10-01 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 02343778-32fd-37ba-a400-cf02fbfed34f | -14.3514 | -45.9437 | 2025-10-01 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| ead0bbd3-6c79-3269-924d-73b9da1b448b | -14.8016 | -45.8178 | 2025-10-01 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| cabff744-f9ab-3648-8785-4a219df6db70 | -11.8622 | -45.0075 | 2025-10-01 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| d2873518-37e6-318b-b276-7b2ac8904773 | -12.7819 | -50.5543 | 2025-10-01 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 224.9 |
| 120b9750-fab2-346d-909a-9498c24e195f | -14.3519 | -45.9206 | 2025-10-01 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| ad87282f-d952-3574-97f5-b7b76203345f | -11.9272 | -47.8941 | 2025-10-01 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 641afd1e-ee3b-3a88-a40b-e3d4c525d468 | -10.9773 | -46.5217 | 2025-10-01 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4bf9b057-276a-3d95-ba72-55678346faaf | -9.8201 | -47.8386 | 2025-10-01 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| e6f81c9d-29c3-30ce-9d12-ca0189f73ab2 | -14.3714 | -45.9172 | 2025-10-01 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| f4661058-cf00-3911-8a0d-aa8548c4adca | -8.8609 | -47.6521 | 2025-10-01 12:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 1bc7aa91-1999-3d78-816d-c13a77df2553 | -9.9376 | -43.6953 | 2025-10-01 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 5ade5f01-8224-3e65-9262-8cb1024a8cb3 | -10.1081 | -50.3203 | 2025-10-01 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| e7e30a22-6e2e-383b-b808-df54bf602265 | -10.1084 | -50.299 | 2025-10-01 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| c0e43c25-fb9c-3119-9aad-d2af545b28b7 | -9.938 | -43.6718 | 2025-10-01 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 9f2218e1-6c02-3293-a3bb-f0bd568e4ad5 | -11.8482 | -48.0595 | 2025-10-01 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 3f804a59-e022-3cb7-9d4b-174a2f0bac31 | -11.4596 | -45.0433 | 2025-10-01 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| ea00510c-fff9-3104-a806-10ec81fcaf40 | -14.3334 | -41.5347 | 2025-10-01 12:20:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 8e4119e4-1a4d-3083-86ae-be94afcc2226 | -8.483 | -47.7983 | 2025-10-01 12:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 782fbba8-b8d2-3a6f-99b5-9f58a05e6926 | -11.383 | -45.0543 | 2025-10-01 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 997503e3-483d-369e-a796-e530feddcd24 | -8.5773 | -44.7623 | 2025-10-01 12:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 86e3d037-4cb2-320f-a67d-63babd85bbfe | -10.9769 | -46.5443 | 2025-10-01 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 227.4 |
| 42e7c6ad-9f21-3dcf-ad6d-bf7854404f19 | -15.9388 | -43.2979 | 2025-10-01 12:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 125.1 |
| c8932bd4-670a-3cd9-8fed-38eb4abc75b7 | -8.8797 | -47.6502 | 2025-10-01 12:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a08510df-d718-36eb-ba58-6d6e3519999d | -9.9189 | -43.6743 | 2025-10-01 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 2c01581e-0e56-38e9-ad87-6b3785bb9c54 | -14.8021 | -45.7946 | 2025-10-01 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 7a68dc51-91ed-303b-93d9-73cb6e66f542 | -8.5776 | -44.7394 | 2025-10-01 12:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 077f53be-8355-3bd3-b330-0a49b13b73de | -7.8002 | -46.7578 | 2025-10-01 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b1b30c81-26bc-34ff-8c45-475e1693c928 | -10.0906 | -50.2154 | 2025-10-01 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| c6d2ddbb-0cab-376b-a5ba-d6a1aa49e909 | -8.5079 | -47.2897 | 2025-10-01 12:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| b0e95d43-a612-3f78-aa69-55142e097abc | -10.9579 | -46.5467 | 2025-10-01 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 66824710-1d49-3034-81aa-2d1a97c320b8 | -10.9388 | -46.5492 | 2025-10-01 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 39c3bdd7-ec7f-3eb0-b1eb-ba355998faac | -7.8882 | -47.281 | 2025-10-01 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 34c31636-4f13-305c-a401-5d848be31819 | -13.3221 | -48.1439 | 2025-10-01 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 281e7d94-63bd-3904-88b4-51a618a7d3b0 | -12.7627 | -50.5567 | 2025-10-01 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 844aa81b-eb5d-31a1-a0aa-be3f4ba97b97 | -8.672 | -47.7144 | 2025-10-01 12:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 6ac48e83-9907-359e-adb8-96c0473c11fb | -11.46 | -45.0202 | 2025-10-01 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 194.5 |
| 0d4f0eea-7071-33e2-a0c3-27948725a920 | -11.8673 | -48.057 | 2025-10-01 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 7c03628d-af40-334d-94fe-97895ccd99d3 | -9.9186 | -43.6978 | 2025-10-01 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 674cc1b0-96e1-35f7-b38a-374739acbe8a | -13.3414 | -48.1411 | 2025-10-01 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 96519fbb-dd07-3db8-8315-40927ddc90f6 | -14.0402 | -45.0479 | 2025-10-01 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 225dbdf6-1c0c-310a-92f0-3be9c5801cf8 | -11.829 | -48.0619 | 2025-10-01 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 6022f3a5-b465-39d2-b647-cac3412b2763 | -9.1248 | -47.6256 | 2025-10-01 12:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0d8d3072-0595-3380-b475-a83bcf965fe8 | -15.9388 | -43.2979 | 2025-10-01 12:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 214.1 |
| c437fad3-bbe4-3870-89c6-a0f865e35e1f | -7.8882 | -47.281 | 2025-10-01 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d77b477d-040e-3716-b7bc-9ce1c725a415 | -11.8482 | -48.0595 | 2025-10-01 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| a247e601-edcc-3577-9f20-69540bf40dd1 | -10.9773 | -46.5217 | 2025-10-01 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 66714126-b3b2-3b5b-af6d-623ca71e32d3 | -14.5137 | -48.4522 | 2025-10-01 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| f5bf0008-16ec-3f70-8a01-529426733201 | -10.1084 | -50.299 | 2025-10-01 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 40cd5313-c754-3bea-a3dd-685a48a22f5b | -12.2536 | -47.806 | 2025-10-01 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 6aea9a24-f985-3b60-a636-65888ac7d0ef | -8.5773 | -44.7623 | 2025-10-01 12:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 788d9a02-0fe8-308b-bef9-c29dca67dbad | -14.8026 | -45.7713 | 2025-10-01 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 02984c5f-49fd-3c58-8c9f-42142d502afe | -11.46 | -45.0202 | 2025-10-01 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 2d08a0b1-bf07-3b6d-8c24-802cfcba1f33 | -14.8016 | -45.8178 | 2025-10-01 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 29ec6c6a-2f12-3798-babf-de9be3651838 | -8.5404 | -44.6975 | 2025-10-01 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2020862c-660a-3f59-87d7-695eddd72d40 | -14.0581 | -47.9883 | 2025-10-01 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 3531b8d7-c7e5-3845-b3ad-1e3263f73df1 | -11.4596 | -45.0433 | 2025-10-01 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 180.6 |
| b9b1a9c0-27ee-362b-9c67-316b35cedb23 | -10.9388 | -46.5492 | 2025-10-01 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6a54d0ad-8591-36d6-99d5-5f459cf4bea2 | -7.5749 | -46.7778 | 2025-10-01 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 3c274151-d06c-35cf-8e5c-c639e49007f2 | -11.8626 | -44.9844 | 2025-10-01 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 6b4bd2dd-7e01-3ade-aea9-82f4151b37e7 | -12.7819 | -50.5543 | 2025-10-01 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 4653b71b-864c-34df-af5f-ba0ef69b1c08 | -8.5079 | -47.2897 | 2025-10-01 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 64f2a31c-2e69-3e62-ab88-30539a192c56 | -11.8622 | -45.0075 | 2025-10-01 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| aafe6f1b-c03e-36a8-9ca6-18f38bcc5998 | -11.9411 | -47.0675 | 2025-10-01 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |


[Clique aqui para ver as próximas entradas](README149.md)
