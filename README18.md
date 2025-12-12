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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2ba4f60-9649-33c7-ac57-9642ea326242 | -3.23121 | -42.07552 | 2025-12-12 04:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6725462-81d7-379c-b7d4-dee3756fc30a | -1.12337 | -47.73925 | 2025-12-12 04:21:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5285bca6-4e05-393c-a2c9-bf7183173721 | -4.15271 | -50.53619 | 2025-12-12 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01f4a8eb-242c-3a33-af8d-2c509e43b8fc | -4.158 | -39.25166 | 2025-12-12 04:21:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 10b5f55a-be35-332a-b5a8-4dc5dda5869b | -2.12202 | -45.35219 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 811d17f2-06f3-3d91-b84c-c2cacad60fba | -0.55499 | -48.66779 | 2025-12-12 04:21:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47f428fc-f65e-354d-9a42-ee1fb770d58b | -1.18941 | -54.04672 | 2025-12-12 04:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e530416f-2106-3369-9749-caa31e025c9b | -2.87942 | -53.01143 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17775de9-e210-39df-9407-0e2d04eb66a6 | -3.30346 | -44.86438 | 2025-12-12 04:21:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e77a2b1-ebe9-363e-ac13-9db3c1a46f81 | -4.7303 | -43.07094 | 2025-12-12 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b09f634-4102-3815-9d8b-2672140c9ef2 | -4.74038 | -49.79881 | 2025-12-12 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 976df3e4-4dbd-3086-8a7b-14037e877b1b | -3.65776 | -40.901 | 2025-12-12 04:21:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dd75d8f8-aed6-3208-9f93-cee7f39704b8 | -3.26404 | -45.5597 | 2025-12-12 04:21:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 475ace1a-a9ae-3016-af98-b5b10f3f20a5 | -1.7014 | -52.14694 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c505bfa-7764-3fe8-92fb-317cbef740da | -4.14306 | -46.11732 | 2025-12-12 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bde498a1-9481-35ea-af74-caa618eb194d | -2.02376 | -48.99529 | 2025-12-12 04:21:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 305f571a-e827-317c-b566-963c682b1f2b | -1.31267 | -46.5323 | 2025-12-12 04:21:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 56f25bc0-67c8-3270-ac1d-c92ae430d143 | -1.03106 | -53.74377 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87afa982-63e6-300d-9b8e-21eeea9be96b | -3.06547 | -45.79578 | 2025-12-12 04:21:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 586a1ded-6070-3488-9154-a7a6214d0483 | -6.02651 | -43.70724 | 2025-12-12 04:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd598f3c-93b8-308e-aa81-ce0e67556177 | -6.40507 | -38.00484 | 2025-12-12 04:21:00 | NOAA-20 | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b8ff9a0-79a7-3720-b39f-2de44b42dfe4 | -3.91332 | -46.0632 | 2025-12-12 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 921803c5-096f-3750-a904-222df1c66a90 | -2.41152 | -46.06788 | 2025-12-12 04:21:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc11a834-6516-37e9-ac35-4b1043443c97 | -6.11975 | -41.27841 | 2025-12-12 04:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 416d5a81-f8b5-3570-ba6c-80a833a016c1 | -1.10999 | -53.69012 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c93b023-7449-3f45-8c62-15f6f99aefb5 | -3.70044 | -44.5018 | 2025-12-12 04:21:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c78a24ae-a6af-3a77-9890-f6eef88b7b45 | -5.97031 | -44.06773 | 2025-12-12 04:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bef672b-e8fd-3aae-94db-0e9937506d77 | -2.50144 | -51.79799 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0700cb59-a334-3c67-b991-88fc705b965f | -2.59725 | -46.87398 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25f11364-ffc4-3f99-85a9-502289bf1e27 | -4.1458 | -42.8823 | 2025-12-12 04:21:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d749a41-4a0b-37d0-a82f-b481cdbc502c | -3.82528 | -42.17607 | 2025-12-12 04:21:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c43c4cef-8433-31d0-8a27-ce13f4eb1934 | -2.48544 | -47.77958 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 038bcf9d-35f2-3268-aa75-0e15067c966d | -6.02372 | -43.70321 | 2025-12-12 04:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb1fca74-397f-3572-bd6c-4e58fd6aa7e7 | -8.0331 | -43.09419 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f6caa9e2-5aab-3c2f-9732-b730a79b912e | -4.65979 | -42.39649 | 2025-12-12 04:21:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 11a4f29d-6013-31a6-a93e-b68d0bd59559 | -4.38807 | -43.63121 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 837d3f26-c1f9-375d-8575-72aab1a83fc5 | -3.02745 | -49.05518 | 2025-12-12 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cce37abe-21d0-3f74-8774-c7b8715f6419 | -3.06068 | -45.79941 | 2025-12-12 04:21:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56ef6bd5-ef11-3fc5-b6d6-7a3a43de0730 | -1.31736 | -52.5315 | 2025-12-12 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5ddf63b-5083-3bc4-b9e7-056ac5eed9c1 | -0.5477 | -48.66336 | 2025-12-12 04:21:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1570440b-3350-325a-ab88-a694a5de3725 | -6.51367 | -55.04296 | 2025-12-12 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dff6e6aa-9477-3550-b3ad-d1df3b89079f | -3.97197 | -42.51579 | 2025-12-12 04:21:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ca668669-b136-33a2-b608-3fe546d2513b | -3.93768 | -40.73497 | 2025-12-12 04:21:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 03aae49a-c855-3165-ae9f-11f5a8d145ae | -4.38782 | -46.66654 | 2025-12-12 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7da726be-ebe3-331f-9222-597d68ed391c | -1.03574 | -53.74134 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a829d2c9-8095-34dc-833b-4aed46c9345a | -2.41883 | -51.93182 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9f5cfb6d-0a4e-3759-85de-04b9139f9710 | -1.01412 | -53.72989 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0de31648-6b13-3384-83e7-3506541e1e25 | -4.7488 | -44.55463 | 2025-12-12 04:21:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2aed283-e1f0-32d6-aa31-ab909e3908b6 | -2.42285 | -51.93819 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| eb99c015-879b-344b-b728-af7da307d32c | -6.47009 | -35.16842 | 2025-12-12 04:21:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 947b2e35-45b9-34cd-813e-52d2d20bc62f | -3.86855 | -40.64427 | 2025-12-12 04:21:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a1e7fd09-b108-32a9-afe0-beb287015d4b | -4.39194 | -43.62825 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fc3d44c-50f5-3c31-9d41-2487bafb4f62 | -2.18957 | -46.61619 | 2025-12-12 04:21:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e72eee2-bf81-3d0b-97a8-389b949c8152 | -3.95578 | -41.52655 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0675f15f-7306-3cf6-99b6-be5370cd4eb0 | -3.04675 | -53.01215 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1f41ec7-18ea-3802-9945-75ad6532ce6b | -6.12212 | -41.28751 | 2025-12-12 04:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bc0dc4d1-0d91-35ef-88a2-72b28aa3d2c9 | -6.64141 | -43.15079 | 2025-12-12 04:21:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65a959dc-4284-3c64-8e64-8cc0ee532bb9 | -2.27857 | -47.05924 | 2025-12-12 04:21:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b360e95-ec65-3e5e-aec9-1f4516f9f3f3 | -2.64822 | -51.64233 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0c47767-ec21-39e2-8dd5-7c28ca8ef0e9 | -3.81491 | -47.05319 | 2025-12-12 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b1be89f-a35b-3349-ba57-6e84f34eaa87 | -2.14397 | -45.65675 | 2025-12-12 04:21:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c64c003c-856d-3d36-ab58-30df2e1f4c4e | -3.85271 | -46.95266 | 2025-12-12 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd248009-754c-3b21-9699-4459ff123e50 | -3.06126 | -45.79576 | 2025-12-12 04:21:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efa405ba-40b4-30f8-95b7-83735936f1af | -2.24139 | -46.51892 | 2025-12-12 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae6db428-3129-34bf-8204-670a072c3d95 | -2.48169 | -47.77897 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 673086b5-7dab-3bf8-8516-756745073523 | -3.21544 | -42.68893 | 2025-12-12 04:21:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| feefb2fc-8bda-3662-9ad8-05ed34d327ab | -12.40507 | -58.04848 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a9e3da1f-dc9f-3e68-91e5-050e4becde69 | -12.39743 | -58.04487 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 21dcd10a-252c-3db1-b425-c4eddc0beb35 | -10.54899 | -48.72419 | 2025-12-12 04:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec6e2def-c9f4-335d-9bec-032202dcf1de | -12.20245 | -49.54905 | 2025-12-12 04:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a60242a-df8c-3d22-bc33-4c4211cdec92 | -10.2322 | -52.22297 | 2025-12-12 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 28811186-5cfe-3601-bf42-ca19a625133e | -11.02774 | -50.53288 | 2025-12-12 04:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 768edbea-1a35-39bc-9e01-c7aa49798272 | -11.88961 | -43.70838 | 2025-12-12 04:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a07b5e52-aceb-3854-a157-6ee74c3088bb | -12.12596 | -39.40714 | 2025-12-12 04:23:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6b63b5a-b830-3a09-8c63-e5226892c8af | -19.01008 | -49.0873 | 2025-12-12 04:23:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b6b03e77-cba7-3c67-988b-88411c1f3506 | -21.31819 | -49.17759 | 2025-12-12 04:23:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 89003adc-3c28-3bc2-b589-31a8635da492 | -12.40466 | -58.04118 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 86158b54-cfca-33f5-85fb-b728f3b285e5 | -19.26901 | -46.52133 | 2025-12-12 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ce6e017f-c20b-315b-a51d-e755bb0055f6 | -20.95559 | -48.77165 | 2025-12-12 04:23:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 34be9395-0234-32d3-b65b-313da7777f76 | -12.38851 | -58.03442 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1b3c00a7-48e8-34ec-a036-4e647b0ef77e | -15.31859 | -42.05233 | 2025-12-12 04:23:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe7c1a90-d562-34b4-96e2-9fe9759e88ea | -12.41806 | -58.03883 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9728ab43-45ad-323f-b12e-c14e93823832 | -12.4191 | -58.03379 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aebe6c4f-485d-3c5a-b57a-77821f010bec | -12.4253 | -58.03505 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8346b42f-10a1-38c7-be24-76ee77e3acbf | -22.12224 | -43.26081 | 2025-12-12 04:23:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d2d8fe3c-d0b0-310c-995e-bddf93400028 | -12.20609 | -49.54971 | 2025-12-12 04:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47ae5dbe-d47e-3cfc-8b98-0e53430795f5 | -12.38501 | -58.04241 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 627b2a25-c3d9-3d44-9366-46cfcf623e8d | -11.02471 | -50.52713 | 2025-12-12 04:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8df5c375-2796-3578-bae4-55a34a8e2f0e | -21.25468 | -49.10414 | 2025-12-12 04:23:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 76cdd316-7a95-3ceb-a840-f10c10b67a31 | -12.4057 | -58.03613 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 488ce4b3-9797-31bd-91eb-ea4fc2255723 | -12.3947 | -58.03571 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 30ae2825-af4e-3d51-b9bd-41c0ff0e441e | -12.39847 | -58.03985 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9965f154-060f-3a13-a593-601176b97ce4 | -12.39888 | -58.04712 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a2f82acd-015b-3ea6-8a44-2b467e69d65b | -8.11807 | -48.01798 | 2025-12-12 04:23:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43448c6a-7bc0-392f-bcda-5077e565fdb9 | -12.62443 | -58.08433 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 154e1b58-c120-392c-a841-2d2b10f358d6 | -12.4315 | -58.03627 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 994345fb-2209-3c24-959e-d012bbad979f | -12.39122 | -58.04363 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 70482317-9456-33dc-99ff-564beae92b82 | -12.50491 | -58.36272 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97b0d4cc-00a5-3c03-8c3d-70eafa392ea5 | -12.51229 | -58.3588 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 994179f0-07db-3ed8-ade1-3b160c05d21a | -12.39951 | -58.03482 | 2025-12-12 04:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |


[Clique aqui para ver as próximas entradas](README19.md)
