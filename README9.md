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
| 8c37dae1-7dab-356c-b2dc-c6500b776fb0 | -12.14445 | -48.45671 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f094e5b-ef52-3e1e-8218-5f747e95beb6 | -20.25776 | -41.85115 | 2026-06-11 04:34:00 | NOAA-20 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e45c9cc9-4af3-3cfe-883c-3ae180f5e00d | -18.52083 | -53.53996 | 2026-06-11 04:34:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da76ed76-487d-3594-bb63-7c834bda116e | -6.4357 | -44.5535 | 2026-06-11 04:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 2268d87a-184e-3d90-a3ea-8339541791b6 | -9.3234 | -45.4787 | 2026-06-11 04:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 90694324-2ebe-3f35-9db5-1bc70076993c | -12.8548 | -44.3625 | 2026-06-11 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| b4aeabe6-37d0-315b-a584-64019ece2cd7 | -9.3234 | -45.4787 | 2026-06-11 04:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a7252c43-e882-3d3a-9077-e6760b43f535 | -6.5672 | -47.91324 | 2026-06-11 05:16:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ccad94ae-b27a-39af-866a-9c5a163eb2f7 | -6.57267 | -47.91811 | 2026-06-11 05:16:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fbfc096-c9f9-366e-a982-1696efc9b563 | -11.80389 | -57.35128 | 2026-06-11 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c72d090-8176-3013-a0d7-cdda4d465cf6 | -9.6249 | -49.02291 | 2026-06-11 05:18:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81119764-a55b-3c0a-b0cf-16a1c14ea600 | -12.30787 | -47.91185 | 2026-06-11 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c02bbf08-d16a-385c-bc1c-31f3e3374ef5 | -10.90279 | -49.35468 | 2026-06-11 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cab72da-2cae-3c37-990f-34b777121c36 | -11.11139 | -49.09576 | 2026-06-11 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 132127b7-0f93-3f5e-ac12-fe0f89f36d4e | -11.80799 | -57.34776 | 2026-06-11 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f04ec9d0-bddb-39ae-809d-7ed38631b012 | -10.88084 | -49.54373 | 2026-06-11 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df6844f8-f7db-3291-845a-e5dc29f91e20 | -7.34946 | -49.84599 | 2026-06-11 05:18:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31acc49c-2a07-3edc-9c04-03fc983967f4 | -7.59834 | -46.46159 | 2026-06-11 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5524829b-cf96-381a-9ed1-c405db43b655 | -9.31777 | -48.97112 | 2026-06-11 05:18:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e83c9750-257d-3a39-bcac-6f6a0434b559 | -11.80741 | -57.35182 | 2026-06-11 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 517d3d74-93dd-3e76-94b2-d27fb978ed82 | -8.98387 | -48.09369 | 2026-06-11 05:18:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47a1d5f1-cea4-385e-84d3-c9f7f4658b86 | -11.8763 | -47.10579 | 2026-06-11 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a48a4c6-f0c8-38ab-b933-88a181107391 | -12.14735 | -48.45343 | 2026-06-11 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c55ad4f8-123c-34e5-ab18-df6f3c233f7e | -9.21499 | -48.57855 | 2026-06-11 05:18:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2b9a3ef-d3c9-305c-a5b8-b140f07df797 | -9.21443 | -48.58286 | 2026-06-11 05:18:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0520664f-a5cc-3ffd-9e19-f2a9e95cdd80 | -11.80218 | -48.79725 | 2026-06-11 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3ba86da-8b48-3cb3-b9a8-927eebec5884 | -7.34901 | -49.8494 | 2026-06-11 05:18:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ccc259c-e7db-366b-a79e-b040679dd89f | -9.11111 | -50.91781 | 2026-06-11 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43f46f35-fcbc-3b90-a06e-b247c4b63e54 | -9.21823 | -48.57984 | 2026-06-11 05:18:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a48878cc-f375-3773-a7bf-e780459a7cc6 | -12.37563 | -47.8924 | 2026-06-11 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f906071-1d3b-3ed7-af28-5d590e53e1df | -12.3696 | -47.89143 | 2026-06-11 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ea45aaa9-549f-3a77-8736-b255d4e5cb62 | -9.21175 | -48.58322 | 2026-06-11 05:18:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3ac8763-7eab-335e-8067-3008fb288109 | -11.11087 | -49.10014 | 2026-06-11 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0db7864f-a04e-3e20-bad1-3593f0fd128f | -10.37878 | -46.62155 | 2026-06-11 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ff8b779-bb4c-3f19-a0e0-da17f0e840a2 | -9.40777 | -49.39691 | 2026-06-11 05:18:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a928f31c-3aef-334b-a173-e7b455aa8aa3 | -9.22095 | -48.57941 | 2026-06-11 05:18:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ad1ecf8-244a-35e2-87f3-b64ddab18573 | -12.02916 | -47.80354 | 2026-06-11 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75250b0a-1e69-35b5-b380-8aba1622f60a | -12.14679 | -48.45838 | 2026-06-11 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c161432-1ed3-3a02-b4cc-78dc4d3ff9a5 | -7.63017 | -50.03646 | 2026-06-11 05:18:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09ec77f1-b5cf-3361-9697-a705f6342d7b | -10.2879 | -47.61223 | 2026-06-11 05:18:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6133e65-da56-3938-8aa4-951031e80c74 | -10.37804 | -46.6279 | 2026-06-11 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ca9af6b-6a9f-3ddd-b09c-5d4849c926bf | -10.89699 | -49.3539 | 2026-06-11 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ef2243a-3cc8-339b-af33-1ce578f745e7 | -12.37608 | -47.89215 | 2026-06-11 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3f0b8ae-ce6a-3adf-9d32-75720211813e | -10.28656 | -47.61221 | 2026-06-11 05:18:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 535cc7d0-c38a-3a28-a5b6-88f65ad2a017 | -10.2859 | -47.61757 | 2026-06-11 05:18:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99c4d11a-3e9a-319a-911d-d70ee6f872e6 | -9.21228 | -48.57892 | 2026-06-11 05:18:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6397c822-37ef-3d56-b9c9-675cf5653393 | -12.02988 | -47.80231 | 2026-06-11 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c84909a-a679-31d9-9497-ca0a4b13f011 | -10.84453 | -46.79086 | 2026-06-11 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11907f72-51f2-3205-a5e6-0c0f9fa0c98b | -9.10815 | -50.9147 | 2026-06-11 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d37db5f-3b12-3797-ac31-5e0c46332a0e | -9.11149 | -50.91484 | 2026-06-11 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a7b771a-4c80-3f06-a576-cd0c780ed35e | -11.81151 | -57.34829 | 2026-06-11 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 036c591f-d611-398e-b019-8cc753076b3e | -9.10774 | -50.91769 | 2026-06-11 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0f60eab-f18f-31e6-9664-24bfa0330974 | -10.37959 | -46.62663 | 2026-06-11 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c9ea36a2-91f1-341c-9efc-fc25291dc47c | -12.03558 | -47.80497 | 2026-06-11 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2b4e4b2-19e4-38c0-9b42-e380d3906a8a | -7.62925 | -50.04305 | 2026-06-11 05:18:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6db1b225-336b-37b2-8bd6-7fd1bb609497 | -12.36915 | -47.8917 | 2026-06-11 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 09d9ec93-aab9-3d70-aaf7-ccf18a3c6311 | -9.21169 | -47.9169 | 2026-06-11 05:18:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fed410aa-52c5-3313-978b-0586d776b733 | -7.60351 | -46.47426 | 2026-06-11 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fbdb562e-7367-3f85-90e6-0db6888af701 | -10.3848 | -46.62925 | 2026-06-11 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0a4279eb-c056-3bbb-a73f-45dc783225e8 | -10.7259 | -59.27399 | 2026-06-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96e8cb4a-ff5c-3d8c-a895-fc3dd7c9b18c | -8.99059 | -48.0898 | 2026-06-11 05:18:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d958bf4d-16c8-3cee-962f-5344a0dcd19e | -9.21228 | -47.91204 | 2026-06-11 05:18:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e41fb7d-f6a0-3774-844c-bbf091681f65 | -11.87699 | -47.09959 | 2026-06-11 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0eaee177-fbf5-3eb3-87c9-b297b607abfb | -10.28727 | -47.61763 | 2026-06-11 05:18:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5a81765-cb39-364d-8444-d56785a7a202 | -12.14791 | -48.44849 | 2026-06-11 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 379813eb-542c-39fd-9f3a-f6c161a18f09 | -12.30845 | -47.90664 | 2026-06-11 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 731e316f-5313-3656-95b3-a83b4b51bafd | -9.31245 | -48.96629 | 2026-06-11 05:18:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0221042f-7a4f-323a-8852-3739ae7d6873 | -9.41346 | -49.39755 | 2026-06-11 05:18:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea35b632-02b6-321a-b884-67a0bbec85c5 | -12.8548 | -44.3625 | 2026-06-11 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| f39a420e-948e-31d7-990a-5b8aea8ad509 | -16.1082 | -56.7592 | 2026-06-11 05:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26fb7637-1421-38dc-8add-87ad9aa81f37 | -15.38222 | -56.95762 | 2026-06-11 05:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1cceee0-00d5-3311-ad90-fd7656eee21a | -16.10502 | -56.75381 | 2026-06-11 05:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66a41d13-d63b-3d0d-8d64-d5db7b3ab3f7 | -17.76458 | -54.66158 | 2026-06-11 05:21:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa8e5d9e-81ba-3ea3-b249-cdff5bc48ac1 | -16.10557 | -56.75637 | 2026-06-11 05:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b31a37c3-b252-329d-af46-ae39220fa7e8 | -15.38906 | -56.96338 | 2026-06-11 05:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0894e477-4d9f-30f8-bbd7-9812cae5c1c2 | -12.55007 | -57.19378 | 2026-06-11 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4f2c644-c994-3e67-b6f5-9e0a80dc1bb9 | -10.31422 | -59.57061 | 2026-06-11 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fca8364-6611-3c87-bb5b-47cbbed6e669 | -5.27853 | -43.96068 | 2026-06-11 06:14:00 | AQUA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91c49443-6063-3e37-84ac-9d1e429d5033 | -6.43616 | -44.5576 | 2026-06-11 06:16:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dabdba72-58a5-31d1-a888-11aac5f6e311 | -6.43473 | -44.56686 | 2026-06-11 06:16:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a407e606-1464-3cc3-95cd-94f0bd244a9b | -12.37195 | -47.88887 | 2026-06-11 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 93f48eea-ed96-3170-aaa6-68ad1d79f515 | -9.30957 | -45.47604 | 2026-06-11 06:16:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1ac2e459-4ef8-3fc7-9a0e-8e9247e2ac94 | -6.95621 | -44.54496 | 2026-06-11 06:16:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4b2659cb-1d86-3b05-8b6a-6bf471f6613b | -12.36181 | -47.8925 | 2026-06-11 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f35cdd30-59cf-3a87-a9e1-5c99e9d87089 | -12.36195 | -47.88721 | 2026-06-11 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 481d9886-e0db-347f-86f4-a0c26cb0f06f | -9.31865 | -45.47748 | 2026-06-11 06:16:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 13d4b9bd-cc05-3949-9e59-ea9e80244bfc | -12.3079 | -47.90772 | 2026-06-11 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 59b6e6ed-6e4c-3a30-a056-a30c92a9f0ef | -11.58011 | -47.4449 | 2026-06-11 06:16:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cedcc514-ee73-3129-bff8-7275543b8e82 | -9.32698 | -45.48467 | 2026-06-11 06:16:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f140f0e7-b745-3225-b6cc-3b2817dd02d3 | -5.55277 | -43.48941 | 2026-06-11 11:51:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 21f24149-3be8-39c3-b2b6-ed7382f49546 | -10.85453 | -46.78995 | 2026-06-11 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e60a3f54-40b9-3ab9-90c4-7a0582dc6654 | -7.28758 | -47.08941 | 2026-06-11 11:51:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 58c6acb5-5101-3998-8fdb-ae540bdeda8d | -8.2976 | -48.26954 | 2026-06-11 11:51:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| c44d1959-b1ae-3f97-b825-6ba0fd26e484 | -8.88001 | -45.68665 | 2026-06-11 11:51:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 102b2089-1747-3ee1-a6ef-522b70d158f2 | -6.90727 | -42.85688 | 2026-06-11 11:51:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| e285ddf0-5e63-309d-aaca-d2f4b6eba72d | -5.73181 | -49.09771 | 2026-06-11 11:51:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3fdadc9e-0956-3bd0-9e7a-d400e7e4383a | -8.89663 | -46.87229 | 2026-06-11 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 103c294f-b4f8-3223-89d8-ae062ecbbb47 | -7.59814 | -46.46147 | 2026-06-11 11:51:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5ed0c95b-091a-3108-9f9b-c1c28fd70f2b | -9.06137 | -44.76989 | 2026-06-11 11:51:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 835ad1ae-f6e8-30c2-a0c6-03e29d90d5a3 | -6.44627 | -44.56574 | 2026-06-11 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README10.md)
