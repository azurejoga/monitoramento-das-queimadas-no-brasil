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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 537bbe37-02ac-3c27-a19c-177008577e6f | -8.9368 | -46.132 | 2025-09-13 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 28f3686d-5199-3675-9ad5-621ce63b9e49 | -9.2503 | -51.2472 | 2025-09-13 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 50889473-ff14-3aae-9b9f-3715f0083620 | -14.2092 | -46.2439 | 2025-09-13 14:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 24460f45-3523-3c91-bcc1-07515a74c7cc | -14.4327 | -52.9197 | 2025-09-13 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 34a1064d-e1d3-3ab8-9af0-83cceedbb84d | -16.0061 | -47.9329 | 2025-09-13 14:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 8c030428-ff4e-326a-9362-a76f6dd436e3 | -8.9371 | -46.1094 | 2025-09-13 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 17b8a367-32fc-3a41-8a4d-2d9f4dda73f9 | -14.3313 | -45.0659 | 2025-09-13 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 8634602c-68b1-3509-893c-55f34a8b65a2 | -12.8456 | -47.9236 | 2025-09-13 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 4ecd29a4-2300-3fac-937e-66e65975d484 | -8.9982 | -45.7645 | 2025-09-13 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a7f66de4-4053-3791-be96-896ed923832b | -9.5006 | -55.9588 | 2025-09-13 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 330.4 |
| 4d03e83b-ad0c-342b-b4b4-ea7ed7b782f4 | -10.7104 | -50.4718 | 2025-09-13 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 07854daf-d3f0-38f5-b8fb-4ab78a263eb8 | -16.5099 | -55.1459 | 2025-09-13 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 235ddf18-9ae3-3db6-875e-9f90f54beedf | -9.673 | -47.5459 | 2025-09-13 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 761e491c-e68d-38e4-8610-06ecf03552f4 | -8.497 | -45.1369 | 2025-09-13 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 143.0 |
| ccd308d3-019d-3220-b9dc-cefb043dd213 | -8.9516 | -45.019 | 2025-09-13 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| b4bda19a-1bf8-3b50-b6b3-6ad626761512 | -10.8785 | -45.5597 | 2025-09-13 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.8 |
| e7eed9aa-8dda-3dc1-8f41-67a9697f17f4 | -14.4584 | -47.34 | 2025-09-13 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 88311813-84a2-37a9-b666-cca8950781ba | -14.1703 | -46.2505 | 2025-09-13 14:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 34c6625d-67ee-397f-b57e-eb461fce1802 | -11.8278 | -50.5835 | 2025-09-13 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 25759005-e43e-3cff-b558-20893f856c47 | -9.5004 | -55.9788 | 2025-09-13 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 247.8 |
| 190ffeb0-e813-3f1b-acda-cc2196caa02b | -15.0432 | -50.1556 | 2025-09-13 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 3354ba08-4da8-3607-b33c-bbadfb1ad415 | -9.976 | -50.3334 | 2025-09-13 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 58d8b358-046b-3322-a41f-0de2183dfc8f | -12.8649 | -62.1268 | 2025-09-13 14:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 0a61c705-2024-32be-886e-8e8b3121bde2 | -13.9172 | -48.2775 | 2025-09-13 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 323af027-54f6-3203-af9a-8048d5b3f2a1 | -11.1237 | -50.7049 | 2025-09-13 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 05101dcc-1499-36d6-a4e8-d80f544832e1 | -12.1044 | -47.5816 | 2025-09-13 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| b7b5b249-fa30-323f-9c0e-e25b6d46e97d | -14.29 | -46.0924 | 2025-09-13 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 3807b646-f84e-3759-81d3-5e2c107f1e4f | -11.0953 | -51.3866 | 2025-09-13 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 868bacd8-41de-3ed1-aa8b-112875599e11 | -11.3117 | -50.8122 | 2025-09-13 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 915164ba-e9f8-329a-9e33-f57dda15f2bd | -11.8659 | -50.5791 | 2025-09-13 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 0e7551eb-9b00-3192-a6ab-1102c99290a2 | -10.463 | -50.604 | 2025-09-13 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f7fec9a0-e601-3f43-9b2e-f0574b16a68a | -11.8698 | -46.7627 | 2025-09-13 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| d0290609-fb07-3a85-919f-049ec7d246b9 | -10.3397 | -49.9333 | 2025-09-13 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 70fa4806-8b66-3a1f-a7e6-64f7f5929da0 | -12.8263 | -47.9263 | 2025-09-13 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 3aa33f55-be08-3577-a0a2-47ed77a3f0b1 | -16.5666 | -49.2247 | 2025-09-13 14:10:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 4355405f-ea39-37c7-aef9-c11a4bacb8fb | -12.8647 | -62.1461 | 2025-09-13 14:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 153.4 |
| 59c1945a-8dde-3fbb-bab1-c4e8d62c320b | -11.4696 | -50.389 | 2025-09-13 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d0792346-bbed-381a-b1d1-2e0151d1430f | -12.8644 | -47.9432 | 2025-09-13 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| fc1972ea-ee55-39f1-9807-8f2b2b76fe87 | -14.4394 | -47.3206 | 2025-09-13 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 113.0 |
| a45f8566-f4f8-31e1-8eb6-20b696263990 | -11.1896 | -51.419 | 2025-09-13 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 9d0bd7e0-cf16-3cde-b30e-ab10461b2b9b | -12.8837 | -62.1449 | 2025-09-13 14:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d270f24e-a2f7-3100-aea4-d9bc384a8488 | -10.5484 | -47.2242 | 2025-09-13 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 921e6297-ae5f-35ae-8b03-954649f77b2a | -14.4588 | -47.3174 | 2025-09-13 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 745e3156-8384-33c6-b078-c6fab4768d62 | -13.9366 | -48.2745 | 2025-09-13 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 03b771c7-f186-3f2a-b818-10c726b6fb95 | -16.3422 | -51.5217 | 2025-09-13 14:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 115.9 |
| d93b0007-ae35-38a8-9e07-03258bef86c3 | -11.3835 | -47.3206 | 2025-09-13 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| b6dfced6-94f8-3519-9409-14d4913d125a | -15.4517 | -47.3291 | 2025-09-13 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d5eeff0f-90e3-36cb-bc75-838ec1f3be30 | -14.4939 | -53.8973 | 2025-09-13 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 21f64d17-5da9-3027-a820-409d0ddd0a3f | -16.5102 | -55.125 | 2025-09-13 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 259bc995-52ce-3fc1-9a88-d127174a4424 | -16.4906 | -55.1276 | 2025-09-13 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 122.3 |
| ec73fcd5-6085-3f92-83b1-c7d92f06ec7c | -9.0897 | -50.5226 | 2025-09-13 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| afb6ea71-c745-3fd1-8b6c-6a479cd0947a | -9.1145 | -46.9629 | 2025-09-13 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| fd8755d7-3ed8-36bf-8991-60c6373ed5e7 | -13.9877 | -44.7767 | 2025-09-13 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 355128fb-a354-3206-aa79-564ffe7f793d | -10.7101 | -50.4932 | 2025-09-13 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 57560b62-a7ba-3971-8247-17e72d86628c | -9.2656 | -59.4191 | 2025-09-13 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 00ba651f-d354-399b-b57d-688ec1177f28 | -11.2882 | -51.1334 | 2025-09-13 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 13ea5f84-6c80-39eb-b54a-e61d7ea7eab3 | -8.956 | -46.1074 | 2025-09-13 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 340.5 |
| 020e83d1-a97e-3bf7-80ef-b2791958e929 | -10.7952 | -46.003 | 2025-09-13 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 02b9bbfa-bbc1-3325-96a6-b27237fac913 | -16.5666 | -49.2247 | 2025-09-13 14:20:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 137.4 |
| fea4fc4f-f8f4-35a9-abbb-f14f463feab4 | -16.5099 | -55.1459 | 2025-09-13 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 393f6b30-6e1d-34a5-9d65-72fcfc9dadcf | -13.4708 | -51.7712 | 2025-09-13 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 07ad5222-0514-3986-9600-c7ef4a985bd6 | -15.4517 | -47.3291 | 2025-09-13 14:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 10407fb7-8121-391c-b77a-3ed0ebcbbbd1 | -15.4713 | -47.3256 | 2025-09-13 14:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 673a411f-0ff7-307d-afd4-4a94a78e855e | -13.9577 | -48.1823 | 2025-09-13 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| f0291972-774c-366f-b10a-32bcfc1d36b1 | -14.3095 | -46.089 | 2025-09-13 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 151.3 |
| bec51b9c-6ee8-37c4-a403-f8e51b3355f1 | -14.4394 | -47.3206 | 2025-09-13 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 96aaffac-b0b6-3384-9cbc-95740ff58613 | -14.2905 | -46.0693 | 2025-09-13 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 6583977c-d1c2-3342-917f-e026962bafd3 | -11.1234 | -50.7262 | 2025-09-13 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| d5e4a730-4922-3bfa-82f1-1a4a8c0fa78c | -12.1236 | -47.579 | 2025-09-13 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| d422ac7b-3fc1-3511-bb48-a1f13bcbbf3f | -12.134 | -44.8275 | 2025-09-13 14:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| e80c21b6-d1c6-35fb-b087-cd81223ad00c | -9.0166 | -45.8077 | 2025-09-13 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| db45dad4-71c6-3367-b98f-9365e5c1afba | -12.0873 | -51.0443 | 2025-09-13 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 36ce681f-33c0-3033-b49e-c3af862cd801 | -8.9368 | -46.132 | 2025-09-13 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 66f50063-dca4-3540-83f9-1ec7b6578b4a | -12.9398 | -48.0213 | 2025-09-13 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 4897f311-0027-39a1-b38a-7521f051ead9 | -13.9375 | -48.2299 | 2025-09-13 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 8beb883a-a36e-36bf-abfb-f9384f509a47 | -12.8837 | -62.1449 | 2025-09-13 14:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| dcd68e68-d1a7-397f-a9b7-54040e247198 | -9.7108 | -47.5418 | 2025-09-13 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 9fd3a826-301d-3d9d-991a-0ed824b770a6 | -15.1605 | -50.116 | 2025-09-13 14:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 5346b18e-0c12-3843-bb91-14a8eac68a20 | -8.9176 | -46.1565 | 2025-09-13 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 13c4797a-c43d-3235-a60a-0a37bc9752bf | -14.7527 | -60.2321 | 2025-09-13 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 446e5c9e-67c4-3822-a98b-1dca0b653bb1 | -12.0314 | -50.9656 | 2025-09-13 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| cb230792-7e02-3397-97b6-b71769bc72f7 | -9.2843 | -59.418 | 2025-09-13 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9712e14b-df58-3b4a-b1d1-3096884bb5ec | -12.9402 | -47.9991 | 2025-09-13 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 575852b1-9efa-3931-b05d-9df1309073c9 | -14.4199 | -47.3238 | 2025-09-13 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 6847c644-0563-3f67-809e-1bb2218f37b1 | -9.2844 | -59.3986 | 2025-09-13 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| c016f6f8-3a5b-3fb7-960a-0eba14d59bf9 | -14.4584 | -47.34 | 2025-09-13 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 1d14bcbd-17ea-326f-a897-82f31529cf81 | -9.2656 | -59.4191 | 2025-09-13 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 0dfeb2a2-a352-3dce-8120-33dff873a27b | -12.8647 | -62.1461 | 2025-09-13 14:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 133.9 |
| cdda971a-029a-3461-9df6-6c937421752b | -9.7602 | -45.3819 | 2025-09-13 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 18bd78cd-4eab-3a41-9e4c-5212f033f508 | -13.9181 | -48.2329 | 2025-09-13 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 41743206-1e94-3cdc-9ea4-dea1967fd09d | -9.5004 | -55.9788 | 2025-09-13 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 299.9 |
| 8c620e8e-a9d8-3148-96db-a98f9d88548c | -18.0667 | -45.4134 | 2025-09-13 14:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 0fea20af-8325-330e-a4d1-27cea14e5d9e | -9.2503 | -51.2472 | 2025-09-13 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 3d10f954-6392-3df7-b4cd-43c5d6feb280 | -9.5006 | -55.9588 | 2025-09-13 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 404.2 |
| 84455b0b-7d3e-35f5-a568-a1dd4f091d0e | -16.5682 | -55.1592 | 2025-09-13 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| d657ec55-be66-3731-8aba-99e31a854831 | -12.9595 | -47.9963 | 2025-09-13 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| aa2bf154-cca0-3414-9087-64b9d86cb197 | -10.463 | -50.604 | 2025-09-13 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b6471192-bc7e-3f50-b191-1c16ff00f641 | -12.8259 | -47.9486 | 2025-09-13 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 8d08e2d0-21a5-3137-bf24-422dd68d78da | -14.394 | -52.9245 | 2025-09-13 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 0c8ce900-7fc9-37f3-b036-bb77481296a6 | -13.9168 | -48.2998 | 2025-09-13 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |


[Clique aqui para ver as próximas entradas](README133.md)
