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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 574a1c5a-ea8e-332d-9669-3fbc9757aa96 | -3.4578 | -50.0679 | 2026-09-24 03:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 668a4721-179d-3d12-80cd-13d6b1072d8f | -3.6764 | -60.5649 | 2026-09-24 03:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| be946b39-975c-36b8-af4c-2146e9b724f3 | -6.6146 | -59.9272 | 2026-09-24 03:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 26826dcb-8742-3270-b283-12eac8872d36 | -2.631 | -54.6975 | 2026-09-24 03:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a1b7f43b-6cd8-3660-b3e5-78920e176c31 | -11.6596 | -43.4951 | 2026-09-24 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| e04a0865-7ca5-3e52-9199-2d09efbdabb1 | -10.0924 | -46.0005 | 2026-09-24 03:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 07ca7900-c967-3051-b83e-c072ace5c854 | -10.0917 | -46.0458 | 2026-09-24 03:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 45d4ed79-1f9b-36b7-91b5-c63a7fb80694 | -10.1098 | -50.1921 | 2026-09-24 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 3db92a0a-9ff8-3669-961f-b223e7323672 | -11.6404 | -43.4981 | 2026-09-24 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d57f0996-2483-3299-a883-b215922aee92 | -11.4015 | -47.3851 | 2026-09-24 03:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 6382510f-6c9f-3faa-a7dd-b8708f809789 | -5.0064 | -45.5401 | 2026-09-24 03:40:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4f366611-37fc-37ce-82e0-1db446351310 | -10.0921 | -46.0232 | 2026-09-24 03:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 19f09816-923f-3757-a18e-31f22aee2078 | -10.423 | -49.3649 | 2026-09-24 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| af95309b-d224-3923-8891-d3bc34e0e481 | -4.9876 | -45.5637 | 2026-09-24 03:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| f4ee2f4b-1f17-31c2-851b-821d170da207 | -3.4577 | -50.089 | 2026-09-24 03:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 14c5437f-a3e1-3271-9c23-b7b984cc161f | -6.6145 | -59.9464 | 2026-09-24 03:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 61071037-ab0d-3910-b264-b23fb4f02ece | -3.4392 | -50.0896 | 2026-09-24 03:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| b69dcdb9-d546-3932-a339-4e6af9db716d | -5.0062 | -45.5626 | 2026-09-24 03:40:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 210205a2-e7dd-3532-bda0-ea262a1751d8 | -12.0096 | -52.4675 | 2026-09-24 03:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 735f26ee-371f-39ad-a15a-e24da2ee6934 | -3.6763 | -60.5839 | 2026-09-24 03:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| dfdacd68-a701-36d8-844e-77d27d5afbfe | -5.1058 | -60.2639 | 2026-09-24 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 70d2c9ef-04b3-3661-93bc-31eb05907148 | -6.6146 | -59.9272 | 2026-09-24 03:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 11e453bf-5541-3e7d-a238-1e4687026262 | -3.4577 | -50.089 | 2026-09-24 03:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| d054e35a-2eb8-376e-934f-aece7a4358ae | -10.423 | -49.3649 | 2026-09-24 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 8abdf2bb-7234-3f74-846f-4bdc48204f99 | -10.0924 | -46.0005 | 2026-09-24 03:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a4e5b640-98f3-384c-ac46-4d5d9e630965 | -11.6601 | -43.4714 | 2026-09-24 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 41a2114d-4b04-3e70-bd65-f10be61c22c0 | -2.6493 | -54.6971 | 2026-09-24 03:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e0197246-902b-336c-b116-c5aeb3dff713 | -10.0917 | -46.0458 | 2026-09-24 03:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a8c3448b-978f-3db8-85e6-6b69f650c4e1 | -10.0731 | -46.0254 | 2026-09-24 03:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2111d886-9be5-3a8f-a862-2295c7c60090 | -10.1095 | -50.2135 | 2026-09-24 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 70ae8f32-9e86-338b-adc7-9ef51e730550 | -10.1098 | -50.1921 | 2026-09-24 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| dd1b9846-2360-3541-a2be-fb977a5bdb82 | -3.6764 | -60.5649 | 2026-09-24 03:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 0255cc56-44aa-3e56-8847-0ee36fbca166 | -11.6596 | -43.4951 | 2026-09-24 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| f8897dc4-80d6-3622-8ab8-89350858c637 | -3.4392 | -50.0896 | 2026-09-24 03:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d866e1b2-b2c7-3bd8-bbe4-c030998d899d | -7.8996 | -61.1772 | 2026-09-24 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 13b2ee3e-777b-3fe6-a0e9-374f0c66454b | -10.0909 | -50.194 | 2026-09-24 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 97e18b99-61e2-31e1-bf3d-2ea148fa9327 | -3.4578 | -50.0679 | 2026-09-24 03:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8d6f04ad-6279-37ee-bc53-dff618417740 | -10.0734 | -46.0028 | 2026-09-24 03:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 61f74f34-e6ed-3f96-9c7c-89d286c3ca92 | -2.7151 | -57.5109 | 2026-09-24 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 88435773-0d14-395f-a568-71c5f8ab271b | -11.6596 | -43.4951 | 2026-09-24 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| af4a3f20-681b-3c01-923d-ae638ba41614 | -10.0909 | -50.194 | 2026-09-24 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 518b7b51-f5a3-3608-bb0d-30ea2ee71547 | -10.0921 | -46.0232 | 2026-09-24 04:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 043c0101-2848-3755-a114-394b85d335a8 | -10.0917 | -46.0458 | 2026-09-24 04:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 4827cffd-ceca-3445-899a-63038ad57140 | -10.423 | -49.3649 | 2026-09-24 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 34e2cc83-5784-387b-9141-3242e7d23b07 | -10.0731 | -46.0254 | 2026-09-24 04:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1d124505-aac7-326c-9d9d-3e37b0ac5654 | -10.1098 | -50.1921 | 2026-09-24 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 55181145-3e0f-3ab4-9de7-d81460cdd44d | -2.6493 | -54.6971 | 2026-09-24 04:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| abacac32-2203-36c3-b70c-0812a54e3525 | -6.6146 | -59.9272 | 2026-09-24 04:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b1ac38a4-a6b8-392f-bde9-02148ef10735 | -11.2281 | -51.3727 | 2026-09-24 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e43535b1-7144-37d7-80af-1c9445f558eb | -11.2284 | -51.3515 | 2026-09-24 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7cf90b8d-e047-3627-b4ad-797fdcad978f | -11.247 | -51.3706 | 2026-09-24 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 8fecf681-41e7-35a5-aab0-15850c86304a | -11.2473 | -51.3495 | 2026-09-24 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 72822dd7-ca7f-3db4-94d6-5c59198f16da | -12.13 | -50.7407 | 2026-09-24 04:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 4fe72e0a-58de-3fa0-b8cf-c38caa833a24 | -11.2278 | -51.3938 | 2026-09-24 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 60cdcee1-eb8a-3498-96f4-bce2446a138d | -10.0734 | -46.0028 | 2026-09-24 04:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 5fdf7c02-c1af-3ab0-bcc8-e5275e2fac88 | -11.2467 | -51.3918 | 2026-09-24 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 2387b007-1df7-39a8-9207-8ed74366689e | -10.0924 | -46.0005 | 2026-09-24 04:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| e078bf4c-63bb-3835-a2c8-85ba25259ddf | -0.93743 | -47.5507 | 2026-09-24 04:06:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| aad33cdc-b126-379c-8dab-c37450561715 | -1.33203 | -47.7866 | 2026-09-24 04:06:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c255ead-e309-3ffb-a9a7-ae028eb3a7c5 | -1.39497 | -47.94631 | 2026-09-24 04:06:00 | NOAA-21 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 95efd7ee-fc5b-3bfe-863e-c93b19c7447a | 2.45302 | -50.94679 | 2026-09-24 04:06:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9283c547-84de-32fb-9240-b1cfcd5d4141 | 0.60709 | -51.56984 | 2026-09-24 04:06:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1253c4c-f38e-3b9f-ac89-acf505703528 | -1.39283 | -48.99515 | 2026-09-24 04:06:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec6267df-ced0-3bab-a31e-65f123cfc608 | -0.93666 | -47.55546 | 2026-09-24 04:06:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 91976d1a-0b4c-3b8b-b339-1f35d68c4676 | -0.50554 | -49.15193 | 2026-09-24 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23322c20-47e9-32f0-b594-1b977f06e2bb | 1.29821 | -50.86325 | 2026-09-24 04:06:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c344001-c08f-37ef-95ce-b24d40dcf500 | -1.78615 | -47.83258 | 2026-09-24 04:06:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 156358bd-e322-317a-ad74-ee76c4439b0c | -2.88208 | -40.02602 | 2026-09-24 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8bc81235-0808-314a-aba0-9786b75bba14 | -0.50604 | -49.14878 | 2026-09-24 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b5da36d-0025-3b53-b410-680790f889e6 | -2.88262 | -40.02254 | 2026-09-24 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f57809c7-7b51-3a13-895d-ebc363e0207b | 1.29407 | -50.8531 | 2026-09-24 04:06:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b9a2875-17f9-3563-8f15-f6b027cc0b3c | 1.29544 | -50.86189 | 2026-09-24 04:06:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55e8ace8-d92f-36d2-9e01-7d3fd1ea2af3 | -1.33283 | -47.78168 | 2026-09-24 04:06:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a7a9e42-3773-3522-b5ec-e1bbb209888f | -0.93377 | -47.55115 | 2026-09-24 04:06:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 204aab8a-bc35-3b44-a431-cc00517c347c | -1.39366 | -47.94411 | 2026-09-24 04:06:00 | NOAA-21 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 501b1d3d-70c5-34f1-a5b1-c62a286851df | 1.29886 | -50.86767 | 2026-09-24 04:06:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b47d46f0-13d5-3788-8568-60b94fccb988 | -1.52222 | -48.03722 | 2026-09-24 04:06:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28be441c-1eec-376f-a1ba-ec67fdd11cd1 | -1.39744 | -48.99892 | 2026-09-24 04:06:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35680b0e-65c8-39e8-810e-45d695e2914e | -4.95473 | -45.14676 | 2026-09-24 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bcabc42-aa03-38ae-a580-0227d01326e5 | -8.73965 | -37.18098 | 2026-09-24 04:08:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 660f2090-7159-384f-9233-5ec94762ca08 | -8.13282 | -41.27768 | 2026-09-24 04:08:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bcb236c9-8b10-3aa2-918f-1e207b8c0730 | -6.4576 | -55.00941 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2afc333-7cc6-36b9-a592-28e2e200f906 | -8.75277 | -45.8779 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9543246c-8a81-3e8c-bedb-7a352b9cab62 | -9.17538 | -49.99193 | 2026-09-24 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53277607-a851-3753-ae57-8491e8ad4c94 | -6.4227 | -43.48097 | 2026-09-24 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 634eed5a-ad9f-3a2f-8ac8-3a258c9e8c0a | -7.03094 | -44.64563 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83f4414e-9f88-3f85-a64a-e0448b9ecfc8 | -5.84471 | -49.87731 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30266b48-d8f6-305d-be8e-ae201b84f0c8 | -6.71848 | -44.15468 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 35c50f0a-8733-347d-8350-92a31fe68ca2 | -6.50821 | -44.02007 | 2026-09-24 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 086d11b1-a319-3c38-a2a1-8bbdc672c3be | -5.57226 | -42.72951 | 2026-09-24 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab4328fd-9332-3b68-ad79-2ccafbc83379 | -5.29598 | -49.27715 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3ef5665-e7e6-3494-a93a-1dcac177b9c5 | -9.9985 | -45.18879 | 2026-09-24 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac6a467a-49c0-39c5-b049-c9c3366b667e | -6.73313 | -43.07081 | 2026-09-24 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ea19dba-a5e0-3a95-ba84-06453cd6dd77 | -9.4676 | -40.33234 | 2026-09-24 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8a800e19-391b-3916-a9a6-613661e5d585 | -6.50221 | -42.42009 | 2026-09-24 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dba8ea14-7546-3dc6-9387-73f9524882bf | -6.41662 | -44.49379 | 2026-09-24 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 969ef995-d9fc-3ea1-823d-619d18997d27 | -5.20103 | -44.69203 | 2026-09-24 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 65746693-fd9a-3a88-9978-6bdaf59b8961 | -7.03384 | -44.65019 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65251371-8309-3a24-9515-3b6513d053b5 | -9.25934 | -46.24385 | 2026-09-24 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0c875091-18cc-38f8-99bb-94e917d7cadb | -6.57559 | -51.49149 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README29.md)
