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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66984478-e73f-3656-9a74-8b2d014d90ce | -4.54115 | -43.56155 | 2024-11-11 00:20:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 032cf006-3853-350f-a965-5d63668034f1 | -3.99349 | -46.41369 | 2024-11-11 00:20:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3d25a7b4-79e7-3318-9535-a33daf463f8c | -5.82001 | -44.11392 | 2024-11-11 00:20:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e4572407-0609-3832-b4e9-f9dc66d4f6c7 | -4.09041 | -43.93945 | 2024-11-11 00:20:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 430cab77-7e83-353d-aa3f-17782565d8b9 | -4.07393 | -43.9481 | 2024-11-11 00:20:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 6a86ff07-797a-3481-bb35-edfe7e3effb1 | -4.07566 | -43.96068 | 2024-11-11 00:20:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 51e5ef0d-1dc6-3154-bd80-4d73afc8b116 | -4.45824 | -38.75541 | 2024-11-11 00:20:00 | TERRA_M-M | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c55197c7-d246-33a5-bb82-7360316e07d9 | -5.38324 | -42.7685 | 2024-11-11 00:20:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3103bb58-c903-3ea8-8664-1fee7aeeddaa | -3.31899 | -44.03711 | 2024-11-11 00:20:00 | TERRA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 7339a1d1-aca2-30eb-ae75-8141d9b3e2b4 | -7.10001 | -35.23816 | 2024-11-11 00:20:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| b4bc30bd-9aea-3fa0-8a19-517c85537d9f | -3.53477 | -45.71921 | 2024-11-11 00:20:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 19196961-011a-38c2-948a-f9eb72cf8cb7 | -3.32767 | -44.02334 | 2024-11-11 00:20:00 | TERRA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 18a90f08-fcca-38a9-a743-bf9c31454cd6 | -3.59318 | -44.54034 | 2024-11-11 00:20:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7dd8094f-9ef7-3d02-95d2-db22d7cd4d1b | -7.53933 | -35.04727 | 2024-11-11 00:20:00 | TERRA_M-M | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 8b9c02eb-09a1-3d0b-a2f4-4f8322d524c9 | -5.53948 | -39.10815 | 2024-11-11 00:20:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4612d8a2-837d-3a77-8359-82bb161ecbe9 | -5.41338 | -43.36919 | 2024-11-11 00:20:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d4106e03-b129-3343-bd57-d64841a7710b | -3.54111 | -43.18842 | 2024-11-11 00:20:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d6ab2c7d-0823-3c1f-813d-9189b9074c6e | -6.65615 | -40.97842 | 2024-11-11 00:20:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| d011a579-4594-3c72-b1cd-8c99c58b304a | -4.02568 | -46.96503 | 2024-11-11 00:20:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 17f27360-a29d-3a16-b399-9263170a929a | -4.90678 | -44.66262 | 2024-11-11 00:20:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ac64bcf2-5119-33c6-a7b7-2b2d318024d7 | -7.47542 | -35.21086 | 2024-11-11 00:20:00 | TERRA_M-M | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| ad39af99-0aff-3775-85f2-9e6c95041cef | -7.75899 | -37.20715 | 2024-11-11 00:20:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4799aee2-1f7b-3827-b953-406b4de967f5 | -6.13668 | -38.89729 | 2024-11-11 00:20:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 80445969-53c3-3cd9-b3be-efe306e3d6fe | -4.02951 | -46.97008 | 2024-11-11 00:20:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9d039837-a423-31a1-ae67-877b1bda3b59 | -3.50022 | -40.86195 | 2024-11-11 00:20:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f8f63a7f-bd0f-31f6-8c3b-aca345977b41 | -8.99269 | -35.55619 | 2024-11-11 00:20:00 | TERRA_M-M | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 03ad66d8-a224-3143-afce-0a986fc41726 | -3.53562 | -42.57694 | 2024-11-11 00:20:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ce6fe08a-6b75-3a7e-a032-e918ba1edc6b | -3.86987 | -46.07731 | 2024-11-11 00:20:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 0ba3b437-4ccf-36cc-99aa-79e45c1f56e9 | -4.54277 | -43.57358 | 2024-11-11 00:20:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 35bb1ffb-8d3f-3a13-aa77-ad1ee516cc57 | -6.8536 | -38.88261 | 2024-11-11 00:20:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e91dcdd2-a080-336d-a93c-9bc6c2277859 | -6.85487 | -38.89165 | 2024-11-11 00:20:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2948c61e-b466-3f38-95e1-9146eb6ea8ca | -6.13795 | -38.90633 | 2024-11-11 00:20:00 | TERRA_M-M | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 19f2534b-02d4-3fe0-a339-2d2e64935a72 | -10.13179 | -36.40777 | 2024-11-11 00:20:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 402fa55d-21fb-3c79-9db4-7810800d265a | -7.58852 | -34.83296 | 2024-11-11 00:20:00 | TERRA_M-M | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| fb214e53-7f91-311f-b9bf-aadc2eb9b4c6 | -4.02654 | -46.94833 | 2024-11-11 00:20:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 707bbc8f-fa5d-322d-aad7-b9edc1c2f6dd | -7.54147 | -35.04122 | 2024-11-11 00:20:00 | TERRA_M-M | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| aabca984-6b83-3063-be38-4a274a932261 | -3.32937 | -44.03571 | 2024-11-11 00:20:00 | TERRA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 430f9329-b312-3819-9889-22886870c8fd | -4.08263 | -43.93429 | 2024-11-11 00:20:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 4e79a20f-c134-3747-a407-5345a72f4500 | -3.28704 | -45.32581 | 2024-11-11 00:22:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| abcfa7d1-1c32-32c9-9db6-3ec2ece19587 | -1.74727 | -46.36771 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 169eaf7c-abfd-3767-b4fe-89ca16926d38 | -2.08185 | -46.49619 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| bc422c5e-cb6b-3457-b296-9183b666dd58 | -2.64068 | -49.52692 | 2024-11-11 00:22:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| bb6d8017-ed53-3774-9afc-30990d7983d9 | -3.24433 | -46.49141 | 2024-11-11 00:22:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f135ae3e-bfec-3642-958b-60c3535c7617 | -0.03818 | -50.78169 | 2024-11-11 00:22:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| dd5873d1-be35-326c-9d71-ea5f29cb44e0 | -3.29851 | -45.32428 | 2024-11-11 00:22:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 125.0 |
| e109e840-a40e-3781-8057-b0edf307fdaf | -3.67304 | -50.22399 | 2024-11-11 00:22:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 05c8ef9b-c048-3fff-a9b8-7ae39c7f99b4 | -2.18366 | -48.37797 | 2024-11-11 00:22:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 4ae91f0b-f634-3545-b412-0cbeec9711e1 | -2.91895 | -45.64534 | 2024-11-11 00:22:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3f245799-d6a4-3c8f-bccc-576bdcde47b5 | -2.74542 | -49.35005 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 418.0 |
| f4ae6608-d478-3050-a4c3-45a33c55ed75 | -2.70103 | -46.81749 | 2024-11-11 00:22:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| fec19211-471d-3dd6-8113-09756b05216e | -2.29491 | -46.52948 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 916b112d-bcf6-367f-881b-864b562278e0 | -2.77977 | -49.40432 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 35f7076b-50fd-3698-8993-a117276896dc | -3.03517 | -45.82318 | 2024-11-11 00:22:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 5bbb32d8-73d8-366c-88f7-8d9377cc730e | -2.91674 | -45.6293 | 2024-11-11 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| fa67a05c-fa59-3369-a87e-bb5fbd4685c4 | -2.98025 | -45.26164 | 2024-11-11 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 21366b3a-f108-3dc1-af6c-fa3506d4b175 | -2.87317 | -46.64428 | 2024-11-11 00:22:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 8a27af5c-95ad-3c95-90cf-58ba9846770f | -2.57722 | -47.35059 | 2024-11-11 00:22:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| dff89df3-da08-3370-9bb8-6932005c79b3 | -3.12345 | -45.97664 | 2024-11-11 00:22:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 93e7a3b5-1cea-3a23-8dc1-e72139a0cdac | -2.84524 | -49.45404 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6471b71d-9fc0-3b54-8b11-fbcc18ef4ec9 | -2.97965 | -45.25281 | 2024-11-11 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d212f102-004f-338e-a4d3-255fc14cdd0b | -1.96589 | -46.40943 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a257ba46-a72e-34eb-a34a-439b21a9d4d3 | -3.19227 | -50.27996 | 2024-11-11 00:22:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a12a5877-3ddc-3bf7-a6eb-0ac2d2e59a85 | -2.97577 | -45.83138 | 2024-11-11 00:22:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 8562d382-577e-3158-b01a-eeec27dcd652 | -2.23029 | -46.45234 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| be9b16b0-c5ff-3eae-a0da-d7ca42b9ec86 | -3.1355 | -45.97499 | 2024-11-11 00:22:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9f3d283b-2b59-3c7b-b4c2-34f5ad887e44 | -2.25036 | -46.50495 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c95d6297-dd11-35e8-a37e-86762360a24b | -2.98536 | -46.98729 | 2024-11-11 00:22:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 412fda56-31a8-3475-9bd4-b573e308ebe4 | -2.73974 | -49.34524 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 723c6135-8b0e-38f8-b319-eaa7e181dc42 | -2.84743 | -49.42764 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| e8b56a75-f2b3-34fb-8fe0-c4c83bd95c96 | -2.1637 | -46.42479 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| afdd05ad-0cc3-361a-863f-5b7d34727063 | -3.66991 | -50.2309 | 2024-11-11 00:22:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| f47f8ccd-8586-3439-9356-da9b97260486 | -2.25011 | -46.5733 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c11db8ce-4d1a-33be-ab5e-e776670e69df | -3.24825 | -50.31116 | 2024-11-11 00:22:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| e618a826-a7bf-3837-98f4-e6bbd1489b42 | -2.98158 | -45.83614 | 2024-11-11 00:22:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 831b86bf-e2fa-36f3-84ed-7aa79b9ddca7 | -2.52321 | -45.43768 | 2024-11-11 00:22:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 54d99ae9-f424-3261-b2fb-3910a61c662e | -2.85196 | -49.45981 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 759d405f-06b3-31c9-9fc6-971f5c727e68 | -2.87293 | -45.39635 | 2024-11-11 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 30.2 |
| f2ae45a5-4a08-3b76-8e6a-ce296a0d3f4b | -2.77118 | -49.34107 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 34b3887d-9c53-3011-a688-9a7fb1347a1e | -2.7499 | -49.38172 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 140.2 |
| ea55dc7e-929b-3372-91f1-34b79e550ad4 | -3.30057 | -45.3396 | 2024-11-11 00:22:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 80a832c4-e165-320f-9da1-27c88bb64f7c | -2.37806 | -50.33427 | 2024-11-11 00:22:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 6a67e369-f1b7-300e-8da4-df68b6a87649 | -2.75971 | -49.37476 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 598.0 |
| d2582374-b10d-30f8-95bf-2600f7e6677d | -2.97496 | -47.00904 | 2024-11-11 00:22:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 35339857-3291-3455-963a-2fc3b0641b1a | -2.60144 | -47.73632 | 2024-11-11 00:22:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b41a232c-6d82-31b6-8916-ead51b0a4c9e | 0.45965 | -50.95898 | 2024-11-11 00:22:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2a61ea97-8b28-34ab-b687-2d310b6d8692 | -2.77547 | -49.37267 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| eb3ec1b9-19a8-3439-899a-9eb842602a7c | -2.41151 | -46.52682 | 2024-11-11 00:22:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 621fb4ee-bd8d-3af7-8bdc-a2c1afe01339 | -2.88228 | -45.37955 | 2024-11-11 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 34af22c8-1262-3a6b-a6b1-003cd5ecfac8 | -2.75545 | -49.34312 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 912.5 |
| cb4e148a-11af-3459-9263-4ead41fb5f73 | -2.76398 | -49.40642 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 5516b1f0-c379-3b63-b974-fb287302097e | -2.19809 | -48.37597 | 2024-11-11 00:22:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 408837d1-923c-37ff-9831-1bc06969dcee | -2.60919 | -47.74178 | 2024-11-11 00:22:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 312106f6-b3e4-3fec-91d7-1ea438dd3a34 | -3.28718 | -44.47768 | 2024-11-11 00:22:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fe612782-766f-33a7-a75f-cb5a73bff448 | -2.176 | -46.70436 | 2024-11-11 00:22:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 84ed0f42-4ee2-3319-b961-b729a8856251 | -1.33337 | -47.71791 | 2024-11-11 00:22:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 47329821-099b-3c2b-ad69-aae545f06621 | -1.983 | -46.44351 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 64a30b2f-c098-3fb9-b78d-77459cc35999 | -2.09923 | -46.53108 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 7fdb4caf-3a5e-31ef-a305-40ea3e55f4e4 | -2.98807 | -47.00739 | 2024-11-11 00:22:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 4c3ad0de-af50-33cd-a5aa-b66deccb2841 | -2.30273 | -48.45578 | 2024-11-11 00:22:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| a58c7fa2-5005-332f-b6ee-cebb2e72afa3 | -3.13863 | -50.45559 | 2024-11-11 00:22:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |


[Clique aqui para ver as próximas entradas](README5.md)
