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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8d91112-0171-3f00-8b34-617f0a646eb3 | -11.06839 | -48.29139 | 2026-09-18 06:46:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3e660da9-ad39-36cf-95d8-dbc71229cfd1 | -7.05786 | -47.47873 | 2026-09-18 06:46:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7a92937b-1304-3bcc-b0e0-a5e902afa102 | -5.75117 | -45.08785 | 2026-09-18 06:46:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 6b9a5b65-9a45-349b-bc9b-6a6aadf77fd8 | -12.16671 | -46.98949 | 2026-09-18 06:46:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e5163a22-6f96-39e0-9ca2-93a52f728b1f | -10.6645 | -50.23552 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| cf5ba7be-fa3d-3501-bfba-41e0dbd62b50 | -11.31338 | -46.76041 | 2026-09-18 06:46:00 | AQUA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 0acd2c87-73f8-39d2-93e8-d0def2d45b31 | -10.68746 | -50.2696 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| a1415574-ef8b-3f67-9a36-0f0f8f089303 | -12.29856 | -50.73369 | 2026-09-18 06:46:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 335e7c04-a866-35d5-85de-6298dea6e780 | -9.7782 | -45.03697 | 2026-09-18 06:46:00 | AQUA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 29e092bc-6875-34a0-a4b6-7f06706fcc00 | -7.80003 | -44.89538 | 2026-09-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 134a47e8-fa0b-3698-8b78-b5f05f5ddf30 | -8.44046 | -45.70267 | 2026-09-18 06:46:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2b16cf68-24b6-3202-ba8b-1c53b798aec4 | -10.82997 | -50.18798 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8b319b52-35f1-3980-ba56-8d0793ba36a2 | -11.06705 | -48.30026 | 2026-09-18 06:46:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 48845ff1-0ba4-3968-a26b-c8870becaa87 | -9.15733 | -49.99294 | 2026-09-18 06:46:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f36224ff-9c80-3c33-ae99-a075e3595dfd | -10.66653 | -50.46126 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 5e78080e-1c9e-355e-a220-af904a4d3ac6 | -7.79045 | -44.89397 | 2026-09-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cb9eec82-df49-3746-879b-dec63d2a17fc | -10.12177 | -45.5614 | 2026-09-18 06:46:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 85664520-ab73-3fb4-9473-09e74f5722fe | -11.312 | -46.76989 | 2026-09-18 06:46:00 | AQUA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c3422906-4bc6-3958-9a78-b150bc198ec6 | -12.17562 | -46.98746 | 2026-09-18 06:46:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 3cbe3733-a97c-37da-b1b5-c4f15e4c6285 | -13.24912 | -46.90736 | 2026-09-18 06:46:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 12b92b72-fe03-3e1f-a654-e385371f1552 | -10.10994 | -45.6438 | 2026-09-18 06:46:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2471e3c4-e30f-3402-8ca2-fe89d13dd5db | -9.93565 | -46.58943 | 2026-09-18 06:46:00 | AQUA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 355721e3-aa22-39c0-b8e4-04fe016e2897 | -19.18504 | -48.7963 | 2026-09-18 06:48:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cbed3f20-24ec-3c1e-be3f-342b200fd837 | -13.38946 | -48.02424 | 2026-09-18 06:48:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 12604be5-3478-30d5-8f1f-2e972f3d8c1a | -14.79926 | -48.54399 | 2026-09-18 06:48:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d606ce9-6429-307e-b571-e0d889cfb923 | -14.93399 | -49.91465 | 2026-09-18 06:48:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc0aba31-e37d-3cd6-b10d-8d8279a79118 | -14.80868 | -48.56053 | 2026-09-18 06:48:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 263543d6-085e-3eb8-aad4-92d373e0a6a6 | -13.38063 | -48.02284 | 2026-09-18 06:48:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| efa29546-5723-3259-a20e-89f088b3c8c4 | -19.18785 | -48.77694 | 2026-09-18 06:48:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e6eee8b9-3a1a-3842-b551-b6b503ce7270 | -14.8959 | -48.15247 | 2026-09-18 06:48:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 496e0e93-75f2-309c-9c48-b3cf0c9bf5b8 | -13.68299 | -48.59277 | 2026-09-18 06:48:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ef4364dc-6d98-3bd5-bde1-dea6e2f2550a | -13.61576 | -48.30876 | 2026-09-18 06:48:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f3066012-3899-339e-8eeb-d4a006edae1d | -18.02996 | -50.94757 | 2026-09-18 06:48:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0e0c44af-5342-3373-bb02-207a6927acbb | -13.61712 | -48.29971 | 2026-09-18 06:48:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a49ff1e6-b31f-3a99-889d-ae64e4b05f48 | -14.94283 | -49.916 | 2026-09-18 06:48:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6eda8621-e517-3099-868d-38a9db826fd2 | -19.17747 | -48.78519 | 2026-09-18 06:48:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| db40fdca-5701-3fcf-98ef-496b4ca96cc4 | -14.17403 | -47.85091 | 2026-09-18 06:48:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ff72a26a-203c-3b58-b6b6-3a986a4666ce | -14.233 | -48.62284 | 2026-09-18 06:48:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8b8b4ba1-dfc1-3605-aa55-4ccbeefd0d14 | -18.02107 | -50.94607 | 2026-09-18 06:48:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| f1ab9203-0f7c-30fb-b769-560e55e7dd0f | -13.76701 | -48.03136 | 2026-09-18 06:48:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c03c93b-f492-3b7b-a63c-cc9a8f23fb42 | -13.60086 | -48.28794 | 2026-09-18 06:48:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0870a5d2-55bf-3405-8267-0fbd2429c78e | -14.22282 | -48.51064 | 2026-09-18 06:48:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3c09665e-9741-3390-8852-7d694e944aab | -19.54963 | -47.63031 | 2026-09-18 06:48:00 | AQUA_M-M | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fe371ede-1288-3efc-b029-7da1950e5217 | -15.63742 | -52.7208 | 2026-09-18 06:48:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7dff751d-6cbc-36f1-9eac-fd317230e758 | -13.74459 | -48.80086 | 2026-09-18 06:48:00 | AQUA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0185db8c-0ab8-3ac5-88cb-33571aafb437 | -18.02255 | -50.93664 | 2026-09-18 06:48:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 34.5 |
| c4fc559e-73ca-37bb-bf7f-4642f36d1a61 | -19.18644 | -48.78663 | 2026-09-18 06:48:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| e5b5e971-743f-3176-a1ff-dcab334e1ac5 | -13.74592 | -48.79192 | 2026-09-18 06:48:00 | AQUA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9122c184-f5f4-3c1d-a757-8fbbbc789e87 | -19.55913 | -47.63155 | 2026-09-18 06:48:00 | AQUA_M-M | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 34c379de-33e5-3a45-b406-bb84619ab3c8 | -19.17886 | -48.77554 | 2026-09-18 06:48:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 36360712-dd80-39dc-994e-f58727037868 | -18.0303 | -50.9385 | 2026-09-18 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 0de3c5c3-fce3-36c1-831a-7a166381a865 | -10.6729 | -50.4545 | 2026-09-18 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 59011e8d-28a9-3c59-b054-cee80a9409c4 | -10.6539 | -50.4564 | 2026-09-18 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| b92db962-069e-35c9-941e-7a5d42078c91 | -8.9107 | -62.41 | 2026-09-18 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 2215bc12-ead7-33a8-8e51-21ec45d6bf92 | -10.6944 | -50.26 | 2026-09-18 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| c238adfc-e5d4-3baa-8bdd-629cdd6b00e5 | -9.7177 | -54.8162 | 2026-09-18 06:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 17707205-d0fb-3b2f-9e4e-5d48bbf0bb0c | -9.699 | -54.8176 | 2026-09-18 06:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3bfa644d-5125-388f-a96b-d456630575ec | -8.9108 | -62.391 | 2026-09-18 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| fba218ec-29d7-3599-a496-01330d883f29 | -8.8922 | -62.4107 | 2026-09-18 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 7e50a2b7-f807-320f-897c-f52320abcdc8 | -8.8923 | -62.3917 | 2026-09-18 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f4844e92-733f-3dd0-a3a7-64e05e83aac3 | -20.61982 | -47.2538 | 2026-09-18 06:50:00 | AQUA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fa5187e0-c828-36a0-ab4f-2b0779e23bff | -18.0303 | -50.9385 | 2026-09-18 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 8aa8a10b-9066-3828-b802-484d27f57ca3 | -10.6755 | -50.262 | 2026-09-18 07:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c8748f28-2604-37e6-919b-f7fecfcb1df2 | -9.7177 | -54.8162 | 2026-09-18 07:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3724c1b5-41f6-3338-ab40-d7bd4902ee55 | -10.6539 | -50.4564 | 2026-09-18 07:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| eb173743-6a66-38cb-8043-d2216652fba6 | -8.8922 | -62.4107 | 2026-09-18 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| cce50780-8cc6-3b8c-b453-0cdb82687229 | -8.9107 | -62.41 | 2026-09-18 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 7b03ef9c-46d1-3158-814c-e3a49390d283 | -10.6758 | -50.2406 | 2026-09-18 07:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| a4ff917e-a92f-3fbf-8636-48d41b0e1c6c | -9.699 | -54.8176 | 2026-09-18 07:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| cd1abd4b-fe36-39ff-9da7-3e883bd1a8e4 | -10.6565 | -50.264 | 2026-09-18 07:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 57a271b0-581d-3c86-a66d-00fc2f9b2ee8 | -18.0502 | -50.935 | 2026-09-18 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 09cb3a42-2f35-3bc5-9192-adfce1afbd59 | -9.699 | -54.8176 | 2026-09-18 07:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 0eaa928c-4c03-3c15-8502-4cfa322667a8 | -18.0104 | -50.942 | 2026-09-18 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f807d5ea-d5da-32d8-864d-c8a3f656f031 | -8.9107 | -62.41 | 2026-09-18 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1e0e8b1e-4294-3c91-a90f-8b6e44411010 | -10.6568 | -50.2426 | 2026-09-18 07:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 230817b5-f5f0-37a5-b394-6b3b3073f0a4 | -18.0303 | -50.9385 | 2026-09-18 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 9ab2fe26-6904-3eb8-beca-e6cf3182ca2a | -10.6758 | -50.2406 | 2026-09-18 07:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| c853d60c-dd4b-3f52-a91f-9e7f43a58d88 | -8.8922 | -62.4107 | 2026-09-18 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e554e42b-5330-32b3-9659-3abda1a5abd4 | -18.0298 | -50.9606 | 2026-09-18 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 51397e29-5582-3bf1-a870-ff9d9e80ff4e | -9.7177 | -54.8162 | 2026-09-18 07:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 2894a8e2-d208-3426-b723-2dba86192378 | -10.6755 | -50.262 | 2026-09-18 07:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e6364c35-2df5-3c23-be30-953def9f052f | -10.6568 | -50.2426 | 2026-09-18 07:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 28a15c1b-88f3-3783-8593-fce0129adce7 | -10.6944 | -50.26 | 2026-09-18 07:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |
| de637f12-2673-384d-832c-6d2baacb1b03 | -9.699 | -54.8176 | 2026-09-18 07:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a313a57d-4ebd-3c2b-a4da-c8aa345bbb71 | -10.6758 | -50.2406 | 2026-09-18 07:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| cd7921c7-5dc7-395a-b20e-afc421c57dba | -9.7177 | -54.8162 | 2026-09-18 07:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| acc77845-4e0c-38ab-916c-6e8ac39f726f | -10.6571 | -50.2212 | 2026-09-18 07:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 1f7ab09d-f793-30b6-a8c1-ecb4dbb74748 | -10.6755 | -50.262 | 2026-09-18 07:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 1686c01c-1868-328c-8c23-03e620c36f8f | -18.0303 | -50.9385 | 2026-09-18 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 923d6430-e85f-376a-a996-925ba76321a4 | -10.6565 | -50.264 | 2026-09-18 07:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 2446d102-65be-3abc-8f4c-3e8a8808c673 | -18.0298 | -50.9606 | 2026-09-18 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| e553676a-9b6b-336e-8042-a9fccdaf2261 | -9.7177 | -54.8162 | 2026-09-18 07:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 77b941bd-a6af-34f9-bc34-88d47196432b | -18.0303 | -50.9385 | 2026-09-18 07:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 130.3 |
| d10cb615-e985-3411-84b5-96914740ce4d | -8.8922 | -62.4107 | 2026-09-18 07:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3b9fc630-e599-3bd9-a0e9-93f0422ab6d2 | -18.0303 | -50.9385 | 2026-09-18 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c343c72c-d513-3481-9f0a-cdfe40c1cbd6 | -9.7177 | -54.8162 | 2026-09-18 07:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| bb67d512-0338-3b67-be6d-f9eb9cc480e4 | -11.3161 | -46.7699 | 2026-09-18 07:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ecab7844-ce3d-33c0-bce9-f1fc10f85548 | -9.699 | -54.8176 | 2026-09-18 07:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1b5cdc29-81aa-3ef3-94e8-ab6762a6c54d | -10.6758 | -50.2406 | 2026-09-18 07:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| c2878946-0c05-3bac-ace8-9cc07c0f18cc | -10.6755 | -50.262 | 2026-09-18 07:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |


[Clique aqui para ver as próximas entradas](README90.md)
