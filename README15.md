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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 782a6fa3-2cee-35ed-8d6c-d147c746d5a7 | -9.0987 | -45.712002 | 2026-09-18 01:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4431f051-2755-3f52-b96f-336069b9b6ba | -5.7375 | -57.580898 | 2026-09-18 01:02:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3529bd74-1998-31fd-bc3d-cbd374ddcef4 | -14.8914 | -48.145802 | 2026-09-18 01:02:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 23d42c74-bf6a-3ed4-a2ef-d98bb0b4e9e6 | -12.4482 | -50.673801 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 578950b0-ddef-30ac-802e-038efb3960b6 | -2.9105 | -54.179298 | 2026-09-18 01:02:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d17eeb62-c68e-3d2e-a836-fcab217901ad | -3.2614 | -54.268799 | 2026-09-18 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 704f7a89-6f20-335f-abe9-0f28907f5a93 | -19.192301 | -48.795101 | 2026-09-18 01:02:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0158d859-b2ff-3702-a6d8-ebd15186e36b | -9.7173 | -54.814701 | 2026-09-18 01:02:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d41337b-f1bf-34a9-bb38-c92dceaece09 | -4.3648 | -47.7976 | 2026-09-18 01:02:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a9ed157-f207-3930-9221-96c784be8245 | -5.8731 | -53.5602 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc90a52-7fe2-3011-a041-2a6ad2213818 | -8.9567 | -51.465698 | 2026-09-18 01:02:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd470f5d-3047-3e35-8bbd-ea226ce713ad | -10.8929 | -53.996799 | 2026-09-18 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74d2c88b-fa72-3a19-b1ee-6dc101cafb52 | -3.3704 | -50.446999 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17e56271-647e-3269-82fe-0c32ca2c20fd | -11.5787 | -46.900101 | 2026-09-18 01:02:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7b106a7-c04e-3371-ad54-3853600cb38b | -12.285 | -50.770901 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f1745a3-51b2-32f5-8c2a-2e9da6f18ce1 | -12.3908 | -50.737099 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7e84126-62ad-3fec-bf88-9bde3ac6c62b | -5.977 | -55.3601 | 2026-09-18 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf80f2b-c4c1-398c-a0ea-5ae1a474bf2d | -4.5226 | -56.0793 | 2026-09-18 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cfc7f72-b493-3144-8d17-ee7dd509034f | -10.4073 | -48.680801 | 2026-09-18 01:02:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1942bf77-3721-3a5b-a102-8c0bfa9c3bf3 | -4.4764 | -54.9762 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 825651cf-3c10-38c6-9ee9-a3cabb144d20 | -5.3401 | -45.1595 | 2026-09-18 01:02:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d9205b3-7feb-3a4a-bd16-8ad20fcc0915 | -12.3798 | -50.6903 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6fc3f6c4-ccb8-37a5-9163-6d38e4db0644 | -3.5937 | -59.066601 | 2026-09-18 01:02:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 852e121d-c0e5-3fd0-b9f8-5a940fa03914 | -12.3419 | -50.748901 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36293d2e-e01e-3606-932f-ae9d95478bd9 | -11.2913 | -43.356499 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98ec426d-2cc7-3fde-94af-c27e6dc89e86 | -3.3179 | -57.848499 | 2026-09-18 01:02:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 996a5c50-2427-3281-b20b-38a27a5d4bfb | -6.0252 | -51.776901 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62220aca-01c5-33c3-82f7-d6bbf7e4fdfb | -12.3596 | -50.736401 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99d68a0c-11cf-3945-976f-1be26cc2f38e | -4.5689 | -42.942001 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2a1523f-5616-3d96-877d-3994ca6a3a64 | -5.7563 | -45.1017 | 2026-09-18 01:02:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8fc6760-771a-3153-be6e-2f82afffb17d | -5.7712 | -45.120602 | 2026-09-18 01:02:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67c235eb-41d8-3311-a176-c1d21ebdf874 | -12.4537 | -50.6973 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e90b49bc-832d-3255-98d5-789c97512d2f | -2.8909 | -54.183701 | 2026-09-18 01:02:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 418771bd-d719-38c4-8283-e7f2d362e3bd | -4.378 | -55.041302 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97ff33fb-bdb6-38e8-b845-8c0acbd0a5e7 | -19.1766 | -48.772999 | 2026-09-18 01:02:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ea56cac4-16c0-3a18-be20-9f995c9bb341 | -3.3607 | -50.449299 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23d68338-4bcb-3c3b-a28b-81fcd9d36efe | -11.6756 | -54.455399 | 2026-09-18 01:02:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82ca7a74-57c2-3881-af52-0523f076a7c3 | -4.5864 | -42.970901 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b140d43e-24a2-34d6-8bf5-9fe6db3339b5 | -12.3651 | -50.7598 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d80dadd-cc64-33cf-9ebc-4f7beb91c080 | -7.8189 | -44.891701 | 2026-09-18 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| baf02b52-7d3f-361a-82ec-de0005d97501 | -5.8921 | -52.089802 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ec40a03-6037-36c6-bc3d-8c2ffaa5cec5 | -12.3162 | -50.771599 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1df02463-ecdb-344a-af9c-0259d62a985f | -4.4386 | -55.530701 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da8b8a64-c25b-33ed-bb7a-6de7a0388f32 | -4.5059 | -54.969501 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ded2e6a9-1d33-3b4d-9c9d-67e340a36048 | -12.3773 | -50.7239 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b5eeef1-06f7-3de1-aa87-f2bcc94c4a0a | -12.2674 | -50.783401 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 71316e51-96b9-3217-b15a-1197d77a0bbf | -10.6346 | -50.2631 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d81da072-8563-34de-9e2a-79ee7e72a68c | -11.3129 | -43.3988 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56c2219e-eb63-3dcb-8ce7-40ac259281be | -12.4715 | -50.6847 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9bbc76f0-8166-39b4-9ee9-b329fecc66a6 | -12.1613 | -48.960602 | 2026-09-18 01:02:00 | METOP-C | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ff628e5-a0c7-38d3-a71b-66b796b52d2e | -12.3462 | -50.723202 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e03a189e-1614-3de6-8641-26df9e751ffc | -2.831 | -50.474701 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38d45f75-bad2-308b-9dac-c4bb070fe6f6 | -5.7401 | -51.749901 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67cca9a5-9e39-3195-b2b4-ffa6a0baefa8 | -4.5128 | -56.081501 | 2026-09-18 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6add1272-8d7f-37f7-afbe-5c5cf8340528 | -2.7049 | -57.598598 | 2026-09-18 01:02:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9dae1ea0-cb4b-3259-93f3-d78bc0788306 | -12.1675 | -46.9786 | 2026-09-18 01:02:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70c4760f-6f5a-3a09-a3ed-2b63c16a1f33 | -11.2734 | -54.1306 | 2026-09-18 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 752ed347-d7d1-35eb-9431-5c891c93fa4c | -6.6591 | -50.920101 | 2026-09-18 01:02:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e65e442c-aab7-3b60-99eb-5ab0101d9c41 | -14.1139 | -46.937199 | 2026-09-18 01:02:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aef9426d-3540-39c4-ab85-032f00f4e3cc | -2.7446 | -57.637199 | 2026-09-18 01:02:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93495bbc-0898-309c-8dcc-1c08f8c3c272 | -3.2595 | -54.305698 | 2026-09-18 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a15f5c-8754-3e42-b531-7c844e482c80 | -3.4321 | -58.215401 | 2026-09-18 01:02:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 322ca8f5-284e-32d7-b857-39eaa758dbee | -3.0427 | -51.376801 | 2026-09-18 01:02:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5a4c464-28f0-3de9-ba4a-8a6837721587 | -13.2696 | -46.915901 | 2026-09-18 01:02:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae7cf20f-2b54-332c-a8a6-da2d6c86c2c1 | -12.6336 | -50.890499 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 70488e7d-3f79-34d4-ab28-a7aa278f8a1a | -2.9007 | -54.181499 | 2026-09-18 01:02:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52d72919-c57f-3689-8bc0-da0f6cabbd04 | -12.403 | -50.701302 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23f2caf7-9469-38c0-a386-9c27f6d3ddcb | -12.4402 | -50.683899 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| faf37f5d-e60f-30a9-b783-404d91f038a5 | -13.2665 | -46.903702 | 2026-09-18 01:02:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 717e2c0f-9590-3942-a70c-87cbc5c0a980 | -2.1932 | -56.082802 | 2026-09-18 01:02:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7923a60-a7c8-34ee-93f6-6e39326fb10b | -12.3657 | -50.718498 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 42e597fd-eb47-3428-9103-d57a4cf082cd | 1.3984 | -50.906898 | 2026-09-18 01:02:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3bbfe59d-9651-3e0a-9d5c-f72e2d28f97f | -9.0933 | -45.7314 | 2026-09-18 01:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9480cc21-717a-3914-b962-e1f80359bd96 | -12.3993 | -50.6856 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e813f212-8f03-3072-9592-46ea6064374f | -5.7429 | -57.605 | 2026-09-18 01:02:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 769677e5-4e8d-3d7a-a910-e8619b2635f1 | -1.7874 | -47.839199 | 2026-09-18 01:02:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7ece99c-b46a-32f0-aad7-8ee86f6d2d16 | -11.3261 | -43.371201 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ff53701-f644-3ab3-bab5-cd12e0490032 | -4.5144 | -56.088501 | 2026-09-18 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1df7677b-6d0c-317a-97fe-7350c47a331f | -19.1903 | -48.7868 | 2026-09-18 01:02:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fe80e04c-00d2-38b3-8cc3-56bc55b998df | -14.7727 | -47.1674 | 2026-09-18 01:02:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a7b0d150-d8aa-34b4-b921-5db700ef3df8 | -9.9411 | -46.594299 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc616822-f97c-36c2-8e26-c6939eaa48ef | -2.8212 | -50.477001 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80ad84b6-06e1-31f0-a8d5-d927c3df885f | -10.6591 | -50.495399 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 970dc642-48bf-3fe9-9237-ab5a63935696 | -12.3792 | -50.731701 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 35f94a48-bfa9-3cec-a37d-ac66030ce10d | -4.3764 | -55.0345 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d2f1ab5-36a2-300b-9234-c2d9d3a0e479 | -7.6697 | -46.092201 | 2026-09-18 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 046a2843-96fd-308e-a16c-e6ab069c2f85 | -9.1658 | -49.9981 | 2026-09-18 01:02:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c84219d2-623a-3506-b95e-a49d76b73932 | -12.4561 | -50.663601 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d485030c-e501-3cd7-9909-1bcf2a04c9a4 | -12.3968 | -50.719101 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 61b6c06e-e122-37b2-b211-260c54f7ad5b | -12.3559 | -50.720901 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 126758f7-ce0c-3478-8e46-cde45cec4661 | -8.5117 | -48.491798 | 2026-09-18 01:02:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21ef5e67-d0d5-39c2-8a40-efff78f1e803 | -10.6174 | -46.572701 | 2026-09-18 01:02:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f44c0c80-d2ea-3309-aa53-1e8b9cded9b3 | -11.2781 | -43.3843 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a0da689b-433b-3092-a728-22d522bcd918 | -3.4419 | -58.213299 | 2026-09-18 01:02:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c269ed12-9f0b-3d66-b053-ef7dd3ab75af | -4.4911 | -55.490002 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea6b2983-9818-3527-bd37-e75d1d615c6f | -12.5347 | -47.0811 | 2026-09-18 01:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea3d19b7-80fd-3ea6-b2ae-38391fbbc0dd | -7.4955 | -55.0126 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f95034f-dff3-3a02-b24c-5b38176baac5 | -10.6532 | -50.470699 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 205df2ba-b9df-3bc9-9671-9f574535796c | -12.4445 | -55.000801 | 2026-09-18 01:02:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eec9318b-1b63-3fd2-b653-4d310e0719cf | -5.7659 | -45.0993 | 2026-09-18 01:02:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
