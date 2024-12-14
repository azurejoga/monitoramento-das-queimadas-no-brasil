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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66281541-55e4-3deb-b704-be171e4ed13f | -4.6568 | -43.82327 | 2024-12-14 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89644307-1c56-3db7-8c63-1cdcd546b59c | -13.16883 | -53.28899 | 2024-12-14 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45071a2c-d107-3509-ac08-f8d7faf8e5fd | -4.41298 | -45.83025 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 097ff46c-05e3-36f3-b151-b1689a8fda30 | -4.31611 | -47.528 | 2024-12-14 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af44e9cb-83ae-3fae-aad3-d400c4c0200a | -14.68725 | -52.63506 | 2024-12-14 04:25:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 443a78ca-115f-3e24-9750-71a18d719782 | -13.16537 | -53.2844 | 2024-12-14 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bcf7ccb0-89d7-3bdc-b19e-1f63f23fd016 | -4.31952 | -47.52857 | 2024-12-14 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2d7cd73-5a60-3f32-b8b8-c9ffdf9c87fa | -4.05199 | -46.67463 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| beb6b52d-266f-3a35-8092-29ee6e2c9605 | -4.05255 | -46.6711 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6d41576-baf8-301f-a9b2-d4c1b22051d9 | -12.55754 | -57.71334 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9d578ad-614a-3111-9363-13ab94ebd94d | -4.40967 | -45.82973 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f875fc83-bd8a-3fe1-a71e-ab2909e8d6b5 | -4.00775 | -46.54874 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e025cbe9-d3fc-3d4a-a6c3-ba72fc10d302 | -4.09766 | -46.66745 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9f85666-b77f-3956-958a-5d95c0cb0397 | -4.41352 | -45.8268 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63d90a3e-8797-3d96-ab2a-18ac5e39f025 | -6.01921 | -45.81136 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9fa9807-69dc-3f0c-b2fa-ffbcea36ca87 | -15.56889 | -47.85393 | 2024-12-14 04:25:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db9e040b-c85a-36ff-b6bd-83a8193bdb85 | -5.06013 | -42.61327 | 2024-12-14 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c370c95-bed3-34d5-a865-b9d7303a2d05 | -4.01089 | -46.54559 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7429e1ea-4cc6-32d1-9884-b503b9d64969 | -6.0379 | -44.04089 | 2024-12-14 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e404db4-8ac0-3b31-b77c-f38cab9d73d0 | -13.94861 | -44.2028 | 2024-12-14 04:25:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a189af9a-0cd5-3ad3-9327-745858d8430a | -5.35269 | -46.22604 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab511766-532b-3bcb-823a-1181413fba26 | -14.95818 | -46.90518 | 2024-12-14 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e70f95cf-2272-319b-aeb4-d2a3d6ae9573 | -5.50584 | -45.48961 | 2024-12-14 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b705ca2-85ba-30dd-a4d2-9e3c3f0b8728 | -4.04865 | -46.67409 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50504e65-2d4e-3d75-9a8a-d5758d35b32a | -5.53482 | -42.8536 | 2024-12-14 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2158489c-bdae-3a6d-9dc1-8852eac4499d | -14.9701 | -44.40791 | 2024-12-14 04:25:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32491e33-c2c4-3a98-9c96-30ff430feb4d | -4.09745 | -46.68502 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b0a145a-79d3-30f0-9f5c-bcfd1ee26daf | -4.05311 | -46.66757 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04033d43-a124-3981-9af0-662920f2df01 | -4.37722 | -47.62897 | 2024-12-14 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f37e2f59-bb4c-3fd9-9a4a-164a5b34ca34 | -4.72259 | -43.19668 | 2024-12-14 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 189a71c4-3d27-37e6-8e26-e6c71c29f8a1 | -4.42013 | -45.82784 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af639822-1d41-3cef-b0a2-3c4b95407d32 | -4.23008 | -46.79266 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba4afe28-c1e9-3622-acf8-9ecc62f17fd4 | -3.98241 | -46.89615 | 2024-12-14 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a65dd51e-557f-3835-b8b8-210e9edcd705 | -4.01033 | -46.5491 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e84ece6d-6b63-329c-9ef5-b33d44c6ab5d | -13.18582 | -49.77797 | 2024-12-14 04:25:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66b08b66-c3fd-3274-bc77-fe502414ea79 | -4.08485 | -46.66183 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d94e5e89-4586-3c9e-ad46-6c6e34b32b33 | -11.82742 | -57.82821 | 2024-12-14 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29597f6e-a464-32ca-a5d2-e61836659413 | -4.22673 | -46.79216 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa7af803-bf54-3594-9785-47aaef06be5e | -16.92112 | -43.59652 | 2024-12-14 04:25:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 616b826c-ecd2-3bfa-9c2e-d51a1f1a0a4a | -4.09875 | -46.61708 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 65f69f64-b65d-30a3-8599-8e2d7ebd726e | -4.41574 | -45.83421 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4f706ab0-4e42-3c02-aba7-7986cc763230 | -4.40745 | -45.82232 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1072905-d990-3776-9952-5b60e9021d75 | -6.01645 | -45.80738 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6d00b89-bbcb-3b0e-9e22-4eedac8fc7d1 | -6.92288 | -35.71482 | 2024-12-14 04:25:00 | NOAA-20 | AREIA | PARAÍBA | Brasil | 2501104 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7c9d578-cd6d-3021-bfc7-ae572042aa7e | -6.52276 | -41.28428 | 2024-12-14 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6958db80-51d5-3722-a1a2-4fb242dcfd05 | -12.55193 | -57.71227 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a819a7c3-f51e-32f4-a790-3cb319598734 | -12.33991 | -51.36286 | 2024-12-14 04:25:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6f461f3-a531-3620-a1ea-c462156f534d | -4.09764 | -46.62414 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a815b21-2f68-3f96-889c-bae9c4516354 | -6.02252 | -45.81187 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f7c9b50-3f6e-3781-9b15-e52c450ef865 | -6.93018 | -42.84777 | 2024-12-14 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 684c48e1-2c77-3515-a4ef-5a4838cb6422 | -12.55896 | -57.76559 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11433e2b-0d79-336c-95c4-fc9b437088d5 | -4.40582 | -45.83265 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea723661-51b9-3387-a337-45fb2648ed93 | -5.30607 | -46.07013 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58dca910-8d89-370a-ad79-77c625473748 | -4.40305 | -45.82869 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 747b9397-ea95-3432-b5ec-78da916feb69 | -11.82903 | -57.82013 | 2024-12-14 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c90064ac-4674-3bfc-949a-7f4a5304bcb4 | -4.40913 | -45.83317 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f4ae3c5e-1fe3-32a2-a9d5-8276d89b1568 | -5.4319 | -37.85137 | 2024-12-14 04:25:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b5c4414-baac-3188-b022-03237231e688 | -4.01467 | -46.65073 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5a512e3-4487-3a55-87b0-c1f13bee5c61 | -6.51427 | -41.28651 | 2024-12-14 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1a0ee60b-9ed5-3131-b339-4835f9e4ebd9 | -4.09541 | -46.61655 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8bc3d1c7-9d0d-3190-9373-bb4352ee90c7 | -5.53419 | -42.85768 | 2024-12-14 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6aede229-3dea-3707-aadd-737740bb5014 | -11.82251 | -57.82304 | 2024-12-14 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c97a01f9-4233-3689-8521-9b132092bd78 | -5.04455 | -43.21932 | 2024-12-14 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33fcdef0-77ce-3a01-b732-e75570dea809 | -4.10153 | -46.62114 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 584f5d11-91b7-32d5-965c-5db784da355e | -6.04819 | -44.04253 | 2024-12-14 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a5867842-821e-3eab-96b1-f8e69700c667 | -6.92232 | -35.71879 | 2024-12-14 04:25:00 | NOAA-20 | AREIA | PARAÍBA | Brasil | 2501104 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c4631ed4-7e55-32a0-bdc2-883bed0a74b1 | -4.0952 | -46.69909 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13366d20-d26b-397c-b998-429ef4febbc1 | -4.42068 | -45.82439 | 2024-12-14 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e900b10f-d8a5-3f1e-929f-ce3f3100f405 | -7.8349 | -35.18473 | 2024-12-14 04:25:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e269d45a-2a7a-3f0c-a175-579877dac005 | -5.43298 | -37.85197 | 2024-12-14 04:25:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4366fc6d-44d3-3e6c-86a2-60bf945385e7 | -11.82679 | -57.82547 | 2024-12-14 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a5df1734-ee61-3c9c-a50b-9b197404c0cd | -4.02723 | -46.89592 | 2024-12-14 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d11d3c08-68a2-38db-9010-623f75d52322 | -5.30661 | -46.06668 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f444797d-3088-31d8-9c73-d9d08a08ce70 | -4.09377 | -46.67042 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff852648-8b4b-3f1c-86ac-ad3d21c70d9b | -13.541 | -55.38546 | 2024-12-14 04:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c537babd-b248-368f-a0be-c929718ea593 | -6.04133 | -44.04145 | 2024-12-14 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cddcde34-b6c2-3c7f-a7b7-97c01be75547 | -6.66811 | -39.2412 | 2024-12-14 04:25:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ae5335a-82cd-3896-b62d-53b7a83a4a8c | -12.55117 | -57.71614 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed4b8509-b869-30d2-a0a0-7f214cb38505 | -4.41959 | -45.83128 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2e9bb097-b585-3c91-9b62-45fc2ec9f8da | -5.28684 | -44.91351 | 2024-12-14 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 264b995d-9248-340f-844b-c35ae341752f | -15.54759 | -48.46602 | 2024-12-14 04:25:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 64000a1b-1e91-3f17-8563-ef0154d20515 | -4.04806 | -46.72102 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aab3478d-4fc1-300f-ad55-95ef50174f58 | -12.54633 | -57.71121 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d27ea038-3c2b-3b0b-891d-e16fefd23622 | -11.91243 | -48.88158 | 2024-12-14 04:25:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ed10d13-ee07-392f-abcc-601918bd7df4 | -4.09711 | -46.67094 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2b6a416-52df-30b2-bd00-08fe3b4596ae | -4.0982 | -46.62061 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d602d1b-a654-31ab-8c0a-9c4fee598bb0 | -12.56531 | -57.76295 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 541cde90-dcf9-38d0-b45d-e0781ab8b643 | -16.05097 | -43.80017 | 2024-12-14 04:25:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ff72675-624f-3696-aa23-632a01d18395 | -5.42113 | -44.85784 | 2024-12-14 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96288a95-6a5c-30a9-8a80-52709655254c | -4.05692 | -46.88242 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e96d31bb-b4f7-3b7b-8eae-185e89183ece | -4.3847 | -47.75608 | 2024-12-14 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28807b06-e821-399a-8fee-3fa2e339594d | -5.53779 | -42.85819 | 2024-12-14 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| af27d631-fbd3-3afe-9559-20b5f4ab4b1e | -6.0419 | -44.03772 | 2024-12-14 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 50fb348a-550f-3638-ac75-88c9c72f5254 | -12.55041 | -57.72001 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| af91461f-176d-3c72-8382-a0229db3c618 | -4.66551 | -44.03899 | 2024-12-14 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80e57705-6207-30e5-8071-a040ce0b9231 | -14.69593 | -52.63134 | 2024-12-14 04:25:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d1ef22b2-08f8-37f9-b224-84c4f4456ebf | -4.03002 | -46.90005 | 2024-12-14 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd346f6e-aaf1-3eab-a400-a7e4583d3427 | -11.82822 | -57.82416 | 2024-12-14 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96ff7035-4eda-3d33-ba79-79b1e75b69a4 | -6.04532 | -44.03828 | 2024-12-14 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 621dd463-a23f-3cec-b8b2-018f7aabeea3 | -4.09913 | -46.67447 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README10.md)
