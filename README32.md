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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a367500-9b5b-3915-9b7b-7b066788723d | -7.3012 | -39.6453 | 2025-08-10 13:50:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 106.7 |
| e8ec2cd3-907d-3564-9280-77cc6171863e | -10.3487 | -46.6227 | 2025-08-10 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 174.3 |
| f689462b-7e44-3a8d-8e29-7b8fc7e7f87e | -11.6431 | -50.2191 | 2025-08-10 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 13f07ac8-e1bf-3ac3-bd02-2c6ea1a6897b | -14.1103 | -45.4077 | 2025-08-10 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 225.6 |
| c41aa965-7c65-3f17-b4bb-068be827cf1e | -7.6015 | -44.4262 | 2025-08-10 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 16f44ebe-99dc-3f2e-baee-1027ce4111a9 | -7.6015 | -44.4262 | 2025-08-10 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 867808f9-acfb-3fd1-a78f-bb87acb912e3 | -6.9411 | -42.9306 | 2025-08-10 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 188a8d9e-19b2-3967-83b3-034db67ab612 | -14.1108 | -45.3844 | 2025-08-10 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| dfcf0795-2061-3c81-bb7f-0b4cfa6c2b55 | -7.3012 | -39.6453 | 2025-08-10 14:00:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 5a96a978-b4a5-376f-94a0-38fa38b73e00 | -6.9414 | -42.907 | 2025-08-10 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| a97beb08-e55c-3976-a8c0-3cc1b9b0f6cf | -11.6431 | -50.2191 | 2025-08-10 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b0a65682-9578-385e-9aef-788bec348e14 | -14.1103 | -45.4077 | 2025-08-10 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 2b58b988-ae51-3e24-96af-91dec6fee3c9 | -10.4686 | -46.2254 | 2025-08-10 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d36d18f4-8a8a-3c0f-9469-aa8752c23d73 | -8.3102 | -44.9967 | 2025-08-10 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 127e26a8-2228-3df8-a9b8-11de3f07e65f | -14.1108 | -45.3844 | 2025-08-10 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 168.1 |
| c96702be-533a-3515-bf82-b02618f66314 | -6.9411 | -42.9306 | 2025-08-10 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 81c7065a-6323-3d1c-94d3-d88c18d22d3f | -8.3102 | -44.9967 | 2025-08-10 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| c83d0da0-9208-34be-aa0f-a0ce43144ca3 | -8.1116 | -47.4371 | 2025-08-10 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f6c355b8-ec91-3dcb-9cb5-79263d3c12f7 | -10.4686 | -46.2254 | 2025-08-10 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7dd14d9d-e53c-3660-954d-8e1ca8a2b4cc | -7.3012 | -39.6453 | 2025-08-10 14:10:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 780b703e-999a-39cb-8845-3183e3351af9 | -7.6015 | -44.4262 | 2025-08-10 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5ff7ec67-2b08-36e7-b3f4-fbb52eb22a82 | -11.624 | -50.2213 | 2025-08-10 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 17046499-dfd0-3484-ba92-f1c174ff001d | -7.2848 | -44.1569 | 2025-08-10 14:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| c09d0198-0aac-3f32-9bcd-6dcd51ea6ba1 | -7.931 | -46.8125 | 2025-08-10 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 6f140913-8b88-36f6-a1a6-e5732ddc4be2 | -6.7811 | -43.8097 | 2025-08-10 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9bfbe345-1214-3803-9bb4-676005c2a821 | -9.5136 | -45.4112 | 2025-08-10 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 1683c98f-b80e-31ab-abfa-f194b4ac3c8b | -11.6621 | -50.2169 | 2025-08-10 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| c1c3c883-a8b7-39fb-bdc3-da98c9af69d7 | -9.5322 | -45.4318 | 2025-08-10 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 920342d8-3e3e-3377-a125-d40bc2221e3d | -9.5325 | -45.409 | 2025-08-10 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 50b01282-c6b8-3941-9a57-35cafbb5d533 | -14.1103 | -45.4077 | 2025-08-10 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 193.3 |
| d6e581c9-fb04-3040-ad4e-a86ceefbbfd1 | -5.435 | -41.2493 | 2025-08-10 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| e3d96368-3de2-362f-a4ee-9bc73b163344 | -11.6431 | -50.2191 | 2025-08-10 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 2034a7d3-50fb-3d55-927f-675883c076b4 | -7.3711 | -44.8378 | 2025-08-10 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| e9ae8428-212d-3c42-b76f-74b92cb95c0e | -7.6015 | -44.4262 | 2025-08-10 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| fdba2cc0-8bb2-3997-a197-1e3f9c09b23f | -11.624 | -50.2213 | 2025-08-10 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| b1842da9-31ce-38ac-af32-d5149d1bdc68 | -11.2068 | -45.3091 | 2025-08-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b828782b-1b2e-3df9-b251-e3f904ba68bd | -10.3483 | -46.6452 | 2025-08-10 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| d633bc5b-7d71-3a31-a092-9212ea972916 | -8.3102 | -44.9967 | 2025-08-10 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| c66dd3af-9763-3943-8f8d-65ae46334f1f | -7.2848 | -44.1569 | 2025-08-10 14:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8443d204-4eab-3f59-b971-b683aca1c3c5 | -10.9662 | -44.859 | 2025-08-10 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 21b6ab75-c140-3dab-b94e-d0931085219e | -6.7811 | -43.8097 | 2025-08-10 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 92807c7a-0879-3cdf-bd3e-da35d1f33c22 | -14.1103 | -45.4077 | 2025-08-10 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| d417f743-1eb6-3d7c-bf82-3132217809f9 | -11.2064 | -45.3321 | 2025-08-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 5c97109e-49a1-3462-a2b6-29d5d4870e5b | -11.6431 | -50.2191 | 2025-08-10 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 1e472cf1-8546-37d3-920f-90ccf7e982c3 | -6.97 | -43.723 | 2025-08-10 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| fdd78065-85f0-3e09-bf16-a164bed71d98 | -14.1108 | -45.3844 | 2025-08-10 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 171.3 |
| c44a5c50-dab7-3f61-9119-c8777d3ebf52 | -10.4686 | -46.2254 | 2025-08-10 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 03cbd9a6-2218-307c-8bcd-34985f3314dc | -7.3012 | -39.6453 | 2025-08-10 14:20:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 174415e1-e7ce-3569-9643-38d952110ceb | -7.5829 | -44.405 | 2025-08-10 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| a3f63171-4931-30e5-ad15-2653d8399dbe | -11.624 | -50.2213 | 2025-08-10 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 67cc47c5-0938-357a-9cdc-3c1104d451c5 | -6.7811 | -43.8097 | 2025-08-10 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 30e8e74c-0a17-3bfd-9734-311b0d7d6f2c | -12.9876 | -47.5015 | 2025-08-10 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8205811d-ccef-3349-b66e-8e536c3c2187 | -12.5914 | -47.1106 | 2025-08-10 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 9501b410-af2a-3d47-9019-d0587a4e0ad0 | -7.3012 | -39.6453 | 2025-08-10 14:40:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 336dd5f1-7b5f-31e7-966c-0469c27a3d3a | -9.5322 | -45.4318 | 2025-08-10 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e9725d5d-8de7-3a37-a45b-974974db3081 | -11.3736 | -50.464 | 2025-08-10 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e7cc3057-5db3-3336-8847-85fdbddbd994 | -13.5782 | -44.8951 | 2025-08-10 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 88021667-1a6a-3947-a3b9-16521b5cd20b | -11.108 | -50.472 | 2025-08-10 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 1efaf0b5-8475-3019-b163-8c00512a1a60 | -14.1108 | -45.3844 | 2025-08-10 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 65d11f65-acca-391a-9a27-afa619e322e6 | -9.5325 | -45.409 | 2025-08-10 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 09f41864-73d3-35ba-9333-e35dd5bf21e3 | -11.6431 | -50.2191 | 2025-08-10 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 50d6774d-a1fc-364b-85c7-c3872b616276 | -10.4686 | -46.2254 | 2025-08-10 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| d10bcb00-c324-341a-a57a-6ed62ea84397 | -11.2064 | -45.3321 | 2025-08-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| c9bcac39-cfab-3fd8-9277-8a60ffba3dfb | -7.6015 | -44.4262 | 2025-08-10 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 0f99d768-db90-328c-9885-7663c2497b7f | -14.1103 | -45.4077 | 2025-08-10 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| eaed717b-2a9d-3e54-b4f6-f59629d25981 | -9.5136 | -45.4112 | 2025-08-10 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c73ba3c0-15d5-377d-ba70-aed1f1c48aac | -11.2068 | -45.3091 | 2025-08-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 88c19750-839b-32c9-9fe4-3993b34843be | -12.5722 | -47.1134 | 2025-08-10 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |


