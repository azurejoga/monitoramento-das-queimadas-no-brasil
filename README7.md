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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d4ab73c-bcdd-3ff3-888c-f29f446b3626 | -10.83685 | -50.7093 | 2026-09-01 00:24:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7f53cbd6-b5cc-3d99-a9c0-f0e9a6b35e5e | -14.72777 | -53.58897 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 67050647-d663-3149-a635-2537576fb849 | -15.45146 | -53.96626 | 2026-09-01 00:24:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e86df3d-86a2-3fc3-a365-1cbf2c77949e | -11.62829 | -54.56995 | 2026-09-01 00:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 9810b4fc-8a87-33c8-b4cb-682ad86b497b | -17.1929 | -54.31187 | 2026-09-01 00:24:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 2e54b2cb-9db1-33d5-a4c4-d821a715691d | -14.45735 | -52.51876 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 806fbbf3-f7a1-3586-b91d-355476201db2 | -14.13697 | -52.79387 | 2026-09-01 00:24:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 4f33612e-87c4-3b84-9c25-bea3fb6b9ac8 | -14.12671 | -52.7859 | 2026-09-01 00:24:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 73468210-34c3-3e75-b11f-c19af3ef979b | -19.19316 | -57.38525 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| bfe27e66-73a6-3ef7-95c3-936bac69e7f0 | -10.19892 | -50.36069 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 91119967-eb0a-331a-8e86-5cceaec9837b | -18.70048 | -46.59691 | 2026-09-01 00:24:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6818a142-034f-3044-be68-1e914818375c | -10.17315 | -50.33658 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| a92f1fa3-3c4b-34ee-844d-0f8e487f9de5 | -10.15808 | -50.31063 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 4387f42c-9ec3-311f-87a7-ff29b87a763c | -10.20553 | -50.33141 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 75198948-7103-3296-a527-8e4759ebc218 | -15.02942 | -52.77585 | 2026-09-01 00:24:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 24361f14-9da0-3dc6-9270-42afe644ba64 | -10.3408 | -50.00765 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0969a060-aad7-37ed-bd62-2f48dcf322e4 | -14.40886 | -52.50314 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| dc3313d1-6a8b-36a6-81d8-b880d5c68c5f | -14.12805 | -52.79526 | 2026-09-01 00:24:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| fd3b236c-0bfb-374b-b89e-0fbbab09820b | -10.41849 | -57.23443 | 2026-09-01 00:24:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ec8a4e99-5561-3838-8bf8-1dcc9dc6434c | -10.74001 | -54.01562 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 30b1762a-63ed-331d-a058-565325be5fd2 | -19.22321 | -57.33098 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.0 |
| 1c129249-66fb-3ba7-bb8a-3ed6da2c63cd | -14.39493 | -52.53424 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 312aa5ce-a894-3816-9b72-d0b88e659747 | -19.21721 | -57.37592 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 49baaf4b-7cbd-33fd-a0f0-3962343f6427 | -14.27525 | -52.86114 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c59badca-753d-33ba-9e74-c7dc22f4df7a | -11.0614 | -51.52631 | 2026-09-01 00:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ecdebfea-af53-300a-b8e8-42fcb10697c3 | -11.69147 | -54.55454 | 2026-09-01 00:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 009f25be-719a-3c8e-bc86-c096d41da4cf | -10.01979 | -44.69816 | 2026-09-01 00:24:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 0a686959-6b05-3ac7-8c01-0170ab1d2b30 | -13.82009 | -54.01504 | 2026-09-01 00:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 02c9ddbb-539a-3fcb-9df8-e59e902d779c | -15.61172 | -56.40047 | 2026-09-01 00:24:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e4deb8ba-bf48-3639-8b36-78a04a9c932f | -17.36837 | -42.34321 | 2026-09-01 00:24:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 836c66e1-37df-3bbe-9bc5-90e3e1ec0d12 | -11.12822 | -51.50444 | 2026-09-01 00:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 476e5cfd-a55a-3acd-ad68-4bccd85d47ba | -13.46506 | -57.034 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f6a274c7-1d94-3c9d-bc62-a12f6282d560 | -15.01743 | -52.7645 | 2026-09-01 00:24:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bfc5c511-0cd9-353f-ab52-3d312ca6a378 | -10.75634 | -54.0682 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 5f63af76-463e-3128-8600-6ca0a56e2055 | -15.11186 | -49.63545 | 2026-09-01 00:24:00 | TERRA_M-M | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3c5d3e55-3c72-3643-8a02-d1ae57274bf8 | -14.9856 | -48.11003 | 2026-09-01 00:24:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 59051c7b-17f3-3d3e-880a-91dfc9b5a5b8 | -15.3952 | -53.75191 | 2026-09-01 00:24:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b45d38c1-1a78-3200-9f38-17f1c47c6534 | -10.03657 | -44.69515 | 2026-09-01 00:24:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 196.3 |
| f5fe5a26-de23-3ee0-898d-e9637630aeb7 | -11.21173 | -46.13683 | 2026-09-01 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 974d8438-7579-380f-ba16-1bd1afa70330 | -19.18806 | -57.3417 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 553807d5-7bcd-31ec-9a69-f5592734941e | -10.16022 | -50.32448 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 680315d9-9118-3557-a0ad-15fba0996745 | -11.31238 | -45.19326 | 2026-09-01 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| fdcdcdeb-3d40-36ec-bc46-bca6d5b4e850 | -10.75643 | -54.00406 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4d1979b4-b9bf-362e-8d48-6866dc4276d7 | -18.49407 | -50.9071 | 2026-09-01 00:24:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cb62f43a-dfcc-3a8b-adb2-5628b62dde2f | -10.51644 | -57.43291 | 2026-09-01 00:24:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9880ff17-3225-3fe7-b218-f092979760ae | -13.47629 | -57.02629 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bc542465-58d3-361b-8c39-89f81c11ce52 | -15.4527 | -53.97536 | 2026-09-01 00:24:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b9c0ea2e-1670-39b0-adf8-f5380b489446 | -10.19264 | -50.31931 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 3324bc9c-797e-3419-88b0-2cfa44aa4e19 | -16.04534 | -54.40598 | 2026-09-01 00:24:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 83b91f10-86a0-3bc9-bac1-f823a9fe10cd | -19.1906 | -57.33512 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| d70151bf-c4b8-3d8e-b71e-084409afb930 | -15.29961 | -53.1912 | 2026-09-01 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f76ba833-0ba7-3b3d-8aee-91aae85c1725 | -14.43789 | -49.00051 | 2026-09-01 00:24:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 21a85467-9476-3856-964c-0d7f068db1e7 | -16.48372 | -47.94719 | 2026-09-01 00:24:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 42103e5e-d672-3a58-8125-3b935afe9b27 | -15.41005 | -52.73062 | 2026-09-01 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| cc311703-8ee2-37ad-98a3-28c5198e091b | -16.41421 | -49.90832 | 2026-09-01 00:24:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| ea34af0e-c156-3653-9fc4-63900ee42258 | -15.73411 | -56.10073 | 2026-09-01 00:24:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| ed3f9605-50c0-3cdd-a528-9d0293199ad2 | -11.66413 | -47.62822 | 2026-09-01 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ab8ff215-41ff-3bd5-b6ae-be2632269dfa | -14.40122 | -52.51398 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9c772c88-21b3-3de1-90db-f511337164c8 | -15.79576 | -51.08452 | 2026-09-01 00:24:00 | TERRA_M-M | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9e955dde-ce7e-3e99-aeb6-556d7377b771 | -14.1383 | -52.80319 | 2026-09-01 00:24:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 03884ac9-8bd1-3103-87b4-d45d51892df6 | -15.39986 | -52.72281 | 2026-09-01 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9f5be404-dbd7-3696-939b-559c2b8ff336 | -10.74907 | -47.98298 | 2026-09-01 00:24:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 97240c08-f434-3e17-8ddd-19eac2b1425b | -15.10895 | -49.64362 | 2026-09-01 00:24:00 | TERRA_M-M | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| db558859-3ccf-3078-9b7e-eab825f7a428 | -11.17364 | -55.09182 | 2026-09-01 00:24:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 23af8767-92dc-3a09-8d34-f2c87e0926ff | -19.23902 | -57.37315 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 21146755-bcbd-3878-a62a-6f58ff626154 | -14.68504 | -53.53989 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| ebdffeae-a1b1-3f65-b66d-390dfc90217a | -14.12045 | -52.80589 | 2026-09-01 00:24:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 07f5a2aa-1023-39eb-acc0-315671b78226 | -15.29933 | -53.85544 | 2026-09-01 00:24:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f2017455-7d6d-3253-9722-8d6b0f9cae7c | -18.49255 | -50.89689 | 2026-09-01 00:24:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| dc94fb07-b56f-36d8-b3ef-0e4311868436 | -9.94426 | -53.98795 | 2026-09-01 00:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e67fa21d-c89b-3774-8639-cb5b44126897 | -17.90261 | -52.10209 | 2026-09-01 00:24:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d9020791-f96f-3137-914e-9c2e12eff41f | -13.56607 | -55.1422 | 2026-09-01 00:24:00 | TERRA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 340ccc53-a9a5-3025-ac33-62eff85788a1 | -15.63937 | -56.38533 | 2026-09-01 00:24:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e8fc73f6-2635-304c-90d9-47c53bd0a91f | -15.02809 | -52.76655 | 2026-09-01 00:24:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e92e7b89-8b14-3d3f-b9bc-78204adc13c0 | -15.01873 | -52.77378 | 2026-09-01 00:24:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b2322079-f9b4-3dd9-9491-db82c928723b | -15.75829 | -56.1018 | 2026-09-01 00:24:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b2deb85e-d009-36a9-ba5e-c9e17f6a273b | -14.58948 | -54.1202 | 2026-09-01 00:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| da114bb9-7890-36bf-bdbc-eccfa2ee2005 | -11.67385 | -47.60604 | 2026-09-01 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 7e2c837c-f066-3bb9-80d6-a31a629435b7 | -14.57573 | -54.08524 | 2026-09-01 00:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2683c71a-0714-3d77-87ec-1b65034c5f75 | -10.7715 | -54.04768 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a9c7e711-af9b-3f75-a2bf-56d131a128e0 | -17.39499 | -42.37389 | 2026-09-01 00:24:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 241.5 |
| 448b147b-9426-30c7-aa0e-f3fae6757f75 | -15.40874 | -52.72145 | 2026-09-01 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 526a091d-48ed-3a20-9c88-2dc8e3913ca2 | -15.39854 | -52.71355 | 2026-09-01 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1668d4a4-dff7-3344-89e3-c08716b47c03 | -15.05447 | -48.38457 | 2026-09-01 00:24:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6bca9457-6d24-395e-afd3-0f10e4cb23ee | -10.04573 | -48.69183 | 2026-09-01 00:24:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| c0167fd1-4038-3153-a034-9d12acb61997 | -10.78499 | -50.5057 | 2026-09-01 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a2afc698-81dd-32a1-afa5-3feb1ebcbf41 | -11.66359 | -47.61288 | 2026-09-01 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 1a8bac4b-afc2-3eb0-893e-98d1348258f2 | -14.3873 | -52.54502 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3efc6a0e-dc32-36ad-bd67-36f83f9e6aec | -13.44006 | -51.87106 | 2026-09-01 00:24:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af7532cb-6047-3987-8efc-69f9574d1648 | -9.9645 | -53.93889 | 2026-09-01 00:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 295b9cfb-1719-322a-9f4e-3da67242775b | -17.36664 | -42.34824 | 2026-09-01 00:24:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 8e90daac-b5ee-3c67-89bd-c2ed892da766 | -16.05425 | -54.40472 | 2026-09-01 00:24:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 58a25550-aa8c-3067-b2ed-311cc95133e2 | -3.63822 | -60.56092 | 2026-09-01 00:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 237d1c85-263e-3f25-820c-5ffcbb0b6c13 | -6.13622 | -55.65182 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 948205ec-fe97-326a-80b0-1c7d56e25f3a | -7.34537 | -55.18945 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b63fb057-8eb4-385f-9d3c-145ce08c7b89 | -9.92378 | -60.49512 | 2026-09-01 00:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 4b4c1711-f94a-3d50-a3fe-f6e160365fff | -3.50669 | -56.31926 | 2026-09-01 00:26:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 78efcf22-1e6c-33a1-ab27-ecf68ceed9c1 | -7.5262 | -61.38445 | 2026-09-01 00:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6fc78f2b-f8e6-33dd-b7c7-162f3c8ca3f8 | -7.54094 | -46.11039 | 2026-09-01 00:26:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 5b3ea9f8-e0f1-3d62-83e7-94f41ebc072b | -7.31389 | -60.57784 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README8.md)
