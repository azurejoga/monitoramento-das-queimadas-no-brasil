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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46b8eb2f-f156-3d79-8eed-42feeedd76ec | -5.58083 | -44.31537 | 2024-10-31 04:25:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 082d762e-2319-371a-a555-78381bbaf540 | -5.54791 | -44.32531 | 2024-10-31 04:25:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f8bdf26-acde-30d7-b19f-6973b2d28f39 | -5.17498 | -44.23184 | 2024-10-31 04:25:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06a2010b-a4c6-3ecf-b0d2-1c12f80f2746 | -5.06563 | -44.2154 | 2024-10-31 04:25:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 973a36c7-d1e0-3cce-9ea1-1914c5103ee5 | -5.06507 | -44.21905 | 2024-10-31 04:25:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf933fc9-baf2-30f0-999c-fcac4380cbc7 | -5.0645 | -44.2227 | 2024-10-31 04:25:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b14511f-e7b7-3cc1-b7ad-5a93158b1c62 | -6.55062 | -43.91219 | 2024-10-31 04:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f58312cf-9bfa-33bd-a225-33ae35d88889 | -6.51039 | -43.65934 | 2024-10-31 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2281c14-5777-364e-90cd-ee92ceca8631 | -6.30698 | -44.88118 | 2024-10-31 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a5ea6ba-cdc2-3fbb-a8ab-ad8f47fde1c9 | -6.14231 | -44.94771 | 2024-10-31 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 283f2546-47e1-36a9-a710-6d5a05db9e81 | -6.13895 | -44.94721 | 2024-10-31 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7726addc-0e96-324c-ad58-0350963a5786 | -6.13839 | -44.95078 | 2024-10-31 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70de3638-77c3-3f4c-b31e-b89af4d879cd | -6.05645 | -44.78023 | 2024-10-31 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 695b4245-288d-36e6-bd30-7e521ef6c45f | -6.05252 | -44.78331 | 2024-10-31 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f42b62d1-c473-3989-9035-f11a961fb1d2 | -6.04014 | -44.77403 | 2024-10-31 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55ed8e04-148e-3eff-a517-ec292905fa12 | -6.03676 | -44.77351 | 2024-10-31 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 92963825-aa48-3db1-a859-33f1b0d40c45 | -6.03621 | -44.7771 | 2024-10-31 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e1dc5d6f-61c9-3aed-bc0a-4bfcce40bcde | -5.96555 | -44.75941 | 2024-10-31 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 39548d60-ad8a-3ce7-a26b-6d4deae67048 | -5.96217 | -44.7589 | 2024-10-31 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c6e29b4-58c6-30a2-9627-eab4a8e50901 | -5.96161 | -44.7625 | 2024-10-31 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee02588a-52d9-332e-979d-06f48fa23cf3 | -5.02459 | -44.80082 | 2024-10-31 04:25:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3061eac3-1c84-39d4-bad5-7e7a583d0dbd | -5.02404 | -44.80434 | 2024-10-31 04:25:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b916c50a-5014-30c1-a0d7-fa241ca8d2a2 | -7.5201 | -44.07978 | 2024-10-31 04:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a40d1f1-aefe-3a70-860e-cdb403eb98ef | -7.51661 | -44.07922 | 2024-10-31 04:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f16c53a-8667-3d66-97dd-cc96b6d9bd87 | -7.12547 | -44.39098 | 2024-10-31 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5565981f-3b3e-306f-89de-a3af586cd3ff | -7.10015 | -44.4638 | 2024-10-31 04:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4d9be03-c84d-31a0-9f23-b120162a31a0 | -6.68706 | -44.15392 | 2024-10-31 04:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27439ca5-f79c-34a4-b071-01980dda5997 | -6.68648 | -44.15771 | 2024-10-31 04:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff5bde7b-734d-3422-ba64-8f9d3d7e13fc | -7.45123 | -45.28723 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d80019c-9681-38f2-8b06-3021c89b3656 | -7.20153 | -45.117 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 567777bc-aa80-37cc-a071-ee76bdb575a2 | -6.93238 | -45.05724 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d008f799-288e-30f9-ad4e-cdba59d608a2 | -6.93182 | -45.06086 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0c36d39-53f8-38ae-b766-213267d4b948 | -6.92845 | -45.06032 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45fe078c-9e08-3065-ba01-e38800ca1ca7 | -6.92564 | -45.05618 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fd7cc48-48e8-3a6b-96db-d71e4139a2d9 | -8.84491 | -44.24675 | 2024-10-31 04:25:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea7d5379-62d6-344c-be5a-113fdbb3fa18 | -8.84431 | -44.25072 | 2024-10-31 04:25:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81d3894f-f318-3f05-8d13-f8ea5aa87b1f | -8.8305 | -44.4361 | 2024-10-31 04:25:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c5df702-ccb3-37fc-b647-9cab0ea2ea28 | -8.74949 | -44.71283 | 2024-10-31 04:25:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 117aac93-3caa-3fee-a944-e29c5d7a963e | -8.26145 | -44.84923 | 2024-10-31 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94f83f7d-baa9-3678-8568-c3f02d3ae108 | -8.26088 | -44.85296 | 2024-10-31 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e069a01-6d78-343e-a8dc-4a6688ee0116 | -8.26032 | -44.85668 | 2024-10-31 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdb7efbe-1052-3201-84f0-f18f59954e77 | -8.25976 | -44.8604 | 2024-10-31 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfc07c7a-bf8d-3e2d-9117-7de3c897b8e0 | -8.2592 | -44.86411 | 2024-10-31 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a58e3dfb-b969-3f5a-8791-3c437c2bec03 | -10.73814 | -44.94608 | 2024-10-31 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce9aa3cb-033b-3e51-8f07-b33c680497f2 | -11.02374 | -44.8375 | 2024-10-31 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59554b89-bb68-3c4c-9340-d1987409bed8 | -5.05237 | -45.40425 | 2024-10-31 04:25:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e65d0fb5-ba95-366e-89cd-baea08fccf6d | -5.05117 | -45.15771 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dace5e5-4d6d-36c5-87d7-ad72a30e2ef1 | -5.05062 | -45.16121 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b74a6048-5df2-395e-8def-36796efda368 | -5.05007 | -45.1647 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d16ed0a0-bfa3-3fa5-9188-1135d706960c | -5.04783 | -45.1572 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f876fd1c-cdc3-3ca9-a977-0a9bc747f20b | -5.04729 | -45.16069 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 845a05e7-20b3-3182-a9f0-86f6d0f75754 | -5.04674 | -45.16418 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 3c8417cb-f80b-3f2e-9bbd-1989679a49f9 | -5.04619 | -45.16767 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9c4491ab-0d96-33c6-91bf-46ba5c957e7b | -5.0445 | -45.15668 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4ec0fb6-d3f8-3847-8130-e5782686ff69 | -5.04395 | -45.16018 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aeec1720-c378-3ab2-94bd-b4b5c3b9ad24 | -5.0434 | -45.16367 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8622f805-8752-3bfb-888e-217444baa801 | -5.04286 | -45.16716 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9f3a792f-5aed-30f8-9f94-c7eda2cd58ae | -5.04062 | -45.15966 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03f9c79f-a709-353f-9531-ce0b375708ba | -5.04007 | -45.16315 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 76bc8163-81d9-339a-8a3e-81a4f31f624f | -5.03952 | -45.16664 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5cff4284-d0c0-3568-a803-08201398f95f | -5.03674 | -45.16264 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd6c92c7-13e0-35c6-a40e-a601eed90074 | -4.97517 | -45.55518 | 2024-10-31 04:25:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c5b0c37-c66e-34c2-9e75-f11876ef9978 | -4.93873 | -44.96453 | 2024-10-31 04:25:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb2195e8-893c-3c9c-837a-490d4f36f636 | -4.88266 | -45.90557 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 731bfbc7-6372-375e-a230-45270c595349 | -4.82863 | -45.84047 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e742d386-ec9e-358f-9733-043c503b91c9 | -4.82531 | -45.83995 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5437b104-7c1e-38e8-bf39-535600f0f90c | -4.82514 | -45.7762 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aa89f2f-3584-345b-ab34-7bc18f21e963 | -4.82477 | -45.84341 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ba318aea-e61f-3c6a-b590-17436ad0a9a5 | -4.8246 | -45.77965 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31c3f8f2-bda3-3658-a7c7-e89d819b6bb2 | -4.82423 | -45.84686 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 8b5b478a-b615-391b-a792-50f35a7ff9e5 | -4.82406 | -45.7831 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be90bd34-bb68-3a85-ae2c-6fd51056e3a4 | -4.82199 | -45.83943 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2c7094fc-7a75-3a4d-834a-0a4233628c1b | -4.82145 | -45.84289 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 06bdf4f2-a413-3889-be46-f3f98787e4a8 | -4.82128 | -45.77913 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4650ad3d-e0d4-3004-917c-24f563aa6ba1 | -4.82091 | -45.84634 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 037c7874-d03a-37ec-85b7-4d4e3fb4018f | -4.82062 | -45.74009 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2a08de2-69d7-3830-97f3-11c0bc858a69 | -4.82036 | -45.8498 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 7349ba17-b53a-3fb6-814d-38f81a85aca7 | -4.81813 | -45.84237 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 90c5497e-d839-3b2f-b1b3-1d976f5c6793 | -4.81759 | -45.84582 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 788b5432-aecf-374d-b64f-b924198abc7f | -4.8173 | -45.73957 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51818a64-5c73-3d88-b9d1-bb8ade9ce206 | -4.81704 | -45.84928 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a76424a9-d4fd-3877-aa16-3c268ae9a376 | -4.81427 | -45.8453 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 696a8cc8-34e7-398d-be2c-4a5ed0ba4c30 | -4.80674 | -45.72021 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d72a591c-9473-3b82-8f19-851fe6e74eab | -4.75985 | -45.75891 | 2024-10-31 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db1159bf-f193-37ef-ae7f-0f61f0a10f7c | -5.34272 | -46.24778 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e25d865-0ab4-38ad-8f9b-22fd1a04251c | -5.31 | -46.33101 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61010ecb-65a2-3737-b597-c0c87ed569a5 | -5.28973 | -46.15741 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f01b667-ced6-36ff-b3d7-2daf9137584c | -5.28918 | -46.16086 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7e334ec4-f639-34d2-a828-25db709b7ae8 | -5.28641 | -46.15689 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8fd03a1-7df8-3f39-a0b5-a6b82a8c78ea | -5.28586 | -46.16034 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1894e317-b346-3897-ba03-882fae8954a4 | -5.2722 | -46.24688 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05821c60-23ec-3c05-aac9-1f55c111a320 | -5.27165 | -46.25034 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 283d63dd-9e19-3825-af23-c1edaf837a97 | -5.22314 | -46.15048 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bbeda1a-998e-36c4-b883-2c5a08f84a54 | -5.19444 | -46.18143 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7507aae-336d-3939-a120-84ada1d6f4a4 | -5.14615 | -46.0994 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de95d494-1917-32ae-9d3c-7de22af2e28e | -5.11658 | -45.38584 | 2024-10-31 04:25:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d29db03-1b65-3db4-a666-325eb60543a3 | -5.08039 | -45.8307 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46ac7e19-27ad-3733-9593-4b7d6ac90253 | -5.07652 | -45.83364 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ad87801-60e8-3d23-870a-09d00488e309 | -5.06128 | -45.80289 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d0d8ec5-a666-32a4-80ee-20c613e1b6a0 | -5.05796 | -45.80237 | 2024-10-31 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
