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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 545d2cdf-500d-377d-9509-5b02107242ac | -6.25766 | -53.64999 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ba46679c-9488-3997-b370-328ca6f9fd75 | -3.38989 | -59.39907 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e4da4d41-000b-306c-9c1f-47ed5d217056 | -7.3132 | -60.57433 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 3b48cf04-f42d-323b-995e-69fc2c7dd0d7 | -2.62372 | -44.99364 | 2026-08-31 16:52:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2afc96c8-5162-3fbd-90bc-f88149e71f95 | -1.91129 | -44.70123 | 2026-08-31 16:52:00 | NOAA-20 | PORTO RICO DO MARANHÃO | MARANHÃO | Brasil | 2109056 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a794c860-e470-3c1d-a9fc-30c033ff4a6a | -4.16011 | -60.71844 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cc7aa6a1-3bf1-343b-8db8-80f5219c970e | -6.38189 | -55.21587 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 312b6f22-8b7c-374c-adb3-c969af77cdac | -6.18443 | -55.44112 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7ad70c38-e765-30ec-9158-62b0addd6837 | -6.67399 | -59.07412 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf765e13-b07b-386f-8884-517692c241a3 | -3.33329 | -59.39641 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0047e875-a1fd-3d28-a281-1520c8ed58d4 | -4.31092 | -49.09197 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 543a8107-89de-31af-8edd-72efb4d58ef0 | -1.67141 | -48.51955 | 2026-08-31 16:52:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| df049158-bd86-3916-a917-34a795eb1669 | -3.63519 | -60.55597 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| cafe0d98-9d14-36d6-aaff-a92ac88e6062 | -7.30881 | -60.57116 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| a437a7b7-7937-3c8f-935c-315a221f2333 | -5.04148 | -49.23125 | 2026-08-31 16:52:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9cb9d7c4-0c6f-37fb-b4fb-f69677c225d6 | -2.04947 | -48.95211 | 2026-08-31 16:52:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| af8c33cc-20f7-3c9c-ada9-d2a75d2b9002 | -2.8075 | -43.55892 | 2026-08-31 16:52:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 29e41800-a7af-351a-a1fa-b0f427413807 | -6.62501 | -58.38365 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 00fe5dd6-1a70-363b-b1da-b0ceb2979bc4 | -1.11937 | -48.04857 | 2026-08-31 16:52:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c2e9a95-ae64-3734-ba83-41f6c7886a26 | -2.3851 | -46.06849 | 2026-08-31 16:52:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f2cee3d-00cc-3cf8-ac95-54421cbac38b | -6.30683 | -53.57801 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 235ed419-7562-3506-bcd1-a731f331bfc0 | -5.95963 | -53.61045 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 9e1f059b-39a9-3ae6-b5f7-dbd9f5722be5 | -4.59682 | -42.92792 | 2026-08-31 16:52:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| cd309013-1011-3909-b00c-3389af5e0e4d | -6.85943 | -59.47701 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e61a20d-c318-3925-9ede-0d70f8439088 | -6.12144 | -57.67469 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 3ab298d5-3125-3c62-9dfd-e5ee2dbbbfd4 | -5.0808 | -62.44374 | 2026-08-31 16:52:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 493187f6-e22f-36b1-8bd9-20667d372de0 | -3.266 | -58.24171 | 2026-08-31 16:52:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 341261b3-bae7-3518-81cb-fd5f5f2d24e3 | -7.48213 | -61.38356 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| db087aad-5227-3b9c-b6c3-cd42af4d9831 | -0.98305 | -48.16632 | 2026-08-31 16:52:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| ade3ee6a-ede0-3edf-8bd4-9101b09f319c | -6.76083 | -59.44813 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e8f12c59-1e18-3eff-9730-00b83fc92206 | -1.75702 | -48.23183 | 2026-08-31 16:52:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b7dccd1-cfbb-3641-a404-fe653f77d2ad | -6.86021 | -59.48014 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 66295ea7-fa21-35e3-8e80-db11d969f9f7 | 1.37351 | -50.74427 | 2026-08-31 16:52:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 257f356d-ae6c-3d9e-8e92-3177d3e2e7ed | -5.82251 | -52.38785 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0609240c-fd52-3f0d-8773-a90cebaa82b1 | -7.52184 | -61.37861 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 16d6651e-0819-37ee-9351-c8bcf1bc0fd6 | -4.14959 | -60.69834 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 60779f8b-ab51-30ee-b7a3-ac2dcf005e18 | -3.62921 | -60.55672 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 795a52ad-e63e-31a3-8a2a-a8a2f490fc26 | -3.38975 | -57.94097 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9d035a0-11e4-3495-92b3-d350a4d2a7d9 | -3.83628 | -55.56558 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| bace28b8-7081-311c-818a-e784d5f90dcd | -6.51847 | -55.26516 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0962a04f-d7da-305a-ad6a-585de7606db6 | -3.64082 | -45.43444 | 2026-08-31 16:52:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 26c24fe0-4cc4-3828-8f3a-40ac8477989f | -3.50265 | -59.04527 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 12ef32e6-2d60-36a9-87ef-21764faaa3d4 | -7.44875 | -60.75959 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 080a4681-a4ee-39db-973a-46d41c9573ca | -4.30504 | -45.14398 | 2026-08-31 16:52:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7639709e-7b57-3670-ac10-dc7675f4f519 | -0.95931 | -47.30888 | 2026-08-31 16:52:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0c9ba521-0b23-3c8a-b8da-7e12bb63607f | -4.22014 | -54.37289 | 2026-08-31 16:52:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6f80e938-ae64-3fc0-aee0-bd10a3fa15b4 | -4.96685 | -55.84698 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5fec25c4-9c3b-3e17-a69b-0fef62e7be6a | -6.20845 | -53.58987 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d59bda36-124d-3ef1-9405-f11d2b03a4d0 | -5.85946 | -57.55469 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| aacb281c-899e-38f2-a984-1146833244ee | -6.25064 | -55.43557 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d4778ec4-88b2-3719-8bbb-2e3dd4b81fed | -3.42222 | -43.37462 | 2026-08-31 16:52:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 9fe66f46-13e1-3209-8c71-55e98838e277 | -1.86161 | -47.34982 | 2026-08-31 16:52:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 15957fea-ec3d-3b4e-80cd-1b5db50b57f3 | -3.39815 | -42.78902 | 2026-08-31 16:52:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 09a06edc-be4a-3be4-87d8-2ae5bb28c744 | -6.21234 | -53.58938 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 38c20943-229f-3320-9f9e-8cb85e0e5196 | -6.14067 | -53.53038 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 73c82b1f-f7b6-3e04-902b-e359c46ef9dc | -1.61487 | -45.09393 | 2026-08-31 16:52:00 | NOAA-20 | APICUM-AÇU | MARANHÃO | Brasil | 2100832 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3e5fd886-a5bf-306d-a588-8cbf80d91a62 | -2.75918 | -44.94987 | 2026-08-31 16:52:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ec29d6f-7ef5-315a-9bd5-417e8b8034bf | -7.31639 | -60.58007 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 013e710d-3ccf-30bb-9638-ac0a546317dc | -6.38246 | -55.21997 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 21bdd46b-7573-3698-aba2-722d0ba0483c | -5.85707 | -52.08734 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e4972e75-c9ce-31cb-a3b0-a2581d8a0b92 | -6.42099 | -55.52782 | 2026-08-31 16:52:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e39880ef-a9e2-3d48-8304-759c5d49f52f | -6.51906 | -55.26934 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acdec6f4-3889-3225-b609-5a9fc8281777 | -3.07836 | -59.13111 | 2026-08-31 16:52:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fee05a40-e466-3586-84f8-be3567ba6509 | -5.68753 | -53.75304 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 20b86534-0588-31c2-bce7-dd329b7e9646 | -2.74267 | -45.97712 | 2026-08-31 16:52:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 32b2dab9-2b8b-31ed-89f9-2a3c8918bfbb | -3.83143 | -55.56224 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b23e92de-262c-398e-8a44-9ae635d456f8 | -1.9277 | -44.80554 | 2026-08-31 16:52:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 97b92f5b-9c96-3feb-ac15-f5308cc726b1 | -6.84565 | -59.46215 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc3b3af4-8aff-324f-9a90-7ada6ade2f37 | -4.53967 | -55.71775 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 644eaacd-cab4-39ba-bce7-bfd7bdf544b5 | -2.76118 | -44.96853 | 2026-08-31 16:52:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0a865e72-8d89-34c4-8377-b8bbd550176a | -4.30814 | -49.09593 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 09f64f06-faf4-3c19-99f5-1292d96db085 | -6.81257 | -57.62959 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 949bbfe1-959c-3752-b6c3-af313de280e9 | -3.41871 | -58.35083 | 2026-08-31 16:52:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5bd5a480-7286-3fc8-8836-d9345772e9c3 | -2.48463 | -48.02068 | 2026-08-31 16:52:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 57026d9d-78b1-35b6-bd67-769755736fab | -4.59455 | -42.92748 | 2026-08-31 16:52:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 3c1d71d2-ae85-3863-8dd8-bec24c5a7094 | -7.44012 | -61.42359 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7927da1b-8862-3f52-b461-34f275cd1061 | -0.82553 | -47.78421 | 2026-08-31 16:52:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fde86460-c34b-38cd-b5ed-6d96636fba53 | -6.05929 | -58.00028 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| db1b6402-f25c-3c58-9459-5dd5f8802c79 | -6.25266 | -53.67084 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1846e982-ca76-3fa6-bf4c-8dd7d42a3d3a | -6.11809 | -59.94345 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 751b06a9-ec5f-3fd2-854e-837bc151459b | -6.25638 | -53.67288 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 191a7a5d-14bf-3a45-a9cc-dc1faa763815 | -6.12102 | -57.67173 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 60e585ef-8f58-38c3-96a7-afce6fff95c2 | -5.92005 | -57.69336 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fea01cbc-fe70-33ef-aeb6-2740acd7757e | -7.33536 | -60.59781 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e8dc190e-f2c5-30f0-940c-0f85a607d80f | -2.5629 | -49.11547 | 2026-08-31 16:52:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b243b3b-742a-39df-861d-6674be1eb59f | -5.42446 | -51.19857 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2cd9ac43-d70e-3297-bf7f-6b45c991134a | -6.86603 | -59.47937 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e72a93a8-7a97-36b0-803a-d4816fd950d9 | -3.63046 | -60.56549 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 80c64cf4-e1eb-3bd9-a259-04000ec885ed | -7.28179 | -60.65738 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| eb0dd3e6-d498-3a76-99ed-6b655a182ff4 | -2.66601 | -45.31509 | 2026-08-31 16:52:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 442c17d5-5422-37eb-83cd-d0ce260bb6cb | -7.19129 | -60.67629 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 935eb914-4aaa-30db-a887-fb05ca579ec0 | -2.55653 | -44.10089 | 2026-08-31 16:52:00 | NOAA-20 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35ec2d11-46c6-31df-ab3f-7b28f88f7985 | -3.26406 | -58.24046 | 2026-08-31 16:52:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| ccf47918-031a-3f52-b2b3-55b0f1870a76 | -5.2485 | -55.8979 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4e0ddd4b-bcaf-3f67-8ac0-7b80a16c7e12 | -3.39993 | -43.26543 | 2026-08-31 16:52:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1ace5831-04d0-3661-b4c5-a2e108ae904d | -3.21753 | -61.17792 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| eeb64ff2-6104-377a-bdcb-f29612252b8e | -6.86579 | -59.48035 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5c249146-73d9-353f-be8e-8d1ede841bae | -2.9865 | -43.1831 | 2026-08-31 16:52:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e03d62a6-db16-31f8-bea4-77ef7ba73b62 | -6.84012 | -59.72754 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 879277fb-9b64-359e-989f-f31356b86940 | -7.48432 | -61.40055 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |


[Clique aqui para ver as próximas entradas](README170.md)
