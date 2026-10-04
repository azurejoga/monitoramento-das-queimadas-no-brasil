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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b86f8be9-55a4-349b-9f13-ab9b9e4874dd | -15.90971 | -56.34485 | 2026-10-04 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04ff255e-73a8-3f1d-8c73-4a3e0418a774 | -13.50293 | -61.13582 | 2026-10-04 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65090d07-dfae-3021-bf65-dcb728bec842 | -9.88224 | -65.14175 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea8d9941-d696-333a-b425-82b00dffe6e2 | -12.55034 | -54.95265 | 2026-10-04 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 648a351c-85cf-3a1f-b872-378e30b8ee4e | -9.9125 | -65.02997 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61d4d926-78c8-362b-8941-402c1fb1e057 | -12.7682 | -62.04035 | 2026-10-04 04:59:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3522c24-eb0e-358c-a03b-031ef5021123 | -17.64622 | -51.38799 | 2026-10-04 04:59:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 040c4c08-8c6e-349c-8a17-51c036196b28 | -12.13339 | -63.17529 | 2026-10-04 04:59:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 659db7d1-5359-3abf-bd3f-5f568bc7a054 | -14.54826 | -49.11404 | 2026-10-04 04:59:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 12563c61-f814-3438-a176-ba4d0c059728 | -9.92548 | -65.03234 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2d42bdb-dc8d-349e-9e60-900d0502ff97 | -12.18601 | -57.1058 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2088a1bb-2545-3390-acff-583cae704c42 | -10.9577 | -60.90966 | 2026-10-04 04:59:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e788303-11bb-30f2-a04e-382ec2034e00 | -14.57607 | -52.88132 | 2026-10-04 04:59:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9de272e3-429b-3539-80cf-77a04fe4beee | -12.13927 | -63.17653 | 2026-10-04 04:59:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32c7c274-4d2f-3b9f-8830-cc4d955c09b4 | -12.20794 | -57.12049 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc693e73-69ba-3976-9f7a-64a2a5c3e24d | -12.18071 | -57.10333 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1099e0c-7be2-3697-867b-56405eb5cf34 | -10.99083 | -59.14949 | 2026-10-04 04:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4798b148-7cc8-361e-8513-1f4b959c6711 | -10.95777 | -60.90755 | 2026-10-04 04:59:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5be5e6a-cb00-3e4d-ab7d-21d3b1de7160 | -9.92349 | -65.0455 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a7aafb4-5f67-312e-9bbd-d798336b159d | -10.26895 | -63.83652 | 2026-10-04 04:59:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 431f7f09-9445-303f-b9dd-99fd57aee6b6 | -13.50349 | -61.13284 | 2026-10-04 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4916dcc-fb3b-3ad7-91e2-87035c5cbd8f | -12.88749 | -61.72461 | 2026-10-04 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2da0303b-1cf9-3b88-8c33-4b7b6676e06f | -9.91379 | -65.02372 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1ccd65b-946f-321d-857d-5850a6a2f8f0 | -12.19393 | -57.10725 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 840276ef-6a74-3127-9577-cd934a4b0b15 | -12.20398 | -57.11974 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d458bf7-c676-3008-970c-34ce4e998852 | -9.9144 | -65.01686 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a93d9b3f-4d8a-3166-9c03-91ed0695fe17 | -12.19657 | -57.10624 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13a70fea-f1ff-3f51-aad8-54f7dfb653b0 | -10.95716 | -60.91082 | 2026-10-04 04:59:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 085966db-c40b-3ad1-ba1f-27d44653848e | -11.05032 | -62.57324 | 2026-10-04 04:59:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc8ffb83-527e-3c14-b5f3-41ccf3e35bac | -10.98891 | -59.13402 | 2026-10-04 04:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a16ff43-5b9a-37ca-9907-2880c12b3a4e | -9.92479 | -65.03918 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43e0fcdf-3da0-37f1-8251-d465c0b051fc | -12.75993 | -62.08287 | 2026-10-04 04:59:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26c118ab-cfde-39fb-aabd-e85671780db8 | -12.19513 | -57.12339 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 880ff671-75f8-354c-8a90-7ab4841744b9 | -12.76063 | -62.07929 | 2026-10-04 04:59:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70f628a3-8114-304a-8761-42d04c030da9 | -10.99173 | -59.14459 | 2026-10-04 04:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d05c0970-090e-3d2b-bd02-8fb334fcc482 | -10.99263 | -59.13969 | 2026-10-04 04:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01c1035c-da38-3702-9218-b2cdfdacb6a7 | -10.27021 | -63.8378 | 2026-10-04 04:59:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aae7d69d-c62e-3c0e-9b7e-90dffdcffc14 | -12.15763 | -60.74829 | 2026-10-04 04:59:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40a8f768-b603-34d1-bd7e-87a5e7e579d9 | -14.54893 | -49.10948 | 2026-10-04 04:59:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1b058569-a7ad-31e2-9d81-3de0eb6c6ea7 | -10.95196 | -60.90982 | 2026-10-04 04:59:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b016430-5968-347b-9171-6279656ccde8 | -12.20184 | -57.12315 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c665782-8b63-37e2-a967-17faa73fc4eb | -12.88815 | -61.72126 | 2026-10-04 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 819f9931-a010-308c-8e82-00b48ffb79df | -12.88287 | -61.72015 | 2026-10-04 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 155c6724-ccde-3579-a97a-20c371992b51 | -12.18468 | -57.10404 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96fb480e-2179-399e-93ab-81af5ea87529 | -12.55387 | -54.95325 | 2026-10-04 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 879a2533-4820-3b1f-8710-be179195cee3 | -12.77292 | -62.04502 | 2026-10-04 04:59:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 910b5615-4e10-3113-b95f-382272c7e85b | -14.56997 | -52.87664 | 2026-10-04 04:59:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc04ece4-e157-3a79-aa0d-a5a1cab9632e | -11.05515 | -62.57928 | 2026-10-04 04:59:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d45e362-6a09-3531-a869-ac99e055eb26 | -12.13425 | -63.17094 | 2026-10-04 04:59:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 419fa11e-f141-3a8f-baf8-9d193478e182 | -13.50245 | -61.13046 | 2026-10-04 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83f4747d-f2b6-39d8-b405-9c6c3d3172f8 | -12.18865 | -57.10476 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8dd2d5c-5556-33f0-9046-92d33092fe70 | -10.9525 | -60.9087 | 2026-10-04 04:59:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca786b1a-f5ea-3749-84d0-97a274c3d56e | -9.89275 | -65.01873 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d37770f8-7027-3505-8be4-57c07e4a1fe5 | -12.18993 | -57.12099 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 520db80a-ec51-3aac-8af6-2e6e14a12f05 | -12.10248 | -57.17487 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c29c0d5-0f10-3b66-ba47-3a761b695a82 | -12.77223 | -62.04855 | 2026-10-04 04:59:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2415782-369d-3a95-a858-789227065b89 | -9.88351 | -65.13544 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 44a07d6d-8ac4-3a24-a38f-7d481864a9b6 | -10.99544 | -59.15039 | 2026-10-04 04:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d37eb4b4-bfa1-3cc5-84a9-d5c7c5fa1b0a | -13.50186 | -61.13344 | 2026-10-04 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53967438-3e6c-3fee-b0de-a2332a2dfaf2 | -14.57331 | -52.87719 | 2026-10-04 04:59:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fedea19d-60a8-390a-a190-e473a99c9d4a | -12.10342 | -57.16959 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a919c46-14b9-30be-818b-ab593cafb99b | -10.99635 | -59.14547 | 2026-10-04 04:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 217f5601-39f1-35a2-8a5e-e9a9f6297841 | -12.19876 | -57.11727 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dd90b55-1f50-3c7f-93c2-511caecd2b47 | -9.91189 | -65.02938 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e04b21f-6326-39e6-8387-1029a9fb82eb | -9.92423 | -65.03864 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89d94914-25bc-34e4-9d40-3b63d930d2a1 | -10.27124 | -63.8327 | 2026-10-04 04:59:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 017fbca9-b640-30c6-853e-5fc2417f14da | -9.9167 | -65.04398 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f6cc6d37-46b1-3e3e-816b-96a4f496aaa9 | -10.99352 | -59.13492 | 2026-10-04 04:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b7b08ed-9472-3bd7-a928-a91f96eeb17e | -12.13618 | -63.17743 | 2026-10-04 04:59:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 247cb80d-e0c0-3e34-a6eb-b251b66792d0 | -12.19485 | -57.10212 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f456fe0f-d719-324f-9a79-0ccd97c143d9 | -14.5755 | -52.8849 | 2026-10-04 04:59:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31124707-0463-38ae-9465-5c193f94aa5c | -12.15874 | -60.7424 | 2026-10-04 04:59:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02a9e593-eb41-3acd-bf32-0cea6bc8d256 | -12.19115 | -57.12269 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7794c567-eed7-35e2-be1d-a31e28468fc7 | -12.20001 | -57.11899 | 2026-10-04 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e393cf8-4033-367d-994e-fa3bffa8fcdd | -12.88353 | -61.7168 | 2026-10-04 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d4770c8-bc79-3204-8f5b-9c3e51d863dc | -14.55265 | -49.11005 | 2026-10-04 04:59:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93981ebb-b731-3fce-b348-588dc6d4fad8 | -9.91869 | -65.03083 | 2026-10-04 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c80f42b-b4ca-3da7-b2b5-298da9583082 | -20.22814 | -57.99483 | 2026-10-04 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f14c409a-c3b3-3ff1-a58f-ddad205d2090 | -20.231 | -58.00022 | 2026-10-04 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d397407a-6bd1-32ff-86f8-dee5f5c0e9ec | -21.56404 | -56.73652 | 2026-10-04 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f16d2f3-7223-3a0f-aab1-bb96fc50589b | -21.91167 | -56.92674 | 2026-10-04 05:01:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc667bd4-0b24-3855-9285-1408b7ac23ea | 2.35053 | -50.75189 | 2026-10-04 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 242b5013-2907-3d6e-b709-04490f3ac65f | 3.42618 | -51.30309 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3f4b982-d7b7-395c-a13e-d864d9cb7959 | 1.90719 | -55.79534 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a677a0c-ef6f-3819-84e9-2d90ca5ea060 | 3.42151 | -51.29677 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c46263ab-f0b8-32de-a954-3b38674dfed4 | 3.42164 | -51.2991 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c1209df-192d-3f07-9e2d-9ef151b48cf5 | 2.34656 | -50.75254 | 2026-10-04 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3734700-f9f3-3457-bd7c-65dbb4ed5704 | 3.42603 | -51.30078 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df7a33bf-b96c-3d50-babb-7f69d5ce4a82 | 3.64494 | -60.76499 | 2026-10-04 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37ee8e93-b4a5-3ecb-ae97-ab503fbcb371 | 3.42225 | -51.30138 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 313d15fb-ec80-3feb-ab20-c2a737dd2a55 | 3.42298 | -51.30599 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be32a0a0-d279-3ec1-a0c3-2fd9e6c592a0 | 2.34258 | -50.75316 | 2026-10-04 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebfcada5-3326-3fbd-9378-c16203b2b8b7 | 1.80873 | -55.56166 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41993f48-30dc-303a-b88d-beec4094994a | 1.91276 | -55.7664 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 257711dd-5329-313f-af05-e6c700713bc1 | 2.34312 | -50.75658 | 2026-10-04 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53dc5d5f-aa0c-39aa-ada6-0b8305097c22 | 2.35957 | -50.75746 | 2026-10-04 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 132a0bc9-ced7-35f1-9168-8f8d9523d43c | 1.89783 | -55.80032 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b21ac77-3c45-37df-8cdd-c9e30602d481 | 1.90389 | -55.79586 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8e7fafb-ef87-3dcf-a036-e34155752a44 | 3.7131 | -51.39732 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 573af4cf-d02f-31b3-981b-70091ae3a19b | 1.91606 | -55.76588 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README50.md)
