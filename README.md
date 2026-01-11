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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a049559f-397f-305c-912f-d8cd71ae4119 | -11.8534 | -57.3582 | 2026-01-11 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 10bd853a-9311-337b-aa5b-3f7e1955d19f | -12.4133 | -58.049 | 2026-01-11 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| f8576fe7-a9a6-3dc5-9d35-69d93437f9a2 | -18.832 | -51.6099 | 2026-01-11 00:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| ae5083f2-26e2-3a23-96e4-d927d490ca02 | -18.8119 | -51.6134 | 2026-01-11 00:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 435a1281-3345-31e8-b1cb-b25f74f8cddd | -11.8532 | -57.3781 | 2026-01-11 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 22fa614a-c1a8-34f4-8444-6a9534c748d9 | -12.3943 | -58.0506 | 2026-01-11 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| a250fcf9-8122-3ec2-8cd3-bc0bb20809b0 | -12.4135 | -58.0292 | 2026-01-11 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a9023c42-00c2-3fd7-a66b-3f22f5158f13 | -12.3946 | -58.0307 | 2026-01-11 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 59fd9962-0f71-30ef-ae80-388fbd9a6e56 | -11.8723 | -57.3566 | 2026-01-11 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 612a194c-c6d7-38b9-b92d-aa325e7f6092 | -12.9041 | -52.515 | 2026-01-11 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 49d9f2bf-d369-3e8b-afc5-afb6a8e3ba16 | -18.8119 | -51.6134 | 2026-01-11 00:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a4bc8fba-759c-3802-85c0-21fdb4d110fa | -11.8534 | -57.3582 | 2026-01-11 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 77ff0506-5ad7-3bb5-8719-dcfbafce82d9 | -12.4135 | -58.0292 | 2026-01-11 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5253cc4e-d451-3b58-adfb-bd56d4f2fec1 | -11.8532 | -57.3781 | 2026-01-11 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 3e988e01-357c-3660-b016-702b24b05290 | -18.832 | -51.6099 | 2026-01-11 00:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 6bb5d830-1494-3fe3-a8ac-e8e94ef80842 | -12.4133 | -58.049 | 2026-01-11 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 2ff81777-ea72-3c0a-9030-ac791e0f9206 | -11.8721 | -57.3766 | 2026-01-11 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 3bac73d2-5051-30e2-a2bd-07112dafa6dd | -12.3943 | -58.0506 | 2026-01-11 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| afb1a169-5912-30d6-91b3-b22092cc3afe | -12.3946 | -58.0307 | 2026-01-11 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| acc11a4e-2d28-35cb-945d-dec9981841b9 | -11.8534 | -57.3582 | 2026-01-11 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 9e98cf88-5755-305e-a0f4-9ab52b86d047 | -12.4135 | -58.0292 | 2026-01-11 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 18ed792a-bfe5-3668-b3eb-fbe276302214 | -11.8723 | -57.3566 | 2026-01-11 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 2dadd486-7141-31e4-9860-390cf0da9099 | -12.3943 | -58.0506 | 2026-01-11 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 9cc9c6e7-277a-349a-9b58-012a7f6a60d2 | -11.8721 | -57.3766 | 2026-01-11 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1b8916fb-8864-3c0c-b876-07c69f04d0c3 | -12.9041 | -52.515 | 2026-01-11 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| df67a13d-71cb-36c8-90d7-ce11c3767be0 | -11.8532 | -57.3781 | 2026-01-11 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| cf93e45c-48a7-3056-a815-4512616b7650 | -12.9038 | -52.536 | 2026-01-11 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 59a100d0-6003-3b5e-b926-dedecda9b0ae | -12.4133 | -58.049 | 2026-01-11 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| fdb44d86-7388-3edb-80e9-156c9f289f1f | -12.3946 | -58.0307 | 2026-01-11 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 12c9c253-784e-31e0-a3f2-036d4d6fecf2 | -12.9041 | -52.515 | 2026-01-11 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 94060019-f494-31c4-9025-37f537b76067 | -12.3943 | -58.0506 | 2026-01-11 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| aadf32ce-7e2a-3932-8182-9f399cc89282 | -11.8532 | -57.3781 | 2026-01-11 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 7a3cccf4-a82f-3483-936e-7df107d3ebd6 | -11.8723 | -57.3566 | 2026-01-11 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a343a4b4-0394-3dbb-b098-8f049812946c | -11.8721 | -57.3766 | 2026-01-11 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8d485f71-2a52-3ec6-ac12-d0f6628514dd | -12.9038 | -52.536 | 2026-01-11 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d5a4df61-d72f-3465-b3c9-ee3dea73bdc4 | -20.2356 | -46.4685 | 2026-01-11 00:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 37d937b0-6fe0-3cd3-9b20-4dc3d720deba | -11.8534 | -57.3582 | 2026-01-11 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 12c57175-687b-3971-9beb-85038f06e1ae | -2.2512 | -47.958099 | 2026-01-11 00:38:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e08ce65d-8a65-3258-8d6b-125e33821d79 | -0.0911 | -51.266102 | 2026-01-11 00:38:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6cb42370-63ee-3734-886e-650f6c827273 | -2.6166 | -43.089401 | 2026-01-11 00:38:00 | METOP-C | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 997dc3b2-833e-3916-923e-8b9869f0506e | -2.1859 | -52.0079 | 2026-01-11 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 998135a8-643a-3860-93b9-19ac299be59e | -0.0847 | -51.283298 | 2026-01-11 00:38:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0d604080-5f9e-3c73-858d-9f6df6e6cb38 | -2.1879 | -52.016399 | 2026-01-11 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99cdd838-9571-3315-b45c-381967e056c7 | -2.6971 | -45.509602 | 2026-01-11 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f78eb6cb-58ea-36c9-b07b-7913a7b37805 | -18.8144 | -51.599899 | 2026-01-11 00:38:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 41eba85d-8296-3965-984f-6f029cbd3ef2 | -20.2316 | -46.474899 | 2026-01-11 00:38:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bdc51285-78c4-3543-8ab3-41b9868b2001 | -22.595301 | -43.311298 | 2026-01-11 00:38:00 | METOP-C | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b968449a-4cc3-3de5-b3bd-bf0fca3325c4 | -0.274 | -48.779499 | 2026-01-11 00:38:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6f29916-653a-3b3f-ad9a-f173a7aca7e9 | -5.4608 | -45.286598 | 2026-01-11 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67e04075-4ad6-392b-931f-c0928e91d19e | -2.1957 | -52.005699 | 2026-01-11 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b200d385-3307-373e-92b6-8329e1dd2df1 | -18.816999 | -51.613899 | 2026-01-11 00:38:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 89dbcbc2-d059-3905-9d38-cdfc8b8d9c18 | -3.5547 | -43.664501 | 2026-01-11 00:38:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b87c2731-a5dc-3e3c-8e5b-aee00533b07b | -20.233299 | -46.4827 | 2026-01-11 00:38:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1e07b324-ef71-37b7-a96b-0aa668501d24 | -0.0945 | -51.2812 | 2026-01-11 00:38:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 734ed57c-9594-357b-95aa-e2b8364f4508 | -1.0238 | -47.687698 | 2026-01-11 00:38:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43489dfa-c93d-3415-a4cb-44a2f894fe10 | -2.2496 | -47.951199 | 2026-01-11 00:38:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c113763-0419-38d6-8922-b50636989905 | -2.184 | -51.999298 | 2026-01-11 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 998e368b-3ea8-3d78-9bef-e0542664646e | -20.23 | -46.466999 | 2026-01-11 00:38:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ff0a2e19-fb20-33b8-8efc-252362b7f43d | -3.5524 | -43.654598 | 2026-01-11 00:38:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 197b59ac-c215-37f7-845c-841831bc82d8 | -2.699 | -45.517601 | 2026-01-11 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 074b61d4-d27c-3ac3-a88e-4e098c8b0c1e | -0.083 | -51.275799 | 2026-01-11 00:38:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 21a113ee-df83-348e-b88e-71d2bcc03a67 | -20.247999 | -46.504101 | 2026-01-11 00:38:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4e14a6a3-760a-3475-b76a-48f752949302 | -17.759899 | -43.4277 | 2026-01-11 00:38:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8c463d05-4eaf-3b34-87d9-ea31694682fb | -17.7582 | -43.4202 | 2026-01-11 00:38:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6356ce9e-aae9-35ea-9f47-a169f4bd7506 | -11.0771 | -48.2607 | 2026-01-11 00:38:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38cbbc76-d2aa-37b8-8c0c-0c3e30c243c3 | -18.826799 | -51.612 | 2026-01-11 00:38:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9782fb2d-aadc-3caf-8435-a7e02bf96c24 | -0.2755 | -48.786301 | 2026-01-11 00:38:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a115200-fe9a-3828-9160-e92be785881d | -1.8433 | -54.302299 | 2026-01-11 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6962587e-492f-378f-a85a-539272731c1a | -11.8544 | -57.353199 | 2026-01-11 00:38:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abc3a98b-48b0-3a4f-9f60-11a3dcf48708 | -1.266 | -45.739101 | 2026-01-11 00:38:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7206b3fb-fbf5-31f0-96f4-328fa0566d38 | -22.597 | -43.318802 | 2026-01-11 00:38:00 | METOP-C | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80a97b94-e213-39e6-be08-49652e8ede79 | -2.6192 | -43.100399 | 2026-01-11 00:38:00 | METOP-C | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 945ae3da-a839-3168-9e5b-5dac63d21a61 | -2.7088 | -45.5154 | 2026-01-11 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c566f61e-31cb-3436-bf6d-eec753f12842 | -0.0928 | -51.273602 | 2026-01-11 00:38:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a381cfba-6d65-3ed2-bb5e-450480248ebc | -5.8563 | -44.9478 | 2026-01-11 00:38:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e956945c-558f-3477-b425-6048c8dc3bd2 | -11.8534 | -57.3582 | 2026-01-11 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 80879200-abd2-377a-82b2-a37eda684767 | -12.9041 | -52.515 | 2026-01-11 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f399377e-e8b0-30ef-a5e6-85809e8456ee | -12.9038 | -52.536 | 2026-01-11 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c3bb0ef9-b1f6-382e-a8d4-f2659557a288 | -11.8721 | -57.3766 | 2026-01-11 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6126e1c9-6dc9-3209-b982-2f01d4316ee3 | -11.8723 | -57.3566 | 2026-01-11 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9d5963b3-7d6d-306a-a4d1-b0e5bc0dec1c | -11.8532 | -57.3781 | 2026-01-11 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 0b2c7ddb-4a5f-301b-93e0-a2383f402aa4 | -20.25137 | -46.51207 | 2026-01-11 00:47:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a453c7d7-5f66-3001-9ad1-c9658e0cef1f | -20.22946 | -46.45848 | 2026-01-11 00:47:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 05321657-3b64-315d-ae9f-b1b9c134cf2e | -20.23562 | -46.47076 | 2026-01-11 00:47:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 84.4 |
| fbd78e6f-13dd-3f9c-9c3f-60c36a887282 | -20.23903 | -46.48957 | 2026-01-11 00:47:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 224ff0b5-6e21-34cc-a3f7-c273b8cf95da | -20.23271 | -46.47716 | 2026-01-11 00:47:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 3fc0d2ad-7461-3d88-b2c1-200689f7d5e0 | -11.8569 | -57.38258 | 2026-01-11 00:49:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 73fb2c73-51b4-35a4-89b8-dfd79798e775 | -11.86515 | -57.37034 | 2026-01-11 00:49:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dcc4901f-902e-3cf9-ab53-9137d512b304 | -12.90617 | -52.53396 | 2026-01-11 00:49:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 2387a6f0-0f08-3390-b977-60140f0104a7 | -11.85549 | -57.37166 | 2026-01-11 00:49:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 89248d93-b709-30a9-a0f6-8cbd84fd03f4 | -12.89808 | -52.5311 | 2026-01-11 00:49:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9303381f-4d25-358b-985d-a63ae617ea14 | -12.91391 | -52.52274 | 2026-01-11 00:49:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7cee569f-4829-3348-bbfe-857658ca4105 | -12.91535 | -52.53252 | 2026-01-11 00:49:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a4155fb4-a35e-32a8-aad1-d2142578396f | -16.58963 | -58.22074 | 2026-01-11 00:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 134a2b79-a08a-3165-b576-ad73a0f310a5 | -12.90472 | -52.52417 | 2026-01-11 00:49:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| aaa414d4-1a8f-391d-865b-5bbe391642a7 | -15.61844 | -58.21564 | 2026-01-11 00:49:00 | TERRA_M-M | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d7f0a631-18ad-3510-8e6d-34bc3c92c7c0 | -16.10277 | -56.75149 | 2026-01-11 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 436f3bd5-4f5a-3637-ac80-2f4130e6a844 | -12.89667 | -52.52129 | 2026-01-11 00:49:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ef91901-ff94-388d-bb66-ea32b9c3cf91 | -16.59115 | -58.2148 | 2026-01-11 00:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 0439f209-1d7e-3b35-8ab8-09f7adf32303 | -15.53631 | -55.76234 | 2026-01-11 00:49:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README2.md)
