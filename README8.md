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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9f0fd05-bd0f-3333-8688-080b9e512e7b | -12.29983 | -45.53242 | 2025-10-24 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4688a264-5390-3079-992f-10e4b26a3efe | -4.27535 | -40.70064 | 2025-10-24 03:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c0e2e8b2-68c1-36b0-a89f-159edfb0471d | -9.2343 | -45.62173 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a793192-bc4c-3112-be7e-159613af348c | -9.23515 | -45.619 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a42cca9a-a3b4-3bf5-8ae6-3c6c3425cde8 | -10.56948 | -49.99589 | 2025-10-24 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86cf3a80-8134-3d23-a7b0-269e31a0ae45 | -14.77396 | -44.97527 | 2025-10-24 03:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f4be50d-3171-3617-9db8-52088099422c | -12.07167 | -46.43333 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 854c466e-4b3e-3c86-8d49-01c4b82e590f | -3.92787 | -47.70083 | 2025-10-24 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 262e9778-c747-3890-b16d-d6fc3954c979 | -9.26743 | -46.46736 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c15216d3-1936-330c-8662-b1c4aa84fc19 | -9.24486 | -45.59105 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a355cfe-db3c-3d15-b3e3-5537f44a413c | -14.48397 | -47.91916 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed2cacc1-e8cb-3263-8144-335074c84a0d | -10.8708 | -44.40977 | 2025-10-24 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf5ed324-87a4-36bb-845f-e27059eaa59a | -9.64269 | -46.88677 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4df2a7e-0a3c-34d2-9d24-fe5d347526ad | -12.05796 | -46.42366 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0afa11ac-ceee-3c5b-be59-a315e3bc5c8a | -12.29872 | -45.5284 | 2025-10-24 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 20e1728e-52dc-31e6-a816-16249892c281 | -10.03863 | -47.0836 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35a71d02-3a5b-3675-8fc7-a37b0169bec2 | -9.78206 | -43.86 | 2025-10-24 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e3c2a9a-b3b8-30c8-bedd-0dee765df2fd | -12.81645 | -50.96245 | 2025-10-24 03:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42bcfb37-baec-312b-a7f9-bd61038dab7c | -10.9087 | -48.04667 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 076baff6-58ce-38eb-bad1-49c75566b3d6 | -4.87678 | -47.54417 | 2025-10-24 03:49:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c3e1135-158b-356d-a9fa-73be8b6a4359 | -9.30352 | -45.19354 | 2025-10-24 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf33c9a4-5e2a-3b50-8529-01cdd4a76d49 | -13.09003 | -47.55334 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24cd301a-e2a7-31cb-a8a0-e2430e785b76 | -12.06338 | -46.42236 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbd8385d-42a0-3726-950a-262a6f1c15b8 | -3.44972 | -41.85381 | 2025-10-24 03:49:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5c736388-e610-3d32-a4ba-7d2e45388fe7 | -11.35853 | -45.95226 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 93004c4d-b7ed-3964-b8e3-4e3e9c056ede | -14.43922 | -50.94822 | 2025-10-24 03:49:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a5cd1988-a550-341f-8f56-fdc17db870bc | -12.03155 | -46.9287 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e643b63-df12-305a-94b8-e727b354d7ff | -8.87408 | -48.29824 | 2025-10-24 03:49:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 94ffe687-9eef-38e5-9ed8-02fa5b3c1b06 | -12.22627 | -43.31057 | 2025-10-24 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 529fdd6d-4231-3d8d-aa7c-f1caef868a4e | -4.63934 | -42.51549 | 2025-10-24 03:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8df67d41-e28b-32c1-8905-afa36af5618b | -10.56142 | -49.99821 | 2025-10-24 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f644ab61-bddc-3625-8d99-21eb23c06181 | -13.64082 | -46.83429 | 2025-10-24 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bbe40bd-941a-3284-9ccf-fa340831b462 | -10.02541 | -47.08454 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d31fa4e3-df49-316f-9d10-3b1908b916e2 | -11.36021 | -45.95414 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ca83f8b4-d985-3548-b43a-f906fa1051ac | -3.13807 | -49.52015 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a8846a6a-5184-3187-81b2-0646faef12f3 | -5.58778 | -41.31882 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 57189b74-4ad1-3686-a854-4576d4778c4e | -10.87444 | -44.41508 | 2025-10-24 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e73f06b6-2128-3c6e-9572-6e034cb1aee9 | -13.66576 | -47.95753 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96192386-0b7c-33b0-9c0e-a23ad9ec2810 | -12.02243 | -46.92019 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0249cde6-3490-343a-b78b-07bdd11380b4 | -13.35457 | -47.96613 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e4761410-8e31-31bd-82f1-714e9229b22f | -15.31745 | -47.85531 | 2025-10-24 03:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acf47101-6c6d-32a4-bcd4-78428144e5c4 | -4.63498 | -42.5148 | 2025-10-24 03:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2921e290-3352-3171-83d2-35a856b826f1 | -13.34131 | -47.96714 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b314466b-f60c-3792-9514-4881b3b3bf63 | -9.86823 | -47.46605 | 2025-10-24 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14c0e7fa-0fd0-39c5-9f1f-35320d899d2f | -4.28768 | -40.69835 | 2025-10-24 03:49:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 18.6 |
| e94ad323-e1ca-34a7-869a-d7d2c6b37f61 | -11.04833 | -45.4016 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| efb06b07-9462-3e58-8db1-a82d058a9c77 | -10.90206 | -48.05064 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55e93261-201d-39ee-8e2c-15faa440e1ee | -10.01196 | -47.09661 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a283ddb-f168-3834-972b-5fd7495bdddd | -3.78463 | -43.90286 | 2025-10-24 03:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2ea0b7dd-9deb-32ee-9e2f-9f73c87b32ce | -9.55564 | -46.69736 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 839638dc-f003-3d4f-ae44-5df99b8f7314 | -12.81016 | -48.65995 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 996e011e-d006-3072-9086-8561e874f56a | -13.61986 | -47.05347 | 2025-10-24 03:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69aeecf8-1821-3bab-b43e-9c47ae2a0bc1 | -14.34681 | -46.88163 | 2025-10-24 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99179a36-a738-3879-b58c-dc50220d2a18 | -12.05849 | -46.42088 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a655678-997a-37ee-a148-ebde3cc18ad4 | -10.4691 | -49.10608 | 2025-10-24 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24505031-d714-39c1-a9b8-9c93ac4538f3 | -13.35613 | -47.97755 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 989ae545-d827-3dcb-b46b-c4a8e5821941 | -15.83537 | -49.09495 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d407567d-b8ba-351c-a699-a05d7ec77381 | -13.90422 | -48.38879 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d59a7ed1-ef45-3f0c-9007-e0db383de8fa | -9.60816 | -46.91006 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f5f6c53c-f9c2-3bae-9e03-e7a18cd2f4cf | -14.46897 | -47.91195 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f9023ff-e0ef-3111-9e1a-b47e85f3c225 | -15.83757 | -49.08862 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a08f0270-9d44-3dc3-a998-0dfecd622695 | -10.59192 | -49.64222 | 2025-10-24 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe28df0f-63df-3c3b-87f3-99e0c2d4888f | -15.51532 | -50.01158 | 2025-10-24 03:49:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 921ef874-993b-3dee-b59d-5d5347adf6fc | -12.07677 | -46.40627 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 773eb3af-d0f3-3d6d-9211-49bf2e4369af | -12.07565 | -46.4122 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f6eeeba-f8c5-3ae3-9b61-021b2013b3e1 | -13.66325 | -47.95667 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54472388-1b39-32d1-a125-5d4367ccf6d9 | -14.26832 | -48.07844 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c662132c-d8b6-3e24-bdfc-ce738ea00110 | -10.87149 | -44.41536 | 2025-10-24 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae12ef41-3ae9-3c88-acde-0d08a36f6a6a | -11.82169 | -44.16861 | 2025-10-24 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c63e4e8a-742f-3462-a7e4-71bf10948590 | -17.04271 | -42.72546 | 2025-10-24 03:49:00 | NOAA-21 | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 28.2 |
| a0138f1e-1bbe-3399-8bf3-5636902b7aea | -10.88237 | -48.06127 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ac7a60e8-21f9-3666-ab28-037e77b4aea1 | -9.64077 | -46.88414 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 831b6cd3-202f-3fd2-86c0-3be4eaf717a7 | -10.01331 | -47.08934 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bbc2b80-7b22-316c-b1a3-d36a0e33a17b | -11.4535 | -43.71976 | 2025-10-24 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfa8da97-6933-375d-8261-0f5d88b863a8 | -2.41545 | -48.44294 | 2025-10-24 03:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9191004f-cd2c-342a-8d25-072e24923b2e | -11.06213 | -44.78429 | 2025-10-24 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3dfc997f-820f-3b8e-9228-775c9df4e761 | -12.06628 | -46.62887 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25256d3f-d4e5-38d2-8d34-55c8ec22978e | -13.90947 | -48.39018 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e197f426-1e5a-399a-849e-1547c9fe704b | -13.35746 | -47.97061 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f25c220-6f29-3bed-b108-a54ca29913eb | -4.95203 | -43.69685 | 2025-10-24 03:49:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4e5df6f-f605-341b-8a8f-f54dc4bcb281 | -4.17701 | -42.98188 | 2025-10-24 03:49:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 15dbd4b1-a359-3d9d-812f-3afbb0fe7212 | -13.24914 | -47.88263 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d894ac32-94d5-3121-937f-fcb85a7f9657 | -3.02609 | -49.47964 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dc211e5-5c92-3dcc-a743-c26ac9161f7c | -14.20631 | -44.5992 | 2025-10-24 03:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f21c01b-fff9-30e7-999d-0305f43573ad | -12.07552 | -46.4404 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 310dc1ed-389b-30af-acd5-09df1390e28e | -5.43043 | -41.07509 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7799179-558c-3ad7-ba60-2702e8342f58 | -14.7418 | -46.60784 | 2025-10-24 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f0f5654-2a0a-3b1a-a004-0ac083a46468 | -14.51756 | -48.35043 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc860565-1ae4-36fa-9acd-bc1d6943c62c | -11.04737 | -45.40685 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4882dada-c65d-3a19-af7a-1531a3af0d96 | -14.48329 | -47.92257 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ea82c81-265e-3e71-b955-3fb8f381c8d5 | -13.28756 | -47.48507 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e646664c-c98c-38ca-863e-49521bf0d0e4 | -4.95119 | -43.70181 | 2025-10-24 03:49:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 960f2d37-d956-3edf-8cbf-2e9ce29756d5 | -3.12718 | -49.10089 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c13682d-2f98-3a66-8ebc-794836416e5a | -12.15763 | -47.01151 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98a456bf-be45-3845-bb57-ed7bd6c2b8d3 | -10.89992 | -44.73937 | 2025-10-24 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be069dec-87cf-34c6-b9ec-a14eb47cb4b0 | -10.0406 | -47.07336 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4e68dac-1e95-3c96-838f-db29227af094 | -12.30079 | -45.52735 | 2025-10-24 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3bcd8f08-89a0-3e44-87a6-3193a03547f7 | -12.92275 | -48.50715 | 2025-10-24 03:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 508df041-213a-3adb-917c-3839ffcd9b00 | -12.31451 | -47.26797 | 2025-10-24 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c5451aa-6e51-3ac6-a782-514393d7ae45 | -13.67183 | -47.95508 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README9.md)
