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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcac0003-b97e-3acd-a561-75dc0bc78b73 | -4.11345 | -48.49343 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c8ebd1a4-9bff-3119-906e-cf1dafc8e484 | -3.91811 | -47.94992 | 2024-11-09 05:33:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f77f22a4-04c3-3ed1-9c34-6590b511bea0 | -2.40971 | -48.52166 | 2024-11-09 05:33:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 66432097-41b7-34fa-a7c7-49e5bd5f29a3 | -2.4611 | -50.39333 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 30c97cb1-e1c2-3b4d-ba3a-19116294269c | -4.19826 | -48.54744 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b6ea3eaa-5877-31e6-8862-c44cf8314ed0 | -3.16528 | -54.47614 | 2024-11-09 05:33:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 47651100-1a99-32b5-9c09-c1cb8943e00c | -4.05751 | -48.25366 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f6df0118-48d2-3bef-9a3a-fcfaeb31bb88 | -3.83456 | -50.04192 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ad5cbc98-94d4-3f5f-a353-28c1542b764e | -3.11599 | -50.14442 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 61798288-5db2-3d07-952d-f898e20f399a | -4.80341 | -44.76786 | 2024-11-09 05:33:00 | AQUA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f14f72ff-7b64-3d0c-b255-d240b7c1f470 | -3.55234 | -43.5675 | 2024-11-09 05:33:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 525b47a6-f385-30e5-8e69-b9952ff8e691 | -2.294 | -48.55317 | 2024-11-09 05:33:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 1ee4a35a-aa2f-3983-ae22-3dba7103d39a | -3.81591 | -49.85823 | 2024-11-09 05:33:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0fe62c48-7f88-3bef-8af2-47b0b0591d29 | -3.55451 | -43.55231 | 2024-11-09 05:33:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 99a9ccb1-39f4-304e-8a5f-6d646ffd12a5 | -2.87035 | -50.31705 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8a1cb9de-b72b-374b-9dfb-5799af11069b | -3.62878 | -50.18266 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d35e1df-9dfd-355f-9421-2534c72aec61 | -6.24027 | -47.28045 | 2024-11-09 05:33:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dd655eef-606d-3a41-ba17-b0a7ef6eb7be | -3.60152 | -47.34129 | 2024-11-09 05:33:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 56288a98-ceba-33e4-a416-273fee08a995 | -6.18855 | -45.44278 | 2024-11-09 05:33:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4ef0edb6-e391-30f6-b0ca-d39373e0ff67 | -3.34906 | -50.26022 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6b18a1e1-529d-344f-a610-afd27e98e8f4 | -3.95401 | -48.14272 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b74b7fac-83af-3053-905c-5df754af13ea | -4.25106 | -47.56833 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 7a25c7b0-8b6c-3c35-8cd3-1f894a96ccd3 | -4.49324 | -48.48366 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dd1b1b91-d6f7-3bc9-a645-b0088af54da5 | -2.97204 | -47.92226 | 2024-11-09 05:33:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| efb2213c-0926-31f2-8f5a-bb3dab9113ef | -10.73358 | -49.52984 | 2024-11-09 05:35:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| f53895bf-13e7-312f-bbec-cb37e6e86c8f | -12.01139 | -44.13176 | 2024-11-09 05:35:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f6f8318e-2a27-3fca-b584-4b62d751fe07 | -12.00908 | -44.14995 | 2024-11-09 05:35:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 60f3294a-bf35-39dc-86b5-6f6c160efd53 | -4.2486 | -47.5729 | 2024-11-09 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 88770c02-939d-3506-a6f9-6a144adfb814 | -3.9854 | -48.1708 | 2024-11-09 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ba7a86c3-5879-3d50-97da-e48f601b4e3c | -3.9853 | -48.1924 | 2024-11-09 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 4bb3b565-f065-3cd4-b22d-ee9ead994ea7 | -11.0881 | -43.3219 | 2024-11-09 05:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 95d37543-ba8a-3e7b-abc0-7411b7d64588 | -3.9669 | -48.1716 | 2024-11-09 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 132.3 |
| a8ec8ded-0422-3c50-8e80-b867452eb517 | -3.6003 | -47.3614 | 2024-11-09 05:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 7c99f9c5-56fd-36dc-a55c-ca03b91a69fe | -3.9668 | -48.1932 | 2024-11-09 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| f58691b0-612a-3b92-ad7b-f17aefa33f48 | -2.4104 | -48.5265 | 2024-11-09 05:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 43715421-7cf3-396e-8a15-f4dbff37db2f | -3.6004 | -47.3395 | 2024-11-09 05:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 57f8dc15-66f2-345e-a78a-82ecb7b2e51c | -3.1089 | -45.3419 | 2024-11-09 05:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 89c174e9-3655-3021-a89b-36a4390835ad | -11.0877 | -43.3456 | 2024-11-09 05:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 44a7fd00-2564-3c8e-8842-099f5449d0a3 | -1.5163 | -52.1901 | 2024-11-09 05:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 9c2a7318-b025-3998-8a7b-c02b8e5d5030 | -23.91112 | -54.06135 | 2024-11-09 05:40:00 | AQUA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| d9a7a4f8-efe1-3da5-9b98-14ca1b1afdcb | -3.9668 | -48.1932 | 2024-11-09 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ead2edd5-b8d0-3aaa-b415-e4fabc2b5602 | -3.9669 | -48.1716 | 2024-11-09 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| f9393e4d-7a25-3b7f-951a-5e31d622e9b8 | -3.6004 | -47.3395 | 2024-11-09 05:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 50b0fc15-b045-3695-bcc7-46cac9e4ffb6 | -3.1089 | -45.3419 | 2024-11-09 05:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 6fffe0ed-1f9a-3ac0-986a-8642d245a6e7 | -4.2486 | -47.5729 | 2024-11-09 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 73159415-4592-377c-b24e-b8ae845fcd74 | -3.0865 | -50.5625 | 2024-11-09 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d571772b-a617-3fc0-bf3c-0fa2bb868275 | -3.6003 | -47.3614 | 2024-11-09 05:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6e9e0308-a5e8-33c8-9fb6-26a139211ca7 | -1.5163 | -52.1901 | 2024-11-09 05:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c84e1732-8de3-3f3a-a3c8-9cacdcd6b84e | -3.8036 | -44.199 | 2024-11-09 06:00:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 57ec7651-a58b-3e0e-924f-26746ce0627a | -4.2486 | -47.5729 | 2024-11-09 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 93e1e39d-d8cd-3d0d-a30f-2e48521dc469 | -3.6003 | -47.3614 | 2024-11-09 06:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5862ff98-6720-3be4-87e1-b2990f63c932 | -2.4104 | -48.5265 | 2024-11-09 06:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 7e5329e3-802a-3872-95ff-0767825f6816 | -3.9668 | -48.1932 | 2024-11-09 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 34d9bf78-dde8-3360-9237-783d0ace48e4 | -1.5163 | -52.1901 | 2024-11-09 06:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 3eff319e-04ee-3800-ae37-2e86a5228aa0 | -2.4551 | -46.3014 | 2024-11-09 06:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 11241cb3-f7fe-3532-aca9-0421358737d3 | -2.455 | -46.3235 | 2024-11-09 06:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| b168c358-82f4-33f0-b13c-7fb44157f446 | -3.6004 | -47.3395 | 2024-11-09 06:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 7aaeee11-5425-392e-9c9c-94624ec19001 | -3.9854 | -48.1708 | 2024-11-09 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5360a073-1f6e-38af-b3d9-4b5b67eff992 | -3.9669 | -48.1716 | 2024-11-09 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 476bbb0c-54f8-3a4b-ba81-6c162af93c40 | -1.5163 | -52.1901 | 2024-11-09 06:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3d6644fd-66ea-379a-9cbd-4b9a3f66dd48 | -2.4551 | -46.3014 | 2024-11-09 06:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 43.7 |
| e88e4879-1780-3f73-9406-853925185dfd | -4.2486 | -47.5729 | 2024-11-09 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 84686309-3fd7-351b-a756-ce7c2ac84ee2 | -2.455 | -46.3235 | 2024-11-09 06:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b7768250-f218-31e6-9d14-10ceab26588e | -3.9853 | -48.1924 | 2024-11-09 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8a39bbad-c9d4-3b4d-9db7-bbc3a4f7b894 | -3.6004 | -47.3395 | 2024-11-09 06:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 54063309-f085-3894-95a0-43fbe687d2db | -3.9668 | -48.1932 | 2024-11-09 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6b19d201-bfda-385f-ad8b-4088781f38ec | -3.9669 | -48.1716 | 2024-11-09 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| f45542f3-def3-354b-a3b4-4cb38414112d | -1.5347 | -52.1899 | 2024-11-09 06:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e1e23846-6227-3f30-9c86-faf519444ab7 | -3.6003 | -47.3614 | 2024-11-09 06:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f739179c-5acd-3e8a-b985-0bbbea4769de | -3.8036 | -44.199 | 2024-11-09 06:10:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| c30eb5e9-9fcf-38cc-a26d-f969ea206689 | -3.9854 | -48.1708 | 2024-11-09 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| dc0fd9eb-5145-3da4-8812-0530f20c6aea | 3.18495 | -64.1998 | 2024-11-09 06:12:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 726a3b8f-99e5-333f-9fe9-0444da360c08 | 3.18569 | -64.20432 | 2024-11-09 06:12:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a0a906c-31a5-3b60-ace4-9e72344cd976 | 3.18038 | -64.20067 | 2024-11-09 06:12:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2a83308-5e67-308e-86e6-dfa375f17241 | -5.13777 | -60.36806 | 2024-11-09 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bbdd8be7-b4c2-3272-b9b4-de8f963ad9e1 | -5.13859 | -60.36217 | 2024-11-09 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b7266bc5-e4c0-3732-a88f-50f6d3b2e980 | -3.9854 | -48.1708 | 2024-11-09 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e5e1c373-6785-3e71-91d4-669a56b482a7 | -3.6004 | -47.3395 | 2024-11-09 06:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| be687a09-e087-30f9-adc4-afa66457659b | -4.2486 | -47.5729 | 2024-11-09 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6e47d945-fece-3963-84dc-582a1f36094e | -3.9669 | -48.1716 | 2024-11-09 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 46eea0bc-a0a1-3c05-88ce-20f13a9fd5ab | -1.5347 | -52.1899 | 2024-11-09 06:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5e64b40c-0d0e-3195-81f9-9a170bc1a926 | -3.9668 | -48.1932 | 2024-11-09 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d215d0c8-b4ed-3342-8bd1-b54f171dfba4 | -3.1511 | -52.9731 | 2024-11-09 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 5b9b4528-bf18-3e30-ab90-c8d7dc622694 | -1.5163 | -52.1901 | 2024-11-09 06:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 13c7ebce-7fc2-39d9-9ee1-105afae58bd8 | -3.9669 | -48.1716 | 2024-11-09 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| ef2fdaf1-4f32-36b5-b2bc-daf852d282b4 | -3.6004 | -47.3395 | 2024-11-09 06:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 7b43a803-a537-30af-861c-690a45cf87cb | -3.2396 | -45.2242 | 2024-11-09 06:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d030d30c-7c7d-35f7-86fa-03cf25c11e6e | -4.2486 | -47.5729 | 2024-11-09 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 853c4c9d-99c1-3a16-9f3d-d144b5d8c35f | -1.5347 | -52.1899 | 2024-11-09 06:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| f5817601-cbf3-3151-8865-6f9b5065d087 | -3.9853 | -48.1924 | 2024-11-09 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 27575e9e-e181-37cd-bc85-dc195e12dcd5 | -3.9668 | -48.1932 | 2024-11-09 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b73eb8d0-4fd3-35b0-83a9-e621d5d120db | -3.9854 | -48.1708 | 2024-11-09 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5cc72921-3aed-3861-846a-8b22ab26dfaa | -3.8956 | -44.4005 | 2024-11-09 06:40:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 29e2771a-26f6-33b2-9b51-caf63fce2a79 | -3.9669 | -48.1716 | 2024-11-09 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 6b74754b-a2b5-3432-bbae-dcb2ebe23070 | -3.8958 | -44.3776 | 2024-11-09 06:40:00 | GOES-16 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 5645c2c1-7e49-322a-80cb-785339dc4152 | -3.6004 | -47.3395 | 2024-11-09 06:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 03c28383-f014-35a7-8d39-13dc57cd7097 | -3.9668 | -48.1932 | 2024-11-09 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 56baf599-9b38-3367-a07b-4924c5656158 | -1.5163 | -52.1901 | 2024-11-09 06:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| bf4b9443-3265-3a64-a102-abde4088434e | -2.4104 | -48.5265 | 2024-11-09 06:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| c53ebd21-9fda-3ae6-8dd2-9f8fb2247c0d | -3.2396 | -45.2242 | 2024-11-09 06:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |


[Clique aqui para ver as próximas entradas](README118.md)
