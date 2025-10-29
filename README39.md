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
| bfcd08dc-6d14-3ed6-9b8e-343331967bb0 | -8.00349 | -46.20583 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 139549d2-1db5-3efc-bd13-0202ae670b6b | -10.28935 | -47.24112 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17aef665-c444-3e23-bc03-3236ea23143d | -7.42504 | -41.86362 | 2025-10-29 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 75d3f756-c113-3b1c-90dc-16b619c9a0d7 | -6.54478 | -46.75939 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2f3684e5-b4ce-397f-a317-977bbc0ad095 | -10.62126 | -47.88083 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0f406b4-6692-3378-817b-401df6269aa7 | -7.80721 | -46.4285 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5b36104-bc51-345f-905a-1d400b391974 | -7.33798 | -42.46906 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5f888747-3a94-36e5-94cb-ffd8fb18eef0 | -6.21593 | -41.82559 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af4f59b0-ebe9-3a9c-89ad-59e18b3f15c5 | -7.80208 | -46.43874 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b5e2f47-3936-3567-8134-cae50c0303bd | -10.62818 | -47.8821 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47914128-0cbd-3d67-ba28-53ece68f4df8 | -9.90708 | -47.65627 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1484fb4-d158-39b0-858c-d970764828bc | -7.59215 | -43.5699 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f004bd77-fdd3-3b8c-92fe-6df37993238d | -6.14526 | -41.56115 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0b3341c6-52d0-396c-9ad7-9e8700de0672 | -6.27541 | -43.75883 | 2025-10-29 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f31b9adf-1d2c-39cc-9955-c9649ef0fa07 | -6.30012 | -41.88684 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 2dd0663b-84b0-358a-bfee-eb422baffc11 | -7.28385 | -44.09957 | 2025-10-29 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71d03534-f3a0-3a33-9ae4-20a20a83fcd7 | -9.1629 | -46.27894 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db6704cf-bdbb-337b-9fa0-569af4ef13a5 | -7.74358 | -44.72826 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29d992a7-c9e1-3498-aa5a-606d134926f1 | -5.61429 | -45.18464 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f454f6bd-9ff4-3790-b528-4034025a8b98 | -7.80779 | -46.4249 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 325dee9f-dcaf-3efa-9f71-b5c7488f9863 | -6.47301 | -42.23746 | 2025-10-29 04:23:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bb0a7da3-c576-3054-8e6e-bc5ab10e8c87 | -8.69233 | -47.13829 | 2025-10-29 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a28e4115-92e3-3fa9-ba4a-b16d87616ab7 | -9.93942 | -47.09354 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ace460f-1ea3-34ef-bd1e-a17b97bd8a3c | -7.80032 | -46.44962 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d43c42b6-9414-3dd1-890a-5381b734520f | -9.807 | -47.60489 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f051b764-ae50-3e14-92ab-3e044f640735 | -7.05522 | -44.80781 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6044b08-a9be-3efe-bb2e-11c6d5937208 | -5.07298 | -47.10852 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc88264b-5911-3e09-aa13-4a2c323dca1a | -7.43804 | -45.12515 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc2ba2fd-9ad5-38e6-979a-58225dce65ee | -7.63962 | -46.9255 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6fbc6b0-1ba6-3f1a-96d4-80aa31610e58 | -8.54875 | -45.69183 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b92b28f-5c28-366f-b140-c014ea52ba23 | -6.14055 | -41.68714 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9ef6170b-6c91-35e1-ae0c-36b4c3e9035a | -8.02756 | -47.40005 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3041267-1dc5-3406-9e49-9a10697d6c50 | -9.88459 | -47.45458 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9bc3305b-9649-3e78-8d8c-26d8349d3550 | -6.88642 | -45.04106 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d25d11c5-b6f0-34db-87ae-5a4652c5398d | -8.17628 | -45.71566 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4564c97b-0ce9-34b2-acb8-cb034972f712 | -7.8767 | -48.41519 | 2025-10-29 04:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b80e67a-1574-360e-8f63-19be8c48d8c0 | -7.35943 | -47.62429 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c80ae36-0ce6-3926-b46c-68eb829371a0 | -8.09464 | -45.94786 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b547ee4b-43d6-32b6-b613-40d3a644d352 | -9.03298 | -47.72549 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93a40aea-0786-3400-a7ec-2f7564f47922 | -7.26992 | -46.90474 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04265f71-41d3-3be1-b60b-1d3e7013cc22 | -10.95827 | -47.61679 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e05b3ca7-dc28-3eb4-b88e-ff408988a7e0 | -8.64033 | -44.77299 | 2025-10-29 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8758fbcd-5493-32fa-beff-f25f4ba29e19 | -9.8954 | -44.89917 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12f90131-d6d7-3e04-bbe0-01b0818bea34 | -7.75132 | -44.72234 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c3bafad-af20-333c-a7e1-ec15521cea19 | -7.78163 | -46.4578 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c71c880-315f-3eb2-8d96-79ce03cbe520 | -9.22605 | -46.34729 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 904ef63d-2c49-3358-b13e-a64aded08cad | -7.06405 | -44.47071 | 2025-10-29 04:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4abf2da-cd00-3b79-8c02-693cde419b2a | -7.13534 | -47.36193 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a0bd451-9700-3885-8878-2c568b9ca4b5 | -7.98833 | -45.53492 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ee0633e-5711-3e05-89ea-08f8df8ba2a1 | -6.56479 | -41.59375 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d901a9c4-4ec3-37ae-880a-454b67126562 | -10.94376 | -47.62277 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d3a4a8e-a497-3952-aff3-45817e304a4c | -10.85104 | -47.88707 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df1a51fd-0162-33de-8864-8354a3e51170 | -5.79563 | -50.16591 | 2025-10-29 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69426309-00cd-3b16-80a2-cd9a9a8f17f0 | -10.4504 | -44.48676 | 2025-10-29 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6442e0ab-eb18-3815-b413-ca8f99154a84 | -7.25772 | -49.94927 | 2025-10-29 04:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc027812-4fcc-3396-987a-b5ff2ae75af8 | -10.76619 | -47.89735 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7f6a58c-f47a-3abd-826a-e31543533efc | -7.08428 | -44.94414 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62d36246-333a-35df-bffd-0f91fa819732 | -10.94082 | -47.80752 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fff0ea7-610e-3721-9ad6-425f12fd1920 | -6.12471 | -41.84883 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 63034279-10d5-3dd4-9b58-397f4de9e5b5 | -10.89729 | -48.37314 | 2025-10-29 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41dad676-c593-3542-92c4-122c0d680af0 | -10.76505 | -44.7381 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0a04b61-9eb6-3868-8996-9902c6a0dad9 | -6.14353 | -41.69165 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b88336ea-6e98-38e3-b596-55fc85fff42d | -10.56953 | -49.83738 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 41ece056-58cb-34b1-bda9-275906991773 | -7.35754 | -47.63594 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 96819ab8-fc04-3e65-bd99-12824c3c34a0 | -6.30199 | -41.87472 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a9eb81cd-820b-3d53-9bf2-851608f0cfd0 | -9.75317 | -45.00658 | 2025-10-29 04:23:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f7b5cd6-afc9-3b1d-9977-30146243b682 | -9.44247 | -46.90731 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fdde7e2-d35d-32a7-872f-c28a10798a52 | -10.56489 | -49.84143 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 71fb9966-dd9c-3f34-8e08-3e5673a2d5ec | -7.60231 | -43.57151 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8cbc619-3e65-3fe7-b3ee-ce0fc6d888d5 | -10.66386 | -44.80259 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 845c693a-fb02-3f52-9b5a-9f2f194f947b | -9.2294 | -46.34787 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4200ddf5-8768-3be7-8996-485635016aa7 | -8.188 | -46.94748 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18065ba9-69f9-30a1-aa4b-fcae4aacf6f2 | -10.52914 | -47.74075 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd79bb91-379a-3c28-a98f-257c64fe9e94 | -8.83332 | -46.93615 | 2025-10-29 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8e6f189-1d55-3936-b93a-36115d700dc9 | -10.92164 | -47.60728 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a454d72e-2edf-3476-aeba-c9b17a65c08d | -9.89928 | -44.89619 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25c2fbdb-90cb-3bec-b578-58aa8e84466f | -10.51595 | -47.73472 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3fdf1cd-dee9-3253-b131-7f25ff04fd03 | -6.46376 | -43.55519 | 2025-10-29 04:23:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14b99b93-a712-3aa9-b864-e31265e3cb4e | -10.69302 | -44.36129 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f103976-d2fc-3a48-816b-60ca31581364 | -7.01869 | -48.65346 | 2025-10-29 04:23:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a0154f3-2398-3ea0-993d-d63180fa13b0 | -8.54021 | -45.68724 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0c1a5e6-2636-3d45-941c-8499327b2397 | -6.17046 | -41.51801 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8aee0f3e-2d4d-3d3a-996a-be8176e3861b | -5.61256 | -47.11458 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f408b557-4ae1-328c-bb6d-95306702be6b | -6.14062 | -41.69397 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1c36bda9-4b83-3425-abe8-f5e32791baa4 | -5.43231 | -46.12246 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 834b9a35-7a9d-3985-9c45-48bfda6523f1 | -7.70782 | -46.90955 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75b467ca-594a-3fe1-bee5-b191d628793e | -10.41077 | -47.09851 | 2025-10-29 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24f614a2-2f13-3184-97d7-10595d63eaed | -5.64483 | -42.80789 | 2025-10-29 04:23:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4361bee6-34a6-3419-9a86-f5effef0b313 | -10.90016 | -48.37775 | 2025-10-29 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 995752e0-2c90-3ef8-8d29-dae215789c55 | -11.1406 | -44.93916 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| caf29164-4463-3386-a637-b49b27dcf019 | -9.89093 | -44.884 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0f063ea-44e1-3172-a616-e397ce67e2e3 | -7.59516 | -45.85675 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b78a1f02-13ea-3f42-8e30-9c38227f0a49 | -6.73444 | -39.04164 | 2025-10-29 04:23:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 27934172-70b0-3193-8d79-4ce6f29e8c5e | -6.11462 | -42.43332 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 00fed56d-75a2-3842-bcc6-9304865df39d | -10.65342 | -47.90183 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49d803ab-806a-3a5a-811c-87b68100d46b | -7.90132 | -49.17863 | 2025-10-29 04:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1dc2a4ee-f9d6-3ae0-a5cc-4d32814bf786 | -10.51033 | -47.72588 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a513af5-d3fa-3853-9c38-eba06972373a | -7.79737 | -46.46778 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e012d43-427a-30f2-b7c5-b9cc2973ec43 | -8.02854 | -47.41604 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22f681ef-9ccb-37b2-8f8b-8a07a27c4540 | -5.78849 | -47.72072 | 2025-10-29 04:23:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README40.md)
