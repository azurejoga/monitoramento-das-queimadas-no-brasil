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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75a56e6d-4897-3ad7-bd4c-0545af187953 | -3.89733 | -55.81622 | 2026-09-12 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 00e03e8b-bd61-3550-9f5d-6c3a1fc7174d | -3.33903 | -53.26849 | 2026-09-12 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02b832b9-08a4-3100-966c-f2ce2728693a | -2.47163 | -48.03989 | 2026-09-12 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 80a48c8f-4a96-3321-9f2e-61245f587828 | -5.51557 | -44.11525 | 2026-09-12 04:32:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 258b88dc-c883-3429-bd57-8f9deb846820 | -4.74193 | -48.14011 | 2026-09-12 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac87fbd7-d470-3a8c-b2b8-06f4526cab0c | -2.22666 | -51.9383 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 828e219b-ac68-3dbe-9aef-413540a47cde | -4.3607 | -54.78036 | 2026-09-12 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| de9094cc-d92e-3f49-8e93-a602081f3be9 | -3.3844 | -50.76441 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b3c3801-8cd4-3ee8-898b-59cd004c464e | -2.94371 | -50.40194 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bc2a8a35-d6ba-39b0-9934-c86ae19e392f | -3.19781 | -51.01702 | 2026-09-12 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a0405be7-5765-3a25-b384-cbf2c6c2a4b5 | -2.72741 | -57.63307 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0388533a-0f60-381d-a7b4-a56837fd7535 | -2.94504 | -50.39363 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f8dfda8-735b-32e4-8f3e-45bef43ae8d9 | -3.22956 | -46.9542 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0e3d357e-d03b-397e-94cc-709c340b4a44 | -6.27176 | -41.9506 | 2026-09-12 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f1a52181-88b6-3fee-8fd7-5a7d3b18d3e8 | -2.96733 | -50.39286 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 99fa0cad-f3c4-30df-94af-ea3c7a21922a | -4.36291 | -54.78418 | 2026-09-12 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dba2c46f-3d1d-30ca-90a2-0b40020aa42e | -3.37045 | -50.7578 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d53c70fe-387c-3678-ba97-1e14aa29e72b | -2.95585 | -50.39534 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 07a297dc-b03c-30d9-97a9-1142a624e7fd | -2.96798 | -50.38873 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a81ae6a-f2d0-32eb-99ce-11ce24cdd9e3 | -2.41232 | -47.96235 | 2026-09-12 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdbe3dd5-f34d-354d-b648-21466a199de6 | -2.7856 | -47.6202 | 2026-09-12 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54b7bb3f-051f-3b91-9d36-cc00b2aec564 | -2.82327 | -51.34531 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 872cc681-57ba-33f0-a046-4b0e4f0e8eb0 | -4.30347 | -49.1145 | 2026-09-12 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8a10feda-d03f-30b4-b3f6-827542798b80 | -5.61203 | -44.84536 | 2026-09-12 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b107cd0e-15ac-39d4-8ce2-298bda7ec947 | -4.8345 | -46.78203 | 2026-09-12 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c26ca2d4-e32f-38c5-8ade-295f43187cfe | -2.78945 | -47.61727 | 2026-09-12 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b06b8338-b75b-345d-bcb1-55d4e148d788 | -2.95026 | -50.4072 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 29beb34c-098a-30a6-adce-883ed423b2d0 | -5.791 | -44.92848 | 2026-09-12 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a883fcea-377c-332a-96dd-df2bca6378a6 | -2.96535 | -50.40528 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 153.9 |
| a40dab7a-6058-342c-a904-7416f54232c3 | -3.3691 | -50.76637 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76cdb05a-aa70-36c4-9e35-7ffd31846807 | 2.51124 | -50.85748 | 2026-09-12 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f0821be-baa9-358a-8b3c-f1d40df9ffe5 | -3.22625 | -46.9537 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 2e560d76-b130-3cda-8ce2-c5bbd3eb8277 | -2.93961 | -50.47382 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3640b2db-46aa-383b-8737-d266dbb1e19c | -2.93826 | -50.48226 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c43de72-8f99-3c1b-b5b2-8323e1d5d261 | 2.50918 | -50.84383 | 2026-09-12 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f80395a-fb24-381d-9b44-ea83ae29f33a | -2.94077 | -50.3972 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d84388df-5e3d-30d0-a07c-4d9db7bb13f6 | -3.24827 | -50.81881 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df7f9041-3f25-3a71-97e3-074570e16254 | -2.95946 | -50.39588 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 59c280fd-6884-3609-ac6a-90afb3690e3d | -5.76181 | -45.09747 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 67296a83-21d1-3acf-beb1-27ac5072c1ca | -2.67019 | -57.51111 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b125b97-ac58-3dad-8a72-c8614698a34f | -3.22679 | -46.95025 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4a014b99-7f80-321d-9ebf-8c0aa2420724 | -2.94188 | -50.48281 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dce610e-7b29-321e-a8d6-34f2d50b27da | -3.23287 | -46.95471 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6421b080-793c-39f4-b18e-c1aec9f712d0 | -3.1941 | -51.01644 | 2026-09-12 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6e7f941-f89c-3389-ac98-e37df1cc637c | -5.60784 | -44.84888 | 2026-09-12 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb8ae4b3-dc28-3df3-a382-6316c33704c6 | -2.9683 | -50.41 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a208ea76-e837-3ab1-a4f1-edff11cd4825 | -2.1164 | -48.8273 | 2026-09-12 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94f472ae-00c9-3798-bd71-3ef2d81c8589 | -1.02814 | -53.7413 | 2026-09-12 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64428bb1-9c50-362f-b987-8aba00341014 | -2.95159 | -50.39891 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4a8fc17a-7ffe-3329-a1eb-037d8a0a5eba | -5.76535 | -45.09803 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fd238fa8-a70b-3406-ad5e-02a629b00d44 | -3.33004 | -42.30222 | 2026-09-12 04:32:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c2468c4e-f854-39b5-9562-d4564782c287 | -2.95651 | -50.3912 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7794a651-1ec1-32a2-9e15-aeffeb205fe5 | -3.72807 | -40.42797 | 2026-09-12 04:32:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8d203b32-1aea-35b3-b8ef-ddac5bb789cf | -2.67707 | -54.59086 | 2026-09-12 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27446fee-f2f1-3c6f-9c4a-4eea464f4a0b | -5.77656 | -45.09575 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 956e003c-ca24-3d03-b4a9-ac86095e8cff | -3.38372 | -50.7687 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0d9cb8d-fbb4-32df-ad91-cc5b7df85b9f | -1.7919 | -47.84036 | 2026-09-12 04:32:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 854f29df-6174-3346-bc82-589a0ae2b6cf | -3.87544 | -51.18126 | 2026-09-12 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1910fafd-9a49-39b3-8ef3-21cee4d6af3b | -3.37113 | -50.75353 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2da613fe-112e-3cd6-8994-0f73e4382e2f | -3.2301 | -46.95076 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| bb60fb97-0a8a-3dcf-b39b-4266097698e7 | -0.96529 | -47.57978 | 2026-09-12 04:32:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89e7f8a6-d41e-3b63-ae5b-2884c4f7b6b2 | -5.12989 | -42.88105 | 2026-09-12 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d202491-6635-381e-a23e-d1cbb58e5928 | -3.36978 | -50.76208 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57a2bb5e-a2b1-3b74-89de-91311b8cfc28 | -4.35759 | -54.77011 | 2026-09-12 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 325124a9-9339-354c-9799-005941d6b4ca | -2.71656 | -57.62611 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 661ceca5-4b7b-3ffd-8fde-db0293caaa9b | -3.85868 | -49.21985 | 2026-09-12 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a44854de-a919-3d74-b284-adf7d09b9ebd | -2.73328 | -57.63301 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cfb37b02-2728-3375-80e5-e980700b0fe2 | -4.54712 | -38.55752 | 2026-09-12 04:32:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c2e395cb-aea1-3178-bd7c-2c227db86d51 | -1.69114 | -45.45502 | 2026-09-12 04:32:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e5ad111-87e8-3451-afc9-71ecb4b72a51 | -3.76966 | -44.08455 | 2026-09-12 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4befac1-4a03-3d07-a623-28ad7c7f1f87 | -4.54305 | -45.15906 | 2026-09-12 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ddd85bb-71c2-342e-ab54-5526762105d3 | -2.95291 | -50.39064 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 968c7875-e415-3041-9507-0c0ddb1a0d53 | -1.98761 | -47.04506 | 2026-09-12 04:32:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 344a9b5c-88dc-3195-a2c8-6f2e2ce4bf74 | -5.60846 | -44.84478 | 2026-09-12 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccf65e40-85ae-340e-b3b5-b5ca9f8c2122 | -2.97322 | -50.40226 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 717593bc-b36b-335c-954c-4747b0957c10 | -2.96764 | -50.41415 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 8a980925-7217-368f-8d0e-83bd2a477227 | -4.24333 | -49.93995 | 2026-09-12 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a13f9f4-53bd-3938-aba6-aaa35cd85c6c | -3.42104 | -40.04062 | 2026-09-12 04:32:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2fd582c2-d68e-36a9-b1c1-6f191d9766be | -2.26546 | -48.44044 | 2026-09-12 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23613e45-f553-310f-8c03-afb1c12061bb | -4.45143 | -50.15808 | 2026-09-12 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4469771-5945-3da1-ac91-cce04308cf83 | -5.77716 | -45.09178 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9e522ab6-7e1a-3162-b120-437bb8d394dc | -5.64277 | -45.55469 | 2026-09-12 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b6376b9-5b24-31ba-8e51-96207f3f0bd4 | -3.81375 | -55.8881 | 2026-09-12 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae1863d0-9dcd-3452-9761-77a4ffdeec4f | -2.96307 | -50.39642 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 4f3d080e-02bf-3a4b-86f3-54a0d70eeb42 | -2.9657 | -50.37991 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab928a37-95b4-31a8-b64a-54e26ee6e2a4 | -1.73114 | -57.15501 | 2026-09-12 04:32:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| eb442e91-9b91-35ad-8394-9709f2d7b6c2 | -2.94238 | -50.41024 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f55a7e69-d149-3654-8493-80c71c81aa22 | -1.79245 | -47.83688 | 2026-09-12 04:32:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a28ea6c0-d5f9-3b9e-a7c1-c696563f9015 | -2.32885 | -49.0826 | 2026-09-12 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa05af61-c571-3dde-8f25-1ae3f4d6f538 | -4.3568 | -54.77493 | 2026-09-12 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae48fcf6-00d4-3c01-96e6-1ff9aa3fb8bd | -3.21696 | -48.97093 | 2026-09-12 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 281e8517-a526-30a8-abc8-8e6eaa93b80c | -3.38508 | -50.76011 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8110961c-a7c7-31f0-b589-49b21a214b3f | -5.76595 | -45.09408 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| ad440dbe-4948-36e0-a36a-228b61cc3afa | -4.27082 | -46.53678 | 2026-09-12 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e956b39-abc1-3997-8fb5-a2fa0ecea733 | -2.41565 | -47.96286 | 2026-09-12 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 084a1d33-c57e-3d7a-8fd0-b0ad2644866f | -3.3712 | -57.70908 | 2026-09-12 04:32:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e3e01430-1239-3978-888c-251e34fced31 | -2.95321 | -50.41189 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| db8a1faf-3a8c-3c73-baa7-43bd558e51cd | -2.73573 | -49.45918 | 2026-09-12 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f06cae99-48cb-3ae5-a2b6-e668308bc5ef | -2.94637 | -50.38536 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae581768-6bec-334e-8aeb-7ab00fb6c06f | -3.74917 | -42.47942 | 2026-09-12 04:32:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
