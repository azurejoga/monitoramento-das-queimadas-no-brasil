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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8caf8db-064e-3be0-b837-0488ec390d69 | -12.3846 | -50.3026 | 2025-10-08 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 39806f13-4483-3f4a-9049-1643f4073977 | -8.6295 | -45.1 | 2025-10-08 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 412.6 |
| aa622710-9d5d-30ed-8115-5c270f8833a4 | -7.7919 | -44.246 | 2025-10-08 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 4004fc10-854e-3a31-8db6-6c2a9ab5706e | -8.9306 | -46.6033 | 2025-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| dfdc9974-9f83-37f3-af85-b719920c05b2 | -18.4125 | -45.2155 | 2025-10-08 13:50:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 34ac5eea-5596-3f11-846b-4689b3952738 | -10.9106 | -47.1353 | 2025-10-08 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 776e6cf6-5b9c-3d78-905a-ac72e301c072 | -11.0451 | -50.9047 | 2025-10-08 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 3f0d6d47-c9ed-31f1-8c09-222f368ee621 | -8.9118 | -46.6052 | 2025-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1a1fa023-dab9-361e-a4e5-b641830f3b77 | -12.1576 | -51.4399 | 2025-10-08 13:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 22adbd5e-6c8c-3676-bbe8-7342137c2f48 | -13.3438 | -48.0072 | 2025-10-08 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6f673899-0035-32ae-a80d-c4034d94a500 | -7.7203 | -42.4023 | 2025-10-08 13:50:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 13ceee16-850b-3c48-b818-6af0366e3769 | -14.9022 | -51.4749 | 2025-10-08 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c6fc95dd-6596-334b-9cbf-69dd4eac6b52 | -12.629 | -50.5519 | 2025-10-08 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 76b36b4a-c9ca-3f02-a737-867dd4a7dca7 | -10.8732 | -47.0953 | 2025-10-08 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8a1b379f-7c91-3108-bf85-da67081e9ba6 | -18.0193 | -44.9485 | 2025-10-08 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 92.5 |
| eb149fb4-0ccf-3c75-8328-c36f170d172c | -7.7924 | -44.1998 | 2025-10-08 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 56bd00e9-0b33-3fd7-872e-54ad0497cb03 | -11.2433 | -50.2859 | 2025-10-08 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| dd1621cc-5064-3d94-ab43-09c8382d2c6a | -8.9121 | -46.5829 | 2025-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 2633625d-37da-3120-a00c-1305a11f5f47 | -15.3979 | -48.0164 | 2025-10-08 13:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 113c0006-9030-3814-a83c-319066301a68 | -10.9492 | -50.9997 | 2025-10-08 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 3cea262e-b16d-35f3-a8fa-55b0f62c9270 | -14.8824 | -51.4992 | 2025-10-08 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8b7f8e8e-f3d7-3175-a80d-18361b21b2d2 | -16.0404 | -50.9613 | 2025-10-08 13:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f9b85b56-5331-3516-b3b6-9b4ef0bc0ddd | -8.4636 | -46.2931 | 2025-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| fad88e90-9d4e-340e-9aef-f10d622d49c4 | -14.3889 | -46.0063 | 2025-10-08 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 2e6f3bbe-4a32-3778-af17-5ca084343994 | -10.8922 | -47.093 | 2025-10-08 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 6c57f653-2882-3548-be99-c9be89e2fdaa | -11.785 | -45.0421 | 2025-10-08 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 70f1b61e-5f5e-3b0f-b8bc-a71237442ef2 | -14.9018 | -51.4965 | 2025-10-08 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 8dd2f798-3c7c-3423-9302-02b37f9a8837 | -7.7736 | -44.2017 | 2025-10-08 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e4b2a2e3-dc6f-33cb-b51f-ae3c020f01a0 | -8.2083 | -44.1105 | 2025-10-08 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 9f0c55ce-f424-3e49-8acb-808333177ab7 | -13.0009 | -46.7795 | 2025-10-08 13:50:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 124.1 |
| c422d3ea-6cc4-3550-a99a-01bd49d8e057 | -7.2471 | -44.1604 | 2025-10-08 13:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| dc9b0304-ecf4-37b4-8db1-8d7899ec7421 | -8.9005 | -46.0233 | 2025-10-08 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 85e95ac5-763d-3c23-9693-99c6d2f266f1 | -13.8117 | -45.7826 | 2025-10-08 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 305.9 |
| bed3a5c6-e38f-33c2-8871-ff90acfc3d01 | -11.0265 | -50.8854 | 2025-10-08 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 027a97f6-3282-3141-ae41-ecec8226cf22 | -8.9309 | -46.5809 | 2025-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 291.1 |
| ff51f5a4-b4f6-3a18-b87e-6f5bb0caeea0 | -14.7379 | -46.0601 | 2025-10-08 13:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2cd0a86c-eaea-391c-8e9a-d88e22319077 | -17.304 | -58.0566 | 2025-10-08 13:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 1c333654-7454-37b6-ba8a-51bd5d94dea3 | -12.5109 | -54.714 | 2025-10-08 13:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 1b385e68-c4b7-392c-836b-6272febcfdd0 | -7.4857 | -43.0655 | 2025-10-08 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 7432fbe5-457f-3b99-addc-5ea0175c74be | -7.7932 | -42.6082 | 2025-10-08 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 131.3 |
| 8a385b8a-1ac7-338d-9f16-f998c3025ecc | -8.5207 | -46.2425 | 2025-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| d16a316b-c09d-3f3c-a900-4a2a09b17ebc | -7.7919 | -44.246 | 2025-10-08 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 12179de2-b6e9-33cf-b5bd-0967a57bb554 | -12.9816 | -46.7824 | 2025-10-08 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 52352b94-2b92-3bf7-b079-9180dcf7d90f | -8.1804 | -43.3445 | 2025-10-08 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 189.2 |
| 5d4f8caf-b381-37ea-8833-6a4716908711 | -11.183 | -54.8991 | 2025-10-08 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 287.3 |
| fe8e56af-b794-3dcb-a7dd-1dc2a7615e68 | -11.0262 | -50.9067 | 2025-10-08 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c79951d5-dcf8-3fea-8060-72af28069be7 | -10.7472 | -46.6409 | 2025-10-08 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d4cd2408-3963-30d2-aab4-77935e6d2cff | -11.0291 | -50.6937 | 2025-10-08 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4126af3d-d28d-3d6b-971b-1e91903a2bb5 | -10.9486 | -51.0422 | 2025-10-08 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 8a5cbaf9-e53a-3cfe-83c1-84fbbb247c73 | -9.6793 | -49.9569 | 2025-10-08 13:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4e1372e0-82fb-334b-b6e9-79bf3b002453 | -14.9026 | -51.4534 | 2025-10-08 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 02510d51-5ff0-30c3-914e-b6e61922ac61 | -7.7927 | -44.1767 | 2025-10-08 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a6aeb3fb-b7d9-3546-a047-dc759c680886 | -14.8828 | -51.4777 | 2025-10-08 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3634766d-5020-3453-806c-9a259694b61c | -17.2837 | -58.0997 | 2025-10-08 13:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 1532d361-e945-3782-8586-3528385590ff | -10.4251 | -46.591 | 2025-10-08 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 01ea104a-8523-3005-9566-01ec486cb43c | -11.2626 | -50.2624 | 2025-10-08 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 87b2c0d6-0119-309b-905d-68104432ece0 | -13.3513 | -47.6042 | 2025-10-08 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 65d3d59e-db74-3124-8725-9c84a740ebd5 | -13.3048 | -48.0352 | 2025-10-08 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| b7f2a36c-f1af-365f-a5c3-507b46fda133 | -11.1835 | -54.8584 | 2025-10-08 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| f51e2217-a254-3fef-853e-46fc0d2d2a30 | -9.6795 | -49.9355 | 2025-10-08 13:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 3d2f3d61-5f74-3e83-81c0-cc174faa7e08 | -13.3778 | -47.2185 | 2025-10-08 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 593737eb-4b5a-3a54-9a43-80a84c55c577 | -8.9383 | -44.6074 | 2025-10-08 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 9c8f0b52-d09a-37bd-b7ba-038ea763b5f4 | -11.4153 | -50.2023 | 2025-10-08 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 2e82ee3f-091d-3333-9c5b-47b153a87180 | -12.4916 | -54.7364 | 2025-10-08 13:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 95404764-4544-35f3-88de-8eecff1923f0 | -10.8923 | -51.0057 | 2025-10-08 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 497ab833-44b9-38cf-9682-b10b5892acc9 | -13.7364 | -45.68 | 2025-10-08 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 402.5 |
| cffa5b10-cb94-3611-916c-e46b27ce244c | -13.3706 | -47.6013 | 2025-10-08 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 0f643f2a-02e1-372b-a047-d25c15e884f4 | -17.2637 | -58.1223 | 2025-10-08 13:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 3ab36c72-afcf-3376-a49e-5d7a0eb458fc | -8.6295 | -45.1 | 2025-10-08 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 390.9 |
| 6871a826-daad-37f0-a094-0ff5b8ca73c3 | -11.2436 | -50.2645 | 2025-10-08 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 2549b18b-cbdb-3ad2-ba21-d71c361e9f48 | -13.3517 | -47.5818 | 2025-10-08 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6835f783-1107-3387-b142-a4b42c789eb4 | -12.5297 | -54.7326 | 2025-10-08 13:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 429d6f9b-2702-3fde-aab9-8a3b27c41172 | -14.7179 | -46.0867 | 2025-10-08 13:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 7e1b1205-0de0-33a8-a208-9849477dd9da | -11.6863 | -46.3139 | 2025-10-08 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| c36cfa10-135c-367c-bff1-6715908c31ae | -13.2855 | -48.0381 | 2025-10-08 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f0f17865-82e7-38e8-b670-40ef124d090d | -7.2091 | -45.9167 | 2025-10-08 13:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 653a02f0-0d4a-33e1-be2f-f90d064d3723 | -12.2525 | -47.8728 | 2025-10-08 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 45e4eb9a-7d00-367b-868a-e6d63c5a92a7 | -11.9331 | -46.4153 | 2025-10-08 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 4b09d401-87e4-39c7-b9da-c9c22dfb1a40 | -10.4245 | -45.3907 | 2025-10-08 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 211.6 |
| f3caaf49-5827-33d4-9292-b401d7fdb5bc | -8.1007 | -39.4489 | 2025-10-08 13:50:00 | GOES-19 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 118.8 |
| 8fde9ffb-2129-3767-b9ea-102ca3d6331c | -15.321 | -46.1622 | 2025-10-08 13:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| af65aa2d-25ed-3807-bbbb-5443586b89fe | -14.7184 | -46.0636 | 2025-10-08 13:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 43192b5e-59f0-343a-bb9a-0ddf775bcf5b | -11.6455 | -44.2731 | 2025-10-08 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3bee72b9-6e8b-35b7-83e5-4cedef19e800 | -7.8119 | -44.1516 | 2025-10-08 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ba098136-f6f3-396d-803e-87dc10fe7990 | -13.3018 | -47.1626 | 2025-10-08 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 0809b646-0427-3cff-8745-5d10881113a4 | -13.7927 | -45.7627 | 2025-10-08 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 01d75f05-4ae7-3ab3-9d25-af81713cf83f | -9.1899 | -49.9818 | 2025-10-08 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 8f2afd83-5b83-3c0e-a617-3157af3805af | -9.2096 | -46.9084 | 2025-10-08 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| c52c3d1e-188e-318a-a100-351ba2a626d0 | -12.0122 | -45.1929 | 2025-10-08 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 225.1 |
| dc05c735-f45d-3316-9ef0-f4b78d83bd6e | -12.3908 | -51.1366 | 2025-10-08 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 97571907-d85b-35a0-8ccc-93a1c388e39d | -13.7923 | -45.7859 | 2025-10-08 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| c9992b21-01c4-3139-ab5d-e8ee5c177d99 | -11.1457 | -54.8617 | 2025-10-08 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 932be590-90fa-3d2e-beba-ecf06810224f | -9.6607 | -49.9373 | 2025-10-08 13:50:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 417bfb02-0d80-3ec7-8af8-c850aef8709e | -7.8116 | -44.1748 | 2025-10-08 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| ae4cba5d-1c01-38c6-8647-599b72d8ea81 | -10.9113 | -51.0037 | 2025-10-08 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 892f3c9a-3238-3f6c-a1b0-92ff4cc83d19 | -12.3911 | -51.1153 | 2025-10-08 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| efe2ec58-1cdb-30d2-abd7-927a2f6ca50d | -11.0373 | -51.477 | 2025-10-08 13:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a5d30ca1-5de1-33fb-ac25-8d39fd87a500 | -11.1833 | -54.8787 | 2025-10-08 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 249.3 |
| d0c424c2-af7d-3fee-b5fb-ce3b8c44f188 | -10.911 | -51.0249 | 2025-10-08 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| ff449578-d93b-34da-ba41-08e5c0a42045 | -14.4079 | -46.026 | 2025-10-08 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |


[Clique aqui para ver as próximas entradas](README107.md)
