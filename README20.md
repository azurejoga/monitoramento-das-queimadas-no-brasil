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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86870f7c-ac17-3b6a-ae8e-ee2f8265451f | -1.5456 | -46.83 | 2024-11-28 01:10:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 2fc460ab-4b84-385f-92c2-aa79fb096c22 | -1.3145 | -51.9465 | 2024-11-28 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 92a4336c-28e8-3742-b265-cb9cf5bff626 | -1.3329 | -51.9463 | 2024-11-28 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 166a59a8-e6d9-3788-b13f-e70c1393f938 | 1.2537 | -55.9467 | 2024-11-28 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| add42e8b-cb28-325d-8c67-2c4bb40ad85b | 1.2538 | -55.927 | 2024-11-28 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| a81e8767-1907-3bc2-9ebb-1f3311bb90df | -3.9747 | -50.1962 | 2024-11-28 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d44c61bc-4f3c-34d8-8133-9ce5b53e94fb | -1.5897 | -52.2915 | 2024-11-28 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4907353d-7964-3027-83aa-40ee1f525d77 | -1.5898 | -52.2505 | 2024-11-28 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 9232cbe1-3d51-36bb-8a28-0d7063ff0839 | -1.5455 | -46.852 | 2024-11-28 01:10:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| eeec7dac-c5ae-3668-8355-f224c14e4d5a | -1.527 | -46.8303 | 2024-11-28 01:10:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 80661550-303a-373d-9915-04f58177a1bd | -6.1048 | -48.0327 | 2024-11-28 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| bc4951dc-ea66-32a6-b429-e0f7dc36d827 | -3.1114 | -53.8041 | 2024-11-28 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 8bf2121b-6eff-3a68-ae14-aef33bed6518 | -1.3145 | -51.9259 | 2024-11-28 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ba654bf0-7223-3394-af4c-44091d6ba4ad | -3.1113 | -53.8242 | 2024-11-28 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 8f0bb879-4bf8-3494-bc20-4885e0cbbf7f | -9.9086 | -36.4254 | 2024-11-28 01:10:00 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.2 |
| 28938cd6-5995-3bfe-b024-1283dac054d7 | -5.9788 | -45.3621 | 2024-11-28 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 198.7 |
| cbdfd204-18a4-356f-88b9-302e46ca7af6 | -5.979 | -45.3395 | 2024-11-28 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e7138b69-36a0-3a20-924e-68090d7d5abb | -5.9975 | -45.3607 | 2024-11-28 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a9084213-1497-399d-9dd8-e15d82cc0e65 | -2.5963 | -53.9771 | 2024-11-28 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8de082a3-717f-3976-9fe2-36b398ef6f1f | -2.8609 | -46.8626 | 2024-11-28 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 38d0eefb-3119-31de-8ffa-9f37df4d751a | -1.6081 | -52.2708 | 2024-11-28 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8dbaaa08-f2d4-35f3-b858-91f5cc8bc8c0 | -21.0803 | -49.8023 | 2024-11-28 01:10:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.0 |
| 691582e5-9b5c-334b-97dd-40af119d2b12 | -6.1735 | -42.6221 | 2024-11-28 01:10:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 41.4 |
| c093e761-5e57-316f-9f8f-c1707b5f2a75 | -2.8795 | -46.84 | 2024-11-28 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| e0ad7ab4-ae7b-380e-93e2-d1e91478083b | -21.0797 | -49.8253 | 2024-11-28 01:10:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.0 |
| f8835ca5-4a17-3492-bee9-1f18ccb498f7 | -2.8794 | -46.862 | 2024-11-28 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 72c0768a-6f48-31b8-91d5-98176b6dfd12 | 1.2537 | -55.9664 | 2024-11-28 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 5c1668d6-a2eb-3d44-8407-b3275dec4be6 | -2.6977 | -45.9384 | 2024-11-28 01:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| a0f72536-013f-33cb-907e-ca6d97a44610 | -6.1047 | -48.0544 | 2024-11-28 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 02ad85c1-4f31-350c-82fa-2da3e12534f9 | -2.861 | -46.8406 | 2024-11-28 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| cfdf923c-729c-3a45-b3a6-00461cf72981 | -1.527 | -46.8523 | 2024-11-28 01:10:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 7785908f-53e3-3287-ad19-ddc409b78aa6 | -3.0929 | -53.8247 | 2024-11-28 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| cfe525d6-b41b-3ddd-ba47-e60b5b1fb612 | -3.3312 | -45.4904 | 2024-11-28 01:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| afe377a0-3524-3f53-8e2f-3dde0e43ea5b | -3.1114 | -53.8041 | 2024-11-28 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b9fafadd-7814-3c86-abf9-d00e8b925979 | -2.8795 | -46.84 | 2024-11-28 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 0b58f5ba-a9f4-3a85-be6d-0244b0fd0ae3 | -2.8794 | -46.862 | 2024-11-28 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| f3ea6a99-db45-3181-968d-3eecea93d79c | -3.093 | -53.8045 | 2024-11-28 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d36daa25-7844-32c8-b2ff-c4ba86bfdc7b | -2.7234 | -48.9034 | 2024-11-28 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 229e9eb6-ec0c-3f48-ba0d-2a914c229a93 | -6.1737 | -42.5985 | 2024-11-28 01:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| 1dd70949-4bb7-3c05-a0f6-9ae16f2950da | -4.772 | -44.4434 | 2024-11-28 01:20:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 8c841738-382c-3707-8921-c716ccea6d55 | -1.5897 | -52.271 | 2024-11-28 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 193.4 |
| 8bc04e48-b20e-3b38-a923-4a9fdba1fd9a | -1.5713 | -52.2713 | 2024-11-28 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 196171a3-830e-350c-8d0c-87cb6f64b97a | -4.7908 | -44.4194 | 2024-11-28 01:20:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b88178a7-957d-3ce8-8207-381698f50417 | -5.979 | -45.3395 | 2024-11-28 01:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| b2010aac-ea57-3265-a5d7-423567c2b1b5 | -6.1041 | -43.9593 | 2024-11-28 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 4f2858dc-d660-36ac-932f-9fde271c2962 | -6.086 | -48.0557 | 2024-11-28 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e915212b-968b-3ae8-a543-b31a7d0e1776 | -3.1113 | -53.8242 | 2024-11-28 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 972e2249-5ab2-33f8-ab98-9059ebab6432 | -21.0803 | -49.8023 | 2024-11-28 01:20:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.5 |
| 234f338f-f75a-3b9b-bca3-f08f6c92106b | -9.0999 | -35.4249 | 2024-11-28 01:20:00 | GOES-16 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.1 |
| 92706a6b-9f4b-37db-a9c5-136d078e47b1 | -4.7722 | -44.4205 | 2024-11-28 01:20:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 221c3b21-14cf-30e3-bfb7-e97df39d9f34 | -21.0797 | -49.8253 | 2024-11-28 01:20:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| dd7bb038-c7da-3627-bc54-c0c6ee96b2d2 | -6.0862 | -48.0339 | 2024-11-28 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 168.6 |
| b1c9f64b-b8fc-3f9a-882c-c7756ff3c616 | -1.5455 | -46.852 | 2024-11-28 01:20:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 2ab8bc4b-e55c-3087-8da3-0dacb51e5fa9 | -2.8424 | -46.8413 | 2024-11-28 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 73dc8436-67e1-3fd8-aa79-8447addce9bc | -1.6081 | -52.2708 | 2024-11-28 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 2a508cc9-d8de-38ef-948a-24a86944b464 | -4.7723 | -44.3976 | 2024-11-28 01:20:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 0a898570-44c6-3022-b4d9-9c70c4ba5710 | -2.861 | -46.8406 | 2024-11-28 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 3dd36c88-d0b7-3081-9012-70fc7c843412 | -1.3329 | -51.9463 | 2024-11-28 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 2668ab03-396a-3870-8b18-6cfa185f0182 | -3.9674 | -48.0851 | 2024-11-28 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5ed4dd62-63eb-37e0-b9d4-ec12dde96187 | -1.5714 | -52.2508 | 2024-11-28 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 05893a35-0a88-301e-94de-5a1cbe7e2732 | -3.3837 | -50.1125 | 2024-11-28 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 133d1f6d-0d2f-3ca3-beba-12499b7babac | -6.1048 | -48.0327 | 2024-11-28 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 4e785a69-623a-33bf-ade4-74dfee7df067 | -2.8609 | -46.8626 | 2024-11-28 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 81454e5e-4454-3aee-bf6c-883d647440d1 | -6.1735 | -42.6221 | 2024-11-28 01:20:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| a46c3399-ca71-33fd-834b-cf89527a770c | -5.9788 | -45.3621 | 2024-11-28 01:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 07310841-51a4-3e70-892e-05ff3f770327 | -1.5456 | -46.83 | 2024-11-28 01:20:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 21379b17-2353-3707-b635-5386920f4920 | -3.0929 | -53.8247 | 2024-11-28 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| ae6e0fbf-7bf5-3be5-acda-9168bc8229de | -2.8423 | -46.8632 | 2024-11-28 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 0099abe5-15ee-3f89-bf6e-edceadbc7844 | -1.5898 | -52.2505 | 2024-11-28 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 30d6882b-cdb1-333d-9074-212a0616fd75 | -18.784 | -55.8416 | 2024-11-28 01:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.4 |
| 6258a12b-3206-34a0-b6a0-23a529578a8d | -6.1039 | -43.9824 | 2024-11-28 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 72fdb026-52d0-3c08-a726-2d1e1a900ae3 | -3.9747 | -50.1962 | 2024-11-28 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2359ed22-336c-3b13-89a0-b97b9c2034a3 | -1.3329 | -51.9257 | 2024-11-28 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| be911b92-1377-3970-8db3-d2c5b9d6cea2 | -2.5963 | -53.9771 | 2024-11-28 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 482109c5-84d8-3f5c-a095-0c692c2d9491 | -5.9975 | -45.3607 | 2024-11-28 01:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 7cdbdf18-aadc-3542-be28-bf47d83f5fb3 | -1.5898 | -52.2505 | 2024-11-28 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 1cbfa48e-140f-3db8-905b-73a4da69e895 | -2.8423 | -46.8632 | 2024-11-28 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 04446c06-b15c-37c7-8596-239aed416d0a | -1.6813 | -52.4537 | 2024-11-28 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 5c4f4f13-7128-3568-a170-c3b78aa6143a | -1.3329 | -51.9257 | 2024-11-28 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 79345ab2-f2dd-3fd6-8a97-5c04e1d7d1dc | -4.7908 | -44.4194 | 2024-11-28 01:30:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 82b4a2b7-447d-338b-9358-ddb3384a69e5 | -3.3312 | -45.4904 | 2024-11-28 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 7a5d8236-579d-3089-8f28-b1c80a19983c | -5.9975 | -45.3607 | 2024-11-28 01:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| bce7c0b5-44eb-3c8d-8301-7e20aa04fe04 | -3.1114 | -53.8041 | 2024-11-28 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2f2334e6-753d-34a4-a200-24be482a6d27 | -3.1113 | -53.8242 | 2024-11-28 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 2ffa797f-5ac1-3f97-8500-9df370a5f9cb | -3.3311 | -45.5129 | 2024-11-28 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ee0c4bcd-3c4d-37f8-9090-7098051f0030 | -1.6629 | -52.4744 | 2024-11-28 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| b1455ac6-29ab-33c4-ac6d-ceea86a97d34 | -6.1048 | -48.0327 | 2024-11-28 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 02ae607e-0e84-388f-a62b-3266dca6828e | -2.8794 | -46.862 | 2024-11-28 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 48a8880d-57cc-35a5-9240-ebd897680c55 | -5.979 | -45.3395 | 2024-11-28 01:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| a23b7e0d-7d35-315d-b523-1684c3b21fed | -6.1041 | -43.9593 | 2024-11-28 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 69a6c4aa-b3bf-317d-a2db-5cb9b8f46494 | -2.7234 | -48.9034 | 2024-11-28 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6ff63c8c-df5c-3aa3-9c28-9409c7ef9af0 | -1.5714 | -52.2508 | 2024-11-28 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9a3af877-9d0e-3b8d-899c-23ee7747edbc | -3.9674 | -48.0851 | 2024-11-28 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a8f64204-d577-323a-9037-d707cfa6c5f6 | -6.1047 | -48.0544 | 2024-11-28 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 87c9559b-08db-3ce5-9f66-9f97109d8658 | -1.6445 | -52.4747 | 2024-11-28 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d6239e0c-f175-3fec-9830-033ed036f648 | -3.9748 | -50.1752 | 2024-11-28 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| dba47ce5-3fb9-3567-9b8e-1699a2641ca0 | -1.6812 | -52.4742 | 2024-11-28 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 5e0d3161-1693-38c2-8ef9-c8aee7bf9f0e | -2.8609 | -46.8626 | 2024-11-28 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| cabcb842-4b6a-3ac9-a5b4-9f07fa16167f | -6.1039 | -43.9824 | 2024-11-28 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| a5c63fe6-5de0-3d9e-a38b-f212dbfbc536 | -1.5713 | -52.2713 | 2024-11-28 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |


[Clique aqui para ver as próximas entradas](README21.md)
