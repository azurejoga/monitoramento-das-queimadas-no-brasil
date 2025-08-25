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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b591b2d-d1ee-34df-b602-9df6156b0284 | -12.29609 | -49.14191 | 2025-08-25 04:42:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87810977-efa7-3139-af97-0b80dadb8cfa | -8.54193 | -48.8549 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48304df2-30ef-304d-ac9f-2da4760ea1d2 | -12.74817 | -48.11355 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e2e0847-728c-39f1-a006-5f2f91866a38 | -9.15331 | -59.47455 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 058fcf18-de6d-329b-87ef-54af5cc7b969 | -9.199 | -59.47603 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0bdef48-3924-3046-a4b9-ab03d8ceb8ab | -13.3825 | -51.78965 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c04e3c13-e2c6-36ba-aa7b-c701a82b9843 | -12.94045 | -46.30811 | 2025-08-25 04:42:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0797a63a-abf1-3da2-95ae-057ad78c6f14 | -6.78249 | -58.62672 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f366d389-dc6a-34e5-bd9f-4008730b7cd2 | -9.25235 | -59.64484 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 907a54d4-3894-3799-b2bf-4d667eec4888 | -9.19967 | -59.47253 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d24f61ba-9868-3657-9a2c-2612db3f5961 | -9.20157 | -59.61243 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79f9f7f6-e22d-3b44-9017-41f931b179d1 | -9.8162 | -64.26487 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37916001-c163-3ea1-8840-7b726c6a32d0 | -9.19081 | -59.45988 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11db9022-4025-3511-8b38-ad9b659a2853 | -13.67185 | -47.96991 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfabf8bf-7339-394f-a75a-fb01ba784507 | -8.5851 | -62.6274 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e88ff7f-1d24-32cb-8555-6b85fdf2e169 | -11.14474 | -44.79162 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c652bed-94b4-3376-9b00-dcdeff7ec4cb | -10.41425 | -47.16211 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35a0a400-9b6b-320a-98c6-b6ed8a5a8895 | -8.11236 | -62.87537 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ab6b442-adfc-3b33-baeb-b9a069d01f02 | -8.90386 | -47.33156 | 2025-08-25 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f65b0cc6-1ccd-30d3-9a84-834fb281bdb3 | -8.49583 | -63.87185 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89d62887-bb7a-322c-a4ab-3e3f27ef6a99 | -13.62982 | -48.15814 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5af1b55c-28cc-3ff0-81ee-1f7b01e881e4 | -13.44226 | -46.88757 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffe3de56-a34b-3ccc-8ac0-25449c8e0887 | -11.70068 | -60.17794 | 2025-08-25 04:42:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 009b22f1-9106-3639-bf2a-a293fb15e6e1 | -10.23832 | -59.66558 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6a1710d-91ca-3454-a394-2ec3974c7d79 | -8.87184 | -62.45762 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 4d0b0ba3-9aab-334b-889c-b8a22bf77b8d | -12.73356 | -48.13935 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d678071-7421-3ac8-8d66-4a349b3b2781 | -9.1705 | -60.8282 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 682cbd29-e112-3aab-b199-749e4f3db3a5 | -9.20446 | -59.50276 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32227e9a-00c2-3d16-96df-0b65d9d8482a | -8.21386 | -61.39413 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 509a9563-1a75-3ddd-a620-3ac1511bb61b | -11.33728 | -47.85411 | 2025-08-25 04:42:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5179f417-0e81-385b-ba5c-42497e731155 | -7.65654 | -63.52542 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e85e9391-ae10-32f2-9c5f-347a78d1a60f | -8.29199 | -47.23628 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 872cb1ef-7ad6-3374-9edd-0c744305d81d | -12.75582 | -48.11072 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 596df8ad-ae86-366a-9618-0a9e87a618e3 | -9.15462 | -59.46749 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d57b604d-9375-34a1-8687-bb779e9d73b2 | -9.57216 | -55.36707 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c97fff5-88cb-32c8-904c-ac0931b526c0 | -9.21763 | -59.70947 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58968134-9ac1-395b-a03d-820fa09081d6 | -9.15287 | -59.50746 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdece79f-69da-3d33-ac83-ecb5ec306472 | -13.48584 | -47.01765 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3fe9db9-c48e-3271-a84f-50b049a981cb | -9.19557 | -59.46448 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d2cca8e-77cd-3e26-be3c-754ba3dd3b77 | -8.91055 | -62.42312 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6eb0dc64-521d-3c68-82b0-3621e1be98ac | -13.49228 | -46.89017 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abd1355f-7402-37a7-93f7-330f391999bc | -8.12041 | -62.87044 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b250ae2c-02b6-3d17-9dc1-013cde3adf7b | -6.8288 | -58.94708 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef0d435f-c284-30cd-b9ba-e97b7d3a7d37 | -6.35463 | -57.96819 | 2025-08-25 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ac4cd7-daa2-3f85-b011-4741113866a5 | -9.1524 | -59.44907 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3179c0b-788b-33fe-876e-e6d98f8578b2 | -8.65666 | -63.43493 | 2025-08-25 04:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a19d09ef-8658-34d1-b3d4-e2ae88c24fc5 | -9.20522 | -59.50276 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c6e4a84-e2cd-3bae-907f-f050ece717df | -9.17959 | -59.60881 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd40d9c7-66fe-3b5e-851f-1f4fdcf37420 | -7.79906 | -50.98589 | 2025-08-25 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77d7c2ac-d886-39d2-858a-9cf832bbffe1 | -9.15702 | -62.35831 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74108689-3182-3d98-be3d-1af57c8f584f | -8.28438 | -47.23905 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08b11453-db4f-3b83-9a1a-d1d7b7792bb3 | -12.75297 | -48.13014 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5649dc28-b045-3c27-83f9-407851aaf29f | -9.30865 | -63.43852 | 2025-08-25 04:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40383c4f-9c34-3ab4-a862-e2b52d8c6616 | -10.83441 | -46.41074 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d0cdd5e-33d2-30be-a837-aeeb8eafad09 | -10.24897 | -59.1083 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33accc8d-3e52-3cd3-8a88-e5114c952964 | -8.60514 | -62.59486 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ff011a2-22cc-35e8-b713-0c72f7ebb625 | -10.62453 | -51.62097 | 2025-08-25 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5fbf456-6c09-31de-b48f-33273d242e56 | -9.14476 | -60.76892 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 41b95d8e-8aab-32a8-a1b5-9eb71a054ad1 | -8.54303 | -48.84779 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fb2031b-2fc9-3756-9a47-dd4aa2f7bdff | -11.17345 | -55.03102 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 645a2e13-7cc1-3bb2-8844-ad46d3f073be | -9.16458 | -62.35412 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c028b073-e6e1-3b4b-8dc1-a030c41f5269 | -9.16661 | -60.83251 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40644d89-971e-37ca-be60-397e1fb5af97 | -6.82842 | -59.42762 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64fda4df-cf5f-3ba3-8931-8b7e34c633af | -11.17986 | -55.03486 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff228601-13cc-3954-8f88-9882ced2e810 | -6.6277 | -58.55236 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1eb38949-c903-3c12-945c-ef68af5f6124 | -11.18469 | -55.03043 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8587f417-e777-3ee6-a2f3-146256b31de6 | -9.15547 | -59.49339 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06aa1817-5cb6-3d92-872e-37599702d845 | -11.60506 | -46.34539 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fc8095cc-77aa-3931-bbcc-19c9e3cf0945 | -12.75821 | -48.11902 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65f1af90-d0ff-3592-a14d-6ce4abd571c4 | -9.61291 | -55.35125 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d9607b4-876d-34a3-9e78-2662e67fa9a7 | -13.46116 | -47.00166 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cb7d60ca-d359-3c7d-aeae-dd411d15631c | -9.18857 | -59.62115 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb474789-1700-325d-96f5-ec82b4ac4a69 | -13.41101 | -51.78337 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e41f9479-2b67-3180-938d-12b7ee8da76c | -9.15397 | -59.47099 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c98c436-2db4-302d-a18d-8ca464403a51 | -6.63306 | -58.55321 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5abd19f8-2a10-355b-a6f0-ae521115813f | -9.16779 | -60.80973 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf9387a8-dc92-390d-8373-34d143e56b9b | -8.90946 | -62.4287 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ff763c1-6155-3252-b2e2-2be2843ed2d6 | -8.06777 | -49.6601 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f233c0e-82b7-3e43-a336-ad4e9408bce3 | -9.20323 | -59.51334 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7474ef74-6a1f-31d1-8e7e-eac1d18ec1ff | -8.10678 | -62.86781 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89058ec5-38cb-35f9-ad39-d0907a6d07cc | -8.4311 | -48.26038 | 2025-08-25 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 04ee72dd-36a5-3ef8-ba3b-3a5dd7e973d6 | -11.17773 | -55.02404 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35ad6cdf-09d0-3754-abc5-bd79ea06a98d | -6.83789 | -58.95852 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7e6f06c9-dc24-301d-972a-526df9645976 | -12.95983 | -46.33994 | 2025-08-25 04:42:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 992241d4-d129-38eb-b962-051b513459e3 | -9.19839 | -59.50517 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c03a199e-91c8-377e-b930-498dd02ce762 | -9.16537 | -60.82276 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 45cc3a71-42f4-3a7d-a699-433a2addd65d | -8.22256 | -61.41631 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e31d1ee1-a9a0-3fa6-8185-0562bffc09ea | -11.63341 | -46.22777 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 722fab1f-cb37-38df-9d11-24f0bde48699 | -6.92325 | -63.00167 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca2517b4-8212-386f-a277-c16c1052d528 | -7.9057 | -63.06505 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 44ebc11c-c036-392b-93a8-15290b9e7728 | -13.4275 | -46.91376 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7102f1b9-9aea-3e8a-ad17-f7e55e14b71b | -9.52068 | -60.51392 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 313b46f5-9767-39df-82a8-99e3456ca1b7 | -9.61352 | -55.34765 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f17d9f8-0fa2-3bf1-89f9-a258ecc91bd0 | -13.39022 | -51.80573 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e3421bd-131e-347d-854f-76d411888e72 | -8.81262 | -45.46404 | 2025-08-25 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ffd538c-6085-3c40-91e2-eb49f9ecac16 | -10.71153 | -47.13583 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30c246d1-8323-35b8-bc38-1d7a094b4703 | -9.20383 | -59.50628 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9321cba-1dac-3e60-82b9-f9ecaf06f930 | -6.35886 | -57.9704 | 2025-08-25 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1957ede7-86a9-3c24-9bea-8d893d873929 | -6.83367 | -58.95153 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5e5bc71-4bde-39c2-a028-6d8148982e9d | -10.77263 | -47.07411 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README42.md)
