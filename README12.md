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
| 1b9cb03f-1868-38da-b9ca-8792d7e82c0a | -4.69121 | -43.24586 | 2025-12-12 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b08a4b9c-f84f-3750-943a-9fd74b8a4574 | -5.15997 | -37.69383 | 2025-12-12 03:57:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38acc6d4-2733-3dfb-96f6-64c69a12f20e | -3.43354 | -41.65239 | 2025-12-12 03:57:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dfc343f3-9382-3516-9bd4-5d05bd06baff | -1.66707 | -46.23229 | 2025-12-12 03:57:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f08b6dd9-7242-3f98-9945-5e0f8212183f | -3.21584 | -42.68896 | 2025-12-12 03:57:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f797ad7-2bb8-34d0-9181-d865452ebbc6 | -2.54396 | -47.80195 | 2025-12-12 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 7eb50898-6e98-31dc-96bf-e98502e14840 | -3.02505 | -49.0582 | 2025-12-12 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94598c4d-a1c6-31fd-b493-058a5efd6319 | -3.626 | -45.38978 | 2025-12-12 03:57:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4d39458-7412-3f4d-965c-abc04a677db8 | -3.02393 | -49.05501 | 2025-12-12 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85514212-f98c-3a60-af8e-8914c040137e | -3.2359 | -42.08061 | 2025-12-12 03:57:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c43cbc75-fef2-30d2-b799-563bc4153f85 | -2.21731 | -45.40487 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e22a1949-f8e2-373a-b30a-28aec8830d2c | -3.82489 | -42.17708 | 2025-12-12 03:57:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 876e5c8a-38a1-3a44-b7a2-2659405f4d62 | -2.70037 | -45.70428 | 2025-12-12 03:57:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c3bbcb3-6df7-334b-9cdd-bf282ad44b28 | -4.73569 | -43.07656 | 2025-12-12 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75222720-0d0c-380d-b98e-e145c1ec79e0 | -4.39418 | -43.63253 | 2025-12-12 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce08b554-87a5-3aa9-95a4-0ef7cb66fc32 | -3.60534 | -45.51689 | 2025-12-12 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e613301-3735-3056-b71c-92596acb51cd | -5.1075 | -38.38741 | 2025-12-12 03:57:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5dafa362-d454-34e3-8f16-64f51f0c274c | -1.66181 | -46.23139 | 2025-12-12 03:57:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd947e08-1d46-35b0-a890-920c032adb64 | -1.84426 | -46.39706 | 2025-12-12 03:57:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65cd8ea7-5b0a-3ad9-b54d-11825fb1c1b2 | -4.45987 | -38.2492 | 2025-12-12 03:57:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ecc225b2-64e1-3a1e-a78e-fff48005e925 | -4.68712 | -43.24518 | 2025-12-12 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dec641d-f24b-3a61-844e-296ad987d7cb | -2.89989 | -40.51231 | 2025-12-12 03:57:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e34d102b-bf19-3af8-a2b7-dff0b3f2d299 | -2.23269 | -45.40813 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42cf245c-3fcb-3438-b556-3cd79ed8cbe5 | -3.85571 | -45.30175 | 2025-12-12 03:57:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54570462-fc6d-3f55-8c95-1c57285f700d | -1.55368 | -45.80626 | 2025-12-12 03:57:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48be41fa-b089-3d87-9263-db9033e051d6 | -4.65827 | -42.39619 | 2025-12-12 03:57:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6938373-36fb-3cf4-a667-d4cb575b7bde | -2.36091 | -47.68607 | 2025-12-12 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 877d6beb-154e-33d2-8719-2fa8b454e3d3 | -4.66215 | -42.39684 | 2025-12-12 03:57:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7543802c-74a3-325b-ae88-20cfdc5fb586 | -3.85514 | -45.30365 | 2025-12-12 03:57:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d41937fa-7f87-331b-8400-206998327cf2 | -3.49463 | -44.88977 | 2025-12-12 03:57:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cd6bc31-6487-3adc-9e51-c232c2837ad4 | -1.66079 | -46.23084 | 2025-12-12 03:57:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc859232-2bff-34f2-84da-f6ca51b63baa | -3.24041 | -47.47089 | 2025-12-12 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 072d2b45-3600-3ee0-b4a0-553d436bd579 | -3.39553 | -42.10858 | 2025-12-12 03:57:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| fa32688f-7997-3271-b1fc-1e7520a17887 | -2.22377 | -45.40092 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82fdc0bf-75f1-3b6e-8e52-fb0d1e026243 | -4.305 | -43.21223 | 2025-12-12 03:57:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83ef0807-9d42-3d6a-84e4-1e445803a184 | -3.06347 | -45.79964 | 2025-12-12 03:57:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 71606bde-2250-3104-b8f3-9b27b2397a48 | -3.26649 | -45.56013 | 2025-12-12 03:57:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c09073f-89dd-30c3-941c-5541421127cc | -3.27377 | -45.70513 | 2025-12-12 03:57:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e213eba4-e537-3566-974b-7928936f973f | -3.9537 | -41.52044 | 2025-12-12 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 28e183d1-f650-3821-9484-3c377a18e566 | -6.06756 | -35.2395 | 2025-12-12 03:57:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3d4c7f4-6675-3619-a1d6-6ba1c91cbeb2 | -4.38997 | -43.63179 | 2025-12-12 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f0668b2-4fbe-3c2a-b64b-48175d6a5fc0 | -2.22777 | -45.40728 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e98def2d-eaaa-3d10-b50f-bff64f7b9247 | -2.46986 | -48.06714 | 2025-12-12 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68b561da-5fd1-380d-8fee-c3788e5b0598 | -4.15831 | -39.25034 | 2025-12-12 03:57:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 970cc00d-840b-3481-8c2e-f1cb98a77c73 | -3.64218 | -39.37608 | 2025-12-12 03:57:00 | NPP-375D | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 63ec33bc-1f3a-387c-940f-5228b6967e26 | -1.31174 | -46.53121 | 2025-12-12 03:57:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e02d5647-74b3-3a3a-bc78-ac3fe1b5ad36 | -5.76392 | -42.07545 | 2025-12-12 03:57:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48ea8c3a-e8c7-3e4b-a3b8-b7c805ebc67e | -2.22312 | -45.40017 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f28db0f4-8950-3407-a23f-b86d60794b4c | -3.61291 | -41.8331 | 2025-12-12 03:57:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 067911b0-e13c-3680-ab6b-d4db655d0a03 | -2.66574 | -46.89663 | 2025-12-12 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 403a334d-5f66-3145-b2f4-1ca7de1b7522 | -1.90117 | -45.46498 | 2025-12-12 03:57:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d36244e3-9bd7-323f-bfbf-72ad2f0c7a03 | -6.47336 | -35.16627 | 2025-12-12 03:57:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e5883099-c1c2-300b-9ca5-3b00cc8be41b | -1.84957 | -46.39795 | 2025-12-12 03:57:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e994e5ca-12c7-3292-a999-eec3db572508 | -3.86048 | -45.30254 | 2025-12-12 03:57:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77ab4a45-72cb-30f0-b3e5-a533e132f453 | -4.99396 | -38.05725 | 2025-12-12 03:57:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 12ddcb0b-f166-347d-9526-cdc646419b4a | -3.85949 | -40.66265 | 2025-12-12 03:57:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc0431c9-e117-348f-9e09-b9496e31bc39 | -6.46909 | -35.16992 | 2025-12-12 03:57:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 65b27d31-217f-3a42-adf3-b03df4fe82b3 | -2.48258 | -47.77936 | 2025-12-12 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8112c5e8-33cb-31a3-b9d0-bb860aefc448 | -4.3822 | -43.62642 | 2025-12-12 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b34bda34-aa97-3a12-aa28-16c2c97d9dcb | -5.15942 | -37.6973 | 2025-12-12 03:57:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bead9ad1-cfa4-359a-a88c-823cf37b327e | -3.86988 | -40.64379 | 2025-12-12 03:57:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 731cc900-6c26-362e-8e96-0823c7ac22f6 | -2.7013 | -45.69857 | 2025-12-12 03:57:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ca624d0-e48c-376a-b4b6-6a27e2f621fe | -3.24056 | -42.07645 | 2025-12-12 03:57:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 768d61cb-8fd6-3205-88d8-3ac51db60bda | -6.47273 | -35.17046 | 2025-12-12 03:57:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e4319ca0-98ab-3771-9ef6-2a1f3becacfb | -4.378 | -43.62567 | 2025-12-12 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3861a6c6-6ead-34c2-98ae-122826a35915 | -3.65471 | -47.15236 | 2025-12-12 03:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 615c720d-230e-3d43-8535-5600171672dd | -4.515 | -40.84999 | 2025-12-12 03:57:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b4b08681-a7e0-3c7e-b43a-4fd702aaf491 | -2.43648 | -47.19035 | 2025-12-12 03:57:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 051329a8-f2fe-3571-bec6-168d4833306c | -3.60296 | -45.51824 | 2025-12-12 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49c5b766-011a-3244-a6b6-d56ee57c4c6f | -3.23982 | -47.47444 | 2025-12-12 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d738c9f2-cd85-3fce-ad63-4f05a89147b3 | -2.83043 | -45.2601 | 2025-12-12 03:57:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bb9d389-2bfb-3e07-b8a2-e8ef5884c34a | -3.98025 | -42.50491 | 2025-12-12 03:57:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9692cb3-037d-389d-b247-faebcd429448 | -2.22717 | -45.40655 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dbdf577e-1f87-3a3f-9074-cd7d46c2080f | -4.73223 | -43.07235 | 2025-12-12 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a3c18530-4016-3593-8498-5bac2aaff6b9 | -2.48248 | -47.77932 | 2025-12-12 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0cb769a8-738c-325f-956a-cc423876330a | -3.22862 | -41.79937 | 2025-12-12 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a1515b92-ae8c-366f-85e1-6115a5ae00e0 | -3.3111 | -42.53436 | 2025-12-12 03:57:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 03a11f93-b7ab-305f-a680-75569c4b1de8 | -6.30833 | -40.20346 | 2025-12-12 03:59:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bcbc3633-e70b-35d6-8f48-4552221e270e | -6.32815 | -41.88683 | 2025-12-12 03:59:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1b88e63-414b-3336-bc24-e7aacd75cd59 | -6.12391 | -41.28402 | 2025-12-12 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c7f1c3a-b5ec-3470-abea-0c09004de0cc | -6.12034 | -41.28343 | 2025-12-12 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 581a35ec-57d6-3cd9-adae-f6eb1d791517 | -7.89371 | -38.44899 | 2025-12-12 03:59:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5405fc7a-4c73-360e-b483-98c7841de752 | -6.11967 | -41.28753 | 2025-12-12 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1d447c45-c3be-3f4c-ae80-0e1ad15d6b48 | -6.93895 | -38.62127 | 2025-12-12 03:59:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 56cf8327-fd44-3731-bee1-460fd5be30b3 | -8.03433 | -43.10882 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| d7a6bc05-a1e3-3e2e-87a1-bb11ee1ce402 | -9.40726 | -35.6488 | 2025-12-12 03:59:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2d433343-d062-358c-9257-4024c2a0566b | -10.56155 | -36.70639 | 2025-12-12 03:59:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 1de926e3-664d-301f-baea-02bd7223879c | -10.23791 | -52.21902 | 2025-12-12 03:59:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efb5422c-9f58-3fe7-97ff-88c02dd634cc | -8.82838 | -36.54951 | 2025-12-12 03:59:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 525f6d6e-e05e-34b2-8917-fd31fdb4c431 | -8.80038 | -36.95144 | 2025-12-12 03:59:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee84046d-804d-362b-9d52-6c5bcb335f72 | -5.9716 | -44.06853 | 2025-12-12 03:59:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d524765-619f-3529-aa03-507cce249485 | -9.39705 | -36.02214 | 2025-12-12 03:59:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8749a653-2ccb-34e3-a035-c64ab8d62fa1 | -8.04366 | -43.10057 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| aea61330-9422-38f5-b29a-816f025f7c12 | -6.9561 | -38.62043 | 2025-12-12 03:59:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 78f8a0c6-d94d-3bd1-9e3b-964a2e852ee2 | -8.03293 | -43.09373 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 94bad56f-68ea-3ad9-8403-6d95afc98c62 | -7.89426 | -38.44551 | 2025-12-12 03:59:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 31cb7f73-544c-30ef-8e69-8eaee40f7351 | -8.03981 | -43.09988 | 2025-12-12 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 3c3faba8-6e90-3634-a251-ceef93575d7b | -6.54642 | -41.73867 | 2025-12-12 03:59:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b3d3ff42-859a-3a0e-9af6-ca4cfcfbadd2 | -7.47234 | -35.30739 | 2025-12-12 03:59:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b20e2b98-b068-34b8-9a4d-48b2e1fb4d88 | -12.13039 | -39.40529 | 2025-12-12 03:59:00 | NPP-375D | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README13.md)
