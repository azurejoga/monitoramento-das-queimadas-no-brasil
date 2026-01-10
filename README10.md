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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7435983-6e67-36c5-a97c-0b4d3a59bea5 | -7.48668 | -45.57681 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1b09b6b9-1dad-3095-a042-3bc105ae90b4 | -11.8378 | -48.64662 | 2026-01-10 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fdfbae9b-97b6-3328-9fd9-a70502204f83 | -7.49364 | -45.56231 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5e64139e-d639-3e9e-b2c4-37e4f62fe532 | -12.38277 | -58.04453 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 978f5387-d6de-31af-9845-1e15c7c11fbd | -10.488 | -44.92999 | 2026-01-10 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27e32ebd-16dd-363c-985e-aa089096afb6 | -13.48313 | -52.9447 | 2026-01-10 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a162125-5e70-3f6c-a9e2-16cdb2bed32e | -12.38734 | -58.04055 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| e1dd34ca-ed93-3564-ab6a-f7e54af5c687 | -7.49144 | -45.57751 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c06db11a-3edc-3eec-8c27-8f61bb286ad8 | -7.49586 | -45.57947 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e555e47-93f7-3412-92b1-1da4d6c774d5 | -10.79308 | -48.22618 | 2026-01-10 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9d368e4-8063-3ef4-8963-2974ede08cb8 | -12.39567 | -58.03724 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 5906b89b-e96d-3989-bd0d-79c8c9e28ffa | -12.3911 | -58.04121 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 4b7edd7f-90ef-3592-8ff6-c525202a5965 | -7.49516 | -45.58457 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 627a03e5-c20a-3fcc-8a5b-6db24541e779 | -7.36006 | -47.02927 | 2026-01-10 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47e7df99-be64-305d-8c0b-a595c0b6a1bb | -7.48998 | -45.58765 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d944027f-91d7-3b84-b6a5-9693f7747662 | -12.40238 | -58.04319 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 57087f64-a82c-366f-bdcc-07bf610feb93 | -12.40024 | -58.03329 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09a4bb09-659f-3007-8a08-7ee067229d59 | -12.29458 | -57.3919 | 2026-01-10 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1cfee34-c702-3a99-ae66-2e340f32b4e5 | -11.15249 | -55.17316 | 2026-01-10 04:57:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32cfc51d-4621-3e9b-9a12-a8b1a62c7b47 | -11.17389 | -43.30625 | 2026-01-10 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a66b6b90-20b5-3aba-960b-b2666f52a2fa | -12.4115 | -58.03531 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8109dd5a-5ae8-3d52-a568-09b38d22f788 | -7.49386 | -45.5585 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 160cc767-a916-3f9a-beb0-e0fec40bd91a | -12.39782 | -58.04714 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 78bfc71d-abc3-326c-84c5-0e8dbc4f4060 | -12.38653 | -58.04517 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29ceef0d-2d9e-345c-b219-8eb83809ed31 | -9.04262 | -46.98873 | 2026-01-10 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8242e3e6-4000-33cd-b2f1-4cd09f536c11 | -12.38477 | -58.03276 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 255c12c9-0b1c-35a6-86a4-ee3fb831f050 | -7.49108 | -45.5788 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 24abeb4a-0e26-354c-874c-969cc43f159f | -7.49291 | -45.56735 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7c2ff0a-5ddd-39ea-8332-949e5acb09d4 | -12.39648 | -58.03262 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d657240-4b8b-357c-a284-a6b1edf1531c | -7.49864 | -45.55918 | 2026-01-10 04:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67a3cd0d-1589-3169-8a75-5dd0f71a3b54 | -13.48652 | -52.94524 | 2026-01-10 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b37d1f12-97f1-3b09-81d9-109f47a2865e | -12.40694 | -58.03925 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 23ef6eb8-6942-319d-9816-525a018dee1c | -8.54652 | -57.31467 | 2026-01-10 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 458445c3-58af-3fa1-a2e0-0132136eb206 | -12.38815 | -58.03592 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9e3c15d4-a6a7-3992-b542-8c7630474df3 | -7.4897 | -45.58894 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7735bb81-d990-348d-b6ea-90269f668529 | -14.27619 | -47.83312 | 2026-01-10 04:57:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4438e59-b23c-3d09-90ab-41ec6ad0b506 | -12.39191 | -58.03658 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 48d2224a-69b6-3c66-bbcb-6f869f91a146 | -7.48522 | -45.58694 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e69f0fa6-b0c2-390e-84f5-1ae54a1ee65d | -14.26649 | -47.83722 | 2026-01-10 04:57:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 364c44ed-f61d-30b2-a69c-a60a4b2f1694 | -12.39943 | -58.0379 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| a4c9a167-b4c5-33ad-a8a8-e345f4767d52 | -12.39029 | -58.04582 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a2843e2-b4ee-33e0-b351-16d3e016daa5 | -7.49178 | -45.5737 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58cc7b5c-b7ea-36ca-a9d1-2e4a79bb5732 | -11.84244 | -48.64346 | 2026-01-10 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2da8f3b6-a313-3459-8787-bc45e94b7f82 | -7.49248 | -45.56861 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 57def350-23fe-361c-8bb7-5724fe156b3f | -11.84192 | -48.64721 | 2026-01-10 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a17d2159-833e-3fa2-9c7c-fd44d46164eb | -7.59844 | -45.89167 | 2026-01-10 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6f89da0e-aa58-3de0-8054-03f724a07de3 | -12.38439 | -58.03526 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93184109-0532-3b36-a056-f01359df0989 | -7.49218 | -45.57241 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b33145c1-5847-3565-8d87-693f95a18de6 | -7.48563 | -45.58317 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 766b9d43-0a0c-3461-900f-92b797a9eeb6 | -8.54192 | -57.3187 | 2026-01-10 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| dc06b030-e923-3d9e-80dd-ea2ee9aef4b5 | -7.48632 | -45.57809 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e7f4e76-2c34-32cc-93aa-85579fc68b2c | -12.40319 | -58.03856 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ec6563ec-e508-3a32-915c-6a513567ed42 | -7.49548 | -45.58325 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| afefb8f3-73e4-353c-8be3-7557dc72869b | -9.04765 | -46.98503 | 2026-01-10 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba65ed7f-17ad-3f1a-bf67-ddd5091b94b2 | -12.39486 | -58.04185 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 24949865-54af-3f23-b5bf-53d173743a09 | -12.40775 | -58.03463 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e64928da-55dc-3405-9600-faaaadcdb811 | -11.83728 | -48.65036 | 2026-01-10 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7d3b5702-d273-3e26-abcf-e3854dd5d5d5 | -12.30114 | -57.37547 | 2026-01-10 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b518a597-27c0-3329-bf1b-8ab86e760b6f | -10.4876 | -44.93311 | 2026-01-10 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bca9231-ec8a-3bab-9a53-2f53b79d2ec7 | -7.49474 | -45.58832 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7d7b65c1-cd66-305f-b4ea-1edc7fffa5d6 | -11.05719 | -49.49626 | 2026-01-10 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb79411e-d088-3c8f-b5df-ed4fb86a8b22 | -12.29384 | -57.39617 | 2026-01-10 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e30ed41-0dc6-3fcd-aa39-eb46d6c04902 | -14.2716 | -47.83311 | 2026-01-10 04:57:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37cb88e5-d893-3249-8e7b-1b0f0bc53ca1 | -7.59376 | -45.89102 | 2026-01-10 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92ff8de6-b139-39a7-b2dd-5ea13e8b7dbf | -7.69519 | -46.84974 | 2026-01-10 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e3ce349-95e8-3c9d-b459-0cc685e81fb3 | -12.3832 | -58.04204 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abf9e79c-1f3b-371e-99b6-6b0e2a185f45 | -12.29898 | -57.36628 | 2026-01-10 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bb0f64ab-11fa-30e6-b3a9-2395c6b5a770 | -12.29094 | -57.39125 | 2026-01-10 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7751a4e-d429-33d2-a097-14fbe7aaab59 | -9.03819 | -46.98808 | 2026-01-10 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e638cf1-2a27-3eec-962c-820e78a7e758 | -12.38949 | -58.05044 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff2194ec-c250-3cfb-b610-da9e8768c517 | -7.49446 | -45.58963 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 80ec975a-ef4c-360d-8aed-9120811d3b34 | -20.26705 | -46.41873 | 2026-01-10 04:59:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae95347d-17ae-3c9d-b9cf-929af24fb073 | -16.09965 | -56.75369 | 2026-01-10 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28a2f399-2d4f-3330-8996-bebfe782fee4 | -16.36959 | -57.20871 | 2026-01-10 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 77183e9e-12f1-37b1-9740-3044dae3acaa | -14.20161 | -57.2523 | 2026-01-10 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9f331e4-ae30-3487-a67a-6eaa664cf451 | -14.19525 | -57.24687 | 2026-01-10 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6883600d-cf9c-3354-a9a9-1179f82fac36 | -20.26447 | -46.41529 | 2026-01-10 04:59:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 41b1e639-d9f3-360b-b12a-569e654d4a65 | -18.52478 | -55.10621 | 2026-01-10 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0f3a8dde-f445-38cf-adb1-4731cff885dd | -16.59519 | -58.21149 | 2026-01-10 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b06d81db-f27a-374b-a4f2-baff3988d9ad | -20.22434 | -46.48726 | 2026-01-10 04:59:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90917dff-72d7-3c31-a163-cfd537f2581f | -20.26988 | -46.41557 | 2026-01-10 04:59:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1adc303e-087d-33f1-ab96-5178880c412c | -15.48098 | -48.95267 | 2026-01-10 04:59:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e590efe-0776-3df6-b3ab-1f4082eb252e | -16.59085 | -58.21506 | 2026-01-10 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7be225c6-6358-34e5-9c99-fe054ed9f607 | -16.59445 | -58.21572 | 2026-01-10 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5dfff01a-d02e-3424-ab80-b1aec1e49e92 | -20.26748 | -46.41442 | 2026-01-10 04:59:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0577621e-3e65-3c7b-87a0-77c04113f3e1 | -16.09688 | -56.74927 | 2026-01-10 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a232c67-077f-33bd-a1fd-6a63f2800b20 | -16.10243 | -56.75812 | 2026-01-10 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9cd3080-513a-310d-a3ec-7181fe5b9711 | -16.10371 | -56.75049 | 2026-01-10 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a06aa9c-1024-30d0-b009-29880fa15984 | -14.1924 | -57.24218 | 2026-01-10 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eefdbeaa-babb-3844-96bb-274eabe09107 | -20.63839 | -49.71588 | 2026-01-10 04:59:00 | NPP-375D | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5718030-b131-3ac9-91ea-7595f33bfba8 | -16.10029 | -56.74988 | 2026-01-10 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa127617-7bfc-354d-8b79-1c0f5c8161a7 | -20.27248 | -46.41877 | 2026-01-10 04:59:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e511bb5-b98a-3007-9a85-90a22b9349cb | -14.31266 | -57.59217 | 2026-01-10 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f11a97e9-60bf-37c9-b055-6132e75fb5ab | -18.52421 | -55.10987 | 2026-01-10 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 86f19af6-8fe3-3857-9ef8-4b093d03b5f7 | -20.21933 | -46.48346 | 2026-01-10 04:59:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8442e7e0-7bd5-31f3-beb3-fd9bafccee49 | -16.44629 | -58.16071 | 2026-01-10 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| db024e2a-76dc-38df-9701-5698f31fd4d8 | -16.26834 | -54.36002 | 2026-01-10 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f979ad1-a09f-3512-af5a-66bba5a930c9 | -14.19171 | -57.24624 | 2026-01-10 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfef5052-570d-3f89-859a-460ae8087e2e | -14.31339 | -57.58794 | 2026-01-10 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddeabb2c-dc4e-393c-873d-579236018f0a | -14.19455 | -57.25097 | 2026-01-10 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README11.md)
