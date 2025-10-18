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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d35e1b9d-03d8-342e-b33f-19aae0c3828e | -5.5777 | -44.1835 | 2025-10-18 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 902e0d47-972a-3909-80f8-2974fd9eb2f2 | -10.4945 | -43.4079 | 2025-10-18 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2f28be06-36e5-3ab7-8faa-e1586bda9761 | -12.7682 | -44.8437 | 2025-10-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 225.2 |
| a25a639e-d15d-36f9-85f2-8d6574dd3063 | -10.9752 | -44.3244 | 2025-10-18 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 13012fd4-028b-3892-83a7-79bdbfe2c718 | -9.7626 | -43.9518 | 2025-10-18 00:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| cb31b294-ab95-3f8f-9fa9-d65809446609 | -10.4937 | -43.4552 | 2025-10-18 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 19ee1d98-2bdc-37fe-91e6-d4df1f8c975f | -4.4633 | -43.2152 | 2025-10-18 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 372a6811-d815-3d0a-a977-721e77a87487 | -3.8384 | -41.5729 | 2025-10-18 00:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 48a5d7a4-a3db-33be-8bc0-7dd29755e9ba | -10.5128 | -43.4525 | 2025-10-18 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 567d5d66-4263-3096-a973-256f8b12f5bb | -11.6109 | -44.0678 | 2025-10-18 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e7b09eba-fbe7-328b-b6f4-5e9e81dbf456 | -12.7673 | -44.8904 | 2025-10-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 521.8 |
| a357641e-acf6-3858-b839-c4952d2c84dd | -12.4678 | -45.4694 | 2025-10-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 72490608-2585-3be5-93f3-1c91dae8c53a | -10.4868 | -47.5424 | 2025-10-18 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 6a860c53-af62-3dfa-b11e-b43e07d3a04f | -17.8445 | -42.6088 | 2025-10-18 00:00:00 | GOES-19 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.6 |
| 11f84162-0725-35c1-a2ff-a7cdbb011f80 | -13.783 | -48.2311 | 2025-10-18 00:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 5243e063-bee1-311a-8311-2bbafa74e59a | -4.4058 | -43.4282 | 2025-10-18 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ca654fd3-767c-3edf-8227-a5bbb96a2d41 | -12.7871 | -44.8639 | 2025-10-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 895.6 |
| afa6168b-3a5b-3886-b46e-03fc93bf0ac9 | -12.7866 | -44.8873 | 2025-10-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 400.6 |
| 15d5750d-8bd7-35b1-ab44-5e1b8f710f1b | -2.9257 | -49.1747 | 2025-10-18 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 79841356-5d62-340b-9149-3b1f52fa890c | -5.0215 | -46.0097 | 2025-10-18 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 86fe6562-8324-3368-8d2b-78e69ec6c85a | -5.0029 | -46.0108 | 2025-10-18 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d60c78c3-c7c6-3e8f-9ea1-9e7d29ff900f | -4.4445 | -43.2397 | 2025-10-18 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 409.0 |
| 7ff26e75-8e65-3426-b8bd-1f72e63f4906 | -5.0214 | -46.032 | 2025-10-18 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 136a4ab7-5a03-3c79-b32e-1ec52c246e86 | -5.9095 | -44.7545 | 2025-10-18 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 9c17a8a7-9afd-34bb-8482-fe76070417d1 | -10.583 | -43.8188 | 2025-10-18 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 453a843c-3bd7-3092-8945-02650d586bff | -11.2044 | -47.8097 | 2025-10-18 00:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 8e7a056b-ac91-328c-8b80-9c452f889885 | -11.5921 | -44.0472 | 2025-10-18 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a94936b5-c26b-3b16-8e79-736129e33a21 | -12.7875 | -44.8406 | 2025-10-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 1dcc9fa1-f308-33c5-944b-700c0f075e07 | -10.9567 | -45.4349 | 2025-10-18 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| f286ced1-8d57-3851-8d18-ac630251e7a0 | -12.7678 | -44.8671 | 2025-10-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1174.8 |
| fb702257-07fe-3638-8a13-9f629628a0d1 | -13.4468 | -43.7652 | 2025-10-18 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3a1e17ec-425b-308f-85be-574d0f30c129 | -12.8004 | -44.1837 | 2025-10-18 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| ce97f2c1-6f13-3b68-b78d-191860e3109a | -3.857 | -41.5958 | 2025-10-18 00:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 754df905-559b-3020-9e47-43e3256ba469 | -10.628 | -42.2928 | 2025-10-18 00:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 5f494763-6f6d-3a5b-ad65-345144d30120 | -11.204 | -47.8318 | 2025-10-18 00:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 22169dd3-ab41-3efb-83d7-9cd09d74d414 | -3.8572 | -41.5719 | 2025-10-18 00:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 16e3ff02-aa69-387c-850d-43bd5ef0fb15 | -4.4632 | -43.2386 | 2025-10-18 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 293.6 |
| 887c4b20-8e68-386e-9b49-d8b2dfd6e2e2 | -4.4446 | -43.2164 | 2025-10-18 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 275.9 |
| 2f46aa87-892e-3fc7-9aa2-3b9aa18a8ac1 | -13.2296 | -43.9692 | 2025-10-18 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| bb434649-6d76-3e71-b2fe-9240ab56c95c | -10.4269 | -47.7484 | 2025-10-18 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| d649288e-939f-34d3-850a-e0a939086840 | -13.7636 | -48.234 | 2025-10-18 00:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ef5bfeab-7126-35de-83c4-11105ae7026d | -8.4073 | -46.2763 | 2025-10-18 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 300f35bd-a0b3-3c73-9eda-7324d2466eb5 | -13.4663 | -43.7617 | 2025-10-18 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 637f8f31-30f7-334e-8296-3c2e58ab203f | -11.2231 | -47.8295 | 2025-10-18 00:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 45ee1563-9759-30fb-ab23-6f89517a0538 | -5.9221 | -45.434 | 2025-10-18 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a8263511-469d-36c3-9360-7b698b7da4eb | -3.1431 | -50.2464 | 2025-10-18 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 08daf1c1-b40b-32c5-9115-36cd59e59279 | -10.4941 | -43.4315 | 2025-10-18 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 253.1 |
| ac9dc9eb-5053-3866-b86f-efa3a9ea7128 | -11.5917 | -44.0707 | 2025-10-18 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 46da71a7-2e4b-30d7-94a4-ee715bcdb0d4 | -10.5058 | -47.5401 | 2025-10-18 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| b7c772fb-2a27-3758-8fbc-8334edb7c7e3 | -3.1431 | -50.2464 | 2025-10-18 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| ffb242b4-174c-3f99-87f9-29b212e36171 | -5.0027 | -46.0331 | 2025-10-18 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ab5ca8f1-a29e-3cad-a6c6-5e66166eaabb | -19.0915 | -57.5512 | 2025-10-18 00:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 61.8 |
| a1fe1abd-3b39-3be7-8bf8-f6221dc9bd88 | -10.4937 | -43.4552 | 2025-10-18 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 45d945e3-b996-317d-8117-24e275765bb2 | -11.5921 | -44.0472 | 2025-10-18 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b50128bd-ee79-33a5-9945-dcae44136a13 | -3.8572 | -41.5719 | 2025-10-18 00:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 83749ff0-66cc-3e3c-bbe4-4fcb69a07971 | -10.4941 | -43.4315 | 2025-10-18 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 384.7 |
| 706ab99b-d5d6-3684-8471-64b9d6ad9099 | -13.4468 | -43.7652 | 2025-10-18 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| d7dbe4d6-f8dd-3905-9181-09d8c0195193 | -8.389 | -46.2333 | 2025-10-18 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| fd96b4e3-b731-3bb9-8a49-2a8d004c23a4 | -12.4678 | -45.4694 | 2025-10-18 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 67b89b90-7c21-3523-b2d3-983d21ca26ea | -5.9221 | -45.434 | 2025-10-18 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 0422ad14-4562-3cb1-b573-b35a74c81951 | -4.4058 | -43.4282 | 2025-10-18 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| eefe300e-4b11-3841-bcea-07c0258c45d6 | -5.0214 | -46.032 | 2025-10-18 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 48bf73da-83c0-3318-8684-60c3cac83da1 | -11.2044 | -47.8097 | 2025-10-18 00:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7a13b122-6c72-361e-a16b-cd5c8307b593 | -5.0029 | -46.0108 | 2025-10-18 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| daa4e46c-b2bf-39a8-b1c0-b7a19fc72e63 | -10.5132 | -43.4289 | 2025-10-18 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| faf1577d-21dd-3877-a08d-f5ba8975f64c | -4.4446 | -43.2164 | 2025-10-18 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 260.0 |
| 222d6cd8-a09d-3d29-a3de-4622effcc914 | -11.6109 | -44.0678 | 2025-10-18 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| bd3c12d0-13f3-38aa-8b01-d5f136c73474 | -11.204 | -47.8318 | 2025-10-18 00:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| ab06c619-c4e0-3dfa-8960-11a9d23033a5 | -11.6104 | -44.0913 | 2025-10-18 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 011f5645-86c2-3793-9fa9-898bff4169dd | -13.2296 | -43.9692 | 2025-10-18 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 844e0a76-41f3-3d56-854a-04ab9f4d3840 | -13.4663 | -43.7617 | 2025-10-18 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 19e685f9-2dca-3171-ad72-7b267a8eafc6 | -10.628 | -42.2928 | 2025-10-18 00:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 739a99bf-40a5-355a-b4e6-56c30da3ab8b | -12.7871 | -44.8639 | 2025-10-18 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| a9979b70-f0a9-36e7-8931-d4cf1f18d3f8 | -10.583 | -43.8188 | 2025-10-18 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 65cd60b2-ccff-3e35-8651-471847d35d13 | -10.4945 | -43.4079 | 2025-10-18 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| fde88123-68b2-3697-bbb4-f6bd19a03131 | -10.9567 | -45.4349 | 2025-10-18 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 88ec4ce3-0066-31d2-812d-b2b1dd32649e | -17.501 | -43.4538 | 2025-10-18 00:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 21f33a9f-2408-34c7-b337-6b4ba72655ea | -10.9752 | -44.3244 | 2025-10-18 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 82dd70ac-93e0-3443-adc2-89a6fb550209 | -4.4633 | -43.2152 | 2025-10-18 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 0d683df7-5f99-3219-8e73-15969f21bbb0 | -12.7678 | -44.8671 | 2025-10-18 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 117e8dfd-f5b4-3322-a2f6-e8cc41bd1610 | -19.1114 | -57.5486 | 2025-10-18 00:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| a3777fe9-16f9-310f-8dbb-71b75f9e9dcb | -8.3704 | -46.2127 | 2025-10-18 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c9b8b4ef-7321-3d0f-a86c-91ed3f96a138 | -3.143 | -50.2674 | 2025-10-18 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 0218d6f5-8e3b-36cf-be64-3f703c65973d | -8.3702 | -46.2352 | 2025-10-18 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 66342d45-87a1-3c91-9bea-411183db6289 | -12.7673 | -44.8904 | 2025-10-18 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 7470e863-0307-3996-8ebb-a451600701d6 | -4.4632 | -43.2386 | 2025-10-18 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 0a5345f7-4c86-3e27-850d-98e3d1fb5e02 | -5.0215 | -46.0097 | 2025-10-18 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 86e8287c-9368-3105-ada8-76bcc87a038b | -12.7866 | -44.8873 | 2025-10-18 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 4467d2e7-02e5-343b-b728-a9bc840c1c5d | -7.3447 | -43.8503 | 2025-10-18 00:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 42a184fb-b607-333a-9d86-340b30a2e0b0 | -11.5917 | -44.0707 | 2025-10-18 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 27826534-7328-3fc7-8e50-2f95692c0fc6 | -4.4445 | -43.2397 | 2025-10-18 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 369.2 |
| 9b87c516-ff6f-3466-8da7-838937e0193c | -2.9257 | -49.1747 | 2025-10-18 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 671fae60-4362-3cbb-b79a-e8fd2f5786d0 | -10.475 | -43.4342 | 2025-10-18 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d855fc27-2912-375b-b787-4088186644b8 | -9.7626 | -43.9518 | 2025-10-18 00:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 206894d6-299c-3814-870e-fb71ac22f7ad | -13.2102 | -43.9726 | 2025-10-18 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 41b41fd6-3801-34c1-984c-75a62b2b6ca0 | -11.6104 | -44.0913 | 2025-10-18 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 65e2fa8f-31e5-3cee-9cc4-e09fe688ccf1 | -3.1616 | -50.2458 | 2025-10-18 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| bbc7b9eb-1a76-3254-b593-26cfe22a5072 | -5.0215 | -46.0097 | 2025-10-18 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 5ce17a0e-b702-38c4-ba3c-5d4396a92720 | -10.4945 | -43.4079 | 2025-10-18 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 05e762ae-30d0-37fb-aaed-b8e4db5fd8e6 | -14.4523 | -52.8961 | 2025-10-18 00:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |


[Clique aqui para ver as próximas entradas](README2.md)
