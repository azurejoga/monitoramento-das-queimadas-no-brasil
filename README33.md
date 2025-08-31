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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5df7de0b-22a2-395c-ad71-931a2964d18e | -6.77211 | -44.83186 | 2025-08-31 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2df0375b-3892-3960-ba24-750e2b9d4166 | -6.16602 | -43.32141 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| fcff2a58-9543-3e44-aa5b-1e10c26caa1e | -5.48152 | -44.40203 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac43ec5f-ea92-378c-8f66-800508e54009 | -6.58242 | -43.68618 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 95d40641-ff88-3294-aa18-651433e78b56 | -5.25054 | -44.45176 | 2025-08-31 04:27:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92d3b730-3064-3872-83f4-d22705ae6905 | -6.12968 | -42.94735 | 2025-08-31 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| bc69a88f-3bd9-3210-8c62-4912f43e110f | -7.73557 | -44.01234 | 2025-08-31 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddc814e1-2186-3833-806c-d3f54c00a764 | -6.17889 | -44.13297 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebb07102-b042-34ed-8d24-b87099d4efcf | -7.75283 | -47.44489 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d6e4faf-bc3a-3b5d-aea4-52b27d7deb9c | -6.83021 | -43.33571 | 2025-08-31 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b5a61ea5-2eb4-3888-9213-1f69150823af | -4.3112 | -48.1018 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 572d0738-bfb5-3eb8-b204-ffe7f1497076 | -6.18201 | -43.33621 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 756e8e44-b1b8-33f1-9941-f906f7d6abec | -9.11692 | -45.21049 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac2cd6b0-6b3f-316a-93bf-938385491fb4 | -7.75725 | -45.45633 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a07ecb8-e9a1-3e34-b193-197c6d3ea76b | -8.73043 | -50.37189 | 2025-08-31 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cbb8dd9-e831-30bf-8c32-0d15964e8e2c | -6.17214 | -43.99271 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 143be54b-34b0-3c43-b9a8-1fdc68b44093 | -5.48826 | -43.19288 | 2025-08-31 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e67eb416-3974-3a11-87a4-9dde28d9bfc3 | -6.25341 | -43.38712 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95d1a4fc-64d7-3175-a4c4-61ae7149ce7b | -3.58851 | -47.52032 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d22e1e7e-bae0-3e66-934b-79def9c6b04e | -7.10921 | -44.31637 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36b32864-4e81-3e79-a34e-2a3b03e11dfb | -7.22786 | -44.22581 | 2025-08-31 04:27:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14542440-0241-326f-b7da-57e1e4ded05f | -6.8176 | -43.34629 | 2025-08-31 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 00085cf4-73bf-35a5-afc0-98fc83a7bba8 | -6.30647 | -43.53845 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 245afe3a-e8b4-3395-93b0-e07f0c07ecb8 | -7.64589 | -42.65263 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d8b1303e-2e70-3be2-bbcf-fa357cdd9299 | -7.6412 | -42.65432 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 87fd7795-a0b6-3b61-a5f3-20cefcf97e91 | -8.19202 | -42.31996 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 91418b05-573a-3309-81d7-dbc1c1ef3512 | -6.16164 | -44.1304 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27d02447-1266-3625-9c66-f7d8f1e1b160 | -7.36975 | -43.4114 | 2025-08-31 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0def8317-30e1-3b3f-8bd8-cd139283c65e | -8.96853 | -48.19184 | 2025-08-31 04:27:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8670d74-f7e9-346e-93ce-9ef232e277b5 | -7.38974 | -46.66037 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ae45c8e-d825-34cc-b33f-50c1040649eb | -8.08978 | -43.64596 | 2025-08-31 04:27:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab38d55a-f074-35b6-8cfc-9d5ec2d116cc | -5.82011 | -43.86333 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a9f0759-c43d-379c-b1b5-c2593563f3d5 | -6.51653 | -42.9485 | 2025-08-31 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24658196-b732-39e2-9813-a78e1d3d561d | -6.44604 | -43.9639 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3baa9e64-002e-3569-a7f4-edbb3f40c026 | -4.40411 | -40.69209 | 2025-08-31 04:27:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 91113c53-b658-3fd2-a532-a51c1517f5da | -6.17825 | -44.20549 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1897856e-d4c5-3226-ad87-b61637f9b0a0 | -3.04697 | -47.01808 | 2025-08-31 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c75bf832-a9f5-3427-b086-0a17483e13a9 | -6.54214 | -44.58131 | 2025-08-31 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| effd30f6-9a57-32f9-9160-a8950064746c | -6.88807 | -44.44084 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a84e61d5-8bc8-3e17-b2f2-2ae121124dc4 | -4.27217 | -40.93784 | 2025-08-31 04:27:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 146690d7-5642-3e3b-8788-9a849082b516 | -7.9541 | -46.38633 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9119d18-72d5-3063-b944-f7d9dcd32dbb | -7.58564 | -42.69214 | 2025-08-31 04:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc1c3282-7907-38a2-8f6c-f32e902c4d71 | -6.31363 | -43.53398 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebf2c2c7-932b-31aa-a239-695dbabb1217 | -7.64213 | -42.65207 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 770ba07c-0c6b-3de8-9d0e-69dc8a526dce | -5.80564 | -43.86496 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b575ccb4-8e4b-304a-802f-da3717fa1417 | -7.12492 | -44.60079 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4620ac52-902c-3cea-a7f7-ea7d7b3c03ea | -7.63675 | -42.65833 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 806943d2-e0f8-3b89-acd1-11cbed208344 | -3.81646 | -41.55176 | 2025-08-31 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0155722c-3c22-3577-9bdc-bfc1648a11ae | -8.54786 | -51.30597 | 2025-08-31 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6b140948-0707-324e-bbe4-74d368c1398e | -7.96743 | -46.40977 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a2d792f-e61a-313c-b91d-a42ffc40856a | -6.58121 | -43.69403 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1bb76f49-6cc0-36ef-822d-69772f2ea21e | -7.57859 | -45.11757 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 219b3c22-662d-3377-a569-15c8d67284c8 | -7.12493 | -44.60136 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94d3a0e2-38d7-3a8b-b2a2-7ec5e1c29189 | -6.57828 | -43.68964 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9c7a4170-83b5-3f41-8131-e4986faed7e7 | -3.80021 | -47.57199 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1de71c56-0248-31bb-89b7-69be76e67559 | -5.80623 | -43.86115 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70201abb-58c3-360e-ab82-f5f86fb1ab12 | -4.74043 | -44.45156 | 2025-08-31 04:27:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96acbac2-8f05-38bb-a64e-9119777dec41 | -6.14038 | -44.13099 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 846e53b7-c8d4-3821-9e11-7adc47f9c5a2 | -5.13892 | -45.03595 | 2025-08-31 04:27:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a860339-e2f0-3d37-979b-ea3036bca01b | -7.67221 | -42.65642 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e4d62e7a-bb84-376a-82d2-718228c7da43 | -7.40657 | -44.08843 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a20c4d81-59b2-32a1-b7e6-813ffe8ccc68 | -6.51573 | -43.5361 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc28d85e-01f3-30cf-a8d6-2234a4168a52 | -8.8777 | -45.08799 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9bb5502-3b6f-3e2d-94bc-a9e251256a55 | -7.44477 | -44.81091 | 2025-08-31 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 689b409d-37e1-313d-9114-c96289d5bcd7 | -7.40777 | -44.08069 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ddb7b8d-480e-305a-b28a-e9952b437189 | -5.54867 | -43.73736 | 2025-08-31 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fa8a38c-7be9-3ab6-8f9d-81c8e049772d | -7.48727 | -45.05895 | 2025-08-31 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dca32f52-271b-354e-94e8-2d79223748e3 | -5.69182 | -45.95378 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4da2f7ef-f867-3a4f-a151-279ae2c8e85b | -7.37818 | -43.40435 | 2025-08-31 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 848433a5-e875-3102-8b76-055132805700 | -6.2917 | -43.54034 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5992bcdc-838b-378d-8572-de64ee9420dc | -6.4357 | -45.60752 | 2025-08-31 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c62674b-33d9-3cb2-a4a1-dfaa37e8b743 | -4.48479 | -48.1209 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b481b92c-0e53-3969-b7a4-bd97b5821fb1 | -7.57465 | -45.12063 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28864bb7-575e-3bad-bc3c-926a22f6e950 | -5.40271 | -45.14911 | 2025-08-31 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba97acea-b5c2-3b13-91c2-bd5e32afb1f2 | -6.4873 | -43.55606 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d823bae-d09c-36d4-a231-4893d25e6cdd | -7.58362 | -42.70561 | 2025-08-31 04:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 35cba8b3-8e1f-3c9c-b0a3-ca1a57e9094e | -8.46494 | -43.63073 | 2025-08-31 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6bdbdf1-3332-35b3-856e-7b094ff8bd26 | -6.15762 | -44.13362 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6476a77-4619-3f97-8e91-a5b957c3c95f | -6.42958 | -45.603 | 2025-08-31 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 474a4de1-adcb-359e-97f4-2eafa24590f4 | -6.83673 | -44.2575 | 2025-08-31 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1850c8f-e38a-39d4-9611-fe4251b934cc | -6.17908 | -43.99372 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c7fd3c5-bf81-3af9-99aa-402876ae942e | -6.51634 | -42.94933 | 2025-08-31 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0ae3d6a-979c-32c3-96e5-4f2976945e4b | -4.00243 | -47.09297 | 2025-08-31 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1d1b4e2-e571-3934-9b63-2b310a410b9c | -6.19712 | -42.74969 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1e40d302-4560-333f-ba34-a7beb9101522 | -7.63019 | -42.65499 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f2926bd-ce83-3788-9904-f60835e1acac | -8.54251 | -45.80743 | 2025-08-31 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc57a5a2-c449-3dc7-829c-5a466ccf396c | -4.17073 | -42.03347 | 2025-08-31 04:27:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cdd4d50f-6df6-3e86-9273-b7535bb1fc52 | -9.25559 | -47.0552 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ed6e50d-e021-365e-81f2-ee088d133d96 | -3.22036 | -46.83035 | 2025-08-31 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d8cd40-db62-3957-9133-4d8746577e48 | -6.70918 | -51.4224 | 2025-08-31 04:27:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 1db6b234-5133-3f0f-bc0c-fd8d331b4be0 | -6.9156 | -44.3764 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ec22148-e752-3080-a611-af95faf547c1 | -6.10827 | -43.28083 | 2025-08-31 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e82a8484-7910-35a2-a7c6-0a2221dea0f3 | -4.0676 | -47.95467 | 2025-08-31 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2aa7eb7-cea6-31c3-9287-f752640b0901 | -7.01379 | -42.03188 | 2025-08-31 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3580de3e-784a-3e52-8ec5-658bb4ada1ef | -6.60945 | -53.12619 | 2025-08-31 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e7a9224-a5db-34c1-8dbe-39dd699ae9fa | -4.30833 | -48.09737 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee49b153-a8f8-3bf6-9062-c5f0accd2b88 | -6.18292 | -44.12973 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d13a93ed-b341-3b53-9f34-4cf779e4ab02 | -6.1791 | -43.56803 | 2025-08-31 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 541a1c59-b6a2-3a4d-b97d-00b55809c9b0 | -6.28524 | -43.53538 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53e266d8-d4a7-3ca4-a79e-df7e78e9d88d | -6.37376 | -43.543 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README34.md)
