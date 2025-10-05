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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5beaa375-69ac-3660-873d-4be4fe1a6920 | -10.35821 | -48.16692 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 3aa5160f-ce84-34c3-a123-f741bd21ae9d | -10.41455 | -51.67291 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 547122ed-02f5-3e55-a654-9d804e040869 | -13.37445 | -47.55277 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75cb0f2c-f77b-34dc-9c4d-5e802a8d6df6 | -8.63257 | -54.99802 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efb6c03e-3ec2-36f8-95a5-5c5669cfc876 | -12.36991 | -50.25558 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e79d185-c79f-3141-973d-a027bb7507ea | -13.14508 | -47.80214 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 117de3bc-d0af-334a-b4a5-f554233abfc0 | -13.14463 | -47.9802 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d01eb9ee-9352-3b22-8b90-4dd28335e721 | -13.30983 | -47.56576 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ccc7ff2-5063-3b85-a0c0-20745c3a35ad | -11.62749 | -52.25092 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7db492a3-ce4b-35f4-a624-205ecea7f35c | -11.48946 | -46.78599 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d446ad22-6b76-33b4-afe1-ce784a0d0310 | -11.81381 | -45.05293 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 6f194a3c-11f6-3bb3-8907-508e3ad47ad7 | -12.82319 | -46.86021 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7bc5993-bd3c-3090-9d50-113f4c728e06 | -13.34372 | -47.19284 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd7f85d2-7db6-375f-8572-4e6396ff682a | -7.52581 | -41.2701 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 68167398-10c0-3053-b950-d66b88b3b427 | -7.03074 | -42.80309 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c3993b96-42ce-3c1c-98eb-b51d01579211 | -10.66268 | -48.46975 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8c78cf4-98b2-3448-a04a-b20589c81842 | -11.59506 | -46.71128 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 628ba126-1bee-3b07-8716-ef4067c47ed1 | -7.78309 | -49.83841 | 2025-10-05 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5a5d769-41a4-3740-8821-c770afa696ab | -11.00654 | -45.59253 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ffdc1c6-5467-30b6-bd02-377e284fc595 | -12.57553 | -54.77338 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4a0ddd1-7bfb-34c4-b1b6-1f6e69cd6451 | -13.43677 | -47.2721 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c993e81-f945-32c5-883f-0fff5effe9ae | -11.05622 | -47.77645 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8757b7e1-a377-36c3-a884-a68bd40bdb3d | -11.03069 | -45.57437 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef172105-e272-3992-b335-f084f9269ffb | -13.15882 | -50.91125 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e9e87c5-49b1-3803-9975-f44f36f0adf3 | -13.35325 | -47.58931 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 471683f5-b0aa-31bf-962b-745e8248ae55 | -11.86318 | -44.94998 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0741929e-65b6-3428-a357-cbc1b74393fb | -11.07913 | -47.90886 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67de7744-6af7-3c4b-b107-71850b4af5f2 | -11.16322 | -47.75898 | 2025-10-05 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bda1436a-9b7c-337e-9749-505fe634f407 | -13.27331 | -47.5938 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47edddae-4b55-3a73-adbe-c340e2b3ac89 | -13.08468 | -47.95264 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c6f54c1-2630-34e8-8751-5df329256b8a | -8.62579 | -54.96741 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5868a93-408a-329e-8506-dcab3c6c90a8 | -7.1922 | -42.93255 | 2025-10-05 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77a6dc85-4b6f-31f7-9ca7-70303d69af33 | -7.44878 | -46.52054 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60e1bf1d-1ab6-33a3-8033-c05254b724af | -10.11684 | -45.69171 | 2025-10-05 04:46:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85ecd427-a27a-372b-b702-8910a1ea5254 | -7.31497 | -45.98929 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 36af678a-2fc8-3376-89d2-464e73f241a1 | -9.91159 | -45.95428 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d12e3516-e4e7-313a-b13f-ef14e5e0d75f | -12.82959 | -48.32492 | 2025-10-05 04:46:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf0f8a87-534c-315b-a989-f997aad2f29e | -13.10368 | -47.87062 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdac85bf-2e17-3b30-8ffd-ffcfa819047f | -13.28723 | -47.58157 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b3c867b-2184-3efa-b76a-54627fa8169a | -9.98041 | -48.01785 | 2025-10-05 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8ecbe22-aefa-31fc-b673-131c8945e04b | -13.23466 | -47.8204 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 789966a2-b6b2-3540-98da-e9688f8347d8 | -11.90937 | -46.23544 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f268a86-3faf-325d-8c52-a6e106e3ebec | -13.33075 | -47.78886 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| da2decbf-1a7b-389d-acbc-a6e552843078 | -11.94423 | -43.92418 | 2025-10-05 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f245c5ad-a81d-3cd7-a874-f6a0b5c5acb7 | -11.95907 | -51.47139 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9afac6d1-14d6-30c7-b104-039a14dda901 | -13.3161 | -48.0745 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2fde4f44-ff55-369f-a7e3-32888768af53 | -9.14193 | -50.06321 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a88fea2-67f5-3d96-a561-9cdb72efb093 | -13.08765 | -47.95663 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 456e9eda-4d66-36f7-8e43-54ff1d05cf3c | -9.84317 | -59.47059 | 2025-10-05 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9919ef99-a74b-34c8-92b4-533bc865bffb | -9.41761 | -49.21523 | 2025-10-05 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da6af7af-6dbe-3d5f-9617-7b3f62b3481d | -6.70993 | -42.83082 | 2025-10-05 04:46:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0daf011b-daec-3f9d-adc9-8dbacea4e39a | -11.63952 | -45.05861 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04b201da-16f9-334c-995b-26e4b48f532e | -10.49702 | -51.84284 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3506d06-5472-3b66-98d0-6c89f06ba6bc | -13.15543 | -50.91072 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56221578-d354-3131-9709-469b9afc2942 | -13.52725 | -47.27824 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b02ae1f-6471-317c-95d3-8b9afbd2226e | -13.27729 | -47.59461 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81096adc-c2bd-358b-89d3-c551e8e4616b | -12.58242 | -54.77458 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bdbcac87-9116-3393-be38-83893f295a4c | -11.83792 | -45.04976 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eccd6734-af47-3a79-910b-a0deccbef629 | -13.12993 | -50.87241 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd6dfc46-3578-3415-9f4d-87b58f591a47 | -10.94118 | -47.08709 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf211ce9-ca00-3429-87d5-eda7c98ff969 | -7.52164 | -50.49764 | 2025-10-05 04:46:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e00e06d-11d7-31d6-932b-ec3443cd8146 | -6.71522 | -42.79252 | 2025-10-05 04:46:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 463911da-566e-37cc-bf9b-08d4824e9414 | -10.0032 | -48.29769 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e68936a-3fe4-3687-a9ec-a598a67788a8 | -8.55557 | -47.66905 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2f6a917-0426-3448-9328-75ec6675a96b | -7.75059 | -42.51501 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 303b8955-89ea-3105-95ea-8d77548beab7 | -11.79508 | -45.01469 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cda005be-7a3c-3907-82ce-6ab6e4976e6a | -11.1347 | -47.92305 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5d63310b-91d8-3f93-95a6-eca1ff989f66 | -8.53808 | -46.30975 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52eac3b1-b2fa-3fcc-ae24-8a6892832e60 | -13.35809 | -47.24166 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d4813eb-6a69-39ca-9275-0ae84936f09e | -11.57832 | -46.7716 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c0062187-8467-3795-ae54-a3be72c3d07a | -10.94702 | -47.04424 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e57df89-e332-371c-aa13-1a4d1dea676d | -7.64263 | -45.41066 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11fe4f2c-557a-3f6e-a485-3f877b10c52d | -12.30503 | -55.13728 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6b8a895-2e41-3fff-bd9c-42eea3f18c50 | -8.57676 | -46.32964 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d4b5c922-ed29-3dab-906f-29493672c142 | -13.35775 | -48.06054 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1f188d7b-056a-31ad-a792-f71920a44061 | -8.62595 | -54.98941 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5125853-ab30-3f82-93d5-da1333f52f3f | -11.82254 | -45.09434 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d7b2ce3-c033-39c0-8fc5-c1af85ffb26b | -10.39548 | -45.39838 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca52153a-423c-3ebf-b79d-08c602cd02ce | -13.32821 | -48.10188 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f622f8d-355e-319d-9e78-f2db5ef147ee | -12.2705 | -49.19817 | 2025-10-05 04:46:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48346985-09d1-3d19-8aa3-791e1d12aa0c | -7.55834 | -42.63464 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3763580c-1a71-36ac-8f53-db9263834d5a | -5.88718 | -49.80404 | 2025-10-05 04:46:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e9e930b-801c-316a-b81e-a822af81d70f | -6.61465 | -43.72396 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8345d5c8-7522-3680-9f93-f5f2d2ea8161 | -13.48086 | -47.22466 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6c3ee78-d830-3da3-9a0b-4a790ed604c7 | -9.64396 | -54.31515 | 2025-10-05 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e993d44-4eb0-37f0-9599-d9e7e0450a3a | -12.41237 | -50.27785 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed127481-a0a5-31e1-916f-3b1bed304012 | -13.13221 | -50.8804 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ecf4cd51-ae0a-3238-bf55-45edb12e85d7 | -12.31015 | -55.13309 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd7ecb6b-5f7e-34a9-b419-5ad97ad3d292 | -12.89964 | -47.31477 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c4e4b4d-c1a5-31e0-863f-f165abe7e6a5 | -10.39355 | -45.41235 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92c615d8-4896-37f8-91b6-1a69ce164f97 | -13.08051 | -47.89407 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bf1baba-233c-3262-a937-4178aef0ab82 | -12.31073 | -55.14655 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7891394d-c3f7-3a6a-9927-03d3711758b2 | -8.6149 | -54.96551 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42b1933e-131c-3777-8264-5a9a309aa18b | -11.63768 | -45.07309 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e64085da-f260-39df-b32d-cbfa3201b7bf | -13.33146 | -47.19038 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36d8111a-e633-3288-9e19-2591b9f24db9 | -11.12951 | -47.9108 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac7cc2c7-1439-37d0-88a9-0509c4506c2d | -7.79039 | -44.12735 | 2025-10-05 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4f69104-1765-3d30-bacb-b149786c3ccb | -13.09538 | -47.84283 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed9bc2dd-eba7-3723-977a-7e9968db78b4 | -11.0991 | -47.73951 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 963e8aa2-b816-3d50-86a3-4214183dc722 | -9.30573 | -59.32658 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README100.md)
