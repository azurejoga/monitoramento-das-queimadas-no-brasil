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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8853d360-c872-3423-b58d-cbf15371e19a | -7.9294 | -46.679699 | 2024-10-31 00:29:59 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 210179af-069b-3376-8a9d-89c255a5396d | -7.8981 | -46.860699 | 2024-10-31 00:30:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 397ce785-854e-34aa-95ba-f828641a99d7 | -7.8867 | -46.855999 | 2024-10-31 00:30:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb4236a-4682-3ccd-aae3-d848d4abaa2a | -7.8883 | -46.8629 | 2024-10-31 00:30:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34df564c-304a-3b79-b945-307628321513 | -7.8898 | -46.869801 | 2024-10-31 00:30:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ccde606-647e-303e-a2df-d80d2732fa4f | -7.5731 | -45.519901 | 2024-10-31 00:30:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22448a6d-6141-32f8-b4de-62468628604f | -7.6419 | -46.365398 | 2024-10-31 00:30:02 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6521e0c-ae57-3045-b615-e58267cc23c1 | -6.7203 | -43.042198 | 2024-10-31 00:30:05 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72b6d469-7ce0-32ca-b2cf-5bac2ea2e1a7 | -6.7225 | -43.051899 | 2024-10-31 00:30:05 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90cc0b12-2814-3448-be42-85c66d7af5c2 | -7.7002 | -47.309601 | 2024-10-31 00:30:05 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 540ab8c7-df47-3a47-a6f0-9aac55b5e046 | -7.6904 | -47.311798 | 2024-10-31 00:30:05 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1be5ec7-4809-3400-ad39-d669888d19df | -7.6919 | -47.318699 | 2024-10-31 00:30:05 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 511add8c-1db7-37aa-abfb-d29c595c015b | -7.6935 | -47.3256 | 2024-10-31 00:30:05 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 783aede5-1bab-346e-ad71-6ab29b924181 | -7.2624 | -45.514 | 2024-10-31 00:30:05 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d0643b4-c9f5-3d9d-8e8e-56fa963674d8 | -7.2641 | -45.5214 | 2024-10-31 00:30:05 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f17c4ea0-be6b-3200-af6e-06d1c7388f45 | -7.2658 | -45.528702 | 2024-10-31 00:30:05 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ecf6104-c8dd-38cc-a3e9-d267c931e976 | -7.4949 | -47.175301 | 2024-10-31 00:30:07 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a390b154-24de-3828-b7dd-c935257df241 | -6.6126 | -43.683601 | 2024-10-31 00:30:09 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a39acb3e-8e71-3729-942a-4e0db181e693 | -7.2065 | -46.309502 | 2024-10-31 00:30:09 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70e280d2-9f9a-3586-b794-22bdbd67f699 | -7.2081 | -46.316601 | 2024-10-31 00:30:09 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d58e9df3-d160-3a09-a7b8-f401f48ac073 | -7.2097 | -46.323601 | 2024-10-31 00:30:09 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9b73dec-b3c1-34de-b119-128a2fdf0c37 | -6.2187 | -43.409901 | 2024-10-31 00:30:14 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17d11db0-9c7a-3d4e-afbc-b8b5e5387e03 | -6.2209 | -43.419201 | 2024-10-31 00:30:14 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acd13cc5-6878-3f78-87b6-c1ecc68e4ab9 | -5.9846 | -42.587601 | 2024-10-31 00:30:15 | METOP-B | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7ee1805d-e692-3d2b-9079-480dc9dcd8d6 | -5.9871 | -42.598202 | 2024-10-31 00:30:15 | METOP-B | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c57d2da8-d94d-36cd-b95e-a97e6ac28842 | -5.3264 | -40.508202 | 2024-10-31 00:30:17 | METOP-B | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bf8aef9a-c53a-3fb6-930d-481cc45cd12d | -6.0891 | -43.605598 | 2024-10-31 00:30:17 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94331ec7-bf70-393d-a5f9-679abaa04761 | -6.0913 | -43.6147 | 2024-10-31 00:30:17 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7e57a7b-fd4d-3dad-bc47-e0a3860ff4c7 | -6.1584 | -43.947201 | 2024-10-31 00:30:17 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba8607f0-a006-3a10-85e3-b797266da267 | -6.1604 | -43.956001 | 2024-10-31 00:30:17 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31b46652-2a53-32dc-8bce-8e82d712b11c | -6.1624 | -43.964699 | 2024-10-31 00:30:17 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9fce1811-8145-3ea5-a8e6-8460c5e64a67 | -6.1486 | -43.949501 | 2024-10-31 00:30:17 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0cb01066-bd3e-3008-bcb9-cfffc5ecb6ae | -6.1506 | -43.958302 | 2024-10-31 00:30:17 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42249abd-1f0e-314a-a46b-97e0db7a53c8 | -6.1526 | -43.966999 | 2024-10-31 00:30:17 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| adddacee-4779-35fe-91aa-b3270b2553ea | -5.3194 | -40.4786 | 2024-10-31 00:30:17 | METOP-B | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 90f6e026-fd79-3175-bcbd-7207db7eae26 | -5.3229 | -40.493401 | 2024-10-31 00:30:17 | METOP-B | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6cf9c96b-c911-3756-81a1-d55f75898ecb | -5.836 | -44.1133 | 2024-10-31 00:30:23 | METOP-B | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58e4502f-102a-3391-8a56-a87840659912 | -5.838 | -44.121899 | 2024-10-31 00:30:23 | METOP-B | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a462ac14-6f4e-3b6a-a657-38febf77e9d3 | -5.4794 | -43.157101 | 2024-10-31 00:30:25 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2143790-e18b-32d5-93f5-5a7bca10dab2 | -5.4818 | -43.167 | 2024-10-31 00:30:25 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4a8af67-aad6-3f69-b394-05a2df5b4f60 | -5.6426 | -43.946098 | 2024-10-31 00:30:25 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cf45090-1e2f-3c3f-860f-a3b01ca45e92 | -5.9973 | -45.3484 | 2024-10-31 00:30:25 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0f13d84-35ad-3607-8a0a-e9071a6c4b23 | -5.9991 | -45.355999 | 2024-10-31 00:30:25 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1c668a-6cc8-37ec-82b1-4410de68664d | -6.0008 | -45.363602 | 2024-10-31 00:30:25 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be88dbdc-7129-35f7-847f-b9086d614919 | -5.9893 | -45.358299 | 2024-10-31 00:30:25 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f305df0d-ed7e-326d-8194-95e0e6fbe04c | -5.4684 | -43.242401 | 2024-10-31 00:30:26 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93c02319-db63-3078-8a00-0f399b1f63f6 | -5.4707 | -43.252201 | 2024-10-31 00:30:26 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c85b797-9f76-3107-a7f3-f74317aef440 | -5.461 | -43.254501 | 2024-10-31 00:30:26 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b036e3b-e820-3c84-8090-80943f29b3dc | -5.3197 | -43.047001 | 2024-10-31 00:30:27 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26b1505a-3472-3f72-9a7d-c8499231d57f | -5.5742 | -44.317902 | 2024-10-31 00:30:28 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e963b354-2329-3264-95f6-c622413dc3a3 | -5.3407 | -43.711399 | 2024-10-31 00:30:29 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27e878e0-5695-388d-940d-aaabba4de43e | -5.3428 | -43.7206 | 2024-10-31 00:30:29 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5d5b4a2-af2a-3fe1-85a9-1eace3bea280 | -5.345 | -43.729801 | 2024-10-31 00:30:29 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89492641-7b4f-3fb0-81a8-0117719cbb24 | -6.2007 | -47.285198 | 2024-10-31 00:30:29 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 074ef893-dbb5-3b79-b6ea-4c647ebc07b7 | -6.2022 | -47.292099 | 2024-10-31 00:30:29 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46fbfa45-bab1-3470-a66e-81cfa5766c70 | -5.3079 | -44.013901 | 2024-10-31 00:30:31 | METOP-B | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40a228fc-2963-3e2e-930b-cd059a1700a2 | -5.1016 | -43.348099 | 2024-10-31 00:30:32 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f033d9c-573f-3f88-97f6-2867db29a567 | -4.8732 | -42.459801 | 2024-10-31 00:30:32 | METOP-B | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e79a965-ff34-3ec7-98e2-73cb8d31106a | -4.8758 | -42.470901 | 2024-10-31 00:30:32 | METOP-B | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6f969835-3f35-3c81-a13b-5b5b7c6f16c9 | -4.8635 | -42.462002 | 2024-10-31 00:30:32 | METOP-B | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 579a990d-32b0-35bc-95a7-8097870812d7 | -4.8661 | -42.473099 | 2024-10-31 00:30:32 | METOP-B | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c71f9f3-87c3-37d6-ac3e-d7a3fb228afb | -4.8923 | -42.628899 | 2024-10-31 00:30:33 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6939d052-3089-35fe-aa06-0a858f8c5236 | -4.8898 | -42.618099 | 2024-10-31 00:30:33 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 006b83da-4404-330f-96d5-2c0156b73c78 | -5.4047 | -45.102699 | 2024-10-31 00:30:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2f1d139-5b58-3df3-a7f3-a44c9c6bd9a9 | -5.4065 | -45.1106 | 2024-10-31 00:30:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85a9f673-d45b-3c63-acb2-b725c03b4fa8 | -5.3579 | -44.988998 | 2024-10-31 00:30:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5b0293f-da76-3b71-b84c-686d6fa7f82a | -5.3597 | -44.996899 | 2024-10-31 00:30:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e56fe6a-448a-31a3-9bd9-54167d504aba | -5.3163 | -44.8978 | 2024-10-31 00:30:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b39a5ef0-08fc-3eca-ae00-4ea6b522538d | -5.3181 | -44.9058 | 2024-10-31 00:30:34 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cb2e321-7bb6-3c9f-8cc1-9e37d2d9c109 | -5.0127 | -43.719002 | 2024-10-31 00:30:35 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d996bbcc-a40e-3959-a6b7-e8e9bdc9fd0f | -5.0029 | -43.721199 | 2024-10-31 00:30:35 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d09c8ee8-046c-38fd-b6bf-b2110e764433 | -4.9573 | -43.6134 | 2024-10-31 00:30:35 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea16e15-c020-30e0-b627-3b2f011dfeaa | -4.9595 | -43.622898 | 2024-10-31 00:30:35 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37306df3-e68a-39e4-bba0-4c34ab86f35f | -5.2538 | -44.895199 | 2024-10-31 00:30:35 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3ae685e-ac87-3c53-81fa-0947a5007730 | -5.2557 | -44.903198 | 2024-10-31 00:30:35 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9deba681-47b8-3c9e-ad60-de68fec798e8 | -5.084 | -44.2043 | 2024-10-31 00:30:35 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1605d41-dee7-3732-8c75-46e62c6e0806 | -5.086 | -44.213001 | 2024-10-31 00:30:35 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85c1b5f9-c47d-3b7f-93aa-8cdacd00bf3f | -5.0881 | -44.221699 | 2024-10-31 00:30:35 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41f5632f-c4c5-3eec-9700-85913904b523 | -5.2505 | -45.1049 | 2024-10-31 00:30:36 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12e76afe-5fd0-3772-ae63-faa6645f0160 | -5.2523 | -45.112801 | 2024-10-31 00:30:36 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b98f1afd-389c-3ef6-a481-b6c1c56de6d3 | -4.7573 | -43.240898 | 2024-10-31 00:30:37 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 917129c9-92de-313f-b18a-c3127bcffeff | -4.6731 | -43.100899 | 2024-10-31 00:30:38 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76432573-df54-3697-ae9e-e12645c455d0 | -4.6755 | -43.111099 | 2024-10-31 00:30:38 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 615aafec-612c-3265-a724-8b18db10ad21 | -4.6633 | -43.103199 | 2024-10-31 00:30:38 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6f70109-8327-34ae-a743-b4cc1d3fd0cf | -4.6657 | -43.1134 | 2024-10-31 00:30:38 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00928064-97eb-3fdc-b48d-e174db6a96e7 | -5.044 | -44.789902 | 2024-10-31 00:30:38 | METOP-B | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30d849d9-d061-30d7-867d-277bbe6598b1 | -5.0459 | -44.798 | 2024-10-31 00:30:38 | METOP-B | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 136de7dd-5b5b-3425-b634-539bc8b174b7 | -5.0742 | -45.1451 | 2024-10-31 00:30:39 | METOP-B | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8afe69fb-cd55-38a3-8a0c-30a3207b7c82 | -5.076 | -45.153 | 2024-10-31 00:30:39 | METOP-B | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd8a833c-a6cb-3c11-baec-b5762c724bd5 | -5.0644 | -45.147301 | 2024-10-31 00:30:39 | METOP-B | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34c0dfa9-e707-366d-9a9a-95ab2d8b1f6d | -5.0662 | -45.155201 | 2024-10-31 00:30:39 | METOP-B | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06c4c201-5fec-373b-b0db-c9bb82ac36bb | -5.068 | -45.162998 | 2024-10-31 00:30:39 | METOP-B | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce9b1d4c-821c-3d55-84a5-4770a3bf1704 | -4.5316 | -43.112099 | 2024-10-31 00:30:40 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f6b08bb-18a5-3712-a784-5421434db622 | -4.2786 | -42.162399 | 2024-10-31 00:30:41 | METOP-B | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1bd77e1a-9872-31c8-9e00-55e9dfbeee15 | -4.2814 | -42.174301 | 2024-10-31 00:30:41 | METOP-B | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 06fa15f6-46e1-35db-9af8-fe5b6c7c8e1d | -4.2689 | -42.1647 | 2024-10-31 00:30:41 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ddff1254-46e8-3ef1-a54c-ae955a798d4f | -3.8862 | -40.627201 | 2024-10-31 00:30:41 | METOP-B | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a5831d27-eb4b-31f3-ad53-46d95fef317c | -4.7327 | -44.155399 | 2024-10-31 00:30:41 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd15a2a6-1059-36ba-a060-fc734e9720dc | -4.7304 | -44.457802 | 2024-10-31 00:30:42 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4adec21e-e69f-35fd-be09-649192d3e976 | -4.7324 | -44.466301 | 2024-10-31 00:30:42 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
