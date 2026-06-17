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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3edd8ef9-f28d-3716-b141-ba561ea35b19 | -13.27449 | -46.06036 | 2026-06-17 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 96127938-1f11-3cd1-bf0e-f10a8bd6410c | -11.58708 | -55.34376 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55e2cc26-d1c2-3db6-84b8-6607661d7b5e | -9.19057 | -58.05142 | 2026-06-17 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68ef30b4-cf2a-3fd4-8651-17ca657cef4b | -10.40436 | -49.44704 | 2026-06-17 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f05262a-9b6a-3a4f-8102-f47ae6f5b895 | -12.26495 | -43.50332 | 2026-06-17 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d29c502-a30e-330a-a90c-0aa988196220 | -12.21665 | -52.79213 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 310.0 |
| 9e67e18c-e2cf-3c92-b862-76258bddd772 | -12.21733 | -52.78738 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 310.0 |
| 503f65e0-9f7b-3063-82b6-c38d5d7bbfd5 | -10.54708 | -53.7229 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef9dae2c-792b-3783-9c19-ecb6198d733e | -12.80833 | -54.86258 | 2026-06-17 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8c634cb0-f357-3232-91e8-761650e5aee7 | -12.20827 | -52.79263 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| f20b4571-76bc-3eb3-bd45-bbdb9b332a41 | -12.54678 | -54.59419 | 2026-06-17 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bddd6b5-7e99-36df-9a72-d27efdb34b86 | -11.74 | -54.79168 | 2026-06-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4c99693-e551-3807-bda1-176c516b75fd | -13.27499 | -46.05576 | 2026-06-17 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1405a2de-7195-33cf-bc4e-370d21b88810 | -11.48288 | -57.10346 | 2026-06-17 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d8b2f6a-1426-39a8-8dad-65bdbf780e18 | -12.21784 | -52.77947 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3934a1db-5a32-3c34-98c5-1a0579cf4773 | -12.50648 | -46.3509 | 2026-06-17 05:06:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 166679dd-a1be-372f-9f02-70b86ba1c41d | -11.54201 | -52.7754 | 2026-06-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c66c7022-3060-3dee-9cb4-59b1b01ae2d6 | -10.55871 | -46.2267 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 153671ea-cde2-3bca-a941-ecc0d1e99838 | -12.19071 | -52.78341 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 3e052dd8-cca9-3494-b7c1-71e0649cd793 | -12.55011 | -57.19788 | 2026-06-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1068aec9-2b0a-3901-8773-9def3651d451 | -12.22283 | -52.79965 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| cc9720f3-208e-33db-ae8d-d3df74255fdd | -12.18378 | -52.7775 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d18cd71d-a94a-3b0c-bfcf-38c59f20f7a5 | -13.27826 | -46.06208 | 2026-06-17 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 259fc695-c0a6-302e-9030-6ff2437d2e12 | -12.21903 | -52.79908 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| badf3367-07ef-32cf-b913-17e3ff063c70 | -11.91539 | -55.91134 | 2026-06-17 05:06:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ffa6311-ccca-3e39-8771-cf5b0b08b6ab | -10.12069 | -52.16739 | 2026-06-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a3afa20-50e1-357a-ae21-bf1395690b65 | -12.20447 | -52.79206 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 6ff30929-06c5-3fec-86de-d0eac50c098c | -14.0953 | -59.45253 | 2026-06-17 05:06:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc12f7b0-9fbe-3696-bc0b-89593bbe78e2 | -12.05896 | -58.04264 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ade246f-af94-32a6-bf57-78b9e361d739 | -12.22099 | -52.78482 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 13d444d6-a8f2-3b5a-a598-5c32cf4ee831 | -12.18066 | -52.77214 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b9bd3d4e-f10f-3697-bd21-85fe7814cf8b | -13.27879 | -46.05749 | 2026-06-17 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9c2524b3-2e97-3f54-96f5-1c9c057ecdbb | -11.2641 | -53.96359 | 2026-06-17 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9a0354d-b931-33da-9278-915990f0ffe9 | -12.18623 | -52.78761 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8cdbeec7-f98c-3377-966f-5071c46f64bb | -13.57176 | -48.20575 | 2026-06-17 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e337373-4535-3c49-8e75-cbf5324618fe | -9.37609 | -50.53943 | 2026-06-17 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cb3b46e-30df-3031-b4cb-a5c5c6db858d | -12.42841 | -58.41474 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba3487bd-520d-36fd-b3fe-f624f531560b | -12.21596 | -52.79688 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| dd8ab0db-64b6-3e64-abde-8d05512278b8 | -12.76552 | -59.00547 | 2026-06-17 05:06:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27f7eb1b-e0d2-33b7-9723-27fe89ad7dde | -14.09683 | -59.46462 | 2026-06-17 05:06:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73885d67-fae1-375f-8bb5-21669ae158e7 | -12.58743 | -54.1652 | 2026-06-17 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c30d1b48-ed53-37a5-84a5-eb58bb22b727 | -10.40511 | -49.44601 | 2026-06-17 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b766a75b-3e5f-34bb-a522-dd3e7d386e43 | -12.06229 | -58.04319 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1205afbb-7fc4-3a77-8c1d-f0894a61f450 | -9.18659 | -58.05456 | 2026-06-17 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b8d1534-cb13-3450-8b56-9e033b3f5cbc | -10.12523 | -52.17958 | 2026-06-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b6d6be25-90ae-380a-b0b6-c1f67b66d0c4 | -12.43017 | -58.40381 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea78f61e-1233-3ba7-92a6-7eeb10d3d750 | -12.21801 | -52.78262 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| baeb6b16-4f7e-3317-87fc-57870e5e11fe | -12.19656 | -52.76963 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eafab70b-f9de-3cdb-937b-352a362d749c | -10.87937 | -54.09645 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72c77b3c-e6e4-3e2a-ba0c-94b7df48cc38 | -11.19655 | -49.68325 | 2026-06-17 05:06:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 621b99ee-e7cd-30cb-aac1-6ed9149ee462 | -11.72185 | -54.49081 | 2026-06-17 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e92802e0-8a0d-3c79-a9d2-169149d4df96 | -12.18759 | -52.77806 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6af2c295-b0dd-3995-a698-2332d99e83dd | -12.91944 | -54.21946 | 2026-06-17 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7bb64e02-201f-3c07-a218-141f430f1af5 | -12.08078 | -54.61772 | 2026-06-17 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 26cbeea7-edb0-3bc8-a24b-b834e68e85f6 | -10.15201 | -56.60536 | 2026-06-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6569e591-5910-3d1e-9b36-67160a899f34 | -11.358 | -55.821 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01aa40ac-dcae-36cd-af2e-f70962fc3172 | -12.2324 | -52.78651 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9fa4fe76-eb61-34c2-8f29-ddff97099588 | -12.21041 | -52.78149 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a40c4087-00ea-33ea-83ea-adb6786e3a73 | -11.06606 | -45.18339 | 2026-06-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aae6765-037e-3dc6-a60b-06455ef410d6 | -10.56396 | -46.23151 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3457cadc-af22-3ac0-bb0f-9edb3e506678 | -14.10088 | -59.46138 | 2026-06-17 05:06:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d67c88a4-c9d9-3a73-b630-a34e4698bc4c | -12.43075 | -58.40017 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22a917cc-498a-3a19-89ae-eb8f4aa6d01c | -12.20972 | -52.78625 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 014ddd1b-af3f-36cf-9bfa-8f1a82ea78bb | -12.85364 | -44.36692 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5274a620-8af2-333f-9d7f-32bf480e2ffa | -10.56972 | -46.23218 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd423246-c980-3e37-8db2-41a30f0704e6 | -12.83976 | -44.37095 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 1f2b355d-6f9c-32d5-b809-9238dc6c0bda | -12.08135 | -54.61385 | 2026-06-17 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 74da97f3-2bd7-397e-866b-42cbd259cd5f | -10.49872 | -53.58152 | 2026-06-17 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26018535-b790-347f-a779-05395b9c5313 | -13.94522 | -53.56734 | 2026-06-17 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f772bc5c-1033-3705-9d6e-963df67578c1 | -12.18243 | -52.78704 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 623177e0-edcf-3023-ade0-d2270aa85a98 | -10.64209 | -51.79981 | 2026-06-17 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aae040cc-da8d-3e92-b127-f9eb99140e0e | -12.17863 | -52.78647 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff3f6777-471e-35de-8cf6-f76af5f7ac59 | -12.21653 | -52.78901 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 314.2 |
| 6da84960-d72b-3008-8714-3b27dc1f40ba | -12.21968 | -52.79433 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c8ffe05e-ef1e-3a2e-8a40-f79464073506 | -12.43469 | -58.39709 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3681840-f2ff-3b9b-90d0-bf383b777ff5 | -11.58426 | -55.33958 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25fafae2-8639-3bb2-9d2c-89012b44b8f3 | -10.38112 | -56.79227 | 2026-06-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bff5381-bace-3c5f-bd17-46d6d35f2c06 | -11.59099 | -55.34063 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59bf1dc2-e61c-39b9-ba80-dbe2639247e3 | -12.47192 | -55.12537 | 2026-06-17 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32f7cc1e-e902-3613-8402-d042534f98c8 | -13.94346 | -53.56509 | 2026-06-17 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8d0445fe-7411-3934-ad0f-f0e60579cff4 | -12.08191 | -54.60997 | 2026-06-17 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9b570bb5-d6ae-39f3-8f36-37053e7223b6 | -12.17998 | -52.77693 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 737b7164-d899-3084-bb80-3248a9c03e30 | -12.15163 | -63.04546 | 2026-06-17 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fbe8083-be2d-3c33-b33b-a251cbbb96cf | -12.67568 | -54.57645 | 2026-06-17 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efa1e856-ff3d-3e10-8aa1-69af4ddfaf42 | -12.58388 | -54.16467 | 2026-06-17 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 162f7b4d-1e2c-39be-ae0e-ddf8c3dc07d4 | -12.84894 | -44.37006 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 12c8fb02-7bc0-3f43-90d1-99a7fd2e4914 | -12.15237 | -63.04133 | 2026-06-17 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3129b440-b038-3a7f-a031-ab952716d9f5 | -12.21718 | -52.78424 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 314.2 |
| ced5453f-1d4d-3f74-9c0f-75475a96a1da | -11.35467 | -55.82047 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 473b2fe4-ace4-3ad8-a8e5-2ee7cbca1b2e | -11.59436 | -55.34116 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1fe107e2-de56-3a00-b692-89d3fb2bec17 | -10.77233 | -54.10979 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b306f0bf-8485-3479-a8fe-87dc16453864 | -11.59491 | -55.33751 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05ed068b-5a18-36bc-a07b-7cb0904ab124 | -10.59369 | -53.52237 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9c9b7df-bd3f-3f12-8032-d9cc801516d3 | -12.15273 | -48.45391 | 2026-06-17 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e90d891-f331-322e-b4d6-c97ce8dd332a | -12.20836 | -52.79575 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c746024d-9512-3f25-953b-311d71f583ca | -11.51511 | -56.12815 | 2026-06-17 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83ba9fb8-1500-327f-a6bd-65879aac6839 | -10.77699 | -54.10243 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fe8a1e7-7cf7-373b-92e6-d7d98bd7d51b | -12.83915 | -44.37674 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 98f45b2e-25e6-31bb-a464-00333e457f48 | -12.20512 | -52.7873 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23a0608e-4ff4-309b-91fa-089b8b5ca917 | -12.54576 | -57.2043 | 2026-06-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README13.md)
