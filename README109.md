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
| 60269e49-253f-3770-ae85-308311cbc868 | -11.55826 | -47.65985 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e43239ad-6299-3346-8ed2-bdc5caad4d62 | -6.68464 | -43.71496 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 285e24f7-2e15-3e7a-99cb-3fb9fe8f9916 | -6.72244 | -45.96756 | 2025-10-03 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3c75229-f12f-301b-b069-02e5fe5e30de | -7.79994 | -46.01717 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd169323-5256-373b-917f-431346052dfc | -6.5536 | -43.89202 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a9e1e61-bd6d-3e6b-8cd7-1e284d561d16 | -7.75118 | -46.26929 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a1ecf473-0b64-3efb-825d-b01a51a0ca6c | -7.75157 | -42.56889 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| fd0dbf52-babb-3130-914a-a37886ef6c10 | -10.98886 | -46.67989 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b378655-2b8d-386a-9c9e-ef1ab15171d1 | -6.37773 | -43.88155 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c669f638-14af-3269-a28c-8a8296261f6b | -11.08689 | -47.70821 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff4e66aa-3e31-384f-802c-92f1ee07045f | -10.91219 | -47.02549 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad46a284-f5c7-3bbd-9fb4-0ab64322f8a9 | -4.65585 | -45.80465 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1cbaa08-9e71-3bcd-b80d-906bb85bb42a | -8.25288 | -47.03097 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5639fae4-7504-353c-8c61-c26b814b3ffc | -7.75515 | -46.26614 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 6dd34774-f15e-3dbc-8862-6d18d7f09b1c | -6.64915 | -42.79002 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| b6171bf5-b5ef-31d7-93ba-6d88daf43eef | -5.63779 | -43.9156 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| ad3d56e7-4258-3c08-8990-0c0af5b8014c | -10.60306 | -48.71895 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06f516c8-a70a-3916-b125-58ad9b8b74d4 | -7.55462 | -42.39742 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa8eb06c-5d8b-3ad5-a5fb-717539f866d4 | -5.24886 | -42.97537 | 2025-10-03 04:32:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| be8bc97d-e3e0-3a0c-9230-d0e715c102dd | -7.76702 | -42.6092 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a6f7db5b-b9ee-3127-8c4c-249f7289ee7c | -10.90635 | -46.71832 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 124e693d-24d1-3e81-901f-2d188799c06b | -7.78209 | -47.37221 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 019d33b9-ebff-31f8-a0a3-0d2a86f6573d | -9.94997 | -43.6549 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26392a34-fe49-3967-a963-a1eb4051d09f | -6.64966 | -42.7865 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 65ed57bf-1f32-31c1-8d14-f69d6371fbe5 | -11.81061 | -45.01181 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cb675fa-b264-3205-84d3-d644adaa08cc | -6.22459 | -45.35862 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7831d57-594d-3d3b-8522-4756757d8c0e | -4.66957 | -45.79209 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 599c21b4-e56f-3f0d-8394-c4cf599482bc | -5.37846 | -47.21554 | 2025-10-03 04:32:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e0879bf-3464-351c-a5e9-67bc7bec3c64 | -9.92555 | -43.62637 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfd3feed-26e6-3667-8183-b24b7ecc8cf4 | -5.63542 | -43.90612 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b95657d3-b2a9-3a1e-a9be-456767b6a6f5 | -10.9075 | -46.71072 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64e1abd5-15c2-34bb-875b-01e7b0e7c21a | -10.59424 | -48.71036 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fa4f9b9b-2e2f-35d2-b46f-5820002b522d | -4.89391 | -49.96623 | 2025-10-03 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37c3f547-abed-3b82-a697-d26be81b34ed | -9.03413 | -46.66955 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c6968ec-cfa0-3ea8-8f86-edd37624eecc | -12.24137 | -44.04026 | 2025-10-03 04:32:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ec4c08a-49d2-3e88-be3f-d03b01ed65f2 | -11.78411 | -46.832 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6316ca2b-37fd-3065-94f2-193491246607 | -7.7864 | -42.56245 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 78328899-b463-3251-84fd-db89b3818db4 | -6.46448 | -44.20641 | 2025-10-03 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cc21339-3983-33d5-bd84-7329c4dac2c0 | -11.67686 | -44.27543 | 2025-10-03 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83847cfd-5ea6-3277-a677-db338c23dbad | -6.6876 | -42.83619 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8d1edde5-1cc3-3e0f-a3f3-c9445455272e | -4.50831 | -55.4579 | 2025-10-03 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29ef8c37-aefd-3d38-9337-d89c0deaf955 | -6.33127 | -44.68854 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d925b2e2-52a3-3344-8834-be499e22791c | -7.7655 | -42.59015 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c2b39365-1393-311c-ad76-2f97e8f3de28 | -14.9076 | -48.29796 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d73033ed-31ea-3ef4-9e55-19c85881086e | -19.45568 | -44.2899 | 2025-10-03 04:34:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 425db0fb-5142-3b07-9946-e2356ee297c1 | -14.67877 | -48.07996 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99f17bc6-c920-3576-8df2-ae78ab958855 | -14.29286 | -45.96992 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51e3cba6-866a-3b27-93dc-c96b1435e924 | -13.16783 | -47.89147 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a255ce1f-772c-3e69-bf85-68cc4dad8ef7 | -12.86424 | -46.99939 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9d5e76d-2f17-364c-a3c5-140c4fa66bc5 | -12.60944 | -46.97841 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6d9e0f89-29a6-3bfa-8c38-a86adc41e0de | -12.90164 | -46.93835 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9e54f261-9051-3fd0-894a-682c945712d0 | -14.74821 | -48.10977 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c279d30f-9796-3d04-8be7-20727af4d424 | -18.24215 | -53.31815 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbac057a-ead0-3558-a2f3-77ca050d5548 | -12.93637 | -48.43159 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c459227-659e-38d6-80e3-c40334a92dde | -18.23362 | -53.34799 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f38c3ff3-de15-3fd3-ab26-24277d20e3dd | -14.87876 | -46.8504 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5f047f23-b0c1-35bc-8dce-9ce639e756db | -19.58556 | -45.908 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc49868c-7032-3dbc-8383-8c605f0a5550 | -13.97295 | -48.16964 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e688487a-ae2c-3af4-9c74-5e72dc8b8980 | -13.58095 | -47.58716 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0b3634cf-88d4-3e5a-84be-41f758c26771 | -12.18715 | -47.80613 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3390af6-ce63-3eff-a503-46c978830944 | -14.87505 | -48.3079 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 581f9b94-0dbb-3f31-af80-4533bfac80bb | -13.13264 | -47.84113 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9724f6f-1601-3ffa-8696-41801dbdc4b8 | -14.9363 | -46.90103 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 08fa2a44-466a-3c41-ae92-6cf9fca3366a | -14.4208 | -46.09575 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa83b411-d1d9-32bd-9477-d4e2e7cc2455 | -13.19811 | -47.80554 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 736339ac-5dd4-3bd7-b0e5-a9991005b839 | -13.31958 | -47.58187 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4abda298-8102-30d2-b803-bc9b16596762 | -12.71693 | -48.57577 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6d82110-8cac-3148-b4a2-1d6d5a6837bd | -12.37139 | -46.52263 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27c5808c-66f6-3ef4-a760-678889a2a903 | -12.47452 | -54.4246 | 2025-10-03 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e5c03db-8a6a-3dd5-8667-d3821b20205d | -17.27411 | -49.01135 | 2025-10-03 04:34:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70e4d5ff-dcb8-3d05-9f8c-312e62aa65ac | -13.82085 | -48.03711 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61070356-ace8-37d8-9e6d-6c6cc76c0b0f | -15.78102 | -43.69696 | 2025-10-03 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aecbfd1-201d-3a76-a98a-8a24af5a05cd | -14.29013 | -45.91755 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03ee0af7-5f23-33bc-8212-bd7e84c21e0d | -15.35645 | -47.06473 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbba571f-858f-301e-8848-d161b8de53b5 | -12.79915 | -46.87553 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02213bb5-dcf1-3b7d-852c-240621497232 | -18.64406 | -50.682 | 2025-10-03 04:34:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40f1474a-2e7c-3ee8-aefb-d8bdd3295a73 | -12.92731 | -46.37607 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 334626ee-2fe4-3eb0-9d10-5a935f496cbf | -13.23542 | -48.49452 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f538587b-0952-3491-a604-f2724e838af7 | -14.46742 | -48.41909 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 220e7226-781b-36d1-93ea-b0e4484c5576 | -14.89752 | -46.96988 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| e657656e-e5e6-3369-b60e-cb3e6a9862ee | -13.55653 | -47.58729 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6132d51c-f734-3a2c-9daf-a339d537bb4e | -14.64973 | -48.24923 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d870e144-3189-3bc7-bc06-69737201e808 | -14.4361 | -46.37601 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fda6a7a1-b68e-3f25-9352-68e11775b227 | -13.35012 | -47.33015 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9aba377f-64d8-305b-af1d-fbde396a9b43 | -14.38037 | -48.48052 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3725ae2e-ab7c-3983-81fd-11543aa88c50 | -18.25849 | -53.30796 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 115cb865-b10a-3876-ab20-2cfeda3c4fbf | -15.23597 | -48.72029 | 2025-10-03 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc3cdebe-11e8-38f9-85f3-2a23d37e2ce7 | -13.2048 | -47.82977 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95464656-fcbd-3874-bdd1-6052311d70d0 | -12.87463 | -44.62946 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9011988-e8fe-3313-ba4b-b0cf06817771 | -18.18628 | -53.34768 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ef6ed4f-e73d-377f-b441-ea5623092956 | -12.8062 | -46.85202 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1abaa10d-e446-3939-a250-cf5524257373 | -15.21042 | -47.98849 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f11012e2-9e93-3021-ac85-77802a6d03cc | -13.79887 | -47.58061 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cfcb2b0-3477-3309-a7a9-912a43da4137 | -14.6559 | -48.25402 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e713d205-7135-3ab3-8779-f1e1509c1147 | -12.9179 | -46.36607 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5eff99d-d11b-3303-b011-259804d1a112 | -13.75647 | -48.0874 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5b8e4a4-6e80-3e0e-939e-ac4e949413cf | -13.77724 | -47.58508 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57275e68-eb94-3feb-9f7a-2cd68c279fea | -15.71571 | -46.27066 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a9c212a-456f-3f7f-aa8c-70b177820d9a | -13.38578 | -48.13388 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03e507f9-60e6-329b-9983-83f7b0f6cdb6 | -14.01142 | -44.96322 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README110.md)
