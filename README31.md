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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59d7e1aa-ff4f-3b0e-a5a0-9fbbc4cb3c7e | -13.73228 | -48.07671 | 2025-10-05 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4dc05d6e-4a07-3041-805a-b329b73b725b | -11.87346 | -44.9655 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b54fba1c-93c7-3982-9e03-2c78595c47cd | -14.27193 | -45.86712 | 2025-10-05 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1abde129-e7d3-3c38-a010-3b88cb369af2 | -11.00449 | -46.52303 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1487ada0-0fab-356b-bb92-886594c596b5 | -10.99849 | -46.5142 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1ffdd73a-cc9b-3ce7-933e-e679f7ff0dc4 | -13.32071 | -47.56859 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e55e0b1-ccac-3cbd-9f55-50a865bf01b7 | -11.7548 | -44.73785 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0dd16f80-f78f-3aae-bd6b-561dc3bee8fe | -13.58173 | -48.16019 | 2025-10-05 03:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7afb8b8c-7df5-3d79-9fc0-74207b7ceff3 | -10.19236 | -45.53304 | 2025-10-05 03:34:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e24371c7-59fb-30e9-b0c9-36afee0186e8 | -13.12631 | -43.84453 | 2025-10-05 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| eec3469a-60ed-3ad8-b745-e9ae3fef28c5 | -9.64644 | -45.84924 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 220a3ff3-2e26-3d37-b4bc-69944405daaf | -13.27698 | -47.60166 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b938e2ba-34f3-306c-98bd-e425c06da6ab | -7.71179 | -46.27229 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c81d387c-f1dd-3c39-b904-3fba85bd2d40 | -13.31846 | -47.17786 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5058ac12-ecd6-3bb2-845f-66ab58b42c9b | -9.31991 | -45.6622 | 2025-10-05 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32b5f497-e141-31c8-b29a-f0d93a41e391 | -11.82852 | -45.05944 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42faf533-36d6-38d8-a8ea-80e7249f34dd | -13.29929 | -48.12588 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e6248c8-dc3d-3545-88c7-fd67c9d1cfd1 | -11.88988 | -44.97958 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df455d9b-57cd-3982-9e96-9f4530021984 | -8.56297 | -46.36039 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a71f1a3d-f89d-374b-9ac3-8ce950bc784d | -7.79641 | -46.02093 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8b9f7fa5-05fc-3bb7-8d40-62eb3c1e84b8 | -9.29671 | -45.99929 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cbd42e69-2a27-394c-882b-2b24772d19c6 | -10.94596 | -47.08224 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9b3e6e4c-9d7b-35d5-87cc-fa6a0657f989 | -7.75376 | -42.52465 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1c597411-d0d1-3380-998f-bbe264c852b9 | -8.57128 | -46.37329 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e3816dc-404f-3983-8ead-0c1c4bda30be | -8.54028 | -46.3274 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 68ae2fea-8b29-342f-9bee-3ad8950690e4 | -11.67475 | -43.90228 | 2025-10-05 03:34:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b0b79db4-f1f3-3c11-98ce-07f0e63d2493 | -13.25163 | -47.82066 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63a80a35-3018-3757-925f-7545d1d1c29b | -11.00276 | -46.52799 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 29644b59-fb07-3e2c-b01b-d7ee50e8a234 | -13.15322 | -47.96373 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c1a157e-3889-308a-91dc-dee76f0616b3 | -11.48947 | -45.0299 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62d62fe4-35b2-350c-bf4d-5823edcdbca2 | -13.35506 | -47.20708 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 258a8f66-ffd5-33bc-96bc-5e3548a286d4 | -7.69347 | -42.59309 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d80fbf6e-b905-3301-a526-6433c6feda2c | -8.56191 | -46.27086 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 918797c0-a908-344e-822a-395ff479ee4b | -13.9561 | -43.06947 | 2025-10-05 03:34:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ed7462f7-fdb0-3c0c-9750-bd535b1da8b3 | -10.39824 | -45.40239 | 2025-10-05 03:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| de8c63ba-6385-3076-8f01-ec370bde220f | -13.28689 | -47.8292 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0da2ed4-a115-3876-8051-a79b37f84512 | -10.75124 | -46.61469 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 646033ea-2541-3ef6-8f1d-9c9290ed714f | -11.8311 | -45.05837 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 013923f8-98d1-3353-b5ff-b8c96612bff5 | -13.28937 | -47.18008 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db9e3a34-c124-3ec9-891b-a5893b5f7d93 | -8.57963 | -46.36805 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b48fc1a-b4da-33a6-bc53-3b768ddb77d8 | -11.81637 | -46.86313 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11be35fd-4492-37ae-9aa5-15b6075427f2 | -12.46292 | -45.53013 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fe738580-2500-3b79-86e4-69cb34d0d498 | -11.49751 | -44.98933 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1853668-8d2e-32a7-addb-92dce4e63c8e | -11.83004 | -45.08358 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3304b4fa-0908-30c0-8faa-54286738748c | -10.62405 | -43.31431 | 2025-10-05 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 978c6c16-6619-3e1d-926a-e1f59709d706 | -9.57623 | -46.12661 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5d134660-85cf-3d26-8813-a6d3b29275b9 | -7.61846 | -45.46305 | 2025-10-05 03:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94943322-814d-31e3-a501-2b9726459c54 | -12.4003 | -44.83017 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1274c2e-4841-38b5-9d60-7728fea328db | -13.30559 | -48.09692 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6334cdff-1a56-3ee4-b0d5-ba737aa21fd6 | -9.25887 | -46.78535 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cd7d1a45-6e2e-3f21-bf6b-c86b3b6622d8 | -13.11737 | -44.0751 | 2025-10-05 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71d43917-2c37-3118-a466-6ea9ea09053f | -13.29179 | -47.8187 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f909b9af-84f3-3a29-a86d-a71294e24032 | -10.71815 | -44.17524 | 2025-10-05 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40f75143-642a-36f0-807c-bd5d53765ed1 | -11.83585 | -45.08687 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5e68c389-c5a7-35f2-bad4-83820c1cc3c5 | -12.1033 | -43.45166 | 2025-10-05 03:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e32b3438-b54d-3ac2-afcb-746a62d8b5e8 | -7.15722 | -46.09215 | 2025-10-05 03:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9868229f-a341-3483-94de-41179848bec7 | -12.80954 | -46.85614 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 751fa950-4e77-33da-930e-aed86f1bca7f | -10.87081 | -45.41429 | 2025-10-05 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb114619-cb62-34d0-8a62-519729ebbbe5 | -8.59532 | -46.27203 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 228a84a3-b45d-3c8a-8709-c944721037e3 | -13.35524 | -47.59714 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bfe5692-0192-3961-ad58-5a4c709748bf | -8.54165 | -46.32061 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 24efb9ee-a31b-3109-9fd6-262a45694f99 | -10.19804 | -45.53878 | 2025-10-05 03:34:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57f6375b-1193-3783-9be9-06d8dc39a425 | -11.68495 | -47.48515 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c843bed8-b00a-33f1-9ff8-6b11c6d9a10f | -9.27381 | -46.00695 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 776e5e64-d0a0-317b-90c1-f025e4f109b2 | -7.47724 | -43.03022 | 2025-10-05 03:34:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63edd08f-3f78-34ba-88f1-37e4859ca7d5 | -8.56863 | -46.36874 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13809562-7713-3856-90b9-81d2d0fce64c | -7.69433 | -42.59111 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d144527-e709-3336-8156-c0ead432d72a | -7.75727 | -46.32016 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cdd0d22-24f2-330c-912e-7217831ccf42 | -7.241 | -44.88431 | 2025-10-05 03:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9f44007-1296-3920-86dc-0cbafe366776 | -9.30356 | -45.99961 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e66c9784-000b-3551-a563-5bfc8686074a | -9.95682 | -43.77201 | 2025-10-05 03:34:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d187876-9328-3a2a-bf9a-e011e12db416 | -8.57569 | -46.37019 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 627b3b46-bc02-330b-82ff-119b0cae59a3 | -12.46925 | -45.52331 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6af00b9e-9c62-3fc1-bdba-18513425deb8 | -10.19705 | -45.53392 | 2025-10-05 03:34:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 96b9f624-d0e9-396c-a9e2-971c70ea1986 | -7.75325 | -46.32643 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00ead479-72d0-3227-b09f-a3bd5649a8ae | -13.28262 | -47.17819 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0a12b0a-f77c-3dd6-ab87-855400787398 | -13.02444 | -42.45344 | 2025-10-05 03:34:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 92fef917-db1d-331c-b5f6-9affcb0f5b85 | -12.45751 | -44.63612 | 2025-10-05 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41d79065-4f01-378c-b3cd-1cca5dbd3c08 | -10.99893 | -46.51524 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6aa6bab3-e31c-3d7e-aa47-c030aad83810 | -7.69493 | -42.58485 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fbd45d28-41c3-303c-b0b2-f410cb70cc10 | -7.11643 | -44.17227 | 2025-10-05 03:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15b685e8-ca53-35fd-b48e-97ae5d276079 | -12.46202 | -45.50311 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68f3225d-e14f-357d-a3a2-615e5fef88a2 | -13.44051 | -47.27231 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fa2d4d8-21d1-32f8-9f9a-7d0a00ed4113 | -6.98823 | -44.21552 | 2025-10-05 03:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bea7f085-2926-3171-ade0-6c827319bbe2 | -12.91915 | -47.3108 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8bb0725-b3fd-37fc-a453-50730c7486f9 | -13.30618 | -47.5682 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04cb5a4e-9a4e-3cad-9b20-b7576869ce20 | -11.81549 | -45.05989 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c94bbf9-90e8-3e94-bbfe-01d7422c1416 | -11.88905 | -44.98368 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2f81bba-9f5e-3b23-8fa0-e4a4252dca05 | -8.56554 | -46.36504 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30c76356-1188-379a-99da-b8118c016c5b | -7.52293 | -41.27324 | 2025-10-05 03:34:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 41563707-b7ea-32f7-98a9-8ac608257899 | -11.82904 | -45.08847 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 091d9ad0-9f18-3425-b21f-765c772ed79c | -8.89771 | -46.68877 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 963c6425-d9ef-3171-948c-d6d8f7626f06 | -13.07955 | -47.91383 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4f12b5a7-68a3-36d0-a9e5-8292481cae71 | -9.20642 | -46.92928 | 2025-10-05 03:34:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37bc84f8-8e39-3243-81f5-aa0fde90f7f2 | -12.81644 | -46.85698 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fd849c1f-5c8e-35a9-ae3e-af04b664b988 | -13.35243 | -48.06324 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 052c1b85-2566-3855-962c-0c1b105d6dba | -13.27859 | -47.59421 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3c75c489-e194-3f72-860d-cb396ee05394 | -9.04395 | -47.02147 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6bc5ae22-c01c-37d0-95bf-31d60debdda6 | -7.72411 | -42.38841 | 2025-10-05 03:34:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74752fcb-dbf3-3305-8f0b-f0c1601b3f1e | -7.79328 | -42.57355 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README32.md)
