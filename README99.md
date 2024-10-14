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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f8be28b-ab01-37f2-ad82-e0795f39ed7c | -17.95986 | -57.40775 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.3 |
| bcc69921-80ef-30ab-b7a0-cb6ef190f811 | -17.95779 | -57.39778 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| dd5fda14-b143-38f6-8689-6a02a804ae74 | -17.95697 | -57.4024 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| cbb1c98d-8ff0-3ed9-9bfb-531776cbf948 | -17.95615 | -57.40702 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 07ecfd6a-8b2e-36b5-95d8-c471509faf59 | -17.9549 | -57.39245 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 3bf455c3-8d6c-33bf-8156-47e89e7e154b | -17.95408 | -57.39706 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 9ff73842-e4ca-3a9c-a7e0-e9881f11f068 | -17.95325 | -57.40168 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| e8a8387e-b14e-33fc-a448-2f61c86328fa | -17.95282 | -57.3825 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9d2c6b39-94be-3f6e-9396-230038ae15eb | -17.95201 | -57.38711 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| f93d501c-0361-3964-8eff-b131b7e70aad | -17.95118 | -57.39172 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| f3865dbe-6517-36f8-9958-81627f4b28c5 | -17.95036 | -57.39634 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 3a8fcf24-8c2c-3bbe-8024-0ece453afb7c | -17.94911 | -57.38178 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 42e6821f-9820-38d9-b4bc-320de0313fcf | -17.94829 | -57.38639 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 6b13f509-1775-3d38-8a9a-b58d23313da8 | -17.94747 | -57.391 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 9415f57f-90db-311f-9246-41cccbee9490 | -17.9454 | -57.38105 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 86d82ff5-88d4-3139-911b-2d24b050d49c | -17.20322 | -57.45777 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| df283126-0abd-3b52-9aa2-0336ebb08adb | -17.19986 | -57.47675 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| b5e2d6bc-6231-323e-af2f-9db0d261a444 | -17.19946 | -57.45704 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 70e19436-5b22-37b7-8e86-3bcc187ba5db | -17.19821 | -57.44211 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 6f8efd3e-075e-3a65-8da0-274c26f48d0c | -17.19693 | -57.47128 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 360c0090-e5e5-3d4f-bafd-b379a12255b4 | -17.19653 | -57.45158 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 637e6ae9-3afc-3f58-8393-f8beb7bb810e | -17.19569 | -57.45631 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 63093021-41ac-3db7-af32-f3cbdf63cf15 | -17.19525 | -57.48077 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0cf94b02-7176-35ec-a5e8-5548ded53d79 | -17.19445 | -57.44139 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 3688c6c1-90ab-3fb3-bc4b-7f297e57a642 | -17.19193 | -57.45558 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 48878bc5-630a-3959-b83f-174ffe71ab25 | -17.19153 | -57.43592 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e8995fb1-ee2a-35de-96fa-239c5aa05b5e | -17.19108 | -57.46033 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 96575510-30a1-33a8-9014-55a7ac885ef9 | -17.19069 | -57.44065 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 7379fdad-b139-3aa6-b8b9-f808c751534f | -17.189 | -57.45012 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 44c383cc-d9aa-363d-aa00-bd916bd40e02 | -17.18861 | -57.43047 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 59d42550-2faa-350d-8197-4f41be84869c | -17.18816 | -57.45485 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| a2e9a259-f9ca-31d4-ad6c-47c75a60610a | -17.18777 | -57.4352 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 800c09b5-427e-3613-8955-d01fb18b32a5 | -17.1877 | -57.47931 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1bdb1a5a-a64f-3e74-a229-cdadb8647914 | -17.18732 | -57.45959 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9fd7ec0f-20ff-3ec7-b558-1ae0eb235e63 | -17.18653 | -57.4203 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 022e99d0-4e6d-323f-81a4-dbe2450c182b | -17.18608 | -57.44466 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2a301416-9173-34b8-a232-0998af0bdead | -17.18569 | -57.42501 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ee5e2a41-1662-3f0f-9561-4ab3f77546ee | -17.18524 | -57.44938 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4059ba3a-0c62-3326-8881-d2488e9db718 | -17.18485 | -57.42974 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 784e7795-b34e-33b5-a9cf-fae7efa07146 | -17.18277 | -57.41956 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a4052626-b637-3800-a14e-9db5cab8784b | -17.18109 | -57.42902 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7ba5ffef-62d3-33af-826b-83d3773e2049 | -17.18016 | -57.47785 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 255b81a3-d9c2-30ee-97f7-e7486be29b89 | -17.1747 | -57.48663 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9e044d8f-cdcf-3ff2-928e-6788bf89558a | -17.17385 | -57.49139 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 499cf84e-7721-3f93-a066-27902afaf3c1 | -17.17092 | -57.4859 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fb459b6d-9002-3b4f-84dc-ee473426ea69 | -17.16885 | -57.47565 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f83accc9-fae0-369f-bedf-343ee82ca18b | -17.16508 | -57.47493 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d243704c-bdac-30f4-bc3c-a4bd661a53af | -19.02314 | -57.62168 | 2024-10-14 04:49:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 54d8efad-c7a9-3e63-b3b1-0210cf659a06 | -18.20876 | -56.8438 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 07d6de8b-fd1c-3e79-9136-6be24d0824b8 | -18.20801 | -56.84813 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 6b1e92cb-a241-36fc-9c04-d2424a703cb1 | -18.20515 | -56.84311 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 413dd70f-9cba-3b2e-97fa-fbc195a050dc | -17.86262 | -57.36762 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5adbb951-103c-3b81-b797-ba0ba52784ae | -17.8618 | -57.37224 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5a7b6318-4615-3109-be4d-86e4a3b83bd9 | -17.85809 | -57.37151 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9a99cd70-6214-3719-85a9-88c976a3f5c7 | -17.82631 | -57.31298 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 82edc579-fba4-3acf-95a9-4023a2df5b8d | -17.82549 | -57.31757 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 73f8218f-97e2-37f3-a407-aa41d009bda4 | -17.82467 | -57.32216 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| f386b015-4193-3f9d-b7ca-baf8ba9abe6c | -17.95146 | -57.28265 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 62d59838-df83-3fa6-affd-1c0761cdcb3c | -17.94695 | -57.2865 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ad13ae08-d612-38a6-93b4-0c00a97ff81d | -17.73562 | -56.26824 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| fb887c2b-d2d6-3011-8204-f1cc93c2aff0 | -17.64243 | -56.28666 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 28f6ccb2-7445-3f0c-b126-975f07250586 | -17.64172 | -56.29081 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3604fb8b-fa36-3aa2-80a2-56da7b2c503f | -17.64101 | -56.29496 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8ea5de21-1dae-30a4-9ada-2553234134d5 | -17.6403 | -56.29911 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5cb2dc78-0325-3a79-b774-ffe0d1c41fac | -17.63889 | -56.286 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d640797e-3961-3bfa-8f1f-6d79674a0780 | -17.63818 | -56.29015 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 54a5b7bc-db41-35b2-ba57-d11b45ef32b5 | -17.63747 | -56.2943 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d6aa180f-8414-350f-9946-d032cee85484 | -17.63676 | -56.29845 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cfa0f73b-1f4d-3c48-a4e1-0059e0f0fad4 | -18.02594 | -53.6787 | 2024-10-14 04:49:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d179e632-fa9b-3aac-ab58-f8ef3f0bf057 | -20.95083 | -46.00226 | 2024-10-14 04:49:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6e64dcc-7257-3d06-8d78-78f7f8627775 | -19.0693 | -47.40075 | 2024-10-14 04:49:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4375d7a4-013c-3727-96d6-faf3a50648d4 | -20.32251 | -47.13966 | 2024-10-14 04:49:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 84fcb2f7-cade-3a55-9fb8-0b96a822985d | -20.3185 | -47.13451 | 2024-10-14 04:49:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| feeb85a6-aa35-345f-b15c-077963bb5a79 | -20.31796 | -47.13926 | 2024-10-14 04:49:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2e5ebd73-16c8-31da-a381-f2984f172dc4 | -21.56301 | -48.00878 | 2024-10-14 04:49:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fff943e9-f3a2-3649-a122-03ea9c506079 | -21.56248 | -48.0132 | 2024-10-14 04:49:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0fe379d-a58c-394a-a4d3-91a88cbb437f | -21.56194 | -48.01762 | 2024-10-14 04:49:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a6b7d2d-9295-31b5-ad01-ce38e8009734 | -21.55813 | -48.0126 | 2024-10-14 04:49:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2be6a65-dba7-3dc3-8977-b728cd18e295 | -21.5576 | -48.01701 | 2024-10-14 04:49:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd8f3c78-7aff-396d-b412-8b9198b08be4 | -21.55707 | -48.02142 | 2024-10-14 04:49:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cfdf0b40-058e-3d72-9535-3e9e83162d06 | -21.55653 | -48.02584 | 2024-10-14 04:49:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d5d09ba8-73d0-3bef-af31-c64f53147284 | -17.28682 | -52.0677 | 2024-10-14 04:49:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3df1060e-a141-3de9-89ab-6e0a6443e174 | -22.58894 | -48.56346 | 2024-10-14 04:49:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dfbec2b1-ef4c-375d-a21b-2abb9d9a20fc | -18.5922 | -50.22552 | 2024-10-14 04:49:00 | NPP-375D | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ff9036cb-8199-3bdc-9bf7-530678ffda54 | -18.02261 | -53.67813 | 2024-10-14 04:49:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3fc49a2-603d-3d94-a295-4a951ddfb0a4 | -22.58846 | -48.56755 | 2024-10-14 04:49:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fb3c0cbc-dfc0-3254-ac77-31bb1427743d | -22.58421 | -48.56694 | 2024-10-14 04:49:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 40c452d1-0cd9-3466-9e49-e8f70e125f73 | -21.0481 | -48.61286 | 2024-10-14 04:49:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| df08ce44-05f7-3824-8b1b-3d0fcc909cf2 | -21.0476 | -48.61687 | 2024-10-14 04:49:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 34c7a109-2b7e-3773-b746-2e37ed6489ca | -17.6523 | -56.25005 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1669ce02-54e3-337f-b559-cac8686218e2 | -18.90096 | -51.84575 | 2024-10-14 04:49:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03e12d6c-39de-37e4-85cb-620fb77518fa | -18.90039 | -51.84965 | 2024-10-14 04:49:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79c19338-87c8-370b-9160-b75903c0b091 | -17.6516 | -56.25418 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8fdf9340-6e6d-30f0-b5e2-9b47551ae49d | -17.64807 | -56.25353 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3e4a9383-9d36-33ef-a549-55d6442aef81 | -17.08802 | -55.99479 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 42eb6de4-a2b3-307b-a9e9-731aaa711f90 | -17.08451 | -55.99414 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5e36527c-d94b-31fb-b682-618065b30f77 | -17.0817 | -56.01046 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e0a17dea-c509-3044-ab4a-ab84aa4a63f0 | -17.07818 | -56.0098 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 25de9784-71fb-3e18-a619-f37e8c4e139a | -17.07607 | -56.00099 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f66aa29c-1c1c-3384-918e-0a8c0b242804 | -17.07537 | -56.00507 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |


[Clique aqui para ver as próximas entradas](README100.md)
