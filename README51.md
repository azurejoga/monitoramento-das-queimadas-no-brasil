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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32ce570c-7588-3a00-aa3a-9dcff6857c9d | -10.0128 | -46.2583 | 2025-09-21 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7e2aa1e8-0a47-3810-aee7-b3cd08457718 | -11.467 | -43.5485 | 2025-09-21 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| ef9ee639-1cce-3eb9-9b97-c9fa00cc310b | -12.7306 | -46.8425 | 2025-09-21 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f46baa08-24cb-366f-8a82-c2841de27187 | -6.704 | -44.0017 | 2025-09-21 13:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e3456e48-6e05-3be9-9dcb-36503d297b57 | -11.5818 | -50.5047 | 2025-09-21 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| b2b26d27-907c-3990-bb99-163b6a860138 | -11.5821 | -50.4833 | 2025-09-21 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 6d9030ce-434c-3e2b-aa93-9ff749891c84 | -7.5272 | -44.3413 | 2025-09-21 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 9f2adf5b-8428-386b-bd09-0c1881642d15 | -14.8675 | -45.481 | 2025-09-21 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 20f150a3-c634-3b13-adb6-cd4f4c2ca5dc | -11.4853 | -43.5929 | 2025-09-21 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 9374e81f-343e-300e-81ce-9d1e8724ed43 | -12.3399 | -44.0946 | 2025-09-21 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 2b78ca20-8ccf-30c8-9857-db23a1bb3bc4 | -14.8479 | -45.4846 | 2025-09-21 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| c08536ad-e157-30c2-af12-52c05768c7ad | -7.714 | -44.4612 | 2025-09-21 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 185.9 |
| f0a9ec32-aaeb-3b95-807f-fcfb85feb57a | -5.5583 | -42.1507 | 2025-09-21 13:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| d32beda8-76ca-3cfa-b03a-85bf32d6c8d9 | -5.5773 | -42.1255 | 2025-09-21 13:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| b7b07c80-9288-365f-942a-0c61b5bf8760 | -11.5045 | -43.59 | 2025-09-21 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| b34e6918-df16-3770-ab3c-ada0a23728e2 | -17.6831 | -44.0901 | 2025-09-21 13:10:00 | GOES-19 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b1941697-9cc3-30d6-9f42-29ff534b3cd2 | -5.5771 | -42.1493 | 2025-09-21 13:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 9afa06c5-133e-3e03-b0a2-e81efffa0be3 | -7.6007 | -44.4952 | 2025-09-21 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3fe30deb-5de9-35a8-b6ec-c8dee259e96a | -12.7341 | -47.7168 | 2025-09-21 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 37d4a65a-e2cc-35e9-af9e-a5bada2f4cbe | -10.8805 | -46.6241 | 2025-09-21 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| cf03ea49-0fc6-342e-b88b-c8169f8f60c1 | -23.3981 | -49.1427 | 2025-09-21 13:10:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 415.5 |
| f6d0db90-ebd1-3a5c-86be-92c07e3e701d | -10.0131 | -46.2358 | 2025-09-21 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 7df09d74-97df-32d0-9ffe-6c428d32ebb0 | -12.2987 | -45.2649 | 2025-09-21 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 755c44d8-4188-3769-b6d0-0ba4c4c61753 | -16.0011 | -47.2757 | 2025-09-21 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 4f6a5a25-846d-35a0-a41b-3c3009d4a25b | -11.4857 | -43.5692 | 2025-09-21 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 1ba46a5a-3e19-3b60-a8f3-24e6af194453 | -23.3989 | -49.1191 | 2025-09-21 13:10:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 342.7 |
| 1abb7207-caa1-3b62-b33a-fcfa63b344c6 | -12.6921 | -46.8482 | 2025-09-21 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| acd3bc72-a4d9-3368-a210-54670365f3a0 | -10.8805 | -46.6241 | 2025-09-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4ed80aa2-1768-3677-9e2a-d022cc88bfb8 | -5.5773 | -42.1255 | 2025-09-21 13:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 30bacd16-0590-320b-b1e0-80ea2f835861 | -12.8781 | -50.5207 | 2025-09-21 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 186d4655-27d7-33c2-8768-a930c26b640c | -5.5583 | -42.1507 | 2025-09-21 13:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| f71738bf-b0c9-33f2-90c1-da2fadd2a50e | -7.6007 | -44.4952 | 2025-09-21 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 616bf641-f9c3-3246-8d71-af24de0f1209 | -23.3989 | -49.1191 | 2025-09-21 13:20:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 263.2 |
| 410ed3cd-ea4b-328e-a192-4d74542705d4 | -12.0767 | -44.8131 | 2025-09-21 13:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5c5678d6-a272-3b2d-b08b-56b704c045a6 | -11.5818 | -50.5047 | 2025-09-21 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 334a036f-8a0a-3070-b9e3-aba117edee85 | -7.714 | -44.4612 | 2025-09-21 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 236.8 |
| 6ee4ec6f-1aeb-3728-8c17-ef4b715116d3 | -12.1156 | -44.7839 | 2025-09-21 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 580444d6-b851-3edc-940f-1ad0ab9ca71c | -12.455 | -45.1254 | 2025-09-21 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 810.9 |
| 2ee854be-ab9f-3c0c-9158-b6c55777fd86 | -11.6438 | -46.5684 | 2025-09-21 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| eaf3a7d7-553e-3ef8-bf6d-4325a30868ec | -5.5771 | -42.1493 | 2025-09-21 13:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 3b962f00-fece-35e3-ab2e-3443f11e6a52 | -12.6921 | -46.8482 | 2025-09-21 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 228.7 |
| 83712236-6ab3-34d3-82c8-30f217cd66f0 | -12.6088 | -45.1244 | 2025-09-21 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 8317ad0e-8d4e-3da4-aecf-10119e2683b7 | -17.1179 | -45.9256 | 2025-09-21 13:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 7bf556e2-c53b-3010-9f9b-19195dadc6be | -16.0011 | -47.2757 | 2025-09-21 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d4ca9b4e-d435-3d43-8f8e-9a077faf9721 | -10.5976 | -46.4798 | 2025-09-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| f2b8afa3-ed82-313c-9bfd-0ba76f390d68 | -10.2811 | -46.0679 | 2025-09-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 9d824eb8-c456-35d6-ac79-b5bd97bfa8ed | -23.3981 | -49.1427 | 2025-09-21 13:20:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 277.2 |
| 528c75de-98c0-3c86-a3fb-ba0f5454e5d6 | -12.7114 | -46.8454 | 2025-09-21 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 23702344-9b03-3eb0-943e-01e57e4731b5 | -10.6932 | -46.4453 | 2025-09-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 665af1de-2456-3582-8e07-f3676726a9f9 | -17.1173 | -45.9491 | 2025-09-21 13:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 105.6 |
| df8f8f42-83f6-3246-a78b-b2d858def3cf | -15.8829 | -47.2973 | 2025-09-21 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 0570d6c9-3ff0-3a84-bfe5-3afe52049e66 | -12.3976 | -47.2281 | 2025-09-21 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 97469ad8-e030-312b-b68a-08f4f7b07c4b | -10.2998 | -46.0882 | 2025-09-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| af3b2b19-d5e8-3b38-b95d-2a160a9940bc | -10.2808 | -46.0906 | 2025-09-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 17ca4ff8-66d9-3a17-9382-7b7336ab8327 | -12.4164 | -45.1314 | 2025-09-21 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 1070bdd7-f7fc-36ed-b866-6245aa748fba | -11.2306 | -46.1722 | 2025-09-21 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 04fda295-13c2-3174-b557-0d6eb7e45520 | -11.2679 | -47.4022 | 2025-09-21 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 68b2cd1f-cb51-38c4-b8fa-9804a8d172af | -11.5821 | -50.4833 | 2025-09-21 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 6b161bf1-dffd-3a9a-9da9-b62c83f691c8 | -10.0317 | -46.2561 | 2025-09-21 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 653d601b-c67d-3c13-be35-884eb90f15a4 | -12.6093 | -45.1012 | 2025-09-21 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 3c82c0b2-c730-3b04-9961-38249667fe2a | -20.8809 | -49.6179 | 2025-09-21 13:20:00 | GOES-19 | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.0 |
| 87cdf0fd-db99-3084-85ce-636d0ed6e393 | -12.4357 | -45.1284 | 2025-09-21 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 278.9 |
| 3337cf5a-e133-3f90-a9b6-4d56c7aae216 | -3.8663 | -43.0854 | 2025-09-21 13:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6a5eaedd-f993-31b6-8546-0f35ed28473b | -12.711 | -46.868 | 2025-09-21 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 94161351-784b-3f36-b108-bc8471e51e9f | -14.8479 | -45.4846 | 2025-09-21 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 392.0 |
| 8c97cd79-1440-392c-bb86-78d6cd434519 | -12.7341 | -47.7168 | 2025-09-21 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| b7aae0a9-0335-3ba9-8f61-7ade8ed21b8b | -12.1344 | -44.8042 | 2025-09-21 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| eaa4ec3c-ead1-3ea7-addb-22e2845068bb | -10.598 | -46.4573 | 2025-09-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 07ff7ce9-0c71-37ec-a0f5-2aeb5b9b4778 | -6.8192 | -43.7599 | 2025-09-21 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 6223c02e-7b20-348a-b510-0b2e1a6df926 | -14.3136 | -47.7913 | 2025-09-21 13:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 4c55ff62-05fd-3063-bbf2-27a5a320a2dc | -7.966 | -43.8809 | 2025-09-21 13:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 886a523c-01f4-39b5-9b82-be8c08bdf0bc | -12.7118 | -46.8227 | 2025-09-21 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 3d28345d-72b3-39a7-9f81-cebf00e040bb | -14.8675 | -45.481 | 2025-09-21 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 418.0 |
| 1774ede3-fc7b-3e95-8902-2e3f9bd49c2b | -12.4169 | -45.1082 | 2025-09-21 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 8a0218a5-a20f-3344-90a5-2c713f81fb1d | -10.6741 | -46.4477 | 2025-09-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| ba87aa67-9c39-3cb7-a4e4-22f0d405cdb2 | -8.3082 | -43.6813 | 2025-09-21 13:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 2c415901-dc93-37af-a9cc-737871d52cfc | -12.7306 | -46.8425 | 2025-09-21 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8a45f3e1-7a8d-3b1f-aaa3-b5d5c102ec44 | -12.3399 | -44.0946 | 2025-09-21 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 325.5 |
| 4a5743d3-6608-307b-8dc7-f93f78ca2c80 | -8.6076 | -45.3302 | 2025-09-21 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d0970472-b6bd-36a8-a05c-fd05d3b53bc7 | -14.6241 | -49.7595 | 2025-09-21 13:20:00 | GOES-19 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e9c85443-e467-3894-80c9-d66a309a6c3d | -14.8071 | -51.3809 | 2025-09-21 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 36591986-1bfd-36ff-85fe-e9c700a74950 | -12.1344 | -44.8042 | 2025-09-21 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a2540594-fd45-302d-a22b-8d08c1c188ad | -10.0317 | -46.2561 | 2025-09-21 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 4cdc8ae4-03ec-3fd1-bed6-07037d45bcfd | -17.1179 | -45.9256 | 2025-09-21 13:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0690c489-a51b-3278-9a18-ae2b952aee38 | -5.5773 | -42.1255 | 2025-09-21 13:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 80474be5-8ad7-36fa-a711-5344e6027256 | -12.7341 | -47.7168 | 2025-09-21 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 0be23782-7266-3784-9095-aecd19fe5a09 | -11.585 | -50.2902 | 2025-09-21 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 9f998cb5-3321-393e-8d1e-002953b7f84a | -8.6076 | -45.3302 | 2025-09-21 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8e89bd91-39ef-3566-a8fe-26eff8939f04 | -12.2983 | -45.2881 | 2025-09-21 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ad352a51-e862-360c-b725-192df45dd6fb | -14.6047 | -49.7624 | 2025-09-21 13:30:00 | GOES-19 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f3d59a2d-c881-373f-9b76-97e8cb2f8290 | -7.714 | -44.4612 | 2025-09-21 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 342.8 |
| 6017262a-309e-3182-a02b-584b9d1a365f | -14.3136 | -47.7913 | 2025-09-21 13:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 1559d5e7-e5fa-35c4-b98a-6ba68411c0d7 | -14.6241 | -49.7595 | 2025-09-21 13:30:00 | GOES-19 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 27cd961d-649d-3791-bb3c-92710d73ac08 | -16.0011 | -47.2757 | 2025-09-21 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b23c4eca-dcb9-3d45-9d43-a9f95b37c923 | -5.5959 | -42.1478 | 2025-09-21 13:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 156.7 |
| 5059c74b-d46f-3979-9d82-6258d65f4705 | -12.7114 | -46.8454 | 2025-09-21 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 2bd2a5ba-9b04-3c95-b1d3-7b86cadd1c8f | -14.8675 | -45.481 | 2025-09-21 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 500.0 |
| f6ba2535-571a-3423-ad99-e52b7eda744b | -12.6921 | -46.8482 | 2025-09-21 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 287.4 |
| b66b3121-746f-3daf-b370-77b9958c918f | -10.8805 | -46.6241 | 2025-09-21 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 9f2c6449-8cbf-3564-81d0-9dfd39c5412e | -3.8662 | -43.1087 | 2025-09-21 13:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |


[Clique aqui para ver as próximas entradas](README52.md)
