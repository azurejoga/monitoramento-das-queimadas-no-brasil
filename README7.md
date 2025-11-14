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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb9803ae-22c2-3a02-a25a-daca7e90a3cd | -15.5543 | -44.4809 | 2025-11-14 00:38:00 | METOP-C | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| bcfc71e5-7083-386d-b9b6-d7f19d6861be | -3.4804 | -45.645802 | 2025-11-14 00:38:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6e390d5-cc6c-337f-acec-89461f461adc | -9.3141 | -47.831501 | 2025-11-14 00:38:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30ee1c27-d3bc-3b75-9f13-5446fce6f457 | -3.6409 | -44.344601 | 2025-11-14 00:38:00 | METOP-C | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9a541e7-efe4-3553-969f-79b895e164b4 | -3.4543 | -50.113201 | 2025-11-14 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93e84956-1026-379d-942d-2130a0248f87 | -6.1593 | -48.0509 | 2025-11-14 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f493c6d0-6361-32bf-9e56-c77742281293 | -7.9387 | -44.3251 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8663ae-a74d-3bd0-8876-a336e040fce9 | -3.6388 | -44.335602 | 2025-11-14 00:38:00 | METOP-C | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af7ce871-9711-38de-8984-3654552cfd73 | -12.6853 | -45.4249 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7938cf3e-ae8b-340d-aaad-00d140cdb2db | -4.7067 | -46.441299 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 470ddd4a-9660-30fe-ad04-799a7650660c | -7.847 | -44.286598 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8cace2-be1c-39af-9230-fb7d3fc73726 | -11.1697 | -43.574902 | 2025-11-14 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fbe689a0-fe9c-32d1-ad03-8590e58d7e80 | -12.0725 | -48.206299 | 2025-11-14 00:38:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06aeebcd-ed0f-3d5e-b24f-162951051165 | -6.2158 | -47.2603 | 2025-11-14 00:38:00 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d97fc650-c4bf-355c-9459-e1d733914383 | -6.1578 | -48.043999 | 2025-11-14 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79eb3cbc-8617-3947-8f9c-7a29f29560ee | -7.9485 | -44.3228 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b07205d1-1d3e-3965-b448-d87a32959de4 | -12.4511 | -44.632702 | 2025-11-14 00:38:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23b6ef70-affa-351f-894a-9b9a4c67109c | -17.5431 | -44.698898 | 2025-11-14 00:38:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0a14df1b-5bf1-3e96-8197-a55c372e6856 | -11.0864 | -44.847198 | 2025-11-14 00:38:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 650ddbd3-693f-333e-9804-24f20921a80f | -9.1187 | -43.943802 | 2025-11-14 00:38:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5af131ca-d347-3eaf-be3a-7adf81f7182d | -3.7477 | -44.272499 | 2025-11-14 00:38:00 | METOP-C | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c1df56b-c8d2-3c3f-a9e0-961ac3c7eb0d | -3.4641 | -50.111099 | 2025-11-14 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62e5c567-5f8a-3265-94bc-43c6323b2403 | -2.8462 | -45.490101 | 2025-11-14 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| baae916a-ea9b-3445-a95b-9061e292f3d9 | -3.521 | -45.554199 | 2025-11-14 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2361dd4e-0718-367b-80ff-3951569746bb | -12.4885 | -47.2948 | 2025-11-14 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8fe4e74-4120-37a0-84a6-f573bee6697f | -4.047 | -46.131699 | 2025-11-14 00:38:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb998912-33f0-30b2-976f-611ab548ee16 | -11.9274 | -43.938999 | 2025-11-14 00:38:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8ca8717-7e70-33e6-95cf-5e004ee582e4 | -5.7512 | -42.717999 | 2025-11-14 00:38:00 | METOP-C | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0b1c54b5-5f80-38e6-a96e-79bdbe4907ca | -14.1384 | -44.205898 | 2025-11-14 00:38:00 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 963b568a-465a-3750-aaf3-3b69468baf02 | -4.288 | -41.810699 | 2025-11-14 00:38:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cc23cf91-317a-3a2e-98e9-0fa47c89fc05 | -7.5338 | -46.576698 | 2025-11-14 00:38:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ff54415-09a3-3539-b568-e95d3184259b | -7.342 | -46.013599 | 2025-11-14 00:38:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92608a3a-e8be-3612-9378-8ed49b034881 | -3.9509 | -47.503101 | 2025-11-14 00:38:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f6fdd29-9bca-3564-905d-95eebc1f20e0 | -12.0627 | -48.2085 | 2025-11-14 00:38:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e44217ff-7ff5-307b-97de-e5bf2386880a | -15.5499 | -43.171299 | 2025-11-14 00:38:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 6e2017ca-7cfd-39f6-9b67-1cbc2e243f28 | -7.9348 | -44.308899 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe2ae3fc-f10b-343a-9025-4ded4af67aef | -5.4909 | -47.697201 | 2025-11-14 00:38:00 | METOP-C | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d530c54e-a4b5-3af3-8f7e-1b5ff86bd93c | -9.919 | -47.865799 | 2025-11-14 00:38:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ed1f8e3-0537-3521-b0a8-0553015d59f3 | -6.1382 | -48.048401 | 2025-11-14 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e75ca92f-a92a-3b63-9a16-e4b67f4e746b | -11.8236 | -47.776402 | 2025-11-14 00:38:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0ada2d9-b978-33ab-823e-ae405ae09fd5 | -7.927 | -44.319302 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 92eb165d-38f6-3087-bf5c-39b63caa0ba6 | -7.4626 | -42.584801 | 2025-11-14 00:38:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0dca1095-1371-3a22-ba1e-586da6a31043 | -3.9156 | -44.328701 | 2025-11-14 00:38:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd1db221-6b00-3325-b9a4-b4573c1e02a3 | -4.2166 | -49.1152 | 2025-11-14 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bb624bf-21c6-3c6a-8cd8-82739f96238e | -2.7935 | -45.4851 | 2025-11-14 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90680842-1115-3622-9d6f-39eb82674588 | -8.9 | -41.066101 | 2025-11-14 00:38:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a4d6326a-53e4-3d90-9ee8-58bedcfaf424 | -17.802601 | -44.983898 | 2025-11-14 00:38:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a25fbd3a-fb03-375b-b8b7-2be351d20737 | -10.7487 | -44.550598 | 2025-11-14 00:38:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4058851d-7a53-38e4-8fd4-b930c81f4b7f | -2.375 | -48.680901 | 2025-11-14 00:38:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66186379-d42f-3b9d-8694-d2421537261a | -7.3403 | -46.0065 | 2025-11-14 00:38:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93be1c43-bf71-34ec-8ed7-e04737773add | -10.7502 | -44.910801 | 2025-11-14 00:38:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5ae812ab-da76-3687-8840-7bf019f047ad | -7.8508 | -44.302898 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ff1615b0-96c8-305d-a3d7-461b7f03515a | -12.0198 | -46.763699 | 2025-11-14 00:38:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 971d2a74-d40b-34fc-be00-12df26fb1d01 | -11.8047 | -44.252102 | 2025-11-14 00:38:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6321e2a0-3e5a-3275-ac49-89c617320353 | -12.5923 | -48.328098 | 2025-11-14 00:38:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72ed37db-0ae8-304f-ae38-dcb22806aef9 | -12.7163 | -45.425098 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 896e2f70-6b0b-3382-96f1-e195ab3cd73c | -11.9986 | -46.7612 | 2025-11-14 00:38:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce554482-78f7-3e30-9a97-d8cc8c607b7c | -6.2142 | -47.253502 | 2025-11-14 00:38:00 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0efba91b-adcf-3454-acc7-f81d905800df | -7.4479 | -42.566799 | 2025-11-14 00:38:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ca2284d1-19e7-3337-96c2-f9c8f44c84f6 | -5.3635 | -46.292198 | 2025-11-14 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8247500d-9f06-3789-bf40-c8a44814d186 | -11.8154 | -47.7859 | 2025-11-14 00:38:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b64063a-25e6-3878-be68-3238328ab8db | -9.1109 | -43.9543 | 2025-11-14 00:38:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c64dafe-4b61-38a7-b53c-c1b577f71d0c | -3.9105 | -50.0354 | 2025-11-14 00:38:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f07c0a31-fe22-3480-a21b-0a19be18518a | -7.8732 | -43.786201 | 2025-11-14 00:38:00 | METOP-C | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 85909040-a566-3d96-b977-562ef517da09 | -7.8451 | -44.2785 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b91b466c-0f7b-319d-8944-7248bdd2b3d9 | -11.0301 | -44.649899 | 2025-11-14 00:38:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94191788-662f-3301-b04c-15c4477eeb00 | -5.0213 | -44.5145 | 2025-11-14 00:38:00 | METOP-C | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3f2b7e3-a6f9-35b6-8ad7-bce2839be445 | -5.3402 | -41.862801 | 2025-11-14 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf22ca27-3951-346f-b8e2-2edc84966413 | -12.133 | -48.013802 | 2025-11-14 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74fe0d9b-c04a-3882-b18a-5a1dd2e5bad3 | -7.4674 | -42.562199 | 2025-11-14 00:38:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ba3613fe-1a60-3d7f-a82e-147f3e484914 | -10.7544 | -45.0177 | 2025-11-14 00:38:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 36052b1d-4f4d-37b2-9752-a1fbaf12711b | -7.3865 | -48.6465 | 2025-11-14 00:38:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1a5a4f-c750-3f7e-852d-4da90462a3cc | -12.0018 | -46.775101 | 2025-11-14 00:38:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb2d063a-c927-342f-8c10-fcbcde96457c | -13.0274 | -46.5257 | 2025-11-14 00:38:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a15883d-b565-331d-b708-7c1f6a484c7c | -9.3172 | -47.845501 | 2025-11-14 00:38:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98747497-3cfc-38b5-9787-6076c0c28369 | -7.6619 | -45.880001 | 2025-11-14 00:38:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b491a2ea-334a-3fbd-8b19-b2f3c0a3d3c3 | -3.4706 | -45.647999 | 2025-11-14 00:38:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da81fd13-9b5d-32d3-9204-a10e43e45d45 | -5.3373 | -41.8507 | 2025-11-14 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 906d33e3-faaf-30fe-82ac-e76f55b116ab | -4.658 | -45.475498 | 2025-11-14 00:38:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae604eca-e6e2-3f49-a6b2-796603fe17b7 | -9.8121 | -48.354801 | 2025-11-14 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3b20f83-f7bb-3331-a689-d29a5e1745c4 | -2.8364 | -45.492298 | 2025-11-14 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2f90e906-b342-3705-b02d-5d9c18444523 | -6.1676 | -48.041801 | 2025-11-14 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea15e068-817e-3d70-aec0-79cae2d93439 | -12.0426 | -49.439499 | 2025-11-14 00:38:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13bc42e4-01a9-3c71-861a-a5d7bc4b2149 | -11.8488 | -49.2066 | 2025-11-14 00:38:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8a21dcf-8ee2-33b3-b600-5048867caa68 | -8.896 | -47.895802 | 2025-11-14 00:38:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40dd65b6-b97e-3bbd-85d2-92220b943714 | -11.2707 | -42.100101 | 2025-11-14 00:38:00 | METOP-C | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 214b155a-052b-3f46-8411-e1dcf7294727 | -4.4625 | -45.389099 | 2025-11-14 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7f40ef0-8488-38d9-89ff-cab0dae9cf8f | -6.2378 | -46.236 | 2025-11-14 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9814591f-4f76-3d36-92be-24a20d28f753 | -9.3157 | -47.838501 | 2025-11-14 00:38:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8745336-4ebc-3d3b-98fc-f76cdedf2405 | -8.6327 | -46.690701 | 2025-11-14 00:38:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a675e7ac-f239-38ec-a9ef-c7b2b4d0eb43 | -11.7283 | -48.511501 | 2025-11-14 00:38:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b22b3085-0566-3a66-95f7-91fd45441b52 | -7.8859 | -44.3204 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9c2dd3a4-2398-3e0f-8853-810fb079cb1d | -12.4494 | -44.625301 | 2025-11-14 00:38:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc5f7c1a-c81a-3db9-a5f4-4a383f39486b | -12.1771 | -48.073799 | 2025-11-14 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32575f98-9e41-3f10-be98-88d131a0405b | -2.866 | -51.468498 | 2025-11-14 00:38:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba889464-93a0-3ce8-85c5-a3f2b5c36e69 | -13.6907 | -43.004398 | 2025-11-14 00:38:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2c0cc00c-955b-382d-ab33-eef0e1c9516c | -3.0112 | -49.434299 | 2025-11-14 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d66ea403-46bf-3498-a455-c166a32e857f | -2.8443 | -45.482101 | 2025-11-14 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36a3ce2e-6046-324e-b9a9-814301a3aeeb | -3.425 | -50.165798 | 2025-11-14 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4fb2074-1033-36f5-89ea-cdbdb219e6b4 | -7.0636 | -48.356899 | 2025-11-14 00:38:00 | METOP-C | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
