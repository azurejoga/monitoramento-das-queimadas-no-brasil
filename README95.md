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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7842e324-2bc7-3199-ad41-0274a37191b5 | -22.54159 | -48.81149 | 2024-10-09 04:17:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74c54d8b-8e3e-30b2-b05c-78d1875e0e9f | -18.11155 | -56.39967 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b1de9d74-b484-305c-a8d7-a14f428ae3f0 | -18.10995 | -56.39153 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ad53141e-6cc2-3cfa-8c2f-c356e5668a44 | -10.75882 | -47.91817 | 2024-10-09 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8586af19-f938-32e9-bfa5-6742332b848e | -9.40839 | -47.87645 | 2024-10-09 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa607274-10b7-38d7-986f-34870092719b | -9.40544 | -47.87103 | 2024-10-09 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f70ec26-342a-3930-8d06-b2a509b6864f | -9.21247 | -47.95414 | 2024-10-09 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4f47893c-c283-3934-b3ab-f189ca5f4f3e | -9.18537 | -47.69694 | 2024-10-09 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51c07136-ff7e-313d-bc43-d11d1c5b2e6e | -8.98931 | -47.73232 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b3d2b75-d692-386f-aa86-47764cd3be90 | -8.91578 | -47.91528 | 2024-10-09 04:17:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7db9888-6be1-36db-a29d-1b9c1997a7c1 | -9.72776 | -48.88528 | 2024-10-09 04:17:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ead151f-77ed-3596-b136-6cab0810f06c | -9.72374 | -48.88473 | 2024-10-09 04:17:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a15420a4-0f15-3212-be5a-37c9ae8f533c | -9.61839 | -48.69666 | 2024-10-09 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2b8e614-f969-3e49-a5bd-e8f28c8f223d | -9.47947 | -48.79963 | 2024-10-09 04:17:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 751a3f97-c5ae-326a-8c8d-38df74c50df4 | -9.35028 | -48.68991 | 2024-10-09 04:17:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23dd21f8-0a01-36f0-b472-e3f618c0a405 | -9.92444 | -47.72069 | 2024-10-09 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4528dfea-fb4f-36cc-83ff-257e69c122a9 | -10.75961 | -47.91351 | 2024-10-09 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c6f4d2d-5b87-3589-bca3-86fb213468fb | -10.49659 | -47.53299 | 2024-10-09 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1941b8f6-7931-3283-a8c6-6e52c93451fc | -10.23459 | -47.50431 | 2024-10-09 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7893ed14-460c-30e5-b419-16a19eba79c5 | -10.12789 | -48.71214 | 2024-10-09 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34db5e84-0ec8-3384-afaf-85cea81ece00 | -10.01171 | -48.84675 | 2024-10-09 04:17:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c122669-43d6-3437-b9f1-64a5671325ea | -10.01112 | -48.85014 | 2024-10-09 04:17:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3f0b78a0-c255-3bc1-965f-c7aca1aee96b | -12.003 | -48.63218 | 2024-10-09 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 181ee93c-cfdc-35f1-babe-1ffb44735227 | -11.91618 | -48.29826 | 2024-10-09 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a55552fb-8d0e-3f7a-a711-587d7817a41c | -11.91245 | -48.29757 | 2024-10-09 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91a9526c-45aa-3bd4-90ed-f6e4624ccfbb | -11.73767 | -48.41162 | 2024-10-09 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa4fb98b-43b4-3773-89f7-006643de038b | -11.73687 | -48.41629 | 2024-10-09 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d2f4be0-a0fa-382a-b766-ddb0a95ad2bc | -11.45197 | -47.90966 | 2024-10-09 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddac5c2b-15d7-37ad-a7c9-886328cb30c9 | -11.45132 | -47.9078 | 2024-10-09 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 787e4fd4-ffac-36d2-81c1-e8c849379a42 | -11.13842 | -48.63369 | 2024-10-09 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c830fffc-03e1-307a-87bf-f24ce0b06293 | -11.13757 | -48.63858 | 2024-10-09 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7643442b-0fe7-3f02-bc05-12f3c3e06357 | -11.13456 | -48.63301 | 2024-10-09 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba3494cc-8ce1-3c89-aa09-e84efb252c9a | -11.13371 | -48.63791 | 2024-10-09 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0f18102-efea-3b23-baca-6b5c6feb57d1 | -11.13071 | -48.63234 | 2024-10-09 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efca640c-3aa3-3b98-a319-046e629221ab | -11.04979 | -48.42566 | 2024-10-09 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d8acb4c-b168-3b0f-98af-a7dcfe35f9a6 | -10.97245 | -48.53898 | 2024-10-09 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad94b299-c747-3efc-b1ed-fa07afd4dbd5 | -10.89788 | -49.13993 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a459819-e53c-3bf5-9cc1-716663a04a60 | -10.89727 | -49.14347 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03c69fda-9026-3106-baa6-3fb332b45b20 | -10.8939 | -49.13915 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebe2a4f7-99bb-31fa-8eb6-8ca02b811e27 | -13.62451 | -48.48215 | 2024-10-09 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9abd067e-8a8a-3a70-9669-c5bb1adf9257 | -13.62375 | -48.48666 | 2024-10-09 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 720e0e14-2ca0-3a19-a06c-1fcfdf0bb168 | -13.14296 | -48.59165 | 2024-10-09 04:17:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6378604-56af-311d-8312-312551704676 | -13.1057 | -48.76264 | 2024-10-09 04:17:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bee06db-9641-3b9d-b1fe-22a7ad99f37c | -12.72867 | -48.42085 | 2024-10-09 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e29d144f-1aa8-3381-8fa9-c603c6d5e8f6 | -12.72789 | -48.42536 | 2024-10-09 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5a7dc2e5-5c0b-300d-bc0b-047d7dc11998 | -12.72416 | -48.42476 | 2024-10-09 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d20ea22-5971-39c0-a57d-ec0171f5638f | -14.7824 | -48.52673 | 2024-10-09 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39ceed41-405e-3588-a8e8-3aabaf5b1189 | -14.5594 | -49.84598 | 2024-10-09 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eebf5291-c3f1-3e88-b488-688f7b23b811 | -14.49404 | -49.26929 | 2024-10-09 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 67491019-8253-35e3-9cf6-22db226c7d35 | -14.24841 | -49.22473 | 2024-10-09 04:17:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbdc1dad-259f-3c40-86c5-04ed4d00aec3 | -14.15165 | -49.68572 | 2024-10-09 04:17:00 | NOAA-21 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e7c7703-20f9-326b-8fa3-141901a2a928 | -14.05435 | -49.41475 | 2024-10-09 04:17:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77d83a5d-2d34-32ba-a7a1-d405f24ffa3f | -14.39045 | -48.48797 | 2024-10-09 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02112278-9f6e-37dd-bb25-66767d83eca4 | -14.79592 | -49.98796 | 2024-10-09 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd58665d-9726-3f9e-b0bb-243098e7bc48 | -15.54599 | -49.81799 | 2024-10-09 04:17:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ded7e95f-7402-3d03-a88e-95c473760b7c | -15.5451 | -49.82298 | 2024-10-09 04:17:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 655b5974-2999-3f0e-b364-f8f2b2eb44d9 | -15.54122 | -49.82229 | 2024-10-09 04:17:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb672339-8fcc-36e6-9631-b3d1d9812ce5 | -20.56805 | -50.11204 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 486bb08d-5ea5-3095-b0a8-648b26857dca | -20.56516 | -50.10889 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0917bfd1-e3ae-36e0-8b35-e99191425198 | -20.5644 | -50.11131 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a6d8e676-391a-3679-a415-90cabed2445d | -20.56435 | -50.11351 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 19c83746-e31a-3bbd-8ce9-efc165557371 | -20.56354 | -50.11814 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b289c421-0914-3969-9fa2-0af34f381c5e | -20.56192 | -50.12736 | 2024-10-09 04:17:00 | NOAA-21 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6fa32821-f5b8-3158-86d9-045116c9443c | -20.56189 | -50.12514 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8a249216-9275-3e47-a4b1-a6293c9ea2ab | -20.56105 | -50.12974 | 2024-10-09 04:17:00 | NOAA-21 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 837fb0b2-5039-3919-af1b-85eafa70548c | -20.56075 | -50.11058 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 14e9dfd7-bb8f-3fa9-aeed-fea50e4da54f | -20.5607 | -50.11278 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 959380d9-c5c4-3609-a732-b5a8b1b93c2d | -20.55827 | -50.12663 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ad65a07e-563b-3009-806e-cb9114cafdd2 | -20.5574 | -50.12901 | 2024-10-09 04:17:00 | NOAA-21 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 22d9c2bc-fe8e-33e5-8ca1-ca2ef8bbed58 | -20.55624 | -50.11666 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32fe2ede-e5c1-30cf-bf32-12f1053d2002 | -20.55543 | -50.11906 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9a479506-be13-3d97-82d5-a8ace5126954 | -20.55258 | -50.11594 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cc1a1342-014c-3383-9f78-9eef111a712e | -20.55177 | -50.12054 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c583bbb3-38dc-3f06-90cc-165e018cd4e2 | -20.54893 | -50.11521 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d606fd10-d745-309b-aeaa-bca81de0d291 | -20.54811 | -50.11983 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 712bae66-884b-3c8b-97ee-d630d662b8d7 | -20.54609 | -50.10985 | 2024-10-09 04:17:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ca74ac84-bb00-3ee6-997b-b62f09d7b8ad | -19.81657 | -49.67878 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e317231b-1d19-3ad4-8b5d-490cbd19ae94 | -19.81296 | -49.67805 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a83b191b-21b0-3ebe-bc68-2cbdc7bcc923 | -21.28777 | -51.04119 | 2024-10-09 04:17:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 9c7de1af-c89f-3ccb-ae11-0ac45b276ab7 | -21.28397 | -51.04043 | 2024-10-09 04:17:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 14b7da35-64c2-3e13-b4df-24dd997a3aa2 | -21.28304 | -51.04544 | 2024-10-09 04:17:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 8841fe07-4336-3993-8a05-547567b43ea6 | -21.27924 | -51.04469 | 2024-10-09 04:17:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.6 |
| 7471aa63-7606-358f-84bd-149d7c0e2dbd | -9.44352 | -48.88773 | 2024-10-09 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a13b7e60-2bd0-3c09-a780-5439b554a8e7 | -9.44289 | -48.89135 | 2024-10-09 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb054279-5d75-39b4-bc9f-5aeb7302c2b9 | -9.34028 | -49.84959 | 2024-10-09 04:17:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebf3cc71-7b73-3343-a2fb-8fa0e8ce1eda | -9.12234 | -50.29429 | 2024-10-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| b38d5cf3-b2ef-326a-9f9b-04e953fad69c | -9.12156 | -50.29873 | 2024-10-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 73e1beb6-f6f4-3e36-89e3-fb4cc352f698 | -9.11791 | -50.2935 | 2024-10-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| c6c4d918-068f-35b0-ac48-9740daca1a5d | -9.11713 | -50.29793 | 2024-10-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7444ea35-2344-3afd-b3a3-47348331136d | -8.74567 | -49.56583 | 2024-10-09 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eca0851f-6e13-374b-a2e3-e719bbb16e7c | -8.74498 | -49.56984 | 2024-10-09 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a8f7760-209b-315a-8e82-39c73f7a6d7b | -8.60067 | -48.84502 | 2024-10-09 04:17:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39303dc6-73b9-37c3-b25e-f0e589668704 | -8.5261 | -50.02725 | 2024-10-09 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73891eaf-0c0e-3aba-8dbb-84fa8226a221 | -8.52168 | -50.02657 | 2024-10-09 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f013da62-231d-3114-922d-f7c15eb0ea51 | -9.86316 | -49.17022 | 2024-10-09 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f75cbe59-ecd1-302f-869e-ea03fd78d0c3 | -10.54081 | -49.46083 | 2024-10-09 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1aedf07b-61b6-359f-9f1c-e84fc48f6012 | -10.54015 | -49.46455 | 2024-10-09 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75cff32e-5c5b-3d1a-8797-15c4fecd92fc | -10.52707 | -49.10952 | 2024-10-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b6674606-9c5d-3ed2-b1a6-beb99bb89bb1 | -10.5237 | -49.10516 | 2024-10-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 26d04681-b67e-329a-ae4d-21af04cbaedd | -10.52307 | -49.10876 | 2024-10-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README96.md)
