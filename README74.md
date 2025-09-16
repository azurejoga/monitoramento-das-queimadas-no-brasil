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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5622d067-dc12-3e30-8a5f-9b0c44fac442 | -8.599 | -46.33822 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6538ffca-22d2-3356-a133-3dae3c3895ec | -11.12495 | -45.12121 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d91921d-04c4-34e6-be56-dd1374af8382 | -14.38581 | -52.90541 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19f48579-3145-36f3-b849-41abc4823ea2 | -12.54189 | -45.87016 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 70387636-8099-3531-9b1e-cffd920ae847 | -11.50129 | -43.72439 | 2025-09-16 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f25f4007-4ff0-3427-9d71-df2770904e9b | -13.28715 | -54.23851 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c05c640-7528-3c9a-b500-9e16e82e6027 | -12.46692 | -53.84087 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16a7c077-332e-33dd-9b63-8bf5d1303b8b | -9.09795 | -44.84243 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 951cf78e-c6f1-3f8e-8bbc-3f2fb9f817ae | -8.39691 | -47.2597 | 2025-09-16 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c687c12b-49d9-367c-9708-b6db9f192d78 | -11.96757 | -46.77844 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb2e5ab1-d3f0-3fd8-b56a-8597697687db | -10.97308 | -47.19391 | 2025-09-16 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5419a4e-c48a-3bfc-b1de-2b55af1cdd71 | -11.11401 | -45.32637 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac401808-0c15-375b-b487-685c0ef09c27 | -9.74375 | -55.3744 | 2025-09-16 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e40554ec-1389-3ec0-b95e-764e1a319699 | -13.7468 | -48.7763 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 809bca73-df8c-3ad3-a4bd-e3d8985d9a70 | -8.12308 | -50.16472 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63a97637-f8ff-3b7a-aa28-1e403a623f39 | -14.81197 | -51.66658 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4d312fa5-6730-396b-882e-31deeefa701d | -12.80134 | -47.25177 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95666710-8a4d-378b-9cb6-5e576e51b358 | -10.71934 | -44.74356 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c8f15c05-5002-38db-b671-981db251492b | -8.12187 | -50.17287 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aef7ad89-5547-3474-b7aa-fa9647f2571b | -8.6126 | -46.40587 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 405d2567-7f0b-3fd8-a0b2-02c4e3379cce | -14.65775 | -52.07332 | 2025-09-16 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8bd0ed60-3015-35ef-a523-36ba72f4a6d7 | -11.10784 | -45.33445 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8350077-6cdd-3f5d-9e24-82c21d23202a | -10.72335 | -44.75373 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da188233-2750-3153-9168-cdfd93310df9 | -11.14263 | -45.34239 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 740b6fac-92d7-361d-9941-931a4ebe5123 | -9.62766 | -62.40341 | 2025-09-16 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7fb7c16-3f3f-398e-ae08-289f101336ef | -10.72304 | -46.48564 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 83312197-5e95-3657-9ca8-5a2d78607a74 | -9.09336 | -44.84687 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e56a052-0008-3ac1-8442-bfe2c7af2bf0 | -10.64155 | -48.74706 | 2025-09-16 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6415f0ca-c2bd-3388-bff6-818a4bcffa63 | -15.62004 | -47.36773 | 2025-09-16 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5c9526fc-5ce0-3cdf-94d4-c4d89ddbce10 | -12.10106 | -44.8292 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8bddbb4-44ca-3269-813c-2f2dd18ae481 | -10.74322 | -44.76397 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82a60447-1a5f-3642-8ceb-328e08ffc433 | -10.89486 | -47.79589 | 2025-09-16 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b8b2db48-ab88-3d38-a568-31fa74d44eb8 | -12.98676 | -47.94983 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a4755bb-d71d-3ca4-b327-65abdbb8d654 | -11.12102 | -45.35111 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdf6e7c5-1ec2-371b-85eb-b98d81f67da0 | -14.61768 | -46.37391 | 2025-09-16 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db9b54be-1bb4-38d1-b401-ad907597f411 | -9.45711 | -48.61051 | 2025-09-16 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edc34e02-8f66-3567-926b-da6bf9027f86 | -10.79973 | -45.97787 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1dd6a8c-fae5-3fc3-8901-b0c4b18a5025 | -11.44146 | -47.30751 | 2025-09-16 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a768f93-0dd4-3893-b28b-a290a30097b5 | -9.04854 | -44.83585 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 50420d41-3f52-3746-8316-52b10179f0b9 | -8.98659 | -45.75511 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61cc0aa6-fa2e-3a81-862a-90520606b1b3 | -9.05826 | -44.8401 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9e34d56-95e3-358a-9012-73cbafc54d45 | -12.77926 | -47.95956 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c816ac31-9ecb-3c3d-b01c-b8a4c0a07f12 | -12.7542 | -47.96658 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5d9ec944-9e28-3e5a-95bb-846fb39a033b | -11.13295 | -45.33815 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e17755db-7d63-3d90-b7fc-6e5df936a34a | -12.10787 | -44.81737 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71078a1a-d425-39bf-a5ab-03913cab5bb5 | -12.11353 | -44.81501 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f39715ff-c105-321b-a896-13530c60105f | -12.11921 | -44.81248 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06dbde05-d117-39c7-8f8c-bef8fd902636 | -14.60301 | -46.3298 | 2025-09-16 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bd097d0-186d-35a1-81a4-e6ee99fa89d2 | -8.66873 | -46.36729 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e828937a-d9a0-3452-a0ef-25fe46901422 | -9.3501 | -56.86538 | 2025-09-16 04:51:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9693f3c8-54b1-3885-9aca-dc86f63d9d53 | -8.66975 | -46.36979 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4f2394c-0a33-3fb3-8558-3974f204c3a1 | -14.35484 | -52.92706 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f6e70a9-a4b0-38ea-9cd7-e21614ec5506 | -12.66565 | -47.9402 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26f62287-0a02-350f-a6e5-0a5b2ccff9f6 | -12.68537 | -47.98962 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 34179495-a66c-305b-be78-79357893d3e8 | -12.80361 | -47.94154 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31cae8b0-e9e0-346f-924b-88ce2f845b7e | -14.38693 | -52.89796 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2aa535f-7388-3290-a8c5-a8bedb8caa35 | -12.73898 | -47.19959 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a85576c9-21d8-3233-8aa2-0959c41703f7 | -11.12718 | -45.34315 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b44d1e7-0d19-3229-9eb8-99b777c48b5c | -12.79434 | -44.74324 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f68314f-b8a4-3202-b4ee-66fed8626534 | -10.72062 | -46.50384 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 402da8e6-e59a-3fd3-8b79-8db553ad9656 | -10.7949 | -45.97754 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6515465-95ed-3722-9c28-c92566165210 | -14.39088 | -52.89477 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 632e4f40-6570-32b2-88dd-27b9d5048f23 | -9.73689 | -55.37323 | 2025-09-16 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c3deea0-c9aa-31f3-8a7e-34413178a1f1 | -12.61285 | -47.98806 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0d873b35-a239-3c3e-812d-aae384b41f40 | -12.74351 | -47.20025 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e749f8f-7f88-3c75-9751-3d69efb53e05 | -8.66463 | -46.37358 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93441039-ad54-38a9-973e-3580ce0ff1e7 | -13.21528 | -47.2995 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 05c2594b-6689-3b84-a0d3-7f62efe4c373 | -10.71872 | -46.51812 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a9741f3f-e68d-37d5-9942-3c355e81c11d | -8.76156 | -48.80379 | 2025-09-16 04:51:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| df973db6-898b-3c64-b68f-2b642a53701d | -12.67371 | -47.94561 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b826a79-2a69-364e-96b5-cbda98681e5b | -9.74032 | -55.37381 | 2025-09-16 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e3cc766e-b62f-3b51-bf08-c0d7d7aa415f | -11.12535 | -45.11803 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cb2b31e-7917-357a-acf1-475c72fcecdd | -8.97479 | -45.04293 | 2025-09-16 04:51:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d22f014-21b4-3730-91cd-1b944539f4fc | -9.04618 | -44.85328 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5deccb16-ea38-3060-949f-f86656bd42bc | -12.63687 | -48.00404 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6ab668e-fea8-3991-ace8-32f5af84413e | -12.84539 | -47.12879 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6349b663-b403-3cc3-afb7-88cd7e184654 | -10.71624 | -44.75905 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5293f55c-316e-3ef9-a08a-5cfea7e8b05a | -11.70827 | -46.87166 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4fe5e59-2703-37b2-a344-a6f2a14bcf06 | -10.71377 | -44.74572 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0f68b90-c4f1-362d-8323-212c573471c2 | -8.66421 | -46.36662 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3848a587-bbdd-357c-86c8-448967237643 | -12.69984 | -47.74756 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c391b0c-9b1e-3ab1-a068-3a65ae6ee5bc | -8.84219 | -47.94298 | 2025-09-16 04:51:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4577e5b3-5216-371a-80e9-fe7d85089236 | -9.0921 | -44.84778 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee9757f7-6f36-3459-bcb0-d7cf355c4c87 | -11.13146 | -45.34954 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d146f2bf-f436-3d7e-be56-aedb1995803f | -8.90897 | -46.1551 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af41f0dc-be0c-3a0a-8f11-e12cf347645b | -10.43367 | -50.65458 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76491983-778b-3567-808a-9e1e4b9dcce1 | -15.61765 | -47.36583 | 2025-09-16 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da9deb5c-0293-3410-beda-af992d9dd3fe | -8.87607 | -46.19341 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ce34226-5096-39a0-941c-69061e4f8371 | -8.13392 | -49.38017 | 2025-09-16 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a03e3c9a-e41a-3f2b-9f8c-7b6641a392cb | -8.87674 | -46.18858 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 33e4f41d-9343-3231-bc7c-a7b2d5a54071 | -13.21585 | -47.29519 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e9df22f-7e20-39eb-abe0-890cdd39d9e6 | -12.95284 | -47.95957 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ed59d44d-ecde-3454-ae74-962a8af400fc | -12.7701 | -47.96256 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b77ea4ff-ec9b-3954-a804-37a651c494ae | -12.62574 | -45.77093 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fec9ef66-5d7d-31df-8d18-d3d8de65e9cc | -12.62288 | -45.75187 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6782809e-736a-384c-bfb6-2bdecc43e3b9 | -14.30042 | -49.52772 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a0091aa4-7000-32f0-b292-4c69cd380666 | -9.74718 | -55.37498 | 2025-09-16 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 777c9e41-4c1c-361f-b971-254ea5ffe5f3 | -12.80765 | -47.23885 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93b13674-b50c-3d67-ba8f-5ebf99f4b3f6 | -14.92281 | -51.64835 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01d789a6-1015-341c-9d23-a3b7e1b3cb09 | -14.54883 | -47.37248 | 2025-09-16 04:51:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README75.md)
