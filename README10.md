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
| c7862b93-a5bc-3b7f-bac5-5dcb4f2d1b66 | -23.25923 | -49.49627 | 2025-05-28 04:14:00 | NPP-375D | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 2aa37e27-38e9-3ef8-bb66-e2e3a2176de5 | -7.695 | -46.0978 | 2025-05-28 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| fc8a3379-e4b5-3985-8b9b-10e78af4c634 | -11.818 | -44.2703 | 2025-05-28 04:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| fcaec685-b031-3187-af79-1378bb563c55 | -7.6762 | -46.0995 | 2025-05-28 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| e9b29031-0b58-3962-bc3e-9c69375fc45f | -6.05692 | -44.04356 | 2025-05-28 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dd7378b-b633-3cd7-8c68-7d62860b6122 | -5.76151 | -43.48291 | 2025-05-28 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02f32c98-ab40-38d0-8c92-a0e8ffee0999 | -4.43089 | -46.10675 | 2025-05-28 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74cd3419-acda-3948-ad1a-9180e4deacbb | -5.96782 | -43.75615 | 2025-05-28 04:29:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cde240d-a724-343d-aef6-1969935d3415 | -6.20676 | -43.34723 | 2025-05-28 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 694a21f4-12f9-3ca2-a6b2-98a1ea9ce81a | -6.33104 | -43.37313 | 2025-05-28 04:29:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74e48c73-7e57-370d-9d87-68f93bc8dfbb | -6.1202 | -43.95165 | 2025-05-28 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a62a18ce-f06b-38c1-8db9-5d1801a33887 | -6.162 | -44.41809 | 2025-05-28 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b36ff19-ec65-3f98-928d-457fa9c54ded | -5.64915 | -43.58818 | 2025-05-28 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 087d350c-379b-354f-a63a-b8295b44eb52 | -4.42226 | -47.95087 | 2025-05-28 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da4c1353-9ba7-3075-8485-5fa0eae561b6 | -6.54294 | -44.0206 | 2025-05-28 04:29:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53207c81-43aa-37c3-aff5-7be21fea9445 | -6.12394 | -43.95223 | 2025-05-28 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e582412e-f90e-3187-a29a-cf5fe5293280 | -5.78346 | -43.61823 | 2025-05-28 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a8f3bfe-2829-3512-a832-00b9265cad19 | -6.3194 | -43.37133 | 2025-05-28 04:29:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 056340ad-57ba-3932-a0fc-6d6cf95c44b2 | -6.32328 | -43.37193 | 2025-05-28 04:29:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43031f91-6c96-3674-9190-9e19fbe9af01 | -6.11714 | -43.94658 | 2025-05-28 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 292bf5f6-c2c0-3801-b0ee-ea185c02609a | -6.32256 | -43.37675 | 2025-05-28 04:29:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35f7a7f6-8619-322b-b5e0-e5601d5d91fd | -6.50739 | -43.64007 | 2025-05-28 04:29:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae485a12-2275-3f42-8ec0-a9cba3da695f | -6.21378 | -43.35341 | 2025-05-28 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1ebb706b-6912-3c6e-8a1c-60d45a7e3cd2 | -6.15836 | -44.41748 | 2025-05-28 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea6c074d-8755-30c1-a0a4-6c8a104cf15c | -3.12839 | -40.98831 | 2025-05-28 04:29:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 85238421-d552-3d14-91ce-612d81503e23 | -6.31868 | -43.37616 | 2025-05-28 04:29:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f4a97e54-36b7-3d98-9dd8-75e7d3702254 | -3.83564 | -49.06044 | 2025-05-28 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 288a345e-3aad-3e61-a0ab-688e50c74a04 | -6.33177 | -43.36829 | 2025-05-28 04:29:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a97e380-9471-386d-91a1-2b073776b19c | -2.50152 | -54.12934 | 2025-05-28 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ec6ddc4-3d7e-33f4-8b1b-3cbc52cadb51 | -4.48495 | -47.79053 | 2025-05-28 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 762182fb-c8e1-39ef-9984-0f655a1ee55b | -4.41894 | -47.95034 | 2025-05-28 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8adfcafb-648b-3ef1-a10a-bbd01a727d7b | -5.96852 | -43.75154 | 2025-05-28 04:29:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8becdcf4-7f7f-322f-b0e1-a874ecff5fff | -6.63065 | -43.2156 | 2025-05-28 04:29:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 05c8ac77-5db1-3a87-bb64-3efcd8e43853 | -3.13273 | -40.98896 | 2025-05-28 04:29:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8d9889e4-ac32-3cfb-94ac-c6e1d216fb3e | -5.78047 | -43.61503 | 2025-05-28 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0467aa4-398b-3f74-beac-80673b2630e6 | -5.76915 | -43.48416 | 2025-05-28 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 399eee79-cffb-3013-8f45-bcda1ab9c7bf | -2.49977 | -54.12603 | 2025-05-28 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32d166ff-e45c-3eae-be37-abcd5f053d3e | -5.60539 | -45.74562 | 2025-05-28 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 589e3881-9c45-3016-a5c1-34d9d86b2282 | -6.12089 | -43.94709 | 2025-05-28 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6195f436-6ad8-3ea1-8efb-7aadef516d39 | -6.63137 | -43.21064 | 2025-05-28 04:29:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d48eec72-88ff-316e-8a8d-a034b6a9aabc | -6.21452 | -43.34849 | 2025-05-28 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| f14eae36-d325-3ef9-85e5-85f6b07af638 | -5.76844 | -43.48887 | 2025-05-28 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d620489-1366-3bd8-9082-8ceb4fbf8b72 | -6.21064 | -43.34785 | 2025-05-28 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 190b1c98-a531-3a8a-b063-3f105b71a749 | -6.06947 | -45.93705 | 2025-05-28 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d8a16c2-0a1e-30de-b76c-583da4a092ff | -5.78356 | -43.62022 | 2025-05-28 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5d0eb38-1931-3013-ace4-c2ff50000849 | -6.33565 | -43.36886 | 2025-05-28 04:29:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab8de35d-f296-3251-b827-bbc132787099 | -5.89891 | -46.22461 | 2025-05-28 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e005e7e-2fd6-3fcb-9d40-f9f52cdeacb7 | -4.43235 | -46.10984 | 2025-05-28 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7ffa70c-c11c-3999-b6ac-bcd7eddfc3ca | -6.03131 | -44.05061 | 2025-05-28 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01b28423-cf04-303e-8a9b-c0e6772b44f6 | -5.9723 | -43.75208 | 2025-05-28 04:29:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea42d8c3-b5f0-3ddf-99c7-e5e30d84a4a6 | -6.26872 | -44.20306 | 2025-05-28 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e1807ac-b74b-3e66-897a-c0d4ce72ae0b | -4.156 | -48.85635 | 2025-05-28 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f77348c-b5fb-3ce4-a3ca-30ec7ebbd051 | -3.81208 | -48.98907 | 2025-05-28 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5cce1e8-8009-3f4b-acd4-6f5c5b84ef1f | -5.64845 | -43.59284 | 2025-05-28 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad752fe0-0089-3e69-924b-c3d6cc5f00c1 | -5.76222 | -43.47819 | 2025-05-28 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d370c8e-0b8b-3840-bbdc-45cc37d05f53 | -6.32716 | -43.37254 | 2025-05-28 04:29:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 370f6a89-813c-39ce-89d2-be09f8f6d308 | -6.3148 | -43.37555 | 2025-05-28 04:29:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7e19de3b-f098-390b-a109-65249b570abc | -7.6762 | -46.0995 | 2025-05-28 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 991a1cef-0059-3298-baeb-0abe038432b0 | -11.818 | -44.2703 | 2025-05-28 04:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 87923148-f9bc-3a35-b98a-b4a5716bf0d0 | -10.73139 | -49.29338 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4085b52-a7af-30ee-b21a-ccf9f0450305 | -12.08275 | -54.58432 | 2025-05-28 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30ab56a6-d651-372c-8a66-f5f1affec05b | -7.18564 | -43.11454 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 820861c4-8230-32ab-9173-77e0d84c4b79 | -11.29683 | -54.01229 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60ba0d06-ec2c-3b98-8b6e-d1b127cffa23 | -11.39597 | -44.83328 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1069a26e-5bf6-3fe3-9a46-6c92d66eead6 | -12.25222 | -53.27728 | 2025-05-28 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e69d801-b5be-3f6e-93cc-f631aa4497b4 | -12.63647 | -49.89496 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3731e665-6f46-3343-bca8-9348e34021b7 | -8.09461 | -46.29207 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea87d0b6-737a-3441-9a68-fdc78322fdc8 | -10.58206 | -48.5187 | 2025-05-28 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40a9e36f-718e-3850-9ade-51fed95ce474 | -10.65908 | -49.4477 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f719f65-b71e-3e33-af2e-32eddcdfe20b | -10.94945 | -48.14496 | 2025-05-28 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 208e59fb-b20b-3d0d-bfa4-2cbf3547b2c1 | -11.14449 | -53.93096 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d35d2bb-d439-3319-935a-197e05394355 | -11.29222 | -54.01513 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3481f789-3805-3160-b69b-4c63abdeaaf7 | -8.0075 | -46.15405 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c45fb14-06a5-3fb5-ade4-fe1ce42e8efd | -7.99721 | -46.15235 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f62dbc0e-3052-3a43-82bd-b1e5a95d5dca | -12.60225 | -46.73405 | 2025-05-28 04:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48d8dd59-1f07-334b-912b-6a2d93b15141 | -12.11046 | -54.66729 | 2025-05-28 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b24dc20-899a-39ce-9c70-5b7c72d33f64 | -7.21864 | -43.1123 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0fe0304f-98ad-3981-932d-bf4edd7d7051 | -7.56705 | -43.32512 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8922371-4d2f-3852-b728-61fb384eb0ce | -11.29365 | -53.98262 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd5f4ca0-9952-3ad9-ad1b-21dbe944eb02 | -10.22818 | -47.42935 | 2025-05-28 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4789d02-ccaf-396e-9d09-e8a6b56c3d6c | -8.39693 | -47.09938 | 2025-05-28 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d3abaf8-c9d4-3103-bd53-b00a6fd7b5d9 | -7.57101 | -43.32574 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9f9c6fb-7eb3-37ba-82a6-977c8ad27575 | -9.03876 | -47.74956 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4be6a249-8111-3a2f-8b58-352f1399f2ca | -12.82277 | -47.39472 | 2025-05-28 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b3f28a1-33fa-3053-92eb-b5f303c4162a | -8.02097 | -49.68696 | 2025-05-28 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae96e3ea-90bf-3b9d-8aae-b716dcb51372 | -12.4092 | -49.99616 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af6b6d5c-d2cc-35ed-ba8d-aef162399ba3 | -7.97714 | -50.70854 | 2025-05-28 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1cad3fe8-c1b1-313f-97e5-93f7a9b53dc1 | -7.6705 | -46.09166 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eb23f55e-d8f1-394d-8291-c3a02ad25b3f | -7.97048 | -45.93451 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11409ade-8eb6-3a0d-8fb1-f8607a280bd9 | -6.63443 | -47.34008 | 2025-05-28 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd29d54d-36e9-33de-8bdd-e26fb1c5f9b3 | -6.21294 | -48.48468 | 2025-05-28 04:32:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 377de07a-33dd-36ae-9ed1-f6982ad5494e | -7.20164 | -43.11685 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4e8c1d60-730b-3740-b95c-2f4be8d2fee8 | -11.9137 | -54.40769 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b91d2f83-072f-3880-83dc-2a3c8498c758 | -8.17608 | -46.49434 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 474d227b-0902-3163-aee8-0d4d683aadcf | -9.03376 | -47.73796 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3cdf78b-87fb-37a0-9f87-624d561115b5 | -7.68424 | -46.09379 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| afd341e4-8714-3c64-b60a-5931e81fc54e | -12.11525 | -54.66428 | 2025-05-28 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a85d6582-f6a0-3ce8-b649-866eb4ffcb33 | -12.41253 | -49.99671 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca89dbc1-b519-30d4-aff1-f58672b026b7 | -7.3428 | -43.68394 | 2025-05-28 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 491b0311-e9a7-349e-bd8d-d375a01a941f | -11.81673 | -55.07222 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |


[Clique aqui para ver as próximas entradas](README11.md)
