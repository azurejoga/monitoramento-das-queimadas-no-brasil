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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64566460-96e0-3989-a570-2fe292c53dbb | -15.1311 | -52.7656 | 2025-10-08 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 923495c9-9945-3ba7-a476-50c36444267a | -14.9228 | -51.4076 | 2025-10-08 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b6d3f285-b75a-3ff0-ae63-1fe12e8304d2 | -6.9987 | -42.8308 | 2025-10-08 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| d1e1b27d-0f4a-309f-873d-1e2df5fcfc0c | -10.8728 | -51.0501 | 2025-10-08 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 3df712c7-ba54-3102-9f75-b651995baab5 | -9.1899 | -49.9818 | 2025-10-08 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| fe0c0e3b-0b3b-39d8-b049-3bdb893ac9be | -7.7919 | -44.246 | 2025-10-08 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 58107867-ac8e-3435-a4cd-48aea5386a1e | -10.4096 | -50.3538 | 2025-10-08 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c5675d95-a2c6-3bfc-80ac-d324369740ed | -10.748 | -50.4892 | 2025-10-08 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 291449c1-d93e-347b-a90d-6ca8cee61741 | -13.3048 | -48.0352 | 2025-10-08 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 5ceb29a5-c525-361a-b3d9-60f416ebc833 | -11.8881 | -51.6606 | 2025-10-08 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3590afa6-d132-32a5-a3fa-756305b111c2 | -12.0314 | -45.1901 | 2025-10-08 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 97374456-7937-38f9-abc0-a190de50a845 | -12.5109 | -54.714 | 2025-10-08 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 185.1 |
| 9f2aa0d6-1465-3dd0-b394-a16be98637c1 | -12.0122 | -45.1929 | 2025-10-08 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 114edb8c-e470-3be6-b4db-f9cb51d1cf5c | -13.2434 | -47.194 | 2025-10-08 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| b647b5c0-d174-365b-a4d4-2515c3d808a8 | -12.4437 | -50.1876 | 2025-10-08 14:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7e76c73b-4b0c-37ad-a469-916087d95457 | -12.1372 | -50.2682 | 2025-10-08 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1ceac3be-e7a2-3096-8fc5-e1f95c6d4129 | -7.7922 | -44.2229 | 2025-10-08 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 57243df4-786e-3fed-a5d1-b71c7f349c84 | -17.304 | -58.0566 | 2025-10-08 14:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 7d7ad0ad-782c-3dff-bf87-e042253de4b1 | -13.3048 | -48.0352 | 2025-10-08 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b6f18000-357e-3db9-be61-0979f65dc984 | -12.0118 | -45.2161 | 2025-10-08 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 6237c907-5a42-3586-83c2-b2ffd06ccecb | -11.1835 | -54.8584 | 2025-10-08 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| da81ab18-b791-3c9c-aab7-776a3388db88 | -12.1271 | -50.9332 | 2025-10-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| bae160a4-1e9d-336f-ab37-d2713c41218b | -14.4079 | -46.026 | 2025-10-08 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 385.3 |
| a668ed86-2356-3c93-8f95-6bd28b42dcaf | -12.1372 | -50.2682 | 2025-10-08 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 355d695e-68a9-3c14-a4f3-e47e2d63fbf8 | -7.7938 | -42.5607 | 2025-10-08 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| b192eb91-d610-3d81-b3ac-aeca3d7453f5 | -17.2837 | -58.0997 | 2025-10-08 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| dc62a10a-b636-35fd-a810-9fef2be61b8b | -12.108 | -50.9354 | 2025-10-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| aae5665f-f3df-31de-89fe-e70c9d302995 | -14.9026 | -51.4534 | 2025-10-08 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b4ba3945-9eed-31c0-95fd-35e3baef9c10 | -7.793 | -44.1535 | 2025-10-08 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0bcbefdd-d47f-3805-b5e2-94faff36aef3 | -11.4153 | -50.2023 | 2025-10-08 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| fd00102f-b79a-3c2a-8ab6-bdca53486c88 | -3.8761 | -41.5468 | 2025-10-08 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 92ec92a7-6a3c-3ed9-8b1f-8cef2cecfec5 | -8.1618 | -43.323 | 2025-10-08 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| 90533a72-9d74-3179-a1cd-176e418a44c0 | -3.2901 | -42.6213 | 2025-10-08 14:20:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 92a27ab9-28b0-3428-803d-6cbbcc9dd833 | -14.8824 | -51.4992 | 2025-10-08 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 74c3fe1e-7bfe-32c6-917e-10caace8e37b | -8.9573 | -44.6052 | 2025-10-08 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 0b0bbe39-facb-3434-b391-b934b2ffd898 | -6.9324 | -47.3391 | 2025-10-08 14:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 757a483b-9de4-3aa7-bee8-30c2b630713d | -8.9309 | -46.5809 | 2025-10-08 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 160.0 |
| f059fb43-f951-3397-a919-cb60744c9d17 | -14.8828 | -51.4777 | 2025-10-08 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f06fbedc-2f20-3bf2-ac00-a42a46407c6c | -11.4678 | -43.5011 | 2025-10-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 222771c8-f979-34c0-bf9f-6940043acde5 | -10.3904 | -50.3771 | 2025-10-08 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b8b98d98-ef5e-3097-851b-f731c762893e | -13.8117 | -45.7826 | 2025-10-08 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 218.3 |
| c5b1a7c3-cac9-363f-a31b-7da3365eac6e | -15.6538 | -44.4838 | 2025-10-08 14:20:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 4a4d8bba-fdfb-3e12-b0c4-5be58b243a9d | -15.6003 | -52.5742 | 2025-10-08 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 45ac61b3-bcda-316f-9e47-0133de7fbb5d | -7.8119 | -44.1516 | 2025-10-08 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| ae155477-897d-3f34-bf0b-fcfb01880ebd | -3.8759 | -41.5708 | 2025-10-08 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 911169c4-5e42-32fe-94ed-69de1e03da3b | -18.0209 | -57.5214 | 2025-10-08 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 208cf11d-eb0b-3178-a4e9-8d108e495a78 | -4.0567 | -42.5354 | 2025-10-08 14:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 127.1 |
| 7c31022d-7851-38e7-a46f-8b0f2d318949 | -13.2662 | -48.0409 | 2025-10-08 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d9f3266c-f5a0-3dac-a42f-754c2c3aad71 | -12.6478 | -50.571 | 2025-10-08 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 74ba658a-f4aa-33c5-9634-41d2d6e63e4d | -11.1292 | -47.7526 | 2025-10-08 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| df972c4f-181a-361f-8811-71a1a5604d88 | -12.6286 | -50.5734 | 2025-10-08 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 928a4589-5974-31d9-b21d-31a967bdadea | -16.0754 | -45.7634 | 2025-10-08 14:20:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 125.1 |
| c444f73a-1fd6-38f4-924a-35055d12a66a | -12.3908 | -51.1366 | 2025-10-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| bbf98333-5cdb-36a0-8dcf-51b17730c49e | -12.1576 | -51.4399 | 2025-10-08 14:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0b00670d-b68a-3b24-9341-d158082a966e | -12.3846 | -50.3026 | 2025-10-08 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| e3bc90b0-8374-3ca1-8f07-141d046d69c9 | -15.3984 | -47.9938 | 2025-10-08 14:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e79776fe-b65f-3e21-8e5c-6b2db32d12f4 | -15.748 | -49.0083 | 2025-10-08 14:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 3260cb2e-f795-3b0c-bbfa-09df9a39e94b | -11.7641 | -45.1375 | 2025-10-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0618f3bb-2cd7-3978-b76d-7916a7a2e422 | -7.5463 | -44.3164 | 2025-10-08 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| af4bc39e-f2f9-3478-aa7f-7129cf94d99f | -12.6481 | -50.5495 | 2025-10-08 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ce11abd7-3a93-388c-949a-b8dc55a57cb4 | -6.7164 | -42.8337 | 2025-10-08 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 549e870c-15a8-3c8f-91ba-635e57fd9ac2 | -11.1646 | -54.86 | 2025-10-08 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| cd64f08f-b504-300f-8f41-c8000e14cd70 | -6.7352 | -42.832 | 2025-10-08 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| f068bd10-54ef-36b1-ae75-076fdfd5fcad | -3.8948 | -41.5458 | 2025-10-08 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 118.6 |
| bbefd016-b979-324a-913d-7b9790832deb | -11.7833 | -45.1347 | 2025-10-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 19a73827-ff25-3d37-91a8-f79d6f63127d | -12.7157 | -47.6748 | 2025-10-08 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| f48e81e3-d780-3fd3-867c-0f4ac1fbac06 | -11.0075 | -50.8875 | 2025-10-08 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 5ba11b76-ed5b-35f2-9584-6655f3247314 | -14.9216 | -51.4722 | 2025-10-08 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 36ebc570-02c1-3f2f-89f9-92631e24de12 | -14.9224 | -51.4292 | 2025-10-08 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 9a6951f0-3263-398d-bbf2-e44071ff7f0b | -7.4669 | -43.0674 | 2025-10-08 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| 4e9c22d4-9ab7-3ab7-9233-7781c3557b3b | -13.2855 | -48.0381 | 2025-10-08 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 4717b21c-c0b9-37ca-a4e5-31f2d47c5bb1 | -12.1083 | -50.914 | 2025-10-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f8fd5f9d-ff1f-3856-99be-0d4c062495f1 | -7.4672 | -43.0438 | 2025-10-08 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| f8c55fe5-c6ba-3e44-bb31-e7d2e8314515 | -6.7355 | -42.8084 | 2025-10-08 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 748711dc-5b38-31c1-bf1e-483e28d01191 | 0.9292 | -51.1455 | 2025-10-08 14:20:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 8978be79-24fb-35f7-bd0a-2bac8f7f0664 | -3.8573 | -41.5479 | 2025-10-08 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| b7e808d1-1877-331a-8143-4776752e1597 | -11.7221 | -45.3508 | 2025-10-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| afbcc4bf-5333-3c90-bf40-a8afe65098ac | -11.7043 | -46.3794 | 2025-10-08 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| d3cba1f1-659b-3b9e-be3c-fd67d966a29b | -11.7386 | -51.4868 | 2025-10-08 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| aac7c4a3-bdc6-3324-8045-b529b3212822 | -12.629 | -50.5519 | 2025-10-08 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 5b6eb414-dc4d-3d70-ad3a-658810881557 | -12.1642 | -50.9928 | 2025-10-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| f8047289-6d51-38d0-a69c-22592acd8144 | -11.0259 | -50.928 | 2025-10-08 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| b6b99a10-b5a4-34bf-8832-e16fcc6fd42b | -14.922 | -51.4507 | 2025-10-08 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| a7e38b85-5612-39d1-9a64-e9d7aeb2e65b | -11.7576 | -51.4847 | 2025-10-08 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| c125b73d-0195-356e-9ac5-0ce7f91b1ebd | -12.0122 | -45.1929 | 2025-10-08 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 2c80cff3-1feb-3946-8523-e97e61189206 | -17.8611 | -57.6436 | 2025-10-08 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| fc3e5c50-490d-3900-a006-68eb879ca924 | -7.7203 | -42.4023 | 2025-10-08 14:20:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| bcb33b48-3061-36fe-9799-ce66eac36e51 | -4.5712 | -41.288 | 2025-10-08 14:20:00 | GOES-19 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| fa40b404-5618-3c65-9b42-82f3fa740b38 | -13.3513 | -47.6042 | 2025-10-08 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6ec7070b-1f42-3d73-affb-e1290cff57dd | -11.4682 | -43.4774 | 2025-10-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 6a67f17a-24f8-37f9-b66f-381afee1ccbb | -11.1457 | -54.8617 | 2025-10-08 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 63024073-0777-3a36-a889-53b7f2e0df24 | -13.2847 | -48.0827 | 2025-10-08 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 5a4a58b6-80b9-33f0-9665-745c93491d42 | -11.0262 | -50.9067 | 2025-10-08 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b5825e10-e4b6-3042-9474-2a98fafc6984 | -13.3706 | -47.6013 | 2025-10-08 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 1e366154-a8ea-36dc-9737-986e18cf02e4 | -11.8042 | -45.0393 | 2025-10-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 770f51d0-d315-30e6-ab07-51fb47951f27 | -12.1646 | -50.9714 | 2025-10-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c070393e-c57f-3e13-ac4a-aa9724123f07 | -12.0314 | -45.1901 | 2025-10-08 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| ce020d61-f50a-3b0d-9fcf-924ac32c386c | -12.385 | -50.281 | 2025-10-08 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b34cba9f-0aee-3631-8beb-a0e842e60fc2 | -8.9121 | -46.5829 | 2025-10-08 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| a5ff903a-65e9-33f9-936f-4ad4997ff2e9 | -14.3889 | -46.0063 | 2025-10-08 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 141.4 |


[Clique aqui para ver as próximas entradas](README110.md)
