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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87b10747-45e8-31f9-9a65-64227484a8f9 | -16.8451 | -56.778702 | 2026-09-22 00:57:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2639df85-e9e1-3b24-b98c-5f15333d9d55 | -6.1341 | -59.961899 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f20df285-4c3a-3c06-9fd2-daaf576b720b | -12.9265 | -51.057598 | 2026-09-22 00:57:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3a14ed3-6b16-35a0-8fe5-4c6792a1ec3a | -6.8616 | -59.896198 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8291cba4-5789-3239-adca-d4a3020fa47e | -4.5035 | -59.551102 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e49a934d-70ca-3f46-9bac-2819802f8143 | -3.4216 | -61.313202 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11122154-68a9-3ed1-8b63-00e74fb8134f | -3.3931 | -59.518501 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f760642-eafd-3bc2-9ee5-04efe1eb5aff | -6.0837 | -57.696201 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aca11f6-d4d7-3027-b6fa-b9736a4b77a3 | -6.2944 | -59.940899 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7e85bca-0a0d-36ad-a3ae-365e0a1096aa | -8.6109 | -54.637798 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 003bd128-a571-3258-9a7d-106583e54e12 | 1.551 | -55.8993 | 2026-09-22 00:57:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47f205c5-87e6-3e1d-9d35-d9d7bd7328a9 | -5.4159 | -60.202499 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c67cd2d-3009-3d3c-a1f0-373609b632d6 | -4.5053 | -59.558899 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6aee720-48c4-342a-9c9e-3c0313182330 | -5.4175 | -60.209801 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fbcd0cb-3ad9-3898-97d4-6c5875de58c2 | -6.7906 | -58.783001 | 2026-09-22 00:57:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51e16338-a479-3770-9314-881cc68bf9c2 | -2.8787 | -60.106998 | 2026-09-22 00:57:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5c62b52-77cc-3fa7-bcb8-530b48ae52b1 | -3.9064 | -60.589901 | 2026-09-22 00:57:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af4a6356-9774-3334-a527-f3b6b0e8d778 | -3.6038 | -60.573799 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b18426bb-cfe5-3960-b6b2-16ae0202c8f7 | -6.1372 | -59.930302 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| beaa6c2a-f3a5-3b5a-b735-1416dadd7b60 | -3.6776 | -60.626202 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d086d37-42f1-3e93-9a4f-9ad0a1e31a6b | -6.0856 | -57.616299 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e361a827-b30c-37b9-b18e-c25d244a588b | -12.1463 | -61.166199 | 2026-09-22 00:57:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e0176c7-49ba-368c-b86b-79662848fc05 | -6.1956 | -57.777802 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70065502-1038-3394-8ff3-d7a0f8adbfb7 | -6.1351 | -59.876301 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb68f68-eaf6-35eb-8da7-a63c675cea98 | -6.3515 | -58.268799 | 2026-09-22 00:57:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd79b4e0-b764-3163-94d9-733f811eaf55 | -2.5597 | -57.510502 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0be18777-23c5-30e2-aef8-288c91f11da6 | -3.4552 | -58.400902 | 2026-09-22 00:57:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3ef8b12-02c3-3584-aa5c-4e3001838829 | -6.5142 | -58.3036 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f7be365-cb1a-3cc1-91de-78a685b5de77 | 0.1781 | -60.48 | 2026-09-22 00:57:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 897af842-e3ea-3184-9740-7502236b5c37 | -3.3353 | -61.2957 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8a99876-d374-3cfd-a885-7fa3f70bb3b2 | -6.0413 | -57.823601 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c92ab6d-c560-3c2d-a352-b6d9cfcc4f80 | -3.917 | -56.055099 | 2026-09-22 00:57:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0a23433-110a-3719-b97e-e2b0f31494d5 | -7.5989 | -55.351799 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78bee697-c2e7-38ea-a774-a4d2abb422a9 | -6.0976 | -57.623501 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bfe9834-5870-3f6e-ad7e-45d5cf5b176c | -3.0692 | -61.259201 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 850019e3-b91e-3634-a13e-a91204b9fc0a | -7.5861 | -57.682499 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42a0e55c-03e3-38c4-b1e6-374f98863b6b | -4.4148 | -55.5075 | 2026-09-22 00:57:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5b725a2-6393-38ce-a5ac-2f1239b99def | -3.4612 | -59.545502 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32f7d087-74f2-3de7-8275-b70b21c995fb | -4.4115 | -55.4939 | 2026-09-22 00:57:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 625282fc-3a25-30ca-9ce4-3b0756861bdb | -10.5886 | -53.997101 | 2026-09-22 00:57:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca4d9294-318e-317a-9aae-51fcc16e3ee6 | -3.4881 | -59.5732 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28f5d61b-a58e-3405-b279-fbe74f02525d | -11.7449 | -50.802399 | 2026-09-22 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cdf0df33-990b-36a8-8684-e5cfa4b21b71 | -6.8369 | -58.982899 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ab05a13-4968-3e26-be7b-6db9542123cb | -3.4918 | -59.1852 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1b4b642-d65d-3604-84b5-b693c1505fe4 | 1.0835 | -60.6646 | 2026-09-22 00:57:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a655336f-ccd6-310a-8914-197620464eb1 | -9.8679 | -55.735401 | 2026-09-22 00:57:00 | METOP-B | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58fdbc2b-26af-3faa-a786-39bad953d2fe | -6.8296 | -55.537701 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f59ad74-b68d-3358-a7bc-3238762531e6 | -12.8051 | -54.019299 | 2026-09-22 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11e9d513-8e10-3918-8b29-774a97b46cab | -6.3535 | -58.277401 | 2026-09-22 00:57:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23018016-cf42-3867-a8e6-e466798999ea | -2.4041 | -58.2631 | 2026-09-22 00:57:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5f15916-c526-3a20-92ab-b05f4d3a29be | -8.1443 | -54.795399 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5c8738f-ebc2-3667-8113-cc8d166fc17b | -3.2853 | -57.844799 | 2026-09-22 00:57:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad5ace4a-2f22-358e-a68e-6a3e861a12b9 | 0.7865 | -59.200401 | 2026-09-22 00:57:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 472e99c5-f859-3731-a9ee-03cc815d652a | -3.3631 | -61.282101 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b516b7b-b7ff-3463-ad02-7ed7142d9c96 | -6.7079 | -59.004398 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ecab2417-90b8-33e4-9053-fd0ff03cbae3 | -6.3736 | -55.267899 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec34ab8-a3d7-3926-b099-baa5bc25f206 | -3.4556 | -59.521301 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f824a6b1-dfc5-39f8-aa2d-b883525673e8 | -10.5256 | -54.493801 | 2026-09-22 00:57:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1dd55a0-47a0-3df2-9f3e-f0fba8aafc9f | -7.2323 | -55.584202 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42d6606a-c3f7-387a-aa2b-f21a143fde14 | -7.5623 | -57.669102 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9efc893b-813a-3dc7-b1f8-26a1cc6e84eb | -9.1023 | -65.363098 | 2026-09-22 00:57:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0870ec44-59dc-3f0e-b711-d2499415a42a | -1.9266 | -56.5951 | 2026-09-22 00:57:00 | METOP-B | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a59b7d75-74fd-39bc-ae1e-71f6865191c4 | -2.5573 | -57.499802 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0552b39e-a3a7-3bc9-96f2-2a3f43da29f7 | -6.1406 | -59.945 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9db90983-2be2-3266-8147-606fecb196c4 | -2.8557 | -60.909901 | 2026-09-22 00:57:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49b63cb2-a102-3044-a9fc-92cd397879f4 | -6.9785 | -59.776798 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a452b62-3ec8-3490-8342-233dcd68c7cd | -3.9342 | -59.630798 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6a6915a-bc1f-3993-941e-3fe2dd42b57f | -6.865 | -59.910801 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0dab5681-de79-3e4e-be92-5485d33e8140 | -3.6855 | -60.570702 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a458393d-d9b0-3ee0-beca-04b7baee6f39 | -6.0815 | -57.686798 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26f7afed-5784-315e-8ee0-50d0d7aab86e | -8.2437 | -55.247501 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 748a71dc-c19c-3765-8ada-fc53adcd0040 | -2.8519 | -57.795502 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3d9aa06-261b-3b3c-a2d5-6a3d0874e37a | -6.3575 | -58.294701 | 2026-09-22 00:57:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 697c1284-90ee-34cb-b737-d386e76ccece | -6.078 | -57.628101 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dddd07eb-6190-3075-9cbc-be509c6d7f48 | -2.8715 | -57.791 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17bb34ba-f7a9-31f2-ae38-6c226138bb81 | -6.3308 | -60.009701 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8415213b-43e0-36cd-89ef-ef399bbfa525 | -6.0923 | -57.6446 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4211eb09-4484-3f42-bcd4-e8c4a893dfaa | -2.7879 | -59.890202 | 2026-09-22 00:57:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c06d5e89-07f6-3e5b-9455-c2bbf6db3628 | -8.2339 | -55.249802 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f13acc70-ebfd-3196-a90e-f85da5bdbe5a | -8.096 | -55.361698 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28c0aa3b-24b8-3a7f-a7c7-5dc0c4ea247f | -3.4937 | -59.1936 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a33ff5f1-e766-3b5d-9fc7-e304b1a21f5d | -6.5122 | -58.295101 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6e3aed2-68f2-393c-9d16-e94f5e32b0ff | -3.4838 | -59.5993 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20218a16-65c1-395a-9577-fc322fc39497 | -8.2429 | -55.2868 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 290366e1-09a3-3c75-9e09-78cb8e873fdf | -6.3429 | -57.878601 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19d39d4c-f829-3fed-83d0-b45222a6d21a | -3.7099 | -60.542198 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9898ddaa-2a62-371f-a2cd-fcde38fa059b | -6.4582 | -59.980701 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03dd7314-a142-39e1-a7a3-fb0f8bd20122 | -3.4055 | -61.2873 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 066caa54-328e-3f46-8493-f26f6086fae4 | -3.4141 | -60.194801 | 2026-09-22 00:57:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| adbb8503-7580-375b-ad8c-c244782ac79a | -2.8641 | -57.803398 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5681b0a9-b78c-36a5-aa71-dab0a2df2476 | -12.909 | -53.896801 | 2026-09-22 00:57:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd120de9-10ae-3943-810b-22c0fa331062 | -3.6005 | -60.5592 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77109a56-c350-3694-8713-9e0547e33e9c | -3.6988 | -60.629002 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54c7cf4b-57d9-349f-a9e8-ecb37cf7a049 | -3.2779 | -57.856998 | 2026-09-22 00:57:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11c0d7ff-0a47-348f-94cd-b5a7deaa71ca | -10.5818 | -53.969501 | 2026-09-22 00:57:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed2fbdd-2945-3b5b-a3cb-c22db6da236d | -3.4169 | -61.292099 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 011164b9-3ff7-3cbc-bfd3-bdb16a5d380f | -5.9794 | -57.7794 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd822191-7e2d-3c1b-894c-2537f88c28b3 | -16.846901 | -56.7868 | 2026-09-22 00:57:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 66d6cbc1-1aea-3c16-8618-1486c98aeec8 | -6.0878 | -57.625801 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ebf0104-fe8c-300e-999f-5d3714b8cc8a | -3.3859 | -61.291698 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
