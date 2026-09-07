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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1a69e5a-e03c-3a40-b890-b2c0dcf85068 | -9.7522 | -43.3907 | 2026-09-07 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 212.2 |
| f98df323-f41a-369b-ad9c-370246b1bfad | -9.7332 | -43.3932 | 2026-09-07 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 184.5 |
| ba804975-187e-398e-be40-ca84c50b73d2 | -3.4053 | -59.4263 | 2026-09-07 13:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 1ea20898-b96b-357f-a47c-ebeeac472659 | -2.7582 | -49.4983 | 2026-09-07 13:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 45d48441-fb1c-3e03-b2a2-a6e56b918e84 | -3.5406 | -48.1889 | 2026-09-07 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 428a7f5c-f00e-348e-b66c-1288ccbabe9b | -3.1461 | -60.6696 | 2026-09-07 13:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| f259656f-9f25-3822-87a0-3a70b8eb59d1 | -11.3251 | -45.0855 | 2026-09-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 6d3ed6d5-cb14-3c86-9968-370a135d7c6c | -2.6387 | -46.7817 | 2026-09-07 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| a7917a15-72df-3568-84b2-8c067c53b89d | -3.1462 | -60.6506 | 2026-09-07 13:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 02e67e7c-aefc-3101-bbc6-51f49e39ea7b | -11.3443 | -45.0828 | 2026-09-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 4d8bdeca-ccca-3b7b-a99e-bdb6674dae8d | -10.6752 | -45.1747 | 2026-09-07 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 39bcfddd-d40c-3a30-8a9a-bb9ec9d0cace | -4.3516 | -48.9713 | 2026-09-07 13:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 05dccec2-f99b-35a0-bcc5-ed6da1bcf92f | -2.6388 | -46.7597 | 2026-09-07 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 6a79533c-df27-3028-9b1f-e48d5a2adbba | -10.1977 | -47.8848 | 2026-09-07 13:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e4563a96-57a9-3982-b3f0-69529cf91596 | -2.8839 | -50.4428 | 2026-09-07 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 827f69ab-86fb-36f6-8c9b-cd79f3a65868 | -2.6387 | -46.7817 | 2026-09-07 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 2035078a-479a-3200-ab40-801ac0f25248 | -9.7325 | -43.4403 | 2026-09-07 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 30b5ca9b-5ac0-3591-a3da-993e87a90f27 | -2.6202 | -46.7822 | 2026-09-07 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b09702d2-5859-33d8-87d7-a21475d82105 | -9.7141 | -43.3956 | 2026-09-07 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 103034d4-a1b3-343c-8ccf-5c382218cb00 | -9.7138 | -43.4192 | 2026-09-07 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 99.5 |
| a0c9bd41-d95b-34ab-aef7-41b04d6852bf | -10.6752 | -45.1747 | 2026-09-07 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 2cb99a76-66f2-3fec-9f1a-d1de30a77079 | -4.3516 | -48.9713 | 2026-09-07 13:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 03786d62-a6e7-3d0e-b633-043f2dc13855 | -2.7582 | -49.4983 | 2026-09-07 13:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| a5933118-4bd5-3ecf-a4b8-31f3b0bc64fd | -11.3447 | -45.0597 | 2026-09-07 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| bffac804-2a8a-3fd8-b279-84c9123d31dd | -10.179 | -47.8649 | 2026-09-07 13:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d89544be-719d-3676-91bd-ad02a929fbe7 | -3.1461 | -60.6696 | 2026-09-07 13:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| d5b05f14-60d5-3d63-b360-c9d1a9906c4e | -5.8031 | -46.2271 | 2026-09-07 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| fe072c5f-a723-3c65-8c6a-595e99906b30 | -2.7582 | -49.4771 | 2026-09-07 13:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 243.4 |
| fee15ae7-b878-34a2-994a-a95f454a7adb | -2.6388 | -46.7597 | 2026-09-07 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 352072ab-ebae-3ab8-9466-06478e6f8f6f | -9.7332 | -43.3932 | 2026-09-07 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 186.5 |
| e1c17a69-25dd-3d29-8a5e-2e28ffc1e846 | -11.3251 | -45.0855 | 2026-09-07 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ebcc85bc-21f1-32dc-8356-9767522ac713 | -11.3443 | -45.0828 | 2026-09-07 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 950f4ed2-c2d2-30c5-85bb-40840a91f93c | -3.1462 | -60.6506 | 2026-09-07 13:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| d3f09f6e-9a62-35ea-b360-ad0fd9c3c84a | -9.7522 | -43.3907 | 2026-09-07 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 238.3 |
| 3c849626-4811-3c25-aa9f-befebcd4bee1 | -9.7325 | -43.4403 | 2026-09-07 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 190.8 |
| ee644680-5140-3f5e-9ed2-125e43810f3a | -9.7522 | -43.3907 | 2026-09-07 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 348.3 |
| f380db66-71d3-3fad-a6d0-815299193aaf | -9.7332 | -43.3932 | 2026-09-07 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 235.9 |
| 8ba29da0-2ed2-3a09-8ba1-a6babbff7f68 | -5.8031 | -46.2271 | 2026-09-07 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 9cd35c5f-e6a3-31a5-8602-c7e2098d0c36 | -2.6202 | -46.7822 | 2026-09-07 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| f4b3d76f-b247-318b-b2b5-0ed6145162e1 | -10.6752 | -45.1747 | 2026-09-07 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 156.6 |
| f2a505d0-0aef-31ac-9366-6911ba5d9859 | -2.8839 | -50.4428 | 2026-09-07 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 70ea67d0-636b-36a4-97e5-c9cdae789bac | -2.6388 | -46.7597 | 2026-09-07 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0c743eac-fbb9-39e7-a9cd-cc0ccef69b2d | -2.7582 | -49.4771 | 2026-09-07 13:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 270.8 |
| c10f2844-99e1-3ca3-940b-f46064206ecf | -10.6748 | -45.1977 | 2026-09-07 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| abf6825d-8b43-3bf5-b754-bedd08872c61 | -3.1462 | -60.6506 | 2026-09-07 13:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 6e4c3ce6-d0cb-3bc9-bc3b-8f290c3e1287 | -2.7582 | -49.4983 | 2026-09-07 13:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 1ec94942-c86d-3018-8a39-4ad5e68e1a4e | -10.179 | -47.8649 | 2026-09-07 13:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2a6f2e16-1ab5-3f2f-9360-07b8f6d4a9c5 | -3.4053 | -59.4263 | 2026-09-07 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 06d463dc-1367-334c-8dbb-e096f380bfc2 | -11.3247 | -45.1086 | 2026-09-07 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 27086dec-dbe9-37ba-88e3-9c243672e1de | -10.1977 | -47.8848 | 2026-09-07 13:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 6f52d22d-bab9-380e-914b-6e6f176c028c | -11.3251 | -45.0855 | 2026-09-07 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 0c81cced-4fb8-34cc-b3eb-379aa3bd11f7 | -5.1439 | -55.9543 | 2026-09-07 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| c84d0c5e-c003-3fc6-a1e8-9b76eeeede85 | -4.3516 | -48.9713 | 2026-09-07 13:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| fcef1288-afdf-3179-b251-b3344b3eabde | -9.7328 | -43.4168 | 2026-09-07 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 420.5 |
| a3d08199-0bb2-3e72-9636-a8238d827001 | -2.6387 | -46.7817 | 2026-09-07 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 22e6f029-2d8b-352a-a36e-a283dda41bc5 | -9.7138 | -43.4192 | 2026-09-07 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 3f8061c2-831b-35e5-af97-f23e79894680 | -5.9818 | -57.7087 | 2026-09-07 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 307.7 |
| 0c27e817-819b-3b24-bb19-bba65a7871c8 | -11.3443 | -45.0828 | 2026-09-07 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 909b1534-8b79-3ccd-bbd6-ac6fd98da54f | -11.3251 | -45.0855 | 2026-09-07 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 37d5ad97-7420-3005-975e-18efda0aa53c | -2.7582 | -49.4771 | 2026-09-07 14:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 216.6 |
| 26116d80-8e09-3e69-be53-c96e3354f49e | -2.6388 | -46.7597 | 2026-09-07 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 96f39bfc-29b4-354c-b77f-f0bdd229402c | -2.6387 | -46.7817 | 2026-09-07 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 9754949a-5b15-382a-a7d1-423e7dc57873 | -9.7332 | -43.3932 | 2026-09-07 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 215.4 |
| f75babf8-f735-39de-b2ce-3c7f021a4753 | -9.7325 | -43.4403 | 2026-09-07 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 329.0 |
| b3bc0db3-1158-38f1-abd2-6f4939555929 | -9.7519 | -43.4143 | 2026-09-07 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1435.5 |
| a9d981c9-9012-3141-abd2-651c4b102b2e | -2.8839 | -50.4428 | 2026-09-07 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 06d585d1-ab60-3395-ba2c-a53a98e75aab | -2.6202 | -46.7822 | 2026-09-07 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2ee7f03c-d383-37e5-ab2c-da3503ef0584 | -5.9819 | -57.6892 | 2026-09-07 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 7d51e758-10df-34f8-a0b4-52fd37b4852e | -11.3247 | -45.1086 | 2026-09-07 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| ae273b2e-cd1f-3ddb-af30-fc6bb8a82355 | -4.3516 | -48.9713 | 2026-09-07 14:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| d0128d3a-fbe1-3c96-97bf-3f29b29624b7 | -9.7328 | -43.4168 | 2026-09-07 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 566.2 |
| 1c2e6a64-abad-3648-83ca-e668782872b6 | -9.7138 | -43.4192 | 2026-09-07 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 180.7 |
| 8553c294-6fde-351a-b852-feb92ce4f826 | -5.1439 | -55.9543 | 2026-09-07 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 2579a36e-c5a5-39e3-aff1-eec9bd43985e | -2.8839 | -50.4428 | 2026-09-07 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 5c478ecb-0d95-3f4a-a27e-db6f84c31065 | -2.6202 | -46.7822 | 2026-09-07 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| daf4623e-6e59-30c9-92db-8561a00b2730 | -10.6752 | -45.1747 | 2026-09-07 14:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| d04af079-0fe9-3ac8-a252-878d1c9f4d75 | -9.7519 | -43.4143 | 2026-09-07 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1486.0 |
| 4644b733-8042-33b3-837c-10c99b9adf9b | -9.7332 | -43.3932 | 2026-09-07 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 229.3 |
| 1f91c0a5-91d6-3e4e-905f-f2aee403cdcd | -5.1439 | -55.9543 | 2026-09-07 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 93604237-f990-3bfc-8ad0-5179d5ec3647 | -11.3443 | -45.0828 | 2026-09-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 57176b97-7478-385d-8ffa-db021fea01a8 | -10.159 | -45.3558 | 2026-09-07 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 486e3cb5-8568-31bf-8358-251c61be65d0 | -4.3516 | -48.9713 | 2026-09-07 14:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 69d42eea-4bd9-3177-ba85-31436cc24099 | -2.7582 | -49.4771 | 2026-09-07 14:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 226.8 |
| 5dd2be84-349d-3c3a-80e4-1b862ff11319 | -2.8655 | -50.4434 | 2026-09-07 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6f08e388-f7de-3220-844e-c39e34c7367a | -9.7328 | -43.4168 | 2026-09-07 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 643.0 |
| 4e6a2867-2d40-370c-a343-673e51cb961b | -11.3251 | -45.0855 | 2026-09-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 6c631821-3c11-346f-8f43-db33ee673eb9 | -9.7522 | -43.3907 | 2026-09-07 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 353.4 |
| 415fc183-39c2-3fbe-8afa-09d99ad84857 | -2.6388 | -46.7597 | 2026-09-07 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| cfa9d7ba-d021-33a6-b453-652dae30eaf2 | -11.3247 | -45.1086 | 2026-09-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c0232c84-0cf8-3ed8-95a6-ebbc489bd81d | -2.6387 | -46.7817 | 2026-09-07 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 184.2 |
| bf07a4db-b18d-3e33-9215-f5571755776e | -5.9818 | -57.7087 | 2026-09-07 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 2f00df7f-0c60-3343-a13f-991eb2af7a4c | -2.8654 | -50.4643 | 2026-09-07 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 638ef717-6049-3bd7-ba3f-0defc38605aa | -9.77 | -43.43 | 2026-09-07 14:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69cd858f-3d7f-3cb8-9a01-310acd1522c8 | -9.71 | -43.42 | 2026-09-07 14:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 998823db-5d9b-3904-8000-a795756f1f71 | -9.74 | -43.38 | 2026-09-07 14:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3f34e2ed-5355-3265-9e19-c0073bacc702 | -11.3251 | -45.0855 | 2026-09-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| d0a33bc1-ebf8-3fd1-8bf2-f9a6069a2216 | -9.7332 | -43.3932 | 2026-09-07 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 245.1 |
| 2909e075-4dfc-3002-82dd-8aa2f0a2f3ba | -4.3516 | -48.9713 | 2026-09-07 14:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 151.1 |
| d4e3cdd8-b89d-3cea-994d-0c16b2ce336c | -2.6387 | -46.7817 | 2026-09-07 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 5193da65-ac3c-3dd9-a6b4-a0beac8c17e9 | -2.7582 | -49.4771 | 2026-09-07 14:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 257.6 |


[Clique aqui para ver as próximas entradas](README41.md)
