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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6f7ff3b-3037-323e-a334-d4d97741984c | -2.884 | -54.13707 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 32fc2002-5801-3ecf-8f3f-8a504830c25d | 3.49211 | -51.45342 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f1c6e41f-c743-3c3f-942d-12e9433dda66 | -2.89902 | -54.1242 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8443985f-286b-3db5-90e3-e35ee11e918b | -2.9415 | -54.13542 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 67b7ced6-2d98-337c-8e95-e5d195bf2418 | -1.35763 | -55.98412 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| c56642c9-f01e-3f0a-aa73-beb2a1633489 | 1.82782 | -55.54295 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7be8e9d5-8ed9-3c34-8ba3-6b2d3a1dc268 | 1.76479 | -55.60344 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5f76c8ff-6888-3f8a-91f1-84a1193653f4 | -2.88506 | -54.14398 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a1be140c-9bc3-3340-8734-c8b72d276bfb | -2.9867 | -54.10292 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3ef4b4f-7d9b-3031-86b5-8c47e370c5b2 | 0.31156 | -50.99941 | 2026-10-05 17:17:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 201db5fc-e968-34a7-8614-cf4e2a468ed7 | -3.69647 | -58.88883 | 2026-10-05 17:17:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 6d1f9886-a5d0-33a8-bef0-20cf781f8f52 | -1.516 | -55.80692 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76a74ef7-d08c-363c-8815-ebaef3b54ada | -1.77706 | -53.77508 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5d8ee17d-b6e8-393d-91d4-917abfab5c1e | -2.05126 | -56.8648 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2f37cce5-ae5f-3c03-b29c-434b46e3943b | 3.31466 | -51.33217 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ba94b98-a731-3bc8-863b-6a40e2ac3010 | 0.9247 | -60.40546 | 2026-10-05 17:17:00 | NPP-375 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e88d29fb-b56b-3848-89d1-7065b45fdcc2 | 1.98273 | -60.61929 | 2026-10-05 17:17:00 | NPP-375 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d3837fba-0b0d-3e69-a1f8-1aad30aa7f41 | 0.30167 | -51.08859 | 2026-10-05 17:17:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a358f9de-e302-3786-99d9-ad161bcf7676 | -1.63683 | -55.5303 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c78bce26-7e02-38ad-9680-a157ddabbd14 | -3.69012 | -60.9475 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fef0f948-23bc-397b-be49-9c7c0f1fc8b1 | -3.3834 | -59.4327 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0910604a-e987-38d7-b69f-66642723325f | -2.53985 | -58.03361 | 2026-10-05 17:17:00 | NPP-375 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ca9a8fa7-f08b-3d7c-8afc-6bba25b64fd9 | 1.84463 | -55.80968 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| daa26f80-02af-395d-9d07-854e98337fd3 | -3.3275 | -59.47785 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6e1a00a0-6769-3fae-ae3b-971a61f65b29 | -2.54463 | -65.8758 | 2026-10-05 17:17:00 | NPP-375 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| bba3b69f-29b4-3780-84d3-9afe3275a13d | -1.22763 | -54.12154 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8bb03eb9-0034-3e5a-8ef0-1963c36e8adb | -1.63079 | -56.00753 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cdf200a6-31f1-3ff1-aee7-96494d0763a5 | 2.09594 | -50.72956 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 18e78404-c2ad-33c5-9279-8793454b7dbb | -1.4884 | -55.6708 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7c3d7631-d701-3907-bf88-2233882c64e7 | -1.38088 | -55.18887 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d9095bff-457e-3958-9ef8-627a5d6d0aec | -0.38522 | -52.08106 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7d86d2af-3b31-3175-8685-d29d5374ccea | -2.45896 | -54.80815 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 208674c8-4091-3bb5-8d1e-129606094d29 | 1.79364 | -55.548 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d5a9357-305b-33c9-bb5b-9390e1a2970d | -3.77265 | -61.18786 | 2026-10-05 17:17:00 | NPP-375 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 453c1e77-7d50-3753-a725-d69583be6523 | -2.0412 | -54.3089 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 217c6318-75d1-330e-8840-b8ea14a6e721 | -1.42743 | -52.72965 | 2026-10-05 17:17:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b060a3bb-e9bf-3ff9-8d93-7216d4fb859a | 3.42302 | -51.51764 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5719d77e-e569-30b1-94c4-0abb92e17e24 | -3.75116 | -61.01366 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 2a30b10d-ca88-3ec2-936f-6e713be646c9 | -1.33497 | -55.92591 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8337bf80-0fdc-3878-a487-e760564120d1 | -1.9302 | -56.75913 | 2026-10-05 17:17:00 | NPP-375 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 598715e0-4156-37c3-a0d1-04d1beb4be48 | -2.80568 | -54.08966 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fc4479f3-97af-3059-b3e9-e6a1f8f474ac | -1.63225 | -55.12886 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 44d2e346-c5e2-3d05-a248-c3437665fece | -2.88166 | -54.07743 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f82cee20-98af-36e7-a610-9de25cf4aa2b | -1.47125 | -53.61721 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48fdc76a-0554-3678-ba9e-623f9ec59b93 | -2.89796 | -54.11729 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 652d0f13-c894-3190-8b46-aca31403188d | -1.40856 | -50.72261 | 2026-10-05 17:17:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a60ebdd-21eb-3741-8fe0-26cb43937390 | -3.58061 | -60.53805 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c8ceaf08-c78e-3d8b-b7d4-fc65e580dcc3 | -1.12874 | -53.09705 | 2026-10-05 17:17:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0bac49a1-3de1-3e86-a09f-e52303af2fed | -1.88846 | -57.06987 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6e874aad-1cf5-306f-8da2-c3efb24d934d | 3.52044 | -51.50216 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 423d45ce-02c1-3b26-9c09-3ec22f6aaac2 | -3.67568 | -60.5427 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| facb0ce8-9c80-3412-b322-de11854a9c42 | -2.99792 | -58.43566 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d199be9d-a309-3edc-980e-c226e7c74f0d | -0.23331 | -49.39372 | 2026-10-05 17:17:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 40faf37f-c07a-3c3a-9074-a570bee9d711 | 1.30012 | -51.13003 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4f0d403c-a9db-3cc3-9dc6-e6e976bac708 | -2.7807 | -54.10397 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 6d9317be-bc8d-3dd0-b87b-1652fc454033 | -1.62148 | -55.0139 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 997b5145-a744-3a00-898d-7d847f2441cf | -2.78455 | -54.10692 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 978596a1-4f93-37e7-8b57-14a6491dee5c | -2.91615 | -54.12513 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b83a8f87-677d-347d-afc5-26a0aa1359ca | -1.52268 | -54.80757 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a79ad0f3-a72b-3283-952f-9b94a1680b8d | -2.77612 | -57.65206 | 2026-10-05 17:17:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 03f07d83-6d43-32d9-855e-cd0c9c770e5d | -2.22925 | -51.88476 | 2026-10-05 17:17:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b97f66d1-c87b-349b-b675-a8924cfd3d23 | 3.52149 | -51.52547 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2f3b37b8-0b3c-32d3-a8b4-e99b80cfb4fa | -2.34581 | -57.11816 | 2026-10-05 17:17:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51f210d3-cc26-3768-9e17-422307dcc40b | 1.57659 | -55.9908 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 174f300a-7f2c-3632-97e3-4c61e45ba87c | -2.88045 | -54.09175 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e16cb094-a0fb-3252-b595-cccbd077a944 | 3.36087 | -51.34216 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f1a8da36-323b-3932-9421-20c08622a81f | -2.04067 | -54.30544 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 7098cbe2-7ee1-388b-b401-499b8f5a50a2 | -2.97712 | -57.90374 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 937898a2-914e-31b2-9784-3e58bb9dc206 | -2.18915 | -56.841 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 604a06e6-8d14-3b9c-9b54-cfc90808e4ea | 1.45545 | -55.65649 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5d284570-946b-3f36-b38c-7e924d7688ea | -3.17785 | -60.06807 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| df8ec655-7e11-346c-9894-b22930d8bd58 | -2.92943 | -54.12312 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 271e14ba-3b68-318f-aa85-0073198c8a01 | -1.96221 | -55.38637 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0b70cd7c-ac25-3fa8-8df9-79a1db0c7e41 | -1.85261 | -50.62947 | 2026-10-05 17:17:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dc9cfc20-bbb2-3fd9-a00a-40fb10e173c9 | -0.99673 | -48.95627 | 2026-10-05 17:17:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 4828df92-9f3f-39c6-91b5-e4cd7cbb1fa3 | -1.74329 | -55.23528 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 08024294-e647-30c5-b3b1-b848c2a7acab | -2.37378 | -56.12513 | 2026-10-05 17:17:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b6710856-19c1-3b37-8f7a-dcfe6b880c35 | -3.28573 | -59.41498 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 18ff4dfe-b9c6-32cd-a781-6a49dc8fe77e | 1.86754 | -55.77082 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5881ce78-abef-38a2-bf9f-b551ec8d04ce | -3.0467 | -57.52056 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e373bbce-b501-33f4-86d3-9476aa38e36a | 2.14596 | -55.96349 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1ecd89ad-2a63-3619-b1cf-8fbe5d3d1024 | -1.87829 | -50.04255 | 2026-10-05 17:17:00 | NPP-375 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e2331520-5180-3f95-b0b7-5df420f81068 | 3.35305 | -51.34101 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c738d516-0df6-3db2-a45b-a11fe8e7a743 | -0.73563 | -57.97546 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8c21caf9-c9f0-3fdf-b339-ddf7ec393586 | -2.77843 | -54.11138 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 89368503-3f3d-33f6-83e3-1564d20f4b14 | 1.17398 | -50.77161 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7a617c4f-a1f4-31b1-a3d0-c4c1d951a85c | -1.66925 | -55.05966 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 379e34e6-e42d-33d4-8e00-cc3fc789b02a | -2.00172 | -55.62395 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d162b3a2-d80a-356c-82c5-2f29c900e03f | -4.27571 | -63.66288 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a69c18c5-2cd9-3f68-a8d8-382500947b87 | -1.28394 | -55.41404 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 949325b1-825b-3d10-8fa7-57dce4e9d54f | -1.85188 | -50.62487 | 2026-10-05 17:17:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 85090688-2b82-3255-9d20-e3a23ca8c06c | -1.61353 | -55.11754 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 5a61ca51-1f63-3e8f-a395-f7e65b15f898 | -2.90264 | -54.08132 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4f171edf-b448-355d-a67b-e26f2a530eea | -2.93275 | -54.12262 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 16d872a6-b0b1-37f7-ab52-ce54aad34c29 | -2.06288 | -56.87092 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a18c9269-7cfc-352f-ad98-3fbd261c2204 | -3.68212 | -58.90124 | 2026-10-05 17:17:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 1926b39b-cc82-3c91-b8f7-527d3238b651 | -1.18574 | -49.25576 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ec9ebb9c-3c21-3868-ba14-5dedc51739bb | 1.72485 | -50.98447 | 2026-10-05 17:17:00 | NPP-375 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2445d80d-6182-3dff-9816-fa02dff0882e | -1.37664 | -55.99579 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3c49ee82-20f5-39d0-844b-d6353804cc98 | -2.55311 | -65.86337 | 2026-10-05 17:17:00 | NPP-375 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |


[Clique aqui para ver as próximas entradas](README125.md)
