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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e48b5508-7d0f-3827-b5e7-31ff67df276c | -4.0477 | -54.2394 | 2026-10-01 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a5fe3c01-8430-3f21-895a-9751b6e4cf96 | -11.81 | -50.4999 | 2026-10-01 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 84234b16-18df-31d4-9acc-9e5247d42052 | -9.1407 | -64.4024 | 2026-10-01 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 3890722b-f516-312c-aace-7dae56fa1b69 | -5.7376 | -45.1533 | 2026-10-01 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| dabf3ab4-2647-3328-85fc-7ecc26aa479c | -5.9993 | -49.566 | 2026-10-01 00:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 92e5231d-351a-361b-b32b-3c55d8a09ad3 | -8.5738 | -66.994 | 2026-10-01 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 0e8c88a3-a7dd-3e8d-b591-0a7c8454a4af | -7.1078 | -43.1732 | 2026-10-01 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 218.3 |
| 1c223659-ca03-3805-91e1-24c21f2d5c06 | -12.1857 | -48.4345 | 2026-10-01 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 608375f4-1f9a-3ee9-9d93-e13d9542d22f | -3.5624 | -51.4631 | 2026-10-01 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 33371138-f6a3-3d93-8ce1-9099788b9375 | -3.1245 | -50.268 | 2026-10-01 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 0ce08807-c80e-34fc-822e-e2d7ef801d21 | -3.1842 | -60.0607 | 2026-10-01 00:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e6f02a03-45f1-3cbf-9802-4ca0e766a707 | -9.1222 | -64.3843 | 2026-10-01 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 145.6 |
| f10313dc-3936-3b80-adea-a782cf555e4c | -11.791 | -50.5021 | 2026-10-01 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f6c6eeeb-4b00-30dc-9406-feaf9e0f33c3 | -6.2797 | -43.2711 | 2026-10-01 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4fb0b959-0904-3d02-9e79-ce069b17447d | -2.908 | -54.151 | 2026-10-01 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 108519bc-f70d-3c88-be15-b2c4c880a013 | -3.0192 | -53.887 | 2026-10-01 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 9c3ff267-8c9e-3518-98da-bdc5f716686f | -3.5809 | -51.4625 | 2026-10-01 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| d0741644-e84f-34e2-acde-f26b72e6f441 | -9.1221 | -64.4031 | 2026-10-01 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 20efc509-5439-3e9a-af2e-bfb8a8fe9b03 | -13.6479 | -53.9336 | 2026-10-01 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 1d108aff-efc6-31ea-b38e-2c4a15128485 | -3.1245 | -50.289 | 2026-10-01 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| e2e9a4dd-b611-3abf-8a40-5196a3e6b3ff | -5.7561 | -45.1747 | 2026-10-01 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| ae8abb0d-2e41-357f-a8e1-d81c956bec72 | -5.7355 | -43.2916 | 2026-10-01 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 13c061db-8ab9-3061-a29c-7aa856edee14 | -3.106 | -50.2896 | 2026-10-01 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| a1539d87-7ca4-3d7f-a3d9-95afe49f6d43 | -7.1269 | -43.1479 | 2026-10-01 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 453.7 |
| e79a1356-0cb2-3098-9f5e-b7251ba46375 | -21.18195 | -47.01247 | 2026-10-01 00:13:00 | TERRA_M-M | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 420c0ba4-a1c7-3f62-b913-3805b60493cd | -23.00055 | -48.62603 | 2026-10-01 00:13:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 56d766a4-7f10-3754-a507-c3abfbbcd86f | -18.84748 | -42.58107 | 2026-10-01 00:13:00 | TERRA_M-M | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.2 |
| c70cbdb0-30c6-3a15-989d-423a84fbd87d | -21.19386 | -48.27242 | 2026-10-01 00:13:00 | TERRA_M-M | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 01a585e5-25d3-3c48-9dcb-9ad5680d8092 | -21.1717 | -47.01469 | 2026-10-01 00:13:00 | TERRA_M-M | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3d82beed-c904-35ba-8b1e-22e992b9e6d4 | -20.89597 | -47.41317 | 2026-10-01 00:13:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 13182e08-4b6a-3a69-9bc4-e4f0122b7197 | -21.71247 | -47.12617 | 2026-10-01 00:13:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 848d431a-7fc3-3e71-842c-bafa97e0eeab | -18.86016 | -42.57249 | 2026-10-01 00:13:00 | TERRA_M-M | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.7 |
| 872cbaab-4d0c-3dcd-a818-f85be659b143 | -18.8744 | -43.82267 | 2026-10-01 00:13:00 | TERRA_M-M | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 7329795c-481a-3467-90bb-6034bee9586b | -21.71451 | -47.13882 | 2026-10-01 00:13:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 1c558ecf-5ad6-3528-a5cc-1cc973d638ce | -18.86673 | -43.8187 | 2026-10-01 00:13:00 | TERRA_M-M | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0d35ddf4-93b4-33cc-a46d-2b924c4de806 | -18.84194 | -42.55115 | 2026-10-01 00:13:00 | TERRA_M-M | GONZAGA | MINAS GERAIS | Brasil | 3127503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 8993d328-e2db-3df2-8ae5-9468d0852e4c | -18.84537 | -42.57652 | 2026-10-01 00:13:00 | TERRA_M-M | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 3f04789c-3ee0-39ac-8379-74ace4643b85 | -22.08947 | -46.97702 | 2026-10-01 00:13:00 | TERRA_M-M | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3843ad99-3b43-34a2-9487-e7c9d303d4bc | -22.999 | -48.61562 | 2026-10-01 00:13:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06961f2a-153a-3f4c-8eec-3a0f3a94847c | -3.2 | -54.07 | 2026-10-01 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3479ee0c-bc57-3e60-a2e5-3b415e5e6c21 | -11.45 | -43.49 | 2026-10-01 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7571cc77-fc20-3210-90e6-92aecd4b7eaa | -4.26 | -50.86 | 2026-10-01 00:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e750c19-f44c-3155-93ed-4b1f9cb9b888 | -11.45 | -43.44 | 2026-10-01 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d879354b-79e2-38aa-828d-75b71943b7c6 | -11.44 | -43.4 | 2026-10-01 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30a27cf9-cbd4-31bf-9060-bd5cf765c253 | -4.23 | -50.75 | 2026-10-01 00:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f331930-8ef0-3847-86a1-10c3ff9f293e | -10.77 | -50.52 | 2026-10-01 00:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b10e150d-ae95-3844-b96b-573d5db8a0d2 | -11.42 | -43.43 | 2026-10-01 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a749d951-f081-316c-be1d-7937bfb6836a | -11.41 | -43.39 | 2026-10-01 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d41fa446-71ac-3c22-95cc-cd07662d0f02 | -4.29 | -50.7 | 2026-10-01 00:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfe32bd2-43fe-3f8a-887a-e0be4425b78c | -4.26 | -50.7 | 2026-10-01 00:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb997d84-3c3a-3d79-8ad7-58c9a3bb49ad | -4.29 | -50.81 | 2026-10-01 00:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1278bec3-f1df-37ef-a3b6-ae7725571718 | -4.26 | -50.81 | 2026-10-01 00:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a907b1e5-2517-3b5f-b87d-b39fea54c508 | -4.26 | -50.75 | 2026-10-01 00:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 096da8ed-f71b-338c-91f5-07e2c724089e | -3.56 | -51.45 | 2026-10-01 00:15:00 | MSG-03 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6180460-da48-3776-83b1-78fea7b67e5d | -3.17 | -54.12 | 2026-10-01 00:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd11a8d1-32fc-31fb-bb35-68ad9e6e631a | -4.29 | -50.76 | 2026-10-01 00:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d42e6866-93ba-3d2f-9ca8-93bdfeb3991c | -4.32 | -50.76 | 2026-10-01 00:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e416c594-dca0-3ef2-ae05-1f45a24300c1 | -11.48 | -43.45 | 2026-10-01 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad1595b8-357a-3638-807a-31e56d9e09ba | -3.17 | -54.06 | 2026-10-01 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f36e3ac-8efb-3bb6-8579-5c2fa6dfbcf9 | -17.1209 | -52.12408 | 2026-10-01 00:16:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a6b8628-5bf0-3c42-9870-d63134cc3b1f | -18.48148 | -50.77768 | 2026-10-01 00:16:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2d8857a4-12f4-3306-be07-553e8f689481 | -15.93912 | -56.34395 | 2026-10-01 00:16:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 751bf515-6d42-3a0a-9029-9e450ba01a3a | -15.21436 | -46.14052 | 2026-10-01 00:16:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 21c45a60-6982-32a3-9e08-5aadaa8e378e | -14.8601 | -42.1576 | 2026-10-01 00:16:00 | TERRA_M-M | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 41.2 |
| 571b9314-7d70-3922-99d7-79399ceea845 | -16.53677 | -50.52481 | 2026-10-01 00:16:00 | TERRA_M-M | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 167d1632-20e9-31fc-8c0f-0a9274f2f462 | -15.50128 | -46.12737 | 2026-10-01 00:16:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 4d80a467-9219-363e-b035-bb196dc76b48 | -15.49503 | -46.14107 | 2026-10-01 00:16:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 81c50bce-9be9-32c1-9529-b222fb8b5e09 | -15.63769 | -43.24282 | 2026-10-01 00:16:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 4cb7c22c-5c34-3089-bd24-0dd538f0e8d2 | -17.57641 | -43.70413 | 2026-10-01 00:16:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 34.4 |
| eac66d45-f36f-31f9-af9a-a4030c2c4dfa | -15.94342 | -56.33758 | 2026-10-01 00:16:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7e3237ce-15f1-309c-b000-dc6c8c6ed9a8 | -18.05433 | -51.14404 | 2026-10-01 00:16:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 1f0e756b-1362-3641-9901-5c828e508f7d | -15.50717 | -46.13832 | 2026-10-01 00:16:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 04f6cfb7-b0cd-3739-a0cd-d9696a246d43 | -17.92578 | -45.02704 | 2026-10-01 00:16:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 1ec459b8-526d-39cd-9da3-711c6491be03 | -15.21734 | -46.15863 | 2026-10-01 00:16:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a4025640-e3f7-3d36-af3b-ad0f383ee8e6 | -16.72019 | -50.71024 | 2026-10-01 00:16:00 | TERRA_M-M | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 24552345-b52b-38ed-a2bb-ace97c379a23 | -15.44364 | -45.69344 | 2026-10-01 00:16:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6b376329-c5cb-3acd-a4ac-4b4343b9cd90 | -15.94499 | -56.35114 | 2026-10-01 00:16:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 8d7fd846-bf13-3fe7-90ea-eb1502e89958 | -14.85608 | -42.16363 | 2026-10-01 00:16:00 | TERRA_M-M | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 9e0fb247-4d2d-3028-a613-78a2c8de10f4 | -15.22961 | -46.1563 | 2026-10-01 00:16:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 761e58a5-bcc5-3f26-8752-90504bd8d3ab | -17.221 | -46.85008 | 2026-10-01 00:16:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| e625af6e-b083-3781-91a2-dc52fd7c9b6e | -15.50424 | -46.14541 | 2026-10-01 00:16:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 5e1ee8b0-aa12-325b-85ce-a509fc098515 | -17.5656 | -43.70187 | 2026-10-01 00:16:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 4c3897a2-5ffe-303e-8d1a-eb11e0318c71 | -17.29716 | -52.06639 | 2026-10-01 00:16:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6ba76e95-51d7-3700-8c79-71fc1991728d | -15.22674 | -46.13874 | 2026-10-01 00:16:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e2451a37-b4d4-3648-840f-024f1ecd73d1 | -16.7783 | -50.53769 | 2026-10-01 00:16:00 | TERRA_M-M | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 37fcde04-8ca8-33c3-a943-8130c33e6b73 | -15.23222 | -46.15088 | 2026-10-01 00:16:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 7da56e50-2b12-3279-bafc-6ced4b6fe16e | -18.98091 | -53.0327 | 2026-10-01 00:16:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 0d9a5165-1d68-34a3-8dc5-6a594d46f01e | -18.98219 | -53.04258 | 2026-10-01 00:16:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| cc6b0ba8-b2a0-3c9f-ac4d-8925ac37565e | -18.97182 | -53.03402 | 2026-10-01 00:16:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0bdef87a-d1df-3713-9685-baa5e76a8dcc | -10.33239 | -47.7976 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9729294b-06ed-3dbb-aa76-1e2246920a19 | -11.26075 | -54.8193 | 2026-10-01 00:18:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f437c65b-e82d-337e-9d85-6060fc015676 | -7.88911 | -54.72881 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 91318d15-443e-318e-b6a8-7581e62a74b1 | -11.82389 | -50.51859 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b50578fe-56c4-30fa-b932-dc4a685704e9 | -13.07741 | -51.2193 | 2026-10-01 00:18:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 38c01362-9505-3864-b239-81da3786fb73 | -10.78322 | -50.53997 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a7b043e6-5441-3c20-8e0a-e74062bc40b1 | -11.86456 | -50.59813 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f9620753-9d5a-3a40-afd4-1338ea503184 | -11.82875 | -49.51533 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0dcf2204-d9eb-33fc-8849-36ba18011767 | -7.83988 | -45.82149 | 2026-10-01 00:18:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 70cfed8a-99f1-302b-90a0-86e9968e999d | -8.16089 | -54.82944 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bc6faf8f-571a-37da-9c56-8cdca0c87012 | -12.64313 | -47.64085 | 2026-10-01 00:18:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |


[Clique aqui para ver as próximas entradas](README3.md)
