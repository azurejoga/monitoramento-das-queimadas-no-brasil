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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b51974d-ba63-3191-8b0f-78cc8ab892e3 | -14.3506 | -53.2243 | 2026-08-12 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 09e238f0-1335-3878-93bb-0845e227db3a | -11.9358 | -47.3814 | 2026-08-12 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 01cb27dd-9d37-3ea0-bcfa-1cb9815f7f90 | -14.4313 | -53.0041 | 2026-08-12 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 180.9 |
| a857ba04-7229-3591-818c-a1363464d6a7 | -14.4309 | -53.0252 | 2026-08-12 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| e6fee805-016f-34a1-a1ae-b2c6799e46f9 | -15.4623 | -53.7972 | 2026-08-12 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c86a8b0b-a6f3-37a2-87f8-e5c9bc233345 | -15.171 | -52.6967 | 2026-08-12 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 174.8 |
| d028e7d7-2aba-3d23-bc42-784e7323a7ab | -13.6273 | -46.2948 | 2026-08-12 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 333.1 |
| 542b0b46-ead9-3cb5-b80e-b477a998acf1 | -11.7902 | -51.8611 | 2026-08-12 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| fdb20a03-2c61-3273-886c-c99f5ce5d7fd | -9.3534 | -47.4475 | 2026-08-12 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 261.5 |
| 9135c2b6-30cf-3fba-8087-81a248e2caea | -14.3695 | -53.243 | 2026-08-12 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 264.9 |
| 9bfa009a-2851-3989-bf11-df8e55b0d566 | -14.2938 | -52.0061 | 2026-08-12 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 1c316814-5503-328d-8b97-503e44dd35cb | -14.3131 | -52.0036 | 2026-08-12 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 376.3 |
| f3ff2361-8ba7-37cc-a6d6-4614e5121d2f | -14.2941 | -51.9848 | 2026-08-12 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 150.0 |
| dd62a78c-73d7-30a8-828f-819c0da53b82 | -11.8859 | -45.831 | 2026-08-12 14:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| fe40caca-5348-3495-998a-b2ee9bb49334 | -14.3699 | -53.2219 | 2026-08-12 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 68057135-3f72-3700-95e1-b2d8935951b7 | -6.5438 | -43.1547 | 2026-08-12 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| c932ca84-b2ef-3493-8967-365715ed3b78 | -11.7905 | -51.84 | 2026-08-12 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 205.2 |
| 23b450c7-078c-344e-b3e4-91c5f5f8a0e6 | -9.3339 | -47.4937 | 2026-08-12 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 546a7fdc-12a1-3dd5-9ac6-d5dc4347d92c | -14.8433 | -52.6131 | 2026-08-12 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 175.1 |
| fb0694f9-f88c-362d-b32f-ff11db8ebe34 | -11.9535 | -46.3444 | 2026-08-12 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 65395758-eae6-38cd-a3c6-6540c101bc29 | -14.3506 | -53.2243 | 2026-08-12 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| de44a1f4-a475-37f7-b113-3aaadd034e97 | -6.5443 | -43.1078 | 2026-08-12 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 347.1 |
| 8257f346-1334-3b12-8ead-a61ccabe00bc | -15.171 | -52.6967 | 2026-08-12 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 317.7 |
| ba5b1cbe-b134-3409-909c-b04cba7064d9 | -6.5255 | -43.1095 | 2026-08-12 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6047fe22-1d0e-3d77-af7f-dafaccda7ae1 | -6.544 | -43.1313 | 2026-08-12 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 748.9 |
| 40792797-6578-3875-a450-caa23b3d7a8e | -14.3135 | -51.9823 | 2026-08-12 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 266.8 |
| f1d49d78-ea43-35e7-a434-725ba4f195b4 | -14.3631 | -53.6417 | 2026-08-12 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| b2547bf8-d359-3f64-9272-038b2d306c51 | -12.1771 | -50.1557 | 2026-08-12 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 1d5fe724-d51f-3021-8177-c2924efc0834 | -7.0008 | -42.6417 | 2026-08-12 14:30:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 5f1677f7-5ed7-396b-b008-a165883bbd41 | -9.3531 | -47.4696 | 2026-08-12 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 332.4 |
| 99e7f9a6-330b-36bb-9d82-221804b81fa3 | -11.9343 | -46.3472 | 2026-08-12 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 09829c4f-e78e-3cbb-aed2-14f01aa9b837 | -11.029 | -45.6765 | 2026-08-12 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 58204d4c-5d63-368c-b81f-60ca0dfb3536 | -9.3336 | -47.5158 | 2026-08-12 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| eb159e46-29b7-35f5-aa7b-bd32feb2c3e1 | -13.6268 | -46.3177 | 2026-08-12 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 148.1 |
| b1040a9f-3af3-3295-a9be-48ee5fe16829 | -15.3808 | -52.9015 | 2026-08-12 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 456f1fa1-bb6f-3eec-928f-3d5b2260e33a | -15.1714 | -52.6754 | 2026-08-12 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 2d172008-7583-3918-bf93-c46f63ed2cec | -10.8445 | -50.3509 | 2026-08-12 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 7ead6790-5928-338a-9275-27f38a2e9a7a | -14.3109 | -52.1314 | 2026-08-12 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 68bd41e5-55ce-3396-b808-e830ed7d7a5a | -14.3502 | -53.2453 | 2026-08-12 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 62df9ad4-4b8a-3103-be86-a469afc64406 | -6.5631 | -43.1061 | 2026-08-12 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 193.0 |
| f1fbb6e4-76ec-34a8-bfff-6bb03448e119 | -11.0286 | -45.6993 | 2026-08-12 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 371.9 |
| b3bcecb7-417e-3607-8eca-ff4e85ab630a | -14.489 | -51.8738 | 2026-08-12 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 93867e9f-b3f8-3352-a5c2-d30dace6b0c3 | -14.3695 | -53.243 | 2026-08-12 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 252.2 |
| e7ba162d-2001-3e0b-a9d9-c20e6b04215f | -11.9911 | -46.3844 | 2026-08-12 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 0d0cebb7-cbe6-34e0-8df7-d3eb81ff7bb3 | -14.2941 | -51.9848 | 2026-08-12 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 8a7710a9-5f25-3bc5-9998-ab1076295ca9 | -9.3333 | -47.5379 | 2026-08-12 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| b8d86858-5cab-3b81-a328-9399dfcb45e8 | -11.6013 | -54.6782 | 2026-08-12 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| caa8858d-2d74-3c94-820c-d520ac1c5fd0 | -11.8859 | -45.831 | 2026-08-12 14:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 5315eeee-0b76-3993-96c7-d4513eba0964 | -14.3131 | -52.0036 | 2026-08-12 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 253.9 |
| 05ee3b20-bdb9-30c3-bbba-9a651ca72f6a | -11.9535 | -46.3444 | 2026-08-12 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ec797a5a-cfd0-3936-b3b2-9591be34883d | -15.3808 | -52.9015 | 2026-08-12 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| df193991-9108-33d3-ab05-ac4f09e0328e | -11.6015 | -54.6577 | 2026-08-12 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 52d23d73-2c30-3e8b-9ea2-555e547a7194 | -14.3502 | -53.2453 | 2026-08-12 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 171.1 |
| e1e9c1c5-8c1f-3bdb-a161-714e35f2f81b | -15.1714 | -52.6754 | 2026-08-12 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 564f70f9-0da6-3afc-a734-6314ff1a70a9 | -11.644 | -50.1546 | 2026-08-12 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 2ac7fb69-6ab5-3c79-9658-0d97bf056022 | -6.5438 | -43.1547 | 2026-08-12 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 96a0222d-290b-3da9-9142-b2320ef546ed | -14.4309 | -53.0252 | 2026-08-12 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 251.2 |
| 34b07927-e1a0-3936-849f-e6013850991f | -7.0008 | -42.6417 | 2026-08-12 14:40:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| d9b96fb8-6484-353a-9919-8b3ce1a0de2a | -12.1771 | -50.1557 | 2026-08-12 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 6482091a-904f-3904-811c-6f45ab9c17e0 | -11.0286 | -45.6993 | 2026-08-12 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 7ed84170-d71d-336c-a082-b839237deca5 | -15.171 | -52.6967 | 2026-08-12 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 434.1 |
| 479f8c54-d42e-3e41-a566-7ab9bb2d83c0 | -14.3893 | -52.0574 | 2026-08-12 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 56870f57-f3ad-3be7-9b7f-7db4d0002394 | -11.9719 | -46.3871 | 2026-08-12 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 042b8fc3-3f7e-3f44-afa3-5e813009b6c1 | -6.5183 | -45.6817 | 2026-08-12 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| d4eb3377-961a-300a-8607-eaaf7f5ed559 | -9.3336 | -47.5158 | 2026-08-12 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 251.6 |
| 48353181-bdfe-3872-a281-a3a04aa02fdd | -14.3109 | -52.1314 | 2026-08-12 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5f61db84-ecff-3017-9ae7-1f9bafabade7 | -14.3699 | -53.2219 | 2026-08-12 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e1c48068-6afa-3bff-bec4-21d302e78185 | -9.3528 | -47.4917 | 2026-08-12 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 9dd4f25e-f470-38d1-b3bc-66e1b470e31d | -6.5626 | -43.1531 | 2026-08-12 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e15c39da-920c-39f0-9aed-bdee3d733b88 | -6.5443 | -43.1078 | 2026-08-12 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 423.7 |
| 633c8bee-e485-378c-90a9-73c8da8f8e82 | -11.9343 | -46.3472 | 2026-08-12 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| a558cf4b-d291-3f37-bb07-e987210ec323 | -15.1901 | -52.7153 | 2026-08-12 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 90ae244d-87c5-39f0-8442-ca0f5a049d5d | -15.1707 | -52.7179 | 2026-08-12 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 876cfae4-cf12-30ff-876b-620bab905faf | -14.3375 | -54.0409 | 2026-08-12 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 00768c25-d6ee-3726-8db8-23053f1757de | -6.5255 | -43.1095 | 2026-08-12 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 4b6c631e-5e17-3409-b5b9-8ff902507430 | -14.3901 | -52.0148 | 2026-08-12 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| eefd0864-8c41-30bd-8268-7e63296e6562 | -10.8445 | -50.3509 | 2026-08-12 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 762e7acd-a51e-3853-800f-9bd8122af495 | -9.3339 | -47.4937 | 2026-08-12 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 280.3 |
| 51da4885-bde2-3ca0-a34b-7694bd772175 | -13.6273 | -46.2948 | 2026-08-12 14:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 567e8033-3e53-3b4b-b412-9cbcb48ad355 | -14.4313 | -53.0041 | 2026-08-12 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 383.0 |
| e8f28c58-3d8d-322b-912b-d09393e9edb6 | -6.5631 | -43.1061 | 2026-08-12 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 7dc4cf79-7b7f-3748-a278-66628d3fad4f | -13.6268 | -46.3177 | 2026-08-12 14:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 0e7fd0e7-5c79-35c9-859f-ef8ffd7cd329 | -14.3135 | -51.9823 | 2026-08-12 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 170.3 |


