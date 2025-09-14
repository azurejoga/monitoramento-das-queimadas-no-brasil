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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce7da004-af47-3c8c-82e7-5011c21d2723 | -8.9173 | -46.179 | 2025-09-14 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 6b4c63fb-be57-3b68-b47c-6d2ce0b4473d | -13.9473 | -44.8541 | 2025-09-14 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 5466da43-d2f0-37eb-b96e-67f722a8f8a4 | -10.3693 | -50.5497 | 2025-09-14 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 2a1279ac-8cf2-39b7-bab6-0c28c8192842 | -10.7288 | -50.5126 | 2025-09-14 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a8403cab-b2c0-3a51-b408-7fd2690def93 | -11.2695 | -51.1142 | 2025-09-14 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 0841a2fb-409f-316f-80f1-6ac5314ef3fc | -10.7496 | -46.4832 | 2025-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 16ced81e-d2d3-3918-bb59-74694d5db811 | -11.293 | -50.793 | 2025-09-14 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c5aa9630-bc38-3495-a4c6-03ff832ceea5 | -14.2102 | -46.1979 | 2025-09-14 14:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 22fce078-bf87-39f1-b5f6-52cd3ed4308c | -10.768 | -46.5259 | 2025-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| c98e881c-84da-3089-b212-c529d1025d38 | -15.0971 | -52.4944 | 2025-09-14 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 8520356c-e52e-3c70-92d1-e886ad722967 | -10.7477 | -50.5106 | 2025-09-14 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| fbadc7e7-e0d5-3e11-a1e1-66b5dc1cfe6b | -12.7827 | -47.1502 | 2025-09-14 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| cf3c362f-f571-32e5-b273-e0da1cdf8b6c | -11.5263 | -50.404 | 2025-09-14 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| de87b41d-5bd0-3fe8-9771-45db1cd80e8f | -13.9468 | -44.8776 | 2025-09-14 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 97d97fc8-2a60-310e-ba4b-863bf76b363e | -10.4331 | -50.0093 | 2025-09-14 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a967ef74-0b43-3932-b4d0-ccd14e0fa067 | -6.5539 | -43.9915 | 2025-09-14 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d2cca0bd-ed3d-3f46-992c-54c0458aa424 | -14.2107 | -46.1749 | 2025-09-14 14:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 271.6 |
| ff96db7a-fb04-34fd-8c56-d84326eec0ab | -8.7871 | -46.0353 | 2025-09-14 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 0e951459-6e65-3703-93cf-ff2905279c4f | -14.2917 | -45.0964 | 2025-09-14 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 215b139c-a8da-3aac-918d-364956f46c07 | -10.7579 | -44.7721 | 2025-09-14 14:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 158e832a-9fa0-37f3-89b9-7110c47c2fbe | -16.0056 | -47.9555 | 2025-09-14 14:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f6dee4ba-900c-301c-afb7-3c97724faf9c | -11.0388 | -51.3713 | 2025-09-14 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 0115dfaf-229c-38fa-86e1-56bf6e658fcb | -15.7333 | -56.2122 | 2025-09-14 14:10:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 49a1637b-8439-3174-866c-1540d46b6b5a | -12.8212 | -47.1445 | 2025-09-14 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 37b9d6c6-9b08-394e-954a-1dc6bdb80652 | -8.9746 | -46.1279 | 2025-09-14 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 162.1 |
| d5b27007-e872-35f4-8e40-8949b652307b | -8.6404 | -45.7122 | 2025-09-14 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| b74162a3-87d8-339c-9c42-427fda2d83ee | -14.1912 | -46.1782 | 2025-09-14 14:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a1a57c3d-3f44-3992-9d8a-f22e3aa2b2da | -15.6906 | -49.9018 | 2025-09-14 14:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 4290d561-3803-3156-a98e-c4b0ffeb986c | -11.3259 | -51.1505 | 2025-09-14 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5cc7a7ca-0931-3600-94ba-656f43aecd81 | -8.9595 | -44.4436 | 2025-09-14 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 8fceb86d-1543-3e31-9701-b4d4ec2d3756 | -6.5541 | -43.9684 | 2025-09-14 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| d39e9f80-ee35-3679-a059-e6a6f2190a8d | -10.5459 | -51.4844 | 2025-09-14 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 4b4d2a87-8797-3394-a87c-11b6b89654f0 | -11.2933 | -50.7716 | 2025-09-14 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 8fea4310-6318-3f0a-8862-9da19d1e95fc | -8.4143 | -47.2545 | 2025-09-14 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| b49bb19f-f8c4-34f2-9315-d4e55f9aaf89 | -13.5879 | -51.6502 | 2025-09-14 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 5be59048-b0cb-3770-81e0-eb403f05e164 | -7.8995 | -46.2805 | 2025-09-14 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 7d02e399-d644-336c-8b9b-4c3d32fc3595 | -11.353 | -43.495 | 2025-09-14 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 7c7401b6-bafc-3f5e-b8a7-70cee085a521 | -8.9176 | -46.1565 | 2025-09-14 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 24c6f0d8-a48e-3cba-8999-49e5a3182a50 | -12.0856 | -47.5618 | 2025-09-14 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 8742e55b-bc14-3688-bf64-5cccc4a141b2 | -10.9096 | -47.2023 | 2025-09-14 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 612380a6-e7dd-38fb-97cc-4cc6203000e5 | -8.9979 | -45.7871 | 2025-09-14 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 9ef92258-2a3a-364c-ba34-9fad87f62d31 | -12.8208 | -47.1671 | 2025-09-14 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 5e7f6e27-8b78-3e67-8e35-d83b786d03e3 | -10.5586 | -51.9661 | 2025-09-14 14:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 2aebea43-d9af-3020-822b-f3febe56fb2f | -15.1995 | -50.1101 | 2025-09-14 14:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| d0229cf6-be8c-3a27-8b4e-135f0dcb3d35 | -11.0571 | -51.4117 | 2025-09-14 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 048ad9e8-d458-3412-97e3-594dc1f5d622 | -8.956 | -46.1074 | 2025-09-14 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 227.7 |
| 607f8131-0443-35a0-9168-a0a36f705da5 | -11.2698 | -51.093 | 2025-09-14 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 52069b72-f5ce-308d-9cc2-2e008baf0877 | -11.2885 | -51.1122 | 2025-09-14 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 969cb139-c975-3e14-8aea-58bd91cf6bb3 | -11.2927 | -50.8143 | 2025-09-14 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4e4a2786-89cb-378c-a80c-694f714e7a11 | -11.5076 | -50.3847 | 2025-09-14 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 24213abd-b6be-3b7d-9c2a-f18b67f4063b | -10.1319 | -47.1843 | 2025-09-14 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 521766ff-4ee9-39f3-8642-cd97cb28bf9b | -10.929 | -47.1776 | 2025-09-14 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 3cc3db31-fbe0-32da-b932-ee6d9c98e399 | -10.3701 | -50.4857 | 2025-09-14 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 3598db56-9665-341c-ad5b-8ec50b9ee1eb | -10.3696 | -50.5283 | 2025-09-14 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d9241fa4-e0bc-357e-8281-9c5e19b915fc | -10.7664 | -50.5299 | 2025-09-14 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b2c67f95-fa81-37a8-8d32-adf920ef6a68 | -8.4334 | -47.2306 | 2025-09-14 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 9b26d61a-96dd-300a-9b3c-0e330ae09e8c | -13.9283 | -44.8341 | 2025-09-14 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| ec5a6e7b-01f7-3442-a677-962f887cf4bc | -10.7285 | -50.5339 | 2025-09-14 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 001c2309-f0bc-3c70-adf9-0de322b4d158 | -9.8646 | -50.1951 | 2025-09-14 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| cbf33e66-69f3-3fcf-b786-599574ade2dd | -9.019 | -47.0616 | 2025-09-14 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 224.8 |
| 0c2aba44-4c91-3124-9802-2e147111ea50 | -11.0391 | -51.3502 | 2025-09-14 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 08d7382e-ef7e-333f-9a5e-7d93329d8d21 | -16.0061 | -47.9329 | 2025-09-14 14:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 697ccbf5-9b9a-3a6f-b39c-5937fc4d399c | -11.3123 | -50.7696 | 2025-09-14 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 4cb89fe3-7e06-36ea-bd40-f5029ffe5fe6 | -12.1044 | -47.5816 | 2025-09-14 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 64a9ae52-6fd0-3cab-ba45-e672086b5015 | -15.7591 | -53.4846 | 2025-09-14 14:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| dfc38a0d-4005-3b09-9602-01310bf080bd | -6.4366 | -42.6229 | 2025-09-14 14:10:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| cc3108be-cd70-3ea4-a93e-a6c29654c559 | -15.0477 | -47.9856 | 2025-09-14 14:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 36b4318b-5553-3667-8ebc-971306aa2f2b | -8.9359 | -46.1995 | 2025-09-14 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 9231e005-83aa-3f8b-9709-d8f24121bd3d | -13.9478 | -44.8306 | 2025-09-14 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 29b3e909-b4a7-36d5-8173-9c0a467a111d | -10.75 | -46.4607 | 2025-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 241.3 |
| 443727c4-41d3-371e-a445-1eea9714d954 | -13.5096 | -51.7451 | 2025-09-14 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 164.1 |
| e8e5298f-8aa5-3475-8211-2bc789c28f7e | -14.2912 | -45.1198 | 2025-09-14 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fd1628f3-f6df-3bbd-9a22-16a0bcffc2d9 | -10.8991 | -45.4656 | 2025-09-14 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 448.7 |
| b887d3b6-f7f8-38f9-8d13-dab4a734a2d2 | -8.9976 | -45.8098 | 2025-09-14 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.1 |
| ea17cf87-2b11-3dac-96a4-81f465d39084 | -14.4137 | -52.901 | 2025-09-14 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| aa63d168-9b70-3dfd-b435-563c23b0ce19 | -10.8803 | -45.4452 | 2025-09-14 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 85f88184-40e3-3df4-a022-3a474fae4ac3 | -10.9286 | -47.2 | 2025-09-14 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| d2cb7f31-bf09-3430-8ccf-1cdf632a10d7 | -12.1048 | -47.5592 | 2025-09-14 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 497679b6-ddbf-35ce-b897-cf11f8e6d182 | -12.7675 | -48.0013 | 2025-09-14 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 8cc0a193-82c2-3567-bd82-d231cb03408f | -10.8994 | -45.4426 | 2025-09-14 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| b084b25f-f1d3-3c4a-b9f6-bb41161bc98b | -8.979 | -45.7892 | 2025-09-14 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 4c39dce0-3e05-3149-b807-dfc62b61a5c8 | -8.1386 | -43.653 | 2025-09-14 14:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| f52f83fa-952d-36c2-9806-305455727faa | -12.1427 | -47.5763 | 2025-09-14 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2be04d74-ed0d-3232-ac77-dfe303fb5274 | -15.7786 | -53.482 | 2025-09-14 14:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 6dfefbce-4f85-3c25-af3f-82f46f7f7df5 | -10.9452 | -47.3538 | 2025-09-14 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| b81a36e9-d368-3159-8f67-f1a4e52a4c9d | -12.7671 | -48.0236 | 2025-09-14 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 1506a96a-47b5-3374-9511-b25c301cc359 | -8.9362 | -46.177 | 2025-09-14 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 1e9dc1c1-c3c2-340b-ad79-fec59d9f0935 | -14.3747 | -52.927 | 2025-09-14 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 154.6 |
| c884c1ac-6b0a-319b-83e9-9ce732c5d3df | -10.5451 | -51.5476 | 2025-09-14 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 53ad7cec-4aac-3b8a-bd45-fc805735e610 | -8.8984 | -46.181 | 2025-09-14 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 5c437aee-e4c5-33f0-b204-bfe8680d8420 | -15.7591 | -53.4846 | 2025-09-14 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 127de05d-1a56-33e9-9d4c-853dd466df5e | -7.8995 | -46.2805 | 2025-09-14 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9ceaadb8-3167-370e-ad9e-cd9122b934cc | -10.7288 | -50.5126 | 2025-09-14 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| ddcc201d-150e-3aac-8ca0-6fe04720ae32 | -16.0056 | -47.9555 | 2025-09-14 14:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1dc5b501-1ecd-3aed-a258-84d634da4f5c | -8.9176 | -46.1565 | 2025-09-14 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ab1174e2-9ed7-38be-adb3-3d06d751aad4 | -11.3259 | -51.1505 | 2025-09-14 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 977dc3f2-79bd-3ee1-93c8-4b947c16e8b8 | -14.31 | -46.066 | 2025-09-14 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 6c6c7dfc-19f0-37e0-82af-2f3d0eaf7c61 | -11.7132 | -50.618 | 2025-09-14 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| eb602327-b47f-3c40-83d2-16a669b79e1b | -15.7786 | -53.482 | 2025-09-14 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| fed41c05-b2f7-3c55-9ec8-9456c32be06b | -11.3114 | -50.8335 | 2025-09-14 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |


[Clique aqui para ver as próximas entradas](README89.md)
