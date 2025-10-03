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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d213163-6de9-3df5-b4d3-56b744b7e825 | -13.3418 | -48.1188 | 2025-10-03 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 3153cbc0-88a7-3af2-8348-d8c644326760 | -15.7905 | -43.7155 | 2025-10-03 14:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 269.7 |
| 86d8d129-f411-3dec-8b74-fd5b9f58a117 | -11.5687 | -47.6526 | 2025-10-03 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| fe36e6a7-2ebf-3943-893a-6b695473a904 | -9.9394 | -43.5777 | 2025-10-03 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 723c6601-5ead-3b42-bdef-793639e4529a | -11.4792 | -45.0174 | 2025-10-03 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5fec30d2-f74d-344f-8c2a-f25741dcfe0b | -14.0037 | -44.9376 | 2025-10-03 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 150.3 |
| af801bf0-5854-30b6-a47f-12bcc6198f95 | -8.8222 | -44.8043 | 2025-10-03 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 0e8e0f71-7016-35da-a663-a8ae4059c99d | -9.8772 | -47.8103 | 2025-10-03 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| afb0a97c-4f3d-35fe-b767-5e351b1f1838 | -5.8927 | -42.5273 | 2025-10-03 14:10:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| f8e648c1-6e38-3314-b5b1-0380a97e9d98 | 3.9534 | -59.7206 | 2025-10-03 14:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 53c5856d-99ba-3a53-9336-b45596ba499d | -5.704 | -42.6369 | 2025-10-03 14:10:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 9d814b35-3738-3fbf-b800-099febd1643c | -10.0148 | -50.2443 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7029a4ae-ae0f-39a7-bad0-0ace47e0fc3c | -8.8343 | -46.7694 | 2025-10-03 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 794bfa79-00c5-37cb-80ab-e37c07a0cad6 | -10.8524 | -47.2094 | 2025-10-03 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a59daf30-1469-30a3-a519-e30601ca7563 | -16.0413 | -50.9177 | 2025-10-03 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| bbbd2f99-ad26-3118-bdca-62d55318cb57 | -12.7822 | -50.5328 | 2025-10-03 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 2c4a951b-a442-395b-bbd3-7ef97d5870ee | -14.8063 | -51.424 | 2025-10-03 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 7bcf38d5-64fd-3f6f-859c-420d468975fb | -11.863 | -44.9612 | 2025-10-03 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 34a55532-16ef-39dd-aa0d-69e4430cf496 | -13.38 | -48.1354 | 2025-10-03 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 26f8b608-4d2b-31df-95e6-fe4d4b2de2e1 | -6.0621 | -42.4897 | 2025-10-03 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 3fbcb940-5319-3564-a432-ac19fc329929 | -7.3101 | -45.2531 | 2025-10-03 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 37221b83-f267-3d41-b9bb-5106d3aa0867 | -12.122 | -43.4215 | 2025-10-03 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| a6b92e55-20c7-317a-aff0-36ae991243f6 | -16.0583 | -51.0454 | 2025-10-03 14:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 2e84e723-3189-36d9-9aa1-cf469d8c5b67 | -9.4747 | -45.484 | 2025-10-03 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 7e6fc04d-ed7a-33f8-abc4-21a1edad26d1 | -13.155 | -47.8121 | 2025-10-03 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 74f95930-83fc-3c72-8169-843a1ad175a7 | -8.9948 | -47.4845 | 2025-10-03 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 8f861fc1-27ea-30ac-b1ef-0d662a619112 | -9.9391 | -43.6012 | 2025-10-03 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 578f53ba-2817-3f08-94eb-4e29332267c4 | -8.9118 | -46.6052 | 2025-10-03 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c3242c82-01d5-3124-a2ec-8c218c479bce | -14.6526 | -48.2964 | 2025-10-03 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 17e6b66b-0a46-3895-9d16-a06ff1088ee4 | -10.1089 | -50.2563 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 3bbcdd93-860e-3e64-b4b9-433eb8e1c3cb | -8.1888 | -44.1588 | 2025-10-03 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| c6eec6af-a72d-3195-8b30-b1e2491881f6 | -13.8447 | -51.2328 | 2025-10-03 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0d3e95c5-ae98-3b7a-9f7b-0bb6f70c9e36 | -7.4469 | -46.4777 | 2025-10-03 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 556476b7-a24a-3005-8f09-86ac1c9b9448 | -5.7033 | -42.7077 | 2025-10-03 14:10:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 89bb6b7c-c07c-3071-b4aa-c287f3b7e553 | -12.1215 | -43.4453 | 2025-10-03 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| e7bd688c-ede8-3e7d-8d93-cbc4cf8d49fc | -6.0806 | -42.5118 | 2025-10-03 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 132.4 |
| f6b5f79b-b60d-324f-a2db-7db370ce6f4b | -6.8761 | -45.4947 | 2025-10-03 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 2bef8808-7bdd-3791-8dc2-3a23b79d8c9c | -7.7944 | -42.5132 | 2025-10-03 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 124.9 |
| b7f9e6ab-cc1e-382b-be54-f54fd8c456ab | -9.3547 | -45.951 | 2025-10-03 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 9402310f-d5d9-351c-b697-5dbc48e10be5 | -9.4747 | -45.484 | 2025-10-03 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| e944e704-163e-3cdd-85d0-1e686ea5db7e | -9.9031 | -45.978 | 2025-10-03 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ab165519-8dcc-3887-9e26-b0b42c746895 | -6.6787 | -42.8372 | 2025-10-03 14:20:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 078d0a03-f034-3fef-a73e-5f9187b06a7c | -8.8732 | -46.6762 | 2025-10-03 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 9355f046-d121-33aa-a716-94e181d8434c | -6.7167 | -42.8101 | 2025-10-03 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| f88f8924-b191-3309-8b87-e893dd560e17 | -15.8097 | -43.7355 | 2025-10-03 14:20:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 91.0 |
| d7ac3fbd-a9b8-3095-bc29-100cfc600824 | -9.9365 | -43.7657 | 2025-10-03 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| af0bb14b-7c30-376c-a38a-21d983436243 | -7.2845 | -44.18 | 2025-10-03 14:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 4454d24b-fce3-3753-a73a-d1e672571ff5 | -5.7323 | -43.6409 | 2025-10-03 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| a43300bb-e8da-3ada-aeb2-ed621f21da7a | -9.3389 | -45.7266 | 2025-10-03 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1db00874-3b5f-3cfb-86ef-51351d334c6c | -14.2934 | -45.9307 | 2025-10-03 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 0ce11a53-bbda-392e-822d-37a8d8918497 | -11.8626 | -44.9844 | 2025-10-03 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 7b91bbbc-22e5-37ef-b85d-eb45d4cdfa27 | -16.0408 | -50.9395 | 2025-10-03 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 32c7883a-8911-33c3-9610-16848d9152d2 | -8.8343 | -46.7694 | 2025-10-03 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| c493274c-1984-3697-b9ef-aa1d29fb7a91 | -14.2939 | -45.9076 | 2025-10-03 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 87f1c77f-5388-33f0-93dd-eb0aa4b45da3 | -11.4792 | -45.0174 | 2025-10-03 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7bda7f42-fb30-338b-91f4-2b1747d91199 | -12.8017 | -50.5088 | 2025-10-03 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ca7e567f-fc68-3708-bfe6-785399df33a1 | -9.9394 | -43.5777 | 2025-10-03 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 7df02272-0db3-3ce1-bb3d-147afe94aa9b | -11.5687 | -47.6526 | 2025-10-03 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4de8fed9-464a-3f18-a9c4-d5b50830e88c | -17.6331 | -44.4626 | 2025-10-03 14:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 6b8bd519-2775-3d85-9521-a73303c3776d | -9.9372 | -43.7187 | 2025-10-03 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 182.4 |
| 4d76cba8-3b1c-31ad-ac6b-2fa171dcb6bf | -7.7752 | -42.539 | 2025-10-03 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 365.3 |
| 60ccc8e4-49e9-35cf-9ebb-43e0dfbe697d | -11.1252 | -43.3874 | 2025-10-03 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 87.0 |
| af702144-579e-3e66-8105-f022f38ff5fa | -16.0413 | -50.9177 | 2025-10-03 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 141.7 |
| ee1faf61-97d6-38a7-afd2-646f20ec60ae | -14.0032 | -44.961 | 2025-10-03 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| a73124b0-090d-34be-a76a-dad99a583f3d | -12.122 | -43.4215 | 2025-10-03 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0e682aa1-2376-3d63-91e9-621540a7fc1a | -6.6978 | -42.8118 | 2025-10-03 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 86e32c09-53c7-30c1-9a39-c5c4e2a96d8a | -6.3587 | -44.7654 | 2025-10-03 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| c2ba6ff5-b12f-307c-8545-f43a09542c15 | -7.7746 | -42.5865 | 2025-10-03 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 199.8 |
| 3d1985f6-56a9-3849-bd5d-f9e18a002189 | -11.4988 | -44.9915 | 2025-10-03 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 89ab2287-a676-3403-91ef-9f37145d46eb | -13.3422 | -48.0965 | 2025-10-03 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 88d5c181-f03b-35e4-8e98-f5538c3511f1 | -6.2408 | -45.3424 | 2025-10-03 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 630d24f7-7ecc-39d6-8af0-32d0172c70e7 | -10.0528 | -50.2192 | 2025-10-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 8288bb41-f5b8-345c-bbb0-7f5f0603bfb6 | -5.4777 | -42.7721 | 2025-10-03 14:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| aee8111b-2e10-3dcc-a43c-174176745b18 | -11.9159 | -46.3044 | 2025-10-03 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 829ea7e4-59fb-39e2-835a-3509680f9063 | -6.2882 | -42.4229 | 2025-10-03 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 71d18579-7bb6-30de-b501-e4c2a5f5d7b8 | -12.8014 | -50.5304 | 2025-10-03 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 555f80d9-9ba6-3f20-8010-ddb89b67b885 | -9.9186 | -43.6978 | 2025-10-03 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 9fb39d8f-c831-3ea9-9a90-84e83ac673ae | -8.1699 | -44.1608 | 2025-10-03 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 158ddeb0-6c64-3f87-a705-9a57913d6574 | -8.9948 | -47.4845 | 2025-10-03 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| ca2279fc-e1c7-345a-9a27-3e9176f7367e | -11.1275 | -47.8634 | 2025-10-03 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 03cabee9-9bb3-313a-8fbe-31ac2242678f | -9.062 | -46.6565 | 2025-10-03 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c86b8b41-bf69-30c4-af20-74122a87c6e0 | -16.0217 | -50.9207 | 2025-10-03 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 4f84c94c-3629-35d6-a38e-61f72a7071a9 | -5.7688 | -41.7278 | 2025-10-03 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 94922b85-1370-347e-8143-085da6e3ddc1 | -13.6724 | -51.1911 | 2025-10-03 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| bb306db8-c4d3-3e45-92a7-fa628fee62b4 | -13.7858 | -51.3047 | 2025-10-03 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 2291af2c-62a7-300a-8d65-44c1b0dfcf9e | -12.1088 | -45.1554 | 2025-10-03 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 8e313ded-4f75-3d92-b3a4-1bc37c78541c | -8.1702 | -44.1377 | 2025-10-03 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 91922560-631d-3090-a7c9-34ea8d10df3e | -14.0037 | -44.9376 | 2025-10-03 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 5a6752a0-1b4d-3af6-bf20-c015f844ea53 | -16.0583 | -51.0454 | 2025-10-03 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 421a52e7-7178-3b41-97b9-872e200dbd31 | -9.9391 | -43.6012 | 2025-10-03 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b373d52f-48f6-33cb-98ef-76877351dbd4 | -11.1444 | -43.3845 | 2025-10-03 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 102.4 |
| ba55032f-06e0-359c-a39c-73a873d7447c | -13.3418 | -48.1188 | 2025-10-03 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 7c44626e-c73f-3b64-9314-a776a07e6a23 | -8.5959 | -44.7833 | 2025-10-03 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 77caf4b2-9dd0-3309-808f-d3ea4247dbb3 | -9.355 | -45.9284 | 2025-10-03 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 3fccb0df-98ce-34e3-8973-c98a51d3b6d7 | -7.3031 | -44.2013 | 2025-10-03 14:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 401efd32-ce80-3683-9c07-f031907f44fd | -10.019 | -48.4964 | 2025-10-03 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| a80479af-86f0-3e81-acbf-35ec9269591c | -11.1379 | -47.1959 | 2025-10-03 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| a7ace93a-31e1-32af-b2e2-e31afb41caad | -8.2128 | -46.8084 | 2025-10-03 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4350e76a-5d54-37af-a44d-cbc9c63cc5b5 | -14.2944 | -45.8845 | 2025-10-03 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| e8376999-8b08-3329-862b-42c4a2191606 | -12.7819 | -50.5543 | 2025-10-03 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |


[Clique aqui para ver as próximas entradas](README154.md)
