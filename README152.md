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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1577bcad-6cb1-3ce9-ad8b-b78cf96bcc73 | -8.5576 | -46.306 | 2025-10-05 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f7d42901-f7ef-354c-8fee-c3ad1fb30d4a | -13.7476 | -51.2883 | 2025-10-05 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| f5e9a161-f94d-3e83-a447-6848dc3634cc | -18.1968 | -53.3638 | 2025-10-05 12:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9a929db1-d1d7-3616-8f73-768f2f00f77a | -12.7106 | -45.8452 | 2025-10-05 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 2e045501-83d1-3359-b85b-5d54a729633d | -8.5384 | -46.3304 | 2025-10-05 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8ee0eeae-6180-3c1d-ad1e-ecf2c46cad42 | -12.5866 | -54.7474 | 2025-10-05 12:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e95cadb1-f8d9-3cc1-b677-309498717dac | -12.2688 | -49.1907 | 2025-10-05 12:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 8bc6e7b0-4419-3a58-a45e-ca2cf7a2ae10 | -10.9303 | -47.0882 | 2025-10-05 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 857f3780-1264-3158-96ac-af117a33503b | -11.0316 | -46.6946 | 2025-10-05 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| c903a80d-96c6-33df-97d3-187cf15673b9 | -15.9829 | -50.905 | 2025-10-05 12:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 9abab948-7c17-3d38-aa76-bc0c2b4f8eae | -12.2684 | -49.2126 | 2025-10-05 12:20:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 4b7a6951-2b93-3589-9259-912dee6075af | -16.0966 | -51.0829 | 2025-10-05 12:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f0c045be-4827-31fa-9236-18cf936144bc | -8.5578 | -46.2836 | 2025-10-05 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 8518b8c1-ed93-3f43-ad10-d1680520eb8c | -13.7284 | -51.2908 | 2025-10-05 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| fe077eed-e372-3ff9-b59a-aece3c7fbdad | -9.9556 | -43.7632 | 2025-10-05 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 70c0f96b-97bf-3bf2-85ee-b4491fdb01e2 | -13.7473 | -51.3097 | 2025-10-05 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 250.5 |
| 71d5e8fc-074f-397c-91e0-ddb02266db76 | -10.8093 | -48.8229 | 2025-10-05 12:20:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2fd07e15-ebee-3c82-95f0-169534e8711e | -8.468 | -45.9332 | 2025-10-05 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 2dadfed3-aae5-3a52-8810-ab4cca81d5b6 | -8.4683 | -45.9106 | 2025-10-05 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 3baa29b7-f5c6-3e3a-a6e6-557e9a38d2d5 | -12.5672 | -54.7698 | 2025-10-05 12:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 704830e5-7dfa-3b13-b024-aa6dded5c7ae | -10.9497 | -47.0634 | 2025-10-05 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| ea261e51-8549-3dd9-bef1-c11526a296ef | -11.0313 | -46.7171 | 2025-10-05 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 980d6cec-c242-3999-9c22-9567e43575fd | -16.077 | -51.0859 | 2025-10-05 12:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 5f10d8d5-b562-3874-9360-339ccc8969a8 | -17.9661 | -51.1474 | 2025-10-05 12:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 132bda2d-ddda-34f5-b6a5-f511381c4f42 | -12.8765 | -47.2712 | 2025-10-05 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ca1c6b44-24c2-34a4-b2ba-b51518d76bd7 | -10.93 | -47.1106 | 2025-10-05 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 1fa40564-5a82-3136-bfc3-f8814a947eef | -10.9501 | -47.041 | 2025-10-05 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 3c1ca100-72d6-35bc-a977-536a71c62eee | -8.539 | -46.2855 | 2025-10-05 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| a4f9cbe1-8a88-3539-9514-6260ba68e8f1 | -11.0126 | -46.6971 | 2025-10-05 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 6f6073a7-c77c-3607-938d-5d976eb88d09 | -8.5581 | -46.2611 | 2025-10-05 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e91bb3c2-1cac-3d96-9ab9-0eccc60922db | -10.4054 | -45.3931 | 2025-10-05 12:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 4b010d4c-9087-3e13-89f1-9723e53e3b17 | -8.5407 | -47.6831 | 2025-10-05 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b9ab7731-8d9f-3f57-9d9f-f79a6116b0dd | -7.7308 | -46.2513 | 2025-10-05 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 81bf495a-627a-325e-8ee4-291c9bc383ab | -8.5578 | -46.2836 | 2025-10-05 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c93b8b2f-0bff-3101-ba4c-27a4d6d44322 | -7.7118 | -46.2754 | 2025-10-05 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| f3fcb7fc-da30-3cf9-92ac-20f0326dfbbf | -8.539 | -46.2855 | 2025-10-05 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 4da2682a-b0d1-3abf-8ad1-03e542a7fe8c | -13.7473 | -51.3097 | 2025-10-05 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 261.1 |
| a0e4ea80-7dab-3030-b7b4-44db80f3cc1c | -11.8225 | -45.0827 | 2025-10-05 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| cf004a31-3a0c-33d9-9c9b-3e10a97e9e65 | -13.7476 | -51.2883 | 2025-10-05 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 073c682a-46a3-3883-a830-34cf068a20ad | -9.3941 | -45.8336 | 2025-10-05 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 027c479f-fa36-3c8d-8c7e-fd0ab681c984 | -7.7123 | -46.2307 | 2025-10-05 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 811aa5d0-daf3-38a6-b68a-91e72b070aae | -8.468 | -45.9332 | 2025-10-05 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 6331c601-fbcc-3eba-b9e9-e14ac0285c36 | -8.1891 | -44.1357 | 2025-10-05 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 5ce72f93-4e35-3c4b-88f1-b238e104a50b | -18.1968 | -53.3638 | 2025-10-05 12:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 4fe1257a-d4d9-3d08-aecb-f2aefaee5526 | -7.712 | -46.2531 | 2025-10-05 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 300.6 |
| cda02006-53c5-3d26-b312-c0c422f7a27b | -9.9556 | -43.7632 | 2025-10-05 12:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 7a94f81b-0c5a-38e9-9ffb-15025254a33d | -16.0966 | -51.0829 | 2025-10-05 12:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 23cd82a7-bb5d-3ec6-ae88-3ef5bf24efb1 | -13.728 | -51.3122 | 2025-10-05 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 8f0e55cb-86bb-379a-8415-a03689f5a364 | -10.93 | -47.1106 | 2025-10-05 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 6e8bb115-6418-36fc-aba4-840d753676c4 | -12.7106 | -45.8452 | 2025-10-05 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e688adbe-8c21-3232-9543-0adf60ddce6d | -17.9605 | -57.5904 | 2025-10-05 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| e20c14d6-1c42-389d-9633-441981580cf4 | -10.8093 | -48.8229 | 2025-10-05 12:30:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 6a90de2e-6a74-3f3d-a4e0-fb575d0e961e | -11.0313 | -46.7171 | 2025-10-05 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 75b6353c-9935-3222-8418-5c6b0a7ef607 | -11.8418 | -45.0799 | 2025-10-05 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 54fe4981-2955-39a6-ab5c-973a3f2c190a | -10.4051 | -45.416 | 2025-10-05 12:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 1d78a264-2018-382b-b457-30cfd346801f | -16.077 | -51.0859 | 2025-10-05 12:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 47d2d984-13d4-39a7-8d22-3095ea919d70 | -11.823 | -45.0596 | 2025-10-05 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| a3f67663-f3a3-31a9-9f0e-43120d5f8a39 | -8.4683 | -45.9106 | 2025-10-05 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| fb801f33-50ec-3c62-8d33-756226be94f8 | -13.7284 | -51.2908 | 2025-10-05 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 5eb068e3-f5fe-3cfa-9b74-119b3bf36e6b | -8.1888 | -44.1588 | 2025-10-05 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| a1ea811f-7c94-393c-9678-75eb0d23ced6 | -8.4872 | -45.9087 | 2025-10-05 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 80ddde8a-683d-3c9c-84aa-40290e36d2d8 | -10.0504 | -50.4113 | 2025-10-05 12:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 97915596-04d9-3c22-a48f-19130bed9cb3 | -15.1886 | -52.8003 | 2025-10-05 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 0402aa55-7eb4-3691-b5fc-a3bbb46e1110 | -18.2569 | -53.3329 | 2025-10-05 12:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ac2de5c5-4a8e-358b-9a0a-6f64342eb547 | -11.0316 | -46.6946 | 2025-10-05 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 50a5268e-0d55-3acb-8cb0-01460c8d6f6a | -19.0155 | -50.6045 | 2025-10-05 12:30:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 194.0 |
| f7b0b231-08a4-3d03-8bb3-909d153a2c39 | -9.2973 | -46.0026 | 2025-10-05 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 838d89b5-c5a7-38b1-9a64-b5e98ee1a95a | -8.5407 | -47.6831 | 2025-10-05 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| c8654ab2-cfb9-3910-be9e-3f829f23c1ad | -8.4872 | -45.9087 | 2025-10-05 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 13a7b7c9-3298-3da2-9b20-4beeefb5f66c | -7.7308 | -46.2513 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 18dda4c4-9adf-37d9-9e61-7a79a69b67fb | -7.8047 | -48.0558 | 2025-10-05 12:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 77e45099-277a-3d18-9f26-d979f0a79212 | -13.7284 | -51.2908 | 2025-10-05 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 1cc0e323-337d-3ab6-a005-b7505dc6cd0c | -7.7118 | -46.2754 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 1d043857-a9f8-3cec-91b6-81cb3bd81317 | -8.468 | -45.9332 | 2025-10-05 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 1263e72e-41de-3737-bac2-62d75c998c34 | -18.1968 | -53.3638 | 2025-10-05 12:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5b693b36-d873-3c2c-9430-b09f070be787 | -11.823 | -45.0596 | 2025-10-05 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 3b47167e-1022-3713-b6b0-ebf824620b84 | -15.5824 | -52.4916 | 2025-10-05 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 330ef8ad-d19a-3114-8809-c60cc14a3bf6 | -9.3941 | -45.8336 | 2025-10-05 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 9f0b4be9-afd3-395c-aadc-c845c227f08b | -10.8093 | -48.8229 | 2025-10-05 12:40:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 44b30d76-4c42-3c48-9aaf-9f65c5a2159e | -11.0978 | -49.8513 | 2025-10-05 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8275dfc4-20ad-33f9-8a94-bfca132cd7cf | -8.4683 | -45.9106 | 2025-10-05 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| aae316a0-5748-3336-a823-f0e3218c0dbc | -10.9501 | -47.041 | 2025-10-05 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| e0cb2e82-0644-3f80-a9c7-6941eb8058bb | -8.5578 | -46.2836 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f73fa867-346d-3335-8882-06979a7a9b44 | -15.582 | -52.5129 | 2025-10-05 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 5a939eec-be1d-30de-b008-d70609d23b1a | -12.7106 | -45.8452 | 2025-10-05 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 08149009-d58b-37e9-948a-834eca77ccb9 | -8.5573 | -46.3285 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f783d5dd-2ffc-37b0-9678-1f2cfe1ec874 | -19.0155 | -50.6045 | 2025-10-05 12:40:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 122.8 |
| fa2358ad-c98c-3ad2-ac80-5089b8bb7d4a | -8.539 | -46.2855 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5c4fda6f-a6d4-3764-8cd6-061f46cb5f4f | -16.077 | -51.0859 | 2025-10-05 12:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 16a75b2d-b3da-35e8-b032-0282e10a0669 | -7.7123 | -46.2307 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| e3343de6-5b00-30d6-bbc7-bdfb286cc461 | -15.6015 | -52.5102 | 2025-10-05 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 8959dfe8-28f2-3da0-b5bf-f47746e2ff54 | -8.595 | -46.3246 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 4557e14e-8498-31f1-a1ae-5181f107e6a0 | -17.9661 | -51.1474 | 2025-10-05 12:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d66e19fe-98cd-3bd5-86d8-06e668d89049 | -17.9605 | -57.5904 | 2025-10-05 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| e07ec0d6-eeeb-3253-a2cb-25aea3f2458f | -8.5953 | -46.3022 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 3263fbae-a331-3131-97ba-d663260b1598 | -10.9494 | -47.0858 | 2025-10-05 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 647379e6-9f47-309f-8988-9cb1396f60b7 | -7.7885 | -44.5228 | 2025-10-05 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 1a8b8b49-1747-36a1-a771-cd8fe6c15a93 | -16.0966 | -51.0829 | 2025-10-05 12:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| cf568eec-b0d9-3793-88d3-94a66df7b080 | -7.712 | -46.2531 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 336.0 |
| 81d53bc9-13c6-3781-be37-4919b9621d7f | -8.5581 | -46.2611 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |


[Clique aqui para ver as próximas entradas](README153.md)
