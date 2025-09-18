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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dd95138-ce02-3534-8a99-0a8adb3838da | -10.0374 | -47.1729 | 2025-09-18 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 63345e44-a9b7-3a3d-bb70-04b45b150278 | -8.9911 | -46.3059 | 2025-09-18 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 01d2e034-c631-3416-bc2a-dc907d64fd8d | -8.9536 | -46.2874 | 2025-09-18 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 43334a0b-3486-3b3f-acc0-07e14e75596f | -8.9516 | -45.019 | 2025-09-18 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e4819919-3232-34e7-bf31-322f78ef538b | -8.0005 | -45.6864 | 2025-09-18 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 73f4b04e-4fdc-376e-962a-f677c65bb361 | -6.3967 | -42.8388 | 2025-09-18 14:20:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| f21727f1-d1ee-32b8-bb96-1b4491821f38 | -5.8807 | -45.8865 | 2025-09-18 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| da30394e-ad7e-37ab-a1b7-fcd5eba15e2a | -5.862 | -45.8878 | 2025-09-18 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| bce15175-1e0a-30e8-b4f4-b93779ba285f | -17.732 | -46.7756 | 2025-09-18 14:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 609c7b98-6005-3ba4-bd4f-144e0fc43f08 | -5.6638 | -45.0452 | 2025-09-18 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| eb737f30-3c7e-3fc6-8b52-18f0cbef5134 | -15.8233 | -59.4016 | 2025-09-18 14:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 0376e6c5-8afd-35b6-99ce-20340d6e9530 | -6.16 | -46.0007 | 2025-09-18 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8478634a-fec0-36a3-acdd-44a5d7ae9f45 | -7.5084 | -44.3431 | 2025-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 729fc93f-c03f-33f6-b0a6-8b118ff4305f | -6.0071 | -44.3124 | 2025-09-18 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 3ea38d18-3aa6-31f5-a17f-899537d21325 | -6.1252 | -47.8355 | 2025-09-18 14:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ff23fa89-a331-3719-97cd-f7bd533c78db | -8.9539 | -46.265 | 2025-09-18 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 1ccb480c-29c1-3398-be29-3c73e7e8891a | -10.0371 | -47.1952 | 2025-09-18 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 11ca8652-12e1-316e-b148-695baa7808d3 | -3.7655 | -44.3383 | 2025-09-18 14:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 4efd044c-2e14-3892-85d6-3359ec9b4585 | -6.1438 | -47.8342 | 2025-09-18 14:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| cc6b9f15-ffb0-3fe5-bace-81fd9b270c4b | -8.669 | -46.4291 | 2025-09-18 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4e29b71c-afbc-31f0-bb6e-c9f747f852e9 | -5.8809 | -45.8641 | 2025-09-18 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 919274c8-62a2-3de9-8147-ed0377a21599 | -7.8509 | -45.6105 | 2025-09-18 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 02a1bfc6-c56c-326d-b22f-e8943bc512b9 | -6.9981 | -44.5971 | 2025-09-18 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c75f6e05-7f5b-3109-b48d-e2fca3ce3ac1 | -8.8801 | -46.138 | 2025-09-18 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 8ff45983-9de6-352a-90ac-40717bf5f45b | -10.6334 | -44.2324 | 2025-09-18 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 2d314cab-2074-3d3e-a64a-cd374d5931aa | -6.0786 | -44.6733 | 2025-09-18 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| cdb1fc11-b6b5-3681-af8e-cd742abaeeb4 | -8.899 | -46.136 | 2025-09-18 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 40fd2902-44d2-3727-8cf7-b24f36827fd3 | -7.5818 | -44.4971 | 2025-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 4f5c4ad0-b10c-3f4e-ab25-5092c3168526 | -6.921 | -44.7869 | 2025-09-18 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c51cfa37-808a-3d00-bcc0-f24561a456e7 | -8.7073 | -46.3804 | 2025-09-18 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 920c023c-3eb3-35fd-b746-49f461d82b5b | -6.0597 | -44.6976 | 2025-09-18 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c38cd3e1-1fb9-34f1-b266-54471f0619cc | -8.4137 | -45.7583 | 2025-09-18 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e40e42ee-9906-3e5e-8fb9-4a604d51a73a | -7.6386 | -44.4686 | 2025-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d55a8362-b069-323a-9643-9316b46d8ec7 | -3.8658 | -43.1787 | 2025-09-18 14:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| cf807020-ed91-3c4d-9224-a39af4185b05 | -8.9722 | -46.3079 | 2025-09-18 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 6fb46eee-bee9-34ec-9b17-66cf62d1ea74 | -11.4482 | -43.5277 | 2025-09-18 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 739ce9ed-28c3-3b76-ad73-fb486bee57fb | -8.5941 | -46.3919 | 2025-09-18 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 88a149ff-46fa-342e-9071-e6ac3ea456c3 | -5.7867 | -45.9603 | 2025-09-18 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 389b6c41-9f8b-3341-859e-19142c54d305 | -5.786 | -43.9147 | 2025-09-18 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ce8fb129-5e85-3507-93d6-e5effd593778 | -7.5164 | -45.2796 | 2025-09-18 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| d36652d6-4e66-3975-9a58-05189920c733 | -9.1523 | -46.9589 | 2025-09-18 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 805d2cec-8711-371a-8f3d-17cecb70e760 | -7.5601 | -44.7514 | 2025-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4f488b74-914b-35dc-b11c-0b1137290fae | -6.1688 | -41.2357 | 2025-09-18 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 196d0b57-17a6-3ef4-b82b-e01055ca620f | -8.7863 | -46.1029 | 2025-09-18 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 6195c87a-e85b-3794-894a-ca66fb76d4bc | -8.9911 | -46.3059 | 2025-09-18 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 06f8ebe9-f15b-3f49-b1a4-99eaa5a20687 | -19.5869 | -57.7765 | 2025-09-18 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.6 |
| e3da3ff2-1b32-3598-9227-a2fed80d91c4 | -8.6136 | -46.3452 | 2025-09-18 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| b9da6b03-01b2-3ed9-bf1f-d1b44e37f37e | -3.8101 | -43.1116 | 2025-09-18 14:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 8b833ee9-e0b6-35d5-b590-2501922b824b | -6.9212 | -44.764 | 2025-09-18 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 1d341d64-196a-3a90-8c8a-8b531b8b518d | -5.2263 | -43.7006 | 2025-09-18 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 57a6c95b-8f57-3463-be39-f88baf732875 | -17.732 | -46.7756 | 2025-09-18 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 6e318dbf-0e83-3cd2-bec9-e10e4c0cb50a | -5.8622 | -45.8654 | 2025-09-18 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 46a99c71-3cd3-3280-b1bd-99db8b10e256 | -6.0071 | -44.3124 | 2025-09-18 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7f0c4f26-c264-311a-8eac-cbe25d30c8a9 | -6.6319 | -45.56 | 2025-09-18 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4d51a646-02c7-3988-b30f-e04679532550 | -5.806 | -45.8918 | 2025-09-18 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 5de842a0-5eb5-30df-8525-178bcff623ad | -5.6638 | -45.0452 | 2025-09-18 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 56154af0-03bc-3294-b33d-81d8bf3d9578 | -8.3523 | -44.6487 | 2025-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 235.2 |
| eade481c-abac-34f8-9539-52c0f4014e17 | -5.8058 | -45.9142 | 2025-09-18 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2f3c033d-f5e6-316e-a712-b2a6755eb89b | -3.7655 | -44.3383 | 2025-09-18 14:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 215.6 |
| fbea384a-2f62-333b-98ad-13dd08fce89d | -9.1239 | -44.862 | 2025-09-18 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 40b28fc2-d329-3d86-ad70-7b6d0babe42d | -6.9022 | -44.7885 | 2025-09-18 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 7fb19f7e-3979-3d6d-b5ba-9cbbae07181d | -5.2143 | -45.1888 | 2025-09-18 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b64cea71-efc7-31e8-955d-f8227fbe5cff | -19.5872 | -57.7557 | 2025-09-18 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 146.4 |
| 699111d4-4be8-3ae0-b09a-72d97ed8a407 | -7.5415 | -44.7303 | 2025-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| d1f3872c-1644-336f-b40a-f67972446657 | -8.6887 | -46.3599 | 2025-09-18 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 28b29d80-fce9-37e2-8d1f-9a3dec3beb56 | -8.8512 | -45.4631 | 2025-09-18 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3c08157c-4c72-3ab2-b110-ca0f4c18a442 | -8.7076 | -46.3579 | 2025-09-18 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| efa100f7-ccb1-3346-a211-17163403b39a | -6.1196 | -46.3385 | 2025-09-18 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c99029cc-334d-39c1-8f34-7874f64b93a5 | -10.0371 | -47.1952 | 2025-09-18 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| f21b7cce-7286-3180-b468-4147484c8e47 | -8.669 | -46.4291 | 2025-09-18 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| f06b9912-aef1-3fb6-980b-6ee0e2be3792 | -6.2133 | -44.2962 | 2025-09-18 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| f5a9ed1f-e7a4-3608-a875-431973ab6ccd | -5.6233 | -45.41 | 2025-09-18 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 897e52a0-99be-3bec-840d-1da20dd0683e | -6.9024 | -44.7656 | 2025-09-18 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| b1c4da62-e796-3534-8ee7-f65c8e674897 | -3.2691 | -43.0674 | 2025-09-18 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| f23af843-33ea-3930-8c8b-238546a34ad3 | -6.2251 | -45.0264 | 2025-09-18 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 4e3cacb2-b01d-361f-9563-08d5bc87b159 | -5.7862 | -43.8915 | 2025-09-18 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 02d7a2b2-6a19-3cf2-9899-73e2f890acac | -5.7871 | -45.9155 | 2025-09-18 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 61202ff0-5eab-30eb-9025-86e009f0815d | -5.642 | -45.4087 | 2025-09-18 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 375875af-6188-3a94-a1eb-a0a87f3db219 | -6.16 | -46.0007 | 2025-09-18 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 5611046d-6c5f-3b72-92c0-c69032b61f83 | -6.4779 | -45.9991 | 2025-09-18 14:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 990477ff-95f6-3a19-8115-e4301386928c | -3.8659 | -43.1554 | 2025-09-18 14:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 184.5 |
| fa3ce29a-7052-3730-9ba1-733ed1e826aa | -3.2692 | -43.0441 | 2025-09-18 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 26f0aa62-25ba-3da7-a945-91e7bad5fda6 | -19.5672 | -57.7584 | 2025-09-18 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 5abccd06-bde8-34bd-af6c-1a0c904abaec | -3.1562 | -43.2587 | 2025-09-18 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 2ea67094-087e-30b8-8153-41ba3607ea28 | -6.0599 | -44.6747 | 2025-09-18 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| fa4dd1a2-6b38-34a6-a105-d9f65fe28595 | -7.5162 | -45.3024 | 2025-09-18 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 4523ca34-1c44-3047-92e0-d31e56e6cefe | -9.7129 | -47.3867 | 2025-09-18 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 24eee68c-4f45-38a8-adc8-4005f45f0cf5 | -8.3334 | -44.6507 | 2025-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e2339ed2-93f6-3e0c-b68f-ca2b815683c9 | -5.7858 | -43.9378 | 2025-09-18 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 58430b56-2c71-3831-81cf-9eaaccab7592 | -9.0671 | -44.8685 | 2025-09-18 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 30c69baf-9c39-3486-93c6-fbea68e594cf | -8.8054 | -46.0784 | 2025-09-18 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 63d04855-982b-385e-9c12-b55a015f9be2 | -9.1901 | -46.9549 | 2025-09-18 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| bb049e02-6aea-3602-b077-47a1254aa1fd | -6.9978 | -44.62 | 2025-09-18 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| be4409cf-1be4-38d2-aa4a-089748779762 | -8.6885 | -46.3823 | 2025-09-18 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 94064be6-339a-30b3-8996-4d99893b6877 | -3.7654 | -44.3611 | 2025-09-18 14:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7131348f-ce13-3c99-84e5-4d78e5043a40 | -19.5865 | -57.7973 | 2025-09-18 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 8089158e-3b45-395d-b676-c1d0ecbcdc05 | -5.6805 | -43.1556 | 2025-09-18 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 5ebc9335-64fc-3c44-955d-cbf1936d4ddb | -11.467 | -43.5485 | 2025-09-18 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| afd311f6-9e33-3d1b-88e2-3bdd073ea6aa | -8.4645 | -44.7286 | 2025-09-18 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 69f61a5f-3af3-3df0-a257-22ac8fcb2398 | -9.1895 | -46.9994 | 2025-09-18 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 183.7 |


[Clique aqui para ver as próximas entradas](README40.md)
