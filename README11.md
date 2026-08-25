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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e921d94-c2e1-38fe-8408-f56faf912abf | -6.1239 | -57.75017 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b20c55b3-3eef-3f59-84e8-33e3c21f7326 | -6.8077 | -58.65667 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c335c919-1289-3e4f-80ee-cec0eb14bd28 | -6.1687 | -53.48093 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 0c716a7c-2e48-363f-bfa8-886fd19d6d6f | -6.62839 | -58.49252 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 166.2 |
| f03ebcfd-fbf9-3d2c-b909-7e085322c36b | -6.18595 | -53.50202 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| e047c46e-5984-3982-9b3e-361d90d9bdfa | -7.0122 | -59.25259 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 15026f9c-3cb2-349c-8fdb-647fc36dbf0c | -6.17496 | -57.3967 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 16a5e4a2-488e-3015-9932-9aba6e90bb14 | -6.55674 | -56.55893 | 2026-08-25 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c3af69a4-55be-3fe5-a209-8b2b54a512e6 | -6.80241 | -59.60086 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cb7a5eec-5324-34f2-8cc8-2fae33935ea4 | -6.54483 | -55.08334 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2658fa0d-24e4-3c09-b8a3-97053011151e | -3.13175 | -61.19261 | 2026-08-25 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9eaeecaf-f983-3d14-b07d-0fbc21389473 | -6.44654 | -54.96248 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 9f62c6f2-8897-34da-8026-467fd2eb5468 | -7.53378 | -61.35383 | 2026-08-25 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2d1c8940-2d43-33c8-9939-80beddfe4f57 | 2.59878 | -60.68852 | 2026-08-25 00:52:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e17ef84c-3e9d-3dd8-85bb-223399610249 | 2.58824 | -60.69694 | 2026-08-25 00:52:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6a91d4c3-1972-3072-b36c-8942bb767fe7 | 2.59745 | -60.69822 | 2026-08-25 00:52:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| a6c092be-fe18-3d99-a275-b47dcc8d66f2 | 2.59611 | -60.70794 | 2026-08-25 00:52:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 44065301-6450-3e19-849b-3e3c1108dfe9 | -6.641 | -58.4987 | 2026-08-25 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 261.1 |
| 88aab789-b8f4-3bdd-8de4-e531282b4901 | -6.6227 | -58.4801 | 2026-08-25 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 5cb1df72-1d12-38d6-be86-d2515fbcb801 | -6.9872 | -59.2582 | 2026-08-25 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 4b884989-2543-34d8-a414-e2dbfc7f01dd | -7.0242 | -59.2374 | 2026-08-25 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1266ed86-e9cc-31f9-8ae9-21b0094a5589 | -12.7797 | -44.2576 | 2026-08-25 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 323.2 |
| 2b5c1992-b2e3-35ab-a254-9093f3b399d8 | -6.1477 | -57.702 | 2026-08-25 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 22885002-d243-3026-8460-8725b9e954eb | -7.0241 | -59.2567 | 2026-08-25 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| fd5aa308-e0ec-34e5-831c-2f0393ce7b98 | -7.2659 | -45.8668 | 2026-08-25 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d4aab9a9-4f27-3fa2-9b40-2d34ee7d2be4 | -8.0918 | -47.527 | 2026-08-25 01:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| eda81a6f-f1a0-3e39-9583-2538a09c21c5 | -12.7792 | -44.2812 | 2026-08-25 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| c1976bd1-4687-35fa-91fa-898a311a08e3 | -7.2661 | -45.8443 | 2026-08-25 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 4ec491bb-079b-3e13-b05a-71d48514611d | -10.3536 | -45.0561 | 2026-08-25 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 34477a74-456b-361e-aa1b-fef3cfe5900a | -7.2856 | -44.0875 | 2026-08-25 01:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6b2d3244-b742-35fe-8fd5-b48bd1795531 | -6.9873 | -59.2389 | 2026-08-25 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 85eba104-729b-37db-a8b9-29496c6d986c | -10.9294 | -51.0654 | 2026-08-25 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 306f26e0-1b1d-39c0-b4ee-f1dea7ceaf59 | -10.3918 | -45.0512 | 2026-08-25 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 02505f56-5e41-30d6-b858-16b2853fcc20 | -7.5475 | -61.3627 | 2026-08-25 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 542961e5-cb2a-3781-b85d-55e2bb97b4fd | -10.9101 | -51.0886 | 2026-08-25 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 59074c40-6e81-33e3-b6e7-64ccd227ed18 | -10.9104 | -51.0674 | 2026-08-25 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 11a22543-5265-3582-a82c-e81b8793fbcd | -3.5221 | -48.1896 | 2026-08-25 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| fd9f9be9-8d15-3107-9293-3d5ff68293e8 | -11.1443 | -44.4865 | 2026-08-25 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e52f94e3-a46c-3c5d-8e04-9bcb8f1f692d | -11.4302 | -44.5382 | 2026-08-25 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 6921bf43-a6b8-3e81-8436-3bf4f4e53301 | 2.5983 | -60.697 | 2026-08-25 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 01b32874-27c6-311a-b051-3356ef52d84f | -11.1447 | -44.4632 | 2026-08-25 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 147e5129-8621-3b4a-aea8-76e30acbc929 | -11.4494 | -44.5353 | 2026-08-25 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 87ffeac7-c5f0-3038-a0cf-e1b1c7dc5943 | -6.6409 | -58.5181 | 2026-08-25 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 7e43f8d8-6214-3365-8360-2b1ac9c1f165 | -7.2474 | -45.846 | 2026-08-25 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| ba3be054-8640-3cde-a66e-251cd5e8b1a1 | -7.0058 | -59.2382 | 2026-08-25 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 184.1 |
| 1db93d7e-323c-32d0-910f-d2e967ecabde | -10.9291 | -51.0866 | 2026-08-25 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| e627dc1e-6cae-35cb-a87e-75cb059e98ce | -3.5222 | -48.168 | 2026-08-25 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 07eed52e-83d2-3cb9-84c5-7eebe75fe5cb | -3.5407 | -48.1673 | 2026-08-25 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 36066777-968f-3c4b-a869-d30ec8ee46b0 | -7.2713 | -45.37 | 2026-08-25 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| e08a8943-eaec-3d7b-b7c3-df690518d4a0 | -7.2901 | -45.3683 | 2026-08-25 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 47cfbd33-dd74-3104-ac72-fc29f8d15679 | -7.2858 | -44.0644 | 2026-08-25 01:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ddb12790-5af3-3f52-b5c3-3a6ac21ae752 | -10.3727 | -45.0537 | 2026-08-25 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 347.0 |
| 698204b0-5051-3bd0-8ec0-68b869f4b4c6 | -8.0695 | -44.6552 | 2026-08-25 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f6f81335-c1a6-3686-bbf1-438475c862d1 | -6.6411 | -58.4793 | 2026-08-25 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| f704a356-07a7-36d2-b4ad-caa00ee9efee | -7.2471 | -45.8685 | 2026-08-25 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f8985b75-923a-3d59-8c73-0280fe9f9ffe | -10.3723 | -45.0767 | 2026-08-25 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 139.5 |
| d33fa6d6-2663-3eca-80d7-c87f5386ce49 | -12.799 | -44.2544 | 2026-08-25 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 5383914c-f3e7-3f0e-ae53-e1f56aa396a7 | -6.8008 | -59.5934 | 2026-08-25 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 16ae1373-c967-366f-8f3d-a84b4b92dd2b | -10.3914 | -45.0742 | 2026-08-25 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 5fcfb08d-664d-334d-b3e1-24df77f57a11 | -7.0057 | -59.2575 | 2026-08-25 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.1 |
| dfc8f1a6-0a49-3e43-a9da-17d8fa3de678 | -12.7986 | -44.278 | 2026-08-25 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ef38b275-10f0-386e-ab6a-7235fcd237cd | -10.9483 | -51.0634 | 2026-08-25 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| ca581d21-f664-3c1b-848d-19a1f32d11ab | -3.5406 | -48.1889 | 2026-08-25 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 757514f2-c3c5-3126-bba3-a433e83269c1 | -6.6226 | -58.4995 | 2026-08-25 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 11048166-93e6-3aac-ac81-ba54ffc28fe5 | -11.4498 | -44.512 | 2026-08-25 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| b5f694aa-a4d4-37af-b5c6-f704acc9ecef | -11.4306 | -44.5148 | 2026-08-25 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 02926f58-6881-3edd-b521-310bcb0d9bc2 | -17.5949 | -50.9041 | 2026-08-25 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 3d44ad79-c50a-3289-a32d-546928b07068 | -7.4286 | -43.1182 | 2026-08-25 01:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 7341f7a3-9250-368b-88de-bda006778ecc | -3.5221 | -48.1896 | 2026-08-25 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 05590d6c-2c5e-3e3e-b4bc-065d2ac0515c | -7.4286 | -43.1182 | 2026-08-25 01:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 6ce5f465-36d5-38bb-a166-2de3838b7c04 | -7.0058 | -59.2382 | 2026-08-25 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 371d97f2-2e5f-31c8-b5b9-e88b21e83ae6 | -11.4302 | -44.5382 | 2026-08-25 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f3cda53a-ce88-3a4f-8e7c-01d64673a3fd | -6.6409 | -58.5181 | 2026-08-25 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8eba126d-a94e-3942-8a8b-603205b4e24f | -8.0695 | -44.6552 | 2026-08-25 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 17190e08-662c-3382-aff4-4407dee163a4 | -10.3723 | -45.0767 | 2026-08-25 01:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 29f85f2b-83f4-3b07-986a-74afdf11578b | -3.5407 | -48.1673 | 2026-08-25 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 32cfd462-e708-3a60-9396-a442dcefc043 | -12.7792 | -44.2812 | 2026-08-25 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| cecdbac3-80fe-37fb-b788-9aeaccb3a441 | -12.7797 | -44.2576 | 2026-08-25 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 363.2 |
| 42c042a4-a076-32a8-8407-465088882e2e | -10.9101 | -51.0886 | 2026-08-25 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 9e37add8-8b89-3580-867a-c711a549ed09 | -10.3727 | -45.0537 | 2026-08-25 01:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 369.3 |
| 89946222-47d0-3869-a1db-34fbdba94b97 | -11.1443 | -44.4865 | 2026-08-25 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 5687f90f-425d-3ffe-ab9c-95443d7bc2de | -7.3287 | -64.7039 | 2026-08-25 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| e9387c75-d1bd-318b-a09b-ae53f251b514 | -6.6227 | -58.4801 | 2026-08-25 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 64cfdeb3-8983-391f-9f04-104c61c8c516 | 2.58 | -60.6973 | 2026-08-25 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 89bca1f5-47b3-34d6-b263-da3761ca6f48 | -10.3536 | -45.0561 | 2026-08-25 01:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 6757ce76-c2c2-3841-bacd-1b35d309fd32 | -10.9104 | -51.0674 | 2026-08-25 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 47c5ad54-7d13-3c0b-8139-434a8ea4b65a | -10.9294 | -51.0654 | 2026-08-25 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 8b9b246f-4622-31c7-a29f-a55ceadf2e7b | -7.2713 | -45.37 | 2026-08-25 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 0d308988-d249-37b8-8e33-54ed01136146 | -6.6411 | -58.4793 | 2026-08-25 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| e3b95fe0-d8ac-354c-9b7c-6198531def95 | -11.4306 | -44.5148 | 2026-08-25 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 785b78f7-af98-377b-aabc-b830ace93473 | -7.5475 | -61.3627 | 2026-08-25 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| d0b89d9b-d566-34f3-801b-3336266e9953 | -6.641 | -58.4987 | 2026-08-25 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 292.8 |
| 5ce5ea69-11c5-3ca5-bafe-31264810197c | -12.799 | -44.2544 | 2026-08-25 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 18539837-447f-3dab-b3a0-932b28dcbee7 | -12.7802 | -44.2341 | 2026-08-25 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| edc546da-a43d-3876-b5df-17f2bb28a78e | -7.2858 | -44.0644 | 2026-08-25 01:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 430cc698-ed82-3dbe-8746-812a2d0e4b11 | -3.5406 | -48.1889 | 2026-08-25 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| fe532cbd-1634-385a-b0df-b9d66f286768 | -7.2474 | -45.846 | 2026-08-25 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 33f8595f-2f15-3386-83fb-58c8fa06865b | -7.2856 | -44.0875 | 2026-08-25 01:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| dc3be8b3-84c7-323d-b65d-8680e63e77f8 | -7.2901 | -45.3683 | 2026-08-25 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| acc8eac6-5c70-3dee-9ded-e4557ba627b1 | -7.2659 | -45.8668 | 2026-08-25 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |


[Clique aqui para ver as próximas entradas](README12.md)
