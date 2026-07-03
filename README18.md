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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8632a85e-5e4d-3f85-95a3-4a7ecf50b383 | -3.51461 | -48.03942 | 2026-07-03 05:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09ea29f4-2476-3bed-80c3-a88c2cedc092 | -4.00696 | -48.06004 | 2026-07-03 05:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f12caa2-3050-3fe1-b017-444ee6f5a6d0 | -3.5105 | -48.04269 | 2026-07-03 05:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc9f9b64-f6d2-3aaf-abc7-e16b2ef68e8a | -4.01222 | -48.0596 | 2026-07-03 05:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8c97b051-b639-3fd4-b306-0eb4784b5342 | -4.01305 | -48.06869 | 2026-07-03 05:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9a00fa2b-b5fa-3960-bed6-36fa948fc616 | 2.61832 | -63.10759 | 2026-07-03 05:38:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e9377a3-3089-3292-bff8-3ca81a5c6226 | -4.01401 | -48.0619 | 2026-07-03 05:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3c54034f-8bfd-3457-ab1b-f3557e548123 | -1.78212 | -55.52742 | 2026-07-03 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2eb0de90-0b7a-33dc-9ccb-189b6093b2b2 | -1.78638 | -55.52806 | 2026-07-03 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5c5fb16-317f-326b-ab81-ac918ef34e3a | -4.00603 | -48.06662 | 2026-07-03 05:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ec4f4e0-14a5-3f48-9842-aaaaf07538f8 | -3.51143 | -48.03654 | 2026-07-03 05:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e760a61-6644-3bb1-b5dd-c8a2a4e9ffd8 | -2.51499 | -57.73876 | 2026-07-03 05:38:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07b681a3-03ed-35ee-a39a-731730edd706 | -4.00422 | -48.06429 | 2026-07-03 05:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 214f7286-6716-30c9-9a6d-2afc288eb756 | -4.01122 | -48.06635 | 2026-07-03 05:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b7917340-773c-37ec-abe3-e0f637a03f0b | -10.9401 | -43.0355 | 2026-07-03 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 3fe78dc9-cf61-3bb9-8b27-ac67378f11df | -10.9397 | -43.0593 | 2026-07-03 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| fda8cdeb-8635-3b0d-9a76-27812053e050 | -12.7553 | -44.5194 | 2026-07-03 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| a8393e2b-fee8-3e54-93d7-0cb42e40ca9a | -10.9588 | -43.0565 | 2026-07-03 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 976efb48-1433-37e8-add3-5d7cb7f607da | -5.7945 | -45.0586 | 2026-07-03 05:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 741c8bf7-5822-3894-9b34-b60075d9750a | -12.7557 | -44.4959 | 2026-07-03 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 186864ca-7253-3121-8282-d904aa441cfb | -10.12932 | -52.10308 | 2026-07-03 05:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15dfefab-77d9-3251-9a5a-37193f1d2a26 | -10.12988 | -52.09852 | 2026-07-03 05:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 738f5b87-eead-314b-8ce1-c62c77c6a5a3 | -8.70072 | -54.58335 | 2026-07-03 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12c00403-07ca-3e00-a526-4ad176e9e657 | -10.7876 | -54.10576 | 2026-07-03 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e19d39f-2df4-3253-965d-c663575b38ae | -9.26159 | -57.87019 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f8eb249-8da4-3e91-8cd1-ea45bd63fbbb | -9.36496 | -65.74242 | 2026-07-03 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23dde9de-3e32-386d-9642-ab53aa7da49e | -8.70576 | -54.58409 | 2026-07-03 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0ffe54e-74fa-30c0-bedf-de54f786f751 | -10.30214 | -57.12779 | 2026-07-03 05:40:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c2d9821-e4e2-3107-af5b-07542cf7aca3 | -8.69608 | -54.57969 | 2026-07-03 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 63577a00-f09f-334d-b3c6-6b2a59b1b242 | -7.64371 | -50.03116 | 2026-07-03 05:40:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2da9bd0-9ce9-359c-bf42-50c936866bf3 | -9.1908 | -58.04847 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98607145-38e3-33a8-b856-c8b19a96a544 | -9.1903 | -58.05202 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86898351-aad5-3014-a6eb-d28caa6be938 | -8.69648 | -54.57681 | 2026-07-03 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b295f242-a233-35de-b57a-dcb39a8963cd | -10.12381 | -52.09765 | 2026-07-03 05:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 453c926e-1a5d-3af9-93fd-b47960280e3a | -9.18831 | -58.06612 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 850e435e-9072-3d6a-a4a3-740e7e39742f | -9.17569 | -58.06385 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9951a509-b347-3390-ba73-47b17e6dc672 | -9.02604 | -59.53479 | 2026-07-03 05:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2505141d-5b86-3e60-aa28-d278e33355f3 | -9.25803 | -57.866 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d61c8bc0-4194-36c9-a80e-2c8690676c9e | -9.18022 | -58.06093 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37923e45-47e2-3ab5-b311-109f476f7d04 | -9.18782 | -58.06962 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f488a078-6570-3676-8efb-277780c3aa8d | -9.1898 | -58.05556 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d401307-dab4-3500-b209-eb47871d574f | -9.37385 | -65.77695 | 2026-07-03 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dea35f3-ffc6-3666-b0e0-79ddc1a33f4f | -9.17673 | -58.05679 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef39490d-ae15-32b9-bbe3-4d33bcb35eef | -9.18708 | -58.07001 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ad61a37-b5f8-32ed-bbfe-f0319c5d59d4 | -9.02237 | -59.53422 | 2026-07-03 05:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f02eccbc-3f33-3d83-8744-abe7674f37fe | -9.18628 | -58.0514 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1028e350-e0b3-34ef-8691-72c1d43d14dd | -9.17905 | -58.06884 | 2026-07-03 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 360176b8-0a84-3c8a-a6ea-c815ca2d6271 | -9.07538 | -65.41986 | 2026-07-03 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8ea30df-179d-3b2c-afef-e879469644f0 | -7.63703 | -50.03027 | 2026-07-03 05:40:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88f63194-f7d4-33be-bf17-c8141c61c46c | -10.30157 | -57.13199 | 2026-07-03 05:40:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f0b186c-b84e-34ae-a4b3-cb4f9636ad2b | -11.35865 | -55.41227 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01f92f46-67c3-3795-87a0-3bfb93b6fae6 | -11.63157 | -59.01365 | 2026-07-03 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6294a61-762a-32f4-848b-98c70182df8d | -12.09058 | -57.14462 | 2026-07-03 05:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e2a0ee5-905d-3ca2-94e5-9829fc0d3820 | -11.41675 | -56.05824 | 2026-07-03 05:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36f3df7d-63ab-3cc7-9d25-41b9f32051f5 | -11.62699 | -59.02137 | 2026-07-03 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7774e12-d025-3ff3-a49c-dd106c88d308 | -11.35781 | -55.41125 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11f69503-03d4-323d-9552-f38ff4299770 | -11.98304 | -58.07071 | 2026-07-03 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4159dcf1-c51a-31cd-953e-e07c06d7b173 | -12.43328 | -58.41357 | 2026-07-03 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 461aad15-7a01-3364-870a-fa4455b6ca16 | -10.90184 | -56.85253 | 2026-07-03 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4f5f832-8c95-323e-9b00-f231530a805c | -10.90123 | -56.85697 | 2026-07-03 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd6811cc-397f-3882-9ff0-b5041b0502f1 | -11.3536 | -55.40496 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcd035ea-748c-3d19-b527-4c4818e20af7 | -11.34492 | -55.43228 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37ca1bd3-290d-3140-a72e-ac325a441630 | -11.34565 | -55.42676 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5979673-3bed-3337-a5ba-c05c1d3e8a67 | -11.62772 | -59.01641 | 2026-07-03 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8908c03-5956-39ff-99dd-2c7cc150dbb7 | -11.41543 | -56.06835 | 2026-07-03 05:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bde412b1-1aed-3ca0-9ddc-b6ff9c3292f0 | -11.41609 | -56.0633 | 2026-07-03 05:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 374590cf-9b9d-3a91-8e88-53cf77408607 | -11.79535 | -57.00341 | 2026-07-03 05:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f53df64-df4e-35c7-9945-f3c3d043f938 | -11.63088 | -59.01862 | 2026-07-03 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2afca9ef-fe44-3ebb-93f5-7c400e7d6c2f | -11.35134 | -55.4219 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f02872a-2bcb-383d-a703-7a5b4547f574 | -11.98354 | -58.07057 | 2026-07-03 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a00e85c-f74f-30b1-81c5-0b88b745b32e | -11.35209 | -55.4163 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d17c3911-8b34-3532-8cc6-3f4cd35caa9d | -11.41201 | -56.05749 | 2026-07-03 05:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6da65a27-4419-3c56-9e72-e72e9f10f30e | -11.50366 | -54.50416 | 2026-07-03 05:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54d9129c-6710-354b-90fc-caf1d1a09b53 | -11.79323 | -57.00109 | 2026-07-03 05:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3940329b-a075-3aab-9799-a15ba4e5cc30 | -12.77867 | -59.87988 | 2026-07-03 05:42:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f226c93-839a-3ab5-a8fa-2e74e25ff122 | -12.42866 | -58.4167 | 2026-07-03 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fade6b4b-8874-3e82-bf7a-a5c515371f41 | -9.64539 | -67.49277 | 2026-07-03 05:42:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8251c33-3e74-3e0a-963b-9c06d92a171a | -14.41194 | -60.2064 | 2026-07-03 05:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e8ac4c0-e757-3d75-a122-b1ef0eac4448 | -11.35284 | -55.41065 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b68971c4-ca8e-3db4-aa07-2a5d11cd1f75 | -11.62697 | -59.01805 | 2026-07-03 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6907747a-fd64-3fa0-8bf3-02cdd874f018 | -10.81896 | -58.0186 | 2026-07-03 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9f43ab7-e27f-3f5d-8ec0-629b120a77a6 | -11.41742 | -56.05315 | 2026-07-03 05:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6a8ec59-3427-3a14-85d8-be3bd813262c | -11.50325 | -54.5074 | 2026-07-03 05:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 235e8611-ba99-30be-9b15-8fcf19149047 | -11.63548 | -59.01424 | 2026-07-03 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 077db8ef-f486-3c22-a7ae-f799ca1accab | -11.34714 | -55.41557 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8e873a6-758f-38a1-aa9c-eef564554828 | -9.96377 | -64.96666 | 2026-07-03 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bb91d37-6803-3eb4-9d44-26e820a8b02c | -11.63626 | -59.01261 | 2026-07-03 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6111a17b-ec3a-3432-9135-35d2258ea618 | -10.9057 | -56.85756 | 2026-07-03 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52287495-b1f2-3171-a047-46d0880b98ae | -12.78244 | -59.88045 | 2026-07-03 05:42:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f40be733-9497-3531-9227-063a94a93c44 | -11.63163 | -59.01698 | 2026-07-03 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78003182-2c3b-3acb-b370-1f10062d9e6f | -11.35705 | -55.41695 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 799da9e3-c7b3-3d68-a232-ad50143b8e73 | -11.34639 | -55.42118 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83dbf4cd-35db-3b1d-81bd-2960a0a9182e | -9.79159 | -65.54211 | 2026-07-03 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a441b443-93f2-3b88-bd37-bc00a1f3f318 | -11.79593 | -56.99899 | 2026-07-03 05:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c8b4174-cfab-3668-858c-9cfd6f4457d3 | -11.63235 | -59.01202 | 2026-07-03 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3a44432-838d-39ce-875d-4f51bfa37b90 | -11.35793 | -55.41798 | 2026-07-03 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d31aa061-4408-32ef-8d1e-487c89ab6fa6 | -11.7977 | -57.00175 | 2026-07-03 05:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b12f951-bc71-350a-9bcf-6bb2fe1b052a | -19.50874 | -52.74302 | 2026-07-03 05:44:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a7c96c5-6868-3a20-8c02-206f8a29097b | -19.50854 | -52.74343 | 2026-07-03 05:44:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f4b7b8e-9db4-3ef8-a904-7b6e36cb2acc | -19.50925 | -52.73755 | 2026-07-03 05:44:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
