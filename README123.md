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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d6625cf-73c3-30bd-afa6-1301ec138611 | -14.2092 | -46.2439 | 2025-09-13 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 6a946be1-c622-3b9d-8825-d78ed541e29c | -13.9185 | -48.2105 | 2025-09-13 12:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| dad4a48e-4427-3704-b231-580d1896ae7a | -15.1359 | -52.4892 | 2025-09-13 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ea1d86d3-5e3d-3c7e-af46-2f060bbdda88 | -8.497 | -45.1369 | 2025-09-13 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 1c5ec3db-a3c8-3722-afcb-1c3ca5244062 | -15.4517 | -47.3291 | 2025-09-13 12:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 756c2c08-8559-370e-aa04-27fd333776d5 | -17.1549 | -48.4908 | 2025-09-13 12:20:00 | GOES-19 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 0c14075b-af32-3420-bd35-0f70e9b45e0d | -16.3422 | -51.5217 | 2025-09-13 12:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 40db5b22-f1ad-3885-9519-33ef6e4f3c73 | -12.8456 | -47.9236 | 2025-09-13 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 9822a601-4f08-3c65-ac3d-237f8b8cddfa | -12.8259 | -47.9486 | 2025-09-13 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 194.0 |
| d67dd843-cdb6-3aa6-8342-d8c66d04a86c | -15.8648 | -47.2322 | 2025-09-13 12:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 6ccba292-8f75-3656-aa94-65c463fb6984 | -14.4199 | -47.3238 | 2025-09-13 12:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b74d9258-12a0-389f-9451-caa2e7336fd3 | -12.8452 | -47.9459 | 2025-09-13 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 1d076c2b-6401-3cf3-9967-97e78cb4f822 | -14.1694 | -46.2965 | 2025-09-13 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 377.5 |
| ef4d2266-270b-36bf-b07c-da3c845e18db | -16.3418 | -51.5434 | 2025-09-13 12:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d0ccce2d-6dc6-398d-b9bc-4914e15be4ef | -9.2656 | -59.4191 | 2025-09-13 12:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 0be0ee3c-4d2c-3c2a-a856-f63861d83f7e | -11.1259 | -51.9309 | 2025-09-13 12:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 35ec6176-79cd-3ca1-ba84-783e5e9d3752 | -17.292 | -46.0996 | 2025-09-13 12:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 318e2e6e-9eaf-3c30-85f0-597137724592 | -15.0436 | -50.1337 | 2025-09-13 12:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 707cb6b7-1aae-3716-bf37-0dffd106c29a | -11.4119 | -50.4383 | 2025-09-13 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| e29aa5f7-fcb5-387e-aa80-04150d428779 | -12.8263 | -47.9263 | 2025-09-13 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 3bc1b13e-3d1b-3b5c-8f61-e04bbedd3da8 | -14.4204 | -47.3011 | 2025-09-13 12:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 6e5da682-af23-3caf-a6ae-359f14286688 | -10.9283 | -47.2223 | 2025-09-13 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 8a2d64e1-7cf8-3a55-9c93-db0209e6eebc | -14.29 | -46.0924 | 2025-09-13 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 214.7 |
| 2d6de8cb-3ef0-354e-aab5-298a054b8ffb | -12.9398 | -48.0213 | 2025-09-13 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 3728728f-bcf0-308e-a74c-e7c05a766ef1 | -11.7826 | -47.402 | 2025-09-13 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5db4c2ce-e713-34e3-b533-3b3e70ac2f65 | -12.9402 | -47.9991 | 2025-09-13 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 6009ada7-21e2-324b-8055-bfb66e063c13 | -14.4398 | -47.2979 | 2025-09-13 12:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 01810d63-8c46-3237-aadb-5cc07bbee550 | -9.2658 | -59.3997 | 2025-09-13 12:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 28307cd8-fa92-346b-9558-6c2c8b44b03b | -7.432 | -44.4425 | 2025-09-13 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4427c28b-a54b-3281-96d0-190ba1cb8b9c | -11.1066 | -51.9538 | 2025-09-13 12:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 30afc601-8dc4-3076-9c76-5df11ececb48 | -21.3715 | -51.1655 | 2025-09-13 12:20:00 | GOES-19 | LAVÍNIA | SÃO PAULO | Brasil | 3526506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.9 |
| 2f638b33-4af6-30e4-a738-a46ee0ae10bc | -14.4394 | -47.3206 | 2025-09-13 12:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 39f9e2f8-34c6-379d-b8e6-c197045ea536 | -11.1152 | -51.3211 | 2025-09-13 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 900b5c28-3c79-3233-9376-93ef2608248a | -15.4713 | -47.3256 | 2025-09-13 12:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5e94cbbb-66b4-3137-825d-0ed28a47b5aa | -7.4322 | -44.4194 | 2025-09-13 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 945e6655-39e1-33d0-9a2c-903f0d3f93f5 | -13.9172 | -48.2775 | 2025-09-13 12:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a25a50ef-abd7-3389-bcb4-379eba8c1585 | -19.3417 | -45.1132 | 2025-09-13 12:20:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 119.6 |
| ec58a515-df4a-38d8-af56-35bceb538b47 | -7.4511 | -44.4177 | 2025-09-13 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 0c805c7a-0736-3f0e-a6a6-e494a097c37c | -16.0796 | -49.993 | 2025-09-13 12:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0d3291a5-4324-37ac-9a83-ebb499f6da6a | -18.0065 | -46.9499 | 2025-09-13 12:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f71d4d29-6e68-3ab1-a61f-2ade66fda481 | -12.8259 | -47.9486 | 2025-09-13 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 0b8d9d37-f5f4-3bbd-a440-fbf4d6f44253 | -14.4394 | -47.3206 | 2025-09-13 12:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 1951d034-e80f-37a1-be17-192c3d28b672 | -18.0065 | -46.9499 | 2025-09-13 12:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 130.3 |
| fa2fdbed-aa58-3229-b8c3-1f17b9506d17 | -16.0796 | -49.993 | 2025-09-13 12:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| a56c842f-88af-38a2-8fa6-ed3086e074fc | -15.1554 | -52.4865 | 2025-09-13 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b476b24c-9107-39fd-907b-5a6e964d9d4a | -15.4713 | -47.3256 | 2025-09-13 12:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9e325c1e-d0d7-3ae7-b56b-fbe1e5e77c8f | -13.2609 | -51.7122 | 2025-09-13 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| cb674bf2-443f-3212-a522-1ed8df322a49 | -13.8979 | -48.2804 | 2025-09-13 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 11188151-c9ad-35bf-9211-2c36c21dd4e8 | -11.1152 | -51.3211 | 2025-09-13 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| c0f66c4a-220f-3c98-b676-7e0508a874a9 | -14.2097 | -46.2209 | 2025-09-13 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| ffb4ee8b-9323-3ae7-990a-7afc5a005fad | -19.3417 | -45.1132 | 2025-09-13 12:30:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 145.9 |
| bb123c87-c467-3994-a0f4-6c5dcc3c34e3 | -11.7763 | -51.5038 | 2025-09-13 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| faf72a88-c453-3499-a018-d6ff19f25d04 | -12.1236 | -47.579 | 2025-09-13 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 070fe54e-35ca-3c1c-86df-f51069c8cf53 | -12.8452 | -47.9459 | 2025-09-13 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| eb3f1f7f-3ff7-327c-b038-c0f055d2a6dd | -13.9185 | -48.2105 | 2025-09-13 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b47a0fbc-66c0-32bc-bb02-375e07df4e86 | -14.31 | -46.066 | 2025-09-13 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 670eb39b-1814-3540-8e53-e1517993e7aa | -9.2658 | -59.3997 | 2025-09-13 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 881595f6-16bb-3ddd-86d8-a131b24792c8 | -11.7208 | -46.5353 | 2025-09-13 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| ae028d12-e080-3f3c-8271-6e0ce443605a | -14.4204 | -47.3011 | 2025-09-13 12:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 212.0 |
| c69d69a0-a424-3ec0-87a1-a490f28a6859 | -8.497 | -45.1369 | 2025-09-13 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 214.1 |
| 4e57f445-3f50-3774-bb00-47ad6a4c1db9 | -9.2656 | -59.4191 | 2025-09-13 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 05ca49e0-2b19-3491-a565-e8fcf823d73b | -12.9398 | -48.0213 | 2025-09-13 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 53a2f8c5-fa7f-3579-9a83-e1175b982386 | -16.0595 | -50.0183 | 2025-09-13 12:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 141ae9b6-7b17-3bc2-b7f3-c2a9f708cb21 | -14.4199 | -47.3238 | 2025-09-13 12:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 3f24427c-3b36-3a78-9953-73e156d20bb4 | -15.0436 | -50.1337 | 2025-09-13 12:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| cff25f59-41d7-3938-8374-806c7af81309 | -11.7826 | -47.402 | 2025-09-13 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 57f3dc19-5a36-3954-96e4-48eba7eb4154 | -16.4906 | -55.1276 | 2025-09-13 12:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| c0bcae12-6e52-36df-9a8f-6caef5c669b1 | -7.4322 | -44.4194 | 2025-09-13 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 375a4230-81ae-3f7e-a90e-858ef2e9eabc | -11.7204 | -46.5579 | 2025-09-13 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 5798c0be-db94-3aaa-a649-dc160d172147 | -15.1169 | -52.4705 | 2025-09-13 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 956a4705-28e4-3f22-9a34-0a09c2b27cd8 | -11.4119 | -50.4383 | 2025-09-13 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b1991264-752d-3fc4-a5e3-bf68856374ef | -11.7391 | -46.5779 | 2025-09-13 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| fe34cac1-53c1-309d-9383-4763bdd26bee | -13.2801 | -51.7099 | 2025-09-13 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e34df414-3304-334c-ab6a-fbd5b302f792 | -11.7573 | -51.5059 | 2025-09-13 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c7de4d57-299e-308b-9213-61a2d1678db9 | -14.4398 | -47.2979 | 2025-09-13 12:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 254.1 |
| 32610db6-3dd4-3a2a-9e92-e36063a413bd | -10.1072 | -59.1564 | 2025-09-13 12:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 4c2dbff1-3537-3b97-8898-f009924b9d35 | -15.1359 | -52.4892 | 2025-09-13 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 145.5 |
| ddcc298f-15e0-3d79-bc96-a96cc3f4cef6 | -14.29 | -46.0924 | 2025-09-13 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 136.3 |
| a76424d2-e0be-3877-9910-8edf31dac02d | -11.1256 | -51.9519 | 2025-09-13 12:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| d0dbef5a-462c-3219-9c23-a194af350782 | -11.776 | -51.525 | 2025-09-13 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 868b89a7-c297-3947-9211-f569e1d174d4 | -15.4517 | -47.3291 | 2025-09-13 12:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| ffdabf78-ebf0-3c83-9849-f3ab55748764 | -21.3715 | -51.1655 | 2025-09-13 12:30:00 | GOES-19 | LAVÍNIA | SÃO PAULO | Brasil | 3526506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 170.1 |
| 02437196-4db5-3149-a8e2-029eeb0b65eb | -14.2092 | -46.2439 | 2025-09-13 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 18436a77-43b5-3dbc-9560-be43d7824acf | -11.1066 | -51.9538 | 2025-09-13 12:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 84ab1008-a0fd-3344-a734-ac5f5ab53b04 | -13.9172 | -48.2775 | 2025-09-13 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 2e8c63a2-373c-3967-a253-5b9941ee411d | -13.203 | -51.7406 | 2025-09-13 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 02e23892-6cb0-3752-b9fc-de689a3b2af6 | -12.8456 | -47.9236 | 2025-09-13 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 94fdd28b-ac39-3244-9beb-cf485ecfae3e | -8.5159 | -45.1349 | 2025-09-13 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 0a59fb61-7f1e-38ee-906e-e62529d2227e | -8.4967 | -45.1597 | 2025-09-13 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| ae37bdf1-0211-3872-bf4d-8d8b97bad760 | -15.1363 | -52.4679 | 2025-09-13 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 7f94b415-4da6-3df9-b79c-ea498e1419ed | -11.1259 | -51.9309 | 2025-09-13 12:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| ac03c909-3e2b-3cee-a198-d1a2afe2e776 | -15.1748 | -52.4839 | 2025-09-13 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 51c20924-a517-36f0-a021-a1732c92d2ed | -12.9402 | -47.9991 | 2025-09-13 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 90e91e67-78c9-39df-8cee-26bc6ab80c88 | -13.9168 | -48.2998 | 2025-09-13 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 9bb3e4a6-f81e-3d38-803e-ceda77ef3c15 | -15.8648 | -47.2322 | 2025-09-13 12:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 5bcf55b7-ef4f-3c95-9570-8969d1da533d | -12.1044 | -47.5816 | 2025-09-13 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 3511e6ec-e438-31f9-85e2-66e8600129b2 | -12.8263 | -47.9263 | 2025-09-13 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 156.7 |
| bc339bda-a909-3982-903e-b34f0e0d9a93 | -14.1694 | -46.2965 | 2025-09-13 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 254.1 |
| 262cdf67-d9d0-30a8-b248-dbe02fa6c409 | -19.3417 | -45.1132 | 2025-09-13 12:40:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 138.2 |
| bfd91491-7fa1-391f-8d23-786091ed5179 | -13.9172 | -48.2775 | 2025-09-13 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |


[Clique aqui para ver as próximas entradas](README124.md)
