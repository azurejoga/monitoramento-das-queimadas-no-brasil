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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aa7b5a8-8a48-340c-b11e-d9989722445f | -3.1503 | -53.1762 | 2024-12-18 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4e6a29bc-f905-313f-9836-e3ff087875b9 | -1.7148 | -45.786 | 2024-12-18 01:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a42f95b9-b700-368c-8747-954d89a640e9 | -4.983 | -43.7169 | 2024-12-18 01:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| a94d793f-e6bd-3c6b-9dc6-8fba0a8c1dd0 | 4.4543 | -61.017601 | 2024-12-18 01:25:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fd4999fb-1e75-3079-8755-717de449a2a3 | -20.7353 | -54.419201 | 2024-12-18 01:25:00 | METOP-C | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 264b60f1-cc7d-3ec8-89b1-de8bd9b55d9d | -20.7335 | -54.411301 | 2024-12-18 01:25:00 | METOP-C | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5809bddf-626a-39e7-87f7-8b73b05bcf5f | -20.7372 | -54.427101 | 2024-12-18 01:25:00 | METOP-C | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3a821d34-3904-3dff-978f-5720ec229de9 | -3.5017 | -53.962601 | 2024-12-18 01:25:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 492acf63-844e-362b-9dfb-62dba805a8f6 | -3.5114 | -53.9604 | 2024-12-18 01:25:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 968f89f6-babb-3657-ab23-dad6ad287ece | -3.4985 | -53.949402 | 2024-12-18 01:25:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86dca569-82b4-3c89-9091-3aa121e87983 | -22.0776 | -56.198299 | 2024-12-18 01:25:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d88c1b63-9690-33a4-9699-217a39c4d40d | -21.057301 | -49.214001 | 2024-12-18 01:25:00 | METOP-C | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 06a99e77-c098-3558-887b-2ca851f133bb | -19.076099 | -52.854698 | 2024-12-18 01:25:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ecf17204-ac3b-3256-b014-19ba91fff7c3 | -21.061199 | -49.228401 | 2024-12-18 01:25:00 | METOP-C | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 011627a2-d182-3b57-b0c5-22ed12d865f6 | -3.5083 | -53.947102 | 2024-12-18 01:25:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f5e4699-feda-3517-bdeb-7d24458c9e30 | 4.4527 | -61.0247 | 2024-12-18 01:25:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e80225bb-cd38-3a71-9f2c-bc19f95399ec | -19.066401 | -52.8573 | 2024-12-18 01:25:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c92c0817-cf12-3df9-bc00-40a2f7ad4b77 | -19.0641 | -52.8479 | 2024-12-18 01:25:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5012b81b-838e-34de-82e6-869f13e1aa1c | -20.5158 | -55.532001 | 2024-12-18 01:25:00 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 20b23a76-6e3c-3c1c-8faf-51ab85930940 | -3.035 | -45.2321 | 2024-12-18 01:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 610577aa-30d1-3c4a-bf52-3afaf6e15032 | -4.9828 | -43.7401 | 2024-12-18 01:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| bba00dc4-5ef3-338d-b6fc-bf47a1187f28 | -4.9643 | -43.7182 | 2024-12-18 01:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 242.0 |
| 8510bb69-7804-327d-be59-2b6a32ad3a5f | -4.5376 | -43.2807 | 2024-12-18 01:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 18c8e267-ef9c-31cb-87f9-7711c3ab12d7 | -4.9645 | -43.695 | 2024-12-18 01:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 47cbecf7-9ead-307f-bc05-bc95bb1014d4 | -4.5375 | -43.304 | 2024-12-18 01:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 8790c6c4-4fc5-3a03-9ed3-4292af999073 | -4.9641 | -43.7413 | 2024-12-18 01:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 1f42dc27-2fe6-3bca-91c1-b1976202b334 | -4.9832 | -43.6938 | 2024-12-18 01:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 8d25736a-9331-3bdc-9ed2-496ca923d6e0 | -3.0164 | -45.2328 | 2024-12-18 01:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 9231db98-20dd-388a-ad1c-7ec5febb6eb0 | -3.2503 | -46.8709 | 2024-12-18 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ecb10fa4-d5bb-3225-bdfe-4539a6e1c313 | -4.983 | -43.7169 | 2024-12-18 01:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 171.1 |
| dd4d39ad-4422-38f3-ad4e-586621dbd4d5 | -4.105 | -46.7246 | 2024-12-18 01:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| faa3bebe-0669-3f57-a3d3-538d5feeb1e4 | -4.9645 | -43.695 | 2024-12-18 01:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 539d78c6-cc7e-3d16-9ce3-3f3a5f51123e | -3.0164 | -45.2328 | 2024-12-18 01:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| bc63a924-3ec2-3d40-9363-6bd12821bfab | -3.2503 | -46.8709 | 2024-12-18 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 82709b1b-8474-3c8a-9ff8-3f7f80857e7e | -4.983 | -43.7169 | 2024-12-18 01:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 72f61a06-69f4-356a-971a-e5dfd422b7e4 | -4.105 | -46.7246 | 2024-12-18 01:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 929cc49c-1377-3903-b401-67e3ecaf1283 | -3.035 | -45.2321 | 2024-12-18 01:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a1ceafd7-f4e5-39af-b736-4b17d592c6b6 | -4.9643 | -43.7182 | 2024-12-18 01:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 7163a486-e46a-3828-9861-4841cd964c21 | -6.9906 | -43.5582 | 2024-12-18 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 5066d22d-f042-3d63-a918-923c5ecc3169 | -4.105 | -46.7246 | 2024-12-18 01:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ff5f20fb-8260-3a8a-ad54-b1698bf99962 | -4.9828 | -43.7401 | 2024-12-18 01:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 94413071-6543-3bf4-b6f0-4d46fd3a8577 | -5.9371 | -48.0437 | 2024-12-18 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| db675eec-08d6-3708-b3f0-484f2c8f0c69 | -3.4969 | -53.9547 | 2024-12-18 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9814ebdb-c2f1-37ee-b58c-ecfea1ddb710 | -5.9369 | -48.0654 | 2024-12-18 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| e8ac72ce-7054-31c2-a5fb-e20dac07d176 | -9.6464 | -36.0397 | 2024-12-18 01:50:00 | GOES-16 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| 57264741-48ea-35bb-9556-4dad77c39237 | -6.9903 | -43.5815 | 2024-12-18 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 45c894cf-40ac-38cd-a97b-2ee95d475f3b | -3.035 | -45.2321 | 2024-12-18 01:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 9db7363e-eaaa-3b2f-a053-f7fde496c867 | -4.9641 | -43.7413 | 2024-12-18 01:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f1195f9b-30a0-36f3-a1aa-5a0b4f4d0aab | -4.9643 | -43.7182 | 2024-12-18 01:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 202.4 |
| cb79a079-ddc1-3012-b115-9f009ac3d37e | -5.9556 | -48.0642 | 2024-12-18 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| dbaa1cd1-2fd7-32d5-87b6-d26c5b266197 | -4.983 | -43.7169 | 2024-12-18 01:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| fcf7fa44-266e-321e-8bdb-f03accd2563f | -4.9645 | -43.695 | 2024-12-18 01:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| f082c61c-58dc-3fbf-a90d-e36e604e0946 | -6.9718 | -43.56 | 2024-12-18 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 7eda0871-3859-30f9-9127-def7926061e7 | -3.2503 | -46.8709 | 2024-12-18 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 761e29ee-6712-3499-b1b8-4263dc982cb7 | -3.0164 | -45.2328 | 2024-12-18 01:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 91f61376-5da4-378a-acb0-8b9fe0c68c36 | -6.9715 | -43.5833 | 2024-12-18 01:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7df629bb-554d-38d9-9f14-dd6803c19c23 | -20.7327 | -54.43067 | 2024-12-18 01:58:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 00e94594-a872-3cc6-a910-78011921cecc | -3.035 | -45.2321 | 2024-12-18 02:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e0375d8b-8803-39ea-b940-f8852c5068e2 | -3.0164 | -45.2328 | 2024-12-18 02:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 44865d28-02b3-33b0-a7d5-221982c68a12 | -4.105 | -46.7246 | 2024-12-18 02:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 070cfff9-1dc5-35c1-bffe-6b9a40470bbd | -6.9903 | -43.5815 | 2024-12-18 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ab78e814-1395-3313-b68c-1217ad397460 | -6.9718 | -43.56 | 2024-12-18 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 174.1 |
| aa58450f-6a93-3226-826d-37d8f39d889a | -5.9369 | -48.0654 | 2024-12-18 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 827a96e2-e3f7-3b6d-8b6a-ebb7f66e6f5e | -6.9715 | -43.5833 | 2024-12-18 02:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c0c7a871-e8a3-36b4-802d-f34d86c7b439 | -5.9371 | -48.0437 | 2024-12-18 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 32f77207-ce73-3990-a5a7-2633acfe8626 | -4.9641 | -43.7413 | 2024-12-18 02:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| b2002959-ce8a-3249-83f2-5a95ebc1ca6b | -11.8648 | -43.8172 | 2024-12-18 02:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| acbf23c3-8166-3a43-8771-71b6fa8d97f7 | -6.9906 | -43.5582 | 2024-12-18 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| c214aa5d-6e95-3c51-a139-6c19d7cdeac9 | -4.9643 | -43.7182 | 2024-12-18 02:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 20fda797-0586-340a-9904-369acde5c113 | -3.2503 | -46.8709 | 2024-12-18 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| dc58e5c3-9ae8-31b4-bad3-d97a28c3c562 | -4.983 | -43.7169 | 2024-12-18 02:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 2fa04c88-229a-31b5-91c7-a67b5b3b3f05 | -4.96 | -43.72 | 2024-12-18 02:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6760f2d2-ce97-336b-a1c6-6cf1e1a6e7fd | -12.01743 | -62.79294 | 2024-12-18 02:00:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cd923734-583d-3500-8af4-6b5fd6219d0e | -4.983 | -43.7169 | 2024-12-18 02:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 5cea8d35-b64b-3b23-b369-45751f040238 | -5.9371 | -48.0437 | 2024-12-18 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 82e265d4-b757-3879-8a62-f137120d4cab | -5.9556 | -48.0642 | 2024-12-18 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ad0788d8-089d-384e-877c-f7bf334b2898 | -4.9643 | -43.7182 | 2024-12-18 02:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| dcf81f2f-2963-30b1-8b83-561a709da3b9 | -4.5375 | -43.304 | 2024-12-18 02:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0ec200e1-392d-38f5-8400-755b4beb2387 | -3.0164 | -45.2328 | 2024-12-18 02:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 46895908-023d-343a-9e1b-df5a4b6d77ac | -3.035 | -45.2321 | 2024-12-18 02:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| c8a89e96-5a45-37ba-ab02-33ef58b00df3 | -5.9369 | -48.0654 | 2024-12-18 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| fb8316c3-da96-3269-8103-fff00bd560ad | -3.2503 | -46.8709 | 2024-12-18 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1ce27faf-0453-3daf-80f7-8302112588b9 | -4.9641 | -43.7413 | 2024-12-18 02:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| d9ae79af-33f8-3ea5-81b8-48ce42425ea5 | -3.2503 | -46.8709 | 2024-12-18 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 71d1736d-bc93-31c9-933b-41536bf8e14f | -4.9643 | -43.7182 | 2024-12-18 02:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 697da60a-875d-3ca6-8220-be3c600d67df | -4.983 | -43.7169 | 2024-12-18 02:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 8a531023-1fab-395e-a7da-d8ed1e63d05a | -5.9557 | -48.0425 | 2024-12-18 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| c5b89fbf-d296-3bfa-9f14-e791142456b7 | -5.9371 | -48.0437 | 2024-12-18 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ea25018f-9358-34a0-936a-1cb81b97acf2 | -5.9556 | -48.0642 | 2024-12-18 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 8cdeea37-edf8-3bbf-9ea6-f95f565b7d03 | -5.9369 | -48.0654 | 2024-12-18 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 53b975c5-3695-3bdb-99ff-6c4c06eaf401 | -3.0164 | -45.2328 | 2024-12-18 02:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b8536981-8d10-304b-a6a2-cc711daab3de | -5.9367 | -48.0872 | 2024-12-18 02:20:00 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 626ee9ed-2a16-359a-95b7-e3c724b4a6c5 | -3.035 | -45.2321 | 2024-12-18 02:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a5217ae0-59ef-3a8c-adee-6adfd3eccc83 | -5.9556 | -48.0642 | 2024-12-18 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 2cd31ff2-be0c-3bc2-95ba-46c3a003dd2b | -6.9906 | -43.5582 | 2024-12-18 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| db0791e7-976e-32ed-b4b2-d2c40b02f4aa | -3.0164 | -45.2328 | 2024-12-18 02:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 4df96707-74d8-3e8b-9d0c-861dac87ec72 | -4.983 | -43.7169 | 2024-12-18 02:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| e39ff12c-6e32-33e8-9fb0-89e472f9d96d | -5.9369 | -48.0654 | 2024-12-18 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 17f93a7f-4bee-39db-845b-54fdf2027ad1 | -3.035 | -45.2321 | 2024-12-18 02:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| aab5c063-70b2-34f9-b1c6-b9b7a117734e | -4.9643 | -43.7182 | 2024-12-18 02:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |


[Clique aqui para ver as próximas entradas](README7.md)
