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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76bb0c03-f3d2-369a-a5d5-642cad98235e | -5.84979 | -50.07339 | 2025-10-10 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbdcb5ca-c4e5-3f20-b86c-e739192b4c24 | -7.78207 | -44.06017 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8621a79-d3d0-3bb6-84b9-2f36b2c977df | -5.42297 | -41.72914 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 207afc94-2902-340d-887d-ba6fde60a642 | -4.94933 | -42.81779 | 2025-10-10 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| df5288e5-7678-3a90-9871-b3c2cba59c53 | -5.90537 | -42.85701 | 2025-10-10 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 454bd00e-3aa7-358b-b5b2-ac20efe29bea | -5.39896 | -40.97929 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c385b96b-4c78-3bbd-ae94-0a88658f89c0 | -7.24555 | -49.5164 | 2025-10-10 04:00:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c88857df-0a31-35b3-bfdc-65d2c0b34e8c | -6.57329 | -43.93324 | 2025-10-10 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a34b3488-b981-3312-ab64-ff86dddbb0e2 | -8.39928 | -39.71174 | 2025-10-10 04:00:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 294deef2-aca4-3b67-967b-1601da5b9a48 | -6.01721 | -45.88008 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efc168be-bd40-31de-b602-506a967892c7 | -4.55877 | -46.69181 | 2025-10-10 04:00:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1baa935b-c9cd-3dd6-a4c6-2986df4e0751 | -7.07959 | -43.51712 | 2025-10-10 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ad0650e-03d7-3457-a8b2-3885f2720a0c | -4.6491 | -43.19687 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3928d55-4e1a-3896-8217-c0c125f4a65f | -10.16049 | -44.59893 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a442a234-2c1a-347f-b112-6f7caf59f6e4 | -10.15891 | -44.60839 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 56fd186c-037e-33c9-99bd-e9f808e567a0 | -6.59106 | -44.625 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ca5dbbaa-efe9-337f-89cb-8536c18ff1ac | -6.5179 | -38.7139 | 2025-10-10 04:00:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3cb5f556-688b-33de-a0fb-ccd81deb9f6e | -7.21174 | -34.90685 | 2025-10-10 04:00:00 | NOAA-20 | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8cc7c46f-5087-31f9-a338-800887c35fc7 | -10.15673 | -44.5983 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cd7e8378-910c-3df7-9636-971f5c9783a1 | -8.50902 | -46.16809 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efe6b3b3-196b-32c5-90c4-6ae5c771cfdc | -10.25759 | -37.86724 | 2025-10-10 04:00:00 | NOAA-20 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e2bc84c-4cf7-3705-974f-ce2ad298f5fe | -5.65027 | -45.96773 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 841d054c-960c-3946-9682-62e09f65a018 | -6.58623 | -44.62938 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6242a60f-b35a-300d-9627-4487f86dcc65 | -8.51327 | -46.16886 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65c6d345-f243-3571-b9e3-1b9cf6dac1d3 | -6.5902 | -44.63005 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e39d76d6-86b3-318b-b5eb-fa2b8e7adf25 | -5.33701 | -45.56981 | 2025-10-10 04:00:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5faeae8d-d19c-303b-9fdf-f8a1b705479e | -8.21052 | -43.35889 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65f9bcdb-a192-3a99-b541-ce5a351c4a68 | -7.77699 | -44.04225 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18718b5f-1463-3557-a5fa-6c3c8d681765 | -6.55227 | -39.98769 | 2025-10-10 04:00:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b5ea8e88-85dc-30d6-af2a-5e8c970ac248 | -8.50619 | -46.15925 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a59ca70-44c8-3564-b99f-b4ec8bfe9a2e | -7.06702 | -46.85473 | 2025-10-10 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6f777c6-99a3-36ad-a22c-afa9c3b6d4e8 | -6.75676 | -42.82981 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 19676e9b-36e8-3ad5-9367-f9a76b0e7376 | -7.78662 | -44.05614 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8af688aa-2bcc-3f7b-baf5-bb7ebae3569a | -5.4257 | -41.36096 | 2025-10-10 04:00:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| edfc11ce-7573-309e-95f6-9e106e338d10 | -6.09956 | -42.65783 | 2025-10-10 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f24f454a-6c26-39e1-ad15-143418aadb45 | -5.99367 | -42.48349 | 2025-10-10 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38a77219-febe-3b59-b123-f188e8af7d76 | -7.14121 | -42.20382 | 2025-10-10 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8ca506f6-44cd-3cec-ad27-35644dd269ae | -7.45338 | -47.18459 | 2025-10-10 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e02d106-1e32-34e8-ab72-eee19a3e95ae | -6.6617 | -41.98385 | 2025-10-10 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2ea8e45f-0087-36d6-a508-6dbc5794d1be | -7.41528 | -45.91883 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 85de68b0-1cd5-367f-8bab-8d67fabf3871 | -5.85009 | -50.07304 | 2025-10-10 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58003ea9-011f-3c05-97a2-1b497dca5f19 | -7.49858 | -42.74449 | 2025-10-10 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a5a0bad9-42d1-3560-8dd7-b7036b9defc9 | -6.71058 | -42.19921 | 2025-10-10 04:00:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| eb434312-a076-3776-93b2-a545520ea6fc | -6.74737 | -42.81981 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 103474b9-16ad-3aa2-9e6d-49359472c3a1 | -7.2596 | -42.96556 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 484206c4-b7f3-3cf8-8d1a-1ceaa230a1b2 | -6.58084 | -44.62181 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f858ba7d-540e-3357-837f-cb35a4670715 | -6.34244 | -43.75591 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 886a8692-1073-395a-ab2e-5d9ba48aa589 | -8.1308 | -42.44305 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1a5a69a6-2676-39c5-aa31-6afb73fb24d5 | -7.63185 | -43.05579 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 170c563d-8583-3fd4-8204-1e27a48e948a | -4.8196 | -47.34763 | 2025-10-10 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e8e983a-001c-30b5-87ab-49e34833079f | -9.66362 | -43.84698 | 2025-10-10 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e88373c-742b-310f-81aa-beacf3b5e6df | -8.89193 | -46.01508 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f343aeeb-8913-38c5-a11c-4dbc245a59ff | -7.5406 | -44.2946 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d70bd3e0-b068-3b30-ae4a-3ae5d087061c | -7.77019 | -42.41332 | 2025-10-10 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6b086d6-074f-36de-80ee-8dd3514698cb | -10.45693 | -40.53642 | 2025-10-10 04:00:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1c856c70-95f4-3f86-9f2a-5fb50e0f272e | -7.40964 | -45.92618 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b48c105-7b82-31a9-972a-e721cd6a4114 | -8.00695 | -43.7547 | 2025-10-10 04:00:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 18513c34-8b8d-3daf-8ab5-10d58846496e | -7.41459 | -45.92287 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9b39db07-e6fe-3461-9a03-cefd4f4e4988 | -5.33077 | -44.81765 | 2025-10-10 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3e817ce-435b-3953-a7c2-d4444afa6bc8 | -7.77619 | -44.92246 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52831b0b-3f9f-3f4d-be97-72c62e88e74b | -4.85244 | -42.76821 | 2025-10-10 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a862757-2cd5-3a4b-9094-5423d0989bd2 | -7.20092 | -45.49084 | 2025-10-10 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae7fae87-51c1-3a65-984a-65613323868c | -5.76877 | -42.39582 | 2025-10-10 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 11aea286-973e-39f1-a739-f99b111c68d6 | -4.84469 | -42.93017 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 12514297-65a7-34b4-b2be-553bbc44a88c | -5.33336 | -45.56505 | 2025-10-10 04:00:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c23e61c0-c175-30f6-adfe-d5aaaf77b580 | -6.73441 | -42.80929 | 2025-10-10 04:00:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ea43adce-eebf-3232-b316-823a9d0671be | -7.79608 | -42.61293 | 2025-10-10 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9811e6d9-d0c9-3487-a96a-2e9a2d270f33 | -6.75028 | -42.82452 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6b0a51fc-e4a5-3ee2-a5e4-12c4775ee43f | -7.20955 | -44.96475 | 2025-10-10 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ac15641-2876-301d-b4db-4df837af2f77 | -8.14944 | -42.44944 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a4e97538-2de3-32f8-83e2-52c22e399af4 | -6.57917 | -44.62296 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9975c9d5-239f-357f-a9f9-dc8823684260 | -7.14592 | -42.19673 | 2025-10-10 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f773b711-af93-3212-8fa1-888165733bc8 | -9.52484 | -45.21994 | 2025-10-10 04:00:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c65b8a2a-9452-3708-9726-5183a0f55eea | -5.40791 | -40.98814 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| e5a217dc-017e-3b70-81bf-fec0581cfa50 | -7.40536 | -45.16356 | 2025-10-10 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6bfb3900-69a9-3da9-905d-8cef5d82e340 | -6.66049 | -41.99132 | 2025-10-10 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 764c266c-1d68-3b7f-b638-4f10e817814e | -9.71878 | -45.92557 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 377c3896-733d-37bf-922e-ca20b5754906 | -6.58398 | -44.62756 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b7feba39-9981-3d6f-b00b-5fb1cbf45265 | -6.7541 | -42.84628 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a4e58e6e-f29b-3cf2-a86a-613ceb4767a2 | -4.84163 | -45.411 | 2025-10-10 04:00:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fa1a610-979a-357b-aeda-d54dd425cd95 | -6.81514 | -42.80051 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 53a1e6a9-abff-364a-a013-2df891fa0645 | -5.97957 | -45.91716 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40419d46-90d4-3a21-a48c-75cbd439c5ce | -7.84295 | -44.55165 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40becc5d-8ae6-36b8-9418-459e5dcd2fe3 | -8.04335 | -43.91455 | 2025-10-10 04:00:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f67e0997-f9bc-317a-9ecd-2ae92979e06c | -7.13376 | -44.12914 | 2025-10-10 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ecbf4293-07f4-38a7-8baf-312a79e68c1c | -8.16913 | -43.31764 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9f41f7b9-ce52-3b80-9572-f10a54d1a2fb | -8.20466 | -43.34939 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 7b655a0e-c42d-372c-80c9-e4643fad320a | -6.57918 | -44.63194 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f77cfc1-da4c-3ad5-949d-3d447363f54f | -7.62828 | -43.05515 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ff886dbb-9630-3ed9-9143-e3c30bd592de | -6.74023 | -42.81863 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 90135e4c-29e2-3f2b-a3d6-6750cc91aa25 | -7.78285 | -44.05553 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e47093f-226e-3a4b-9127-5135acce33c6 | -7.57384 | -44.37918 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac94a61e-a6c8-3a9d-900f-50276f075d7d | -9.65925 | -43.85067 | 2025-10-10 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2446cb16-3f50-3835-828b-dd7de00cc9d2 | -6.45528 | -44.57749 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76f94662-1831-3c3c-b191-32ed7a57b5dd | -7.4139 | -45.92695 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3166db3a-cd47-3110-af67-8bcc987d506f | -7.13299 | -44.13371 | 2025-10-10 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce3e16cf-6743-3b3f-a044-6b3395b3533f | -6.64081 | -43.68522 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db446091-4357-3722-973b-342e92602d1d | -8.89744 | -46.00816 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 492a1582-a18e-3cda-88e5-d149e18992a3 | -7.78054 | -44.1842 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcf9dfd9-6e04-3152-bff0-a3bb64f39f0a | -6.08765 | -42.55178 | 2025-10-10 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README23.md)
