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

## Dados Diários - Página 231

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a63f604-587c-3e9c-8302-6bbc5d7f6737 | -2.77632 | -54.08799 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 680737cb-c302-3ccd-8475-dff0672b364a | -2.94782 | -54.18984 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 88ad79c5-18ef-35ea-b2a3-2f9db92b7b9c | -0.28658 | -48.62986 | 2026-10-07 16:39:00 | NPP-375 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41ca6420-8d0f-3daa-a2c8-f98428ddf0a4 | -3.04169 | -53.941 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ff1b87b-2c33-3dcb-8f66-70eee707edb8 | -1.12868 | -54.1192 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e3477e2-5487-3dbe-af35-63c34e0dde74 | -2.49507 | -56.11732 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2cb7b676-94dc-3dfd-ba75-4eedd8b22992 | -2.7403 | -41.82825 | 2026-10-07 16:39:00 | NPP-375 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2cc412b-53a7-3cef-a08a-a2c640f04e3f | -3.07568 | -54.25244 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 379a9960-edf2-3c98-8175-3799564bf048 | 1.76168 | -55.58509 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8281229c-6435-37ab-8a74-9ccd4a47f4e4 | -1.41944 | -55.42842 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| c22011ec-46f2-39bc-90e6-d247394432fa | -3.11354 | -54.16749 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 7d80b090-705d-3d87-ae20-57120b3922a3 | -3.07996 | -54.28056 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 9150c562-fb16-3e71-899c-4d273ecc1650 | -3.85385 | -55.97839 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a929c315-43dc-3d9f-9cc5-6481e9a267a1 | -3.18102 | -50.55846 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 64781909-08e8-3c53-8b93-64d88370b2d8 | -3.24329 | -56.80537 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 97749f20-1d3e-3e00-9731-c133b716dd94 | -2.94361 | -54.16208 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| ec1b2975-a615-321c-ba5c-fd9f96aa9caa | -3.65482 | -50.95119 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 09b6867c-6d47-3254-8048-50ed299cebe9 | -2.45576 | -46.02812 | 2026-10-07 16:39:00 | NPP-375 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 254b5697-53fd-3f52-90df-22efb618daed | -2.99827 | -54.18217 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b13caff1-8914-3304-b81c-23b3c000a095 | -2.83797 | -54.13126 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| af618732-60a5-3add-9c0d-494600c18838 | -3.30467 | -44.70414 | 2026-10-07 16:39:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bc1fad2-9bfd-37f1-8528-c55b7131a339 | -3.10192 | -53.76073 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 9bb587f4-7f9f-3769-b136-a6feadf04069 | -1.46991 | -54.52702 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 1ecd3a11-165e-3501-ae63-4b5e0bcbccd3 | -3.84215 | -55.98506 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 08e644cb-d7c2-3e71-a614-13e8f5a23ca8 | 1.4774 | -50.76892 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 04d5cec7-57c1-3698-b783-f387364e8757 | -3.05 | -53.88578 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 173f8539-755a-33b9-b1d8-b4294f27c992 | -3.04417 | -53.88315 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7e892153-fd1d-3a8d-bf95-405e4072ad43 | -3.27666 | -54.05154 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4c24f255-528c-3f3e-b87d-4c6455b2874a | -4.92927 | -55.86948 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 518455e0-ae04-3f22-aab6-15834f0b38ad | -2.89235 | -54.07853 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 57fbdd36-6952-32a3-925e-3909a9e6ffd7 | -2.49341 | -56.10233 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 63f82c87-8e55-3e53-833a-1e00b5027d94 | -2.94377 | -54.15074 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| a4e72c84-5bfc-3170-bb72-f98adc46bdc7 | -4.43232 | -55.66103 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1d4209c5-da2d-320d-99de-76ee7ba2026a | -0.8943 | -46.86009 | 2026-10-07 16:39:00 | NPP-375 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 42d0364e-b895-3b85-ab95-15ad37058956 | -2.97084 | -56.62036 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 55ff97b8-cca9-3815-8221-5dad3f469e27 | -2.88079 | -43.0154 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5686bc3-3dd7-387e-8abe-a5174442380c | 1.75521 | -55.59475 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c3dfe1a1-78f1-3a7d-9414-c136f7a0efb5 | -2.79416 | -57.65681 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 605b5ca2-0bcb-33c7-83a5-a3e547aee4af | -0.59102 | -49.41734 | 2026-10-07 16:39:00 | NPP-375 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 047d5622-e6c8-349f-9e01-15fe2ac4c6fb | -3.59024 | -54.31531 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dfb8ad11-ee06-3da8-9d60-f6dbc3ba8e80 | -3.02674 | -54.14961 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a603e58-818d-3de0-83a7-64095fc6d9b0 | -2.92911 | -54.13953 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfcb9d59-19f6-3945-af1f-a3527129ebb2 | -3.57762 | -54.65917 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| dac9ebc9-21b6-3bbb-a408-54a78a6a5408 | -3.42569 | -50.43606 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| f4733065-c3e7-3786-96c1-ade85a3587d0 | -2.11902 | -54.69264 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7bca220f-f13f-360d-b9c0-1310625b2cfe | -2.62611 | -54.74477 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8bb75842-57fc-3bc6-b67a-2e46a0611a0f | -2.75067 | -42.76729 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5600e4cc-1e9f-3be3-b50c-aef46664b274 | -1.5522 | -48.1831 | 2026-10-07 16:39:00 | NPP-375 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 38f7a5d3-78a8-3008-bd42-46e3628161fb | -2.13971 | -54.45885 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e7846d1b-e354-3fe8-8e5b-32db7c4e669e | -4.11419 | -54.02124 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| de7d1f74-6354-34cb-8fd8-ff0777c344a0 | -3.03878 | -57.49057 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 20cad87d-44bc-36f5-a50a-0c7c7039ad4f | -3.53934 | -58.42304 | 2026-10-07 16:39:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 76ab7fac-0304-3312-a96c-2746683e38d2 | -3.46795 | -54.59426 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5aa65197-5222-3415-a6b7-af079d0e11da | -1.21535 | -49.03778 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dec47c89-4601-3aa9-98d0-9bc0684570cb | -0.83999 | -48.59365 | 2026-10-07 16:39:00 | NPP-375 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f1454a5-a814-3cf8-a557-1563050a2eea | -3.08668 | -57.63022 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2674aeeb-cac5-31a0-b213-09c703ed0c74 | -3.04121 | -53.93766 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 86863d77-2d2b-3b7c-8c57-51b4722f0a40 | -3.27027 | -54.04555 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3258cb61-e4ce-39fb-a5a0-2da6c7533e38 | -2.91712 | -57.6312 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0d4f4cf7-e05f-3e32-95a0-999d99d2d681 | -2.36432 | -56.90277 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c43194ab-9436-3813-afec-d2107a3d9f7f | -3.50494 | -54.65048 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 510e2ed8-e3e2-3ffe-9807-8950b95060d9 | -3.98489 | -56.22494 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| df07e0b6-1002-3796-bda1-5dbdf65e36b1 | -3.24975 | -56.80444 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| a366ab92-96a2-391f-b42a-546e354e1a6c | -2.89865 | -54.15796 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0787342f-388f-37d5-8af8-11476cae79d9 | -3.84834 | -55.9841 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 681513ec-95ab-316f-a913-f1d6e12eb470 | -3.10231 | -54.96835 | 2026-10-07 16:39:00 | NPP-375 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 520fe27d-1096-339c-8abf-576f9099d3b8 | -2.58036 | -56.14406 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fc6b21c5-47e1-32a3-a482-7ef5e4c909ba | -4.17591 | -56.34907 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 765e8880-47e4-3a76-8d73-03f6ab1c8114 | -2.91236 | -57.39748 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0e109c7f-31c2-3883-a0a2-5de5854d1c7d | -3.07614 | -54.2548 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b3e1bdf5-3603-3160-83ff-28506957203a | -2.99201 | -42.97116 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 601efc7f-a2ce-33ca-a75d-8cd4bc372307 | -3.02911 | -53.89196 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a1fc2c1a-d300-3df6-83be-55ae0442840c | 2.55413 | -51.10171 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 87144e0d-20be-39a0-8234-ceacdd2a1335 | -2.58838 | -49.62462 | 2026-10-07 16:39:00 | NPP-375 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| eb23ee35-67bc-3cbc-9226-fcec54fa4c55 | -3.28358 | -54.06108 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ad65e79-1aa2-3353-817b-2b9353c43fa7 | -3.29384 | -54.01786 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9b5b0a67-6ed0-3b8b-a57c-692528024f99 | -2.30518 | -57.08402 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cc7e16f2-df0c-3a7f-bdbc-598ada3ee4c2 | -3.50539 | -51.68777 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 9ac32254-55d6-3bc1-b998-bd0e30cb8bb7 | -3.05433 | -53.91532 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e32c811a-5d3d-336e-bc33-6b713cd91c84 | -4.60929 | -55.72146 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 963d5a8a-da51-3133-a655-7f53cfa3f30e | -2.95125 | -54.20263 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f7f0dea-f94c-32f1-be92-e2c4e0c092b3 | -3.24409 | -56.81064 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| c99f3a88-85f2-34ff-be17-db70a90323b6 | -1.41884 | -55.42438 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 66819957-da08-343c-a8ab-cab712cf2875 | -2.79787 | -54.08488 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 5e341a62-524c-3e27-98bd-91b08e35b5f3 | -3.29584 | -54.03148 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c25b27eb-ce01-3b4b-ac07-64a25af79554 | -1.27594 | -55.855 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 6b2be9ba-de39-3e7d-9900-2e2fe72683ca | -3.76073 | -51.33368 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 71454073-3651-3240-bdc5-8239e8f4fdab | -3.06995 | -44.45158 | 2026-10-07 16:39:00 | NPP-375 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 36adf173-32e2-3b32-a5c9-bb8698d20c27 | -3.8643 | -55.9993 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f28cb23c-2294-3c99-8d64-89be9f8dbc3b | -3.06409 | -54.20991 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5b338598-dfa8-33de-9894-63c7e1b5d184 | -2.4794 | -56.09554 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 07dc48e4-1402-3a20-a820-b7949273f262 | -3.08072 | -54.28649 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 852b19c1-d104-3ee0-93a3-db2dbd69e2ac | 1.95421 | -55.13212 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 881b3be3-6e7f-37fe-9032-99eafe9b8dde | -3.15545 | -50.44289 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 94b93f1e-08c6-34c9-9c7e-3c1e503e9660 | 1.65165 | -55.81151 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0c1342ba-dd50-39c9-a3f4-1c3bccfcf064 | -3.09455 | -53.71218 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9bcaf08d-670f-3678-9518-9bfe47d1326b | -4.92231 | -55.86515 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4c9257a6-36e2-3da2-9ab7-8f40f478c4f1 | -3.0922 | -54.28841 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ddf6b03-24e9-3d80-a701-ca093f938d75 | -2.78989 | -51.6795 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| dfc4f871-9d8f-3fd2-8d32-0fdd69bb9237 | -3.07563 | -54.25128 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README232.md)
