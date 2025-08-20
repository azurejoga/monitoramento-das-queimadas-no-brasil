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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e5852b5-ab49-346c-bdf6-e525a4e3ad49 | -12.6629 | -45.81323 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 582e88df-1d8d-34b2-92c9-0b34bc3401ec | -8.63264 | -62.13823 | 2025-08-20 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 087acb99-5cec-3965-a1bd-f2781523b8e5 | -13.03426 | -46.7899 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf1f8810-1172-3a5d-ab35-c2322469879f | -9.17982 | -59.59775 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e77ef46-08da-3f5e-b6d6-725231d0e4ef | -7.05319 | -59.23359 | 2025-08-20 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfd41f66-c47b-313a-af14-2d1ca2195c40 | -12.66192 | -55.79356 | 2025-08-20 04:57:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73fa70c6-3ec2-3f0b-8c1c-f6be42367357 | -8.65416 | -54.71755 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef50108e-cf84-3899-9c90-506ef2649843 | -9.16756 | -59.61838 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bf3fe2e-86b8-3a85-84ce-5ac1d6a13fd6 | -13.87258 | -45.56241 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3b3bff6-46eb-3925-8f55-5b5d53f3e333 | -11.73669 | -48.18862 | 2025-08-20 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 928e3e50-7712-39ba-aca0-870a5cc68594 | -7.65515 | -45.25616 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13796c0d-12c6-3b47-8def-68dfd57133ba | -10.91428 | -57.51229 | 2025-08-20 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa5fde3a-473d-35f8-b377-c7a923dcdd53 | -7.59225 | -44.38884 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 24675b0b-b7a8-3a96-ab1a-be9928dab9a3 | -7.585 | -44.39976 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8ef07e9b-1065-35e0-b27f-0685e865fb53 | -9.17589 | -59.59707 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c909b5a-8aa8-3517-b0e0-3d109cba949b | -14.15217 | -45.28561 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f421ceb-ac8e-38f6-8043-d6cc4f634161 | -11.31706 | -55.2121 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05095b47-a16b-3444-948e-7ebebeebd9eb | -11.75075 | -48.19056 | 2025-08-20 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 09342d80-e650-3f80-9745-f8e09743a95a | -7.66006 | -45.26045 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3f8826a-24b0-38ab-ba19-a4e8c241df16 | -13.57559 | -47.03125 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f09d4def-fa1d-3f59-8ed7-41bde38b7300 | -8.30205 | -46.3567 | 2025-08-20 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 504df160-f219-353f-83ac-3d98e35086c6 | -7.5836 | -44.3968 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b2c82be-016a-3bcf-a02f-b773efba9d2a | -8.30708 | -46.3576 | 2025-08-20 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 742f8561-c295-3bc3-93aa-e6d740a8c6b9 | -11.12781 | -46.9976 | 2025-08-20 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edb48c66-ab1a-3945-95e5-83c0627d20bf | -13.14227 | -54.93452 | 2025-08-20 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ea14e21a-fc8b-3170-9617-2321ab751624 | -9.20689 | -59.62506 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f2f0a79-2d3c-3c90-b2a3-eee8ea557201 | -8.82338 | -52.03545 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720da6f1-d517-320c-9c81-1f67c7677b82 | -9.23696 | -59.61479 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f175d4b2-a47f-38ff-a66b-16bad57d48b1 | -12.87322 | -46.06551 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f05a9409-a091-3eb0-b914-73a537d26ef9 | -13.57038 | -47.03066 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffb5bbc3-34ec-31a4-abca-985e6f5e75df | -9.53114 | -45.1777 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31814cc8-6e73-3b51-ad4e-07528b310f6d | -12.51846 | -45.60506 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff6f8d91-dc0e-37c2-9480-4384b4fc57d8 | -6.73947 | -50.95982 | 2025-08-20 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a571ebcb-8b11-3a5c-a10a-c01e98cd75e8 | -7.60322 | -44.39381 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8500354b-2f25-33f2-9c08-f7ad5a5b7c46 | -8.80552 | -45.43929 | 2025-08-20 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0084e60-2135-385c-9974-3dceb450f31d | -9.18679 | -59.60083 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe22e2e2-31f7-3cd3-9b65-7ea4f95577cc | -11.97407 | -46.77844 | 2025-08-20 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3af62955-54ea-3181-82d1-5cf8d4be3e00 | -9.14709 | -44.39038 | 2025-08-20 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fdc835e-2541-33e9-b24b-de0cc603c825 | -7.55478 | -63.85174 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb9884c8-e2ef-3a53-9896-415e0246e5f7 | -13.5752 | -47.03452 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 809499f5-231e-373c-8e33-3a31a699ba7f | -13.59237 | -47.55765 | 2025-08-20 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99582d9b-9306-33a3-b47c-5d55d6915cf5 | -13.59271 | -47.55485 | 2025-08-20 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2badc931-179a-38da-ac0c-1b115ef5c40f | -8.7949 | -45.47704 | 2025-08-20 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b66efef6-0c8f-3ef0-a1ec-2bf3d594a321 | -12.52085 | -45.60651 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d390453f-6131-37ea-a1a1-46664b98ee40 | -12.63287 | -46.88583 | 2025-08-20 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecde23ec-7f08-3f0d-bf96-8729572ec98c | -12.98996 | -45.19289 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd017045-f737-39ed-94d3-78622f5b4e0c | -12.66469 | -44.95351 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8df77737-6b2b-31c0-afcb-7073077710b7 | -9.8073 | -46.88552 | 2025-08-20 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33b1f539-cc7f-369e-bb3d-4062160944f5 | -9.18375 | -59.59507 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2436abe1-46dd-312e-a8f7-1f463a441d38 | -7.57788 | -45.42101 | 2025-08-20 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eeb62b34-8e3b-3b29-b8e1-c6f21635e8d5 | -8.82746 | -52.05641 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3244998c-2077-34e6-8fa5-dc742e5d5026 | -8.8977 | -50.8627 | 2025-08-20 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c12c8894-6579-3567-ae91-d9e59746be04 | -14.15709 | -45.28539 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 096f7c51-faac-3446-bd0d-2a34ea21f498 | -10.69635 | -48.22036 | 2025-08-20 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b88922a-ffeb-3cce-94cd-d8b843cdcb78 | -9.18151 | -59.58762 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b48cf3a-679e-3c6d-bb7d-c1aaa013e37a | -13.17873 | -46.87344 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c3d2628-f144-3bad-bced-63b76486b388 | -13.18979 | -46.86993 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f69d4577-a821-3e2f-ba6a-8db1354145e8 | -12.89797 | -46.09084 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3f08011-22d4-3511-8665-c9f5ba509c13 | -8.82331 | -52.05993 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccd3cac1-d2a4-3212-b755-0f2c82d722c2 | -13.5812 | -47.0286 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6282504a-7c25-3c78-a7ea-6e53ea3063dd | -7.58307 | -44.40063 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 563bfbb9-d277-31f4-aff3-0d8e6019c4f4 | -6.26037 | -52.82159 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f9e5118-5e0e-3970-84b9-705c87276f74 | -13.57716 | -47.0183 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f05b0b3e-e12f-3287-9b44-091714af57ad | -7.60271 | -44.39766 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1afe2862-e6b4-3a8c-9383-09855a2f4be7 | -14.15122 | -45.28461 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7ff6df6-013b-3d4e-97af-ec03f7fae9e6 | -7.84414 | -45.1135 | 2025-08-20 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b322f174-a00d-3f71-be86-e685b545efed | -13.41055 | -46.35632 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff8732e5-597e-322e-9132-982e946e8f3a | -6.69648 | -52.09614 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed8e1769-490c-3fa4-a996-e499004d7468 | -8.63541 | -67.2663 | 2025-08-20 04:57:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53453343-136a-3f8c-a0db-beeae8968f3b | -7.81568 | -46.88725 | 2025-08-20 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7692379b-7efa-31b1-927f-9ee41ed58a9d | -8.96556 | -60.4938 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40951257-b75b-3cf1-bbef-c83c38757258 | -10.81771 | -43.27914 | 2025-08-20 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a94a27db-c1d1-358e-816d-4ed26de0d314 | -6.18966 | -53.52047 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e998b0f5-fae1-3b44-afe6-51200276b8ec | -10.82004 | -43.27676 | 2025-08-20 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 42eb82df-d90b-343f-b304-469b39c70fc5 | -9.25113 | -44.4997 | 2025-08-20 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5ffc339-97e6-3f25-bbd6-406ea0584dfd | -7.64546 | -45.28642 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e73f52d-0e51-369c-9927-5c7bac286942 | -6.22207 | -55.63754 | 2025-08-20 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 236381fb-9a26-359f-8bf8-05bb9ef1fd40 | -7.64978 | -45.25523 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48fa2938-84cd-3960-a528-fb3c09a44b8f | -11.32037 | -55.21264 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7eee183-83e9-3900-ad87-12ed00170975 | -9.07496 | -60.41422 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 399eadde-7049-3e1d-a3c3-765e492706ee | -12.93999 | -46.16212 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14b4f7b5-6dbe-393f-b7d8-a523da5785a8 | -5.97921 | -61.35952 | 2025-08-20 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bb519047-ced7-3d45-bc43-2956df8a74ee | -9.15848 | -59.60451 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3eb48565-c67e-3abd-b433-565fde6c597f | -9.18767 | -59.59574 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1ae05b3-a3a8-3506-8ccb-081f24c88603 | -6.46627 | -53.38093 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e8ce28c-fe53-3fe0-a3d1-521e6cecb39e | -7.54678 | -63.85031 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cb8fa92-8bef-3800-936a-f30864782b76 | -7.63813 | -45.25996 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74bafdcf-2e0d-31b0-947b-d4fb8d5e79c7 | -12.95033 | -46.16828 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baa3d71e-c378-3d74-b6b1-603e5fde0e83 | -9.16774 | -59.62175 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2383815-5d3f-3f7c-939d-0ae3a4b48463 | -7.59041 | -44.38971 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2b0cee99-f390-3067-9af2-ebd7d560ad34 | -13.02733 | -46.80246 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae318056-3c84-30ce-a025-dff593a963d5 | -9.89144 | -60.28456 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d611769-eaf5-32e8-aba2-f5f0203993a2 | -14.15804 | -45.28639 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fd08e29-3a33-3c62-a3ad-6a7a00d8fd37 | -7.2748 | -50.18562 | 2025-08-20 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 42268e63-f2ca-387c-a1ea-9c1da72f4ad1 | -12.81238 | -48.56187 | 2025-08-20 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b6fa64d-2c6f-3fc5-8bf1-a7c86ac60746 | -10.27524 | -46.77429 | 2025-08-20 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a588b61-b1a7-3da9-aa42-a46a8a682f5b | -8.3018 | -47.6193 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9bdf4dee-076c-39e5-9386-6704366aefa9 | -12.08954 | -47.91402 | 2025-08-20 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5a37373-e091-388c-849f-00372e475266 | -8.68426 | -62.10399 | 2025-08-20 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d0a5f08b-f33d-35ac-816c-c15e061a8512 | -13.19544 | -50.74331 | 2025-08-20 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README49.md)
