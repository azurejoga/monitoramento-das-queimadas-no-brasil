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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 097fecfb-91ff-3a85-b776-d8cbe47afa80 | -6.4395 | -42.3383 | 2025-10-25 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| d01b1186-6b82-342c-8064-6af6dd14fbcf | -12.2348 | -50.1272 | 2025-10-25 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| a5fd52c5-29e3-3706-937b-d1541ef511f3 | -5.886 | -41.2847 | 2025-10-25 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 217.0 |
| 664edae8-802f-3fd9-b941-aeb10e676bd3 | -6.2854 | -40.885 | 2025-10-25 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 224.8 |
| 2786f397-0b1e-3d7d-a9a2-3f6347b5a88f | -14.3171 | -51.7688 | 2025-10-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| a5e493ef-a627-3466-a59e-3bb264ed3773 | 1.6753 | -55.6858 | 2025-10-25 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 15c5e06e-ce22-3689-9b0a-5e2d923a4300 | -13.6488 | -48.1845 | 2025-10-25 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 6fd81bf1-0155-3aa7-a207-86671c4388a6 | 1.657 | -55.7058 | 2025-10-25 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 89b3036a-42dd-3f70-8ea5-665b95446e91 | -6.5286 | -41.0567 | 2025-10-25 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 747e674d-2787-36e7-a3a3-1c5ee21014e7 | -7.7971 | -45.3893 | 2025-10-25 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6da4148e-38c6-3159-94ec-bdfe4f9dbddf | -12.8384 | -47.2543 | 2025-10-25 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 4b46af5e-0d01-3da5-9b61-050721bd8190 | 1.6386 | -55.7652 | 2025-10-25 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 225838c8-4628-35fe-a26b-910a864a0f53 | -6.2857 | -40.8606 | 2025-10-25 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 087ed89a-7c62-375f-9223-e894fb1742fd | -12.852 | -48.653 | 2025-10-25 14:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1770a43b-a91c-3d24-93fa-1364c06ede30 | -7.5713 | -47.1102 | 2025-10-25 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4103bafd-8023-3921-8195-577cf49ed971 | -4.8935 | -43.2115 | 2025-10-25 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 1bc72a3b-da07-32a5-948e-dc109281d160 | -14.2974 | -51.7927 | 2025-10-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 389ba3f2-f77c-35d4-9df7-f7313a05afff | -12.3901 | -49.9569 | 2025-10-25 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 77c9b682-64a4-3840-aee5-a7786ee98616 | 1.6386 | -55.7258 | 2025-10-25 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 60fdc3a4-6147-3eef-aa4c-84afefa3b073 | -8.0256 | -45.1625 | 2025-10-25 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 30cae079-822a-3bae-ac9d-a8b6b3fd328f | -6.9371 | -45.0362 | 2025-10-25 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 279e23a8-a7c5-306f-adbe-8c266c0116b2 | -17.4112 | -46.8881 | 2025-10-25 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 69d5e7b5-83e7-31f4-b0ad-073f94a0c306 | -14.4859 | -47.8982 | 2025-10-25 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 47.7 |
| d2de926d-29c8-38c4-abd7-a63e9579b10a | -13.0635 | -47.5575 | 2025-10-25 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 10b5b230-bca4-3dc7-8db1-24d81fa6474c | -11.5505 | -48.8005 | 2025-10-25 14:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 1465c02a-936a-34f6-8b07-3d1648b011ae | -6.802 | -45.4105 | 2025-10-25 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| bd6f3a6a-02d6-3a8c-bf59-41429bdf88c7 | -12.2863 | -47.0194 | 2025-10-25 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 04ca1ccd-3847-3fc8-b0d0-2152895b5e77 | -7.8238 | -40.256 | 2025-10-25 14:20:00 | GOES-19 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 132.3 |
| d2dc6186-a872-36b5-aa2d-301f58ee8fe8 | -12.3427 | -47.0788 | 2025-10-25 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 9efcd931-ac53-3bab-b6e4-30cf662d6f1f | -6.783 | -45.4347 | 2025-10-25 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 2e2c9497-ee1c-355e-ab7d-9cdb482b087c | -6.5475 | -41.0549 | 2025-10-25 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 270.8 |
| b5bffdd3-c65c-368e-aabd-52631e0c2f8d | 1.6386 | -55.7455 | 2025-10-25 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 97679567-86e7-3ecb-abd8-8db8ec13e43f | -14.2974 | -51.7927 | 2025-10-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c9cf23d4-446d-3aa0-bd2e-e75eebea2ddd | -12.852 | -48.653 | 2025-10-25 14:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 49e35536-e78d-311a-9a9a-da4fbb74d059 | -3.3103 | -42.3374 | 2025-10-25 14:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 854f8f60-f2e9-34bb-b82b-a768dabf3cd4 | -11.927 | -50.3147 | 2025-10-25 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 08d4e0c2-ce2d-3454-a4d1-36435bd8e53c | -14.3792 | -51.5255 | 2025-10-25 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4759c1ca-73d3-3e3f-ba4c-f691e144a301 | -12.8384 | -47.2543 | 2025-10-25 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 733c461c-189a-332d-a6ee-5582472de27a | -8.5444 | -47.3745 | 2025-10-25 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 634b19e1-5564-3912-93a7-c85939fb3dd6 | -12.0862 | -46.4162 | 2025-10-25 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a4d66495-c8c4-3218-a945-92377b3c7cfa | -6.8017 | -45.4332 | 2025-10-25 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 4a744a48-3181-337e-a9d0-cf7c3eba8164 | -11.327 | -53.9254 | 2025-10-25 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| af170212-8b11-38e0-8f2f-69ddd89e960e | -7.5525 | -47.1119 | 2025-10-25 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 0faf2298-5418-33b9-b6fd-fc6f4c90a334 | 1.6753 | -55.6858 | 2025-10-25 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 145311c2-6681-38fb-9cd9-ab0a5f202351 | -14.2978 | -51.7713 | 2025-10-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 75ed1c2c-5d6c-38b9-afa8-fa0216add695 | -13.6488 | -48.1845 | 2025-10-25 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f0fce622-6daa-3e31-8481-c76e9ea54754 | -13.8953 | -48.4141 | 2025-10-25 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| f8c9e043-5783-3c8f-b1c6-bfb3b73a4dab | -12.2863 | -47.0194 | 2025-10-25 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e930f6cb-5933-3040-a939-217688d4f1a5 | -4.8933 | -43.2349 | 2025-10-25 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 7a68bb13-6cbc-33fd-9cfb-2469976d1815 | -5.6055 | -41.1145 | 2025-10-25 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 150.4 |
| 66525c34-4986-38fa-8488-55988515a4b9 | -9.8624 | -44.8886 | 2025-10-25 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| f4d6c5ea-e6ed-3d7e-832c-d2e009ff5186 | -7.7822 | -48.4058 | 2025-10-25 14:30:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| fb2fccfc-cb01-3213-841d-83581114c0e6 | -9.3086 | -45.1841 | 2025-10-25 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 3442309b-5564-3abe-8486-7feb1495ee45 | -13.0635 | -47.5575 | 2025-10-25 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 5d32af17-089b-3e30-91a9-1dcf98d2f92b | -4.8935 | -43.2115 | 2025-10-25 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 14825fb1-4fb7-333d-bcc5-0e62a4776d04 | -4.8931 | -43.2582 | 2025-10-25 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 7f782d8b-46bf-34e8-ae7a-68ce0fa9b6f9 | -14.9041 | -52.4566 | 2025-10-25 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3bdb144a-91eb-35e9-908c-a914baf35829 | -6.783 | -45.4347 | 2025-10-25 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| dbe439a0-aae6-3ed1-a43b-a438a74f39fa | -4.912 | -43.2337 | 2025-10-25 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| e63d9175-f2e8-3af1-b961-05171bffed4b | -14.3171 | -51.7688 | 2025-10-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| f9cccb64-9057-3dbf-8f31-d8e76b89de65 | 1.6386 | -55.7455 | 2025-10-25 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7b2c9fac-6e3c-391d-8d89-ec801eaf4465 | -4.2488 | -44.5648 | 2025-10-25 14:30:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 0ceb19f5-5bcf-3282-9081-bdc391d7406f | -6.802 | -45.4105 | 2025-10-25 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 15e511bc-e50c-3f7b-a335-3db1492ff7e8 | -6.2854 | -40.885 | 2025-10-25 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 407.6 |
| 1e126b1a-ff49-309e-9e59-2408545d176e | -12.2348 | -50.1272 | 2025-10-25 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1786b6cd-6269-30fa-931d-b558b215cc15 | -6.5475 | -41.0549 | 2025-10-25 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| ef2d73ed-8775-36f4-a49a-6b5697d88ce4 | -6.2857 | -40.8606 | 2025-10-25 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 166.9 |
| fd71a1d6-f8ed-3b91-a4b1-2627d5466456 | -9.3089 | -45.1612 | 2025-10-25 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 1d02446a-571a-3507-8408-601aa637223c | -12.3427 | -47.0788 | 2025-10-25 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| bc5c9749-0b7d-38ed-8da3-912919b7578c | 1.6386 | -55.7258 | 2025-10-25 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 93a95199-f8f7-31f3-9181-7adad94eb4f6 | -12.0545 | -47.1415 | 2025-10-25 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 9043f523-13f5-3a8a-ba78-796173b194c2 | -14.3744 | -51.8038 | 2025-10-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 6b6c7659-5dd5-3a32-a84c-e414e25a1b51 | -7.9341 | -48.219 | 2025-10-25 14:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| b3c3024f-f001-3c47-b404-3f0c322e0423 | -13.9147 | -48.4112 | 2025-10-25 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c252de0e-3e14-3737-8b78-1a5cd18626d5 | -11.8724 | -50.1493 | 2025-10-25 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 54e0a3f3-9c49-3150-968a-9fc3c6bddc87 | -11.8727 | -50.1277 | 2025-10-25 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 80726bd9-883f-3a41-b0c4-524db6920bf4 | -12.3133 | -45.516 | 2025-10-25 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 9a8fd5f5-089a-386c-859a-5e5583878566 | -14.9045 | -52.4354 | 2025-10-25 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 6276f42a-b7fe-314f-8d78-dbb79d74707f | -8.183 | -47.7602 | 2025-10-25 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 0af10ec5-71a5-3362-8f43-208070dbbe23 | -8.135 | -47.0376 | 2025-10-25 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| df826b56-0986-3006-ab94-f87dc774b5a1 | -12.2475 | -47.0473 | 2025-10-25 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| a9900cc6-3aad-3d1e-8fed-f66ee4e32a47 | -7.7824 | -48.3841 | 2025-10-25 14:30:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| a30a160c-1af9-3bf2-8748-10979d09e7da | -12.8327 | -48.6557 | 2025-10-25 14:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |


