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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56044c77-6fb3-3e18-bbd9-9fd9f9800950 | -19.71135 | -56.73301 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| ba0fb7da-9f6e-316c-9e6a-3b095763ce5e | -19.71078 | -56.73669 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 49d25683-6cd4-3c36-8cca-fa1c73991f7f | -19.71021 | -56.74038 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| eec29aa0-4d15-3d20-a6f9-3f8cc8a50ada | -19.7084 | -56.77409 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1179341a-bc1a-3352-881a-f1cd306b7326 | -19.70801 | -56.73244 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 138353fc-d2a6-3001-951f-802cfcf2ed70 | -19.70744 | -56.73612 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a2d71188-8850-3a06-b70f-a0825458ace7 | -19.70735 | -56.75879 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 245ccd30-cee9-3e0a-aeb3-97838f104903 | -19.70506 | -56.77352 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5d022b10-5c6e-3f71-a2e1-1a588959aca9 | -19.70468 | -56.73186 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e0baa414-da8a-30ce-80a7-506bac347bc8 | -19.69915 | -56.72334 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c810a2ec-bfef-3608-8cff-ed166b1603f3 | -19.50693 | -56.63467 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7b3fdddf-de19-3b4b-aefb-f663b3110989 | -19.50579 | -56.64203 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1e2e0d49-c520-3583-b85f-9342dae011bf | -19.50465 | -56.64939 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3c6914e0-0935-3665-8af8-a9239ff3cb47 | -19.5036 | -56.63409 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 67d505dd-0b71-3f77-bf26-80169329ae35 | -19.50303 | -56.63778 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| d9667735-b83e-3ab3-ac62-777febdc64b2 | -19.50522 | -56.64571 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f363d6e7-268d-3d91-96d9-355feddf6d76 | -19.50408 | -56.65308 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ef512833-592c-32b3-92e7-4111c738c1b8 | -19.50351 | -56.65676 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 7ed4121c-8bec-309f-834d-b015f016f444 | -19.51369 | -56.61314 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c232d61a-3d0e-326d-9540-10dced41d9d1 | -19.6863 | -56.74004 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 830d87b3-fe0b-379e-922a-7f8e645c6d74 | -19.6845 | -56.77374 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f43df8dd-2a49-32f2-b101-3817b1a2c67c | -19.68297 | -56.73946 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 19b32ceb-d8f0-3b3d-8a56-f612877291f6 | -19.6624 | -56.73969 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 79ec226f-7414-3e8c-ab93-a1d09ae26f5e | -19.6606 | -56.77339 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 92621cc4-8219-3a7f-9a27-ac0c8fba90f3 | -19.65955 | -56.75809 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 84378582-93a2-3ffa-ab05-bc27b1b4d027 | -19.65898 | -56.76178 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e4b440d6-d486-3cce-9412-fcedd484eeda | -19.65849 | -56.7428 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2193138b-0e02-330c-9ec5-a11d38ba71bb | -19.65841 | -56.76546 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a8640343-4028-311f-83d1-7ccd68d3f344 | -19.65792 | -56.74648 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| da3b0bc8-84b0-3265-9b76-2ac2e2ac46ed | -19.65784 | -56.76914 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| daced05c-94d1-3447-ae40-e7b5f21f4631 | -19.65726 | -56.77282 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 0727a7af-84bf-313e-903e-4a5e092f0e49 | -19.65621 | -56.75751 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 92d1ca4f-7659-3496-99fa-58a27e5b3e38 | -19.65564 | -56.7612 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 31072f7b-303e-3b53-9ad8-fc7d3f5ea8b4 | -19.65516 | -56.74222 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 84543860-28f7-35e1-9951-13c138f2cbbc | -19.65507 | -56.76488 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 341d0bb2-165d-3555-bd6e-0072ce65e9db | -19.65459 | -56.7459 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9b0f4d1d-db1d-35cb-9ba0-feb596848b4b | -19.6545 | -56.76856 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 637a57ba-1a88-309c-a5ad-4a9112645bfc | -19.65402 | -56.74958 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cdeb4705-302d-3050-81f1-b374cc930095 | -19.65393 | -56.77224 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 8a7f893d-fdcf-359e-8856-dda3abba53d5 | -19.65345 | -56.75327 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ef4b890b-5d26-3d11-918a-3e5ec6e45920 | -19.65288 | -56.75694 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4ffa62f8-365d-358f-8b15-668975b6b977 | -19.65231 | -56.76062 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 571a88ce-3cd1-369a-bc3c-623d899653f4 | -19.65183 | -56.74165 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dbb21c6f-8ba6-3835-9364-084b7ba028a7 | -19.65174 | -56.76431 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 0b08e790-760f-3107-b4f6-304daeb07bc0 | -19.65126 | -56.74533 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4fb088f3-b65f-3610-b1ff-b7e04aadc812 | -19.65117 | -56.76798 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| cbbca672-27c4-3efb-8c7b-ceeeff38add5 | -19.65069 | -56.74901 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 65c94108-387b-3100-b0ae-32adeb2a6062 | -19.6506 | -56.77166 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| ff8750b8-a52b-321c-8c91-6be02d78c3d9 | -19.65012 | -56.75269 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fe06df66-b110-3dfc-9be2-2569e02ef484 | -19.64955 | -56.75637 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| af1a4fea-39c7-3936-8983-f38ed32b84e5 | -19.64898 | -56.76005 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 72827e91-4534-3770-8b4c-1ceaa87098d5 | -19.64849 | -56.74107 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 58580dcc-6da2-3d38-b1c2-bcfc5e2aa8a9 | -19.64841 | -56.76373 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| fe6ae70f-3fe1-32b2-97cd-a094366f6805 | -19.64792 | -56.74475 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7d43f883-d690-3417-a662-c7ceeaaa5805 | -19.64784 | -56.76741 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 7ab8de39-f210-31fd-b609-1aca0749e133 | -19.64735 | -56.74843 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5073bfb3-e191-39e1-8487-ecd5ff5e1c18 | -19.64727 | -56.77109 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 8110e241-7df5-3f57-b72b-b360ac394d63 | -19.64678 | -56.75211 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 99c46871-3df9-3b15-bdb2-ec754b32bda8 | -19.64622 | -56.75573 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 171b992a-8640-3953-b330-d85a82c27613 | -19.64564 | -56.75947 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| aa5ccdac-9156-32a8-852f-dda4af3f62dd | -19.64516 | -56.74049 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| a11a8f02-82a0-3d29-9daf-12ed61395753 | -19.64507 | -56.76315 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1b1a9e32-f9c1-3910-8130-c600bb1c20db | -19.64459 | -56.74417 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 2eb311cc-5dfe-3ff5-bc64-6a62bdc1cf6f | -19.6445 | -56.76683 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e323151e-8e86-3ee2-915f-491001f82ad8 | -19.64402 | -56.74786 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f7bc8aaa-3f59-344b-b38d-b2c630e6204f | -19.64393 | -56.77052 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 686dbda0-ee58-3bbc-a808-cef31324027c | -19.64345 | -56.75154 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8457a31a-d806-355c-8c7c-1b53a04439c8 | -19.64289 | -56.75516 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c560b176-2ed8-3f39-b664-c0cab8a27bb6 | -19.64232 | -56.75884 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6b6d5f95-dbdb-3da3-aa01-8afd7be1e1ff | -19.64183 | -56.73992 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 44913b48-de25-3d68-9c5b-eb9c6c25d4eb | -19.64174 | -56.76258 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ba2fdd6e-d69b-327c-ac8c-a2f0e398c657 | -19.64126 | -56.7436 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| e5e5d178-0ba5-3ff5-a094-bef1936b2726 | -19.64117 | -56.76626 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d6070303-fe41-32f1-9c15-4f608621e6a1 | -19.64069 | -56.74728 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a057c3a8-1eaa-3260-b5da-9436f7a6319b | -19.64012 | -56.75096 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 199032fb-0f9d-3608-8cf9-f2bd8b7a6a50 | -19.63955 | -56.75458 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 35a5e090-c441-39f0-a4cf-773c18e79c5d | -19.63898 | -56.75826 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5cc8e136-755b-323f-8e96-7fc4b48d0fa2 | -19.63849 | -56.73935 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 84b3afaf-7f36-3e3f-9631-de2e48f6b391 | -19.63841 | -56.762 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 688a410e-fbd0-31cd-add4-3ec258edc190 | -19.63792 | -56.74303 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| e359df24-8a7d-38bb-928c-aadb7a7fd279 | -19.63784 | -56.76568 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b13a8aa-0565-31e3-92c2-837c14bf8326 | -19.63736 | -56.74671 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9f8e88a8-85f5-3701-aa3d-a8382ff07fdf | -19.63679 | -56.75039 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3a8bf6d1-2861-369b-a75d-1f25a291265f | -19.63622 | -56.75401 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 79d48b98-14c8-33b8-93c5-9257d7206ee1 | -19.63565 | -56.75769 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f23d8cae-f7cf-350e-8705-0079d4297eed | -19.63459 | -56.74245 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8c04d21a-efcb-3b4b-8b25-fbd66ac8f9df | -19.63402 | -56.74613 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bee85f07-6f8e-3342-be26-e7e15ffaba8a | -19.63346 | -56.74975 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 25ff580c-e822-30ec-8d27-29ba738665ac | -19.63289 | -56.75343 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e2a64ba0-b7e1-349e-9a8e-2388f229ac30 | -19.63232 | -56.75711 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 13bd5483-44ee-352d-9aa9-8cdb7ee7fc46 | -19.63175 | -56.7608 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8dff65cf-ac03-3e87-999a-eabc831d275f | -19.63126 | -56.74181 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b98ff3df-b664-3312-a6e0-13e6802b8259 | -19.63069 | -56.74549 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 73c830c7-58d3-3fdf-8936-ef7370c343ed | -19.63013 | -56.74918 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0fc00cf9-d747-35b6-bbec-4a66bf144085 | -19.62955 | -56.75286 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2bef979e-1710-3474-b166-2b905760feec | -19.62898 | -56.75653 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d4cb462d-6c5a-3b63-916f-39956efa82c7 | -19.62842 | -56.76022 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5b0e3abf-3d74-3a43-8e9b-af1724993b4e | -19.62793 | -56.74124 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 340db9e2-b90f-338b-ad81-3394a9c1dc14 | -19.62785 | -56.7639 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8d9b23fb-ccf8-3bcb-8019-3b5f6f7ec6d9 | -19.62736 | -56.74492 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README85.md)
